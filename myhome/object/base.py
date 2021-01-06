# -*- coding: utf-8 -*-
import json
import typing

from ..gen import ObjectValue  # type: ignore
from ..gen import (
    DefaultApi,
    ObjectInfo,
    ObjectValueDimmer,
    ObjectValueLight,
    ObjectValueShutter,
    ObjectValueThermostat,
    SetObjectValueRequest,
    SpecificObjectRequest,
)


class BaseObject(object):
    def __init__(self, api: DefaultApi, object_info: ObjectInfo):
        self._api = api
        self._object_info = object_info
        self._decoded_property: typing.Optional[typing.Iterable[str]] = None

    def get_value(self) -> ObjectValue:
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
        return self._api.set_object_value(
            SetObjectValueRequest(id=self.id, value=value)
        )

    @property
    def id(self) -> int:
        return int(self._object_info.id)

    @property
    def room_id(self) -> int:
        return int(self._object_info.id_room)

    @property
    def zone_id(self) -> int:
        return int(self._object_info.id_zone)

    @property
    def type(self) -> str:
        return self._object_info.type

    @property
    def name(self) -> str:
        return self._object_info.name

    @property
    def property(self) -> typing.Iterable[str]:
        if self._decoded_property is None:
            self._decoded_property = json.loads(
                self._object_info._property
            )  # noqa: E501
        return self._decoded_property

    def __repr__(self) -> str:
        return "<Object: id={},type={},name={}>".format(self.id, self.type, self.name)
