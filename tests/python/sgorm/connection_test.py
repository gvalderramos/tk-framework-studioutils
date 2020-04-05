import os
import sys
import json
import unittest
from pprint import pprint


class TestConnection(unittest.TestCase):
    def setUp(self):
        try:
            import sgorm

            self.sgorm = sgorm
        except Exception as e:
            self.fail("Module sgorm import error, because: {}".format(e))

        self.user = os.getenv("SG_USER")
        self.user_password = os.getenv("SG_USER_PASSWORD")
        self.user_token = os.getenv("SG_USER_TOKEN")
        self.host = os.getenv("SG_HOST")
        self.script_name = os.getenv("SG_SCRIPT_NAME")
        self.script_pass = os.getenv("SG_SCRIPT_PASS")

    def test_issingleton(self):
        cn1 = self.sgorm.Connection()
        cn2 = self.sgorm.Connection()
        self.assertIs(cn1, cn2, "The Connection class must be a singleton class")

    def test_sameattrs(self):
        cn1 = self.sgorm.Connection()
        cn2 = self.sgorm.Connection()
        cn1._test_attr = "hey"
        cn2._test_attr = "man"
        self.assertEqual(
            cn1._test_attr,
            cn2._test_attr,
            "The connection class must be a singleton class",
        )

    def test_shotgun_connection(self):
        cnn = self.sgorm.Connection()
        self.assertIsNone(cnn.shotgun)

        import shotgun_api3

        auth = self.sgorm.SgAuth(
            host=self.sg_credentials["host"],
            script_name=self.sg_credentials["script_name"],
            script_pass=self.sg_credentials["script_pass"],
        )
        cnn.shotgun = auth

        self.assertIsInstance(cnn.shotgun, shotgun_api3.Shotgun)


if __name__ == "__main__":
    unittest.main()
