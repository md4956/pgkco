from flask import Blueprint, render_template, request, redirect, url_for, flash, get_flashed_messages, abort, Response, session
from pymongo import MongoClient
from src.security.models import security
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from werkzeug.security import check_password_hash
from var_dump import var_dump


main_page_blueprint = Blueprint('main_page', __name__, template_folder='templates')


@main_page_blueprint.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main_page/main_page.html')


# logout
@main_page_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('logout successfully done', 'login')
    return redirect(url_for('login.login'))
