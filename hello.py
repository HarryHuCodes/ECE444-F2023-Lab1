from flask import Flask
app = Flask(__name__)
#application instance created as an object of Flask library

@app.route('/')  #route decorator
def index():     #view function index
    return '<h1>Hello World</h1>'
