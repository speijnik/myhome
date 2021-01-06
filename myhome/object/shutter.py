# -*- coding: utf-8 -*-
from ..gen import DefaultApi, ObjectInfo, ObjectValueShutter  # type: ignore
from . import BaseObject


class Shutter(BaseObject):
    def __init__(self, api: DefaultApi, object_info: ObjectInfo):
        super().__init__(api, object_info)

    def move_up(self):
        return self.move_shutter("UP")

    def move_stop(self):
        return self.move_shutter("STOP")

    def move_down(self):
        return self.move_shutter("DOWN")

    def move_shutter(self, direction: str):
        return self.set_value(ObjectValueShutter(move=direction))

    def get_shutter_move(self):
        return self.get_value().move
