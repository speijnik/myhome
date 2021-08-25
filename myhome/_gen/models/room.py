"""
    MyHomeSERVER1 API

    API provided by the Bticino MyHomeSERVER1 system and used by the MyHomeUp mobile application  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec

import pprint
import re  # noqa: F401

import six

from myhome._gen.configuration import Configuration


class Room:
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
    openapi_types = {"id": "int", "id_zone": "str", "image": "str", "name": "str"}

    attribute_map = {"id": "id", "id_zone": "idZone", "image": "image", "name": "name"}

    def __init__(
        self,
        id=None,
        id_zone=None,
        image=None,
        name=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Room - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._id_zone = None
        self._image = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if id_zone is not None:
            self.id_zone = id_zone
        if image is not None:
            self.image = image
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this Room.  # noqa: E501

        Room ID  # noqa: E501

        :return: The id of this Room.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Room.

        Room ID  # noqa: E501

        :param id: The id of this Room.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def id_zone(self):
        """Gets the id_zone of this Room.  # noqa: E501

        Zone ID  # noqa: E501

        :return: The id_zone of this Room.  # noqa: E501
        :rtype: str
        """
        return self._id_zone

    @id_zone.setter
    def id_zone(self, id_zone):
        """Sets the id_zone of this Room.

        Zone ID  # noqa: E501

        :param id_zone: The id_zone of this Room.  # noqa: E501
        :type id_zone: str
        """

        self._id_zone = id_zone

    @property
    def image(self):
        """Gets the image of this Room.  # noqa: E501

        Possibly always empty  # noqa: E501

        :return: The image of this Room.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Room.

        Possibly always empty  # noqa: E501

        :param image: The image of this Room.  # noqa: E501
        :type image: str
        """

        self._image = image

    @property
    def name(self):
        """Gets the name of this Room.  # noqa: E501

        Display name  # noqa: E501

        :return: The name of this Room.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Room.

        Display name  # noqa: E501

        :param name: The name of this Room.  # noqa: E501
        :type name: str
        """

        self._name = name

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(lambda item: (item[0], convert(item[1])), value.items())
                )
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Room):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Room):
            return True

        return self.to_dict() != other.to_dict()
