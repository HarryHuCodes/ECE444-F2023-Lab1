from flask import Flask
app = Flask(__name__)
#application instance created as an object of Flask library

@app.route('/')  #route decorator
def index():     #view function index
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')                          #dynamic route decorator
def user(name):                                     #view function for name specified in url 
    return '<h1>Hello, {}!</h1>'.format(name)       #personalized greeting - dynamic part enclosed in {}


