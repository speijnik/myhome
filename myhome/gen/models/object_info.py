"""
    MyHomeSERVER1 API

    API provided by the Bticino MyHomeSERVER1 system and used by the MyHomeUp mobile application  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from myhome.gen.configuration import Configuration


class ObjectInfo:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "id": "int",
        "id_room": "int",
        "id_zone": "int",
        "name": "str",
        "type": "str",
        "protocol_name": "str",
        "protocol_config": "str",
        "_property": "str",
    }

    attribute_map = {
        "id": "id",
        "id_room": "idRoom",
        "id_zone": "idZone",
        "name": "name",
        "type": "type",
        "protocol_name": "protocolName",
        "protocol_config": "protocolConfig",
        "_property": "property",
    }

    def __init__(
        self,
        id=None,
        id_room=None,
        id_zone=None,
        name=None,
        type=None,
        protocol_name=None,
        protocol_config=None,
        _property=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """ObjectInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._id_room = None
        self._id_zone = None
        self._name = None
        self._type = None
        self._protocol_name = None
        self._protocol_config = None
        self.__property = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if id_room is not None:
            self.id_room = id_room
        if id_zone is not None:
            self.id_zone = id_zone
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if protocol_name is not None:
            self.protocol_name = protocol_name
        if protocol_config is not None:
            self.protocol_config = protocol_config
        if _property is not None:
            self._property = _property

    @property
    def id(self):
        """Gets the id of this ObjectInfo.  # noqa: E501

        Object ID  # noqa: E501

        :return: The id of this ObjectInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ObjectInfo.

        Object ID  # noqa: E501

        :param id: The id of this ObjectInfo.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def id_room(self):
        """Gets the id_room of this ObjectInfo.  # noqa: E501

        ID of the room the object is located in  # noqa: E501

        :return: The id_room of this ObjectInfo.  # noqa: E501
        :rtype: int
        """
        return self._id_room

    @id_room.setter
    def id_room(self, id_room):
        """Sets the id_room of this ObjectInfo.

        ID of the room the object is located in  # noqa: E501

        :param id_room: The id_room of this ObjectInfo.  # noqa: E501
        :type: int
        """

        self._id_room = id_room

    @property
    def id_zone(self):
        """Gets the id_zone of this ObjectInfo.  # noqa: E501

        ID of the zone the object belongs to  # noqa: E501

        :return: The id_zone of this ObjectInfo.  # noqa: E501
        :rtype: int
        """
        return self._id_zone

    @id_zone.setter
    def id_zone(self, id_zone):
        """Sets the id_zone of this ObjectInfo.

        ID of the zone the object belongs to  # noqa: E501

        :param id_zone: The id_zone of this ObjectInfo.  # noqa: E501
        :type: int
        """

        self._id_zone = id_zone

    @property
    def name(self):
        """Gets the name of this ObjectInfo.  # noqa: E501

        Display name  # noqa: E501

        :return: The name of this ObjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ObjectInfo.

        Display name  # noqa: E501

        :param name: The name of this ObjectInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this ObjectInfo.  # noqa: E501

        Object type  # noqa: E501

        :return: The type of this ObjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ObjectInfo.

        Object type  # noqa: E501

        :param type: The type of this ObjectInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["light", "shutter", "thermostat"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and type not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({}), must be one of {}".format(  # noqa: E501
                    type, allowed_values
                )
            )

        self._type = type

    @property
    def protocol_name(self):
        """Gets the protocol_name of this ObjectInfo.  # noqa: E501

        Name of protocol via which the object is connected  # noqa: E501

        :return: The protocol_name of this ObjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._protocol_name

    @protocol_name.setter
    def protocol_name(self, protocol_name):
        """Sets the protocol_name of this ObjectInfo.

        Name of protocol via which the object is connected  # noqa: E501

        :param protocol_name: The protocol_name of this ObjectInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["Bticino"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and protocol_name not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `protocol_name` ({}), must be one of {}".format(  # noqa: E501
                    protocol_name, allowed_values
                )
            )

        self._protocol_name = protocol_name

    @property
    def protocol_config(self):
        """Gets the protocol_config of this ObjectInfo.  # noqa: E501

        Protocol-specific object identification/address  # noqa: E501

        :return: The protocol_config of this ObjectInfo.  # noqa: E501
        :rtype: str
        """
        return self._protocol_config

    @protocol_config.setter
    def protocol_config(self, protocol_config):
        """Sets the protocol_config of this ObjectInfo.

        Protocol-specific object identification/address  # noqa: E501

        :param protocol_config: The protocol_config of this ObjectInfo.  # noqa: E501
        :type: str
        """

        self._protocol_config = protocol_config

    @property
    def _property(self):
        """Gets the _property of this ObjectInfo.  # noqa: E501

        Object type as JSON array encoded into string (escaped)  # noqa: E501

        :return: The _property of this ObjectInfo.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this ObjectInfo.

        Object type as JSON array encoded into string (escaped)  # noqa: E501

        :param _property: The _property of this ObjectInfo.  # noqa: E501
        :type: str
        """

        self.__property = _property

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ObjectInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObjectInfo):
            return True

        return self.to_dict() != other.to_dict()
