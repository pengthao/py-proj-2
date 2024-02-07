from project import app
from flask import render_template

#            <a class="nav-item nav-link" href="{{url_for('cart.list')}}">view Shopping Cart</a>
#            <a class="nav-item nav-link" href="{{url_for('orders.list')}}">View Orders</a>


app.app_context().push()


@app.route('/')
def home():
    return render_template('home.html')


if __name__=='__main__':
    app.run(debug=True)