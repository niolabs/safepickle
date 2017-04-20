from datetime import datetime, timedelta
from unittest.mock import Mock

from safepickle import dumps, loads, load, dump, PicklingError, UnpicklingError

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

    def test_load_failures(self):
        """ Asserts several load/loads error conditions
        """

        # TypeError to UnpicklingError
        with self.assertRaises(UnpicklingError):
            loads(['invalid'])

        # ValueError to UnpicklingError
        with self.assertRaises(UnpicklingError):
            loads('{invalid}')

        # TypeError to UnpicklingError
        fp = Mock()
        fp.read = Mock(return_value=['invalid'])
        with self.assertRaises(UnpicklingError):
            load(fp)

        # ValueError to UnpicklingError
        fp = Mock()
        fp.read = Mock(return_value='{invalid}')
        with self.assertRaises(UnpicklingError):
            load(fp)

        # assert that an error not related to unpickling is propagated as such
        with self.assertRaises(AttributeError):
            # here an opened file object is expected
            load('not an opened file instance')

    def test_dump_failures(self):
        """ Asserts several dump/dumps error conditions
        """

        # TypeError to PicklingError
        with self.assertRaises(PicklingError):
            dumps(callable)

        # TypeError to PicklingError
        with self.assertRaises(PicklingError):
            # here an opened file object is expected
            dump(callable, Mock())

        # assert that an error not related to pickling is propagated as such
        with self.assertRaises(AttributeError):
            # here an opened file object is expected
            dump("", 'not an opened file instance')
