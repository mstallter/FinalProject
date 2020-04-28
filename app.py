from flask import Flask, render_template, flash, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_sqlalchemy import SQLAlchemy as _BaseSQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.urls import url_parse
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from functools import wraps
import pymysql
#import os
import secrets


conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

# Open database connection
#dbhost = os.environ.get('DBHOST')
#dbuser = os.environ.get('DBUSER')
#dbpass = os.environ.get('DBPASS')
#dbname = os.environ.get('DBNAME')

#conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(dbuser, dbpass, dbhost, dbname)

#db = pymysql.connect(dbhost, dbuser, dbpass, dbname)

app = Flask(__name__)


app.config['SECRET_KEY']='SuperSecretKey'
#import os
# = os.environ.get('SECRET_KEY')


# Prevent --> pymysql.err.OperationalError) (2006, "MySQL server has gone away (BrokenPipeError(32, 'Broken pipe')
class SQLAlchemy(_BaseSQLAlchemy):
     def apply_pool_defaults(self, app, options):
        super(SQLAlchemy, self).apply_pool_defaults(app, options)
        options["pool_pre_ping"] = True
# <-- MWC


app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
db = SQLAlchemy(app)


class LoginForm(FlaskForm):
    studentid = StringField('StudentID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


ACCESS = {
    'guest': 0,
    'user': 1,
    'admin': 2
}


class LoginForm(FlaskForm):
    studentid = StringField('Student ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')



#### Routes ####

# index
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', pageTitle='Flask App Home Page')

# register
@app.route('/register')
def register():
    return render_template('register.html', pageTitle='Create your account')

#login
@app.route('/login')
def login():
    return render_template('login.html', pageTitle='Login Page')


if __name__ == '__main__':
    app.run(debug=True)
