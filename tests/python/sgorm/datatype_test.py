import os
import sys
import json
import unittest


class TestField(unittest.TestCase):
    def setUp(self):
        try:
            from python import sgorm

            self.sgorm = sgorm
        except Exception as e:
            self.fail("Module sgorm import error, because: {}".format(e))

    def test_value_getter_and_setter(self):
        field1 = self.sgorm.Field("code", "Asset_01")
        field2 = self.sgorm.Field("code", "Asset_02")

        self.assertEqual(field1.value, "Asset_01")
        self.assertEqual(field2.value, "Asset_02")

        field1.value = "Other_Asset_01"
        field2.value = "Other_Asset_02"

        self.assertEqual(field1.value, "Other_Asset_01")
        self.assertEqual(field2.value, "Other_Asset_02")

    def test_eq_operator(self):
        field1 = self.sgorm.Field("some_int1", 1)
        field2 = self.sgorm.Field("some_int2", 2)

        espected = ["some_int1", "is", 2]
        self.assertEqual(field1 == field2, espected)

    def test_not_eq_operator(self):
        field1 = self.sgorm.Field("some_int1", 1)
        field2 = self.sgorm.Field("some_int2", 2)

        espected = ["some_int1", "is_not", 2]
        self.assertEqual(field1 != field2, espected)

    def test_less_than_operator(self):
        field1 = self.sgorm.Field("some_int1", 1)
        field2 = self.sgorm.Field("some_int2", 2)

        espected = ["some_int1", "less_than", 2]
        self.assertEqual(field1 < field2, espected)

    def test_greater_than_operator(self):
        field1 = self.sgorm.Field("some_int1", 1)
        field2 = self.sgorm.Field("some_int2", 2)

        espected = ["some_int1", "greater_than", 2]
        self.assertEqual(field1 > field2, espected)

    def test_contains_simple_str_operator(self):
        field1 = self.sgorm.Field("some_int1", 1)

        espected = ["some_int1", "contains", "some_string"]
        self.assertEqual(field1.contains("some_string"), espected)

    def test_contains_array_operator(self):
        field1 = self.sgorm.Field("some_int1", 1)
        field2 = self.sgorm.Field("some_int2", 2)
        field3 = self.sgorm.Field("some_int3", 3)

        espected = ["some_int1", "in", [2, 3]]
        self.assertEqual(field1.contains([field2, field3]), espected)

    def test_not_contains_simple_str_operator(self):
        field1 = self.sgorm.Field("some_int1", 1)

        espected = ["some_int1", "not_contains", "some_string"]
        self.assertEqual(field1.not_contains("some_string"), espected)

    def test_not_contains_array_operator(self):
        field1 = self.sgorm.Field("some_int1", 1)
        field2 = self.sgorm.Field("some_int2", 2)
        field3 = self.sgorm.Field("some_int3", 3)

        espected = ["some_int1", "not_in", [2, 3]]
        self.assertEqual(field1.not_contains([field2, field3]), espected)

    def test_start_with(self):
        field1 = self.sgorm.Field("some_attr", "code_54")

        expected = ["some_attr", "starts_with", "code"]
        self.assertEqual(field1.start_with("code"), expected)

    def test_ends_with(self):
        field1 = self.sgorm.Field("some_attr", "code_54")

        expected = ["some_attr", "ends_with", "code"]
        self.assertEqual(field1.ends_with("code"), expected)

    def test_between_with(self):
        field1 = self.sgorm.Field("some_attr", 1)

        expected = ["some_attr", "between", 0, 3]
        self.assertEqual(field1.between(0, 3), expected)

    def test_not_between_with(self):
        field1 = self.sgorm.Field("some_attr", 1)

        expected = ["some_attr", "not_between", 0, 3]
        self.assertEqual(field1.not_between(0, 3), expected)

    def test_in_last(self):
        field1 = self.sgorm.Field("some_attr", 1)

        expected = ["some_attr", "in_last", 1, "DAY"]
        self.assertEqual(field1.in_last(1, "day"), expected)
        self.assertEqual(field1.in_last(1, "DAY"), expected)

    def test_in_next(self):
        field1 = self.sgorm.Field("some_attr", 1)

        expected = ["some_attr", "in_next", 1, "DAY"]
        self.assertEqual(field1.in_next(1, "day"), expected)
        self.assertEqual(field1.in_next(1, "DAY"), expected)

    def test_type_is(self):
        field1 = self.sgorm.Field("some_attr", 1)

        expected = ["some_attr", "type_is", "Asset"]
        self.assertEqual(field1.type_is("Asset"), expected)

    def test_type_is_not(self):
        field1 = self.sgorm.Field("some_attr", 1)

        expected = ["some_attr", "type_is_not", "Asset"]
        self.assertEqual(field1.type_is_not("Asset"), expected)

    def test_in_calendar_week(self):
        field1 = self.sgorm.Field("some_attr", 1)

        expected = ["some_attr", "in_calendar_week", 2]
        self.assertEqual(field1.in_calendar_week(2), expected)

    def test_in_calendar_day(self):
        field1 = self.sgorm.Field("some_attr", 1)

        expected = ["some_attr", "in_calendar_day", 2]
        self.assertEqual(field1.in_calendar_day(2), expected)

    def test_in_calendar_month(self):
        field1 = self.sgorm.Field("some_attr", 1)

        expected = ["some_attr", "in_calendar_month", 2]
        self.assertEqual(field1.in_calendar_month(2), expected)

    def test_name_contains(self):
        field1 = self.sgorm.Field("some_attr", "code_1")

        expected = ["some_attr", "name_contains", "code"]
        self.assertEqual(field1.name_contains("code"), expected)

    def test_name_not_contains(self):
        field1 = self.sgorm.Field("some_attr", "code_1")

        expected = ["some_attr", "name_not_contains", "code"]
        self.assertEqual(field1.name_not_contains("code"), expected)

    def test_name_starts_with(self):
        field1 = self.sgorm.Field("some_attr", "code_1")

        expected = ["some_attr", "name_starts_with", "code"]
        self.assertEqual(field1.name_starts_with("code"), expected)

    def test_name_ends_with(self):
        field1 = self.sgorm.Field("some_attr", "code_1")

        expected = ["some_attr", "name_ends_with", "code"]
        self.assertEqual(field1.name_ends_with("code"), expected)
