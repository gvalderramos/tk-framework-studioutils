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

        with open(
            os.path.abspath(
                os.path.join(".", "tests", "python", "sgorm", "sg_secrets.json")
            ),
            "r",
        ) as sgc:
            self.sg_credentials = json.load(sgc)

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
