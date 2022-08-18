from crypt import methods
from flask import Flask, render_template, request, redirect
# https://stackoverflow.com/questions/27539309/how-do-i-create-a-link-to-another-html-page

app = Flask(__name__)

@app.route("/")
def mainPage():
    return """
        <strong>Hello World! 🥺</strong>
        <br/>
        <p>this is my website</p>
    """

@app.route("/fun")
def fun():
    return "this is funn"

@app.route("/goodbye")
def goodbye():
    return render_template("main.html",name="Abi")

@app.route("/id")
def myid():
    
    # nah, form in main.html
    # trying to get post request working :(
    return render_template("myid.html")
    
@app.route("/name/<name>")
def dynamic_url(name):
    return """
    <html>
        <body>
            <p>hello my name is {} </p>
        <body>
    </html>
    """.format(name)

#! pretty cool 😍 👍
# default error function 
@app.errorhandler(404)
def not_found():
    return "!!404, Page not found. Try again nerd >:("