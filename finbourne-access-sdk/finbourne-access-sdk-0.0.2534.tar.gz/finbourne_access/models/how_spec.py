# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.2534
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from finbourne_access.configuration import Configuration


class HowSpec(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'type': 'str',
        'parameters': 'list[KeyValuePairOfStringToString]'
    }

    attribute_map = {
        'type': 'type',
        'parameters': 'parameters'
    }

    required_map = {
        'type': 'optional',
        'parameters': 'optional'
    }

    def __init__(self, type=None, parameters=None, local_vars_configuration=None):  # noqa: E501
        """HowSpec - a model defined in OpenAPI"
        
        :param type: 
        :type type: str
        :param parameters: 
        :type parameters: list[finbourne_access.KeyValuePairOfStringToString]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._parameters = None
        self.discriminator = None

        self.type = type
        self.parameters = parameters

    @property
    def type(self):
        """Gets the type of this HowSpec.  # noqa: E501


        :return: The type of this HowSpec.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HowSpec.


        :param type: The type of this HowSpec.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def parameters(self):
        """Gets the parameters of this HowSpec.  # noqa: E501


        :return: The parameters of this HowSpec.  # noqa: E501
        :rtype: list[finbourne_access.KeyValuePairOfStringToString]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this HowSpec.


        :param parameters: The parameters of this HowSpec.  # noqa: E501
        :type parameters: list[finbourne_access.KeyValuePairOfStringToString]
        """

        self._parameters = parameters

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

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, HowSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HowSpec):
            return True

        return self.to_dict() != other.to_dict()
