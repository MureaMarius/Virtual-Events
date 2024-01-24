from flask import *


def home_page():
    return render_template("home.html")
