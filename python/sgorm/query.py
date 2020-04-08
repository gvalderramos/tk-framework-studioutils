from .connection import Connection


class Query(object):
    def __init__(self, model):
        self._filters = []
        self._model = model
        self._select = []
        self._conn = Connection()
        self.__valid_methods = ["find", "find_one", "create", "update"]

    @property
    def select(self):
        return self._select if self._select else ["type", "id"]

    @select.setter
    def select(self, value):
        if value is not None:
            self._select = value

    @property
    def method(self):
        return getattr(self._conn.shotgun, self._method)

    @method.setter
    def method(self, value):
        if value not in self.__valid_methods:
            raise RuntimeError(
                "Method property must be: {}".format(self.__valid_methods)
            )
        self._method = value

    def where(self, filters):
        if not isinstance(filters, list) or not isinstance(filters, tuple):
            filters = [filters]

        self._filters += filters
        return self._resolve()

    def _resolve(self):
        qi = QueryInteractor(
            self.method(self._model.type.value, self._filters[0], self.select),
            self._model.__class__,
        )
        return qi


class QueryInteractor(object):
    def __init__(self, obj_list, model):
        self.__all_objs = []
        for obj in obj_list:
            new_obj = model()
            self.__all_objs.append(new_obj)
            for key, value in obj.iteritems():
                attr = getattr(new_obj, key)
                attr.value = value

    def __iter__(self):
        for obj in self.__all_objs:
            yield obj
