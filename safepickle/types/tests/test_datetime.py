from unittest import TestCase

from datetime import datetime
from safepickle.types.datetime_ import DatetimeType
from safepickle.encoding import encode, decode


class TestDatetime(TestCase):

    def test_datetime(self):
        """ Asserts datetime type is handled as expected
        """
        obj = datetime(year=1, month=2, day=3,
                       hour=4, minute=5, second=6, microsecond=7)
        type_ = DatetimeType()
        encoding = type_.encode(obj, encode)
        decoding = decode(encoding)

        self.assertEqual(obj, decoding)
