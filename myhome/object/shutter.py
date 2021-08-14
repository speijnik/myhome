"""Shutter support."""
from . import BaseObject
from ..gen import DefaultApi, ObjectInfo, ObjectValueShutter  # type: ignore


class Shutter(BaseObject):
    """Represent a shutter."""

    def __init__(self, api: DefaultApi, object_info: ObjectInfo):
        """Construct shutter."""
        super().__init__(api, object_info)

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
