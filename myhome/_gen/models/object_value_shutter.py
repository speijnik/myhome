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


class ObjectValueShutter:
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
        'move': 'str'
    }

    attribute_map = {
        'move': 'move'
    }

    def __init__(self, move=None, local_vars_configuration=None):  # noqa: E501
        """ObjectValueShutter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._move = None
        self.discriminator = None

        self.move = move

    @property
    def move(self):
        """Gets the move of this ObjectValueShutter.  # noqa: E501

        Operating mode  # noqa: E501

        :return: The move of this ObjectValueShutter.  # noqa: E501
        :rtype: str
        """
        return self._move

    @move.setter
    def move(self, move):
        """Sets the move of this ObjectValueShutter.

        Operating mode  # noqa: E501

        :param move: The move of this ObjectValueShutter.  # noqa: E501
        :type move: str
        """
        if self.local_vars_configuration.client_side_validation and move is None:  # noqa: E501
            raise ValueError("Invalid value for `move`, must not be `None`")  # noqa: E501
        allowed_values = ["STOP", "UP", "DOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and move not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `move` ({}), must be one of {}"  # noqa: E501
                .format(move, allowed_values)
            )

        self._move = move

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
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
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
        if not isinstance(other, ObjectValueShutter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObjectValueShutter):
            return True

        return self.to_dict() != other.to_dict()
