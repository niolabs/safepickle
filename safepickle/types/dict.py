from .interface import EncoderDecoderType


class DictType(EncoderDecoderType):
    def can_encode(self, obj):
        return isinstance(obj, dict)

    def encode(self, obj, encode_fn):
        if all(isinstance(k, str) for k in obj):
            return {k: encode_fn(v) for k, v in obj.items()}
        return {"__dct__": {encode_fn(k): encode_fn(v) for k, v in obj.items()}}

    def can_decode(self, obj):
        return isinstance(obj, dict) and '__dct__' in obj

    def decode(self, obj):
        return obj['__dct__']
