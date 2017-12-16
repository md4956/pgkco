from flask import Blueprint, render_template, request, redirect, url_for, flash, get_flashed_messages
from pymongo import MongoClient
from src.security.models import security

# blueprint for this .py
signup_blueprint = Blueprint('signup', __name__, template_folder='templates')

# connect to mongodb
client = MongoClient('mongodb://localhost:27017/')
db = client.pgco
collection = db.users


# signup page
@signup_blueprint.route('/', methods=['GET', 'POST'])
def signup():
    return render_template('signup/signup.html')


# checking user and pass
@signup_blueprint.route('/processing', methods=['POST'])
def signing_processing():
    find = collection.find_one({'email': request.form['email']})

    p1 = request.form['password']
    p2 = request.form['repassword']
    #print(p1, p2)

    if p1 == p2:

    if find:
        flash('this email is already exists. please log in or use another email', 'signup')
        return redirect(url_for('signup.signup'))
    elif p1 != p2:
        flash('both password fields must match', 'login')
        return redirect(url_for('signup.signup'))
    else:
        hashed_password = security.set_password(request.form['password'])
        user = {'email': request.form['email'], 'password': hashed_password}
        collection.insert_one(user).inserted_id
        flash('successful. now you can log in', 'login')
        return redirect(url_for('login.login'))


# redirect authenticated users to main page
@signup_blueprint.route('/signed_up')
def signed_up():
    return '<h1>done !</h1>'


@signup_blueprint.route('/test')
def test():
    mhasani = {
        'email': "mohammad@live.com",
        'passwrod': 'pass',
        'name': 'mohammad',
        'family': 'hasani',
        'asdasdasd': 'asdasdasdasd'
    }
    collection = db.username
    x = collection.insert_one(mhasani).inserted_id
    y = collection.find_one({'email': 'mohammaasdasdasdd@live.com'})

    print(y)
    return 'ok'
