from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField


class AddForm(FlaskForm):

    size = RadioField('Select Cupcake Size', choices=['regular', 'mini', 'large', 'cake!'])
    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')