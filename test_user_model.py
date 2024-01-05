import unittest
from models import db, User
from app import app

class TestUserModel(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///voyagr_test'  # Use test database
        app.config['TESTING'] = True
        self.app = app.test_client()

        with app.app_context():
            db.create_all()

    def tearDown(self):
        """Clean up after the test"""
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register_user(self):
        """Test user registration"""
        with app.app_context():
            username = 'test_user'
            password = 'test_password'

            # Register a new user
            new_user = User.register(username, password)
            db.session.add(new_user)
            db.session.commit()

            # Retrieve the registered user from the test database
            retrieved_user = User.query.filter_by(username=username).first()

            # Check if the retrieved user matches the registered one
            self.assertEqual(retrieved_user.username, username)

    def test_authenticate_user(self):
        """Test user authentication"""
        with app.app_context():
            username = 'test_user'
            password = 'test_password'

            # Register a new user
            new_user = User.register(username, password)
            db.session.add(new_user)
            db.session.commit()

            # Authenticate the user
            authenticated_user = User.authenticate(username, password)

            # Check if the authenticated user is not False
            self.assertIsNot(authenticated_user, False)
            # Check if the authenticated user's username matches
            self.assertEqual(authenticated_user.username, username)

            # Attempt authentication with incorrect password
            invalid_authenticated_user = User.authenticate(username, 'wrong_password')

            # Check if the invalid authentication returns False
            self.assertIs(invalid_authenticated_user, False)

if __name__ == '__main__':
    unittest.main()
