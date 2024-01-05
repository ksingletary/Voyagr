import unittest
from models import db, Booked_Trip, Trip, User, Location
from app import app

class TestBookedTripModel(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        with app.app_context():
            app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///voyagr_test'
            app.config['TESTING'] = True
            self.app = app.test_client()
            db.create_all()

    def tearDown(self):
        """Clean up after the test"""
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_booked_trip_creation(self):
        """Test creating a Booked_Trip instance"""
        # Create sample data for testing
        with app.app_context():
            location = Location(city='Italy', country='Rome', id=1)  # Update with actual Location model attributes
            db.session.add(location)
            db.session.commit()
            user = User(username='test_user',  id=2, password="HASHED_PASSWORD")  # Update with actual User model attributes
            trip = Trip(location_id=location.id, cost=100.0, activity_link="https://www.travelocity.com/", activity_link1="https://www.travelocity.com/", activity_link2="https://www.travelocity.com/" )  # Update with actual Trip model attributes

            # Save the sample data to the test database
            db.session.add(user)
            db.session.add(trip)
            db.session.commit()

            # Create a Booked_Trip instance
            booked_trip = Booked_Trip(location_id=trip.id, user_id=user.id, cost=trip.cost)

            # Save the Booked_Trip instance to the test database
            db.session.add(booked_trip)
            db.session.commit()

            # Retrieve the saved Booked_Trip from the test database
            saved_trip = Booked_Trip.query.filter_by(id=booked_trip.id).first()

            # Check if the saved Booked_Trip matches the created one
            self.assertEqual(saved_trip.location_id, trip.id)
            self.assertEqual(saved_trip.user_id, user.id)
            self.assertEqual(saved_trip.cost, trip.cost)

if __name__ == '__main__':
    unittest.main()
