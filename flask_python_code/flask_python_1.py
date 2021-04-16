#Programmer: Abraham V.
#Project: flask_python_1.py
#Description: 
#       This project will have an intro to using Flask, flask is a micro 
#       framework to set up websites (from my understanding)

#import flask tools
from flask import Flask, redirect, url_for

#create an app
app = Flask(__name__)

#give flask a route to access this page
@app.route("/")

#create the pages that are going to be in the website
#this will return an inline HTML
def home():
    return "Hello this is the home function <h1>Hello</h1>"

#creating another page aka function
#first we need to give it a route
@app.route("/<name>")
def user(name):
    return f"Hi this is the user function {names}!"

#creating another page aka function for admin only.
#if not an admin, the we will REDERECT to a different page
#first I will route it
#Then, we use the redirect function and give it the argument
#with the url_for of the home page aka the name of the function
#we want them to go
@app.route("/admin/") #add another slash after admin to know go there when added in url
def admin():
    return redirect(url_for("home", name = "Admin!"))



#run app and start a website
if __name__ == "__main__":
    app.run()

