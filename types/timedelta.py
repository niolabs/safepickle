from datetime import timedelta

from .interface import EncoderDecoderType


class TimedeltaType(EncoderDecoderType):

    def encoder_type(self, obj):
        return isinstance(obj, timedelta)

    def encode(self, obj):
        return {'__timedelta__': True,
                'value': {'days': obj.days,
                          'seconds': obj.seconds,
                          'microseconds': obj.microseconds}}

    def decoder_type(self, obj):
        return '__timedelta__' in obj

    def decode(self, obj):
        return timedelta(**obj['value'])
