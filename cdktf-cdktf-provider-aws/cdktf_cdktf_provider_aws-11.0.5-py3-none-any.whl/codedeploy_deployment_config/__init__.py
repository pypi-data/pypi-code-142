'''
# `aws_codedeploy_deployment_config`

Refer to the Terraform Registory for docs: [`aws_codedeploy_deployment_config`](https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config).
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


class CodedeployDeploymentConfig(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentConfig.CodedeployDeploymentConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config aws_codedeploy_deployment_config}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        deployment_config_name: builtins.str,
        compute_platform: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        minimum_healthy_hosts: typing.Optional[typing.Union["CodedeployDeploymentConfigMinimumHealthyHosts", typing.Dict[str, typing.Any]]] = None,
        traffic_routing_config: typing.Optional[typing.Union["CodedeployDeploymentConfigTrafficRoutingConfig", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config aws_codedeploy_deployment_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param deployment_config_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#deployment_config_name CodedeployDeploymentConfig#deployment_config_name}.
        :param compute_platform: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#compute_platform CodedeployDeploymentConfig#compute_platform}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#id CodedeployDeploymentConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param minimum_healthy_hosts: minimum_healthy_hosts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#minimum_healthy_hosts CodedeployDeploymentConfig#minimum_healthy_hosts}
        :param traffic_routing_config: traffic_routing_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#traffic_routing_config CodedeployDeploymentConfig#traffic_routing_config}
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
                deployment_config_name: builtins.str,
                compute_platform: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                minimum_healthy_hosts: typing.Optional[typing.Union[CodedeployDeploymentConfigMinimumHealthyHosts, typing.Dict[str, typing.Any]]] = None,
                traffic_routing_config: typing.Optional[typing.Union[CodedeployDeploymentConfigTrafficRoutingConfig, typing.Dict[str, typing.Any]]] = None,
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
        config = CodedeployDeploymentConfigConfig(
            deployment_config_name=deployment_config_name,
            compute_platform=compute_platform,
            id=id,
            minimum_healthy_hosts=minimum_healthy_hosts,
            traffic_routing_config=traffic_routing_config,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putMinimumHealthyHosts")
    def put_minimum_healthy_hosts(
        self,
        *,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#type CodedeployDeploymentConfig#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#value CodedeployDeploymentConfig#value}.
        '''
        value_ = CodedeployDeploymentConfigMinimumHealthyHosts(type=type, value=value)

        return typing.cast(None, jsii.invoke(self, "putMinimumHealthyHosts", [value_]))

    @jsii.member(jsii_name="putTrafficRoutingConfig")
    def put_traffic_routing_config(
        self,
        *,
        time_based_canary: typing.Optional[typing.Union["CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanary", typing.Dict[str, typing.Any]]] = None,
        time_based_linear: typing.Optional[typing.Union["CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinear", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param time_based_canary: time_based_canary block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#time_based_canary CodedeployDeploymentConfig#time_based_canary}
        :param time_based_linear: time_based_linear block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#time_based_linear CodedeployDeploymentConfig#time_based_linear}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#type CodedeployDeploymentConfig#type}.
        '''
        value = CodedeployDeploymentConfigTrafficRoutingConfig(
            time_based_canary=time_based_canary,
            time_based_linear=time_based_linear,
            type=type,
        )

        return typing.cast(None, jsii.invoke(self, "putTrafficRoutingConfig", [value]))

    @jsii.member(jsii_name="resetComputePlatform")
    def reset_compute_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComputePlatform", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMinimumHealthyHosts")
    def reset_minimum_healthy_hosts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumHealthyHosts", []))

    @jsii.member(jsii_name="resetTrafficRoutingConfig")
    def reset_traffic_routing_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrafficRoutingConfig", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigId")
    def deployment_config_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentConfigId"))

    @builtins.property
    @jsii.member(jsii_name="minimumHealthyHosts")
    def minimum_healthy_hosts(
        self,
    ) -> "CodedeployDeploymentConfigMinimumHealthyHostsOutputReference":
        return typing.cast("CodedeployDeploymentConfigMinimumHealthyHostsOutputReference", jsii.get(self, "minimumHealthyHosts"))

    @builtins.property
    @jsii.member(jsii_name="trafficRoutingConfig")
    def traffic_routing_config(
        self,
    ) -> "CodedeployDeploymentConfigTrafficRoutingConfigOutputReference":
        return typing.cast("CodedeployDeploymentConfigTrafficRoutingConfigOutputReference", jsii.get(self, "trafficRoutingConfig"))

    @builtins.property
    @jsii.member(jsii_name="computePlatformInput")
    def compute_platform_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computePlatformInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigNameInput")
    def deployment_config_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentConfigNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumHealthyHostsInput")
    def minimum_healthy_hosts_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentConfigMinimumHealthyHosts"]:
        return typing.cast(typing.Optional["CodedeployDeploymentConfigMinimumHealthyHosts"], jsii.get(self, "minimumHealthyHostsInput"))

    @builtins.property
    @jsii.member(jsii_name="trafficRoutingConfigInput")
    def traffic_routing_config_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentConfigTrafficRoutingConfig"]:
        return typing.cast(typing.Optional["CodedeployDeploymentConfigTrafficRoutingConfig"], jsii.get(self, "trafficRoutingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="computePlatform")
    def compute_platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "computePlatform"))

    @compute_platform.setter
    def compute_platform(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computePlatform", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentConfigName"))

    @deployment_config_name.setter
    def deployment_config_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentConfigName", value)

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
    jsii_type="@cdktf/provider-aws.codedeployDeploymentConfig.CodedeployDeploymentConfigConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "deployment_config_name": "deploymentConfigName",
        "compute_platform": "computePlatform",
        "id": "id",
        "minimum_healthy_hosts": "minimumHealthyHosts",
        "traffic_routing_config": "trafficRoutingConfig",
    },
)
class CodedeployDeploymentConfigConfig(cdktf.TerraformMetaArguments):
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
        deployment_config_name: builtins.str,
        compute_platform: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        minimum_healthy_hosts: typing.Optional[typing.Union["CodedeployDeploymentConfigMinimumHealthyHosts", typing.Dict[str, typing.Any]]] = None,
        traffic_routing_config: typing.Optional[typing.Union["CodedeployDeploymentConfigTrafficRoutingConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param deployment_config_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#deployment_config_name CodedeployDeploymentConfig#deployment_config_name}.
        :param compute_platform: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#compute_platform CodedeployDeploymentConfig#compute_platform}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#id CodedeployDeploymentConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param minimum_healthy_hosts: minimum_healthy_hosts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#minimum_healthy_hosts CodedeployDeploymentConfig#minimum_healthy_hosts}
        :param traffic_routing_config: traffic_routing_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#traffic_routing_config CodedeployDeploymentConfig#traffic_routing_config}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(minimum_healthy_hosts, dict):
            minimum_healthy_hosts = CodedeployDeploymentConfigMinimumHealthyHosts(**minimum_healthy_hosts)
        if isinstance(traffic_routing_config, dict):
            traffic_routing_config = CodedeployDeploymentConfigTrafficRoutingConfig(**traffic_routing_config)
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
                deployment_config_name: builtins.str,
                compute_platform: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                minimum_healthy_hosts: typing.Optional[typing.Union[CodedeployDeploymentConfigMinimumHealthyHosts, typing.Dict[str, typing.Any]]] = None,
                traffic_routing_config: typing.Optional[typing.Union[CodedeployDeploymentConfigTrafficRoutingConfig, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument deployment_config_name", value=deployment_config_name, expected_type=type_hints["deployment_config_name"])
            check_type(argname="argument compute_platform", value=compute_platform, expected_type=type_hints["compute_platform"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument minimum_healthy_hosts", value=minimum_healthy_hosts, expected_type=type_hints["minimum_healthy_hosts"])
            check_type(argname="argument traffic_routing_config", value=traffic_routing_config, expected_type=type_hints["traffic_routing_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "deployment_config_name": deployment_config_name,
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
        if compute_platform is not None:
            self._values["compute_platform"] = compute_platform
        if id is not None:
            self._values["id"] = id
        if minimum_healthy_hosts is not None:
            self._values["minimum_healthy_hosts"] = minimum_healthy_hosts
        if traffic_routing_config is not None:
            self._values["traffic_routing_config"] = traffic_routing_config

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
    def deployment_config_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#deployment_config_name CodedeployDeploymentConfig#deployment_config_name}.'''
        result = self._values.get("deployment_config_name")
        assert result is not None, "Required property 'deployment_config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def compute_platform(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#compute_platform CodedeployDeploymentConfig#compute_platform}.'''
        result = self._values.get("compute_platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#id CodedeployDeploymentConfig#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_healthy_hosts(
        self,
    ) -> typing.Optional["CodedeployDeploymentConfigMinimumHealthyHosts"]:
        '''minimum_healthy_hosts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#minimum_healthy_hosts CodedeployDeploymentConfig#minimum_healthy_hosts}
        '''
        result = self._values.get("minimum_healthy_hosts")
        return typing.cast(typing.Optional["CodedeployDeploymentConfigMinimumHealthyHosts"], result)

    @builtins.property
    def traffic_routing_config(
        self,
    ) -> typing.Optional["CodedeployDeploymentConfigTrafficRoutingConfig"]:
        '''traffic_routing_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#traffic_routing_config CodedeployDeploymentConfig#traffic_routing_config}
        '''
        result = self._values.get("traffic_routing_config")
        return typing.cast(typing.Optional["CodedeployDeploymentConfigTrafficRoutingConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentConfig.CodedeployDeploymentConfigMinimumHealthyHosts",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "value": "value"},
)
class CodedeployDeploymentConfigMinimumHealthyHosts:
    def __init__(
        self,
        *,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#type CodedeployDeploymentConfig#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#value CodedeployDeploymentConfig#value}.
        '''
        if __debug__:
            def stub(
                *,
                type: typing.Optional[builtins.str] = None,
                value: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#type CodedeployDeploymentConfig#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#value CodedeployDeploymentConfig#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentConfigMinimumHealthyHosts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentConfigMinimumHealthyHostsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentConfig.CodedeployDeploymentConfigMinimumHealthyHostsOutputReference",
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

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

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
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentConfigMinimumHealthyHosts]:
        return typing.cast(typing.Optional[CodedeployDeploymentConfigMinimumHealthyHosts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentConfigMinimumHealthyHosts],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodedeployDeploymentConfigMinimumHealthyHosts],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentConfig.CodedeployDeploymentConfigTrafficRoutingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "time_based_canary": "timeBasedCanary",
        "time_based_linear": "timeBasedLinear",
        "type": "type",
    },
)
class CodedeployDeploymentConfigTrafficRoutingConfig:
    def __init__(
        self,
        *,
        time_based_canary: typing.Optional[typing.Union["CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanary", typing.Dict[str, typing.Any]]] = None,
        time_based_linear: typing.Optional[typing.Union["CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinear", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param time_based_canary: time_based_canary block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#time_based_canary CodedeployDeploymentConfig#time_based_canary}
        :param time_based_linear: time_based_linear block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#time_based_linear CodedeployDeploymentConfig#time_based_linear}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#type CodedeployDeploymentConfig#type}.
        '''
        if isinstance(time_based_canary, dict):
            time_based_canary = CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanary(**time_based_canary)
        if isinstance(time_based_linear, dict):
            time_based_linear = CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinear(**time_based_linear)
        if __debug__:
            def stub(
                *,
                time_based_canary: typing.Optional[typing.Union[CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanary, typing.Dict[str, typing.Any]]] = None,
                time_based_linear: typing.Optional[typing.Union[CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinear, typing.Dict[str, typing.Any]]] = None,
                type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument time_based_canary", value=time_based_canary, expected_type=type_hints["time_based_canary"])
            check_type(argname="argument time_based_linear", value=time_based_linear, expected_type=type_hints["time_based_linear"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if time_based_canary is not None:
            self._values["time_based_canary"] = time_based_canary
        if time_based_linear is not None:
            self._values["time_based_linear"] = time_based_linear
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def time_based_canary(
        self,
    ) -> typing.Optional["CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanary"]:
        '''time_based_canary block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#time_based_canary CodedeployDeploymentConfig#time_based_canary}
        '''
        result = self._values.get("time_based_canary")
        return typing.cast(typing.Optional["CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanary"], result)

    @builtins.property
    def time_based_linear(
        self,
    ) -> typing.Optional["CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinear"]:
        '''time_based_linear block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#time_based_linear CodedeployDeploymentConfig#time_based_linear}
        '''
        result = self._values.get("time_based_linear")
        return typing.cast(typing.Optional["CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinear"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#type CodedeployDeploymentConfig#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentConfigTrafficRoutingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentConfigTrafficRoutingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentConfig.CodedeployDeploymentConfigTrafficRoutingConfigOutputReference",
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

    @jsii.member(jsii_name="putTimeBasedCanary")
    def put_time_based_canary(
        self,
        *,
        interval: typing.Optional[jsii.Number] = None,
        percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#interval CodedeployDeploymentConfig#interval}.
        :param percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#percentage CodedeployDeploymentConfig#percentage}.
        '''
        value = CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanary(
            interval=interval, percentage=percentage
        )

        return typing.cast(None, jsii.invoke(self, "putTimeBasedCanary", [value]))

    @jsii.member(jsii_name="putTimeBasedLinear")
    def put_time_based_linear(
        self,
        *,
        interval: typing.Optional[jsii.Number] = None,
        percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#interval CodedeployDeploymentConfig#interval}.
        :param percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#percentage CodedeployDeploymentConfig#percentage}.
        '''
        value = CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinear(
            interval=interval, percentage=percentage
        )

        return typing.cast(None, jsii.invoke(self, "putTimeBasedLinear", [value]))

    @jsii.member(jsii_name="resetTimeBasedCanary")
    def reset_time_based_canary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeBasedCanary", []))

    @jsii.member(jsii_name="resetTimeBasedLinear")
    def reset_time_based_linear(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeBasedLinear", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="timeBasedCanary")
    def time_based_canary(
        self,
    ) -> "CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanaryOutputReference":
        return typing.cast("CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanaryOutputReference", jsii.get(self, "timeBasedCanary"))

    @builtins.property
    @jsii.member(jsii_name="timeBasedLinear")
    def time_based_linear(
        self,
    ) -> "CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinearOutputReference":
        return typing.cast("CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinearOutputReference", jsii.get(self, "timeBasedLinear"))

    @builtins.property
    @jsii.member(jsii_name="timeBasedCanaryInput")
    def time_based_canary_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanary"]:
        return typing.cast(typing.Optional["CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanary"], jsii.get(self, "timeBasedCanaryInput"))

    @builtins.property
    @jsii.member(jsii_name="timeBasedLinearInput")
    def time_based_linear_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinear"]:
        return typing.cast(typing.Optional["CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinear"], jsii.get(self, "timeBasedLinearInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

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
    ) -> typing.Optional[CodedeployDeploymentConfigTrafficRoutingConfig]:
        return typing.cast(typing.Optional[CodedeployDeploymentConfigTrafficRoutingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentConfigTrafficRoutingConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodedeployDeploymentConfigTrafficRoutingConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentConfig.CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanary",
    jsii_struct_bases=[],
    name_mapping={"interval": "interval", "percentage": "percentage"},
)
class CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanary:
    def __init__(
        self,
        *,
        interval: typing.Optional[jsii.Number] = None,
        percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#interval CodedeployDeploymentConfig#interval}.
        :param percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#percentage CodedeployDeploymentConfig#percentage}.
        '''
        if __debug__:
            def stub(
                *,
                interval: typing.Optional[jsii.Number] = None,
                percentage: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
        self._values: typing.Dict[str, typing.Any] = {}
        if interval is not None:
            self._values["interval"] = interval
        if percentage is not None:
            self._values["percentage"] = percentage

    @builtins.property
    def interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#interval CodedeployDeploymentConfig#interval}.'''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#percentage CodedeployDeploymentConfig#percentage}.'''
        result = self._values.get("percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanaryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentConfig.CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanaryOutputReference",
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

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetPercentage")
    def reset_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="percentageInput")
    def percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentageInput"))

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="percentage")
    def percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percentage"))

    @percentage.setter
    def percentage(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanary]:
        return typing.cast(typing.Optional[CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanary], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanary],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanary],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentConfig.CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinear",
    jsii_struct_bases=[],
    name_mapping={"interval": "interval", "percentage": "percentage"},
)
class CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinear:
    def __init__(
        self,
        *,
        interval: typing.Optional[jsii.Number] = None,
        percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#interval CodedeployDeploymentConfig#interval}.
        :param percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#percentage CodedeployDeploymentConfig#percentage}.
        '''
        if __debug__:
            def stub(
                *,
                interval: typing.Optional[jsii.Number] = None,
                percentage: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
        self._values: typing.Dict[str, typing.Any] = {}
        if interval is not None:
            self._values["interval"] = interval
        if percentage is not None:
            self._values["percentage"] = percentage

    @builtins.property
    def interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#interval CodedeployDeploymentConfig#interval}.'''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_config#percentage CodedeployDeploymentConfig#percentage}.'''
        result = self._values.get("percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinear(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinearOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentConfig.CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinearOutputReference",
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

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetPercentage")
    def reset_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="percentageInput")
    def percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "percentageInput"))

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="percentage")
    def percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "percentage"))

    @percentage.setter
    def percentage(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "percentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinear]:
        return typing.cast(typing.Optional[CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinear], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinear],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinear],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CodedeployDeploymentConfig",
    "CodedeployDeploymentConfigConfig",
    "CodedeployDeploymentConfigMinimumHealthyHosts",
    "CodedeployDeploymentConfigMinimumHealthyHostsOutputReference",
    "CodedeployDeploymentConfigTrafficRoutingConfig",
    "CodedeployDeploymentConfigTrafficRoutingConfigOutputReference",
    "CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanary",
    "CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedCanaryOutputReference",
    "CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinear",
    "CodedeployDeploymentConfigTrafficRoutingConfigTimeBasedLinearOutputReference",
]

publication.publish()
