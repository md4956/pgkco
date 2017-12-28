from functools import wraps
from flask import request, render_template, redirect, url_for, flash, Flask

app = Flask(__name__, instance_relative_config=True)


def required_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if get_current_user_role() not in roles:
                flash('Authentication error, please check your details and try again', 'error')
                return redirect(url_for('index'))
            return f(*args, **kwargs)

        return wrapped

    return wrapper


def get_current_user_role():
    return g.user.role


@app.route('/register' , methods=['GET','POST'])
@required_roles('admin')
def register():
    return 'hi !'




if __name__ == '__main__':
    app.run(debug=True)
