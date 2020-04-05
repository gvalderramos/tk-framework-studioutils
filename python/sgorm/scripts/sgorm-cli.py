"""
Sgorm CLI
"""

from studioutils_third_party import shotgun_api3
import json
import os
import argparse
import textwrap


class SgormCli(object):
    def __init__(self, args):
        self.__dict__ = args
        self._sg = self._connect()
        self.schema = {}
        self.cache()
        self.create_entities()

    def _connect(self):
        return shotgun_api3.Shotgun(
            self.host, login=self.user_name, password=self.user_password
        )

    def cache(self):
        if not os.path.isdir(self.cache_folder):
            os.makedirs(self.cache_folder)

        with open("{}/schema.json".format(self.cache_folder), "w") as json_file:
            self.schema = self._sg.schema_read()
            json.dump(self.schema, json_file, indent=4)

    def create_entities(self):
        if not os.path.isdir(self.entity_folder):
            os.makedirs(self.entity_folder)

        for entity, entity_data in self.schema.iteritems():
            entity_file = "{}/{}.py".format(self.entity_folder, entity)
            py_data = str(
                "import Model\n"
                "import DataType\n"
                "\n"
                "\n"
                "class {entity_name}(Model.Entity):\n"
                "    def __init__(self):\n"
                "        super({entity_name}, self).__init__(self.__class__.__name__)\n"
                "\n".format(entity_name=entity)
            )
            for field, field_data in entity_data.iteritems():
                if field_data.get("visible", {}).get("value") is False:
                    continue
                py_data += "        self.{field} = DataType.Field('{field}', None)\n".format(
                    field=field
                )
            with open(entity_file, "w") as py_entity:
                py_entity.write(py_data)


def _args_parser():
    parser = argparse.ArgumentParser(
        description=textwrap.dedent(__doc__),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        prog="pipeline_configuration.py",
    )

    parser.add_argument(
        "-un", "--user_name", type=str, required=False, help="User name"
    )

    parser.add_argument(
        "-up", "--user_password", type=str, required=False, help="User password"
    )

    parser.add_argument("-ht", "--host", type=str, required=False, help="Studio's host")

    parser.add_argument(
        "-cf",
        "--cache_folder",
        type=str,
        required=False,
        help="Cache folder",
        default=os.path.abspath("./sgorm/cache"),
    )

    parser.add_argument(
        "-ef",
        "--entity_folder",
        type=str,
        required=False,
        help="Entity folder",
        default=os.path.abspath("./sgorm/Entity"),
    )

    return parser.parse_args()


def main():
    SgormCli(vars(_args_parser()))


if __name__ == "__main__":
    main()
