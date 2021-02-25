from flask import Flask
from flask_mail import Mail
from .config import Config
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

app = Flask(__name__)
app.config.from_object(Config)
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = '82a2db10bc2089'
app.config['MAIL_PASSWORD'] = '0e941b762f2293'
app.config['SECRET_KEY'] = 'spicy'

mail = Mail(app)
csrf.init_app(app)
from app import views
