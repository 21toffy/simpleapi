# test_post.py
import unittest
import os
import json
from app import app, db
from flask import Flask





class SignupTest(unittest.TestCase):
    # check if status is 200
    def test_posts(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # checking for data returned
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertTrue(b'posts' in response.data)



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
