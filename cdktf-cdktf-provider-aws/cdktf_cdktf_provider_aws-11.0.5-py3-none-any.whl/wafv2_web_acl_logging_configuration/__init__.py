'''
# `aws_wafv2_web_acl_logging_configuration`

Refer to the Terraform Registory for docs: [`aws_wafv2_web_acl_logging_configuration`](https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration).
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

from .._jsii import *

import cdktf
import constructs


class Wafv2WebAclLoggingConfiguration(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration aws_wafv2_web_acl_logging_configuration}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        log_destination_configs: typing.Sequence[builtins.str],
        resource_arn: builtins.str,
        id: typing.Optional[builtins.str] = None,
        logging_filter: typing.Optional[typing.Union["Wafv2WebAclLoggingConfigurationLoggingFilter", typing.Dict[str, typing.Any]]] = None,
        redacted_fields: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2WebAclLoggingConfigurationRedactedFields", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration aws_wafv2_web_acl_logging_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param log_destination_configs: AWS Kinesis Firehose Delivery Stream ARNs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#log_destination_configs Wafv2WebAclLoggingConfiguration#log_destination_configs}
        :param resource_arn: AWS WebACL ARN. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#resource_arn Wafv2WebAclLoggingConfiguration#resource_arn}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#id Wafv2WebAclLoggingConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param logging_filter: logging_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#logging_filter Wafv2WebAclLoggingConfiguration#logging_filter}
        :param redacted_fields: redacted_fields block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#redacted_fields Wafv2WebAclLoggingConfiguration#redacted_fields}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id_: builtins.str,
                *,
                log_destination_configs: typing.Sequence[builtins.str],
                resource_arn: builtins.str,
                id: typing.Optional[builtins.str] = None,
                logging_filter: typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationLoggingFilter, typing.Dict[str, typing.Any]]] = None,
                redacted_fields: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2WebAclLoggingConfigurationRedactedFields, typing.Dict[str, typing.Any]]]]] = None,
                connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
                count: typing.Optional[jsii.Number] = None,
                depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
                for_each: typing.Optional[cdktf.ITerraformIterator] = None,
                lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
                provider: typing.Optional[cdktf.TerraformProvider] = None,
                provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = Wafv2WebAclLoggingConfigurationConfig(
            log_destination_configs=log_destination_configs,
            resource_arn=resource_arn,
            id=id,
            logging_filter=logging_filter,
            redacted_fields=redacted_fields,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putLoggingFilter")
    def put_logging_filter(
        self,
        *,
        default_behavior: builtins.str,
        filter: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2WebAclLoggingConfigurationLoggingFilterFilter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param default_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#default_behavior Wafv2WebAclLoggingConfiguration#default_behavior}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#filter Wafv2WebAclLoggingConfiguration#filter}
        '''
        value = Wafv2WebAclLoggingConfigurationLoggingFilter(
            default_behavior=default_behavior, filter=filter
        )

        return typing.cast(None, jsii.invoke(self, "putLoggingFilter", [value]))

    @jsii.member(jsii_name="putRedactedFields")
    def put_redacted_fields(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2WebAclLoggingConfigurationRedactedFields", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2WebAclLoggingConfigurationRedactedFields, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRedactedFields", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLoggingFilter")
    def reset_logging_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingFilter", []))

    @jsii.member(jsii_name="resetRedactedFields")
    def reset_redacted_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedactedFields", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="loggingFilter")
    def logging_filter(
        self,
    ) -> "Wafv2WebAclLoggingConfigurationLoggingFilterOutputReference":
        return typing.cast("Wafv2WebAclLoggingConfigurationLoggingFilterOutputReference", jsii.get(self, "loggingFilter"))

    @builtins.property
    @jsii.member(jsii_name="redactedFields")
    def redacted_fields(self) -> "Wafv2WebAclLoggingConfigurationRedactedFieldsList":
        return typing.cast("Wafv2WebAclLoggingConfigurationRedactedFieldsList", jsii.get(self, "redactedFields"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logDestinationConfigsInput")
    def log_destination_configs_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "logDestinationConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingFilterInput")
    def logging_filter_input(
        self,
    ) -> typing.Optional["Wafv2WebAclLoggingConfigurationLoggingFilter"]:
        return typing.cast(typing.Optional["Wafv2WebAclLoggingConfigurationLoggingFilter"], jsii.get(self, "loggingFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="redactedFieldsInput")
    def redacted_fields_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2WebAclLoggingConfigurationRedactedFields"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2WebAclLoggingConfigurationRedactedFields"]]], jsii.get(self, "redactedFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="logDestinationConfigs")
    def log_destination_configs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "logDestinationConfigs"))

    @log_destination_configs.setter
    def log_destination_configs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logDestinationConfigs", value)

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "log_destination_configs": "logDestinationConfigs",
        "resource_arn": "resourceArn",
        "id": "id",
        "logging_filter": "loggingFilter",
        "redacted_fields": "redactedFields",
    },
)
class Wafv2WebAclLoggingConfigurationConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        log_destination_configs: typing.Sequence[builtins.str],
        resource_arn: builtins.str,
        id: typing.Optional[builtins.str] = None,
        logging_filter: typing.Optional[typing.Union["Wafv2WebAclLoggingConfigurationLoggingFilter", typing.Dict[str, typing.Any]]] = None,
        redacted_fields: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2WebAclLoggingConfigurationRedactedFields", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param log_destination_configs: AWS Kinesis Firehose Delivery Stream ARNs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#log_destination_configs Wafv2WebAclLoggingConfiguration#log_destination_configs}
        :param resource_arn: AWS WebACL ARN. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#resource_arn Wafv2WebAclLoggingConfiguration#resource_arn}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#id Wafv2WebAclLoggingConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param logging_filter: logging_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#logging_filter Wafv2WebAclLoggingConfiguration#logging_filter}
        :param redacted_fields: redacted_fields block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#redacted_fields Wafv2WebAclLoggingConfiguration#redacted_fields}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(logging_filter, dict):
            logging_filter = Wafv2WebAclLoggingConfigurationLoggingFilter(**logging_filter)
        if __debug__:
            def stub(
                *,
                connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
                count: typing.Optional[jsii.Number] = None,
                depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
                for_each: typing.Optional[cdktf.ITerraformIterator] = None,
                lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
                provider: typing.Optional[cdktf.TerraformProvider] = None,
                provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
                log_destination_configs: typing.Sequence[builtins.str],
                resource_arn: builtins.str,
                id: typing.Optional[builtins.str] = None,
                logging_filter: typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationLoggingFilter, typing.Dict[str, typing.Any]]] = None,
                redacted_fields: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2WebAclLoggingConfigurationRedactedFields, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument log_destination_configs", value=log_destination_configs, expected_type=type_hints["log_destination_configs"])
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument logging_filter", value=logging_filter, expected_type=type_hints["logging_filter"])
            check_type(argname="argument redacted_fields", value=redacted_fields, expected_type=type_hints["redacted_fields"])
        self._values: typing.Dict[str, typing.Any] = {
            "log_destination_configs": log_destination_configs,
            "resource_arn": resource_arn,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if id is not None:
            self._values["id"] = id
        if logging_filter is not None:
            self._values["logging_filter"] = logging_filter
        if redacted_fields is not None:
            self._values["redacted_fields"] = redacted_fields

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def log_destination_configs(self) -> typing.List[builtins.str]:
        '''AWS Kinesis Firehose Delivery Stream ARNs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#log_destination_configs Wafv2WebAclLoggingConfiguration#log_destination_configs}
        '''
        result = self._values.get("log_destination_configs")
        assert result is not None, "Required property 'log_destination_configs' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''AWS WebACL ARN.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#resource_arn Wafv2WebAclLoggingConfiguration#resource_arn}
        '''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#id Wafv2WebAclLoggingConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_filter(
        self,
    ) -> typing.Optional["Wafv2WebAclLoggingConfigurationLoggingFilter"]:
        '''logging_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#logging_filter Wafv2WebAclLoggingConfiguration#logging_filter}
        '''
        result = self._values.get("logging_filter")
        return typing.cast(typing.Optional["Wafv2WebAclLoggingConfigurationLoggingFilter"], result)

    @builtins.property
    def redacted_fields(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2WebAclLoggingConfigurationRedactedFields"]]]:
        '''redacted_fields block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#redacted_fields Wafv2WebAclLoggingConfiguration#redacted_fields}
        '''
        result = self._values.get("redacted_fields")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Wafv2WebAclLoggingConfigurationRedactedFields"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2WebAclLoggingConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationLoggingFilter",
    jsii_struct_bases=[],
    name_mapping={"default_behavior": "defaultBehavior", "filter": "filter"},
)
class Wafv2WebAclLoggingConfigurationLoggingFilter:
    def __init__(
        self,
        *,
        default_behavior: builtins.str,
        filter: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2WebAclLoggingConfigurationLoggingFilterFilter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param default_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#default_behavior Wafv2WebAclLoggingConfiguration#default_behavior}.
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#filter Wafv2WebAclLoggingConfiguration#filter}
        '''
        if __debug__:
            def stub(
                *,
                default_behavior: builtins.str,
                filter: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2WebAclLoggingConfigurationLoggingFilterFilter, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument default_behavior", value=default_behavior, expected_type=type_hints["default_behavior"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_behavior": default_behavior,
            "filter": filter,
        }

    @builtins.property
    def default_behavior(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#default_behavior Wafv2WebAclLoggingConfiguration#default_behavior}.'''
        result = self._values.get("default_behavior")
        assert result is not None, "Required property 'default_behavior' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filter(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["Wafv2WebAclLoggingConfigurationLoggingFilterFilter"]]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#filter Wafv2WebAclLoggingConfiguration#filter}
        '''
        result = self._values.get("filter")
        assert result is not None, "Required property 'filter' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["Wafv2WebAclLoggingConfigurationLoggingFilterFilter"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2WebAclLoggingConfigurationLoggingFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationLoggingFilterFilter",
    jsii_struct_bases=[],
    name_mapping={
        "behavior": "behavior",
        "condition": "condition",
        "requirement": "requirement",
    },
)
class Wafv2WebAclLoggingConfigurationLoggingFilterFilter:
    def __init__(
        self,
        *,
        behavior: builtins.str,
        condition: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition", typing.Dict[str, typing.Any]]]],
        requirement: builtins.str,
    ) -> None:
        '''
        :param behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#behavior Wafv2WebAclLoggingConfiguration#behavior}.
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#condition Wafv2WebAclLoggingConfiguration#condition}
        :param requirement: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#requirement Wafv2WebAclLoggingConfiguration#requirement}.
        '''
        if __debug__:
            def stub(
                *,
                behavior: builtins.str,
                condition: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition, typing.Dict[str, typing.Any]]]],
                requirement: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument behavior", value=behavior, expected_type=type_hints["behavior"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument requirement", value=requirement, expected_type=type_hints["requirement"])
        self._values: typing.Dict[str, typing.Any] = {
            "behavior": behavior,
            "condition": condition,
            "requirement": requirement,
        }

    @builtins.property
    def behavior(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#behavior Wafv2WebAclLoggingConfiguration#behavior}.'''
        result = self._values.get("behavior")
        assert result is not None, "Required property 'behavior' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition"]]:
        '''condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#condition Wafv2WebAclLoggingConfiguration#condition}
        '''
        result = self._values.get("condition")
        assert result is not None, "Required property 'condition' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition"]], result)

    @builtins.property
    def requirement(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#requirement Wafv2WebAclLoggingConfiguration#requirement}.'''
        result = self._values.get("requirement")
        assert result is not None, "Required property 'requirement' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2WebAclLoggingConfigurationLoggingFilterFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition",
    jsii_struct_bases=[],
    name_mapping={
        "action_condition": "actionCondition",
        "label_name_condition": "labelNameCondition",
    },
)
class Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition:
    def __init__(
        self,
        *,
        action_condition: typing.Optional[typing.Union["Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition", typing.Dict[str, typing.Any]]] = None,
        label_name_condition: typing.Optional[typing.Union["Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param action_condition: action_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#action_condition Wafv2WebAclLoggingConfiguration#action_condition}
        :param label_name_condition: label_name_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#label_name_condition Wafv2WebAclLoggingConfiguration#label_name_condition}
        '''
        if isinstance(action_condition, dict):
            action_condition = Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition(**action_condition)
        if isinstance(label_name_condition, dict):
            label_name_condition = Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition(**label_name_condition)
        if __debug__:
            def stub(
                *,
                action_condition: typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition, typing.Dict[str, typing.Any]]] = None,
                label_name_condition: typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument action_condition", value=action_condition, expected_type=type_hints["action_condition"])
            check_type(argname="argument label_name_condition", value=label_name_condition, expected_type=type_hints["label_name_condition"])
        self._values: typing.Dict[str, typing.Any] = {}
        if action_condition is not None:
            self._values["action_condition"] = action_condition
        if label_name_condition is not None:
            self._values["label_name_condition"] = label_name_condition

    @builtins.property
    def action_condition(
        self,
    ) -> typing.Optional["Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition"]:
        '''action_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#action_condition Wafv2WebAclLoggingConfiguration#action_condition}
        '''
        result = self._values.get("action_condition")
        return typing.cast(typing.Optional["Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition"], result)

    @builtins.property
    def label_name_condition(
        self,
    ) -> typing.Optional["Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition"]:
        '''label_name_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#label_name_condition Wafv2WebAclLoggingConfiguration#label_name_condition}
        '''
        result = self._values.get("label_name_condition")
        return typing.cast(typing.Optional["Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition",
    jsii_struct_bases=[],
    name_mapping={"action": "action"},
)
class Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition:
    def __init__(self, *, action: builtins.str) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#action Wafv2WebAclLoggingConfiguration#action}.
        '''
        if __debug__:
            def stub(*, action: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
        }

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#action Wafv2WebAclLoggingConfiguration#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionConditionOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition]:
        return typing.cast(typing.Optional[Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition",
    jsii_struct_bases=[],
    name_mapping={"label_name": "labelName"},
)
class Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition:
    def __init__(self, *, label_name: builtins.str) -> None:
        '''
        :param label_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#label_name Wafv2WebAclLoggingConfiguration#label_name}.
        '''
        if __debug__:
            def stub(*, label_name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument label_name", value=label_name, expected_type=type_hints["label_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "label_name": label_name,
        }

    @builtins.property
    def label_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#label_name Wafv2WebAclLoggingConfiguration#label_name}.'''
        result = self._values.get("label_name")
        assert result is not None, "Required property 'label_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameConditionOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="labelNameInput")
    def label_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelNameInput"))

    @builtins.property
    @jsii.member(jsii_name="labelName")
    def label_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "labelName"))

    @label_name.setter
    def label_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labelName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition]:
        return typing.cast(typing.Optional[Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                wraps_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            def stub(value: cdktf.IInterpolatingParent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                complex_object_index: jsii.Number,
                complex_object_is_from_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putActionCondition")
    def put_action_condition(self, *, action: builtins.str) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#action Wafv2WebAclLoggingConfiguration#action}.
        '''
        value = Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition(
            action=action
        )

        return typing.cast(None, jsii.invoke(self, "putActionCondition", [value]))

    @jsii.member(jsii_name="putLabelNameCondition")
    def put_label_name_condition(self, *, label_name: builtins.str) -> None:
        '''
        :param label_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#label_name Wafv2WebAclLoggingConfiguration#label_name}.
        '''
        value = Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition(
            label_name=label_name
        )

        return typing.cast(None, jsii.invoke(self, "putLabelNameCondition", [value]))

    @jsii.member(jsii_name="resetActionCondition")
    def reset_action_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActionCondition", []))

    @jsii.member(jsii_name="resetLabelNameCondition")
    def reset_label_name_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabelNameCondition", []))

    @builtins.property
    @jsii.member(jsii_name="actionCondition")
    def action_condition(
        self,
    ) -> Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionConditionOutputReference:
        return typing.cast(Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionConditionOutputReference, jsii.get(self, "actionCondition"))

    @builtins.property
    @jsii.member(jsii_name="labelNameCondition")
    def label_name_condition(
        self,
    ) -> Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameConditionOutputReference:
        return typing.cast(Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameConditionOutputReference, jsii.get(self, "labelNameCondition"))

    @builtins.property
    @jsii.member(jsii_name="actionConditionInput")
    def action_condition_input(
        self,
    ) -> typing.Optional[Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition]:
        return typing.cast(typing.Optional[Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition], jsii.get(self, "actionConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="labelNameConditionInput")
    def label_name_condition_input(
        self,
    ) -> typing.Optional[Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition]:
        return typing.cast(typing.Optional[Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition], jsii.get(self, "labelNameConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2WebAclLoggingConfigurationLoggingFilterFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationLoggingFilterFilterList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                wraps_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Wafv2WebAclLoggingConfigurationLoggingFilterFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2WebAclLoggingConfigurationLoggingFilterFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            def stub(value: cdktf.IInterpolatingParent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2WebAclLoggingConfigurationLoggingFilterFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2WebAclLoggingConfigurationLoggingFilterFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2WebAclLoggingConfigurationLoggingFilterFilter]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2WebAclLoggingConfigurationLoggingFilterFilter]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2WebAclLoggingConfigurationLoggingFilterFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationLoggingFilterFilterOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                complex_object_index: jsii.Number,
                complex_object_is_from_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCondition", [value]))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(
        self,
    ) -> Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionList:
        return typing.cast(Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionList, jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="behaviorInput")
    def behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "behaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition]]], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="requirementInput")
    def requirement_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requirementInput"))

    @builtins.property
    @jsii.member(jsii_name="behavior")
    def behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "behavior"))

    @behavior.setter
    def behavior(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "behavior", value)

    @builtins.property
    @jsii.member(jsii_name="requirement")
    def requirement(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requirement"))

    @requirement.setter
    def requirement(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requirement", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationLoggingFilterFilter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationLoggingFilterFilter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationLoggingFilterFilter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationLoggingFilterFilter, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2WebAclLoggingConfigurationLoggingFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationLoggingFilterOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2WebAclLoggingConfigurationLoggingFilterFilter, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Wafv2WebAclLoggingConfigurationLoggingFilterFilter, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> Wafv2WebAclLoggingConfigurationLoggingFilterFilterList:
        return typing.cast(Wafv2WebAclLoggingConfigurationLoggingFilterFilterList, jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="defaultBehaviorInput")
    def default_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2WebAclLoggingConfigurationLoggingFilterFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2WebAclLoggingConfigurationLoggingFilterFilter]]], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultBehavior")
    def default_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultBehavior"))

    @default_behavior.setter
    def default_behavior(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2WebAclLoggingConfigurationLoggingFilter]:
        return typing.cast(typing.Optional[Wafv2WebAclLoggingConfigurationLoggingFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2WebAclLoggingConfigurationLoggingFilter],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Wafv2WebAclLoggingConfigurationLoggingFilter],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationRedactedFields",
    jsii_struct_bases=[],
    name_mapping={
        "all_query_arguments": "allQueryArguments",
        "body": "body",
        "method": "method",
        "query_string": "queryString",
        "single_header": "singleHeader",
        "single_query_argument": "singleQueryArgument",
        "uri_path": "uriPath",
    },
)
class Wafv2WebAclLoggingConfigurationRedactedFields:
    def __init__(
        self,
        *,
        all_query_arguments: typing.Optional[typing.Union["Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArguments", typing.Dict[str, typing.Any]]] = None,
        body: typing.Optional[typing.Union["Wafv2WebAclLoggingConfigurationRedactedFieldsBody", typing.Dict[str, typing.Any]]] = None,
        method: typing.Optional[typing.Union["Wafv2WebAclLoggingConfigurationRedactedFieldsMethod", typing.Dict[str, typing.Any]]] = None,
        query_string: typing.Optional[typing.Union["Wafv2WebAclLoggingConfigurationRedactedFieldsQueryString", typing.Dict[str, typing.Any]]] = None,
        single_header: typing.Optional[typing.Union["Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeader", typing.Dict[str, typing.Any]]] = None,
        single_query_argument: typing.Optional[typing.Union["Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgument", typing.Dict[str, typing.Any]]] = None,
        uri_path: typing.Optional[typing.Union["Wafv2WebAclLoggingConfigurationRedactedFieldsUriPath", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param all_query_arguments: all_query_arguments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#all_query_arguments Wafv2WebAclLoggingConfiguration#all_query_arguments}
        :param body: body block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#body Wafv2WebAclLoggingConfiguration#body}
        :param method: method block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#method Wafv2WebAclLoggingConfiguration#method}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#query_string Wafv2WebAclLoggingConfiguration#query_string}
        :param single_header: single_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#single_header Wafv2WebAclLoggingConfiguration#single_header}
        :param single_query_argument: single_query_argument block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#single_query_argument Wafv2WebAclLoggingConfiguration#single_query_argument}
        :param uri_path: uri_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#uri_path Wafv2WebAclLoggingConfiguration#uri_path}
        '''
        if isinstance(all_query_arguments, dict):
            all_query_arguments = Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArguments(**all_query_arguments)
        if isinstance(body, dict):
            body = Wafv2WebAclLoggingConfigurationRedactedFieldsBody(**body)
        if isinstance(method, dict):
            method = Wafv2WebAclLoggingConfigurationRedactedFieldsMethod(**method)
        if isinstance(query_string, dict):
            query_string = Wafv2WebAclLoggingConfigurationRedactedFieldsQueryString(**query_string)
        if isinstance(single_header, dict):
            single_header = Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeader(**single_header)
        if isinstance(single_query_argument, dict):
            single_query_argument = Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgument(**single_query_argument)
        if isinstance(uri_path, dict):
            uri_path = Wafv2WebAclLoggingConfigurationRedactedFieldsUriPath(**uri_path)
        if __debug__:
            def stub(
                *,
                all_query_arguments: typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArguments, typing.Dict[str, typing.Any]]] = None,
                body: typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationRedactedFieldsBody, typing.Dict[str, typing.Any]]] = None,
                method: typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationRedactedFieldsMethod, typing.Dict[str, typing.Any]]] = None,
                query_string: typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationRedactedFieldsQueryString, typing.Dict[str, typing.Any]]] = None,
                single_header: typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeader, typing.Dict[str, typing.Any]]] = None,
                single_query_argument: typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgument, typing.Dict[str, typing.Any]]] = None,
                uri_path: typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationRedactedFieldsUriPath, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument all_query_arguments", value=all_query_arguments, expected_type=type_hints["all_query_arguments"])
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument single_header", value=single_header, expected_type=type_hints["single_header"])
            check_type(argname="argument single_query_argument", value=single_query_argument, expected_type=type_hints["single_query_argument"])
            check_type(argname="argument uri_path", value=uri_path, expected_type=type_hints["uri_path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if all_query_arguments is not None:
            self._values["all_query_arguments"] = all_query_arguments
        if body is not None:
            self._values["body"] = body
        if method is not None:
            self._values["method"] = method
        if query_string is not None:
            self._values["query_string"] = query_string
        if single_header is not None:
            self._values["single_header"] = single_header
        if single_query_argument is not None:
            self._values["single_query_argument"] = single_query_argument
        if uri_path is not None:
            self._values["uri_path"] = uri_path

    @builtins.property
    def all_query_arguments(
        self,
    ) -> typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArguments"]:
        '''all_query_arguments block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#all_query_arguments Wafv2WebAclLoggingConfiguration#all_query_arguments}
        '''
        result = self._values.get("all_query_arguments")
        return typing.cast(typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArguments"], result)

    @builtins.property
    def body(
        self,
    ) -> typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsBody"]:
        '''body block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#body Wafv2WebAclLoggingConfiguration#body}
        '''
        result = self._values.get("body")
        return typing.cast(typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsBody"], result)

    @builtins.property
    def method(
        self,
    ) -> typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsMethod"]:
        '''method block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#method Wafv2WebAclLoggingConfiguration#method}
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsMethod"], result)

    @builtins.property
    def query_string(
        self,
    ) -> typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsQueryString"]:
        '''query_string block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#query_string Wafv2WebAclLoggingConfiguration#query_string}
        '''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsQueryString"], result)

    @builtins.property
    def single_header(
        self,
    ) -> typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeader"]:
        '''single_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#single_header Wafv2WebAclLoggingConfiguration#single_header}
        '''
        result = self._values.get("single_header")
        return typing.cast(typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeader"], result)

    @builtins.property
    def single_query_argument(
        self,
    ) -> typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgument"]:
        '''single_query_argument block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#single_query_argument Wafv2WebAclLoggingConfiguration#single_query_argument}
        '''
        result = self._values.get("single_query_argument")
        return typing.cast(typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgument"], result)

    @builtins.property
    def uri_path(
        self,
    ) -> typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsUriPath"]:
        '''uri_path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#uri_path Wafv2WebAclLoggingConfiguration#uri_path}
        '''
        result = self._values.get("uri_path")
        return typing.cast(typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsUriPath"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2WebAclLoggingConfigurationRedactedFields(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArguments",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArguments:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArguments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArgumentsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArgumentsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArguments]:
        return typing.cast(typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArguments], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArguments],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArguments],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationRedactedFieldsBody",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2WebAclLoggingConfigurationRedactedFieldsBody:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2WebAclLoggingConfigurationRedactedFieldsBody(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2WebAclLoggingConfigurationRedactedFieldsBodyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationRedactedFieldsBodyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsBody]:
        return typing.cast(typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsBody], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsBody],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsBody],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2WebAclLoggingConfigurationRedactedFieldsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationRedactedFieldsList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                wraps_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Wafv2WebAclLoggingConfigurationRedactedFieldsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Wafv2WebAclLoggingConfigurationRedactedFieldsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            def stub(value: cdktf.IInterpolatingParent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2WebAclLoggingConfigurationRedactedFields]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2WebAclLoggingConfigurationRedactedFields]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2WebAclLoggingConfigurationRedactedFields]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Wafv2WebAclLoggingConfigurationRedactedFields]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationRedactedFieldsMethod",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2WebAclLoggingConfigurationRedactedFieldsMethod:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2WebAclLoggingConfigurationRedactedFieldsMethod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2WebAclLoggingConfigurationRedactedFieldsMethodOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationRedactedFieldsMethodOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsMethod]:
        return typing.cast(typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsMethod], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsMethod],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsMethod],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Wafv2WebAclLoggingConfigurationRedactedFieldsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationRedactedFieldsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                complex_object_index: jsii.Number,
                complex_object_is_from_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAllQueryArguments")
    def put_all_query_arguments(self) -> None:
        value = Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArguments()

        return typing.cast(None, jsii.invoke(self, "putAllQueryArguments", [value]))

    @jsii.member(jsii_name="putBody")
    def put_body(self) -> None:
        value = Wafv2WebAclLoggingConfigurationRedactedFieldsBody()

        return typing.cast(None, jsii.invoke(self, "putBody", [value]))

    @jsii.member(jsii_name="putMethod")
    def put_method(self) -> None:
        value = Wafv2WebAclLoggingConfigurationRedactedFieldsMethod()

        return typing.cast(None, jsii.invoke(self, "putMethod", [value]))

    @jsii.member(jsii_name="putQueryString")
    def put_query_string(self) -> None:
        value = Wafv2WebAclLoggingConfigurationRedactedFieldsQueryString()

        return typing.cast(None, jsii.invoke(self, "putQueryString", [value]))

    @jsii.member(jsii_name="putSingleHeader")
    def put_single_header(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#name Wafv2WebAclLoggingConfiguration#name}.
        '''
        value = Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeader(name=name)

        return typing.cast(None, jsii.invoke(self, "putSingleHeader", [value]))

    @jsii.member(jsii_name="putSingleQueryArgument")
    def put_single_query_argument(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#name Wafv2WebAclLoggingConfiguration#name}.
        '''
        value = Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgument(
            name=name
        )

        return typing.cast(None, jsii.invoke(self, "putSingleQueryArgument", [value]))

    @jsii.member(jsii_name="putUriPath")
    def put_uri_path(self) -> None:
        value = Wafv2WebAclLoggingConfigurationRedactedFieldsUriPath()

        return typing.cast(None, jsii.invoke(self, "putUriPath", [value]))

    @jsii.member(jsii_name="resetAllQueryArguments")
    def reset_all_query_arguments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllQueryArguments", []))

    @jsii.member(jsii_name="resetBody")
    def reset_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBody", []))

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetQueryString")
    def reset_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryString", []))

    @jsii.member(jsii_name="resetSingleHeader")
    def reset_single_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleHeader", []))

    @jsii.member(jsii_name="resetSingleQueryArgument")
    def reset_single_query_argument(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleQueryArgument", []))

    @jsii.member(jsii_name="resetUriPath")
    def reset_uri_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUriPath", []))

    @builtins.property
    @jsii.member(jsii_name="allQueryArguments")
    def all_query_arguments(
        self,
    ) -> Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArgumentsOutputReference:
        return typing.cast(Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArgumentsOutputReference, jsii.get(self, "allQueryArguments"))

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(self) -> Wafv2WebAclLoggingConfigurationRedactedFieldsBodyOutputReference:
        return typing.cast(Wafv2WebAclLoggingConfigurationRedactedFieldsBodyOutputReference, jsii.get(self, "body"))

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(
        self,
    ) -> Wafv2WebAclLoggingConfigurationRedactedFieldsMethodOutputReference:
        return typing.cast(Wafv2WebAclLoggingConfigurationRedactedFieldsMethodOutputReference, jsii.get(self, "method"))

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(
        self,
    ) -> "Wafv2WebAclLoggingConfigurationRedactedFieldsQueryStringOutputReference":
        return typing.cast("Wafv2WebAclLoggingConfigurationRedactedFieldsQueryStringOutputReference", jsii.get(self, "queryString"))

    @builtins.property
    @jsii.member(jsii_name="singleHeader")
    def single_header(
        self,
    ) -> "Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeaderOutputReference":
        return typing.cast("Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeaderOutputReference", jsii.get(self, "singleHeader"))

    @builtins.property
    @jsii.member(jsii_name="singleQueryArgument")
    def single_query_argument(
        self,
    ) -> "Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgumentOutputReference":
        return typing.cast("Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgumentOutputReference", jsii.get(self, "singleQueryArgument"))

    @builtins.property
    @jsii.member(jsii_name="uriPath")
    def uri_path(
        self,
    ) -> "Wafv2WebAclLoggingConfigurationRedactedFieldsUriPathOutputReference":
        return typing.cast("Wafv2WebAclLoggingConfigurationRedactedFieldsUriPathOutputReference", jsii.get(self, "uriPath"))

    @builtins.property
    @jsii.member(jsii_name="allQueryArgumentsInput")
    def all_query_arguments_input(
        self,
    ) -> typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArguments]:
        return typing.cast(typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArguments], jsii.get(self, "allQueryArgumentsInput"))

    @builtins.property
    @jsii.member(jsii_name="bodyInput")
    def body_input(
        self,
    ) -> typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsBody]:
        return typing.cast(typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsBody], jsii.get(self, "bodyInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(
        self,
    ) -> typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsMethod]:
        return typing.cast(typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsMethod], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(
        self,
    ) -> typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsQueryString"]:
        return typing.cast(typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsQueryString"], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="singleHeaderInput")
    def single_header_input(
        self,
    ) -> typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeader"]:
        return typing.cast(typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeader"], jsii.get(self, "singleHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="singleQueryArgumentInput")
    def single_query_argument_input(
        self,
    ) -> typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgument"]:
        return typing.cast(typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgument"], jsii.get(self, "singleQueryArgumentInput"))

    @builtins.property
    @jsii.member(jsii_name="uriPathInput")
    def uri_path_input(
        self,
    ) -> typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsUriPath"]:
        return typing.cast(typing.Optional["Wafv2WebAclLoggingConfigurationRedactedFieldsUriPath"], jsii.get(self, "uriPathInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationRedactedFields, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationRedactedFields, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationRedactedFields, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[Wafv2WebAclLoggingConfigurationRedactedFields, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationRedactedFieldsQueryString",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2WebAclLoggingConfigurationRedactedFieldsQueryString:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2WebAclLoggingConfigurationRedactedFieldsQueryString(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2WebAclLoggingConfigurationRedactedFieldsQueryStringOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationRedactedFieldsQueryStringOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsQueryString]:
        return typing.cast(typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsQueryString], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsQueryString],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsQueryString],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeader",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeader:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#name Wafv2WebAclLoggingConfiguration#name}.
        '''
        if __debug__:
            def stub(*, name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#name Wafv2WebAclLoggingConfiguration#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeaderOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeader]:
        return typing.cast(typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeader],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeader],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgument",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgument:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#name Wafv2WebAclLoggingConfiguration#name}.
        '''
        if __debug__:
            def stub(*, name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/wafv2_web_acl_logging_configuration#name Wafv2WebAclLoggingConfiguration#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgument(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgumentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgumentOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgument]:
        return typing.cast(typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgument], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgument],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgument],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationRedactedFieldsUriPath",
    jsii_struct_bases=[],
    name_mapping={},
)
class Wafv2WebAclLoggingConfigurationRedactedFieldsUriPath:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Wafv2WebAclLoggingConfigurationRedactedFieldsUriPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Wafv2WebAclLoggingConfigurationRedactedFieldsUriPathOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.wafv2WebAclLoggingConfiguration.Wafv2WebAclLoggingConfigurationRedactedFieldsUriPathOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsUriPath]:
        return typing.cast(typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsUriPath], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsUriPath],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Wafv2WebAclLoggingConfigurationRedactedFieldsUriPath],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Wafv2WebAclLoggingConfiguration",
    "Wafv2WebAclLoggingConfigurationConfig",
    "Wafv2WebAclLoggingConfigurationLoggingFilter",
    "Wafv2WebAclLoggingConfigurationLoggingFilterFilter",
    "Wafv2WebAclLoggingConfigurationLoggingFilterFilterCondition",
    "Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition",
    "Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionActionConditionOutputReference",
    "Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition",
    "Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameConditionOutputReference",
    "Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionList",
    "Wafv2WebAclLoggingConfigurationLoggingFilterFilterConditionOutputReference",
    "Wafv2WebAclLoggingConfigurationLoggingFilterFilterList",
    "Wafv2WebAclLoggingConfigurationLoggingFilterFilterOutputReference",
    "Wafv2WebAclLoggingConfigurationLoggingFilterOutputReference",
    "Wafv2WebAclLoggingConfigurationRedactedFields",
    "Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArguments",
    "Wafv2WebAclLoggingConfigurationRedactedFieldsAllQueryArgumentsOutputReference",
    "Wafv2WebAclLoggingConfigurationRedactedFieldsBody",
    "Wafv2WebAclLoggingConfigurationRedactedFieldsBodyOutputReference",
    "Wafv2WebAclLoggingConfigurationRedactedFieldsList",
    "Wafv2WebAclLoggingConfigurationRedactedFieldsMethod",
    "Wafv2WebAclLoggingConfigurationRedactedFieldsMethodOutputReference",
    "Wafv2WebAclLoggingConfigurationRedactedFieldsOutputReference",
    "Wafv2WebAclLoggingConfigurationRedactedFieldsQueryString",
    "Wafv2WebAclLoggingConfigurationRedactedFieldsQueryStringOutputReference",
    "Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeader",
    "Wafv2WebAclLoggingConfigurationRedactedFieldsSingleHeaderOutputReference",
    "Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgument",
    "Wafv2WebAclLoggingConfigurationRedactedFieldsSingleQueryArgumentOutputReference",
    "Wafv2WebAclLoggingConfigurationRedactedFieldsUriPath",
    "Wafv2WebAclLoggingConfigurationRedactedFieldsUriPathOutputReference",
]

publication.publish()
