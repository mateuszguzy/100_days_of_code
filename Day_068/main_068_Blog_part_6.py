import flask_login
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
login_manager = LoginManager()

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager.init_app(app)
login_manager.login_view = 'login'
db = SQLAlchemy(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
db.create_all()


# CREATE USER
class CreateUser(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["name"]
        # hashing and salting user password
        password = generate_password_hash(password=request.form["password"], method='pbkdf2:sha256', salt_length=8)
        new_user = User()
        new_user.email = email
        new_user.password = password
        new_user.name = name
        # try to add new user to DB, in case that exact record exists,
        # redirect to login page with info for user
        try:
            db.session.add(new_user)
            db.session.commit()
        except exc.IntegrityError:
            flash("Email already registered.")
            return redirect("/login")
        return redirect(url_for("secrets", name=name))
    return render_template("register.html")


@app.route('/secrets/<name>')
@flask_login.login_required
def secrets(name):
    return render_template("secrets.html", name=name)


@login_manager.user_loader
def load_user(user_id):
    if User.query.get(user_id):
        user = User.query.get(user_id)
        return user
    else:
        return None


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # search for user in DB
        user = User.query.filter_by(email=request.form["email"]).first()
        # if user exists and user's password is correct, redirect to "secrets" page
        if user and check_password_hash(user.password, request.form["password"]):
            username = user.name
            login_user(user)
            flash("Logged in successfully.")
            return redirect(f"/secrets/{username}")
        else:
            flash("Invalid login or password.")
    return render_template("login.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect("/")


@app.route('/downloads')
@login_required
def download():
    return send_from_directory(directory='static/files', path="cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
