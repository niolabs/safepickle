from unittest import TestCase

from safepickle.types.set import SetType
from safepickle.encoding import encode, decode


class TestSet(TestCase):

    def test_list(self):
        """ Asserts set type is handled as expected
        """
        obj = {1, 2}
        type_ = SetType()
        encoding = type_.encode(obj, encode)
        decoding = decode(encoding)

        self.assertEqual(obj, decoding)
