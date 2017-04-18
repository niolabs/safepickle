import json

from .encoding import Encoder, Decoder
from pickle import PickleError, PicklingError, UnpicklingError


def load(file):
    """ Read a json object representation from the open file object file. 
    
    Args:
        file: file object
        
    Returns:
        object representation as a dict
    """
    try:
        return json.load(file, cls=Decoder)
    except Exception as e:
        raise UnpicklingError(str(e))


def dump(obj, file, **kwargs):
    """ Write a json representation to the open file object
    
    Args:
        obj: object to represent  
        file: open file object 
    """
    # apply json defaults if not present
    if 'indent' not in kwargs:
        kwargs['indent'] = 4
    if 'separators' not in kwargs:
        kwargs['separators'] = (',', ': ')

    try:
        return json.dump(obj, file, cls=Encoder, **kwargs)
    except Exception as e:
        raise PicklingError(str(e))


def loads(str_obj):
    """ Read a json object representation from the open file object file. 

    Args:
        str_obj: object as a string

    Returns:
        object representation as a dict
    """
    try:
        return json.loads(str_obj, cls=Decoder)
    except Exception as e:
        raise UnpicklingError(str(e))


def dumps(obj):
    """ Write a json representation of object to string

    Args:
        obj: object to represent
          
    Returns:
        object as a string
    """
    try:
        return json.dumps(obj, cls=Encoder)
    except Exception as e:
        raise PicklingError(str(e))
