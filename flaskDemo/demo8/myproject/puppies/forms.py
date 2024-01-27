from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):
    
    pup_id = IntegerField("Id number of Puppy to remove: ")
    submit = SubmitField('Remove Puppy')