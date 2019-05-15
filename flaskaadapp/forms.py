from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError


class Form1(FlaskForm):
    parameter1 = StringField('Parameter1')
    parameter2 = StringField('Parameter2')
    submit = SubmitField('Submit')