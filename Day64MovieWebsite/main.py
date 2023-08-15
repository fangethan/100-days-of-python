from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

"""
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""
db = SQLAlchemy()
app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    image_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    all_movies = result.scalars()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_movie = Movie(
            title="Phone Booth",
            year=2002,
            description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
            rating=7.3,
            ranking=10,
            review="My favourite character was the caller.",
            image_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg",
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie_selected = db.get_or_404(Movie, movie_id)

    if form.validate_on_submit():
        movie_selected.rating = float(form.rating.data)
        movie_selected.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", movie=movie_selected, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_be_deleted = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_be_deleted)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
