from unittest import TestCase

from safepickle.types.bytearray import ByteArrayType
from safepickle.encoding import encode, decode


class TestByteArray(TestCase):

    def test_bytearray(self):
        """ Asserts bytearray type is handled as expected
        """
        obj = bytearray([1, 2, 3])
        type_ = ByteArrayType()
        encoding = type_.encode(obj, encode)
        decoding = decode(encoding)

        self.assertEqual(obj, decoding)
