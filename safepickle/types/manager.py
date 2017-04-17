from .set import SetType
from .datetime_ import DatetimeType
from .timedelta import TimedeltaType


class _TypesManager(object):
    """ Allows the definition of the types supported by the package
    """
    def __init__(self):
        self._types = [
            SetType(),
            DatetimeType(),
            TimedeltaType()
        ]

    def get_types(self):
        return self._types

# Singleton instance to _TypesManager
TypesManager = _TypesManager()
