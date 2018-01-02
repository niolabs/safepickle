from unittest import TestCase
from collections import defaultdict

from safepickle.types import TypesManager
from datetime import timedelta, datetime


class TestManager(TestCase):

    def test_get_type(self):
        types = [int, bool, float, str,
                 bytearray, bytes, datetime, defaultdict, dict,
                 list, set, timedelta, tuple]
        for type1 in types:
            type2 = TypesManager.get_type(TypesManager.get_str_type(type1))
            self.assertEqual(type1, type2)
