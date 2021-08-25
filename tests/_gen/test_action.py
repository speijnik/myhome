"""
    MyHomeSERVER1 API

    API provided by the Bticino MyHomeSERVER1 system and used by the MyHomeUp mobile application  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import datetime
import unittest

import myhome._gen
from myhome._gen.models.action import Action  # noqa: E501
from myhome._gen.rest import ApiException


class TestAction(unittest.TestCase):
    """Action unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Action
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = myhome._gen.models.action.Action()  # noqa: E501
        if include_optional:
            return Action(
                arr_events=["button"],
                arr_events_dis=["button"],
                id=56,
                image="",
                name="",
            )
        else:
            return Action()

    def testAction(self):
        """Test Action"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()