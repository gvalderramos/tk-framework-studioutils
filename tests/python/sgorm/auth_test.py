import os
import unittest
import json
import sys


class TestAuth(unittest.TestCase):
    def setUp(self):
        try:
            from python import sgorm

            self.sgorm = sgorm
        except Exception as e:
            self.fail("Module sgorm import error, because: {}".format(e))

        self.user = os.getenv("SG_USER")
        self.user_password = os.getenv("SG_USER_PASSWORD")
        self.user_token = os.getenv("SG_USER_TOKEN")
        self.host = os.getenv("SG_HOST")
        self.script_name = os.getenv("SG_SCRIPT_NAME")
        self.script_pass = os.getenv("SG_SCRIPT_PASS")

    def test_user_auth_method(self):
        auth = self.sgorm.SgAuth(
            host=self.host, user=self.user, user_password=self.user_password
        )
        self.assertTrue(
            auth.user_auth_method,
            "Failed to assert if this class is a user auth method",
        )

    def test_script_auth_method(self):
        auth = self.sgorm.SgAuth(
            host=self.host, script_name=self.script_name, script_pass=self.script_pass,
        )
        self.assertTrue(
            auth.script_auth_method,
            "Failed to assert if this class is a script auth method",
        )

    def test_connection_by_script_user(self):
        from vendor import shotgun_api3

        auth = self.sgorm.SgAuth(
            host=self.host, script_name=self.script_name, script_pass=self.script_pass,
        )
        sg = auth.connect()
        self.assertIsInstance(sg, shotgun_api3.Shotgun, "Failed to connect to shotgun.")
