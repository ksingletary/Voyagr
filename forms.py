from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, Email, Optional, URL

class UserForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class UpdatesForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()], render_kw={"placeholder": "name"})
    email = StringField("E-mail", validators=[InputRequired(), Email()], render_kw={"placeholder": "email"})

class EditProfileForm(FlaskForm):
    """Form for editing users."""

    username = StringField('Username', validators=[InputRequired()])
    image_url = StringField("Profile Image(URL)", validators=[URL(), Optional()])

class BookedTrips(FlaskForm):
    """Booking Trips Button"""

    date = SelectField("Available Dates", validators=[InputRequired()], choices=[(1, 'Available Dates'), (2, '03/5/24 - 03/12/24'), (3, '04/10/24 - 04/17/24'), (4, '05/1/24 - 05/8/24'), (5, '01/5/24 - 01/12/24'), (6, '02/10/24 - 02/17/24'), (7, '03/1/24 - 03/8/24'), (8, '06/5/24 - 06/12/24'), (9, '07/10/24 - 07/17/24'), (10, '08/1/24 - 08/8/24')])
    booking = SubmitField("Book Now")

class PremiumBookedTrips(FlaskForm):
    """Booking Trips Button"""

    date = SelectField("Available Dates", validators=[InputRequired()], choices=[(1, 'Available Dates'), (2, '03/5/24 - 03/19/24'), (3, '04/10/24 - 04/24/24'), (4, '05/1/24 - 05/15/24'), (5, '01/5/24 - 01/19/24'), (6, '02/10/24 - 02/24/24'), (7, '03/1/24 - 03/15/24'), (8, '06/5/24 - 06/19/24'), (9, '07/10/24 - 07/24/24'), (10, '08/1/24 - 08/15/24')])
    premium_booking = SubmitField("Book Now")

class CancelTrip(FlaskForm):
    """Canceling a trip"""

    cancel = SelectField("Cancel Trip", choices=[("Tokyo", "Tokyo"), ("Rome", "Rome"), ("Greater Cairo", "Greater Cairo"), ("Dubai", "Dubai"), ("Paris", "Paris") ])
    submit_cancellation = SubmitField("Cancel Trip")





    



