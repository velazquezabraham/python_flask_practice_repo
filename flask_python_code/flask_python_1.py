#Programmer: Abraham V.
#Project: flask_python_1.py
#Description: 
#       This project will have an intro to using Flask, flask is a micro 
#       framework to set up websites (from my understanding) tutorial 1
#       working with templates tutorial 2


#import flask tools
#added render_template to render html files and render them as our web pages
from flask import Flask, redirect, url_for, render_template, request

#create an app
#__name__ is a key word
app = Flask(__name__)

#We use get request by default 
@app.route("/")
def home():
        return render_template("index.html")

#we want to know the functions we can use with get and post
#How did we reached this page; POST or GET? use the request method to find out
@app.route("/login", methods=["POST", "GET"])
def logic():
    if request.method == "POST": #make sure you use capitals
        user == request.form["nm"]#use the same variable name from the html login to use the same value. This only works with request POST
        return redirect(url_for("user", usr=user))#passig the user value to the user func
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>in user function {usr}</h1>"

#run the app
if __name__ == "__main__":
    app.run(debug=True)