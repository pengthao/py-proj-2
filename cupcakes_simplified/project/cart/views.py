from flask import Blueprint, render_template, redirect, url_for, session
from project.models import Cupcake, write_shoppingCart, read_shoppingCart, write_order
from project.cart.forms import EditForm,OrderForm
from datetime import datetime
current_datetime = datetime.now()
print(current_datetime)

cart_blueprint = Blueprint('cart', __name__,template_folder='templates/cart')

@cart_blueprint.route('/cart')
def cart():
    shoppingCart = read_shoppingCart()
    formEdit = EditForm()
    formSubmit = OrderForm()
    total = 0.00
    for cupcake in shoppingCart:
        mod = 1.00
        if cupcake['size'] == 'mini':
            mod = 0.8
        elif cupcake['size'] == 'large':
            mod = 1.25
        elif cupcake['size'] == 'cake!':
            mod = 3.0

        total += cupcake['price'] * cupcake['quantity'] * mod

    formSubmit.total.data = total
    return render_template('cart.html', shoppingCart=shoppingCart, formEdit=formEdit, formSubmit=formSubmit, mod=mod )

@cart_blueprint.route('/editCart/<int:cupcake_id>', methods=["GET", "POST"])
def editCart(cupcake_id):

    formEdit = EditForm()

    if formEdit.validate_on_submit():
        shoppingCart = read_shoppingCart()

        for cupcake in shoppingCart:
            if cupcake['id'] == cupcake_id:
                if formEdit.quantity.data == 0:
                    # If quantity is 0, skip and do not add to the updated cart
                    continue
                else:
                    # Update cupcake details
                    cupcake['size'] = formEdit.size.data
                    cupcake['quantity'] = formEdit.quantity.data

        
        write_shoppingCart(shoppingCart)
        formSubmit = OrderForm()
        return redirect(url_for('cart.cart'))
    return render_template('cart.html', formEdit=formEdit, formSubmit=formSubmit)


@cart_blueprint.route('/order', methods=['GET', 'POST'])
def submitOrder():
    shoppingCart = read_shoppingCart()
    
    formSubmit = OrderForm()

    if formSubmit.validate_on_submit():
        order_data = {
            'name': formSubmit.name.data,
            'phone': formSubmit.phone.data,
            'date': formSubmit.date.data,
            'total': formSubmit.total.data,
            'shoppingCart': shoppingCart
        }

        write_order(order_data)
        write_shoppingCart([])

        return redirect(url_for('orders.viewOrders'))

    return render_template('cart.html', formSubmit=formSubmit)