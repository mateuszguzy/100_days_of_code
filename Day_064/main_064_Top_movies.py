from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import os
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top_10_movies_data.db'
db = SQLAlchemy(app)
API_KEY = os.environ.get("THE_MOVIE_DB_API")

# edit movie details form definition
class EditRating(FlaskForm):
    rating = FloatField(label="Rating (out of 10)")
    review = StringField(label="Review")
    submit = SubmitField(label="Save")

# add movie form definition
class AddMovie(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add")

# DB table creation
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(4), nullable=False)
    description = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), unique=True, nullable=False)

db.create_all()


@app.route("/")
def home():
    # sort movies by user rating to create flexbile rating
    movies_in_order = Movie.query.order_by("rating")
    # count how many movies there are in DB to create ranking
    rank = Movie.query.count()
    # depending on rating value movies are sorted worst-best, and assigned respective rank
    for movie in movies_in_order:
        movie_to_change = Movie.query.get(movie.id)
        movie_to_change.ranking = rank
        rank -= 1
    db.session.commit()
    return render_template("index.html", movies=movies_in_order)


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    # extract movie data form DB by ID, passed from HTML
    movie_to_edit = Movie.query.get(movie_id)
    # create form for movie details edition
    form = EditRating()
    # when form is submitted update DB and return to main page
    if form.validate_on_submit():
        # extract new data from form, and assign them to values passed into the DB, then return to main page
        new_rating = request.form["rating"]
        new_review = request.form["review"]
        movie_to_edit.rating = new_rating
        movie_to_edit.review = new_review
        db.session.commit()
        return redirect('/')
    return render_template("edit.html", movie=movie_to_edit, form=form)


@app.route('/delete/<int:movie_id>')
def delete(movie_id):
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect('/')


@app.route('/add', methods=["GET", "POST"])
def add():
    # create form for adding a new movie
    form = AddMovie()
    # if route gets "GET" response, send request to Movie DB API for list of movies containing searched phrase
    if form.validate_on_submit():
        movie_title = request.form["title"]
        response = requests.get(url=f"https://api.themoviedb.org/3/search/movie?"
                                f"api_key={API_KEY}&"
                                f"language=en-US&"
                                f"query={movie_title}"
                                )
        data = response.json()['results']
        # render select page, where every result is a hyperlink adding given result into DB
        return render_template('select.html', data=data)
    return render_template('add.html', form=form)


@app.route('/movie_info/<int:movie_id>')
def get_movie_info(movie_id):
    # after choosing movie on "add" route, there are downloaded additional information about the movie from Movie DB
    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id}?"
                                f"api_key={API_KEY}&"
                                f"language=en-US")
    data = response.json()
    # those data are passed into the DB, without "rating", "ranking" and "review"
    # those arguments are filled by the user, because function redirects to the movie edit page directly
    new_movie = Movie(
        title=data["title"],
        year=data["release_date"].split("-")[0],
        description=data["overview"],
        rating=None,
        ranking=None,
        review="None",
        img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
    )
    db.session.add(new_movie)
    db.session.commit()
    movie_id = Movie.query.filter_by(title=f'{data["title"]}').first().id
    return redirect(f'/edit/{movie_id}')


if __name__ == '__main__':
    app.run(debug=True)
