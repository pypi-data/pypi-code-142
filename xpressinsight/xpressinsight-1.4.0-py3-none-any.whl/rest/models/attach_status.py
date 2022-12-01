#

"""
    Python Insight API

    This is an internal REST API between Python and Mosel  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech

    This material is the confidential, proprietary, unpublished property
    of Fair Isaac Corporation.  Receipt or possession of this material
    does not convey rights to divulge, reproduce, use, or allow others
    to use it without the specific written authorization of Fair Isaac
    Corporation and use must conform strictly to the license agreement.

    Copyright (c) 2020-2022 Fair Isaac Corporation. All rights reserved.
"""


import pprint
import re  #

import six

from xpressinsight.rest.configuration import Configuration


class AttachStatus(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    OK = "INSIGHT_ATTACH_OK"
    RUNTIME_ERROR = "INSIGHT_ATTACH_RUNTIME_ERROR"
    NOT_FOUND = "INSIGHT_ATTACH_NOT_FOUND"
    SEVERAL_FOUND = "INSIGHT_ATTACH_SEVERAL_FOUND"
    INVALID_FILENAME = "INSIGHT_ATTACH_INVALID_FILENAME"
    INVALID_DESCRIPTION = "INSIGHT_ATTACH_INVALID_DESCRIPTION"
    ALREADY_EXISTS = "INSIGHT_ATTACH_ALREADY_EXISTS"
    TOO_LARGE = "INSIGHT_ATTACH_TOO_LARGE"
    TOO_MANY = "INSIGHT_ATTACH_TOO_MANY"
    INVALID_TAGS = "INSIGHT_ATTACH_INVALID_TAGS"

    allowable_values = [OK, RUNTIME_ERROR, NOT_FOUND, SEVERAL_FOUND, INVALID_FILENAME, INVALID_DESCRIPTION, ALREADY_EXISTS, TOO_LARGE, TOO_MANY, INVALID_TAGS]  #

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  #
        """AttachStatus - a model defined in OpenAPI"""  #
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
        if not isinstance(other, AttachStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachStatus):
            return True

        return self.to_dict() != other.to_dict()
