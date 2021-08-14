"""Thermostat support."""

from ..gen import DefaultApi, ObjectInfo, ObjectValueThermostat  # type: ignore
from .base import BaseObject


class Thermostat(BaseObject):
    """Represent a thermostat."""

    def __init__(self, api: DefaultApi, object_info: ObjectInfo):
        """Create thermostat object."""
        super().__init__(api, object_info)

    def set_temperature(self, temperature: float):
        """Set thermostat temperature."""
        return self.set_value(ObjectValueThermostat(setpoint=temperature))

    def get_temperature(self):
        """Retrieve thermostat temperature."""
        value = self.get_value()
        return value.setpoint
