from .interface import EncoderDecoderType


class SetType(EncoderDecoderType):
    def encoder_type(self, obj):
        return isinstance(obj, set)

    def encode(self, obj):
        return {'__set__': True, 'value': list(obj)}

    def decoder_type(self, obj):
        return '__set__' in obj

    def decode(self, obj):
        return set(obj['value'])
