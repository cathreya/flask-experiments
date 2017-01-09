from flask_wtf import FlaskForm 
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username = StringField('username', validators=[DataRequired()])
	remember = BooleanField('remember', default=False)
