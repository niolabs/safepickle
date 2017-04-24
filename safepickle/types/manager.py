from .set import SetType
from .tuple import TupleType
from .dict import DictType
from .list import ListType
from .instance import InstanceType
from .datetime_ import DatetimeType
from .timedelta import TimedeltaType


class _TypesManager(object):
    """ Allows the definition of the types supported by the package
    """
    def __init__(self):
        self._types = [
            SetType(),
            TupleType(),
            DictType(),
            ListType(),
            DatetimeType(),
            TimedeltaType(),
            InstanceType()
        ]

    def get_types(self):
        return self._types

# Singleton instance to _TypesManager
TypesManager = _TypesManager()
