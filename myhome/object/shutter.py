"""Shutter support."""
import typing

from .._gen.api.default_api import DefaultApi
from .._gen.model.object_info import ObjectInfo
from .._gen.model.object_value_shutter import ObjectValueShutter
from .._gen.model.room import Room
from .._gen.model.zone import Zone
from .base import BaseObject


class Shutter(BaseObject):
    """Represent a shutter."""

    def __init__(
        self,
        api: DefaultApi,
        object_info: ObjectInfo,
        zone: typing.Optional[Zone] = None,
        room: typing.Optional[Room] = None,
    ):
        """Construct shutter."""
        super().__init__(api, object_info, zone=zone, room=room)

    def move_up(self):
        """Shortcut for moving shutter up."""
        return self.move_shutter("UP")

    def move_stop(self):
        """Shortcut for stopping shutter movement."""
        return self.move_shutter("STOP")

    def move_down(self):
        """Shortcut for moving shutter down."""
        return self.move_shutter("DOWN")

    def move_shutter(self, direction: str):
        """Move shutter."""
        return self.set_value(ObjectValueShutter(move=direction))

    def get_shutter_move(self):
        """Return shutter move value."""
        return self.get_value().move
