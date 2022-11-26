import typing

from myhome._gen.api.default_api import DefaultApi
from myhome._gen.model.object_info import ObjectInfo
from myhome._gen.model.object_value_towel_warmer import ObjectValueTowelWarmer
from myhome._gen.model.room import Room
from myhome._gen.model.zone import Zone
from myhome.object.base import BaseObject


class TowelWarmer(BaseObject):
    """Represent a towel warmer."""

    def __init__(
        self,
        api: DefaultApi,
        object_info: ObjectInfo,
        zone: typing.Optional[Zone] = None,
        room: typing.Optional[Room] = None,
    ):
        """Construct towel warmer."""
        super().__init__(api, object_info, zone=zone, room=room)

    def switch_on(self):
        """Switch towel warmer on."""
        return self.set_value(ObjectValueTowelWarmer(power=True))

    def switch_off(self):
        """Switch towel warmer off."""
        return self.set_value(ObjectValueTowelWarmer(power=False))

    @property
    def is_on(self):
        """Return True if towel warmer is switched on."""
        return self.get_value().power
