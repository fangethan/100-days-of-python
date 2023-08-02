from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route("/")
def home():
    return (
        '<h1>Guess a number between 0 and 9" and display a gif of your choice from giphy.com.</h1>'
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></img>'
    )


@app.route("/url/<int: number>")
def guess_number(number):
    if number > random_number:
        return (
            '<h1 style="color: red">Too high!</h1>'
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.g"></img>'
        )
    if number < random_number:
        return (
            '<h1 style="color: red">Too low!</h1>'
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"></img>'
        )

    return (
        '<h1 style="color: green">You found me!</h1>'
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"></img>'
    )


if __name__ == "__main__":
    app.run(debug=True)
