from datetime import datetime

from .interface import EncoderDecoderType


class DatetimeType(EncoderDecoderType):
    def encoder_type(self, obj):
        return isinstance(obj, datetime)

    def encode(self, obj):
        return {'__datetime__': True,
                'value': {'year': obj.year,
                          'month': obj.month,
                          'day': obj.day,
                          'hour': obj.hour,
                          'minute': obj.minute,
                          'second': obj.second,
                          'microsecond': obj.microsecond}}

    def decoder_type(self, obj):
        return '__datetime__' in obj

    def decode(self, obj):
        return datetime(**obj['value'])
