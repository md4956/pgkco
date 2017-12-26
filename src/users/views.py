from flask import Blueprint, request, render_template, redirect, url_for
from src.login.views import collection
from src.security.models import security


users_blueprint = Blueprint('users', __name__, template_folder='templates')


#TODO check user structure in database
@users_blueprint.route('/users', methods=['get', 'post'])
def user_list():
    find = collection.find()
    usr = []
    for i in find:
        usr.append(i)
    if request.args.get('edit'):
        x = request.args.get('edit')
        return render_template('test.html',x=x)
    # print(request.args.get('id'))
    # print(usr[0])
    print(usr[0]['email'])
    return render_template('users/users.html', usr=usr)


@users_blueprint.route('/user_edit', methods=['get', 'post'])
# def create_user():
#     pass


# def read_user():
#     pass


def update_user():
    finduser = collection.find_one({'email': request.form['email']})
    newemail = request.form['email']
    newpassword = security.set_password(request.form['password'])
    newfirstname = request.form['first name']
    newlastname = request.form['last name']
    newphone = request.form['phone']
    collection.update({'email': finduser['email']}, {'$set': {'firstname': newfirstname}})
    collection.update({'email': finduser['email']}, {'$set': {'lastname': newlastname}})
    collection.update({'email': finduser['email']}, {'$set': {'phone': newphone}})
    collection.update({'email': finduser['email']}, {'$set': {'password': newpassword}})
    # collection.update({'firstname': finduser['firstname']}, {'$set': {'email': newemail}})
    print(finduser['firstname'])
    return redirect(url_for('users.user_list'))


# def delete_user():
#     pass
