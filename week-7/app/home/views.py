from sqlite3 import Cursor
from flask import render_template

from flask import request

from . import home

@home.route("/", methods = ["GET"])
def index():
    return render_template("index.html")
