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
        return render_template('users/edit_users.html', x=x)
    elif request.args.get('show'):
        y = request.args.get('show')
        showuser = collection.find_one({'email': y})
        return render_template('users/show_users.html', y=y, showuser=showuser)
    elif request.args.get('delete'):
        z = request.args.get('delete')
        selectuser = collection.find_one({'email': z})
        return render_template('users/delete_users.html', z=z, selectuser=selectuser)
    elif request.args.get('create'):
        w = request.args.get('create')
        print(w)
        return render_template('users/create_users.html', w=w)
    # print(request.args.get('id'))
    # print(usr[0])
    return render_template('users/users.html', usr=usr)


@users_blueprint.route('/users_create', methods=['get', 'post'])
def create_user():
    finduser = collection.find_one({'email': request.form['email']})
    useremail = request.form['email']
    p1 = request.form['password']
    p2 = request.form['password1']
    if finduser:
        return 'the email' + useremail + 'does exists. please try again with a new email address'
    if p1 == p2:
        password = security.set_password(request.form['password'])
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        phone = request.form['phone']

        collection.insert_one({
            'email': useremail,
            'password': password,
            'firstname': firstname,
            'lastname': lastname,
            'phone': phone
        })
        return 'user (' + useremail + ') created.'
    else:
        return 'both password fields does not match. try again'


@users_blueprint.route('/users_read', methods=['get', 'post'])
def read_user():
    return redirect(url_for('users.user_list'))


@users_blueprint.route('/users_update', methods=['get', 'post'])
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


@users_blueprint.route('/users_delete/', methods=['get', 'post'])
@users_blueprint.route('/users_delete/<email>', methods=['get', 'post'])
def delete_user(email):
    print('deleting user: ' + email)
    collection.remove({'email': email})
    return redirect(url_for('users.user_list'))
