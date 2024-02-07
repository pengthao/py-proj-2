from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField, DateField
from wtforms.validators import InputRequired


class AddForm(FlaskForm):

    size = SelectField('Select Cupcake Size: ', choices=['regular', 'mini', 'large', 'cake!'])
    quantity = IntegerField('Quantity: ', validators=[InputRequired()])
    sprinkles = SelectField('Select Sprinkles: ', choices=['red', 'white', 'blue', 'None'], default='None')
    filling = SelectField('Select Filling: ', choices=['vanilla', 'lemon', 'chocolate', 'None'], default='None')
    submit = SubmitField('Add to Cart')