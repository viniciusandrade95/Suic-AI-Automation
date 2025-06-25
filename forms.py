from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class AdminLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class BusinessForm(FlaskForm):
    # Add fields as needed for admin edit
    pass

class ServiceForm(FlaskForm):
    # Add fields as needed for service add/update
    pass
