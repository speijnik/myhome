"""Thermostat support."""
import typing

from ..gen import (  # type: ignore
    DefaultApi,
    ObjectInfo,
    ObjectValueThermostat,
    Room,
    Zone,
)
from .base import BaseObject


class Thermostat(BaseObject):
    """Represent a thermostat."""

    def __init__(
        self,
        api: DefaultApi,
        object_info: ObjectInfo,
        zone: typing.Optional[Zone] = None,
        room: typing.Optional[Room] = None,
    ):
        """Create thermostat object."""
        super().__init__(api, object_info, zone=zone, room=room)

    def set_temperature(self, temperature: float):
        """Set thermostat temperature."""
        return self.set_value(ObjectValueThermostat(setpoint=temperature))

    def get_temperature(self):
        """Retrieve thermostat temperature."""
        value = self.get_value()
        return value.setpoint
