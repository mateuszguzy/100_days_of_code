from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

db.create_all()

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = request.form
        new_entry = Book(title=data['title'], author=data['author'], rating=data['rating'])
        db.session.add(new_entry)
        db.session.commit()
        return redirect('/')
    return render_template('add.html')

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    book_to_update = Book.query.get(id)
    if request.method == "POST":
        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit.html', book=book_to_update)

@app.route('/delete/<int:id>')
def delete(id):
    book_to_delete = Book.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

