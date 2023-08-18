from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

"""
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
"""

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


class AddBlogPostForm(FlaskForm):
    title = StringField("Blog Post Title")
    subtitle = StringField("Subtitle")
    author = StringField("Your name")
    img_url = StringField("Blog Image URL")
    body = CKEditorField("Blog Content")
    submit = SubmitField("Submit Post")


with app.app_context():
    db.create_all()


@app.route("/")
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    try:
        requested_post = db.get_or_404(BlogPost, post_id)
        return render_template("post.html", post=requested_post)
    except:
        return "Error, nothing found"


# TODO: add_new_post() to create a new blog post
@app.route("/add", methods=["GET", "POST"])
def add_new_post():
    form = AddBlogPostForm()
    if form.validate_on_submit():
        all_items = {
            item: value.data
            for (item, value) in form._fields.items()
            if item not in ["submit", "csrf_token"]
        }
        current_date = date.today()
        new_post = BlogPost(date=current_date, **all_items)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form)


# TODO: edit_post() to change an existing blog post

# TODO: delete_post() to remove a blog post from the database

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
