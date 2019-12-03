"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,request,redirect,url_for
from flasksite import app
from flasksite.form import SignupForm
#from flasksite import form

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

@app.route('/survey',methods=['GET','POST'])
def survey():
    """Renders the about page."""
    form = LoginForm()
    if request.method == 'POST':
        print('teste')
        return redirect(url_for('contact'))
    return render_template('survey.html',title='survey',
                           message='Your application description page.',form=form
    )

#import sqlite3  
#con = sqlite3.connect("database.db")  
@app.route('/form',methods=['GET','POST'])
def form():
    form = SignupForm()
    print('entrei')
    if request.method == 'POST':
        print('submit')
        print('email', form.email.data)
        print('title:' ,form.title.data)
        return redirect(url_for('form2'))
    return render_template('form.html',form=form)

@app.route('/form2',methods=['GET','POST'])
def form2():
    form = SignupForm()
    print('entrei')
    if request.method == 'POST':
        print('submit')
        return redirect(url_for('survey'))
    return render_template('form2.html',form=form)


'''
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
'''
@app.route('/success', methods=('GET', 'POST'))
def success():
    return render_template('success.html',template='success-template')

