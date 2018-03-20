from flask import Flask, render_template, os

turtle = new Flask(__name__)

turtle.secret_key = os.urandom(32)

@turtle.route("/")
def root():
    return hi


if __name__ == "__main__":
    turtle.run(debug=True)
