# -*- coding: utf-8 -*-
from ..gen import ObjectValueDimmer  # type: ignore
from ..gen import DefaultApi, ObjectInfo, ObjectValueLight
from .base import BaseObject


class Light(BaseObject):
    def __init__(self, api: DefaultApi, object_info: ObjectInfo):
        super().__init__(api, object_info)

    def switch_on(self):
        return self.set_value(ObjectValueLight(power=True))

    def switch_off(self):
        return self.set_value(ObjectValueLight(power=False))

    @property
    def is_on(self):
        return self.get_value().power


class DimmableLight(Light):
    def dim(self, percentage: int):
        return self.set_value(ObjectValueDimmer(dimmer=percentage))

    def is_on(self):
        return self.dimmer_level > 0

    @property
    def dimmer_level(self):
        return self.get_value().dimmer
