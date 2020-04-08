"""
This file provide a collection of decorators.
"""


def singleton(cls):
    """
    Provide a decorator with the purpose of making a class a singleton class

    :type cls: Object
    :param cls: A class instance

    :return: The singleton instance
    """
    instances = {}

    def instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return instance
