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


class AccessStatus:
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
    openapi_types = {"access": "str"}

    attribute_map = {"access": "access"}

    def __init__(self, access=None, local_vars_configuration=None):  # noqa: E501
        """AccessStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._access = None
        self.discriminator = None

        self.access = access

    @property
    def access(self):
        """Gets the access of this AccessStatus.  # noqa: E501


        :return: The access of this AccessStatus.  # noqa: E501
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this AccessStatus.


        :param access: The access of this AccessStatus.  # noqa: E501
        :type access: str
        """
        if (
            self.local_vars_configuration.client_side_validation and access is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `access`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["success", "error"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and access not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `access` ({}), must be one of {}".format(  # noqa: E501
                    access, allowed_values
                )
            )

        self._access = access

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
        if not isinstance(other, AccessStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessStatus):
            return True

        return self.to_dict() != other.to_dict()
