# -*- coding: utf-8 -*-
import typing

from ..exception import BaseException
from ..gen import DefaultApi, ObjectInfo  # type: ignore
from .base import BaseObject
from .light import DimmableLight, Light
from .shutter import Shutter
from .thermostat import Thermostat

OBJ_TYPE_CLASS_MAP = {
    "light": Light,
    "shutter": Shutter,
    "thermostat": Thermostat,
}

OBJ_TYPE_SUBCLASS_MAP = {
    "light": {
        "dimmer": DimmableLight,
    }
}


def object_factory(api: DefaultApi, raw_obj: ObjectInfo) -> BaseObject:
    obj_class: typing.Optional[typing.Type[BaseObject]] = None
    subclass_map = OBJ_TYPE_SUBCLASS_MAP.get(raw_obj.type, None)
    if subclass_map:
        base_obj = BaseObject(api, raw_obj)
        for prop in base_obj.property:
            obj_class = subclass_map.get(prop, None)
            if obj_class:
                break

    if not obj_class:
        obj_class = OBJ_TYPE_CLASS_MAP.get(raw_obj.type, None)

    if not obj_class:
        obj_class = BaseObject

    return obj_class(api, raw_obj)


class InvalidMatcherFunc(BaseException):
    def __init__(self, match_name: str):
        super().__init__("Invalid matcher name: {}".format(match_name))


class FilterMatcher(object):
    def __init__(self, filters: typing.Dict[str, typing.Any]):
        self._filters = filters

    @staticmethod
    def match_eq(a, b):
        return a == b

    @staticmethod
    def match_startswith(a, b):
        if not isinstance(a, str) or not isinstance(b, str):
            return False

        return a.startswith(b)

    @staticmethod
    def match_endswith(a, b):
        if not isinstance(a, str) or not isinstance(b, str):
            return False

        return a.endswith(b)

    @staticmethod
    def match_contains(a, b):
        if not a or not b:
            return False

        return b in a

    def matches(self, obj: object):
        for attr, value in self._filters.items():
            attr_name, *rest = attr.split("__", 1)
            match_name = "__".join(rest) or "eq"

            match_fn = getattr(self, "match_" + match_name, None)
            if not callable(match_fn):
                raise InvalidMatcherFunc(match_name)

            if not match_fn(getattr(obj, attr_name, None), value):
                return False
        return True


class ObjectNotFound(BaseException):
    def __init__(self, filters: typing.Dict[str, typing.Any]):
        filter_defs = ["{}={}".format(key, value) for key, value in filters.items()]
        super().__init__(
            "No object found matching filter {}".format(",".join(sorted(filter_defs)))
        )


class MultipleObjectsFound(BaseException):
    def __init__(self, filters: typing.Dict[str, typing.Any]):
        filter_defs = ["{}={}".format(key, value) for key, value in filters.items()]
        super().__init__(
            "Multiple objects found matching filter {}".format(
                ",".join(sorted(filter_defs))
            )
        )


class ObjectList(list):
    def __init__(
        self,
        api: DefaultApi,
        objs: typing.Iterable[typing.Union[ObjectInfo, BaseObject]],
    ):
        self._api = api
        list = []

        for obj in objs:
            if not isinstance(obj, BaseObject):
                obj = object_factory(api, obj)
            list.append(obj)
        super().__init__(list)

    def all(self) -> typing.List[BaseObject]:
        return ObjectList(self._api, self[:])

    def filter(self, **filters) -> typing.List[BaseObject]:
        filtered_objs = []
        matcher = FilterMatcher(filters)

        for obj in self:
            if matcher.matches(obj):
                filtered_objs.append(obj)

        return ObjectList(self._api, filtered_objs)

    def get(self, **filters) -> BaseObject:
        filtered = self.filter(**filters)

        if len(list(filtered)) == 0:
            raise ObjectNotFound(filters)
        elif len(list(filtered)) > 1:
            raise MultipleObjectsFound(filters)

        return filtered[0]
