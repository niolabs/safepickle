from datetime import datetime, timedelta
from tempfile import mkstemp
from unittest.mock import Mock

from safepickle import dumps, loads, load, dump, PicklingError, UnpicklingError

from unittest import TestCase
import os


class TestSafepickle(TestCase):

    def test_instance_roundtrip(self):
        class ClassToPersist(object):
            def __init__(self):
                self._list = [1, 2]
                self._dict = {"one": 1}
                self._set = {1, 2}
                self._tuple = (1, 2),
                self._int = 1
                self._float = 1.0
                self._datetime = datetime(year=1, month=1, day=1)
                self._timedelta = timedelta(days=1)

        instance = ClassToPersist()

        instance_as_bytes = dumps(instance)
        from_instance = loads(instance_as_bytes)
        for key, value in instance.__dict__.items():
            self.assertEqual(from_instance[key], value)

    def test_load_failures(self):
        """ Asserts several load/loads error conditions
        """

        # Invalid type (no bytes passed in)
        with self.assertRaises(AttributeError):
            loads('{}')

        # ValueError to UnpicklingError
        with self.assertRaises(UnpicklingError):
            loads(b'[invalid]')

        # ValueError to UnpicklingError
        with self.assertRaises(UnpicklingError):
            loads(b'{invalid}')

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

    def test_dict_roundtrip(self):
        """ Asserts dumps/loads dealing with bytes
        """
        obj = {
            "_list": [1, 2],
            "_dict": {"one": 1},
            "_set": {1, 2},
            "_tuple": (1, 2),
            "_int": 1,
            "_float": 1.0,
            "_datetime": datetime(year=1, month=1, day=1),
            "_timedelta": timedelta(days=1)
        }
        obj_as_bytes = dumps(obj)
        from_obj = loads(obj_as_bytes)

        self.assertDictEqual(obj, from_obj)
        self.assertIsInstance(obj_as_bytes, bytes)

    def test_save_load_roundtrip(self):
        """ Asserts dump/load file saving/loading
        """
        obj = {
            "_list": [1, 2],
            "_dict": {"one": 1},
            "_set": {1, 2},
            "_tuple": (1, 2),
            "_int": 1,
            "_float": 1.0,
            "_datetime": datetime(year=1, month=1, day=1),
            "_timedelta": timedelta(days=1)
        }
        fd, temp_path = mkstemp()
        try:
            with open(temp_path, 'w') as fd:
                dump(obj, fd)

            self.assertTrue(os.path.isfile(temp_path))
            with open(temp_path, 'r') as fd:
                from_file = load(fd)
            self.assertDictEqual(obj, from_file)
        finally:
            os.remove(temp_path)

    def test_converted_keys(self):
        """ Asserts that keys can be instances of types that are converted
        """
        obj = {
            (1, 2): 3,
            datetime.now(): 1,
            timedelta(seconds=1): "timedelta",
            datetime.now(): {datetime.now(): datetime.now()}
        }
        obj_as_bytes = dumps(obj)
        from_obj = loads(obj_as_bytes)

        self.assertDictEqual(obj, from_obj)
        self.assertIsInstance(obj_as_bytes, bytes)

        # assert that there is no difference when dumping to file
        fd, temp_path = mkstemp()
        try:
            with open(temp_path, 'w') as fd:
                dump(obj, fd)

            with open(temp_path, 'r') as fd:
                from_file = load(fd)

            self.assertDictEqual(obj, from_file)

        finally:
            os.remove(temp_path)

    def test_numeric_keys(self):
        """ Asserts that keys can be numeric
        """
        obj = {
            None: 1,
            1: 2,
            1.1: 1.2
        }
        s = dumps(obj)
        from_s = loads(s)
        self.assertEqual(obj, from_s)

        # assert that there is no difference when dumping to file
        fd, temp_path = mkstemp()
        try:
            with open(temp_path, 'w') as fd:
                dump(obj, fd)

            with open(temp_path, 'r') as fd:
                from_file = load(fd)

            self.assertDictEqual(obj, from_file)

        finally:
            os.remove(temp_path)
