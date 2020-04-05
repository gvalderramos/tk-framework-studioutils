import DataType
import Query


class Entity(object):
    def __init__(self, entity_type=None, entity_id=None):
        self._to_commit = {}
        self._query = Query.Query(self)
        # Default fields
        self.type = DataType.Field("type", entity_type)
        self.id = DataType.Field("id", entity_id)
        self.updated_at = DataType.Field("updated_at", None)
        self.created_by = DataType.Field("created_by", None)
        self.created_at = DataType.Field("created_at", None)
        self.open_notes = DataType.Field("open_notes", None)
        self.notes = DataType.Field("notes", None)

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
