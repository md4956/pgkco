from flask import Flask
from flask_login import LoginManager
from src.login.views import login_blueprint
from src.signup.views import signup_blueprint
from src.main_page.views import main_page_blueprint
from src.users.views import users_blueprint

app = Flask(__name__, instance_relative_config=True)

# blueprints
app.register_blueprint(login_blueprint, url_prefix='/auth')
app.register_blueprint(signup_blueprint, url_prefix='/signup')
app.register_blueprint(main_page_blueprint)
app.register_blueprint(users_blueprint)
# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login.login"

