# coding: utf-8

"""
    FINBOURNE Scheduler API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.673
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

from lusid_scheduler.configuration import Configuration


class JobDefinition(object):
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
        'job_id': 'ResourceId',
        'name': 'str',
        'author': 'str',
        'date_created': 'datetime',
        'description': 'str',
        'docker_image': 'str',
        'command': 'str',
        'ttl': 'int',
        'min_cpu': 'str',
        'max_cpu': 'str',
        'min_memory': 'str',
        'max_memory': 'str',
        'argument_definitions': 'dict(str, ArgumentDefinition)',
        'command_line_argument_separator': 'str',
        'required_resources': 'RequiredResources'
    }

    attribute_map = {
        'job_id': 'jobId',
        'name': 'name',
        'author': 'author',
        'date_created': 'dateCreated',
        'description': 'description',
        'docker_image': 'dockerImage',
        'command': 'command',
        'ttl': 'ttl',
        'min_cpu': 'minCpu',
        'max_cpu': 'maxCpu',
        'min_memory': 'minMemory',
        'max_memory': 'maxMemory',
        'argument_definitions': 'argumentDefinitions',
        'command_line_argument_separator': 'commandLineArgumentSeparator',
        'required_resources': 'requiredResources'
    }

    required_map = {
        'job_id': 'required',
        'name': 'optional',
        'author': 'optional',
        'date_created': 'optional',
        'description': 'optional',
        'docker_image': 'optional',
        'command': 'optional',
        'ttl': 'optional',
        'min_cpu': 'optional',
        'max_cpu': 'optional',
        'min_memory': 'optional',
        'max_memory': 'optional',
        'argument_definitions': 'optional',
        'command_line_argument_separator': 'optional',
        'required_resources': 'required'
    }

    def __init__(self, job_id=None, name=None, author=None, date_created=None, description=None, docker_image=None, command=None, ttl=None, min_cpu=None, max_cpu=None, min_memory=None, max_memory=None, argument_definitions=None, command_line_argument_separator=None, required_resources=None, local_vars_configuration=None):  # noqa: E501
        """JobDefinition - a model defined in OpenAPI"
        
        :param job_id:  (required)
        :type job_id: lusid_scheduler.ResourceId
        :param name:  Name of the job
        :type name: str
        :param author:  Author of the job
        :type author: str
        :param date_created:  Date when job was created
        :type date_created: datetime
        :param description:  Description of this job
        :type description: str
        :param docker_image:  Information about the docker image in the format “image_source/image_name:image_tag”
        :type docker_image: str
        :param command:  The command for running this job
        :type command: str
        :param ttl:  Time To Live of the job run in seconds  Defaults to 5 minutes(300)
        :type ttl: int
        :param min_cpu:  Specifies  minimum number of CPUs to be allocated for the job  Default to 2
        :type min_cpu: str
        :param max_cpu:  Specifies  maximum number of CPUs to be allocated for the job
        :type max_cpu: str
        :param min_memory:  Specifies the minimum amount of memory (in GiB) to be allocated for the job
        :type min_memory: str
        :param max_memory:  Specifies the maximum amount of memory (in GiB) to be allocated for the job
        :type max_memory: str
        :param argument_definitions:  All arguments for this job to run
        :type argument_definitions: dict[str, lusid_scheduler.ArgumentDefinition]
        :param command_line_argument_separator:  Value to separate command line arguments  e.g : If a job has a command line argument named 'folder' and the runtime value is 's3://path' then this  would be supplied to the command as 'folder{separatorValue}s3://path'  Default to a space
        :type command_line_argument_separator: str
        :param required_resources:  (required)
        :type required_resources: lusid_scheduler.RequiredResources

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._job_id = None
        self._name = None
        self._author = None
        self._date_created = None
        self._description = None
        self._docker_image = None
        self._command = None
        self._ttl = None
        self._min_cpu = None
        self._max_cpu = None
        self._min_memory = None
        self._max_memory = None
        self._argument_definitions = None
        self._command_line_argument_separator = None
        self._required_resources = None
        self.discriminator = None

        self.job_id = job_id
        self.name = name
        self.author = author
        if date_created is not None:
            self.date_created = date_created
        self.description = description
        self.docker_image = docker_image
        self.command = command
        if ttl is not None:
            self.ttl = ttl
        self.min_cpu = min_cpu
        self.max_cpu = max_cpu
        self.min_memory = min_memory
        self.max_memory = max_memory
        self.argument_definitions = argument_definitions
        self.command_line_argument_separator = command_line_argument_separator
        self.required_resources = required_resources

    @property
    def job_id(self):
        """Gets the job_id of this JobDefinition.  # noqa: E501


        :return: The job_id of this JobDefinition.  # noqa: E501
        :rtype: lusid_scheduler.ResourceId
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this JobDefinition.


        :param job_id: The job_id of this JobDefinition.  # noqa: E501
        :type job_id: lusid_scheduler.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and job_id is None:  # noqa: E501
            raise ValueError("Invalid value for `job_id`, must not be `None`")  # noqa: E501

        self._job_id = job_id

    @property
    def name(self):
        """Gets the name of this JobDefinition.  # noqa: E501

        Name of the job  # noqa: E501

        :return: The name of this JobDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobDefinition.

        Name of the job  # noqa: E501

        :param name: The name of this JobDefinition.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def author(self):
        """Gets the author of this JobDefinition.  # noqa: E501

        Author of the job  # noqa: E501

        :return: The author of this JobDefinition.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this JobDefinition.

        Author of the job  # noqa: E501

        :param author: The author of this JobDefinition.  # noqa: E501
        :type author: str
        """

        self._author = author

    @property
    def date_created(self):
        """Gets the date_created of this JobDefinition.  # noqa: E501

        Date when job was created  # noqa: E501

        :return: The date_created of this JobDefinition.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this JobDefinition.

        Date when job was created  # noqa: E501

        :param date_created: The date_created of this JobDefinition.  # noqa: E501
        :type date_created: datetime
        """

        self._date_created = date_created

    @property
    def description(self):
        """Gets the description of this JobDefinition.  # noqa: E501

        Description of this job  # noqa: E501

        :return: The description of this JobDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JobDefinition.

        Description of this job  # noqa: E501

        :param description: The description of this JobDefinition.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def docker_image(self):
        """Gets the docker_image of this JobDefinition.  # noqa: E501

        Information about the docker image in the format “image_source/image_name:image_tag”  # noqa: E501

        :return: The docker_image of this JobDefinition.  # noqa: E501
        :rtype: str
        """
        return self._docker_image

    @docker_image.setter
    def docker_image(self, docker_image):
        """Sets the docker_image of this JobDefinition.

        Information about the docker image in the format “image_source/image_name:image_tag”  # noqa: E501

        :param docker_image: The docker_image of this JobDefinition.  # noqa: E501
        :type docker_image: str
        """

        self._docker_image = docker_image

    @property
    def command(self):
        """Gets the command of this JobDefinition.  # noqa: E501

        The command for running this job  # noqa: E501

        :return: The command of this JobDefinition.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this JobDefinition.

        The command for running this job  # noqa: E501

        :param command: The command of this JobDefinition.  # noqa: E501
        :type command: str
        """

        self._command = command

    @property
    def ttl(self):
        """Gets the ttl of this JobDefinition.  # noqa: E501

        Time To Live of the job run in seconds  Defaults to 5 minutes(300)  # noqa: E501

        :return: The ttl of this JobDefinition.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this JobDefinition.

        Time To Live of the job run in seconds  Defaults to 5 minutes(300)  # noqa: E501

        :param ttl: The ttl of this JobDefinition.  # noqa: E501
        :type ttl: int
        """

        self._ttl = ttl

    @property
    def min_cpu(self):
        """Gets the min_cpu of this JobDefinition.  # noqa: E501

        Specifies  minimum number of CPUs to be allocated for the job  Default to 2  # noqa: E501

        :return: The min_cpu of this JobDefinition.  # noqa: E501
        :rtype: str
        """
        return self._min_cpu

    @min_cpu.setter
    def min_cpu(self, min_cpu):
        """Sets the min_cpu of this JobDefinition.

        Specifies  minimum number of CPUs to be allocated for the job  Default to 2  # noqa: E501

        :param min_cpu: The min_cpu of this JobDefinition.  # noqa: E501
        :type min_cpu: str
        """

        self._min_cpu = min_cpu

    @property
    def max_cpu(self):
        """Gets the max_cpu of this JobDefinition.  # noqa: E501

        Specifies  maximum number of CPUs to be allocated for the job  # noqa: E501

        :return: The max_cpu of this JobDefinition.  # noqa: E501
        :rtype: str
        """
        return self._max_cpu

    @max_cpu.setter
    def max_cpu(self, max_cpu):
        """Sets the max_cpu of this JobDefinition.

        Specifies  maximum number of CPUs to be allocated for the job  # noqa: E501

        :param max_cpu: The max_cpu of this JobDefinition.  # noqa: E501
        :type max_cpu: str
        """

        self._max_cpu = max_cpu

    @property
    def min_memory(self):
        """Gets the min_memory of this JobDefinition.  # noqa: E501

        Specifies the minimum amount of memory (in GiB) to be allocated for the job  # noqa: E501

        :return: The min_memory of this JobDefinition.  # noqa: E501
        :rtype: str
        """
        return self._min_memory

    @min_memory.setter
    def min_memory(self, min_memory):
        """Sets the min_memory of this JobDefinition.

        Specifies the minimum amount of memory (in GiB) to be allocated for the job  # noqa: E501

        :param min_memory: The min_memory of this JobDefinition.  # noqa: E501
        :type min_memory: str
        """

        self._min_memory = min_memory

    @property
    def max_memory(self):
        """Gets the max_memory of this JobDefinition.  # noqa: E501

        Specifies the maximum amount of memory (in GiB) to be allocated for the job  # noqa: E501

        :return: The max_memory of this JobDefinition.  # noqa: E501
        :rtype: str
        """
        return self._max_memory

    @max_memory.setter
    def max_memory(self, max_memory):
        """Sets the max_memory of this JobDefinition.

        Specifies the maximum amount of memory (in GiB) to be allocated for the job  # noqa: E501

        :param max_memory: The max_memory of this JobDefinition.  # noqa: E501
        :type max_memory: str
        """

        self._max_memory = max_memory

    @property
    def argument_definitions(self):
        """Gets the argument_definitions of this JobDefinition.  # noqa: E501

        All arguments for this job to run  # noqa: E501

        :return: The argument_definitions of this JobDefinition.  # noqa: E501
        :rtype: dict[str, lusid_scheduler.ArgumentDefinition]
        """
        return self._argument_definitions

    @argument_definitions.setter
    def argument_definitions(self, argument_definitions):
        """Sets the argument_definitions of this JobDefinition.

        All arguments for this job to run  # noqa: E501

        :param argument_definitions: The argument_definitions of this JobDefinition.  # noqa: E501
        :type argument_definitions: dict[str, lusid_scheduler.ArgumentDefinition]
        """

        self._argument_definitions = argument_definitions

    @property
    def command_line_argument_separator(self):
        """Gets the command_line_argument_separator of this JobDefinition.  # noqa: E501

        Value to separate command line arguments  e.g : If a job has a command line argument named 'folder' and the runtime value is 's3://path' then this  would be supplied to the command as 'folder{separatorValue}s3://path'  Default to a space  # noqa: E501

        :return: The command_line_argument_separator of this JobDefinition.  # noqa: E501
        :rtype: str
        """
        return self._command_line_argument_separator

    @command_line_argument_separator.setter
    def command_line_argument_separator(self, command_line_argument_separator):
        """Sets the command_line_argument_separator of this JobDefinition.

        Value to separate command line arguments  e.g : If a job has a command line argument named 'folder' and the runtime value is 's3://path' then this  would be supplied to the command as 'folder{separatorValue}s3://path'  Default to a space  # noqa: E501

        :param command_line_argument_separator: The command_line_argument_separator of this JobDefinition.  # noqa: E501
        :type command_line_argument_separator: str
        """

        self._command_line_argument_separator = command_line_argument_separator

    @property
    def required_resources(self):
        """Gets the required_resources of this JobDefinition.  # noqa: E501


        :return: The required_resources of this JobDefinition.  # noqa: E501
        :rtype: lusid_scheduler.RequiredResources
        """
        return self._required_resources

    @required_resources.setter
    def required_resources(self, required_resources):
        """Sets the required_resources of this JobDefinition.


        :param required_resources: The required_resources of this JobDefinition.  # noqa: E501
        :type required_resources: lusid_scheduler.RequiredResources
        """
        if self.local_vars_configuration.client_side_validation and required_resources is None:  # noqa: E501
            raise ValueError("Invalid value for `required_resources`, must not be `None`")  # noqa: E501

        self._required_resources = required_resources

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
        if not isinstance(other, JobDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobDefinition):
            return True

        return self.to_dict() != other.to_dict()
