from unittest import TestCase

from safepickle.types.list import ListType
from safepickle.encoding import encode, decode


class TestList(TestCase):

    def test_list(self):
        """ Asserts list type is handled as expected
        """
        obj = [1, 2, "some text"]
        type_ = ListType()
        encoding = type_.encode(obj, encode)
        decoding = decode(encoding)

        self.assertEqual(obj, decoding)
