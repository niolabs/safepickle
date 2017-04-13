from .set import SetType
from .datetime_ import DatetimeType
from .timedelta import TimedeltaType


class TypesManager(object):
    _types = []

    @classmethod
    def get_types(cls):
        if not cls._types:
            cls._types = [
                SetType(),
                DatetimeType(),
                TimedeltaType()
            ]

        return cls._types
