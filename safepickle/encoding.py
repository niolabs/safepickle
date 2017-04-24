from .types import TypesManager


def encode(obj):

    # handle basic types separately
    if obj is None or isinstance(obj, (bool, int, float, str)):
        return obj

    for type_ in TypesManager.get_types():
        if type_.can_encode(obj):
            return type_.encode(obj, encode)

    raise TypeError("Type: '{}' is not supported".format(type(obj)))


def decode(dct):
    for type_ in TypesManager.get_types():
        if type_.can_decode(dct):
            return type_.decode(dct)

    return dct
