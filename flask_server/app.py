# url_shortner/ flask_url/ app.py

 
import urllib.request, json

from flask import Flask, session, render_template, request, redirect,jsonify
from flask_session import Session
from helper import login_required, apology
from werkzeug.security import check_password_hash, generate_password_hash
from api_helper import shorten_url
import api_helper
# Configure APP
app = Flask(__name__)

# Ensure templates are auto reloaded after
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///url_front.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def shorten():
    if request.method == "GET":
        return render_template("index.html")
    else:
        return render_template("shortened.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Register user"""
    username = request.form.get("username")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")
    hash = generate_password_hash("password")

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("apology.html", message="must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("apology.html", message="must provide password")

        # Ensure  password is matching
        elif password != confirmation:
            return render_template("apology.html", message="passwords not matching ")

        # Query database if username exists
        rows = db.execute("SELECT * from users where username = ?", username)

        if len(rows) != 0:
            return render_template("apology.html", message="user name not available")

        # insert new user
        db.execute(
            "INSERT INTO users (username, hash) VALUES (?,?)", username, hash)

        return redirect("/")

    else:
        return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in """

    # forget any user_id
    session.clear()

    # if user reached route via post by submitting the form
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("apology.html", message="must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("apology.html", message="must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return render_template("index.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/history")
def my_urls():
    """ show historical  urls of user """
    user_id = session["user_id"]
        
    return render_template("/history.html", message=" #TO DO - Work In Progress")

@app.route("/url",methods=["GET", "POST"])
def url():
    
    if request.method == "POST":
        
        """ Get target url """
        target_url = request.form.get("target_url")
         
        """ Access API from  helper script 
        """
        payload = api_helper.shorten_url(target_url)   
        
        
        return render_template("shortened.html",database = payload)
    else:
        return redirect("/")