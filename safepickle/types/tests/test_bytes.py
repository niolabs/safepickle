from unittest import TestCase

from safepickle.types.bytes import BytesType
from safepickle.encoding import encode, decode


class TestBytes(TestCase):

    def test_bytes(self):
        """ Asserts bytes type is handled as expected
        """
        obj = bytes([1, 2, 3])
        type_ = BytesType()
        encoding = type_.encode(obj, encode)
        decoding = decode(encoding)

        self.assertEqual(obj, decoding)

    def test_string_encoding_as_bytes(self):
        """ Asserts an encoded string can be encoded/decoded accordingly
        """
        obj = "some string".encode()
        type_ = BytesType()
        encoding = type_.encode(obj, encode)
        decoding = decode(encoding)

        self.assertEqual(obj, decoding)
