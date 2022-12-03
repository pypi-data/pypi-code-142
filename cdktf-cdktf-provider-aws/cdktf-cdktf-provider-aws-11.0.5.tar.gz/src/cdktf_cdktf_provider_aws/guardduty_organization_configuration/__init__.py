'''
# `aws_guardduty_organization_configuration`

Refer to the Terraform Registory for docs: [`aws_guardduty_organization_configuration`](https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration).
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


class GuarddutyOrganizationConfiguration(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.guarddutyOrganizationConfiguration.GuarddutyOrganizationConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration aws_guardduty_organization_configuration}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        auto_enable: typing.Union[builtins.bool, cdktf.IResolvable],
        detector_id: builtins.str,
        datasources: typing.Optional[typing.Union["GuarddutyOrganizationConfigurationDatasources", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration aws_guardduty_organization_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param auto_enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#auto_enable GuarddutyOrganizationConfiguration#auto_enable}.
        :param detector_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#detector_id GuarddutyOrganizationConfiguration#detector_id}.
        :param datasources: datasources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#datasources GuarddutyOrganizationConfiguration#datasources}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#id GuarddutyOrganizationConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
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
                auto_enable: typing.Union[builtins.bool, cdktf.IResolvable],
                detector_id: builtins.str,
                datasources: typing.Optional[typing.Union[GuarddutyOrganizationConfigurationDatasources, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
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
        config = GuarddutyOrganizationConfigurationConfig(
            auto_enable=auto_enable,
            detector_id=detector_id,
            datasources=datasources,
            id=id,
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
        kubernetes: typing.Optional[typing.Union["GuarddutyOrganizationConfigurationDatasourcesKubernetes", typing.Dict[str, typing.Any]]] = None,
        malware_protection: typing.Optional[typing.Union["GuarddutyOrganizationConfigurationDatasourcesMalwareProtection", typing.Dict[str, typing.Any]]] = None,
        s3_logs: typing.Optional[typing.Union["GuarddutyOrganizationConfigurationDatasourcesS3Logs", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param kubernetes: kubernetes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#kubernetes GuarddutyOrganizationConfiguration#kubernetes}
        :param malware_protection: malware_protection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#malware_protection GuarddutyOrganizationConfiguration#malware_protection}
        :param s3_logs: s3_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#s3_logs GuarddutyOrganizationConfiguration#s3_logs}
        '''
        value = GuarddutyOrganizationConfigurationDatasources(
            kubernetes=kubernetes,
            malware_protection=malware_protection,
            s3_logs=s3_logs,
        )

        return typing.cast(None, jsii.invoke(self, "putDatasources", [value]))

    @jsii.member(jsii_name="resetDatasources")
    def reset_datasources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasources", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="datasources")
    def datasources(
        self,
    ) -> "GuarddutyOrganizationConfigurationDatasourcesOutputReference":
        return typing.cast("GuarddutyOrganizationConfigurationDatasourcesOutputReference", jsii.get(self, "datasources"))

    @builtins.property
    @jsii.member(jsii_name="autoEnableInput")
    def auto_enable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoEnableInput"))

    @builtins.property
    @jsii.member(jsii_name="datasourcesInput")
    def datasources_input(
        self,
    ) -> typing.Optional["GuarddutyOrganizationConfigurationDatasources"]:
        return typing.cast(typing.Optional["GuarddutyOrganizationConfigurationDatasources"], jsii.get(self, "datasourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="detectorIdInput")
    def detector_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "detectorIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="autoEnable")
    def auto_enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoEnable"))

    @auto_enable.setter
    def auto_enable(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoEnable", value)

    @builtins.property
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorId", value)

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


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.guarddutyOrganizationConfiguration.GuarddutyOrganizationConfigurationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "auto_enable": "autoEnable",
        "detector_id": "detectorId",
        "datasources": "datasources",
        "id": "id",
    },
)
class GuarddutyOrganizationConfigurationConfig(cdktf.TerraformMetaArguments):
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
        auto_enable: typing.Union[builtins.bool, cdktf.IResolvable],
        detector_id: builtins.str,
        datasources: typing.Optional[typing.Union["GuarddutyOrganizationConfigurationDatasources", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param auto_enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#auto_enable GuarddutyOrganizationConfiguration#auto_enable}.
        :param detector_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#detector_id GuarddutyOrganizationConfiguration#detector_id}.
        :param datasources: datasources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#datasources GuarddutyOrganizationConfiguration#datasources}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#id GuarddutyOrganizationConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(datasources, dict):
            datasources = GuarddutyOrganizationConfigurationDatasources(**datasources)
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
                auto_enable: typing.Union[builtins.bool, cdktf.IResolvable],
                detector_id: builtins.str,
                datasources: typing.Optional[typing.Union[GuarddutyOrganizationConfigurationDatasources, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument auto_enable", value=auto_enable, expected_type=type_hints["auto_enable"])
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument datasources", value=datasources, expected_type=type_hints["datasources"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "auto_enable": auto_enable,
            "detector_id": detector_id,
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
        if datasources is not None:
            self._values["datasources"] = datasources
        if id is not None:
            self._values["id"] = id

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
    def auto_enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#auto_enable GuarddutyOrganizationConfiguration#auto_enable}.'''
        result = self._values.get("auto_enable")
        assert result is not None, "Required property 'auto_enable' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#detector_id GuarddutyOrganizationConfiguration#detector_id}.'''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def datasources(
        self,
    ) -> typing.Optional["GuarddutyOrganizationConfigurationDatasources"]:
        '''datasources block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#datasources GuarddutyOrganizationConfiguration#datasources}
        '''
        result = self._values.get("datasources")
        return typing.cast(typing.Optional["GuarddutyOrganizationConfigurationDatasources"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#id GuarddutyOrganizationConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyOrganizationConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.guarddutyOrganizationConfiguration.GuarddutyOrganizationConfigurationDatasources",
    jsii_struct_bases=[],
    name_mapping={
        "kubernetes": "kubernetes",
        "malware_protection": "malwareProtection",
        "s3_logs": "s3Logs",
    },
)
class GuarddutyOrganizationConfigurationDatasources:
    def __init__(
        self,
        *,
        kubernetes: typing.Optional[typing.Union["GuarddutyOrganizationConfigurationDatasourcesKubernetes", typing.Dict[str, typing.Any]]] = None,
        malware_protection: typing.Optional[typing.Union["GuarddutyOrganizationConfigurationDatasourcesMalwareProtection", typing.Dict[str, typing.Any]]] = None,
        s3_logs: typing.Optional[typing.Union["GuarddutyOrganizationConfigurationDatasourcesS3Logs", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param kubernetes: kubernetes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#kubernetes GuarddutyOrganizationConfiguration#kubernetes}
        :param malware_protection: malware_protection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#malware_protection GuarddutyOrganizationConfiguration#malware_protection}
        :param s3_logs: s3_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#s3_logs GuarddutyOrganizationConfiguration#s3_logs}
        '''
        if isinstance(kubernetes, dict):
            kubernetes = GuarddutyOrganizationConfigurationDatasourcesKubernetes(**kubernetes)
        if isinstance(malware_protection, dict):
            malware_protection = GuarddutyOrganizationConfigurationDatasourcesMalwareProtection(**malware_protection)
        if isinstance(s3_logs, dict):
            s3_logs = GuarddutyOrganizationConfigurationDatasourcesS3Logs(**s3_logs)
        if __debug__:
            def stub(
                *,
                kubernetes: typing.Optional[typing.Union[GuarddutyOrganizationConfigurationDatasourcesKubernetes, typing.Dict[str, typing.Any]]] = None,
                malware_protection: typing.Optional[typing.Union[GuarddutyOrganizationConfigurationDatasourcesMalwareProtection, typing.Dict[str, typing.Any]]] = None,
                s3_logs: typing.Optional[typing.Union[GuarddutyOrganizationConfigurationDatasourcesS3Logs, typing.Dict[str, typing.Any]]] = None,
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
    def kubernetes(
        self,
    ) -> typing.Optional["GuarddutyOrganizationConfigurationDatasourcesKubernetes"]:
        '''kubernetes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#kubernetes GuarddutyOrganizationConfiguration#kubernetes}
        '''
        result = self._values.get("kubernetes")
        return typing.cast(typing.Optional["GuarddutyOrganizationConfigurationDatasourcesKubernetes"], result)

    @builtins.property
    def malware_protection(
        self,
    ) -> typing.Optional["GuarddutyOrganizationConfigurationDatasourcesMalwareProtection"]:
        '''malware_protection block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#malware_protection GuarddutyOrganizationConfiguration#malware_protection}
        '''
        result = self._values.get("malware_protection")
        return typing.cast(typing.Optional["GuarddutyOrganizationConfigurationDatasourcesMalwareProtection"], result)

    @builtins.property
    def s3_logs(
        self,
    ) -> typing.Optional["GuarddutyOrganizationConfigurationDatasourcesS3Logs"]:
        '''s3_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#s3_logs GuarddutyOrganizationConfiguration#s3_logs}
        '''
        result = self._values.get("s3_logs")
        return typing.cast(typing.Optional["GuarddutyOrganizationConfigurationDatasourcesS3Logs"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyOrganizationConfigurationDatasources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.guarddutyOrganizationConfiguration.GuarddutyOrganizationConfigurationDatasourcesKubernetes",
    jsii_struct_bases=[],
    name_mapping={"audit_logs": "auditLogs"},
)
class GuarddutyOrganizationConfigurationDatasourcesKubernetes:
    def __init__(
        self,
        *,
        audit_logs: typing.Union["GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogs", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param audit_logs: audit_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#audit_logs GuarddutyOrganizationConfiguration#audit_logs}
        '''
        if isinstance(audit_logs, dict):
            audit_logs = GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogs(**audit_logs)
        if __debug__:
            def stub(
                *,
                audit_logs: typing.Union[GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogs, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument audit_logs", value=audit_logs, expected_type=type_hints["audit_logs"])
        self._values: typing.Dict[str, typing.Any] = {
            "audit_logs": audit_logs,
        }

    @builtins.property
    def audit_logs(
        self,
    ) -> "GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogs":
        '''audit_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#audit_logs GuarddutyOrganizationConfiguration#audit_logs}
        '''
        result = self._values.get("audit_logs")
        assert result is not None, "Required property 'audit_logs' is missing"
        return typing.cast("GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogs", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyOrganizationConfigurationDatasourcesKubernetes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.guarddutyOrganizationConfiguration.GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogs",
    jsii_struct_bases=[],
    name_mapping={"enable": "enable"},
)
class GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogs:
    def __init__(
        self,
        *,
        enable: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#enable GuarddutyOrganizationConfiguration#enable}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#enable GuarddutyOrganizationConfiguration#enable}.'''
        result = self._values.get("enable")
        assert result is not None, "Required property 'enable' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.guarddutyOrganizationConfiguration.GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogsOutputReference",
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
    ) -> typing.Optional[GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogs]:
        return typing.cast(typing.Optional[GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogs],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogs],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GuarddutyOrganizationConfigurationDatasourcesKubernetesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.guarddutyOrganizationConfiguration.GuarddutyOrganizationConfigurationDatasourcesKubernetesOutputReference",
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
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#enable GuarddutyOrganizationConfiguration#enable}.
        '''
        value = GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogs(
            enable=enable
        )

        return typing.cast(None, jsii.invoke(self, "putAuditLogs", [value]))

    @builtins.property
    @jsii.member(jsii_name="auditLogs")
    def audit_logs(
        self,
    ) -> GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogsOutputReference:
        return typing.cast(GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogsOutputReference, jsii.get(self, "auditLogs"))

    @builtins.property
    @jsii.member(jsii_name="auditLogsInput")
    def audit_logs_input(
        self,
    ) -> typing.Optional[GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogs]:
        return typing.cast(typing.Optional[GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogs], jsii.get(self, "auditLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GuarddutyOrganizationConfigurationDatasourcesKubernetes]:
        return typing.cast(typing.Optional[GuarddutyOrganizationConfigurationDatasourcesKubernetes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GuarddutyOrganizationConfigurationDatasourcesKubernetes],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GuarddutyOrganizationConfigurationDatasourcesKubernetes],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.guarddutyOrganizationConfiguration.GuarddutyOrganizationConfigurationDatasourcesMalwareProtection",
    jsii_struct_bases=[],
    name_mapping={"scan_ec2_instance_with_findings": "scanEc2InstanceWithFindings"},
)
class GuarddutyOrganizationConfigurationDatasourcesMalwareProtection:
    def __init__(
        self,
        *,
        scan_ec2_instance_with_findings: typing.Union["GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param scan_ec2_instance_with_findings: scan_ec2_instance_with_findings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#scan_ec2_instance_with_findings GuarddutyOrganizationConfiguration#scan_ec2_instance_with_findings}
        '''
        if isinstance(scan_ec2_instance_with_findings, dict):
            scan_ec2_instance_with_findings = GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings(**scan_ec2_instance_with_findings)
        if __debug__:
            def stub(
                *,
                scan_ec2_instance_with_findings: typing.Union[GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings, typing.Dict[str, typing.Any]],
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
    ) -> "GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings":
        '''scan_ec2_instance_with_findings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#scan_ec2_instance_with_findings GuarddutyOrganizationConfiguration#scan_ec2_instance_with_findings}
        '''
        result = self._values.get("scan_ec2_instance_with_findings")
        assert result is not None, "Required property 'scan_ec2_instance_with_findings' is missing"
        return typing.cast("GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyOrganizationConfigurationDatasourcesMalwareProtection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.guarddutyOrganizationConfiguration.GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionOutputReference",
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
        ebs_volumes: typing.Union["GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param ebs_volumes: ebs_volumes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#ebs_volumes GuarddutyOrganizationConfiguration#ebs_volumes}
        '''
        value = GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings(
            ebs_volumes=ebs_volumes
        )

        return typing.cast(None, jsii.invoke(self, "putScanEc2InstanceWithFindings", [value]))

    @builtins.property
    @jsii.member(jsii_name="scanEc2InstanceWithFindings")
    def scan_ec2_instance_with_findings(
        self,
    ) -> "GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsOutputReference":
        return typing.cast("GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsOutputReference", jsii.get(self, "scanEc2InstanceWithFindings"))

    @builtins.property
    @jsii.member(jsii_name="scanEc2InstanceWithFindingsInput")
    def scan_ec2_instance_with_findings_input(
        self,
    ) -> typing.Optional["GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings"]:
        return typing.cast(typing.Optional["GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings"], jsii.get(self, "scanEc2InstanceWithFindingsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GuarddutyOrganizationConfigurationDatasourcesMalwareProtection]:
        return typing.cast(typing.Optional[GuarddutyOrganizationConfigurationDatasourcesMalwareProtection], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GuarddutyOrganizationConfigurationDatasourcesMalwareProtection],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GuarddutyOrganizationConfigurationDatasourcesMalwareProtection],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.guarddutyOrganizationConfiguration.GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings",
    jsii_struct_bases=[],
    name_mapping={"ebs_volumes": "ebsVolumes"},
)
class GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings:
    def __init__(
        self,
        *,
        ebs_volumes: typing.Union["GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param ebs_volumes: ebs_volumes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#ebs_volumes GuarddutyOrganizationConfiguration#ebs_volumes}
        '''
        if isinstance(ebs_volumes, dict):
            ebs_volumes = GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes(**ebs_volumes)
        if __debug__:
            def stub(
                *,
                ebs_volumes: typing.Union[GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes, typing.Dict[str, typing.Any]],
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
    ) -> "GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes":
        '''ebs_volumes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#ebs_volumes GuarddutyOrganizationConfiguration#ebs_volumes}
        '''
        result = self._values.get("ebs_volumes")
        assert result is not None, "Required property 'ebs_volumes' is missing"
        return typing.cast("GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.guarddutyOrganizationConfiguration.GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes",
    jsii_struct_bases=[],
    name_mapping={"auto_enable": "autoEnable"},
)
class GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes:
    def __init__(
        self,
        *,
        auto_enable: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param auto_enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#auto_enable GuarddutyOrganizationConfiguration#auto_enable}.
        '''
        if __debug__:
            def stub(
                *,
                auto_enable: typing.Union[builtins.bool, cdktf.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument auto_enable", value=auto_enable, expected_type=type_hints["auto_enable"])
        self._values: typing.Dict[str, typing.Any] = {
            "auto_enable": auto_enable,
        }

    @builtins.property
    def auto_enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#auto_enable GuarddutyOrganizationConfiguration#auto_enable}.'''
        result = self._values.get("auto_enable")
        assert result is not None, "Required property 'auto_enable' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.guarddutyOrganizationConfiguration.GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesOutputReference",
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
    @jsii.member(jsii_name="autoEnableInput")
    def auto_enable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoEnableInput"))

    @builtins.property
    @jsii.member(jsii_name="autoEnable")
    def auto_enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoEnable"))

    @auto_enable.setter
    def auto_enable(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoEnable", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes]:
        return typing.cast(typing.Optional[GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.guarddutyOrganizationConfiguration.GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsOutputReference",
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
        auto_enable: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param auto_enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#auto_enable GuarddutyOrganizationConfiguration#auto_enable}.
        '''
        value = GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes(
            auto_enable=auto_enable
        )

        return typing.cast(None, jsii.invoke(self, "putEbsVolumes", [value]))

    @builtins.property
    @jsii.member(jsii_name="ebsVolumes")
    def ebs_volumes(
        self,
    ) -> GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesOutputReference:
        return typing.cast(GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesOutputReference, jsii.get(self, "ebsVolumes"))

    @builtins.property
    @jsii.member(jsii_name="ebsVolumesInput")
    def ebs_volumes_input(
        self,
    ) -> typing.Optional[GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes]:
        return typing.cast(typing.Optional[GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes], jsii.get(self, "ebsVolumesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings]:
        return typing.cast(typing.Optional[GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GuarddutyOrganizationConfigurationDatasourcesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.guarddutyOrganizationConfiguration.GuarddutyOrganizationConfigurationDatasourcesOutputReference",
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
        audit_logs: typing.Union[GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogs, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param audit_logs: audit_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#audit_logs GuarddutyOrganizationConfiguration#audit_logs}
        '''
        value = GuarddutyOrganizationConfigurationDatasourcesKubernetes(
            audit_logs=audit_logs
        )

        return typing.cast(None, jsii.invoke(self, "putKubernetes", [value]))

    @jsii.member(jsii_name="putMalwareProtection")
    def put_malware_protection(
        self,
        *,
        scan_ec2_instance_with_findings: typing.Union[GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param scan_ec2_instance_with_findings: scan_ec2_instance_with_findings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#scan_ec2_instance_with_findings GuarddutyOrganizationConfiguration#scan_ec2_instance_with_findings}
        '''
        value = GuarddutyOrganizationConfigurationDatasourcesMalwareProtection(
            scan_ec2_instance_with_findings=scan_ec2_instance_with_findings
        )

        return typing.cast(None, jsii.invoke(self, "putMalwareProtection", [value]))

    @jsii.member(jsii_name="putS3Logs")
    def put_s3_logs(
        self,
        *,
        auto_enable: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param auto_enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#auto_enable GuarddutyOrganizationConfiguration#auto_enable}.
        '''
        value = GuarddutyOrganizationConfigurationDatasourcesS3Logs(
            auto_enable=auto_enable
        )

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
    def kubernetes(
        self,
    ) -> GuarddutyOrganizationConfigurationDatasourcesKubernetesOutputReference:
        return typing.cast(GuarddutyOrganizationConfigurationDatasourcesKubernetesOutputReference, jsii.get(self, "kubernetes"))

    @builtins.property
    @jsii.member(jsii_name="malwareProtection")
    def malware_protection(
        self,
    ) -> GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionOutputReference:
        return typing.cast(GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionOutputReference, jsii.get(self, "malwareProtection"))

    @builtins.property
    @jsii.member(jsii_name="s3Logs")
    def s3_logs(
        self,
    ) -> "GuarddutyOrganizationConfigurationDatasourcesS3LogsOutputReference":
        return typing.cast("GuarddutyOrganizationConfigurationDatasourcesS3LogsOutputReference", jsii.get(self, "s3Logs"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesInput")
    def kubernetes_input(
        self,
    ) -> typing.Optional[GuarddutyOrganizationConfigurationDatasourcesKubernetes]:
        return typing.cast(typing.Optional[GuarddutyOrganizationConfigurationDatasourcesKubernetes], jsii.get(self, "kubernetesInput"))

    @builtins.property
    @jsii.member(jsii_name="malwareProtectionInput")
    def malware_protection_input(
        self,
    ) -> typing.Optional[GuarddutyOrganizationConfigurationDatasourcesMalwareProtection]:
        return typing.cast(typing.Optional[GuarddutyOrganizationConfigurationDatasourcesMalwareProtection], jsii.get(self, "malwareProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="s3LogsInput")
    def s3_logs_input(
        self,
    ) -> typing.Optional["GuarddutyOrganizationConfigurationDatasourcesS3Logs"]:
        return typing.cast(typing.Optional["GuarddutyOrganizationConfigurationDatasourcesS3Logs"], jsii.get(self, "s3LogsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GuarddutyOrganizationConfigurationDatasources]:
        return typing.cast(typing.Optional[GuarddutyOrganizationConfigurationDatasources], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GuarddutyOrganizationConfigurationDatasources],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GuarddutyOrganizationConfigurationDatasources],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.guarddutyOrganizationConfiguration.GuarddutyOrganizationConfigurationDatasourcesS3Logs",
    jsii_struct_bases=[],
    name_mapping={"auto_enable": "autoEnable"},
)
class GuarddutyOrganizationConfigurationDatasourcesS3Logs:
    def __init__(
        self,
        *,
        auto_enable: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param auto_enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#auto_enable GuarddutyOrganizationConfiguration#auto_enable}.
        '''
        if __debug__:
            def stub(
                *,
                auto_enable: typing.Union[builtins.bool, cdktf.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument auto_enable", value=auto_enable, expected_type=type_hints["auto_enable"])
        self._values: typing.Dict[str, typing.Any] = {
            "auto_enable": auto_enable,
        }

    @builtins.property
    def auto_enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/guardduty_organization_configuration#auto_enable GuarddutyOrganizationConfiguration#auto_enable}.'''
        result = self._values.get("auto_enable")
        assert result is not None, "Required property 'auto_enable' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuarddutyOrganizationConfigurationDatasourcesS3Logs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GuarddutyOrganizationConfigurationDatasourcesS3LogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.guarddutyOrganizationConfiguration.GuarddutyOrganizationConfigurationDatasourcesS3LogsOutputReference",
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
    @jsii.member(jsii_name="autoEnableInput")
    def auto_enable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoEnableInput"))

    @builtins.property
    @jsii.member(jsii_name="autoEnable")
    def auto_enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoEnable"))

    @auto_enable.setter
    def auto_enable(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoEnable", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GuarddutyOrganizationConfigurationDatasourcesS3Logs]:
        return typing.cast(typing.Optional[GuarddutyOrganizationConfigurationDatasourcesS3Logs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GuarddutyOrganizationConfigurationDatasourcesS3Logs],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GuarddutyOrganizationConfigurationDatasourcesS3Logs],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GuarddutyOrganizationConfiguration",
    "GuarddutyOrganizationConfigurationConfig",
    "GuarddutyOrganizationConfigurationDatasources",
    "GuarddutyOrganizationConfigurationDatasourcesKubernetes",
    "GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogs",
    "GuarddutyOrganizationConfigurationDatasourcesKubernetesAuditLogsOutputReference",
    "GuarddutyOrganizationConfigurationDatasourcesKubernetesOutputReference",
    "GuarddutyOrganizationConfigurationDatasourcesMalwareProtection",
    "GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionOutputReference",
    "GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings",
    "GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes",
    "GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesOutputReference",
    "GuarddutyOrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsOutputReference",
    "GuarddutyOrganizationConfigurationDatasourcesOutputReference",
    "GuarddutyOrganizationConfigurationDatasourcesS3Logs",
    "GuarddutyOrganizationConfigurationDatasourcesS3LogsOutputReference",
]

publication.publish()
