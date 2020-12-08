# test_bucketlist.py
import unittest
import os
import json
from app import app, db




class SignupTest(unittest.TestCase):

    def setUp(self):
        self.app.cofig[] = app.Post()
        self.Post = db.get_db()

    def test_successful_creation(self):
        # Given
        payload = json.dumps({
            "title": "my strange addiction",
            "body": "im a mess my head id blowing up"
        })

        # When
        response = self.app.post('/add-post', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)



    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
