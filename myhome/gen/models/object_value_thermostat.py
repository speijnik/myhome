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


class ObjectValueThermostat:
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
    openapi_types = {"setpoint": "float"}

    attribute_map = {"setpoint": "setpoint"}

    def __init__(self, setpoint=None, local_vars_configuration=None):  # noqa: E501
        """ObjectValueThermostat - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._setpoint = None
        self.discriminator = None

        if setpoint is not None:
            self.setpoint = setpoint

    @property
    def setpoint(self):
        """Gets the setpoint of this ObjectValueThermostat.  # noqa: E501

        Desired room temperature  # noqa: E501

        :return: The setpoint of this ObjectValueThermostat.  # noqa: E501
        :rtype: float
        """
        return self._setpoint

    @setpoint.setter
    def setpoint(self, setpoint):
        """Sets the setpoint of this ObjectValueThermostat.

        Desired room temperature  # noqa: E501

        :param setpoint: The setpoint of this ObjectValueThermostat.  # noqa: E501
        :type: float
        """

        self._setpoint = setpoint

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
        if not isinstance(other, ObjectValueThermostat):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObjectValueThermostat):
            return True

        return self.to_dict() != other.to_dict()
