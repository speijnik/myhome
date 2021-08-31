"""Light support."""
import typing

from .._gen.api.default_api import DefaultApi
from .._gen.model.object_info import ObjectInfo
from .._gen.model.object_value_dimmer import ObjectValueDimmer
from .._gen.model.object_value_light import ObjectValueLight
from .._gen.model.room import Room
from .._gen.model.zone import Zone
from .base import BaseObject


class Light(BaseObject):
    """Represent a light."""

    def __init__(
        self,
        api: DefaultApi,
        object_info: ObjectInfo,
        zone: typing.Optional[Zone] = None,
        room: typing.Optional[Room] = None,
    ):
        """Construct light."""
        super().__init__(api, object_info, zone=zone, room=room)

    def switch_on(self):
        """Switch light on."""
        return self.set_value(ObjectValueLight(power=True))

    def switch_off(self):
        """Switch light off."""
        return self.set_value(ObjectValueLight(power=False))

    @property
    def is_on(self):
        """Return True if light is switched on."""
        return self.get_value().power


class Dimmer(Light):
    """Represent a dimmer."""

    def dim(self, percentage: int):
        """Dim to provided percentage."""
        return self.set_value(ObjectValueDimmer(dimmer=percentage))

    def is_on(self):
        """Return True if dimmer is switched on."""
        return self.dimmer_level > 0

    @property
    def dimmer_level(self):
        """Return dimmer level."""
        return self.get_value().dimmer
