import os
import unittest
import json
import sys
import shotgun_api3


class TestAuth(unittest.TestCase):
    def setUp(self):
        try:
            from python import sgorm

            self.sgorm = sgorm
        except Exception as e:
            self.fail("Module sgorm import error, because: {}".format(e))

        self.user = os.getenv("SG_USER")
        self.user_password = os.getenv("SG_USER_PASSWORD")
        self.user_token = os.getenv("SG_USER_TOKE")
        self.host = os.getenv("SG_HOST")
        self.script_name = os.getenv("SG_SCRIPT_NAME")
        self.script_pass = os.getenv("SG_SCRIPT_PASS")

    def test_script_auth_method(self):
        auth = self.sgorm.SgAuth(
            host=self.host, script_name=self.script_name, script_pass=self.script_pass,
        )
        self.assertEqual(
            auth.script_auth_method,
            True,
            "Failed to assert if this class is a script auth method",
        )

    def test_connection_by_script_user(self):
        auth = self.sgorm.SgAuth(
            host=self.host, script_name=self.script_name, script_pass=self.script_pass,
        )
        sg = auth.connect()
        self.assertIsInstance(sg, shotgun_api3.Shotgun, "Failed to connect to shotgun.")
