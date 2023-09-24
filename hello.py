from flask import Flask, render_template
from flask_bootstrap import Bootstrap 
from flask_moment import Moment
from datetime import datetime 

app = Flask(__name__)
#application instance created as an object of Flask library
bootstrap = Bootstrap(app)  #initialization of bootstrap object from flask_bootstrap library
moment = Moment(app) 



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')  #route decorator
def index():     #view function index
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')                                                          #dynamic route decorator
def user(name):                                                                     #view function for name specified in url 
    return render_template('user.html', name=name, current_time=datetime.utcnow())  #Jinja2 renders user.html template to get information on client's name
                                                                                    #first argument of render_template() is the filename of template, all succeeding arguments are values for variables referenced in template


