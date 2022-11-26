"""Fancoil support."""
import typing

from .._gen.api.default_api import DefaultApi
from .._gen.model.object_info import ObjectInfo
from .._gen.model.object_value_fancoil import ObjectValueFancoil
from .._gen.model.room import Room
from .._gen.model.zone import Zone
from .base import BaseObject


class Fancoil(BaseObject):
    """Represent a fancoil object."""

    def __init__(
        self,
        api: DefaultApi,
        object_info: ObjectInfo,
        zone: typing.Optional[Zone] = None,
        room: typing.Optional[Room] = None,
    ):
        """Create fancoil object."""
        super().__init__(api, object_info, zone=zone, room=room)

    def set_fan_speed(self, fan_speed: float):
        """Set fan on with a specific speed."""
        return self.set_value(ObjectValueFancoil(power=True, fan=fan_speed))

    def get_fan_speed(self):
        """Retrieve current fan speed"""
        return self.get_value().fan

    def is_on(self):
        """Return true if the fan is on"""
        return self.get_value().power

    def switch_on(self):
        """Switch the fan on with existing fan speed"""
        return self.set_value(ObjectValueFancoil(power=True))

    def switch_off(self):
        """Switch the fan on with existing fan speed"""
        return self.set_value(ObjectValueFancoil(power=False))
