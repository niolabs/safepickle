from datetime import timedelta

from .interface import EncoderDecoderType


class TimedeltaType(EncoderDecoderType):

    def is_type(self, obj):
        return isinstance(obj, timedelta) or \
               (isinstance(obj, dict) and '__timedelta__' in obj)

    def encode(self, obj):
        return {'__timedelta__': True,
                'value': {'days': obj.days,
                          'seconds': obj.seconds,
                          'microseconds': obj.microseconds}}

    def decode(self, obj):
        return timedelta(**obj['value'])
