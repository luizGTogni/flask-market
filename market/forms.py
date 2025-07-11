from market.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError

class RegisterForm(FlaskForm):
  username = StringField(label='Username:', validators=[Length(min=3, max=30), DataRequired()])
  email_address = StringField(label='Email:', validators=[Email(), DataRequired()])
  password1 = PasswordField(label='Password:', validators=[Length(min=8), DataRequired()])
  password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
  submit = SubmitField(label='Create Account')

  def validate_username(self, username_to_check):
    user = User.query.filter_by(username=username_to_check.data).first()
    if user:
      raise ValidationError('Username already exists! Pleasy try a different username')
    
  def validate_email_address(self, email_address_to_check):
    user = User.query.filter_by(email_address=email_address_to_check.data).first()
    if user:
      raise ValidationError('Email Address already exists! Please try a different email')
    
class LoginForm(FlaskForm):
  username = StringField(label='Username:', validators=[DataRequired()])
  password = PasswordField(label='Password:', validators=[DataRequired()])
  submit = SubmitField(label='Sign In')

class PurchaseItemForm(FlaskForm):
  submit = SubmitField(label='Purchase')

class SellItemForm(FlaskForm):
  submit = SubmitField(label='Sell Item')