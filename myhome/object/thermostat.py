# -*- coding: utf-8 -*-
from ..gen import DefaultApi, ObjectInfo, ObjectValueThermostat  # type: ignore
from .base import BaseObject


class Thermostat(BaseObject):
    def __init__(self, api: DefaultApi, object_info: ObjectInfo):
        super().__init__(api, object_info)

    def set_temperature(self, temperature: float):
        return self.set_value(ObjectValueThermostat(setpoint=temperature))

    def get_temperature(self):
        value = self.get_value()
        return value.setpoint
