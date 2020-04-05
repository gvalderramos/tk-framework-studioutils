import os
import unittest
import json
import sys


class TestAuth(unittest.TestCase):
    def setUp(self):
        try:
            import sgorm

            self.sgorm = sgorm
        except Exception as e:
            self.fail("Module sgorm import error, because: {}".format(e))
        with open(
            os.path.abspath(
                os.path.join(".", "tests", "python", "sgorm", "sg_secrets.json")
            ),
            "r",
        ) as sgc:
            self.sg_credentials = json.load(sgc)

    def test_user_auth_method(self):
        auth = self.sgorm.SgAuth(
            host=self.sg_credentials["host"], user="gvalderramos", user_password="1234"
        )
        self.assertTrue(
            auth.user_auth_method,
            "Failed to assert if this class is a user auth method",
        )

    def test_script_auth_method(self):
        auth = self.sgorm.SgAuth(
            host=self.sg_credentials["host"],
            script_name=self.sg_credentials["script_name"],
            script_pass=self.sg_credentials["script_pass"],
        )
        self.assertTrue(
            auth.script_auth_method,
            "Failed to assert if this class is a script auth method",
        )

    def test_connection_by_script_user(self):
        import shotgun_api3

        auth = self.sgorm.SgAuth(
            host=self.sg_credentials["host"],
            script_name=self.sg_credentials["script_name"],
            script_pass=self.sg_credentials["script_pass"],
        )
        sg = auth.connect()
        self.assertIsInstance(sg, shotgun_api3.Shotgun, "Failed to connect to shotgun.")
