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
from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta


#create an app
#__name__ is a key word
app = Flask(__name__)
app.secret_key = "HI" 
app.permenent_session_lifetime = timedelta(days=5)

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
        return redirect(url_for("user"))#No need to pass the user value
    else:
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login.html")

 #RETRIEVE DATA Before referencing to the session dictionary key, Check that the user 
 #logged in, and No need for a parameter.
@app.route("/user/") 
def user():
    if "user" in session:      
        user = session["user"]
        return f"<h1>in user function {user}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None) #remove data from session
    return redirect(url_for("login"))

#run the app
if __name__ == "__main__":
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