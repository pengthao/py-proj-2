from flask import Blueprint, render_template, redirect, url_for, session, flash
from project.models import Cupcake, cupcakes_list, write_shoppingCart, read_shoppingCart
from project.cupcakes.forms import AddForm
from datetime import datetime
current_datetime = datetime.now()
print(current_datetime)

cupcakes_blueprint = Blueprint('cupcakes', __name__,template_folder='templates/cupcakes')

@cupcakes_blueprint.route('/list')
def list():
    session.clear()
    cupcakes = cupcakes_list()
    for index, cupcake in enumerate(cupcakes, start=1):
        session[str(index)] = cupcake.to_dictionary()

    return render_template('list.html', cupcakes=cupcakes)


@cupcakes_blueprint.route('/add/<int:cupcake_id>', methods=["GET", "POST"])
def add(cupcake_id):
    
    cupcake_key = str(cupcake_id)
    session_cupcake = session.get(cupcake_key, {})

    if not session_cupcake:
        flash('Cupcake not found.', 'error')
        return redirect(url_for('cupcakes.list'))

    cupcake = Cupcake.from_dict(session_cupcake)

    form = AddForm()

    print("Form data received:", form.data)

    if form.validate_on_submit():
        print("Validation is successful.")
        shoppingCart = read_shoppingCart()
        
        session_cupcake['size'] = form.size.data
        session_cupcake['quantity'] = form.quantity.data
        if form.sprinkles.data is not None:
            session_cupcake['sprinkles'] = form.sprinkles.data
        if form.filling.data is not None:
            session_cupcake['filling'] = form.filling.data

        cupcake_found = False
        for cupcake in shoppingCart:
            if cupcake['id'] == session_cupcake['id']:
                cupcake['quantity'] += session_cupcake['quantity']
                shoppingCart.append(cupcake)
                cupcake_found = True
                break

        if not cupcake_found:
            shoppingCart.append(session_cupcake)

        write_shoppingCart(shoppingCart)

        session.clear()
        form = AddForm(formdata=None)
        return redirect(url_for('cart.cart'))

    else:
        print("Validation failed. Errors:", form.errors)  # Add this line
        print("Form errors:", form.errors)  # Add this line

    return render_template('add.html', form=form, cupcake=cupcake)


