"""
    MyHomeSERVER1 API

    API provided by the Bticino MyHomeSERVER1 system and used by the MyHomeUp mobile application  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import myhome._gen
from myhome._gen.model.object_value import ObjectValue

globals()['ObjectValue'] = ObjectValue
from myhome._gen.model.set_object_value_request import SetObjectValueRequest


class TestSetObjectValueRequest(unittest.TestCase):
    """SetObjectValueRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSetObjectValueRequest(self):
        """Test SetObjectValueRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SetObjectValueRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()