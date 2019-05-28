from flask import Flask
from flask_login import LoginManager
from flask_compress import Compress
from flask_mail import Mail
from models import db
from liqpay.liqpay import LiqPay


PUBLIC_KEY = 'i18183574422'
PRIVATE_KEY = 'DWHmS0mwLkNTIUJJhP6bTmAN4WpKshVJomDSdeZ3'


app = Flask(__name__)
app.config.from_pyfile('app.cfg')
db.init_app(app)

compress = Compress(app)
login_manager = LoginManager()
mail = Mail(app)
liqpay = LiqPay(PUBLIC_KEY, PRIVATE_KEY)

login_manager.init_app(app)
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message = "Please LOG IN"
login_manager.login_message_category = "info"


import views
