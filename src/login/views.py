from flask import Blueprint, render_template, request, redirect, url_for, flash, get_flashed_messages
from pymongo import MongoClient
from src.security.models import security


# blueprint for this .py
login_blueprint = Blueprint('login', __name__, template_folder='templates')

# connect to mongodb
client = MongoClient('mongodb://localhost:27017/')
db = client.pgco
collection = db.users


# login page
@login_blueprint.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login/login.html')


# checking user and pass
@login_blueprint.route('/processing', methods=['POST'])
def logging_processing():
    finduser = collection.find_one({'email': request.form['email']})
    if finduser:
        if security.check_password(finduser['password'], request.form['password']) is True:
            return redirect(url_for('login.logged_in'))
        else:
            flash('please check your password and try again', 'login')
            return redirect(url_for('login.login'))
    else:
        flash('please check your email and try again', 'login')
        return redirect(url_for('login.login'))


# redirect authenticated users to main page
@login_blueprint.route('/logged_in')
def logged_in():
    return '<h1>welcome !</h1>'

#
# @login_blueprint.route('/test1')
# def logged1():
#     flash("i'm coming from test1", 'login')
#     return 'this is test'
#
#
# @login_blueprint.route('/test2')
# def logged2():
#     return render_template('test.html')
