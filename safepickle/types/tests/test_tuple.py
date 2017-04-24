from unittest import TestCase

from safepickle.types.tuple import TupleType
from safepickle.encoding import encode, decode


class TestSet(TestCase):

    def test_list(self):
        """ Asserts tuple type is handled as expected
        """
        obj = (1, 2)
        type_ = TupleType()
        encoding = type_.encode(obj, encode)
        decoding = decode(encoding)

        self.assertEqual(obj, decoding)
