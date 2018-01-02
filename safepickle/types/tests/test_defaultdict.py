from collections import defaultdict

from datetime import timedelta, datetime

from safepickle.types.defaultdict import DefaultDictType
from safepickle.encoding import encode, decode

from unittest import TestCase


class TestDefaultDict(TestCase):

    def test_defaultdict(self):
        _types = [int, bool, float, str,
                  bytearray, bytes, datetime, defaultdict, dict,
                  list, set, timedelta, tuple]
        for _type in _types:
            obj = defaultdict(_type)
            type_ = DefaultDictType()
            encoding = type_.encode(obj, encode)
            decoding = decode(encoding)
            self.assertDictEqual(obj, decoding)
            self.assertEqual(obj.default_factory, decoding.default_factory)
