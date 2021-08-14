"""Base implementation and helpers."""
import json
import typing

from ..gen import (
    DefaultApi,
    ObjectInfo,
    ObjectValueDimmer,
    ObjectValueLight,
    ObjectValueShutter,
    ObjectValueThermostat,
    Room,
    SetObjectValueRequest,
    SpecificObjectRequest,
    Zone,
)
from ..gen import ObjectValue  # type: ignore


class BaseObject:
    """Base object class."""

    def __init__(
        self,
        api: DefaultApi,
        object_info: ObjectInfo,
        zone: typing.Optional[Zone] = None,
        room: typing.Optional[Room] = None,
    ):
        """Construct base object."""
        self._api = api
        self._object_info = object_info
        self._decoded_property: typing.Optional[typing.Iterable[str]] = None
        self._zone = zone
        self._room = room

    def get_value(self) -> ObjectValue:
        """Retrieve object value."""
        return self._api.get_object_value(SpecificObjectRequest(id=self.id))

    def set_value(
        self,
        value: typing.Union[
            ObjectValueDimmer,
            ObjectValueLight,
            ObjectValueShutter,
            ObjectValueThermostat,
        ],
    ):
        """Set object value."""
        return self._api.set_object_value(
            SetObjectValueRequest(id=self.id, value=value)
        )

    @property
    def id(self) -> int:
        """Return object ID."""
        return int(self._object_info.id)

    @property
    def room_id(self) -> int:
        """Return object room ID."""
        return int(self._object_info.id_room)

    @property
    def room(self) -> typing.Optional[Room]:
        """Return room object if known."""
        return self._room

    @property
    def zone_id(self) -> int:
        """Return object zone ID."""
        return int(self._object_info.id_zone)

    @property
    def zone(self) -> typing.Optional[Zone]:
        """Return zone object if known."""
        return self._zone

    @property
    def type(self) -> str:
        """Return object type name."""
        return self._object_info.type

    @property
    def name(self) -> str:
        """Return object name."""
        return self._object_info.name

    @property
    def property(self) -> typing.Iterable[str]:
        """Return object property."""
        if self._decoded_property is None:
            self._decoded_property = json.loads(self._object_info._property)
        return self._decoded_property

    def __repr__(self) -> str:
        """Return the basic object properties."""
        return f"<Object: id={self.id},type={self.type},name={self.name}>"
