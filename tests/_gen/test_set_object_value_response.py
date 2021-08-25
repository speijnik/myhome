"""
    MyHomeSERVER1 API

    API provided by the Bticino MyHomeSERVER1 system and used by the MyHomeUp mobile application  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import datetime
import unittest

import myhome._gen
from myhome._gen.models.set_object_value_response import (  # noqa: E501
    SetObjectValueResponse,
)
from myhome._gen.rest import ApiException


class TestSetObjectValueResponse(unittest.TestCase):
    """SetObjectValueResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SetObjectValueResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = myhome._gen.models.set_object_value_response.SetObjectValueResponse()  # noqa: E501
        if include_optional:
            return SetObjectValueResponse(set_value="")
        else:
            return SetObjectValueResponse()

    def testSetObjectValueResponse(self):
        """Test SetObjectValueResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()