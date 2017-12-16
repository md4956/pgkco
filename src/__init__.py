from flask import Flask
from src.login.views import login_blueprint
from src.signup.views import signup_blueprint
from flask_login import LoginManager

app = Flask(__name__, instance_relative_config=True)


# moarafi o link e blueprint ha be app
app.register_blueprint(login_blueprint, url_prefix='/login')
app.register_blueprint(signup_blueprint, url_prefix='/signup')

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "users.login"

