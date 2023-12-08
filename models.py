"""Models for Voyagr"""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime


db = SQLAlchemy()

bcrypt = Bcrypt()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    """User Model"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=True)

    # start_register
    @classmethod
    def register(cls, username, pwd):
        """Register user w/hashed password & return user."""

        hashed = bcrypt.generate_password_hash(pwd)
        # turn bystestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode("utf8")

        # return instance of user w/username and hashed pwd
        return cls(username=username, password=hashed_utf8)
    # end register
    @classmethod
    def authenticate(cls, username, pwd):
        """Validate that user exists & password is correct
        
        Return user if valid; else return False.
        """

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            # return user instance
            return u
        else:
            return False
    # end authenticate

class Trip(db.Model):
    """Trip Model"""

    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    description = db.Column(db.Text, nullable=True, default=None)
    photo = db.Column(db.Text, nullable=True, default=None)
    cost = db.Column(db.Float, nullable=False, unique=True)


class Activity(db.Model):
    """Activity Model"""

    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    name = db.Column(db.Text, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=True)
    description = db.Column(db.Text, nullable=True, default=None)
    
class Location(db.Model):
    """Location Model"""

    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.Text, nullable=False)
    country = db.Column(db.Text, nullable=False)

class Booked_Trip(db.Model):
    """Booked Trips Model"""

    __tablename__ = 'booked_trips'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cost = db.Column(db.Float, db.ForeignKey('trips.cost'), nullable=False)
    booked_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    

