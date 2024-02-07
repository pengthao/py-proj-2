from flask import Blueprint, render_template, redirect, url_for
from project.models import read_orders



orders_blueprint = Blueprint('orders', __name__,template_folder='templates/orders')

@orders_blueprint.route('/cart')
def viewOrders():
    orders = read_orders()
    return render_template('orders.html', orders=orders)