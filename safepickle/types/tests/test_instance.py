from unittest import TestCase

from safepickle.types.instance import InstanceType
from safepickle.encoding import encode, decode


class TestInstance(TestCase):

    def test_instance(self):
        """ Asserts instance type is handled as expected
        """

        class ClassToPersist(object):
            def __init__(self):
                self._int = 1
                self._float = 1.0

        obj = ClassToPersist()
        type_ = InstanceType()
        encoding = type_.encode(obj, encode)
        decoding = decode(encoding)

        self.assertDictEqual(obj.__dict__, decoding)
