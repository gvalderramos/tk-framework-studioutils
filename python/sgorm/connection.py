from .decorators import singleton
import shotgun_api3


@singleton
class Connection(object):
    def __init__(self):
        self.__sg = None

    @property
    def shotgun(self):
        return self.__sg

    @shotgun.setter
    def shotgun(self, auth):
        if isinstance(auth, shotgun_api3.Shotgun):
            self.__sg = auth
            return

        if not isinstance(auth, SgAuth):
            raise RuntimeError(
                "Auth parameter must be a SgAuth instance, not a '{}' instance".format(
                    auth.__class__.__name__
                )
            )
        self.__sg = auth.connect()

    def find(self, query, ret):
        pass

    def find_one(self, query, ret):
        pass

    def create(self, data):
        pass

    def batch(self, data):
        pass


class SgAuth(object):
    def __init__(
        self,
        host=None,
        user=None,
        user_password=None,
        user_token=None,
        script_name=None,
        script_pass=None,
    ):
        self.__host = host
        self.__user = user
        self.__user_password = user_password
        self.__user_token = user_token
        self.__script_name = script_name
        self.__script_pass = script_pass

    @property
    def user_auth_method(self):
        return (
            True
            if self.__user and (self.__user_password or self.__user_token)
            else False
        )

    @property
    def script_auth_method(self):
        return True if self.__script_name and self.__script_pass else False

    def connect(self):
        sg = None
        if self.user_auth_method:
            try:
                if not self.__user_token:
                    sg = shotgun_api3.Shotgun(
                        self.__host, login=self.__user, password=self.__user_password
                    )
                elif self.__user_token:
                    sg = shotgun_api3.Shotgun(
                        self.__host, login=self.__user, token=self.__user_token
                    )
                else:
                    raise RuntimeError(
                        "You must provide a valid user authentication or script authentication."
                    )
            except Exception as e:
                raise RuntimeError("Error while connect with Shotgun - {}".format(e))
        elif self.script_auth_method:
            try:
                sg = shotgun_api3.Shotgun(
                    self.__host,
                    script_name=self.__script_name,
                    api_key=self.__script_pass,
                )
            except Exception as e:
                raise RuntimeError("Error while connect with Shotgun - {}".format(e))

        return sg
