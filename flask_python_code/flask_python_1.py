#Programmer: Abraham V.
#Project: flask_python_1.py
#Description: 
#       This project will have an intro to using Flask, flask is a micro 
#       framework to set up websites (from my understanding) tutorial 1
#       working with templates tutorial 2


#import flask tools
#added render_template to render html files and render them as our web pages
#imported session
#impirted timedelta to set how long we want our session to last for
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

#create an app
#__name__ is a key word
app = Flask(__name__)
app.secret_key = "HI"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3' #users is name of the table we'll be referencing                                       
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #to stop showing warning signs on every mod
app.permenent_session_lifetime = timedelta(minutes=5)

#create database
db = SQLAlchemy(app) #creating a model now

#rows pieces of information, columns are objects....we only want name and email to store
class users(db.Model):
    _id = db.Column("id",db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


#create secret key to encrypt and decrypt data saved in server

#We use get request by default 
@app.route("/")
def home():
        return render_template("index.html")

#we want to know the functions we can use with get and post
#How did we reached this page; POST or GET? use the request method to find out
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST": #make sure you use capitals
        session.permenent = True #default is false
        user = request.form["nm"]#use the same variable name from the html login to use the same value. This only works with request POST
        session["user"] = user #STORE DATA  set up some data for our session as a dictionary
        flash(f"You have successfully logged in, {user}")
        return redirect(url_for("user"))#No need to pass the user value
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))

        return render_template("login.html")

 #RETRIEVE DATA Before referencing to the session dictionary key, Check that the user 
 #logged in, and No need for a parameter.
@app.route("/user/", methods=["POST","GET"]) 
def user():
    email = None
    if "user" in session:      
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email=email)#passing email to front-end
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))


@app.route("/logout/")
def logout():
    flash("You have been logged out", "info") #Message and category
    session.pop("user", None) #remove data from session
    session.pop("email", None)
    return redirect(url_for("login"))

#run the app
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

    #Sessions- pass information from our back end to from end, temporary for some time we could set,
    #stored on web server, 
    #there for quick access of info between all of the different pages of website. Load in, use
    #it while user in website, deasapears when they leave.
    #import session
    #create secret key app.secret_key = "whatever"
    #store data in login
    #reference data in user, redirect if key session empty,
    #use permenent session - set up defining how long you want to stay logged in.