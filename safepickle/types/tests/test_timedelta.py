from unittest import TestCase

from datetime import timedelta
from safepickle.types.timedelta import TimedeltaType
from safepickle.encoding import encode, decode


class TestTimedelta(TestCase):

    def test_timedelta(self):
        """ Asserts timedelta type is handled as expected
        """
        obj = timedelta(days=1, seconds=2, microseconds=3)
        type_ = TimedeltaType()
        encoding = type_.encode(obj, encode)
        decoding = decode(encoding)

        self.assertEqual(obj, decoding)
