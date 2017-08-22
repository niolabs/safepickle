
from safepickle.types.dict import DictType
from safepickle.encoding import encode, decode

from unittest import TestCase


class TestDict(TestCase):

    def test_dict_numbered_keys(self):
        """ Asserts dict with numbered keys
        """
        obj = {
            1: 1, 2: 2
        }
        type_ = DictType()
        encoding = type_.encode(obj, encode)
        decoding = decode(encoding)
        self.assertDictEqual(obj, decoding)

    def test_dict_non_numbered_keys(self):
        """ Asserts dict with non-numbered keys
        """
        obj = {
            "1": 1, "2": 2
        }
        type_ = DictType()
        encoding = type_.encode(obj, encode)
        decoding = decode(encoding)
        self.assertDictEqual(obj, decoding)
