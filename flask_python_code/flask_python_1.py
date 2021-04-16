#Programmer: Abraham V.
#Project: flask_python_1.py
#Description: 
#       This project will have an intro to using Flask, flask is a micro 
#       framework to set up websites (from my understanding) tutorial 1
#       working with templates tutorial 2




#import flask tools
from flask import Flask, redirect, url_for

#create an app
app = Flask(__name__) #__name__ is a key word

@app.route("/")
def home():
    return "Hello! This is the main page <h1>Hello<h1>"

#route will pass a variable to user()
#user() wi;; return an f string only available ion python3
@app.route("/<name>")
def user(name): 
    return f"Hello {name}!" 

#admin() will send the user to another website aka 'user' using the redirect
#function- the redirect function takes as input the name of the website to be
#re-directed to.
#The user function takes an argument called 'name', therefor we need to make 
#sure we pass an argument named 'name' and its value will be  "Admin"
@app.route("/admin/")#added slash at the end to work with slash or no slash
def admin():
    return redirect(url_for("user", name = "Admin"))

#run the app
if __name__ == "__main__":
    app.run()

