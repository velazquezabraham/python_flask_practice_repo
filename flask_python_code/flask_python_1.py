#Programmer: Abraham V.
#Project: flask_python_1.py
#Description: 
#       This project will have an intro to using Flask, flask is a micro 
#       framework to set up websites (from my understanding) tutorial 1
#       working with templates tutorial 2


#import flask tools
#added render_template to render html files and render them as our web pages
from flask import Flask, redirect, url_for, render_template

#create an app
app = Flask(__name__) #__name__ is a key word

@app.route("/")
def home():
    return "Hello! This is the main page <h1>Hello</h1>"

#run the app
if __name__ == "__main__":
    app.run()

