import os

# from cs50 import SQL
import sqlite3

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
# import plotly.express as px
from helpers import apology, login_required
# from pyquery import PyQuery as pq

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = sqlite3.connect("project.db") #SQL("sqlite:///project.db")

@app.route("/")
# @login_required
def index():
    # user_id = session["user_id"]
    return render_template("index.html")

@app.route("/mod",methods=["GET"])
# @login_required
def mod():
    return render_template("mod.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
# @login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    # """Register user"""
    if request.method == "GET":
        return (render_template("register.html"))
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not username:
            return (apology("You must give Username"))
        if not password:
            return (apology("You must give Password"))
        if not confirmation:
            return (apology("You must give Confirmation"))
        if password != confirmation:
            return (apology("Passwords do not match"))
        hash = generate_password_hash(password)
        try:
            # sql = "INSERT INTO users (username, hash) VALUES (?, ?)"
            # val = (username, hash)
            new_user = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
        except:
            return apology("Username already exists")

        session["user_id"] = new_user

    return redirect("/")


@app.route("/change_password", methods=["POST", "GET"])
# @login_required
def change_password():
    """Change Password"""
    if request.method == "GET":
        return render_template("changepwd.html")
    else:
        new_password = request.form.get("new_password")
        old_password = request.form.get("old_password")

        # Ensure username exists and password is correct
        user_id = session["user_id"]
        username = db.execute("SELECT username  FROM users WHERE id = ?", user_id)
        print(username)
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], old_password):
            return apology("invalid password", 403)

        """Update Password"""
        # username  = session["username"]
        db.execute("UPDATE users (username, hash) VALUES (?, ?)", username, hash)

        return redirect("/")
