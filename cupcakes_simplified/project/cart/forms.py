from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField, StringField, HiddenField
from wtforms.validators import InputRequired
from datetime import date, timedelta
twodays= date.today() + timedelta(days=2)
threedays= date.today() + timedelta(days=3)
fourdays= date.today() + timedelta(days=4)
fivedays= date.today() + timedelta(days=5)
sixdays= date.today() + timedelta(days=6)
sevendays= date.today() + timedelta(days=7)

def dateRange():
    dates = []
    max = 7
    index = 2
    while index < max:
        pickup = date.today() + timedelta(days=index)
        dates.append(pickup)
        index+=1
    
    return dates

class AddForm(FlaskForm):
    
    size = SelectField('Select Cupcake Size: ', choices=['regular', 'mini', 'large', 'cake!'])
    quantity = IntegerField('Quantity: ')
    submit = SubmitField('Add to Cart')

class EditForm(FlaskForm):

    size = SelectField('Update Cupcake Size: ', choices=['regular', 'mini', 'large', 'cake!'])
    quantity = IntegerField('Quantity: ')
    submit = SubmitField('Update')


class OrderForm(FlaskForm):

    name = StringField('Name: ', validators=[InputRequired()])
    phone = StringField('Phone Number: ', validators=[InputRequired()])
    date = SelectField('Pickup date: ', choices=dateRange(), validators=[InputRequired()])
    total = HiddenField('Total')
    submit = SubmitField('Checkout')