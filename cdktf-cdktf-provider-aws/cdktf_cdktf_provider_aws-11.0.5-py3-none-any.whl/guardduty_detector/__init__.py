'''
# `aws_guardduty_detector`

Refer to the Terraform Registory for docs: [`aws_guardduty_detector`](https://www.terraform.io/docs/providers/aws/r/guardduty_detector).
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


class GuarddutyDetector(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.guarddutyDetector.GuarddutyDetector",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector aws_guardduty_detector}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        datasources: typing.Optional[typing.Union["GuarddutyDetectorDatasources", typing.Dict[str, typing.Any]]] = None,
        enable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        finding_publishing_frequency: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector aws_guardduty_detector} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param datasources: datasources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#datasources GuarddutyDetector#datasources}
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#enable GuarddutyDetector#enable}.
        :param finding_publishing_frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#finding_publishing_frequency GuarddutyDetector#finding_publishing_frequency}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#id GuarddutyDetector#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#tags GuarddutyDetector#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#tags_all GuarddutyDetector#tags_all}.
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
                datasources: typing.Optional[typing.Union[GuarddutyDetectorDatasources, typing.Dict[str, typing.Any]]] = None,
                enable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                finding_publishing_frequency: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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
        config = GuarddutyDetectorConfig(
            datasources=datasources,
            enable=enable,
            finding_publishing_frequency=finding_publishing_frequency,
            id=id,
            tags=tags,
            tags_all=tags_all,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDatasources")
    def put_datasources(
        self,
        *,
        kubernetes: typing.Optional[typing.Union["GuarddutyDetectorDatasourcesKubernetes", typing.Dict[str, typing.Any]]] = None,
        malware_protection: typing.Optional[typing.Union["GuarddutyDetectorDatasourcesMalwareProtection", typing.Dict[str, typing.Any]]] = None,
        s3_logs: typing.Optional[typing.Union["GuarddutyDetectorDatasourcesS3Logs", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param kubernetes: kubernetes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#kubernetes GuarddutyDetector#kubernetes}
        :param malware_protection: malware_protection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#malware_protection GuarddutyDetector#malware_protection}
        :param s3_logs: s3_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#s3_logs GuarddutyDetector#s3_logs}
        '''
        value = GuarddutyDetectorDatasources(
            kubernetes=kubernetes,
            malware_protection=malware_protection,
            s3_logs=s3_logs,
        )

        return typing.cast(None, jsii.invoke(self, "putDatasources", [value]))

    @jsii.member(jsii_name="resetDatasources")
    def reset_datasources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasources", []))

    @jsii.member(jsii_name="resetEnable")
    def reset_enable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnable", []))

    @jsii.member(jsii_name="resetFindingPublishingFrequency")
    def reset_finding_publishing_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFindingPublishingFrequency", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="datasources")
    def datasources(self) -> "GuarddutyDetectorDatasourcesOutputReference":
        return typing.cast("GuarddutyDetectorDatasourcesOutputReference", jsii.get(self, "datasources"))

    @builtins.property
    @jsii.member(jsii_name="datasourcesInput")
    def datasources_input(self) -> typing.Optional["GuarddutyDetectorDatasources"]:
        return typing.cast(typing.Optional["GuarddutyDetectorDatasources"], jsii.get(self, "datasourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="enableInput")
    def enable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableInput"))

    @builtins.property
    @jsii.member(jsii_name="findingPublishingFrequencyInput")
    def finding_publishing_frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "findingPublishingFrequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="enable")
    def enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enable"))

    @enable.setter
    def enable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="findingPublishingFrequency")
    def finding_publishing_frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "findingPublishingFrequency"))

    @finding_publishing_frequency.setter
    def finding_publishing_frequency(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "findingPublishingFrequency", value)

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.guarddutyDetector.GuarddutyDetectorConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "datasources": "datasources",
        "enable": "enable",
        "finding_publishing_frequency": "findingPublishingFrequency",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class GuarddutyDetectorConfig(cdktf.TerraformMetaArguments):
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
        datasources: typing.Optional[typing.Union["GuarddutyDetectorDatasources", typing.Dict[str, typing.Any]]] = None,
        enable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        finding_publishing_frequency: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param datasources: datasources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#datasources GuarddutyDetector#datasources}
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#enable GuarddutyDetector#enable}.
        :param finding_publishing_frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#finding_publishing_frequency GuarddutyDetector#finding_publishing_frequency}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#id GuarddutyDetector#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#tags GuarddutyDetector#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#tags_all GuarddutyDetector#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(datasources, dict):
            datasources = GuarddutyDetectorDatasources(**datasources)
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
                datasources: typing.Optional[typing.Union[GuarddutyDetectorDatasources, typing.Dict[str, typing.Any]]] = None,
                enable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                finding_publishing_frequency: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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
            check_type(argname="argument datasources", value=datasources, expected_type=type_hints["datasources"])
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            check_type(argname="argument finding_publishing_frequency", value=finding_publishing_frequency, expected_type=type_hints["finding_publishing_frequency"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
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
        if datasources is not None:
            self._values["datasources"] = datasources
        if enable is not None:
            self._values["enable"] = enable
        if finding_publishing_frequency is not None:
            self._values["finding_publishing_frequency"] = finding_publishing_frequency
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

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
    def datasources(self) -> typing.Optional["GuarddutyDetectorDatasources"]:
        '''datasources block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#datasources GuarddutyDetector#datasources}
        '''
        result = self._values.get("datasources")
        return typing.cast(typing.Optional["GuarddutyDetectorDatasources"], result)

    @builtins.property
    def enable(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#enable GuarddutyDetector#enable}.'''
        result = self._values.get("enable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def finding_publishing_frequency(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#finding_publishing_frequency GuarddutyDetector#finding_publishing_frequency}.'''
        result = self._values.get("finding_publishing_frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#id GuarddutyDetector#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#tags GuarddutyDetector#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#tags_all GuarddutyDetector#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyDetectorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.guarddutyDetector.GuarddutyDetectorDatasources",
    jsii_struct_bases=[],
    name_mapping={
        "kubernetes": "kubernetes",
        "malware_protection": "malwareProtection",
        "s3_logs": "s3Logs",
    },
)
class GuarddutyDetectorDatasources:
    def __init__(
        self,
        *,
        kubernetes: typing.Optional[typing.Union["GuarddutyDetectorDatasourcesKubernetes", typing.Dict[str, typing.Any]]] = None,
        malware_protection: typing.Optional[typing.Union["GuarddutyDetectorDatasourcesMalwareProtection", typing.Dict[str, typing.Any]]] = None,
        s3_logs: typing.Optional[typing.Union["GuarddutyDetectorDatasourcesS3Logs", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param kubernetes: kubernetes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#kubernetes GuarddutyDetector#kubernetes}
        :param malware_protection: malware_protection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#malware_protection GuarddutyDetector#malware_protection}
        :param s3_logs: s3_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#s3_logs GuarddutyDetector#s3_logs}
        '''
        if isinstance(kubernetes, dict):
            kubernetes = GuarddutyDetectorDatasourcesKubernetes(**kubernetes)
        if isinstance(malware_protection, dict):
            malware_protection = GuarddutyDetectorDatasourcesMalwareProtection(**malware_protection)
        if isinstance(s3_logs, dict):
            s3_logs = GuarddutyDetectorDatasourcesS3Logs(**s3_logs)
        if __debug__:
            def stub(
                *,
                kubernetes: typing.Optional[typing.Union[GuarddutyDetectorDatasourcesKubernetes, typing.Dict[str, typing.Any]]] = None,
                malware_protection: typing.Optional[typing.Union[GuarddutyDetectorDatasourcesMalwareProtection, typing.Dict[str, typing.Any]]] = None,
                s3_logs: typing.Optional[typing.Union[GuarddutyDetectorDatasourcesS3Logs, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument kubernetes", value=kubernetes, expected_type=type_hints["kubernetes"])
            check_type(argname="argument malware_protection", value=malware_protection, expected_type=type_hints["malware_protection"])
            check_type(argname="argument s3_logs", value=s3_logs, expected_type=type_hints["s3_logs"])
        self._values: typing.Dict[str, typing.Any] = {}
        if kubernetes is not None:
            self._values["kubernetes"] = kubernetes
        if malware_protection is not None:
            self._values["malware_protection"] = malware_protection
        if s3_logs is not None:
            self._values["s3_logs"] = s3_logs

    @builtins.property
    def kubernetes(self) -> typing.Optional["GuarddutyDetectorDatasourcesKubernetes"]:
        '''kubernetes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#kubernetes GuarddutyDetector#kubernetes}
        '''
        result = self._values.get("kubernetes")
        return typing.cast(typing.Optional["GuarddutyDetectorDatasourcesKubernetes"], result)

    @builtins.property
    def malware_protection(
        self,
    ) -> typing.Optional["GuarddutyDetectorDatasourcesMalwareProtection"]:
        '''malware_protection block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#malware_protection GuarddutyDetector#malware_protection}
        '''
        result = self._values.get("malware_protection")
        return typing.cast(typing.Optional["GuarddutyDetectorDatasourcesMalwareProtection"], result)

    @builtins.property
    def s3_logs(self) -> typing.Optional["GuarddutyDetectorDatasourcesS3Logs"]:
        '''s3_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#s3_logs GuarddutyDetector#s3_logs}
        '''
        result = self._values.get("s3_logs")
        return typing.cast(typing.Optional["GuarddutyDetectorDatasourcesS3Logs"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyDetectorDatasources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.guarddutyDetector.GuarddutyDetectorDatasourcesKubernetes",
    jsii_struct_bases=[],
    name_mapping={"audit_logs": "auditLogs"},
)
class GuarddutyDetectorDatasourcesKubernetes:
    def __init__(
        self,
        *,
        audit_logs: typing.Union["GuarddutyDetectorDatasourcesKubernetesAuditLogs", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param audit_logs: audit_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#audit_logs GuarddutyDetector#audit_logs}
        '''
        if isinstance(audit_logs, dict):
            audit_logs = GuarddutyDetectorDatasourcesKubernetesAuditLogs(**audit_logs)
        if __debug__:
            def stub(
                *,
                audit_logs: typing.Union[GuarddutyDetectorDatasourcesKubernetesAuditLogs, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument audit_logs", value=audit_logs, expected_type=type_hints["audit_logs"])
        self._values: typing.Dict[str, typing.Any] = {
            "audit_logs": audit_logs,
        }

    @builtins.property
    def audit_logs(self) -> "GuarddutyDetectorDatasourcesKubernetesAuditLogs":
        '''audit_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#audit_logs GuarddutyDetector#audit_logs}
        '''
        result = self._values.get("audit_logs")
        assert result is not None, "Required property 'audit_logs' is missing"
        return typing.cast("GuarddutyDetectorDatasourcesKubernetesAuditLogs", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyDetectorDatasourcesKubernetes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.guarddutyDetector.GuarddutyDetectorDatasourcesKubernetesAuditLogs",
    jsii_struct_bases=[],
    name_mapping={"enable": "enable"},
)
class GuarddutyDetectorDatasourcesKubernetesAuditLogs:
    def __init__(
        self,
        *,
        enable: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#enable GuarddutyDetector#enable}.
        '''
        if __debug__:
            def stub(*, enable: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
        self._values: typing.Dict[str, typing.Any] = {
            "enable": enable,
        }

    @builtins.property
    def enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#enable GuarddutyDetector#enable}.'''
        result = self._values.get("enable")
        assert result is not None, "Required property 'enable' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyDetectorDatasourcesKubernetesAuditLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GuarddutyDetectorDatasourcesKubernetesAuditLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.guarddutyDetector.GuarddutyDetectorDatasourcesKubernetesAuditLogsOutputReference",
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
    @jsii.member(jsii_name="enableInput")
    def enable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableInput"))

    @builtins.property
    @jsii.member(jsii_name="enable")
    def enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enable"))

    @enable.setter
    def enable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GuarddutyDetectorDatasourcesKubernetesAuditLogs]:
        return typing.cast(typing.Optional[GuarddutyDetectorDatasourcesKubernetesAuditLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GuarddutyDetectorDatasourcesKubernetesAuditLogs],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GuarddutyDetectorDatasourcesKubernetesAuditLogs],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GuarddutyDetectorDatasourcesKubernetesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.guarddutyDetector.GuarddutyDetectorDatasourcesKubernetesOutputReference",
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

    @jsii.member(jsii_name="putAuditLogs")
    def put_audit_logs(
        self,
        *,
        enable: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#enable GuarddutyDetector#enable}.
        '''
        value = GuarddutyDetectorDatasourcesKubernetesAuditLogs(enable=enable)

        return typing.cast(None, jsii.invoke(self, "putAuditLogs", [value]))

    @builtins.property
    @jsii.member(jsii_name="auditLogs")
    def audit_logs(
        self,
    ) -> GuarddutyDetectorDatasourcesKubernetesAuditLogsOutputReference:
        return typing.cast(GuarddutyDetectorDatasourcesKubernetesAuditLogsOutputReference, jsii.get(self, "auditLogs"))

    @builtins.property
    @jsii.member(jsii_name="auditLogsInput")
    def audit_logs_input(
        self,
    ) -> typing.Optional[GuarddutyDetectorDatasourcesKubernetesAuditLogs]:
        return typing.cast(typing.Optional[GuarddutyDetectorDatasourcesKubernetesAuditLogs], jsii.get(self, "auditLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GuarddutyDetectorDatasourcesKubernetes]:
        return typing.cast(typing.Optional[GuarddutyDetectorDatasourcesKubernetes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GuarddutyDetectorDatasourcesKubernetes],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GuarddutyDetectorDatasourcesKubernetes],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.guarddutyDetector.GuarddutyDetectorDatasourcesMalwareProtection",
    jsii_struct_bases=[],
    name_mapping={"scan_ec2_instance_with_findings": "scanEc2InstanceWithFindings"},
)
class GuarddutyDetectorDatasourcesMalwareProtection:
    def __init__(
        self,
        *,
        scan_ec2_instance_with_findings: typing.Union["GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param scan_ec2_instance_with_findings: scan_ec2_instance_with_findings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#scan_ec2_instance_with_findings GuarddutyDetector#scan_ec2_instance_with_findings}
        '''
        if isinstance(scan_ec2_instance_with_findings, dict):
            scan_ec2_instance_with_findings = GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings(**scan_ec2_instance_with_findings)
        if __debug__:
            def stub(
                *,
                scan_ec2_instance_with_findings: typing.Union[GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scan_ec2_instance_with_findings", value=scan_ec2_instance_with_findings, expected_type=type_hints["scan_ec2_instance_with_findings"])
        self._values: typing.Dict[str, typing.Any] = {
            "scan_ec2_instance_with_findings": scan_ec2_instance_with_findings,
        }

    @builtins.property
    def scan_ec2_instance_with_findings(
        self,
    ) -> "GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings":
        '''scan_ec2_instance_with_findings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#scan_ec2_instance_with_findings GuarddutyDetector#scan_ec2_instance_with_findings}
        '''
        result = self._values.get("scan_ec2_instance_with_findings")
        assert result is not None, "Required property 'scan_ec2_instance_with_findings' is missing"
        return typing.cast("GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyDetectorDatasourcesMalwareProtection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GuarddutyDetectorDatasourcesMalwareProtectionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.guarddutyDetector.GuarddutyDetectorDatasourcesMalwareProtectionOutputReference",
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

    @jsii.member(jsii_name="putScanEc2InstanceWithFindings")
    def put_scan_ec2_instance_with_findings(
        self,
        *,
        ebs_volumes: typing.Union["GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param ebs_volumes: ebs_volumes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#ebs_volumes GuarddutyDetector#ebs_volumes}
        '''
        value = GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings(
            ebs_volumes=ebs_volumes
        )

        return typing.cast(None, jsii.invoke(self, "putScanEc2InstanceWithFindings", [value]))

    @builtins.property
    @jsii.member(jsii_name="scanEc2InstanceWithFindings")
    def scan_ec2_instance_with_findings(
        self,
    ) -> "GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsOutputReference":
        return typing.cast("GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsOutputReference", jsii.get(self, "scanEc2InstanceWithFindings"))

    @builtins.property
    @jsii.member(jsii_name="scanEc2InstanceWithFindingsInput")
    def scan_ec2_instance_with_findings_input(
        self,
    ) -> typing.Optional["GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings"]:
        return typing.cast(typing.Optional["GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings"], jsii.get(self, "scanEc2InstanceWithFindingsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GuarddutyDetectorDatasourcesMalwareProtection]:
        return typing.cast(typing.Optional[GuarddutyDetectorDatasourcesMalwareProtection], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GuarddutyDetectorDatasourcesMalwareProtection],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GuarddutyDetectorDatasourcesMalwareProtection],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.guarddutyDetector.GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings",
    jsii_struct_bases=[],
    name_mapping={"ebs_volumes": "ebsVolumes"},
)
class GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings:
    def __init__(
        self,
        *,
        ebs_volumes: typing.Union["GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param ebs_volumes: ebs_volumes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#ebs_volumes GuarddutyDetector#ebs_volumes}
        '''
        if isinstance(ebs_volumes, dict):
            ebs_volumes = GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes(**ebs_volumes)
        if __debug__:
            def stub(
                *,
                ebs_volumes: typing.Union[GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument ebs_volumes", value=ebs_volumes, expected_type=type_hints["ebs_volumes"])
        self._values: typing.Dict[str, typing.Any] = {
            "ebs_volumes": ebs_volumes,
        }

    @builtins.property
    def ebs_volumes(
        self,
    ) -> "GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes":
        '''ebs_volumes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#ebs_volumes GuarddutyDetector#ebs_volumes}
        '''
        result = self._values.get("ebs_volumes")
        assert result is not None, "Required property 'ebs_volumes' is missing"
        return typing.cast("GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.guarddutyDetector.GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes",
    jsii_struct_bases=[],
    name_mapping={"enable": "enable"},
)
class GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes:
    def __init__(
        self,
        *,
        enable: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#enable GuarddutyDetector#enable}.
        '''
        if __debug__:
            def stub(*, enable: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
        self._values: typing.Dict[str, typing.Any] = {
            "enable": enable,
        }

    @builtins.property
    def enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#enable GuarddutyDetector#enable}.'''
        result = self._values.get("enable")
        assert result is not None, "Required property 'enable' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.guarddutyDetector.GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesOutputReference",
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
    @jsii.member(jsii_name="enableInput")
    def enable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableInput"))

    @builtins.property
    @jsii.member(jsii_name="enable")
    def enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enable"))

    @enable.setter
    def enable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes]:
        return typing.cast(typing.Optional[GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.guarddutyDetector.GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsOutputReference",
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

    @jsii.member(jsii_name="putEbsVolumes")
    def put_ebs_volumes(
        self,
        *,
        enable: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#enable GuarddutyDetector#enable}.
        '''
        value = GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes(
            enable=enable
        )

        return typing.cast(None, jsii.invoke(self, "putEbsVolumes", [value]))

    @builtins.property
    @jsii.member(jsii_name="ebsVolumes")
    def ebs_volumes(
        self,
    ) -> GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesOutputReference:
        return typing.cast(GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesOutputReference, jsii.get(self, "ebsVolumes"))

    @builtins.property
    @jsii.member(jsii_name="ebsVolumesInput")
    def ebs_volumes_input(
        self,
    ) -> typing.Optional[GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes]:
        return typing.cast(typing.Optional[GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes], jsii.get(self, "ebsVolumesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings]:
        return typing.cast(typing.Optional[GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GuarddutyDetectorDatasourcesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.guarddutyDetector.GuarddutyDetectorDatasourcesOutputReference",
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

    @jsii.member(jsii_name="putKubernetes")
    def put_kubernetes(
        self,
        *,
        audit_logs: typing.Union[GuarddutyDetectorDatasourcesKubernetesAuditLogs, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param audit_logs: audit_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#audit_logs GuarddutyDetector#audit_logs}
        '''
        value = GuarddutyDetectorDatasourcesKubernetes(audit_logs=audit_logs)

        return typing.cast(None, jsii.invoke(self, "putKubernetes", [value]))

    @jsii.member(jsii_name="putMalwareProtection")
    def put_malware_protection(
        self,
        *,
        scan_ec2_instance_with_findings: typing.Union[GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param scan_ec2_instance_with_findings: scan_ec2_instance_with_findings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#scan_ec2_instance_with_findings GuarddutyDetector#scan_ec2_instance_with_findings}
        '''
        value = GuarddutyDetectorDatasourcesMalwareProtection(
            scan_ec2_instance_with_findings=scan_ec2_instance_with_findings
        )

        return typing.cast(None, jsii.invoke(self, "putMalwareProtection", [value]))

    @jsii.member(jsii_name="putS3Logs")
    def put_s3_logs(
        self,
        *,
        enable: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#enable GuarddutyDetector#enable}.
        '''
        value = GuarddutyDetectorDatasourcesS3Logs(enable=enable)

        return typing.cast(None, jsii.invoke(self, "putS3Logs", [value]))

    @jsii.member(jsii_name="resetKubernetes")
    def reset_kubernetes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKubernetes", []))

    @jsii.member(jsii_name="resetMalwareProtection")
    def reset_malware_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMalwareProtection", []))

    @jsii.member(jsii_name="resetS3Logs")
    def reset_s3_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Logs", []))

    @builtins.property
    @jsii.member(jsii_name="kubernetes")
    def kubernetes(self) -> GuarddutyDetectorDatasourcesKubernetesOutputReference:
        return typing.cast(GuarddutyDetectorDatasourcesKubernetesOutputReference, jsii.get(self, "kubernetes"))

    @builtins.property
    @jsii.member(jsii_name="malwareProtection")
    def malware_protection(
        self,
    ) -> GuarddutyDetectorDatasourcesMalwareProtectionOutputReference:
        return typing.cast(GuarddutyDetectorDatasourcesMalwareProtectionOutputReference, jsii.get(self, "malwareProtection"))

    @builtins.property
    @jsii.member(jsii_name="s3Logs")
    def s3_logs(self) -> "GuarddutyDetectorDatasourcesS3LogsOutputReference":
        return typing.cast("GuarddutyDetectorDatasourcesS3LogsOutputReference", jsii.get(self, "s3Logs"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesInput")
    def kubernetes_input(
        self,
    ) -> typing.Optional[GuarddutyDetectorDatasourcesKubernetes]:
        return typing.cast(typing.Optional[GuarddutyDetectorDatasourcesKubernetes], jsii.get(self, "kubernetesInput"))

    @builtins.property
    @jsii.member(jsii_name="malwareProtectionInput")
    def malware_protection_input(
        self,
    ) -> typing.Optional[GuarddutyDetectorDatasourcesMalwareProtection]:
        return typing.cast(typing.Optional[GuarddutyDetectorDatasourcesMalwareProtection], jsii.get(self, "malwareProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="s3LogsInput")
    def s3_logs_input(self) -> typing.Optional["GuarddutyDetectorDatasourcesS3Logs"]:
        return typing.cast(typing.Optional["GuarddutyDetectorDatasourcesS3Logs"], jsii.get(self, "s3LogsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GuarddutyDetectorDatasources]:
        return typing.cast(typing.Optional[GuarddutyDetectorDatasources], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GuarddutyDetectorDatasources],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[GuarddutyDetectorDatasources]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.guarddutyDetector.GuarddutyDetectorDatasourcesS3Logs",
    jsii_struct_bases=[],
    name_mapping={"enable": "enable"},
)
class GuarddutyDetectorDatasourcesS3Logs:
    def __init__(
        self,
        *,
        enable: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#enable GuarddutyDetector#enable}.
        '''
        if __debug__:
            def stub(*, enable: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
        self._values: typing.Dict[str, typing.Any] = {
            "enable": enable,
        }

    @builtins.property
    def enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_detector#enable GuarddutyDetector#enable}.'''
        result = self._values.get("enable")
        assert result is not None, "Required property 'enable' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyDetectorDatasourcesS3Logs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GuarddutyDetectorDatasourcesS3LogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.guarddutyDetector.GuarddutyDetectorDatasourcesS3LogsOutputReference",
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
    @jsii.member(jsii_name="enableInput")
    def enable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableInput"))

    @builtins.property
    @jsii.member(jsii_name="enable")
    def enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enable"))

    @enable.setter
    def enable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GuarddutyDetectorDatasourcesS3Logs]:
        return typing.cast(typing.Optional[GuarddutyDetectorDatasourcesS3Logs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GuarddutyDetectorDatasourcesS3Logs],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GuarddutyDetectorDatasourcesS3Logs],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GuarddutyDetector",
    "GuarddutyDetectorConfig",
    "GuarddutyDetectorDatasources",
    "GuarddutyDetectorDatasourcesKubernetes",
    "GuarddutyDetectorDatasourcesKubernetesAuditLogs",
    "GuarddutyDetectorDatasourcesKubernetesAuditLogsOutputReference",
    "GuarddutyDetectorDatasourcesKubernetesOutputReference",
    "GuarddutyDetectorDatasourcesMalwareProtection",
    "GuarddutyDetectorDatasourcesMalwareProtectionOutputReference",
    "GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings",
    "GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes",
    "GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesOutputReference",
    "GuarddutyDetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsOutputReference",
    "GuarddutyDetectorDatasourcesOutputReference",
    "GuarddutyDetectorDatasourcesS3Logs",
    "GuarddutyDetectorDatasourcesS3LogsOutputReference",
]

publication.publish()
