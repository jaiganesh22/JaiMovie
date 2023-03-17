from flask import Blueprint
from flask import Flask, render_template, url_for, session, request, redirect, flash, jsonify
from .user_database import User_db
view = Blueprint("views", __name__)

USER_NAME = 'name'

@view.route("/", methods=["GET"])
@view.route("/home/", methods=["GET"])
def load_home():
    if USER_NAME not in session:
        session[USER_NAME] = 'Guest'
    return render_template("home.html", **{'session': session})

@view.route("/register", methods=["GET", "POST"])
def load_register():
    if request.method == "GET":
        return render_template("register.html")
    
    else:
        name = request.form["name"]
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        user_db = User_db()
        found_user = user_db.check_user(username)
        if(found_user):
            flash(f"User {username} already exists.")
            return render_template("register.html")
        else:
            flash(f"User {username} registered successfully.")
            user_db.register_user(name, username, email, password, "Basic")
            return redirect(url_for("views.load_home"))
        
@view.route("/signin/", methods=["POST", "GET"])
def load_signin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_db = User_db()
        found_user = user_db.check_user(username)
        if(found_user):
            user = user_db.get_user(username)
            if(password == user["password"]):
                session[USER_NAME] = username
                flash(f"Welcome back {username}!")
                return redirect(url_for("views.load_home"))
            else:
                flash("Invalid username or password")
                return render_template("signin.html")
        else:
            flash(f"User {username} not registered")
            return redirect(url_for("views.load_register"))
        
    else:
        return render_template("signin.html")
    
@view.route("/signout", methods=["GET"])
def load_signout():
    if USER_NAME in session:
        flash(f"{session[USER_NAME]} signed out sucessfully.")
        session.pop(USER_NAME, None)
    else:
        flash("Login first to Logout")
    return redirect(url_for("views.load_home"))
        
        
                
        

