from datetime import datetime

from .interface import EncoderDecoderType


class DatetimeType(EncoderDecoderType):
    def is_type(self, obj):
        return isinstance(obj, datetime) or \
               (isinstance(obj, dict) and '__datetime__' in obj)

    def encode(self, obj):
        return {'__datetime__': True,
                'value': {'year': obj.year,
                          'month': obj.month,
                          'day': obj.day,
                          'hour': obj.hour,
                          'minute': obj.minute,
                          'second': obj.second,
                          'microsecond': obj.microsecond}}

    def decode(self, obj):
        return datetime(**obj['value'])
