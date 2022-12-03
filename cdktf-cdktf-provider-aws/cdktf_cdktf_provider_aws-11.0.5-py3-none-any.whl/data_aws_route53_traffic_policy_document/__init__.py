'''
# `data_aws_route53_traffic_policy_document`

Refer to the Terraform Registory for docs: [`data_aws_route53_traffic_policy_document`](https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document).
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


class DataAwsRoute53TrafficPolicyDocument(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocument",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document aws_route53_traffic_policy_document}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        endpoint: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentEndpoint", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        record_type: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentRule", typing.Dict[str, typing.Any]]]]] = None,
        start_endpoint: typing.Optional[builtins.str] = None,
        start_rule: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document aws_route53_traffic_policy_document} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param endpoint: endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint DataAwsRoute53TrafficPolicyDocument#endpoint}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#id DataAwsRoute53TrafficPolicyDocument#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param record_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#record_type DataAwsRoute53TrafficPolicyDocument#record_type}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule DataAwsRoute53TrafficPolicyDocument#rule}
        :param start_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#start_endpoint DataAwsRoute53TrafficPolicyDocument#start_endpoint}.
        :param start_rule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#start_rule DataAwsRoute53TrafficPolicyDocument#start_rule}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#version DataAwsRoute53TrafficPolicyDocument#version}.
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
                endpoint: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentEndpoint, typing.Dict[str, typing.Any]]]]] = None,
                id: typing.Optional[builtins.str] = None,
                record_type: typing.Optional[builtins.str] = None,
                rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRule, typing.Dict[str, typing.Any]]]]] = None,
                start_endpoint: typing.Optional[builtins.str] = None,
                start_rule: typing.Optional[builtins.str] = None,
                version: typing.Optional[builtins.str] = None,
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
        config = DataAwsRoute53TrafficPolicyDocumentConfig(
            endpoint=endpoint,
            id=id,
            record_type=record_type,
            rule=rule,
            start_endpoint=start_endpoint,
            start_rule=start_rule,
            version=version,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putEndpoint")
    def put_endpoint(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentEndpoint", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentEndpoint, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEndpoint", [value]))

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRule, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="resetEndpoint")
    def reset_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoint", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRecordType")
    def reset_record_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordType", []))

    @jsii.member(jsii_name="resetRule")
    def reset_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRule", []))

    @jsii.member(jsii_name="resetStartEndpoint")
    def reset_start_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartEndpoint", []))

    @jsii.member(jsii_name="resetStartRule")
    def reset_start_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartRule", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> "DataAwsRoute53TrafficPolicyDocumentEndpointList":
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentEndpointList", jsii.get(self, "endpoint"))

    @builtins.property
    @jsii.member(jsii_name="json")
    def json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "json"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "DataAwsRoute53TrafficPolicyDocumentRuleList":
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentEndpoint"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentEndpoint"]]], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="recordTypeInput")
    def record_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="startEndpointInput")
    def start_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="startRuleInput")
    def start_rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

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
    @jsii.member(jsii_name="recordType")
    def record_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordType"))

    @record_type.setter
    def record_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordType", value)

    @builtins.property
    @jsii.member(jsii_name="startEndpoint")
    def start_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startEndpoint"))

    @start_endpoint.setter
    def start_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="startRule")
    def start_rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startRule"))

    @start_rule.setter
    def start_rule(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startRule", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "endpoint": "endpoint",
        "id": "id",
        "record_type": "recordType",
        "rule": "rule",
        "start_endpoint": "startEndpoint",
        "start_rule": "startRule",
        "version": "version",
    },
)
class DataAwsRoute53TrafficPolicyDocumentConfig(cdktf.TerraformMetaArguments):
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
        endpoint: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentEndpoint", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        record_type: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentRule", typing.Dict[str, typing.Any]]]]] = None,
        start_endpoint: typing.Optional[builtins.str] = None,
        start_rule: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param endpoint: endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint DataAwsRoute53TrafficPolicyDocument#endpoint}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#id DataAwsRoute53TrafficPolicyDocument#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param record_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#record_type DataAwsRoute53TrafficPolicyDocument#record_type}.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule DataAwsRoute53TrafficPolicyDocument#rule}
        :param start_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#start_endpoint DataAwsRoute53TrafficPolicyDocument#start_endpoint}.
        :param start_rule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#start_rule DataAwsRoute53TrafficPolicyDocument#start_rule}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#version DataAwsRoute53TrafficPolicyDocument#version}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
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
                endpoint: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentEndpoint, typing.Dict[str, typing.Any]]]]] = None,
                id: typing.Optional[builtins.str] = None,
                record_type: typing.Optional[builtins.str] = None,
                rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRule, typing.Dict[str, typing.Any]]]]] = None,
                start_endpoint: typing.Optional[builtins.str] = None,
                start_rule: typing.Optional[builtins.str] = None,
                version: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument record_type", value=record_type, expected_type=type_hints["record_type"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument start_endpoint", value=start_endpoint, expected_type=type_hints["start_endpoint"])
            check_type(argname="argument start_rule", value=start_rule, expected_type=type_hints["start_rule"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
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
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if id is not None:
            self._values["id"] = id
        if record_type is not None:
            self._values["record_type"] = record_type
        if rule is not None:
            self._values["rule"] = rule
        if start_endpoint is not None:
            self._values["start_endpoint"] = start_endpoint
        if start_rule is not None:
            self._values["start_rule"] = start_rule
        if version is not None:
            self._values["version"] = version

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
    def endpoint(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentEndpoint"]]]:
        '''endpoint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint DataAwsRoute53TrafficPolicyDocument#endpoint}
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentEndpoint"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#id DataAwsRoute53TrafficPolicyDocument#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def record_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#record_type DataAwsRoute53TrafficPolicyDocument#record_type}.'''
        result = self._values.get("record_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRule"]]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule DataAwsRoute53TrafficPolicyDocument#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRule"]]], result)

    @builtins.property
    def start_endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#start_endpoint DataAwsRoute53TrafficPolicyDocument#start_endpoint}.'''
        result = self._values.get("start_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_rule(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#start_rule DataAwsRoute53TrafficPolicyDocument#start_rule}.'''
        result = self._values.get("start_rule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#version DataAwsRoute53TrafficPolicyDocument#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsRoute53TrafficPolicyDocumentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentEndpoint",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "region": "region", "type": "type", "value": "value"},
)
class DataAwsRoute53TrafficPolicyDocumentEndpoint:
    def __init__(
        self,
        *,
        id: builtins.str,
        region: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#id DataAwsRoute53TrafficPolicyDocument#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#region DataAwsRoute53TrafficPolicyDocument#region}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#type DataAwsRoute53TrafficPolicyDocument#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#value DataAwsRoute53TrafficPolicyDocument#value}.
        '''
        if __debug__:
            def stub(
                *,
                id: builtins.str,
                region: typing.Optional[builtins.str] = None,
                type: typing.Optional[builtins.str] = None,
                value: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if region is not None:
            self._values["region"] = region
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#id DataAwsRoute53TrafficPolicyDocument#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#region DataAwsRoute53TrafficPolicyDocument#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#type DataAwsRoute53TrafficPolicyDocument#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#value DataAwsRoute53TrafficPolicyDocument#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsRoute53TrafficPolicyDocumentEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsRoute53TrafficPolicyDocumentEndpointList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentEndpointList",
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
    ) -> "DataAwsRoute53TrafficPolicyDocumentEndpointOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentEndpointOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentEndpoint]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentEndpoint]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentEndpoint]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentEndpoint]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsRoute53TrafficPolicyDocumentEndpointOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentEndpointOutputReference",
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

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

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
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentEndpoint, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentEndpoint, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentEndpoint, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentEndpoint, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRule",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "geo_proximity_location": "geoProximityLocation",
        "items": "items",
        "location": "location",
        "primary": "primary",
        "region": "region",
        "secondary": "secondary",
        "type": "type",
    },
)
class DataAwsRoute53TrafficPolicyDocumentRule:
    def __init__(
        self,
        *,
        id: builtins.str,
        geo_proximity_location: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation", typing.Dict[str, typing.Any]]]]] = None,
        items: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentRuleItems", typing.Dict[str, typing.Any]]]]] = None,
        location: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentRuleLocation", typing.Dict[str, typing.Any]]]]] = None,
        primary: typing.Optional[typing.Union["DataAwsRoute53TrafficPolicyDocumentRulePrimary", typing.Dict[str, typing.Any]]] = None,
        region: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentRuleRegion", typing.Dict[str, typing.Any]]]]] = None,
        secondary: typing.Optional[typing.Union["DataAwsRoute53TrafficPolicyDocumentRuleSecondary", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#id DataAwsRoute53TrafficPolicyDocument#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param geo_proximity_location: geo_proximity_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#geo_proximity_location DataAwsRoute53TrafficPolicyDocument#geo_proximity_location}
        :param items: items block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#items DataAwsRoute53TrafficPolicyDocument#items}
        :param location: location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#location DataAwsRoute53TrafficPolicyDocument#location}
        :param primary: primary block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#primary DataAwsRoute53TrafficPolicyDocument#primary}
        :param region: region block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#region DataAwsRoute53TrafficPolicyDocument#region}
        :param secondary: secondary block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#secondary DataAwsRoute53TrafficPolicyDocument#secondary}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#type DataAwsRoute53TrafficPolicyDocument#type}.
        '''
        if isinstance(primary, dict):
            primary = DataAwsRoute53TrafficPolicyDocumentRulePrimary(**primary)
        if isinstance(secondary, dict):
            secondary = DataAwsRoute53TrafficPolicyDocumentRuleSecondary(**secondary)
        if __debug__:
            def stub(
                *,
                id: builtins.str,
                geo_proximity_location: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation, typing.Dict[str, typing.Any]]]]] = None,
                items: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleItems, typing.Dict[str, typing.Any]]]]] = None,
                location: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleLocation, typing.Dict[str, typing.Any]]]]] = None,
                primary: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRulePrimary, typing.Dict[str, typing.Any]]] = None,
                region: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleRegion, typing.Dict[str, typing.Any]]]]] = None,
                secondary: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleSecondary, typing.Dict[str, typing.Any]]] = None,
                type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument geo_proximity_location", value=geo_proximity_location, expected_type=type_hints["geo_proximity_location"])
            check_type(argname="argument items", value=items, expected_type=type_hints["items"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument secondary", value=secondary, expected_type=type_hints["secondary"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if geo_proximity_location is not None:
            self._values["geo_proximity_location"] = geo_proximity_location
        if items is not None:
            self._values["items"] = items
        if location is not None:
            self._values["location"] = location
        if primary is not None:
            self._values["primary"] = primary
        if region is not None:
            self._values["region"] = region
        if secondary is not None:
            self._values["secondary"] = secondary
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#id DataAwsRoute53TrafficPolicyDocument#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def geo_proximity_location(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation"]]]:
        '''geo_proximity_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#geo_proximity_location DataAwsRoute53TrafficPolicyDocument#geo_proximity_location}
        '''
        result = self._values.get("geo_proximity_location")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation"]]], result)

    @builtins.property
    def items(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleItems"]]]:
        '''items block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#items DataAwsRoute53TrafficPolicyDocument#items}
        '''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleItems"]]], result)

    @builtins.property
    def location(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleLocation"]]]:
        '''location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#location DataAwsRoute53TrafficPolicyDocument#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleLocation"]]], result)

    @builtins.property
    def primary(
        self,
    ) -> typing.Optional["DataAwsRoute53TrafficPolicyDocumentRulePrimary"]:
        '''primary block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#primary DataAwsRoute53TrafficPolicyDocument#primary}
        '''
        result = self._values.get("primary")
        return typing.cast(typing.Optional["DataAwsRoute53TrafficPolicyDocumentRulePrimary"], result)

    @builtins.property
    def region(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleRegion"]]]:
        '''region block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#region DataAwsRoute53TrafficPolicyDocument#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleRegion"]]], result)

    @builtins.property
    def secondary(
        self,
    ) -> typing.Optional["DataAwsRoute53TrafficPolicyDocumentRuleSecondary"]:
        '''secondary block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#secondary DataAwsRoute53TrafficPolicyDocument#secondary}
        '''
        result = self._values.get("secondary")
        return typing.cast(typing.Optional["DataAwsRoute53TrafficPolicyDocumentRuleSecondary"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#type DataAwsRoute53TrafficPolicyDocument#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsRoute53TrafficPolicyDocumentRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation",
    jsii_struct_bases=[],
    name_mapping={
        "bias": "bias",
        "endpoint_reference": "endpointReference",
        "evaluate_target_health": "evaluateTargetHealth",
        "health_check": "healthCheck",
        "latitude": "latitude",
        "longitude": "longitude",
        "region": "region",
        "rule_reference": "ruleReference",
    },
)
class DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation:
    def __init__(
        self,
        *,
        bias: typing.Optional[builtins.str] = None,
        endpoint_reference: typing.Optional[builtins.str] = None,
        evaluate_target_health: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_check: typing.Optional[builtins.str] = None,
        latitude: typing.Optional[builtins.str] = None,
        longitude: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        rule_reference: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bias: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#bias DataAwsRoute53TrafficPolicyDocument#bias}.
        :param endpoint_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.
        :param evaluate_target_health: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.
        :param health_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.
        :param latitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#latitude DataAwsRoute53TrafficPolicyDocument#latitude}.
        :param longitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#longitude DataAwsRoute53TrafficPolicyDocument#longitude}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#region DataAwsRoute53TrafficPolicyDocument#region}.
        :param rule_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.
        '''
        if __debug__:
            def stub(
                *,
                bias: typing.Optional[builtins.str] = None,
                endpoint_reference: typing.Optional[builtins.str] = None,
                evaluate_target_health: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                health_check: typing.Optional[builtins.str] = None,
                latitude: typing.Optional[builtins.str] = None,
                longitude: typing.Optional[builtins.str] = None,
                region: typing.Optional[builtins.str] = None,
                rule_reference: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bias", value=bias, expected_type=type_hints["bias"])
            check_type(argname="argument endpoint_reference", value=endpoint_reference, expected_type=type_hints["endpoint_reference"])
            check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument latitude", value=latitude, expected_type=type_hints["latitude"])
            check_type(argname="argument longitude", value=longitude, expected_type=type_hints["longitude"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument rule_reference", value=rule_reference, expected_type=type_hints["rule_reference"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bias is not None:
            self._values["bias"] = bias
        if endpoint_reference is not None:
            self._values["endpoint_reference"] = endpoint_reference
        if evaluate_target_health is not None:
            self._values["evaluate_target_health"] = evaluate_target_health
        if health_check is not None:
            self._values["health_check"] = health_check
        if latitude is not None:
            self._values["latitude"] = latitude
        if longitude is not None:
            self._values["longitude"] = longitude
        if region is not None:
            self._values["region"] = region
        if rule_reference is not None:
            self._values["rule_reference"] = rule_reference

    @builtins.property
    def bias(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#bias DataAwsRoute53TrafficPolicyDocument#bias}.'''
        result = self._values.get("bias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.'''
        result = self._values.get("endpoint_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluate_target_health(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.'''
        result = self._values.get("evaluate_target_health")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def health_check(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.'''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def latitude(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#latitude DataAwsRoute53TrafficPolicyDocument#latitude}.'''
        result = self._values.get("latitude")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def longitude(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#longitude DataAwsRoute53TrafficPolicyDocument#longitude}.'''
        result = self._values.get("longitude")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#region DataAwsRoute53TrafficPolicyDocument#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.'''
        result = self._values.get("rule_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationList",
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
    ) -> "DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationOutputReference",
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

    @jsii.member(jsii_name="resetBias")
    def reset_bias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBias", []))

    @jsii.member(jsii_name="resetEndpointReference")
    def reset_endpoint_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointReference", []))

    @jsii.member(jsii_name="resetEvaluateTargetHealth")
    def reset_evaluate_target_health(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluateTargetHealth", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetLatitude")
    def reset_latitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLatitude", []))

    @jsii.member(jsii_name="resetLongitude")
    def reset_longitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongitude", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetRuleReference")
    def reset_rule_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleReference", []))

    @builtins.property
    @jsii.member(jsii_name="biasInput")
    def bias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "biasInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointReferenceInput")
    def endpoint_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealthInput")
    def evaluate_target_health_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "evaluateTargetHealthInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="latitudeInput")
    def latitude_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "latitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="longitudeInput")
    def longitude_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "longitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleReferenceInput")
    def rule_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="bias")
    def bias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bias"))

    @bias.setter
    def bias(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bias", value)

    @builtins.property
    @jsii.member(jsii_name="endpointReference")
    def endpoint_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointReference"))

    @endpoint_reference.setter
    def endpoint_reference(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointReference", value)

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealth")
    def evaluate_target_health(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "evaluateTargetHealth"))

    @evaluate_target_health.setter
    def evaluate_target_health(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluateTargetHealth", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheck"))

    @health_check.setter
    def health_check(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheck", value)

    @builtins.property
    @jsii.member(jsii_name="latitude")
    def latitude(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "latitude"))

    @latitude.setter
    def latitude(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "latitude", value)

    @builtins.property
    @jsii.member(jsii_name="longitude")
    def longitude(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "longitude"))

    @longitude.setter
    def longitude(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longitude", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="ruleReference")
    def rule_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleReference"))

    @rule_reference.setter
    def rule_reference(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleReference", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleItems",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_reference": "endpointReference",
        "health_check": "healthCheck",
    },
)
class DataAwsRoute53TrafficPolicyDocumentRuleItems:
    def __init__(
        self,
        *,
        endpoint_reference: typing.Optional[builtins.str] = None,
        health_check: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.
        :param health_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.
        '''
        if __debug__:
            def stub(
                *,
                endpoint_reference: typing.Optional[builtins.str] = None,
                health_check: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument endpoint_reference", value=endpoint_reference, expected_type=type_hints["endpoint_reference"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
        self._values: typing.Dict[str, typing.Any] = {}
        if endpoint_reference is not None:
            self._values["endpoint_reference"] = endpoint_reference
        if health_check is not None:
            self._values["health_check"] = health_check

    @builtins.property
    def endpoint_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.'''
        result = self._values.get("endpoint_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.'''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsRoute53TrafficPolicyDocumentRuleItems(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsRoute53TrafficPolicyDocumentRuleItemsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleItemsList",
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
    ) -> "DataAwsRoute53TrafficPolicyDocumentRuleItemsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentRuleItemsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleItems]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleItems]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleItems]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleItems]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsRoute53TrafficPolicyDocumentRuleItemsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleItemsOutputReference",
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

    @jsii.member(jsii_name="resetEndpointReference")
    def reset_endpoint_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointReference", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @builtins.property
    @jsii.member(jsii_name="endpointReferenceInput")
    def endpoint_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointReference")
    def endpoint_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointReference"))

    @endpoint_reference.setter
    def endpoint_reference(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointReference", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheck"))

    @health_check.setter
    def health_check(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheck", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleItems, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleItems, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleItems, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleItems, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsRoute53TrafficPolicyDocumentRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleList",
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
    ) -> "DataAwsRoute53TrafficPolicyDocumentRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentRuleOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRule]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRule]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleLocation",
    jsii_struct_bases=[],
    name_mapping={
        "continent": "continent",
        "country": "country",
        "endpoint_reference": "endpointReference",
        "evaluate_target_health": "evaluateTargetHealth",
        "health_check": "healthCheck",
        "is_default": "isDefault",
        "rule_reference": "ruleReference",
        "subdivision": "subdivision",
    },
)
class DataAwsRoute53TrafficPolicyDocumentRuleLocation:
    def __init__(
        self,
        *,
        continent: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        endpoint_reference: typing.Optional[builtins.str] = None,
        evaluate_target_health: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_check: typing.Optional[builtins.str] = None,
        is_default: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        rule_reference: typing.Optional[builtins.str] = None,
        subdivision: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param continent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#continent DataAwsRoute53TrafficPolicyDocument#continent}.
        :param country: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#country DataAwsRoute53TrafficPolicyDocument#country}.
        :param endpoint_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.
        :param evaluate_target_health: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.
        :param health_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.
        :param is_default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#is_default DataAwsRoute53TrafficPolicyDocument#is_default}.
        :param rule_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.
        :param subdivision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#subdivision DataAwsRoute53TrafficPolicyDocument#subdivision}.
        '''
        if __debug__:
            def stub(
                *,
                continent: typing.Optional[builtins.str] = None,
                country: typing.Optional[builtins.str] = None,
                endpoint_reference: typing.Optional[builtins.str] = None,
                evaluate_target_health: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                health_check: typing.Optional[builtins.str] = None,
                is_default: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                rule_reference: typing.Optional[builtins.str] = None,
                subdivision: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument continent", value=continent, expected_type=type_hints["continent"])
            check_type(argname="argument country", value=country, expected_type=type_hints["country"])
            check_type(argname="argument endpoint_reference", value=endpoint_reference, expected_type=type_hints["endpoint_reference"])
            check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument is_default", value=is_default, expected_type=type_hints["is_default"])
            check_type(argname="argument rule_reference", value=rule_reference, expected_type=type_hints["rule_reference"])
            check_type(argname="argument subdivision", value=subdivision, expected_type=type_hints["subdivision"])
        self._values: typing.Dict[str, typing.Any] = {}
        if continent is not None:
            self._values["continent"] = continent
        if country is not None:
            self._values["country"] = country
        if endpoint_reference is not None:
            self._values["endpoint_reference"] = endpoint_reference
        if evaluate_target_health is not None:
            self._values["evaluate_target_health"] = evaluate_target_health
        if health_check is not None:
            self._values["health_check"] = health_check
        if is_default is not None:
            self._values["is_default"] = is_default
        if rule_reference is not None:
            self._values["rule_reference"] = rule_reference
        if subdivision is not None:
            self._values["subdivision"] = subdivision

    @builtins.property
    def continent(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#continent DataAwsRoute53TrafficPolicyDocument#continent}.'''
        result = self._values.get("continent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def country(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#country DataAwsRoute53TrafficPolicyDocument#country}.'''
        result = self._values.get("country")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.'''
        result = self._values.get("endpoint_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluate_target_health(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.'''
        result = self._values.get("evaluate_target_health")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def health_check(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.'''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_default(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#is_default DataAwsRoute53TrafficPolicyDocument#is_default}.'''
        result = self._values.get("is_default")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def rule_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.'''
        result = self._values.get("rule_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdivision(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#subdivision DataAwsRoute53TrafficPolicyDocument#subdivision}.'''
        result = self._values.get("subdivision")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsRoute53TrafficPolicyDocumentRuleLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsRoute53TrafficPolicyDocumentRuleLocationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleLocationList",
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
    ) -> "DataAwsRoute53TrafficPolicyDocumentRuleLocationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentRuleLocationOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleLocation]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleLocation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleLocation]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleLocation]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsRoute53TrafficPolicyDocumentRuleLocationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleLocationOutputReference",
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

    @jsii.member(jsii_name="resetContinent")
    def reset_continent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContinent", []))

    @jsii.member(jsii_name="resetCountry")
    def reset_country(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountry", []))

    @jsii.member(jsii_name="resetEndpointReference")
    def reset_endpoint_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointReference", []))

    @jsii.member(jsii_name="resetEvaluateTargetHealth")
    def reset_evaluate_target_health(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluateTargetHealth", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetIsDefault")
    def reset_is_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsDefault", []))

    @jsii.member(jsii_name="resetRuleReference")
    def reset_rule_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleReference", []))

    @jsii.member(jsii_name="resetSubdivision")
    def reset_subdivision(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubdivision", []))

    @builtins.property
    @jsii.member(jsii_name="continentInput")
    def continent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "continentInput"))

    @builtins.property
    @jsii.member(jsii_name="countryInput")
    def country_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointReferenceInput")
    def endpoint_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealthInput")
    def evaluate_target_health_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "evaluateTargetHealthInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="isDefaultInput")
    def is_default_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isDefaultInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleReferenceInput")
    def rule_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="subdivisionInput")
    def subdivision_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdivisionInput"))

    @builtins.property
    @jsii.member(jsii_name="continent")
    def continent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "continent"))

    @continent.setter
    def continent(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "continent", value)

    @builtins.property
    @jsii.member(jsii_name="country")
    def country(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "country"))

    @country.setter
    def country(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "country", value)

    @builtins.property
    @jsii.member(jsii_name="endpointReference")
    def endpoint_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointReference"))

    @endpoint_reference.setter
    def endpoint_reference(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointReference", value)

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealth")
    def evaluate_target_health(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "evaluateTargetHealth"))

    @evaluate_target_health.setter
    def evaluate_target_health(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluateTargetHealth", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheck"))

    @health_check.setter
    def health_check(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheck", value)

    @builtins.property
    @jsii.member(jsii_name="isDefault")
    def is_default(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isDefault"))

    @is_default.setter
    def is_default(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isDefault", value)

    @builtins.property
    @jsii.member(jsii_name="ruleReference")
    def rule_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleReference"))

    @rule_reference.setter
    def rule_reference(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleReference", value)

    @builtins.property
    @jsii.member(jsii_name="subdivision")
    def subdivision(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subdivision"))

    @subdivision.setter
    def subdivision(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subdivision", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleLocation, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleLocation, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleLocation, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleLocation, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsRoute53TrafficPolicyDocumentRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleOutputReference",
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

    @jsii.member(jsii_name="putGeoProximityLocation")
    def put_geo_proximity_location(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGeoProximityLocation", [value]))

    @jsii.member(jsii_name="putItems")
    def put_items(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleItems, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleItems, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putItems", [value]))

    @jsii.member(jsii_name="putLocation")
    def put_location(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleLocation, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleLocation, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLocation", [value]))

    @jsii.member(jsii_name="putPrimary")
    def put_primary(
        self,
        *,
        endpoint_reference: typing.Optional[builtins.str] = None,
        evaluate_target_health: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_check: typing.Optional[builtins.str] = None,
        rule_reference: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.
        :param evaluate_target_health: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.
        :param health_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.
        :param rule_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.
        '''
        value = DataAwsRoute53TrafficPolicyDocumentRulePrimary(
            endpoint_reference=endpoint_reference,
            evaluate_target_health=evaluate_target_health,
            health_check=health_check,
            rule_reference=rule_reference,
        )

        return typing.cast(None, jsii.invoke(self, "putPrimary", [value]))

    @jsii.member(jsii_name="putRegion")
    def put_region(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataAwsRoute53TrafficPolicyDocumentRuleRegion", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleRegion, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRegion", [value]))

    @jsii.member(jsii_name="putSecondary")
    def put_secondary(
        self,
        *,
        endpoint_reference: typing.Optional[builtins.str] = None,
        evaluate_target_health: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_check: typing.Optional[builtins.str] = None,
        rule_reference: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.
        :param evaluate_target_health: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.
        :param health_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.
        :param rule_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.
        '''
        value = DataAwsRoute53TrafficPolicyDocumentRuleSecondary(
            endpoint_reference=endpoint_reference,
            evaluate_target_health=evaluate_target_health,
            health_check=health_check,
            rule_reference=rule_reference,
        )

        return typing.cast(None, jsii.invoke(self, "putSecondary", [value]))

    @jsii.member(jsii_name="resetGeoProximityLocation")
    def reset_geo_proximity_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeoProximityLocation", []))

    @jsii.member(jsii_name="resetItems")
    def reset_items(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetItems", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetPrimary")
    def reset_primary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimary", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetSecondary")
    def reset_secondary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondary", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="geoProximityLocation")
    def geo_proximity_location(
        self,
    ) -> DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationList:
        return typing.cast(DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationList, jsii.get(self, "geoProximityLocation"))

    @builtins.property
    @jsii.member(jsii_name="items")
    def items(self) -> DataAwsRoute53TrafficPolicyDocumentRuleItemsList:
        return typing.cast(DataAwsRoute53TrafficPolicyDocumentRuleItemsList, jsii.get(self, "items"))

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> DataAwsRoute53TrafficPolicyDocumentRuleLocationList:
        return typing.cast(DataAwsRoute53TrafficPolicyDocumentRuleLocationList, jsii.get(self, "location"))

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(
        self,
    ) -> "DataAwsRoute53TrafficPolicyDocumentRulePrimaryOutputReference":
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentRulePrimaryOutputReference", jsii.get(self, "primary"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> "DataAwsRoute53TrafficPolicyDocumentRuleRegionList":
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentRuleRegionList", jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="secondary")
    def secondary(
        self,
    ) -> "DataAwsRoute53TrafficPolicyDocumentRuleSecondaryOutputReference":
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentRuleSecondaryOutputReference", jsii.get(self, "secondary"))

    @builtins.property
    @jsii.member(jsii_name="geoProximityLocationInput")
    def geo_proximity_location_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation]]], jsii.get(self, "geoProximityLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="itemsInput")
    def items_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleItems]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleItems]]], jsii.get(self, "itemsInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleLocation]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleLocation]]], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryInput")
    def primary_input(
        self,
    ) -> typing.Optional["DataAwsRoute53TrafficPolicyDocumentRulePrimary"]:
        return typing.cast(typing.Optional["DataAwsRoute53TrafficPolicyDocumentRulePrimary"], jsii.get(self, "primaryInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleRegion"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataAwsRoute53TrafficPolicyDocumentRuleRegion"]]], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="secondaryInput")
    def secondary_input(
        self,
    ) -> typing.Optional["DataAwsRoute53TrafficPolicyDocumentRuleSecondary"]:
        return typing.cast(typing.Optional["DataAwsRoute53TrafficPolicyDocumentRuleSecondary"], jsii.get(self, "secondaryInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

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
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRule, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRulePrimary",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_reference": "endpointReference",
        "evaluate_target_health": "evaluateTargetHealth",
        "health_check": "healthCheck",
        "rule_reference": "ruleReference",
    },
)
class DataAwsRoute53TrafficPolicyDocumentRulePrimary:
    def __init__(
        self,
        *,
        endpoint_reference: typing.Optional[builtins.str] = None,
        evaluate_target_health: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_check: typing.Optional[builtins.str] = None,
        rule_reference: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.
        :param evaluate_target_health: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.
        :param health_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.
        :param rule_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.
        '''
        if __debug__:
            def stub(
                *,
                endpoint_reference: typing.Optional[builtins.str] = None,
                evaluate_target_health: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                health_check: typing.Optional[builtins.str] = None,
                rule_reference: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument endpoint_reference", value=endpoint_reference, expected_type=type_hints["endpoint_reference"])
            check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument rule_reference", value=rule_reference, expected_type=type_hints["rule_reference"])
        self._values: typing.Dict[str, typing.Any] = {}
        if endpoint_reference is not None:
            self._values["endpoint_reference"] = endpoint_reference
        if evaluate_target_health is not None:
            self._values["evaluate_target_health"] = evaluate_target_health
        if health_check is not None:
            self._values["health_check"] = health_check
        if rule_reference is not None:
            self._values["rule_reference"] = rule_reference

    @builtins.property
    def endpoint_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.'''
        result = self._values.get("endpoint_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluate_target_health(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.'''
        result = self._values.get("evaluate_target_health")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def health_check(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.'''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.'''
        result = self._values.get("rule_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsRoute53TrafficPolicyDocumentRulePrimary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsRoute53TrafficPolicyDocumentRulePrimaryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRulePrimaryOutputReference",
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

    @jsii.member(jsii_name="resetEndpointReference")
    def reset_endpoint_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointReference", []))

    @jsii.member(jsii_name="resetEvaluateTargetHealth")
    def reset_evaluate_target_health(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluateTargetHealth", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetRuleReference")
    def reset_rule_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleReference", []))

    @builtins.property
    @jsii.member(jsii_name="endpointReferenceInput")
    def endpoint_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealthInput")
    def evaluate_target_health_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "evaluateTargetHealthInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleReferenceInput")
    def rule_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointReference")
    def endpoint_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointReference"))

    @endpoint_reference.setter
    def endpoint_reference(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointReference", value)

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealth")
    def evaluate_target_health(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "evaluateTargetHealth"))

    @evaluate_target_health.setter
    def evaluate_target_health(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluateTargetHealth", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheck"))

    @health_check.setter
    def health_check(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheck", value)

    @builtins.property
    @jsii.member(jsii_name="ruleReference")
    def rule_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleReference"))

    @rule_reference.setter
    def rule_reference(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleReference", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsRoute53TrafficPolicyDocumentRulePrimary]:
        return typing.cast(typing.Optional[DataAwsRoute53TrafficPolicyDocumentRulePrimary], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsRoute53TrafficPolicyDocumentRulePrimary],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[DataAwsRoute53TrafficPolicyDocumentRulePrimary],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleRegion",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_reference": "endpointReference",
        "evaluate_target_health": "evaluateTargetHealth",
        "health_check": "healthCheck",
        "region": "region",
        "rule_reference": "ruleReference",
    },
)
class DataAwsRoute53TrafficPolicyDocumentRuleRegion:
    def __init__(
        self,
        *,
        endpoint_reference: typing.Optional[builtins.str] = None,
        evaluate_target_health: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_check: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        rule_reference: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.
        :param evaluate_target_health: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.
        :param health_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#region DataAwsRoute53TrafficPolicyDocument#region}.
        :param rule_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.
        '''
        if __debug__:
            def stub(
                *,
                endpoint_reference: typing.Optional[builtins.str] = None,
                evaluate_target_health: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                health_check: typing.Optional[builtins.str] = None,
                region: typing.Optional[builtins.str] = None,
                rule_reference: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument endpoint_reference", value=endpoint_reference, expected_type=type_hints["endpoint_reference"])
            check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument rule_reference", value=rule_reference, expected_type=type_hints["rule_reference"])
        self._values: typing.Dict[str, typing.Any] = {}
        if endpoint_reference is not None:
            self._values["endpoint_reference"] = endpoint_reference
        if evaluate_target_health is not None:
            self._values["evaluate_target_health"] = evaluate_target_health
        if health_check is not None:
            self._values["health_check"] = health_check
        if region is not None:
            self._values["region"] = region
        if rule_reference is not None:
            self._values["rule_reference"] = rule_reference

    @builtins.property
    def endpoint_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.'''
        result = self._values.get("endpoint_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluate_target_health(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.'''
        result = self._values.get("evaluate_target_health")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def health_check(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.'''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#region DataAwsRoute53TrafficPolicyDocument#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.'''
        result = self._values.get("rule_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsRoute53TrafficPolicyDocumentRuleRegion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsRoute53TrafficPolicyDocumentRuleRegionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleRegionList",
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
    ) -> "DataAwsRoute53TrafficPolicyDocumentRuleRegionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsRoute53TrafficPolicyDocumentRuleRegionOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleRegion]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleRegion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleRegion]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataAwsRoute53TrafficPolicyDocumentRuleRegion]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsRoute53TrafficPolicyDocumentRuleRegionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleRegionOutputReference",
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

    @jsii.member(jsii_name="resetEndpointReference")
    def reset_endpoint_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointReference", []))

    @jsii.member(jsii_name="resetEvaluateTargetHealth")
    def reset_evaluate_target_health(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluateTargetHealth", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetRuleReference")
    def reset_rule_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleReference", []))

    @builtins.property
    @jsii.member(jsii_name="endpointReferenceInput")
    def endpoint_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealthInput")
    def evaluate_target_health_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "evaluateTargetHealthInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleReferenceInput")
    def rule_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointReference")
    def endpoint_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointReference"))

    @endpoint_reference.setter
    def endpoint_reference(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointReference", value)

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealth")
    def evaluate_target_health(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "evaluateTargetHealth"))

    @evaluate_target_health.setter
    def evaluate_target_health(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluateTargetHealth", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheck"))

    @health_check.setter
    def health_check(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheck", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="ruleReference")
    def rule_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleReference"))

    @rule_reference.setter
    def rule_reference(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleReference", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleRegion, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleRegion, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleRegion, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[DataAwsRoute53TrafficPolicyDocumentRuleRegion, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleSecondary",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_reference": "endpointReference",
        "evaluate_target_health": "evaluateTargetHealth",
        "health_check": "healthCheck",
        "rule_reference": "ruleReference",
    },
)
class DataAwsRoute53TrafficPolicyDocumentRuleSecondary:
    def __init__(
        self,
        *,
        endpoint_reference: typing.Optional[builtins.str] = None,
        evaluate_target_health: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_check: typing.Optional[builtins.str] = None,
        rule_reference: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.
        :param evaluate_target_health: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.
        :param health_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.
        :param rule_reference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.
        '''
        if __debug__:
            def stub(
                *,
                endpoint_reference: typing.Optional[builtins.str] = None,
                evaluate_target_health: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                health_check: typing.Optional[builtins.str] = None,
                rule_reference: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument endpoint_reference", value=endpoint_reference, expected_type=type_hints["endpoint_reference"])
            check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument rule_reference", value=rule_reference, expected_type=type_hints["rule_reference"])
        self._values: typing.Dict[str, typing.Any] = {}
        if endpoint_reference is not None:
            self._values["endpoint_reference"] = endpoint_reference
        if evaluate_target_health is not None:
            self._values["evaluate_target_health"] = evaluate_target_health
        if health_check is not None:
            self._values["health_check"] = health_check
        if rule_reference is not None:
            self._values["rule_reference"] = rule_reference

    @builtins.property
    def endpoint_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#endpoint_reference DataAwsRoute53TrafficPolicyDocument#endpoint_reference}.'''
        result = self._values.get("endpoint_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluate_target_health(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#evaluate_target_health DataAwsRoute53TrafficPolicyDocument#evaluate_target_health}.'''
        result = self._values.get("evaluate_target_health")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def health_check(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#health_check DataAwsRoute53TrafficPolicyDocument#health_check}.'''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_reference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/route53_traffic_policy_document#rule_reference DataAwsRoute53TrafficPolicyDocument#rule_reference}.'''
        result = self._values.get("rule_reference")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsRoute53TrafficPolicyDocumentRuleSecondary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsRoute53TrafficPolicyDocumentRuleSecondaryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsRoute53TrafficPolicyDocument.DataAwsRoute53TrafficPolicyDocumentRuleSecondaryOutputReference",
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

    @jsii.member(jsii_name="resetEndpointReference")
    def reset_endpoint_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointReference", []))

    @jsii.member(jsii_name="resetEvaluateTargetHealth")
    def reset_evaluate_target_health(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluateTargetHealth", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetRuleReference")
    def reset_rule_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleReference", []))

    @builtins.property
    @jsii.member(jsii_name="endpointReferenceInput")
    def endpoint_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealthInput")
    def evaluate_target_health_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "evaluateTargetHealthInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleReferenceInput")
    def rule_reference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointReference")
    def endpoint_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointReference"))

    @endpoint_reference.setter
    def endpoint_reference(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointReference", value)

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealth")
    def evaluate_target_health(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "evaluateTargetHealth"))

    @evaluate_target_health.setter
    def evaluate_target_health(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluateTargetHealth", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheck"))

    @health_check.setter
    def health_check(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheck", value)

    @builtins.property
    @jsii.member(jsii_name="ruleReference")
    def rule_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleReference"))

    @rule_reference.setter
    def rule_reference(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleReference", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsRoute53TrafficPolicyDocumentRuleSecondary]:
        return typing.cast(typing.Optional[DataAwsRoute53TrafficPolicyDocumentRuleSecondary], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsRoute53TrafficPolicyDocumentRuleSecondary],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[DataAwsRoute53TrafficPolicyDocumentRuleSecondary],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAwsRoute53TrafficPolicyDocument",
    "DataAwsRoute53TrafficPolicyDocumentConfig",
    "DataAwsRoute53TrafficPolicyDocumentEndpoint",
    "DataAwsRoute53TrafficPolicyDocumentEndpointList",
    "DataAwsRoute53TrafficPolicyDocumentEndpointOutputReference",
    "DataAwsRoute53TrafficPolicyDocumentRule",
    "DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocation",
    "DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationList",
    "DataAwsRoute53TrafficPolicyDocumentRuleGeoProximityLocationOutputReference",
    "DataAwsRoute53TrafficPolicyDocumentRuleItems",
    "DataAwsRoute53TrafficPolicyDocumentRuleItemsList",
    "DataAwsRoute53TrafficPolicyDocumentRuleItemsOutputReference",
    "DataAwsRoute53TrafficPolicyDocumentRuleList",
    "DataAwsRoute53TrafficPolicyDocumentRuleLocation",
    "DataAwsRoute53TrafficPolicyDocumentRuleLocationList",
    "DataAwsRoute53TrafficPolicyDocumentRuleLocationOutputReference",
    "DataAwsRoute53TrafficPolicyDocumentRuleOutputReference",
    "DataAwsRoute53TrafficPolicyDocumentRulePrimary",
    "DataAwsRoute53TrafficPolicyDocumentRulePrimaryOutputReference",
    "DataAwsRoute53TrafficPolicyDocumentRuleRegion",
    "DataAwsRoute53TrafficPolicyDocumentRuleRegionList",
    "DataAwsRoute53TrafficPolicyDocumentRuleRegionOutputReference",
    "DataAwsRoute53TrafficPolicyDocumentRuleSecondary",
    "DataAwsRoute53TrafficPolicyDocumentRuleSecondaryOutputReference",
]

publication.publish()
