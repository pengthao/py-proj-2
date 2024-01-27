from pprint import pprint
from cakeStore import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Cupcakes(db.Model):

    __tablename__='cupcakes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    flavor = db.Column(db.Text)
    filling = db.Column(db.Text)
    toppings = db.Column(db.Text)
    price = db.Column(db.Float)
    sprinkles = db.Column(db.Boolean)

    def __init__(self, name, description, flavor, filling, toppings, price):
        

        self.name = name
        self.description = description
        self.flavor = flavor
        self.filling = filling
        self.toppings = toppings
        self.price = price
        self.sprinkles = False
    
    def display_details(self):
        return f"{self.name} a {self.flavor} flavored cupcake topped with {self.toppings}. {self.servings} servings for ${self.price}."

    
    def add_sprinkles(self):
        self.sprinkles = True


class User(db.Model):

    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
    def __repr__(self):
        return f"UserName: {self.username}"

    #objectives
#Student can use Python decorator.
#Student can use Python generator.
#Student can use collections module.
#Student knows about the OS module and can use open/read files function.
#Student can use the datetime module.
#Student can use random module.
#Student can use Python math module.
#Student can use pdb module.


     #Flask objectives
#Student has an understanding of all the elements that make up a full-stack web app.
#Student has an understanding of the structure of a Flask app.
#Student can run a minimal Flask app.
#Student can set an endpoints during the @app.route() decorator, and create a paired view function with it.
#Add an argument to an endpoint, and be able to pass it in as an argument to the respective view function.
#Student can use Flask debug mode.
#Student can use Flask’s “render_template” function.
            

#enter a cupcake
#view all cupcakes
#filter by properties
#add to cart
#view cart
#checkout
