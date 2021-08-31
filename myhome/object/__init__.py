"""Object-specific logic."""
import typing

from .._gen.api.default_api import DefaultApi  # type: ignore
from .._gen.model.object_info import ObjectInfo  # type: ignore
from .._gen.model.room import Room  # type: ignore
from .._gen.model.zone import Zone  # type: ignore
from ..exception import MyHomeException
from .base import BaseObject
from .light import Dimmer, Light
from .shutter import Shutter
from .thermostat import Thermostat

OBJ_TYPE_CLASS_MAP = {
    "light": Light,
    "shutter": Shutter,
    "thermostat": Thermostat,
}

OBJ_TYPE_SUBCLASS_MAP = {
    "light": {
        "dimmer": Dimmer,
    }
}


def object_factory(
    api: DefaultApi,
    raw_obj: ObjectInfo,
    zone: typing.Optional[Zone],
    room: typing.Optional[Room],
) -> BaseObject:
    """Return type-specific instance from raw object."""
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

    return obj_class(api, raw_obj, zone=zone, room=room)


class InvalidMatcherFunc(MyHomeException):
    """Invalid matcher provided."""

    def __init__(self, match_name: str):
        """Construct exception."""
        super().__init__(f"Invalid matcher name: {match_name}")


class FilterMatcher:
    """Filter matcher."""

    def __init__(self, filters: typing.Dict[str, typing.Any]):
        """Construct matcher."""
        self._filters = filters

    @staticmethod
    def match_eq(a, b):
        """Match equality."""
        return a == b

    @staticmethod
    def match_startswith(a, b):
        """Match string-starts-with."""
        if not isinstance(a, str) or not isinstance(b, str):
            return False

        return a.startswith(b)

    @staticmethod
    def match_endswith(a, b):
        """Match string-ends-with."""
        if not isinstance(a, str) or not isinstance(b, str):
            return False

        return a.endswith(b)

    @staticmethod
    def match_contains(a, b):
        """Match contains."""
        if not a or not b:
            return False

        return b in a

    def matches(self, obj: object):
        """Return true if object matches filters."""
        for attr, value in self._filters.items():
            attr_name, *rest = attr.split("__", 1)
            match_name = "__".join(rest) or "eq"

            match_fn = getattr(self, "match_" + match_name, None)
            if not callable(match_fn):
                raise InvalidMatcherFunc(match_name)

            if not match_fn(getattr(obj, attr_name, None), value):
                return False
        return True


class ObjectNotFound(MyHomeException):
    """Object matching filters not found."""

    def __init__(self, filters: typing.Dict[str, typing.Any]):
        """Construct exception."""
        filter_defs = [f"{key}={value}" for key, value in filters.items()]
        super().__init__(
            "No object found matching filter {}".format(",".join(sorted(filter_defs)))
        )


class MultipleObjectsFound(MyHomeException):
    """Multiple objects matching filters found."""

    def __init__(self, filters: typing.Dict[str, typing.Any]):
        """Construct exception."""
        filter_defs = [f"{key}={value}" for key, value in filters.items()]
        super().__init__(
            "Multiple objects found matching filter {}".format(
                ",".join(sorted(filter_defs))
            )
        )


class ObjectList(list):
    """Represent a list of objects."""

    def __init__(
        self,
        api: DefaultApi,
        objs: typing.Iterable[typing.Union[ObjectInfo, BaseObject]],
        zones: typing.List[Zone],
        rooms: typing.List[Room],
    ):
        """Construct object list."""
        self._api = api
        self._zones = zones
        self._rooms = rooms

        obj_list = []
        zone_map = {}
        room_map = {}

        for z in zones:
            zone_map.update(
                {
                    z.id: z,
                }
            )

        for r in rooms:
            room_map.update(
                {
                    r.id: r,
                }
            )

        for obj in objs:
            if not isinstance(obj, BaseObject):
                room = room_map.get(obj.id_room, None)
                zone = zone_map.get(obj.id_zone, None)
                obj = object_factory(api, obj, zone, room)
            obj_list.append(obj)
        super().__init__(obj_list)

    def all(self) -> typing.List[BaseObject]:
        """Return all objects."""
        return ObjectList(self._api, self[:])

    def filter(self, **filters) -> typing.List[BaseObject]:
        """Return all objects matching filters."""
        filtered_objs = []
        matcher = FilterMatcher(filters)

        for obj in self:
            if matcher.matches(obj):
                filtered_objs.append(obj)

        return ObjectList(
            self._api, filtered_objs, zones=self._zones, rooms=self._rooms
        )

    def get(self, **filters) -> BaseObject:
        """Return single object matching filters."""
        filtered = self.filter(**filters)

        if len(list(filtered)) == 0:
            raise ObjectNotFound(filters)
        elif len(list(filtered)) > 1:
            raise MultipleObjectsFound(filters)

        return filtered[0]
