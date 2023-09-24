from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap 
from flask_moment import Moment
from datetime import datetime 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, ValidationError, Email

app = Flask(__name__)
#application instance created as an object of Flask library
bootstrap = Bootstrap(app)  #initialization of bootstrap object from flask_bootstrap library
moment = Moment(app)        #initialization of moment object from flask_moment
app.config['SECRET_KEY'] = 'hard to guess string'



#------------------------------ Form Class ------------------------------

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT Email address?', validators=[Email()])
    submit = SubmitField('Submit')
    

#------------------------------ Custom Error Pages ------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

#------------------------------ Route decorators and view functions ------------------------------ 

@app.route('/', methods=['GET', 'POST'])  #route decorator
def index(): #view function index
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')

        if old_name is not None and old_name != form.name.data:   #name mismatch
            flash('Looks like you have changed your name!')       #inform user by message flashing
        if old_email is not None and old_email != form.name.data: #email mismatch from session
            flash('Looks like you have changed your email!')      #inform user by message flashing
        
        session['name'] = form.name.data                          #name stored in user session so that it is remembered beyond the request
        session['email'] = form.email.data                        #email stored in user session so that it can be remembered beyond the request
        return redirect(url_for('index'))                         #respond to POST requests through a redirect
    return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'))

@app.route('/user/<name>')                                                          #dynamic route decorator
def user(name):                                                                     #view function for name specified in url 
    return render_template('user.html', name=name, current_time=datetime.utcnow())  #Jinja2 renders user.html template to get information on client's name
                                                                                    #first argument of render_template() is the filename of template, all succeeding arguments are values for variables referenced in template


