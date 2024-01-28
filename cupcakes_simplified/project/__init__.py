import os
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))


from project.cupcakes.views import cupcakes_blueprint
from project.orders.views import orders_blueprints
from project.cart.views import cart_blueprints

app.register_blueprint(cupcakes_blueprint, url_prefix='/cupcakes')
app.register_blueprint(orders_blueprints, url_prefix='/orders')
app.register_blueprint(cart_blueprints, url_prefix='/cart')