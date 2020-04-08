from . import datatype
from . import query


class Entity(object):
    def __init__(self, entity_type=None, entity_id=None):
        self._to_commit = {}
        self._query = query.Query(self)
        # Default fields
        self.type = datatype.Field("type", entity_type)
        self.id = datatype.Field("id", entity_id)
        self.updated_at = datatype.Field("updated_at", None)
        self.created_by = datatype.Field("created_by", None)
        self.created_at = datatype.Field("created_at", None)
        self.open_notes = datatype.Field("open_notes", None)
        self.notes = datatype.Field("notes", None)

    def __eq__(self, other):
        return [self.type.value, "is", {"type": other.type.value, "id": other.id.value}]

    def __ne__(self, other):
        return [
            self.type.value,
            "not_is",
            {"type": other.type.value, "id": other.id.value},
        ]

    def find(self, select=None):
        self._query.select = select
        self._query.method = "find"
        return self._query
