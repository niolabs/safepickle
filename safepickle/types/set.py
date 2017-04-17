from .interface import EncoderDecoderType


class SetType(EncoderDecoderType):
    def is_type(self, obj):
        return isinstance(obj, set)or \
               (isinstance(obj, dict) and '__set__' in obj)

    def encode(self, obj):
        return {'__set__': True, 'value': list(obj)}

    def decode(self, obj):
        return set(obj['value'])
