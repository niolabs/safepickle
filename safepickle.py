import json

from .encoding import Encoder, Decoder


def load(file):
    return json.load(file, cls=Decoder)


def dump(obj, file, **kwargs):
    # apply json defaults if not present
    if 'indent' not in kwargs:
        kwargs['indent'] = 4
    if 'separators' not in kwargs:
        kwargs['separators'] = (',', ': ')

    return json.dump(obj, file, cls=Encoder, **kwargs)


def loads(str_obj):
    return json.loads(str_obj, cls=Decoder)


def dumps(obj):
    return json.dumps(obj, cls=Encoder)
