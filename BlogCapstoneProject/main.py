from flask import Flask, render_template
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/post/<int:id>')
def post(id):
    print(posts[id-1])
    return render_template("post.html", post=posts[id-1])


if __name__ == "__main__":
    app.run(debug=True)
