import json
from .types import TypesManager


class Encoder(json.JSONEncoder):
    def default(self, obj):
        for type_ in TypesManager.get_types():
            if type_.encoder_type(obj):
                return type_.encode(obj)

        if hasattr(obj, "__dict__"):
            return obj.__dict__
        # likely a list, dict, str, unicode, int, float, bool, type()
        return json.JSONEncoder.default(self, obj)


class Decoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self._decoder, *args, **kwargs)

    def _decoder(self, obj):
        for type_ in TypesManager.get_types():
            if type_.decoder_type(obj):
                return type_.decode(obj)

        return obj
