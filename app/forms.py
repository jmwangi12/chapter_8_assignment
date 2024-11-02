from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    """Register Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class AddProductForm(FlaskForm):
    """Add Product Form"""
    product_name = StringField('Product name', validators=[DataRequired(), Length(1, 64)])
    product_description = TextAreaField('Product description', validators=[DataRequired()])
    stock_available = SelectField('Stock available', validators=[DataRequired()],choices=[('1', '1'), ('2', '2'), ('3', '3')])
    submit = SubmitField('Add product')
