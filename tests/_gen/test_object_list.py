"""
    MyHomeSERVER1 API

    API provided by the Bticino MyHomeSERVER1 system and used by the MyHomeUp mobile application  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import myhome._gen
from myhome._gen.model.object_info import ObjectInfo

globals()["ObjectInfo"] = ObjectInfo
from myhome._gen.model.object_list import ObjectList


class TestObjectList(unittest.TestCase):
    """ObjectList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testObjectList(self):
        """Test ObjectList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ObjectList()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()