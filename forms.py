from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, InputRequired, Email

class UserForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class UpdatesForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    email = StringField("E-mail", validators=[InputRequired(), Email()])