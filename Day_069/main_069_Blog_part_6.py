from flask import Flask, render_template, redirect, url_for, flash, abort, request
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from forms import CreatePostForm, CreateCommentForm, RegisterUser, LoginUser
from functools import wraps
from flask_gravatar import Gravatar

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shbfdhsbfjbshJABSDBASJDhasd'
ckeditor = CKEditor(app)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
# default user avatar API
gravatar = Gravatar(app,
                    size=200,
                    rating='r',
                    default='robohash',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CONFIGURE TABLES
# USERS DB
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="user")


# POSTS DB
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author = relationship("User", back_populates="posts")
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    comments = relationship("Comment", back_populates="post")


# COMMENTS DB
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    text = db.Column(db.String(250), nullable=False)
    user = relationship("User", back_populates="comments")
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    post = relationship("BlogPost", back_populates="comments")


# only first run, to create the DB
# db.create_all()


# custom decorator that only allows admin to access certain views
def admin_only(func):
    @wraps(func)
    def wrapped_view(*args, **kwargs):
        user_id = int(current_user.get_id())
        if user_id != 1:
            return abort(403)
        return func(*args, **kwargs)
    return wrapped_view


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    try:
        user_id = int(current_user.get_id())
        return render_template("index.html", all_posts=posts, id=user_id)
    except TypeError:
        return render_template("index.html", all_posts=posts)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterUser()
    if form.validate_on_submit():
        # create new user record with hashed password
        new_user = User()
        new_user.email = form.email.data,
        new_user.name = form.name.data,
        new_user.password = generate_password_hash(password=form.password.data, method="pbkdf2:sha256", salt_length=8)
        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect("/")
        except exc.IntegrityError:
            flash("Given email is already registered! Please log in.")
            return redirect("/login")
    else:
        return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginUser()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(pwhash=user.password, password=form.password.data):
            login_user(user)
            return redirect("/")
        else:
            flash("Email or password incorrect!")
    return render_template("login.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(user_id)
    if user:
        return user
    else:
        return None


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    form = CreateCommentForm()
    user_id = current_user.get_id()
    post = BlogPost.query.get(post_id)
    comments = post.comments
    # when user submits a comment and is logged in add comment to DB
    if form.validate_on_submit() and user_id is not None:
        comment = Comment(
                text=form.text.data,
                user_id=user_id,
                post_id=post_id,
            )
        db.session.add(comment)
        db.session.commit()
    # if user is not logged and,
    if user_id is None:
        # views the page, show everything including comment text field
        if request.method == "GET":
            return render_template("post.html", post=requested_post, comment_form=form, comments=comments,
                                   gravatar=gravatar)
        # if user is not logged in, redirect to login page
        else:
            flash("Login or register first!")
            return redirect("/login")
    # if user, doesn't submit comment and is logged in, show page normally
    else:
        return render_template("post.html", post=requested_post, id=int(user_id), comment_form=form, comments=comments,
                               gravatar=gravatar)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(debug=True)