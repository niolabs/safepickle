from datetime import datetime, timedelta
from safepickle import dumps, loads

from unittest import TestCase


class TestSafepickle(TestCase):

    def test_roundtrip(self):
        class ClassToPersist(object):
            def __init__(self):
                self._list = [1, 2]
                self._dict = {"one": 1}
                self._set = {1, 2}
                self._int = 1
                self._float = 1.0
                self._datetime = datetime(year=1, month=1, day=1)
                self._timedelta = timedelta(days=1)

        instance = ClassToPersist()

        instance_as_str = dumps(instance)
        from_instance = loads(instance_as_str)
        for key, value in instance.__dict__.items():
            self.assertEqual(from_instance[key], value)
