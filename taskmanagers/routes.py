from flask import render_template
from taskmanagers import app, db
from taskmanagers.models import Category, Task


@app.route("/")
def home():
    return render_template("base.html")
