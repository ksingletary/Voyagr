from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Optional, URL

class UserForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class UpdatesForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    email = StringField("E-mail", validators=[InputRequired(), Email()])

class EditProfileForm(FlaskForm):
    """Form for editing users."""

    username = StringField('Username', validators=[InputRequired()])
    image_url = StringField("Profile Image(URL)", validators=[URL(), Optional()])

class BookedTrips(FlaskForm):
    """Booking Trips Button"""

    booking = SubmitField("Book Now")

class PremiumBookedTrips(FlaskForm):
    """Booking Trips Button"""

    premium_booking = SubmitField("Book Now")


    



