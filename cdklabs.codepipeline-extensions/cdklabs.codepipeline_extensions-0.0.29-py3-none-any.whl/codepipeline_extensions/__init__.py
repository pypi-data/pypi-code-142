'''
## CDK CodePipeline Extensions

This project is for use in the workshop DOP 401: Get better at building AWS CDK constructs.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This project is licensed under the Apache-2.0 License.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk
import aws_cdk.aws_codecommit
import aws_cdk.aws_codeguruprofiler
import aws_cdk.aws_codepipeline
import aws_cdk.aws_ec2
import aws_cdk.aws_events
import aws_cdk.aws_iam
import aws_cdk.aws_kms
import aws_cdk.aws_lambda
import aws_cdk.aws_logs
import aws_cdk.aws_s3
import aws_cdk.aws_sns
import aws_cdk.aws_sqs
import constructs


@jsii.data_type(
    jsii_type="@cdklabs/cdk-codepipeline-extensions.AggregateAlarmState",
    jsii_struct_bases=[],
    name_mapping={
        "alarm_details": "alarmDetails",
        "state": "state",
        "summary": "summary",
    },
)
class AggregateAlarmState:
    def __init__(
        self,
        *,
        alarm_details: typing.Sequence["IAlarmDetail"],
        state: "AlarmState",
        summary: builtins.str,
    ) -> None:
        '''
        :param alarm_details: 
        :param state: 
        :param summary: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                alarm_details: typing.Sequence[IAlarmDetail],
                state: AlarmState,
                summary: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument alarm_details", value=alarm_details, expected_type=type_hints["alarm_details"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
        self._values: typing.Dict[str, typing.Any] = {
            "alarm_details": alarm_details,
            "state": state,
            "summary": summary,
        }

    @builtins.property
    def alarm_details(self) -> typing.List["IAlarmDetail"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("alarm_details")
        assert result is not None, "Required property 'alarm_details' is missing"
        return typing.cast(typing.List["IAlarmDetail"], result)

    @builtins.property
    def state(self) -> "AlarmState":
        '''
        :stability: experimental
        '''
        result = self._values.get("state")
        assert result is not None, "Required property 'state' is missing"
        return typing.cast("AlarmState", result)

    @builtins.property
    def summary(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("summary")
        assert result is not None, "Required property 'summary' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AggregateAlarmState(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@cdklabs/cdk-codepipeline-extensions.AlarmState")
class AlarmState(enum.Enum):
    '''
    :stability: experimental
    '''

    OK = "OK"
    '''
    :stability: experimental
    '''
    ALARM = "ALARM"
    '''
    :stability: experimental
    '''
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"
    '''
    :stability: experimental
    '''


class Calendar(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@cdklabs/cdk-codepipeline-extensions.Calendar",
):
    '''(experimental) The calendar for determining if pipeline stage should be open or closed.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="path")
    @builtins.classmethod
    def path(
        cls,
        *,
        calendar_path: builtins.str,
        calendar_name: builtins.str,
    ) -> "Calendar":
        '''(experimental) Creates a calendar from a local file.

        :param calendar_path: (experimental) The relative path to the calendar file.
        :param calendar_name: (experimental) The name of the calendar file.

        :stability: experimental
        '''
        options = LocalPathOptions(
            calendar_path=calendar_path, calendar_name=calendar_name
        )

        return typing.cast("Calendar", jsii.sinvoke(cls, "path", [options]))

    @jsii.member(jsii_name="s3Location")
    @builtins.classmethod
    def s3_location(
        cls,
        *,
        bucket: aws_cdk.aws_s3.IBucket,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        calendar_name: builtins.str,
    ) -> "Calendar":
        '''(experimental) Creates a calendar from a S3 bucket.

        :param bucket: (experimental) The bucket where the calendar is stored.
        :param role: (experimental) The role used for getting the calendar file. Default: - A role created by the Custom Resource.
        :param calendar_name: (experimental) The name of the calendar file.

        :stability: experimental
        '''
        options = S3LocationOptions(
            bucket=bucket, role=role, calendar_name=calendar_name
        )

        return typing.cast("Calendar", jsii.sinvoke(cls, "s3Location", [options]))

    @builtins.property
    @jsii.member(jsii_name="calendarArn")
    def calendar_arn(self) -> builtins.str:
        '''(experimental) The ARN of the calendar in SSM.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "calendarArn"))

    @calendar_arn.setter
    def calendar_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "calendarArn", value)

    @builtins.property
    @jsii.member(jsii_name="calendarName")
    def calendar_name(self) -> builtins.str:
        '''(experimental) The name of the calendar.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "calendarName"))

    @calendar_name.setter
    def calendar_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "calendarName", value)


class _CalendarProxy(Calendar):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Calendar).__jsii_proxy_class__ = lambda : _CalendarProxy


@jsii.data_type(
    jsii_type="@cdklabs/cdk-codepipeline-extensions.CalendarLocationOptionsBase",
    jsii_struct_bases=[],
    name_mapping={"calendar_name": "calendarName"},
)
class CalendarLocationOptionsBase:
    def __init__(self, *, calendar_name: builtins.str) -> None:
        '''(experimental) Options for creating a calendar object.

        :param calendar_name: (experimental) The name of the calendar file.

        :stability: experimental
        '''
        if __debug__:
            def stub(*, calendar_name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument calendar_name", value=calendar_name, expected_type=type_hints["calendar_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "calendar_name": calendar_name,
        }

    @builtins.property
    def calendar_name(self) -> builtins.str:
        '''(experimental) The name of the calendar file.

        :stability: experimental
        '''
        result = self._values.get("calendar_name")
        assert result is not None, "Required property 'calendar_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CalendarLocationOptionsBase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CalendarSetupFunction(
    aws_cdk.aws_lambda.Function,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-codepipeline-extensions.CalendarSetupFunction",
):
    '''(experimental) An AWS Lambda function which executes src/time-windows/calendar/calendar-setup.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        architecture: typing.Optional[aws_cdk.aws_lambda.Architecture] = None,
        code_signing_config: typing.Optional[aws_cdk.aws_lambda.ICodeSigningConfig] = None,
        current_version_options: typing.Optional[typing.Union[aws_cdk.aws_lambda.VersionOptions, typing.Dict[str, typing.Any]]] = None,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        dead_letter_topic: typing.Optional[aws_cdk.aws_sns.ITopic] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        ephemeral_storage_size: typing.Optional[aws_cdk.Size] = None,
        events: typing.Optional[typing.Sequence[aws_cdk.aws_lambda.IEventSource]] = None,
        filesystem: typing.Optional[aws_cdk.aws_lambda.FileSystem] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.Sequence[aws_cdk.aws_iam.PolicyStatement]] = None,
        insights_version: typing.Optional[aws_cdk.aws_lambda.LambdaInsightsVersion] = None,
        layers: typing.Optional[typing.Sequence[aws_cdk.aws_lambda.ILayerVersion]] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        log_retention_retry_options: typing.Optional[typing.Union[aws_cdk.aws_lambda.LogRetentionRetryOptions, typing.Dict[str, typing.Any]]] = None,
        log_retention_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[aws_cdk.aws_codeguruprofiler.IProfilingGroup] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        tracing: typing.Optional[aws_cdk.aws_lambda.Tracing] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        max_event_age: typing.Optional[aws_cdk.Duration] = None,
        on_failure: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
        on_success: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param allow_all_outbound: Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Default: true
        :param allow_public_subnet: Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param architecture: The system architectures compatible with this lambda function. Default: Architecture.X86_64
        :param code_signing_config: Code signing config associated with this function. Default: - Not Sign the Code
        :param current_version_options: Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: The SQS queue to use if DLQ is enabled. If SNS topic is desired, specify ``deadLetterTopic`` property instead. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param dead_letter_topic: The SNS topic to use as a DLQ. Note that if ``deadLetterQueueEnabled`` is set to ``true``, an SQS queue will be created rather than an SNS topic. Using an SNS topic as a DLQ requires this property to be set explicitly. Default: - no SNS topic
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param ephemeral_storage_size: The size of the function’s /tmp directory in MiB. Default: 512 MiB
        :param events: Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param insights_version: Specify the version of CloudWatch Lambda insights to use for monitoring. Default: - No Lambda Insights
        :param layers: A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by multiple functions. Default: - No layers.
        :param log_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. Default: - Default AWS SDK retry options.
        :param log_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param memory_size: The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param profiling: Enable profiling. Default: - No profiling.
        :param profiling_group: Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param reserved_concurrent_executions: The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param security_groups: The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. This is required when ``vpcSubnets`` is specified. Default: - Function is not placed within a VPC.
        :param vpc_subnets: Where to place the network interfaces within the VPC. This requires ``vpc`` to be specified in order for interfaces to actually be placed in the subnets. If ``vpc`` is not specify, this will raise an error. Note: Internet access for Lambda Functions requires a NAT Gateway, so picking public subnets is not allowed (unless ``allowPublicSubnet`` is set to ``true``). Default: - the Vpc default strategy if not specified
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: The destination for failed invocations. Default: - no destination
        :param on_success: The destination for successful invocations. Default: - no destination
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                allow_all_outbound: typing.Optional[builtins.bool] = None,
                allow_public_subnet: typing.Optional[builtins.bool] = None,
                architecture: typing.Optional[aws_cdk.aws_lambda.Architecture] = None,
                code_signing_config: typing.Optional[aws_cdk.aws_lambda.ICodeSigningConfig] = None,
                current_version_options: typing.Optional[typing.Union[aws_cdk.aws_lambda.VersionOptions, typing.Dict[str, typing.Any]]] = None,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
                dead_letter_topic: typing.Optional[aws_cdk.aws_sns.ITopic] = None,
                description: typing.Optional[builtins.str] = None,
                environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                environment_encryption: typing.Optional[aws_cdk.aws_kms.IKey] = None,
                ephemeral_storage_size: typing.Optional[aws_cdk.Size] = None,
                events: typing.Optional[typing.Sequence[aws_cdk.aws_lambda.IEventSource]] = None,
                filesystem: typing.Optional[aws_cdk.aws_lambda.FileSystem] = None,
                function_name: typing.Optional[builtins.str] = None,
                initial_policy: typing.Optional[typing.Sequence[aws_cdk.aws_iam.PolicyStatement]] = None,
                insights_version: typing.Optional[aws_cdk.aws_lambda.LambdaInsightsVersion] = None,
                layers: typing.Optional[typing.Sequence[aws_cdk.aws_lambda.ILayerVersion]] = None,
                log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
                log_retention_retry_options: typing.Optional[typing.Union[aws_cdk.aws_lambda.LogRetentionRetryOptions, typing.Dict[str, typing.Any]]] = None,
                log_retention_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                memory_size: typing.Optional[jsii.Number] = None,
                profiling: typing.Optional[builtins.bool] = None,
                profiling_group: typing.Optional[aws_cdk.aws_codeguruprofiler.IProfilingGroup] = None,
                reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
                role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                tracing: typing.Optional[aws_cdk.aws_lambda.Tracing] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
                vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
                max_event_age: typing.Optional[aws_cdk.Duration] = None,
                on_failure: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
                on_success: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CalendarSetupFunctionProps(
            allow_all_outbound=allow_all_outbound,
            allow_public_subnet=allow_public_subnet,
            architecture=architecture,
            code_signing_config=code_signing_config,
            current_version_options=current_version_options,
            dead_letter_queue=dead_letter_queue,
            dead_letter_queue_enabled=dead_letter_queue_enabled,
            dead_letter_topic=dead_letter_topic,
            description=description,
            environment=environment,
            environment_encryption=environment_encryption,
            ephemeral_storage_size=ephemeral_storage_size,
            events=events,
            filesystem=filesystem,
            function_name=function_name,
            initial_policy=initial_policy,
            insights_version=insights_version,
            layers=layers,
            log_retention=log_retention,
            log_retention_retry_options=log_retention_retry_options,
            log_retention_role=log_retention_role,
            memory_size=memory_size,
            profiling=profiling,
            profiling_group=profiling_group,
            reserved_concurrent_executions=reserved_concurrent_executions,
            role=role,
            security_groups=security_groups,
            timeout=timeout,
            tracing=tracing,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cdklabs/cdk-codepipeline-extensions.CalendarSetupFunctionProps",
    jsii_struct_bases=[aws_cdk.aws_lambda.FunctionOptions],
    name_mapping={
        "max_event_age": "maxEventAge",
        "on_failure": "onFailure",
        "on_success": "onSuccess",
        "retry_attempts": "retryAttempts",
        "allow_all_outbound": "allowAllOutbound",
        "allow_public_subnet": "allowPublicSubnet",
        "architecture": "architecture",
        "code_signing_config": "codeSigningConfig",
        "current_version_options": "currentVersionOptions",
        "dead_letter_queue": "deadLetterQueue",
        "dead_letter_queue_enabled": "deadLetterQueueEnabled",
        "dead_letter_topic": "deadLetterTopic",
        "description": "description",
        "environment": "environment",
        "environment_encryption": "environmentEncryption",
        "ephemeral_storage_size": "ephemeralStorageSize",
        "events": "events",
        "filesystem": "filesystem",
        "function_name": "functionName",
        "initial_policy": "initialPolicy",
        "insights_version": "insightsVersion",
        "layers": "layers",
        "log_retention": "logRetention",
        "log_retention_retry_options": "logRetentionRetryOptions",
        "log_retention_role": "logRetentionRole",
        "memory_size": "memorySize",
        "profiling": "profiling",
        "profiling_group": "profilingGroup",
        "reserved_concurrent_executions": "reservedConcurrentExecutions",
        "role": "role",
        "security_groups": "securityGroups",
        "timeout": "timeout",
        "tracing": "tracing",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
    },
)
class CalendarSetupFunctionProps(aws_cdk.aws_lambda.FunctionOptions):
    def __init__(
        self,
        *,
        max_event_age: typing.Optional[aws_cdk.Duration] = None,
        on_failure: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
        on_success: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        architecture: typing.Optional[aws_cdk.aws_lambda.Architecture] = None,
        code_signing_config: typing.Optional[aws_cdk.aws_lambda.ICodeSigningConfig] = None,
        current_version_options: typing.Optional[typing.Union[aws_cdk.aws_lambda.VersionOptions, typing.Dict[str, typing.Any]]] = None,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        dead_letter_topic: typing.Optional[aws_cdk.aws_sns.ITopic] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        ephemeral_storage_size: typing.Optional[aws_cdk.Size] = None,
        events: typing.Optional[typing.Sequence[aws_cdk.aws_lambda.IEventSource]] = None,
        filesystem: typing.Optional[aws_cdk.aws_lambda.FileSystem] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.Sequence[aws_cdk.aws_iam.PolicyStatement]] = None,
        insights_version: typing.Optional[aws_cdk.aws_lambda.LambdaInsightsVersion] = None,
        layers: typing.Optional[typing.Sequence[aws_cdk.aws_lambda.ILayerVersion]] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        log_retention_retry_options: typing.Optional[typing.Union[aws_cdk.aws_lambda.LogRetentionRetryOptions, typing.Dict[str, typing.Any]]] = None,
        log_retention_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[aws_cdk.aws_codeguruprofiler.IProfilingGroup] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        tracing: typing.Optional[aws_cdk.aws_lambda.Tracing] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Props for CalendarSetupFunction.

        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: The destination for failed invocations. Default: - no destination
        :param on_success: The destination for successful invocations. Default: - no destination
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        :param allow_all_outbound: Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Default: true
        :param allow_public_subnet: Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param architecture: The system architectures compatible with this lambda function. Default: Architecture.X86_64
        :param code_signing_config: Code signing config associated with this function. Default: - Not Sign the Code
        :param current_version_options: Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: The SQS queue to use if DLQ is enabled. If SNS topic is desired, specify ``deadLetterTopic`` property instead. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param dead_letter_topic: The SNS topic to use as a DLQ. Note that if ``deadLetterQueueEnabled`` is set to ``true``, an SQS queue will be created rather than an SNS topic. Using an SNS topic as a DLQ requires this property to be set explicitly. Default: - no SNS topic
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param ephemeral_storage_size: The size of the function’s /tmp directory in MiB. Default: 512 MiB
        :param events: Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param insights_version: Specify the version of CloudWatch Lambda insights to use for monitoring. Default: - No Lambda Insights
        :param layers: A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by multiple functions. Default: - No layers.
        :param log_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. Default: - Default AWS SDK retry options.
        :param log_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param memory_size: The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param profiling: Enable profiling. Default: - No profiling.
        :param profiling_group: Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param reserved_concurrent_executions: The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param security_groups: The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. This is required when ``vpcSubnets`` is specified. Default: - Function is not placed within a VPC.
        :param vpc_subnets: Where to place the network interfaces within the VPC. This requires ``vpc`` to be specified in order for interfaces to actually be placed in the subnets. If ``vpc`` is not specify, this will raise an error. Note: Internet access for Lambda Functions requires a NAT Gateway, so picking public subnets is not allowed (unless ``allowPublicSubnet`` is set to ``true``). Default: - the Vpc default strategy if not specified

        :stability: experimental
        '''
        if isinstance(current_version_options, dict):
            current_version_options = aws_cdk.aws_lambda.VersionOptions(**current_version_options)
        if isinstance(log_retention_retry_options, dict):
            log_retention_retry_options = aws_cdk.aws_lambda.LogRetentionRetryOptions(**log_retention_retry_options)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = aws_cdk.aws_ec2.SubnetSelection(**vpc_subnets)
        if __debug__:
            def stub(
                *,
                max_event_age: typing.Optional[aws_cdk.Duration] = None,
                on_failure: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
                on_success: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
                allow_all_outbound: typing.Optional[builtins.bool] = None,
                allow_public_subnet: typing.Optional[builtins.bool] = None,
                architecture: typing.Optional[aws_cdk.aws_lambda.Architecture] = None,
                code_signing_config: typing.Optional[aws_cdk.aws_lambda.ICodeSigningConfig] = None,
                current_version_options: typing.Optional[typing.Union[aws_cdk.aws_lambda.VersionOptions, typing.Dict[str, typing.Any]]] = None,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
                dead_letter_topic: typing.Optional[aws_cdk.aws_sns.ITopic] = None,
                description: typing.Optional[builtins.str] = None,
                environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                environment_encryption: typing.Optional[aws_cdk.aws_kms.IKey] = None,
                ephemeral_storage_size: typing.Optional[aws_cdk.Size] = None,
                events: typing.Optional[typing.Sequence[aws_cdk.aws_lambda.IEventSource]] = None,
                filesystem: typing.Optional[aws_cdk.aws_lambda.FileSystem] = None,
                function_name: typing.Optional[builtins.str] = None,
                initial_policy: typing.Optional[typing.Sequence[aws_cdk.aws_iam.PolicyStatement]] = None,
                insights_version: typing.Optional[aws_cdk.aws_lambda.LambdaInsightsVersion] = None,
                layers: typing.Optional[typing.Sequence[aws_cdk.aws_lambda.ILayerVersion]] = None,
                log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
                log_retention_retry_options: typing.Optional[typing.Union[aws_cdk.aws_lambda.LogRetentionRetryOptions, typing.Dict[str, typing.Any]]] = None,
                log_retention_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                memory_size: typing.Optional[jsii.Number] = None,
                profiling: typing.Optional[builtins.bool] = None,
                profiling_group: typing.Optional[aws_cdk.aws_codeguruprofiler.IProfilingGroup] = None,
                reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
                role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                tracing: typing.Optional[aws_cdk.aws_lambda.Tracing] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
                vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument on_failure", value=on_failure, expected_type=type_hints["on_failure"])
            check_type(argname="argument on_success", value=on_success, expected_type=type_hints["on_success"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument allow_all_outbound", value=allow_all_outbound, expected_type=type_hints["allow_all_outbound"])
            check_type(argname="argument allow_public_subnet", value=allow_public_subnet, expected_type=type_hints["allow_public_subnet"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument code_signing_config", value=code_signing_config, expected_type=type_hints["code_signing_config"])
            check_type(argname="argument current_version_options", value=current_version_options, expected_type=type_hints["current_version_options"])
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument dead_letter_queue_enabled", value=dead_letter_queue_enabled, expected_type=type_hints["dead_letter_queue_enabled"])
            check_type(argname="argument dead_letter_topic", value=dead_letter_topic, expected_type=type_hints["dead_letter_topic"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument environment_encryption", value=environment_encryption, expected_type=type_hints["environment_encryption"])
            check_type(argname="argument ephemeral_storage_size", value=ephemeral_storage_size, expected_type=type_hints["ephemeral_storage_size"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument filesystem", value=filesystem, expected_type=type_hints["filesystem"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument initial_policy", value=initial_policy, expected_type=type_hints["initial_policy"])
            check_type(argname="argument insights_version", value=insights_version, expected_type=type_hints["insights_version"])
            check_type(argname="argument layers", value=layers, expected_type=type_hints["layers"])
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument log_retention_retry_options", value=log_retention_retry_options, expected_type=type_hints["log_retention_retry_options"])
            check_type(argname="argument log_retention_role", value=log_retention_role, expected_type=type_hints["log_retention_role"])
            check_type(argname="argument memory_size", value=memory_size, expected_type=type_hints["memory_size"])
            check_type(argname="argument profiling", value=profiling, expected_type=type_hints["profiling"])
            check_type(argname="argument profiling_group", value=profiling_group, expected_type=type_hints["profiling_group"])
            check_type(argname="argument reserved_concurrent_executions", value=reserved_concurrent_executions, expected_type=type_hints["reserved_concurrent_executions"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument tracing", value=tracing, expected_type=type_hints["tracing"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if on_success is not None:
            self._values["on_success"] = on_success
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if allow_all_outbound is not None:
            self._values["allow_all_outbound"] = allow_all_outbound
        if allow_public_subnet is not None:
            self._values["allow_public_subnet"] = allow_public_subnet
        if architecture is not None:
            self._values["architecture"] = architecture
        if code_signing_config is not None:
            self._values["code_signing_config"] = code_signing_config
        if current_version_options is not None:
            self._values["current_version_options"] = current_version_options
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if dead_letter_queue_enabled is not None:
            self._values["dead_letter_queue_enabled"] = dead_letter_queue_enabled
        if dead_letter_topic is not None:
            self._values["dead_letter_topic"] = dead_letter_topic
        if description is not None:
            self._values["description"] = description
        if environment is not None:
            self._values["environment"] = environment
        if environment_encryption is not None:
            self._values["environment_encryption"] = environment_encryption
        if ephemeral_storage_size is not None:
            self._values["ephemeral_storage_size"] = ephemeral_storage_size
        if events is not None:
            self._values["events"] = events
        if filesystem is not None:
            self._values["filesystem"] = filesystem
        if function_name is not None:
            self._values["function_name"] = function_name
        if initial_policy is not None:
            self._values["initial_policy"] = initial_policy
        if insights_version is not None:
            self._values["insights_version"] = insights_version
        if layers is not None:
            self._values["layers"] = layers
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if log_retention_retry_options is not None:
            self._values["log_retention_retry_options"] = log_retention_retry_options
        if log_retention_role is not None:
            self._values["log_retention_role"] = log_retention_role
        if memory_size is not None:
            self._values["memory_size"] = memory_size
        if profiling is not None:
            self._values["profiling"] = profiling
        if profiling_group is not None:
            self._values["profiling_group"] = profiling_group
        if reserved_concurrent_executions is not None:
            self._values["reserved_concurrent_executions"] = reserved_concurrent_executions
        if role is not None:
            self._values["role"] = role
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if timeout is not None:
            self._values["timeout"] = timeout
        if tracing is not None:
            self._values["tracing"] = tracing
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def max_event_age(self) -> typing.Optional[aws_cdk.Duration]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum: 60 seconds
        Maximum: 6 hours

        :default: Duration.hours(6)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def on_failure(self) -> typing.Optional[aws_cdk.aws_lambda.IDestination]:
        '''The destination for failed invocations.

        :default: - no destination
        '''
        result = self._values.get("on_failure")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.IDestination], result)

    @builtins.property
    def on_success(self) -> typing.Optional[aws_cdk.aws_lambda.IDestination]:
        '''The destination for successful invocations.

        :default: - no destination
        '''
        result = self._values.get("on_success")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.IDestination], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum: 0
        Maximum: 2

        :default: 2
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def allow_all_outbound(self) -> typing.Optional[builtins.bool]:
        '''Whether to allow the Lambda to send all network traffic.

        If set to false, you must individually add traffic rules to allow the
        Lambda to connect to network targets.

        :default: true
        '''
        result = self._values.get("allow_all_outbound")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_public_subnet(self) -> typing.Optional[builtins.bool]:
        '''Lambda Functions in a public subnet can NOT access the internet.

        Use this property to acknowledge this limitation and still place the function in a public subnet.

        :default: false

        :see: https://stackoverflow.com/questions/52992085/why-cant-an-aws-lambda-function-inside-a-public-subnet-in-a-vpc-connect-to-the/52994841#52994841
        '''
        result = self._values.get("allow_public_subnet")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def architecture(self) -> typing.Optional[aws_cdk.aws_lambda.Architecture]:
        '''The system architectures compatible with this lambda function.

        :default: Architecture.X86_64
        '''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.Architecture], result)

    @builtins.property
    def code_signing_config(
        self,
    ) -> typing.Optional[aws_cdk.aws_lambda.ICodeSigningConfig]:
        '''Code signing config associated with this function.

        :default: - Not Sign the Code
        '''
        result = self._values.get("code_signing_config")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.ICodeSigningConfig], result)

    @builtins.property
    def current_version_options(
        self,
    ) -> typing.Optional[aws_cdk.aws_lambda.VersionOptions]:
        '''Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method.

        :default: - default options as described in ``VersionOptions``
        '''
        result = self._values.get("current_version_options")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.VersionOptions], result)

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[aws_cdk.aws_sqs.IQueue]:
        '''The SQS queue to use if DLQ is enabled.

        If SNS topic is desired, specify ``deadLetterTopic`` property instead.

        :default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.IQueue], result)

    @builtins.property
    def dead_letter_queue_enabled(self) -> typing.Optional[builtins.bool]:
        '''Enabled DLQ.

        If ``deadLetterQueue`` is undefined,
        an SQS queue with default options will be defined for your Function.

        :default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        '''
        result = self._values.get("dead_letter_queue_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def dead_letter_topic(self) -> typing.Optional[aws_cdk.aws_sns.ITopic]:
        '''The SNS topic to use as a DLQ.

        Note that if ``deadLetterQueueEnabled`` is set to ``true``, an SQS queue will be created
        rather than an SNS topic. Using an SNS topic as a DLQ requires this property to be set explicitly.

        :default: - no SNS topic
        '''
        result = self._values.get("dead_letter_topic")
        return typing.cast(typing.Optional[aws_cdk.aws_sns.ITopic], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the function.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Key-value pairs that Lambda caches and makes available for your Lambda functions.

        Use environment variables to apply configuration changes, such
        as test and production environment configurations, without changing your
        Lambda function source code.

        :default: - No environment variables.
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def environment_encryption(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        '''The AWS KMS key that's used to encrypt your function's environment variables.

        :default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        '''
        result = self._values.get("environment_encryption")
        return typing.cast(typing.Optional[aws_cdk.aws_kms.IKey], result)

    @builtins.property
    def ephemeral_storage_size(self) -> typing.Optional[aws_cdk.Size]:
        '''The size of the function’s /tmp directory in MiB.

        :default: 512 MiB
        '''
        result = self._values.get("ephemeral_storage_size")
        return typing.cast(typing.Optional[aws_cdk.Size], result)

    @builtins.property
    def events(self) -> typing.Optional[typing.List[aws_cdk.aws_lambda.IEventSource]]:
        '''Event sources for this function.

        You can also add event sources using ``addEventSource``.

        :default: - No event sources.
        '''
        result = self._values.get("events")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_lambda.IEventSource]], result)

    @builtins.property
    def filesystem(self) -> typing.Optional[aws_cdk.aws_lambda.FileSystem]:
        '''The filesystem configuration for the lambda function.

        :default: - will not mount any filesystem
        '''
        result = self._values.get("filesystem")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.FileSystem], result)

    @builtins.property
    def function_name(self) -> typing.Optional[builtins.str]:
        '''A name for the function.

        :default:

        - AWS CloudFormation generates a unique physical ID and uses that
        ID for the function's name. For more information, see Name Type.
        '''
        result = self._values.get("function_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_policy(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]:
        '''Initial policy statements to add to the created Lambda Role.

        You can call ``addToRolePolicy`` to the created lambda to add statements post creation.

        :default: - No policy statements are added to the created Lambda role.
        '''
        result = self._values.get("initial_policy")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]], result)

    @builtins.property
    def insights_version(
        self,
    ) -> typing.Optional[aws_cdk.aws_lambda.LambdaInsightsVersion]:
        '''Specify the version of CloudWatch Lambda insights to use for monitoring.

        :default: - No Lambda Insights

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-Getting-Started-docker.html
        '''
        result = self._values.get("insights_version")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.LambdaInsightsVersion], result)

    @builtins.property
    def layers(self) -> typing.Optional[typing.List[aws_cdk.aws_lambda.ILayerVersion]]:
        '''A list of layers to add to the function's execution environment.

        You can configure your Lambda function to pull in
        additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies
        that can be used by multiple functions.

        :default: - No layers.
        '''
        result = self._values.get("layers")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_lambda.ILayerVersion]], result)

    @builtins.property
    def log_retention(self) -> typing.Optional[aws_cdk.aws_logs.RetentionDays]:
        '''The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.INFINITE
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.RetentionDays], result)

    @builtins.property
    def log_retention_retry_options(
        self,
    ) -> typing.Optional[aws_cdk.aws_lambda.LogRetentionRetryOptions]:
        '''When log retention is specified, a custom resource attempts to create the CloudWatch log group.

        These options control the retry policy when interacting with CloudWatch APIs.

        :default: - Default AWS SDK retry options.
        '''
        result = self._values.get("log_retention_retry_options")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.LogRetentionRetryOptions], result)

    @builtins.property
    def log_retention_role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''The IAM role for the Lambda function associated with the custom resource that sets the retention policy.

        :default: - A new role is created.
        '''
        result = self._values.get("log_retention_role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def memory_size(self) -> typing.Optional[jsii.Number]:
        '''The amount of memory, in MB, that is allocated to your Lambda function.

        Lambda uses this value to proportionally allocate the amount of CPU
        power. For more information, see Resource Model in the AWS Lambda
        Developer Guide.

        :default: 128
        '''
        result = self._values.get("memory_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def profiling(self) -> typing.Optional[builtins.bool]:
        '''Enable profiling.

        :default: - No profiling.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        '''
        result = self._values.get("profiling")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def profiling_group(
        self,
    ) -> typing.Optional[aws_cdk.aws_codeguruprofiler.IProfilingGroup]:
        '''Profiling Group.

        :default: - A new profiling group will be created if ``profiling`` is set.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        '''
        result = self._values.get("profiling_group")
        return typing.cast(typing.Optional[aws_cdk.aws_codeguruprofiler.IProfilingGroup], result)

    @builtins.property
    def reserved_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        '''The maximum of concurrent executions you want to reserve for the function.

        :default: - No specific limit - account limit.

        :see: https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html
        '''
        result = self._values.get("reserved_concurrent_executions")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''Lambda execution role.

        This is the role that will be assumed by the function upon execution.
        It controls the permissions that the function will have. The Role must
        be assumable by the 'lambda.amazonaws.com' service principal.

        The default Role automatically has permissions granted for Lambda execution. If you
        provide a Role, you must add the relevant AWS managed policies yourself.

        The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and
        "service-role/AWSLambdaVPCAccessExecutionRole".

        :default:

        - A unique role will be generated for this lambda function.
        Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]]:
        '''The list of security groups to associate with the Lambda's network interfaces.

        Only used if 'vpc' is supplied.

        :default:

        - If the function is placed within a VPC and a security group is
        not specified, either by this or securityGroup prop, a dedicated security
        group will be created for this function.
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.Duration]:
        '''The function execution time (in seconds) after which Lambda terminates the function.

        Because the execution time affects cost, set this value
        based on the function's expected execution time.

        :default: Duration.seconds(3)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def tracing(self) -> typing.Optional[aws_cdk.aws_lambda.Tracing]:
        '''Enable AWS X-Ray Tracing for Lambda Function.

        :default: Tracing.Disabled
        '''
        result = self._values.get("tracing")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.Tracing], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''VPC network to place Lambda network interfaces.

        Specify this if the Lambda function needs to access resources in a VPC.
        This is required when ``vpcSubnets`` is specified.

        :default: - Function is not placed within a VPC.
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''Where to place the network interfaces within the VPC.

        This requires ``vpc`` to be specified in order for interfaces to actually be
        placed in the subnets. If ``vpc`` is not specify, this will raise an error.

        Note: Internet access for Lambda Functions requires a NAT Gateway, so picking
        public subnets is not allowed (unless ``allowPublicSubnet`` is set to ``true``).

        :default: - the Vpc default strategy if not specified
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CalendarSetupFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@cdklabs/cdk-codepipeline-extensions.CalendarSourceType")
class CalendarSourceType(enum.Enum):
    '''(experimental) The source types for the calendar file.

    :stability: experimental
    '''

    S3_OBJECT = "S3_OBJECT"
    '''(experimental) The calendar source is an S3 Bucket.

    :stability: experimental
    '''
    PATH = "PATH"
    '''(experimental) The calendar source is a local path.

    :stability: experimental
    '''


class ChangeController(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-codepipeline-extensions.ChangeController",
):
    '''(experimental) A change controller.

    When added to a stage in a pipeline, this will check against
    a calendar and enable or disable the stage transition based off that calendar,
    defaulting to closed when the calendar cannot be found or when
    the check against it fails. It also checks to against alarms.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        calendar: Calendar,
        schedule: aws_cdk.aws_events.Schedule,
        search_terms: typing.Sequence[builtins.str],
        stage: aws_cdk.aws_codepipeline.IStage,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param calendar: (experimental) The calendar object.
        :param schedule: (experimental) The schedule on which to check the calendar and alarm state.
        :param search_terms: (experimental) The terms to search for in alarm descriptions. These if these alarms are in ALARM state, the change controller will close the pipeline stage.
        :param stage: (experimental) The pipeline stage.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                calendar: Calendar,
                schedule: aws_cdk.aws_events.Schedule,
                search_terms: typing.Sequence[builtins.str],
                stage: aws_cdk.aws_codepipeline.IStage,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ChangeControllerProps(
            calendar=calendar,
            schedule=schedule,
            search_terms=search_terms,
            stage=stage,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cdklabs/cdk-codepipeline-extensions.ChangeControllerEvent",
    jsii_struct_bases=[],
    name_mapping={
        "calendar": "calendar",
        "pipeline_name": "pipelineName",
        "search_terms": "searchTerms",
        "stage_name": "stageName",
    },
)
class ChangeControllerEvent:
    def __init__(
        self,
        *,
        calendar: Calendar,
        pipeline_name: builtins.str,
        search_terms: typing.Sequence[builtins.str],
        stage_name: builtins.str,
    ) -> None:
        '''(experimental) The event inputs required for the ChangeController lambda function.

        :param calendar: (experimental) The calendar used to determine whether a stage transition should be opened or closed.
        :param pipeline_name: (experimental) The name of the pipeline the Change Controller will be added to.
        :param search_terms: (experimental) The terms in alarm descriptions to seach for to determine if alarms should be checked. If any of the alarms matching these search terms are in ALARM state, the stage transition will be closed.
        :param stage_name: (experimental) The name of the stage the Change Controller will be added to.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                calendar: Calendar,
                pipeline_name: builtins.str,
                search_terms: typing.Sequence[builtins.str],
                stage_name: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument calendar", value=calendar, expected_type=type_hints["calendar"])
            check_type(argname="argument pipeline_name", value=pipeline_name, expected_type=type_hints["pipeline_name"])
            check_type(argname="argument search_terms", value=search_terms, expected_type=type_hints["search_terms"])
            check_type(argname="argument stage_name", value=stage_name, expected_type=type_hints["stage_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "calendar": calendar,
            "pipeline_name": pipeline_name,
            "search_terms": search_terms,
            "stage_name": stage_name,
        }

    @builtins.property
    def calendar(self) -> Calendar:
        '''(experimental) The calendar used to determine whether a stage transition should be opened or closed.

        :stability: experimental
        '''
        result = self._values.get("calendar")
        assert result is not None, "Required property 'calendar' is missing"
        return typing.cast(Calendar, result)

    @builtins.property
    def pipeline_name(self) -> builtins.str:
        '''(experimental) The name of the pipeline the Change Controller will be added to.

        :stability: experimental
        '''
        result = self._values.get("pipeline_name")
        assert result is not None, "Required property 'pipeline_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def search_terms(self) -> typing.List[builtins.str]:
        '''(experimental) The terms in alarm descriptions to seach for to determine if alarms should be checked.

        If any of the alarms matching these search terms are in ALARM state, the stage transition will be closed.

        :stability: experimental
        '''
        result = self._values.get("search_terms")
        assert result is not None, "Required property 'search_terms' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def stage_name(self) -> builtins.str:
        '''(experimental) The name of the stage the Change Controller will be added to.

        :stability: experimental
        '''
        result = self._values.get("stage_name")
        assert result is not None, "Required property 'stage_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChangeControllerEvent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ChangeControllerFunction(
    aws_cdk.aws_lambda.Function,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-codepipeline-extensions.ChangeControllerFunction",
):
    '''(experimental) An AWS Lambda function which executes src/time-windows/change-controller/change-controller.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        architecture: typing.Optional[aws_cdk.aws_lambda.Architecture] = None,
        code_signing_config: typing.Optional[aws_cdk.aws_lambda.ICodeSigningConfig] = None,
        current_version_options: typing.Optional[typing.Union[aws_cdk.aws_lambda.VersionOptions, typing.Dict[str, typing.Any]]] = None,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        dead_letter_topic: typing.Optional[aws_cdk.aws_sns.ITopic] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        ephemeral_storage_size: typing.Optional[aws_cdk.Size] = None,
        events: typing.Optional[typing.Sequence[aws_cdk.aws_lambda.IEventSource]] = None,
        filesystem: typing.Optional[aws_cdk.aws_lambda.FileSystem] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.Sequence[aws_cdk.aws_iam.PolicyStatement]] = None,
        insights_version: typing.Optional[aws_cdk.aws_lambda.LambdaInsightsVersion] = None,
        layers: typing.Optional[typing.Sequence[aws_cdk.aws_lambda.ILayerVersion]] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        log_retention_retry_options: typing.Optional[typing.Union[aws_cdk.aws_lambda.LogRetentionRetryOptions, typing.Dict[str, typing.Any]]] = None,
        log_retention_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[aws_cdk.aws_codeguruprofiler.IProfilingGroup] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        tracing: typing.Optional[aws_cdk.aws_lambda.Tracing] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        max_event_age: typing.Optional[aws_cdk.Duration] = None,
        on_failure: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
        on_success: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param allow_all_outbound: Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Default: true
        :param allow_public_subnet: Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param architecture: The system architectures compatible with this lambda function. Default: Architecture.X86_64
        :param code_signing_config: Code signing config associated with this function. Default: - Not Sign the Code
        :param current_version_options: Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: The SQS queue to use if DLQ is enabled. If SNS topic is desired, specify ``deadLetterTopic`` property instead. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param dead_letter_topic: The SNS topic to use as a DLQ. Note that if ``deadLetterQueueEnabled`` is set to ``true``, an SQS queue will be created rather than an SNS topic. Using an SNS topic as a DLQ requires this property to be set explicitly. Default: - no SNS topic
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param ephemeral_storage_size: The size of the function’s /tmp directory in MiB. Default: 512 MiB
        :param events: Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param insights_version: Specify the version of CloudWatch Lambda insights to use for monitoring. Default: - No Lambda Insights
        :param layers: A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by multiple functions. Default: - No layers.
        :param log_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. Default: - Default AWS SDK retry options.
        :param log_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param memory_size: The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param profiling: Enable profiling. Default: - No profiling.
        :param profiling_group: Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param reserved_concurrent_executions: The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param security_groups: The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. This is required when ``vpcSubnets`` is specified. Default: - Function is not placed within a VPC.
        :param vpc_subnets: Where to place the network interfaces within the VPC. This requires ``vpc`` to be specified in order for interfaces to actually be placed in the subnets. If ``vpc`` is not specify, this will raise an error. Note: Internet access for Lambda Functions requires a NAT Gateway, so picking public subnets is not allowed (unless ``allowPublicSubnet`` is set to ``true``). Default: - the Vpc default strategy if not specified
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: The destination for failed invocations. Default: - no destination
        :param on_success: The destination for successful invocations. Default: - no destination
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                allow_all_outbound: typing.Optional[builtins.bool] = None,
                allow_public_subnet: typing.Optional[builtins.bool] = None,
                architecture: typing.Optional[aws_cdk.aws_lambda.Architecture] = None,
                code_signing_config: typing.Optional[aws_cdk.aws_lambda.ICodeSigningConfig] = None,
                current_version_options: typing.Optional[typing.Union[aws_cdk.aws_lambda.VersionOptions, typing.Dict[str, typing.Any]]] = None,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
                dead_letter_topic: typing.Optional[aws_cdk.aws_sns.ITopic] = None,
                description: typing.Optional[builtins.str] = None,
                environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                environment_encryption: typing.Optional[aws_cdk.aws_kms.IKey] = None,
                ephemeral_storage_size: typing.Optional[aws_cdk.Size] = None,
                events: typing.Optional[typing.Sequence[aws_cdk.aws_lambda.IEventSource]] = None,
                filesystem: typing.Optional[aws_cdk.aws_lambda.FileSystem] = None,
                function_name: typing.Optional[builtins.str] = None,
                initial_policy: typing.Optional[typing.Sequence[aws_cdk.aws_iam.PolicyStatement]] = None,
                insights_version: typing.Optional[aws_cdk.aws_lambda.LambdaInsightsVersion] = None,
                layers: typing.Optional[typing.Sequence[aws_cdk.aws_lambda.ILayerVersion]] = None,
                log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
                log_retention_retry_options: typing.Optional[typing.Union[aws_cdk.aws_lambda.LogRetentionRetryOptions, typing.Dict[str, typing.Any]]] = None,
                log_retention_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                memory_size: typing.Optional[jsii.Number] = None,
                profiling: typing.Optional[builtins.bool] = None,
                profiling_group: typing.Optional[aws_cdk.aws_codeguruprofiler.IProfilingGroup] = None,
                reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
                role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                tracing: typing.Optional[aws_cdk.aws_lambda.Tracing] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
                vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
                max_event_age: typing.Optional[aws_cdk.Duration] = None,
                on_failure: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
                on_success: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ChangeControllerFunctionProps(
            allow_all_outbound=allow_all_outbound,
            allow_public_subnet=allow_public_subnet,
            architecture=architecture,
            code_signing_config=code_signing_config,
            current_version_options=current_version_options,
            dead_letter_queue=dead_letter_queue,
            dead_letter_queue_enabled=dead_letter_queue_enabled,
            dead_letter_topic=dead_letter_topic,
            description=description,
            environment=environment,
            environment_encryption=environment_encryption,
            ephemeral_storage_size=ephemeral_storage_size,
            events=events,
            filesystem=filesystem,
            function_name=function_name,
            initial_policy=initial_policy,
            insights_version=insights_version,
            layers=layers,
            log_retention=log_retention,
            log_retention_retry_options=log_retention_retry_options,
            log_retention_role=log_retention_role,
            memory_size=memory_size,
            profiling=profiling,
            profiling_group=profiling_group,
            reserved_concurrent_executions=reserved_concurrent_executions,
            role=role,
            security_groups=security_groups,
            timeout=timeout,
            tracing=tracing,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cdklabs/cdk-codepipeline-extensions.ChangeControllerFunctionProps",
    jsii_struct_bases=[aws_cdk.aws_lambda.FunctionOptions],
    name_mapping={
        "max_event_age": "maxEventAge",
        "on_failure": "onFailure",
        "on_success": "onSuccess",
        "retry_attempts": "retryAttempts",
        "allow_all_outbound": "allowAllOutbound",
        "allow_public_subnet": "allowPublicSubnet",
        "architecture": "architecture",
        "code_signing_config": "codeSigningConfig",
        "current_version_options": "currentVersionOptions",
        "dead_letter_queue": "deadLetterQueue",
        "dead_letter_queue_enabled": "deadLetterQueueEnabled",
        "dead_letter_topic": "deadLetterTopic",
        "description": "description",
        "environment": "environment",
        "environment_encryption": "environmentEncryption",
        "ephemeral_storage_size": "ephemeralStorageSize",
        "events": "events",
        "filesystem": "filesystem",
        "function_name": "functionName",
        "initial_policy": "initialPolicy",
        "insights_version": "insightsVersion",
        "layers": "layers",
        "log_retention": "logRetention",
        "log_retention_retry_options": "logRetentionRetryOptions",
        "log_retention_role": "logRetentionRole",
        "memory_size": "memorySize",
        "profiling": "profiling",
        "profiling_group": "profilingGroup",
        "reserved_concurrent_executions": "reservedConcurrentExecutions",
        "role": "role",
        "security_groups": "securityGroups",
        "timeout": "timeout",
        "tracing": "tracing",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
    },
)
class ChangeControllerFunctionProps(aws_cdk.aws_lambda.FunctionOptions):
    def __init__(
        self,
        *,
        max_event_age: typing.Optional[aws_cdk.Duration] = None,
        on_failure: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
        on_success: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        architecture: typing.Optional[aws_cdk.aws_lambda.Architecture] = None,
        code_signing_config: typing.Optional[aws_cdk.aws_lambda.ICodeSigningConfig] = None,
        current_version_options: typing.Optional[typing.Union[aws_cdk.aws_lambda.VersionOptions, typing.Dict[str, typing.Any]]] = None,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        dead_letter_topic: typing.Optional[aws_cdk.aws_sns.ITopic] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        ephemeral_storage_size: typing.Optional[aws_cdk.Size] = None,
        events: typing.Optional[typing.Sequence[aws_cdk.aws_lambda.IEventSource]] = None,
        filesystem: typing.Optional[aws_cdk.aws_lambda.FileSystem] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.Sequence[aws_cdk.aws_iam.PolicyStatement]] = None,
        insights_version: typing.Optional[aws_cdk.aws_lambda.LambdaInsightsVersion] = None,
        layers: typing.Optional[typing.Sequence[aws_cdk.aws_lambda.ILayerVersion]] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        log_retention_retry_options: typing.Optional[typing.Union[aws_cdk.aws_lambda.LogRetentionRetryOptions, typing.Dict[str, typing.Any]]] = None,
        log_retention_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[aws_cdk.aws_codeguruprofiler.IProfilingGroup] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        tracing: typing.Optional[aws_cdk.aws_lambda.Tracing] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Props for ChangeControllerFunction.

        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: The destination for failed invocations. Default: - no destination
        :param on_success: The destination for successful invocations. Default: - no destination
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        :param allow_all_outbound: Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Default: true
        :param allow_public_subnet: Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param architecture: The system architectures compatible with this lambda function. Default: Architecture.X86_64
        :param code_signing_config: Code signing config associated with this function. Default: - Not Sign the Code
        :param current_version_options: Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: The SQS queue to use if DLQ is enabled. If SNS topic is desired, specify ``deadLetterTopic`` property instead. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param dead_letter_topic: The SNS topic to use as a DLQ. Note that if ``deadLetterQueueEnabled`` is set to ``true``, an SQS queue will be created rather than an SNS topic. Using an SNS topic as a DLQ requires this property to be set explicitly. Default: - no SNS topic
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param ephemeral_storage_size: The size of the function’s /tmp directory in MiB. Default: 512 MiB
        :param events: Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param insights_version: Specify the version of CloudWatch Lambda insights to use for monitoring. Default: - No Lambda Insights
        :param layers: A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by multiple functions. Default: - No layers.
        :param log_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. Default: - Default AWS SDK retry options.
        :param log_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param memory_size: The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param profiling: Enable profiling. Default: - No profiling.
        :param profiling_group: Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param reserved_concurrent_executions: The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param security_groups: The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. This is required when ``vpcSubnets`` is specified. Default: - Function is not placed within a VPC.
        :param vpc_subnets: Where to place the network interfaces within the VPC. This requires ``vpc`` to be specified in order for interfaces to actually be placed in the subnets. If ``vpc`` is not specify, this will raise an error. Note: Internet access for Lambda Functions requires a NAT Gateway, so picking public subnets is not allowed (unless ``allowPublicSubnet`` is set to ``true``). Default: - the Vpc default strategy if not specified

        :stability: experimental
        '''
        if isinstance(current_version_options, dict):
            current_version_options = aws_cdk.aws_lambda.VersionOptions(**current_version_options)
        if isinstance(log_retention_retry_options, dict):
            log_retention_retry_options = aws_cdk.aws_lambda.LogRetentionRetryOptions(**log_retention_retry_options)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = aws_cdk.aws_ec2.SubnetSelection(**vpc_subnets)
        if __debug__:
            def stub(
                *,
                max_event_age: typing.Optional[aws_cdk.Duration] = None,
                on_failure: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
                on_success: typing.Optional[aws_cdk.aws_lambda.IDestination] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
                allow_all_outbound: typing.Optional[builtins.bool] = None,
                allow_public_subnet: typing.Optional[builtins.bool] = None,
                architecture: typing.Optional[aws_cdk.aws_lambda.Architecture] = None,
                code_signing_config: typing.Optional[aws_cdk.aws_lambda.ICodeSigningConfig] = None,
                current_version_options: typing.Optional[typing.Union[aws_cdk.aws_lambda.VersionOptions, typing.Dict[str, typing.Any]]] = None,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
                dead_letter_topic: typing.Optional[aws_cdk.aws_sns.ITopic] = None,
                description: typing.Optional[builtins.str] = None,
                environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                environment_encryption: typing.Optional[aws_cdk.aws_kms.IKey] = None,
                ephemeral_storage_size: typing.Optional[aws_cdk.Size] = None,
                events: typing.Optional[typing.Sequence[aws_cdk.aws_lambda.IEventSource]] = None,
                filesystem: typing.Optional[aws_cdk.aws_lambda.FileSystem] = None,
                function_name: typing.Optional[builtins.str] = None,
                initial_policy: typing.Optional[typing.Sequence[aws_cdk.aws_iam.PolicyStatement]] = None,
                insights_version: typing.Optional[aws_cdk.aws_lambda.LambdaInsightsVersion] = None,
                layers: typing.Optional[typing.Sequence[aws_cdk.aws_lambda.ILayerVersion]] = None,
                log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
                log_retention_retry_options: typing.Optional[typing.Union[aws_cdk.aws_lambda.LogRetentionRetryOptions, typing.Dict[str, typing.Any]]] = None,
                log_retention_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                memory_size: typing.Optional[jsii.Number] = None,
                profiling: typing.Optional[builtins.bool] = None,
                profiling_group: typing.Optional[aws_cdk.aws_codeguruprofiler.IProfilingGroup] = None,
                reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
                role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                tracing: typing.Optional[aws_cdk.aws_lambda.Tracing] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
                vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument on_failure", value=on_failure, expected_type=type_hints["on_failure"])
            check_type(argname="argument on_success", value=on_success, expected_type=type_hints["on_success"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument allow_all_outbound", value=allow_all_outbound, expected_type=type_hints["allow_all_outbound"])
            check_type(argname="argument allow_public_subnet", value=allow_public_subnet, expected_type=type_hints["allow_public_subnet"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument code_signing_config", value=code_signing_config, expected_type=type_hints["code_signing_config"])
            check_type(argname="argument current_version_options", value=current_version_options, expected_type=type_hints["current_version_options"])
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument dead_letter_queue_enabled", value=dead_letter_queue_enabled, expected_type=type_hints["dead_letter_queue_enabled"])
            check_type(argname="argument dead_letter_topic", value=dead_letter_topic, expected_type=type_hints["dead_letter_topic"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument environment_encryption", value=environment_encryption, expected_type=type_hints["environment_encryption"])
            check_type(argname="argument ephemeral_storage_size", value=ephemeral_storage_size, expected_type=type_hints["ephemeral_storage_size"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument filesystem", value=filesystem, expected_type=type_hints["filesystem"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument initial_policy", value=initial_policy, expected_type=type_hints["initial_policy"])
            check_type(argname="argument insights_version", value=insights_version, expected_type=type_hints["insights_version"])
            check_type(argname="argument layers", value=layers, expected_type=type_hints["layers"])
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument log_retention_retry_options", value=log_retention_retry_options, expected_type=type_hints["log_retention_retry_options"])
            check_type(argname="argument log_retention_role", value=log_retention_role, expected_type=type_hints["log_retention_role"])
            check_type(argname="argument memory_size", value=memory_size, expected_type=type_hints["memory_size"])
            check_type(argname="argument profiling", value=profiling, expected_type=type_hints["profiling"])
            check_type(argname="argument profiling_group", value=profiling_group, expected_type=type_hints["profiling_group"])
            check_type(argname="argument reserved_concurrent_executions", value=reserved_concurrent_executions, expected_type=type_hints["reserved_concurrent_executions"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument tracing", value=tracing, expected_type=type_hints["tracing"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if on_success is not None:
            self._values["on_success"] = on_success
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if allow_all_outbound is not None:
            self._values["allow_all_outbound"] = allow_all_outbound
        if allow_public_subnet is not None:
            self._values["allow_public_subnet"] = allow_public_subnet
        if architecture is not None:
            self._values["architecture"] = architecture
        if code_signing_config is not None:
            self._values["code_signing_config"] = code_signing_config
        if current_version_options is not None:
            self._values["current_version_options"] = current_version_options
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if dead_letter_queue_enabled is not None:
            self._values["dead_letter_queue_enabled"] = dead_letter_queue_enabled
        if dead_letter_topic is not None:
            self._values["dead_letter_topic"] = dead_letter_topic
        if description is not None:
            self._values["description"] = description
        if environment is not None:
            self._values["environment"] = environment
        if environment_encryption is not None:
            self._values["environment_encryption"] = environment_encryption
        if ephemeral_storage_size is not None:
            self._values["ephemeral_storage_size"] = ephemeral_storage_size
        if events is not None:
            self._values["events"] = events
        if filesystem is not None:
            self._values["filesystem"] = filesystem
        if function_name is not None:
            self._values["function_name"] = function_name
        if initial_policy is not None:
            self._values["initial_policy"] = initial_policy
        if insights_version is not None:
            self._values["insights_version"] = insights_version
        if layers is not None:
            self._values["layers"] = layers
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if log_retention_retry_options is not None:
            self._values["log_retention_retry_options"] = log_retention_retry_options
        if log_retention_role is not None:
            self._values["log_retention_role"] = log_retention_role
        if memory_size is not None:
            self._values["memory_size"] = memory_size
        if profiling is not None:
            self._values["profiling"] = profiling
        if profiling_group is not None:
            self._values["profiling_group"] = profiling_group
        if reserved_concurrent_executions is not None:
            self._values["reserved_concurrent_executions"] = reserved_concurrent_executions
        if role is not None:
            self._values["role"] = role
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if timeout is not None:
            self._values["timeout"] = timeout
        if tracing is not None:
            self._values["tracing"] = tracing
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def max_event_age(self) -> typing.Optional[aws_cdk.Duration]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum: 60 seconds
        Maximum: 6 hours

        :default: Duration.hours(6)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def on_failure(self) -> typing.Optional[aws_cdk.aws_lambda.IDestination]:
        '''The destination for failed invocations.

        :default: - no destination
        '''
        result = self._values.get("on_failure")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.IDestination], result)

    @builtins.property
    def on_success(self) -> typing.Optional[aws_cdk.aws_lambda.IDestination]:
        '''The destination for successful invocations.

        :default: - no destination
        '''
        result = self._values.get("on_success")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.IDestination], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum: 0
        Maximum: 2

        :default: 2
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def allow_all_outbound(self) -> typing.Optional[builtins.bool]:
        '''Whether to allow the Lambda to send all network traffic.

        If set to false, you must individually add traffic rules to allow the
        Lambda to connect to network targets.

        :default: true
        '''
        result = self._values.get("allow_all_outbound")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_public_subnet(self) -> typing.Optional[builtins.bool]:
        '''Lambda Functions in a public subnet can NOT access the internet.

        Use this property to acknowledge this limitation and still place the function in a public subnet.

        :default: false

        :see: https://stackoverflow.com/questions/52992085/why-cant-an-aws-lambda-function-inside-a-public-subnet-in-a-vpc-connect-to-the/52994841#52994841
        '''
        result = self._values.get("allow_public_subnet")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def architecture(self) -> typing.Optional[aws_cdk.aws_lambda.Architecture]:
        '''The system architectures compatible with this lambda function.

        :default: Architecture.X86_64
        '''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.Architecture], result)

    @builtins.property
    def code_signing_config(
        self,
    ) -> typing.Optional[aws_cdk.aws_lambda.ICodeSigningConfig]:
        '''Code signing config associated with this function.

        :default: - Not Sign the Code
        '''
        result = self._values.get("code_signing_config")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.ICodeSigningConfig], result)

    @builtins.property
    def current_version_options(
        self,
    ) -> typing.Optional[aws_cdk.aws_lambda.VersionOptions]:
        '''Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method.

        :default: - default options as described in ``VersionOptions``
        '''
        result = self._values.get("current_version_options")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.VersionOptions], result)

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[aws_cdk.aws_sqs.IQueue]:
        '''The SQS queue to use if DLQ is enabled.

        If SNS topic is desired, specify ``deadLetterTopic`` property instead.

        :default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.IQueue], result)

    @builtins.property
    def dead_letter_queue_enabled(self) -> typing.Optional[builtins.bool]:
        '''Enabled DLQ.

        If ``deadLetterQueue`` is undefined,
        an SQS queue with default options will be defined for your Function.

        :default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        '''
        result = self._values.get("dead_letter_queue_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def dead_letter_topic(self) -> typing.Optional[aws_cdk.aws_sns.ITopic]:
        '''The SNS topic to use as a DLQ.

        Note that if ``deadLetterQueueEnabled`` is set to ``true``, an SQS queue will be created
        rather than an SNS topic. Using an SNS topic as a DLQ requires this property to be set explicitly.

        :default: - no SNS topic
        '''
        result = self._values.get("dead_letter_topic")
        return typing.cast(typing.Optional[aws_cdk.aws_sns.ITopic], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the function.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Key-value pairs that Lambda caches and makes available for your Lambda functions.

        Use environment variables to apply configuration changes, such
        as test and production environment configurations, without changing your
        Lambda function source code.

        :default: - No environment variables.
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def environment_encryption(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        '''The AWS KMS key that's used to encrypt your function's environment variables.

        :default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        '''
        result = self._values.get("environment_encryption")
        return typing.cast(typing.Optional[aws_cdk.aws_kms.IKey], result)

    @builtins.property
    def ephemeral_storage_size(self) -> typing.Optional[aws_cdk.Size]:
        '''The size of the function’s /tmp directory in MiB.

        :default: 512 MiB
        '''
        result = self._values.get("ephemeral_storage_size")
        return typing.cast(typing.Optional[aws_cdk.Size], result)

    @builtins.property
    def events(self) -> typing.Optional[typing.List[aws_cdk.aws_lambda.IEventSource]]:
        '''Event sources for this function.

        You can also add event sources using ``addEventSource``.

        :default: - No event sources.
        '''
        result = self._values.get("events")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_lambda.IEventSource]], result)

    @builtins.property
    def filesystem(self) -> typing.Optional[aws_cdk.aws_lambda.FileSystem]:
        '''The filesystem configuration for the lambda function.

        :default: - will not mount any filesystem
        '''
        result = self._values.get("filesystem")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.FileSystem], result)

    @builtins.property
    def function_name(self) -> typing.Optional[builtins.str]:
        '''A name for the function.

        :default:

        - AWS CloudFormation generates a unique physical ID and uses that
        ID for the function's name. For more information, see Name Type.
        '''
        result = self._values.get("function_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_policy(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]:
        '''Initial policy statements to add to the created Lambda Role.

        You can call ``addToRolePolicy`` to the created lambda to add statements post creation.

        :default: - No policy statements are added to the created Lambda role.
        '''
        result = self._values.get("initial_policy")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]], result)

    @builtins.property
    def insights_version(
        self,
    ) -> typing.Optional[aws_cdk.aws_lambda.LambdaInsightsVersion]:
        '''Specify the version of CloudWatch Lambda insights to use for monitoring.

        :default: - No Lambda Insights

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-Getting-Started-docker.html
        '''
        result = self._values.get("insights_version")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.LambdaInsightsVersion], result)

    @builtins.property
    def layers(self) -> typing.Optional[typing.List[aws_cdk.aws_lambda.ILayerVersion]]:
        '''A list of layers to add to the function's execution environment.

        You can configure your Lambda function to pull in
        additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies
        that can be used by multiple functions.

        :default: - No layers.
        '''
        result = self._values.get("layers")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_lambda.ILayerVersion]], result)

    @builtins.property
    def log_retention(self) -> typing.Optional[aws_cdk.aws_logs.RetentionDays]:
        '''The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.INFINITE
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.RetentionDays], result)

    @builtins.property
    def log_retention_retry_options(
        self,
    ) -> typing.Optional[aws_cdk.aws_lambda.LogRetentionRetryOptions]:
        '''When log retention is specified, a custom resource attempts to create the CloudWatch log group.

        These options control the retry policy when interacting with CloudWatch APIs.

        :default: - Default AWS SDK retry options.
        '''
        result = self._values.get("log_retention_retry_options")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.LogRetentionRetryOptions], result)

    @builtins.property
    def log_retention_role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''The IAM role for the Lambda function associated with the custom resource that sets the retention policy.

        :default: - A new role is created.
        '''
        result = self._values.get("log_retention_role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def memory_size(self) -> typing.Optional[jsii.Number]:
        '''The amount of memory, in MB, that is allocated to your Lambda function.

        Lambda uses this value to proportionally allocate the amount of CPU
        power. For more information, see Resource Model in the AWS Lambda
        Developer Guide.

        :default: 128
        '''
        result = self._values.get("memory_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def profiling(self) -> typing.Optional[builtins.bool]:
        '''Enable profiling.

        :default: - No profiling.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        '''
        result = self._values.get("profiling")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def profiling_group(
        self,
    ) -> typing.Optional[aws_cdk.aws_codeguruprofiler.IProfilingGroup]:
        '''Profiling Group.

        :default: - A new profiling group will be created if ``profiling`` is set.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        '''
        result = self._values.get("profiling_group")
        return typing.cast(typing.Optional[aws_cdk.aws_codeguruprofiler.IProfilingGroup], result)

    @builtins.property
    def reserved_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        '''The maximum of concurrent executions you want to reserve for the function.

        :default: - No specific limit - account limit.

        :see: https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html
        '''
        result = self._values.get("reserved_concurrent_executions")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''Lambda execution role.

        This is the role that will be assumed by the function upon execution.
        It controls the permissions that the function will have. The Role must
        be assumable by the 'lambda.amazonaws.com' service principal.

        The default Role automatically has permissions granted for Lambda execution. If you
        provide a Role, you must add the relevant AWS managed policies yourself.

        The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and
        "service-role/AWSLambdaVPCAccessExecutionRole".

        :default:

        - A unique role will be generated for this lambda function.
        Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]]:
        '''The list of security groups to associate with the Lambda's network interfaces.

        Only used if 'vpc' is supplied.

        :default:

        - If the function is placed within a VPC and a security group is
        not specified, either by this or securityGroup prop, a dedicated security
        group will be created for this function.
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.Duration]:
        '''The function execution time (in seconds) after which Lambda terminates the function.

        Because the execution time affects cost, set this value
        based on the function's expected execution time.

        :default: Duration.seconds(3)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def tracing(self) -> typing.Optional[aws_cdk.aws_lambda.Tracing]:
        '''Enable AWS X-Ray Tracing for Lambda Function.

        :default: Tracing.Disabled
        '''
        result = self._values.get("tracing")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.Tracing], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''VPC network to place Lambda network interfaces.

        Specify this if the Lambda function needs to access resources in a VPC.
        This is required when ``vpcSubnets`` is specified.

        :default: - Function is not placed within a VPC.
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''Where to place the network interfaces within the VPC.

        This requires ``vpc`` to be specified in order for interfaces to actually be
        placed in the subnets. If ``vpc`` is not specify, this will raise an error.

        Note: Internet access for Lambda Functions requires a NAT Gateway, so picking
        public subnets is not allowed (unless ``allowPublicSubnet`` is set to ``true``).

        :default: - the Vpc default strategy if not specified
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChangeControllerFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-codepipeline-extensions.ChangeControllerProps",
    jsii_struct_bases=[],
    name_mapping={
        "calendar": "calendar",
        "schedule": "schedule",
        "search_terms": "searchTerms",
        "stage": "stage",
    },
)
class ChangeControllerProps:
    def __init__(
        self,
        *,
        calendar: Calendar,
        schedule: aws_cdk.aws_events.Schedule,
        search_terms: typing.Sequence[builtins.str],
        stage: aws_cdk.aws_codepipeline.IStage,
    ) -> None:
        '''(experimental) Properties used to create change controller.

        :param calendar: (experimental) The calendar object.
        :param schedule: (experimental) The schedule on which to check the calendar and alarm state.
        :param search_terms: (experimental) The terms to search for in alarm descriptions. These if these alarms are in ALARM state, the change controller will close the pipeline stage.
        :param stage: (experimental) The pipeline stage.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                calendar: Calendar,
                schedule: aws_cdk.aws_events.Schedule,
                search_terms: typing.Sequence[builtins.str],
                stage: aws_cdk.aws_codepipeline.IStage,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument calendar", value=calendar, expected_type=type_hints["calendar"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument search_terms", value=search_terms, expected_type=type_hints["search_terms"])
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
        self._values: typing.Dict[str, typing.Any] = {
            "calendar": calendar,
            "schedule": schedule,
            "search_terms": search_terms,
            "stage": stage,
        }

    @builtins.property
    def calendar(self) -> Calendar:
        '''(experimental) The calendar object.

        :stability: experimental
        '''
        result = self._values.get("calendar")
        assert result is not None, "Required property 'calendar' is missing"
        return typing.cast(Calendar, result)

    @builtins.property
    def schedule(self) -> aws_cdk.aws_events.Schedule:
        '''(experimental) The schedule on which to check the calendar and alarm state.

        :stability: experimental
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast(aws_cdk.aws_events.Schedule, result)

    @builtins.property
    def search_terms(self) -> typing.List[builtins.str]:
        '''(experimental) The terms to search for in alarm descriptions.

        These if these alarms are in ALARM state, the change controller will close
        the pipeline stage.

        :stability: experimental
        '''
        result = self._values.get("search_terms")
        assert result is not None, "Required property 'search_terms' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def stage(self) -> aws_cdk.aws_codepipeline.IStage:
        '''(experimental) The pipeline stage.

        :stability: experimental
        '''
        result = self._values.get("stage")
        assert result is not None, "Required property 'stage' is missing"
        return typing.cast(aws_cdk.aws_codepipeline.IStage, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChangeControllerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-codepipeline-extensions.GetAlarmStateOptions",
    jsii_struct_bases=[],
    name_mapping={"search_terms": "searchTerms"},
)
class GetAlarmStateOptions:
    def __init__(self, *, search_terms: typing.Sequence[builtins.str]) -> None:
        '''(experimental) searchTerms: a list of terms to match in the alarm description.

        :param search_terms: 

        :stability: experimental
        '''
        if __debug__:
            def stub(*, search_terms: typing.Sequence[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument search_terms", value=search_terms, expected_type=type_hints["search_terms"])
        self._values: typing.Dict[str, typing.Any] = {
            "search_terms": search_terms,
        }

    @builtins.property
    def search_terms(self) -> typing.List[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("search_terms")
        assert result is not None, "Required property 'search_terms' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GetAlarmStateOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@cdklabs/cdk-codepipeline-extensions.IAlarmDetail")
class IAlarmDetail(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="alarmArn")
    def alarm_arn(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="alarmDescription")
    def alarm_description(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="reason")
    def reason(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        ...

    @reason.setter
    def reason(self, value: builtins.str) -> None:
        ...


class _IAlarmDetailProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/cdk-codepipeline-extensions.IAlarmDetail"

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="alarmArn")
    def alarm_arn(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alarmArn"))

    @builtins.property
    @jsii.member(jsii_name="alarmDescription")
    def alarm_description(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alarmDescription"))

    @builtins.property
    @jsii.member(jsii_name="reason")
    def reason(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "reason"))

    @reason.setter
    def reason(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reason", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAlarmDetail).__jsii_proxy_class__ = lambda : _IAlarmDetailProxy


@jsii.data_type(
    jsii_type="@cdklabs/cdk-codepipeline-extensions.LocalPathOptions",
    jsii_struct_bases=[CalendarLocationOptionsBase],
    name_mapping={"calendar_name": "calendarName", "calendar_path": "calendarPath"},
)
class LocalPathOptions(CalendarLocationOptionsBase):
    def __init__(
        self,
        *,
        calendar_name: builtins.str,
        calendar_path: builtins.str,
    ) -> None:
        '''(experimental) Options for creating a calendar from a local file path.

        :param calendar_name: (experimental) The name of the calendar file.
        :param calendar_path: (experimental) The relative path to the calendar file.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                calendar_name: builtins.str,
                calendar_path: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument calendar_name", value=calendar_name, expected_type=type_hints["calendar_name"])
            check_type(argname="argument calendar_path", value=calendar_path, expected_type=type_hints["calendar_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "calendar_name": calendar_name,
            "calendar_path": calendar_path,
        }

    @builtins.property
    def calendar_name(self) -> builtins.str:
        '''(experimental) The name of the calendar file.

        :stability: experimental
        '''
        result = self._values.get("calendar_name")
        assert result is not None, "Required property 'calendar_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def calendar_path(self) -> builtins.str:
        '''(experimental) The relative path to the calendar file.

        :stability: experimental
        '''
        result = self._values.get("calendar_path")
        assert result is not None, "Required property 'calendar_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocalPathOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PipelineWithChangeControl(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/cdk-codepipeline-extensions.PipelineWithChangeControl",
):
    '''(experimental) A pipeline with a change controller.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        change_control_calendar: Calendar,
        change_control_check_schedule: aws_cdk.aws_events.Schedule,
        pipeline_name: builtins.str,
        search_terms: typing.Sequence[builtins.str],
        source_repository: aws_cdk.aws_codecommit.IRepository,
        pipeline_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param change_control_calendar: (experimental) The calendar used for determining time windows.
        :param change_control_check_schedule: (experimental) The schedule on which to check the calendar.
        :param pipeline_name: (experimental) The name of the pipeline.
        :param search_terms: (experimental) The terms in the alarm descriptions to search for. These if the alarms containing those search terms are in ALARM, the stage transition will be closed.
        :param source_repository: (experimental) The AWS CodeCommit repository to be used as the source stage.
        :param pipeline_role: (experimental) The role used for running the pipeline. Default: - A new role is created when the pipeline is created.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                change_control_calendar: Calendar,
                change_control_check_schedule: aws_cdk.aws_events.Schedule,
                pipeline_name: builtins.str,
                search_terms: typing.Sequence[builtins.str],
                source_repository: aws_cdk.aws_codecommit.IRepository,
                pipeline_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = PipelineWithChangeControlProps(
            change_control_calendar=change_control_calendar,
            change_control_check_schedule=change_control_check_schedule,
            pipeline_name=pipeline_name,
            search_terms=search_terms,
            source_repository=source_repository,
            pipeline_role=pipeline_role,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@cdklabs/cdk-codepipeline-extensions.PipelineWithChangeControlProps",
    jsii_struct_bases=[],
    name_mapping={
        "change_control_calendar": "changeControlCalendar",
        "change_control_check_schedule": "changeControlCheckSchedule",
        "pipeline_name": "pipelineName",
        "search_terms": "searchTerms",
        "source_repository": "sourceRepository",
        "pipeline_role": "pipelineRole",
    },
)
class PipelineWithChangeControlProps:
    def __init__(
        self,
        *,
        change_control_calendar: Calendar,
        change_control_check_schedule: aws_cdk.aws_events.Schedule,
        pipeline_name: builtins.str,
        search_terms: typing.Sequence[builtins.str],
        source_repository: aws_cdk.aws_codecommit.IRepository,
        pipeline_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
    ) -> None:
        '''(experimental) Props for creating a pipeline with a change controller.

        :param change_control_calendar: (experimental) The calendar used for determining time windows.
        :param change_control_check_schedule: (experimental) The schedule on which to check the calendar.
        :param pipeline_name: (experimental) The name of the pipeline.
        :param search_terms: (experimental) The terms in the alarm descriptions to search for. These if the alarms containing those search terms are in ALARM, the stage transition will be closed.
        :param source_repository: (experimental) The AWS CodeCommit repository to be used as the source stage.
        :param pipeline_role: (experimental) The role used for running the pipeline. Default: - A new role is created when the pipeline is created.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                change_control_calendar: Calendar,
                change_control_check_schedule: aws_cdk.aws_events.Schedule,
                pipeline_name: builtins.str,
                search_terms: typing.Sequence[builtins.str],
                source_repository: aws_cdk.aws_codecommit.IRepository,
                pipeline_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument change_control_calendar", value=change_control_calendar, expected_type=type_hints["change_control_calendar"])
            check_type(argname="argument change_control_check_schedule", value=change_control_check_schedule, expected_type=type_hints["change_control_check_schedule"])
            check_type(argname="argument pipeline_name", value=pipeline_name, expected_type=type_hints["pipeline_name"])
            check_type(argname="argument search_terms", value=search_terms, expected_type=type_hints["search_terms"])
            check_type(argname="argument source_repository", value=source_repository, expected_type=type_hints["source_repository"])
            check_type(argname="argument pipeline_role", value=pipeline_role, expected_type=type_hints["pipeline_role"])
        self._values: typing.Dict[str, typing.Any] = {
            "change_control_calendar": change_control_calendar,
            "change_control_check_schedule": change_control_check_schedule,
            "pipeline_name": pipeline_name,
            "search_terms": search_terms,
            "source_repository": source_repository,
        }
        if pipeline_role is not None:
            self._values["pipeline_role"] = pipeline_role

    @builtins.property
    def change_control_calendar(self) -> Calendar:
        '''(experimental) The calendar used for determining time windows.

        :stability: experimental
        '''
        result = self._values.get("change_control_calendar")
        assert result is not None, "Required property 'change_control_calendar' is missing"
        return typing.cast(Calendar, result)

    @builtins.property
    def change_control_check_schedule(self) -> aws_cdk.aws_events.Schedule:
        '''(experimental) The schedule on which to check the calendar.

        :stability: experimental
        '''
        result = self._values.get("change_control_check_schedule")
        assert result is not None, "Required property 'change_control_check_schedule' is missing"
        return typing.cast(aws_cdk.aws_events.Schedule, result)

    @builtins.property
    def pipeline_name(self) -> builtins.str:
        '''(experimental) The name of the pipeline.

        :stability: experimental
        '''
        result = self._values.get("pipeline_name")
        assert result is not None, "Required property 'pipeline_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def search_terms(self) -> typing.List[builtins.str]:
        '''(experimental) The terms in the alarm descriptions to search for.

        These if the alarms containing those search terms are in ALARM,
        the stage transition will be closed.

        :stability: experimental
        '''
        result = self._values.get("search_terms")
        assert result is not None, "Required property 'search_terms' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def source_repository(self) -> aws_cdk.aws_codecommit.IRepository:
        '''(experimental) The AWS CodeCommit repository to be used as the source stage.

        :stability: experimental
        '''
        result = self._values.get("source_repository")
        assert result is not None, "Required property 'source_repository' is missing"
        return typing.cast(aws_cdk.aws_codecommit.IRepository, result)

    @builtins.property
    def pipeline_role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(experimental) The role used for running the pipeline.

        :default: - A new role is created when the pipeline is created.

        :stability: experimental
        '''
        result = self._values.get("pipeline_role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineWithChangeControlProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/cdk-codepipeline-extensions.S3LocationOptions",
    jsii_struct_bases=[CalendarLocationOptionsBase],
    name_mapping={"calendar_name": "calendarName", "bucket": "bucket", "role": "role"},
)
class S3LocationOptions(CalendarLocationOptionsBase):
    def __init__(
        self,
        *,
        calendar_name: builtins.str,
        bucket: aws_cdk.aws_s3.IBucket,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
    ) -> None:
        '''(experimental) Options for creating a calendar from a file in a S3 Bucket.

        :param calendar_name: (experimental) The name of the calendar file.
        :param bucket: (experimental) The bucket where the calendar is stored.
        :param role: (experimental) The role used for getting the calendar file. Default: - A role created by the Custom Resource.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                calendar_name: builtins.str,
                bucket: aws_cdk.aws_s3.IBucket,
                role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument calendar_name", value=calendar_name, expected_type=type_hints["calendar_name"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[str, typing.Any] = {
            "calendar_name": calendar_name,
            "bucket": bucket,
        }
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def calendar_name(self) -> builtins.str:
        '''(experimental) The name of the calendar file.

        :stability: experimental
        '''
        result = self._values.get("calendar_name")
        assert result is not None, "Required property 'calendar_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket(self) -> aws_cdk.aws_s3.IBucket:
        '''(experimental) The bucket where the calendar is stored.

        :stability: experimental
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(aws_cdk.aws_s3.IBucket, result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(experimental) The role used for getting the calendar file.

        :default: - A role created by the Custom Resource.

        :stability: experimental
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3LocationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AggregateAlarmState",
    "AlarmState",
    "Calendar",
    "CalendarLocationOptionsBase",
    "CalendarSetupFunction",
    "CalendarSetupFunctionProps",
    "CalendarSourceType",
    "ChangeController",
    "ChangeControllerEvent",
    "ChangeControllerFunction",
    "ChangeControllerFunctionProps",
    "ChangeControllerProps",
    "GetAlarmStateOptions",
    "IAlarmDetail",
    "LocalPathOptions",
    "PipelineWithChangeControl",
    "PipelineWithChangeControlProps",
    "S3LocationOptions",
]

publication.publish()
