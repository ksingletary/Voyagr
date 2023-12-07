from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Email, Optional

class UserForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    image_url = StringField("Profile Image(URL)", validators=[Optional()])

class UpdatesForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    email = StringField("E-mail", validators=[InputRequired(), Email()])

class EditProfileForm(FlaskForm):
    """Form for editing users."""

    username = StringField('Username', validators=[InputRequired()])
    new_password = PasswordField("New Password", validators=[InputRequired()])
    image_url = StringField("Profile Image(URL)", validators=[Optional()])

