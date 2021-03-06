from flask import Blueprint, render_template, request, redirect, url_for, flash, get_flashed_messages, abort, Response, session
from pymongo import MongoClient
from src.security.models import security
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from werkzeug.security import check_password_hash
from var_dump import var_dump
from src.models import collection
from flask_user import roles_required, UserMixin


# blueprint for this .py
login_blueprint = Blueprint('login', __name__, template_folder='templates')

login_manager = LoginManager()


# Define the Role data-model
class Role:
    __tablename__ = 'roles'
    id = collection['_id']
    email = collection['email']


# Define the UserRoles association table
class UserRoles:
    __tablename__ = 'user_roles'
    id = collection['_id']
    user_id = collection['_id']
    role_id = collection['role']


class User(UserMixin):

    def __init__(self, username):
        self.id = username

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)


@login_manager.user_loader
def load_user(username):
    return User(username)
    # u = collection.find_one({"_id": username})
    # if not u:
    #     return None
    # return User(u['_id'])
    # return User(username)


# login page
@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login/login.html')


# checking user and pass
@login_blueprint.route('/processing', methods=['POST'])
def logging_processing():
    finduser = collection.find_one({'email': request.form['email']})
    if finduser:
        if security.check_password(finduser['password'], request.form['password']) is True:
            var_dump(finduser['_id'])
            print(finduser['role'])
            user_obj = User(str(finduser['_id']))
            login_user(user_obj)
            session['username'] = request.form['email']
            return redirect(url_for('main_page.main'))
        else:
            flash('please check your password and try again', 'login')
        return redirect(url_for('login.login'))
    else:
        flash('please check your email and try again', 'login')
        return redirect(url_for('login.login'))


# # redirect authenticated users to main page
# @login_blueprint.route('/logged_in')
# @login_required
# def logged_in():
#     if 'username' in session:
#         return 'you are logged in as ' + session['username']
#     return '<h1>welcome !</h1>'


# # logout
# @login_blueprint.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return 'logout done'


# test route
@login_blueprint.route('/test')
@login_required
@roles_required('admin')
def test():
    return 'done'
