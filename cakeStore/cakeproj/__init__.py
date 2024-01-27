import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view = 'login'

from cakeStore.cupcakes.views import cupcakes_blueprint
from cakeStore.orders.views import orders_blueprints
from cakeStore.cart.views import cart_blueprints

app.register_blueprint(cupcakes_blueprint, url_prefix='/cupcakes')
app.register_blueprint(orders_blueprints, url_prefix='/orders')
app.register_blueprint(cart_blueprints, url_prefix='/cart')