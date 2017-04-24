from unittest.mock import Mock, patch
from unittest import TestCase

from safepickle import dumps, PicklingError


from safepickle.types import TypesManager
from safepickle.types.instance import InstanceType


class TestEncoding(TestCase):

    def test_unhandled(self):
        """ Asserts that an unhandled type raises a PicklingError
        """
        # find instance type
        for type_ in TypesManager.get_types():
            if isinstance(type_, InstanceType):
                # patch can_encode so that no satisfying type is found
                with patch.object(type_, "can_encode") as can_encode_patch:
                    can_encode_patch.return_value = False
                    with self.assertRaises(PicklingError):
                        dumps(Mock())
