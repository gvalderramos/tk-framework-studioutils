import Model


class Field(object):
    def __init__(self, field_name, value):
        self.__field_name = field_name
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        self.__value = v

    def __str__(self):
        return str("<Field Class - {}: {}>".format(self.__field_name, self.value))

    def __get_other_inst_value(self, inst):
        if isinstance(inst, self.__class__):
            return inst.value
        elif isinstance(inst, Model.Entity):
            return {"type": inst.type.value, "id": inst.id.value}
        else:
            return inst

    def __add__(self, inst):
        self.__value += self.__get_other_inst_value(inst)
        return self.__value

    def __sub__(self, inst):
        self.__value -= self.__get_other_inst_value(inst)
        return self.__value

    def __mul__(self, inst):
        self.__value *= self.__get_other_inst_value(inst)
        return self.__value

    def __div__(self, inst):
        self.__value /= self.__get_other_inst_value(inst)
        return self.__value

    def __eq__(self, inst):
        return [self.__field_name, "is", self.__get_other_inst_value(inst)]

    def __ne__(self, inst):
        return [self.__field_name, "is_not", self.__get_other_inst_value(inst)]

    def __gt__(self, inst):
        return [self.__field_name, "greater_than", self.__get_other_inst_value(inst)]

    def __lt__(self, inst):
        return [self.__field_name, "less_than", self.__get_other_inst_value(inst)]

    def contains(self, inst):
        v = []
        if isinstance(inst, list):
            v = [i.value for i in inst] if isinstance(inst[0], Field) else inst
        else:
            v = self.__get_other_inst_value(inst)
        op = "in" if isinstance(v, list) else "contains"
        return [self.__field_name, op, v]

    def not_contains(self, inst):
        if isinstance(inst, list):
            v = [i.value for i in inst] if isinstance(inst[0], Field) else inst
        else:
            v = self.__get_other_inst_value(inst)
        op = "not_in" if isinstance(v, list) else "not_contains"
        return [self.__field_name, op, v]

    def start_with(self, inst):
        return [self.__field_name, "starts_with", self.__get_other_inst_value(inst)]

    def ends_with(self, inst):
        return [self.__field_name, "ends_with", self.__get_other_inst_value(inst)]

    def between(self, min_value, max_value):
        min_value = self.__get_other_inst_value(min_value)
        max_value = self.__get_other_inst_value(max_value)
        return [self.__field_name, "between", min_value, max_value]

    def not_between(self, min_value, max_value):
        min_value = self.__get_other_inst_value(min_value)
        max_value = self.__get_other_inst_value(max_value)
        return [self.__field_name, "not_between", min_value, max_value]

    def in_last(self, qnt, mtd):
        valid_attr = ["HOUR", "DAY", "WEEK", "MONTH", "YEAR"]
        mtd = mtd.upper()
        if mtd not in valid_attr:
            raise AttributeError("mtd attribute not in {}".format(valid_attr))

        if not isinstance(qnt, int):
            raise AttributeError("qnt attribute must be a int value")

        return [self.__field_name, "in_last", qnt, mtd]

    def in_next(self, qnt, mtd):
        valid_attr = ["HOUR", "DAY", "WEEK", "MONTH", "YEAR"]
        mtd = mtd.upper()
        if mtd not in valid_attr:
            raise AttributeError("mtd attribute not in {}".format(valid_attr))

        if not isinstance(qnt, int):
            raise AttributeError("qnt attribute must be a int value")

        return [self.__field_name, "in_next", qnt, mtd]

    def type_is(self, t):
        if not isinstance(t, str):
            raise AttributeError("'t' attribute must be a string value")

        return [self.__field_name, "type_is", t]

    def type_is_not(self, t):
        if not isinstance(t, str):
            raise AttributeError("'t' attribute must be a string value")

        return [self.__field_name, "type_is_not", t]

    def in_calendar_day(self, offset):
        offset = self.__get_other_inst_value(offset)
        return [self.__field_name, "in_calendar_day", offset]

    def in_calendar_week(self, offset):
        offset = self.__get_other_inst_value(offset)
        return [self.__field_name, "in_calendar_week", offset]

    def in_calendar_month(self, offset):
        offset = self.__get_other_inst_value(offset)
        return [self.__field_name, "in_calendar_month", offset]

    def name_contains(self, pattern):
        pattern = self.__get_other_inst_value(pattern)
        return [self.__field_name, "name_contains", pattern]

    def name_not_contains(self, pattern):
        pattern = self.__get_other_inst_value(pattern)
        return [self.__field_name, "name_not_contains", pattern]

    def name_starts_with(self, pattern):
        pattern = self.__get_other_inst_value(pattern)
        return [self.__field_name, "name_starts_with", pattern]

    def name_ends_with(self, pattern):
        pattern = self.__get_other_inst_value(pattern)
        return [self.__field_name, "name_ends_with", pattern]
