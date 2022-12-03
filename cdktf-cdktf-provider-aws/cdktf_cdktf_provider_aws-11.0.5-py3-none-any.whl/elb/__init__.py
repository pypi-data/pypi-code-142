'''
# `aws_elb`

Refer to the Terraform Registory for docs: [`aws_elb`](https://www.terraform.io/docs/providers/aws/r/elb).
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


class Elb(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elb.Elb",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/elb aws_elb}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        listener: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElbListener", typing.Dict[str, typing.Any]]]],
        access_logs: typing.Optional[typing.Union["ElbAccessLogs", typing.Dict[str, typing.Any]]] = None,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection_draining: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection_draining_timeout: typing.Optional[jsii.Number] = None,
        cross_zone_load_balancing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        desync_mitigation_mode: typing.Optional[builtins.str] = None,
        health_check: typing.Optional[typing.Union["ElbHealthCheck", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        idle_timeout: typing.Optional[jsii.Number] = None,
        instances: typing.Optional[typing.Sequence[builtins.str]] = None,
        internal: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_security_group: typing.Optional[builtins.str] = None,
        subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/elb aws_elb} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param listener: listener block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#listener Elb#listener}
        :param access_logs: access_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#access_logs Elb#access_logs}
        :param availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#availability_zones Elb#availability_zones}.
        :param connection_draining: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#connection_draining Elb#connection_draining}.
        :param connection_draining_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#connection_draining_timeout Elb#connection_draining_timeout}.
        :param cross_zone_load_balancing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#cross_zone_load_balancing Elb#cross_zone_load_balancing}.
        :param desync_mitigation_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#desync_mitigation_mode Elb#desync_mitigation_mode}.
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#health_check Elb#health_check}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#id Elb#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idle_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#idle_timeout Elb#idle_timeout}.
        :param instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#instances Elb#instances}.
        :param internal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#internal Elb#internal}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#name Elb#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#name_prefix Elb#name_prefix}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#security_groups Elb#security_groups}.
        :param source_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#source_security_group Elb#source_security_group}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#subnets Elb#subnets}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#tags Elb#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#tags_all Elb#tags_all}.
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
                listener: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElbListener, typing.Dict[str, typing.Any]]]],
                access_logs: typing.Optional[typing.Union[ElbAccessLogs, typing.Dict[str, typing.Any]]] = None,
                availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
                connection_draining: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                connection_draining_timeout: typing.Optional[jsii.Number] = None,
                cross_zone_load_balancing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                desync_mitigation_mode: typing.Optional[builtins.str] = None,
                health_check: typing.Optional[typing.Union[ElbHealthCheck, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                idle_timeout: typing.Optional[jsii.Number] = None,
                instances: typing.Optional[typing.Sequence[builtins.str]] = None,
                internal: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                name: typing.Optional[builtins.str] = None,
                name_prefix: typing.Optional[builtins.str] = None,
                security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
                source_security_group: typing.Optional[builtins.str] = None,
                subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
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
        config = ElbConfig(
            listener=listener,
            access_logs=access_logs,
            availability_zones=availability_zones,
            connection_draining=connection_draining,
            connection_draining_timeout=connection_draining_timeout,
            cross_zone_load_balancing=cross_zone_load_balancing,
            desync_mitigation_mode=desync_mitigation_mode,
            health_check=health_check,
            id=id,
            idle_timeout=idle_timeout,
            instances=instances,
            internal=internal,
            name=name,
            name_prefix=name_prefix,
            security_groups=security_groups,
            source_security_group=source_security_group,
            subnets=subnets,
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

    @jsii.member(jsii_name="putAccessLogs")
    def put_access_logs(
        self,
        *,
        bucket: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#bucket Elb#bucket}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#bucket_prefix Elb#bucket_prefix}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#enabled Elb#enabled}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#interval Elb#interval}.
        '''
        value = ElbAccessLogs(
            bucket=bucket,
            bucket_prefix=bucket_prefix,
            enabled=enabled,
            interval=interval,
        )

        return typing.cast(None, jsii.invoke(self, "putAccessLogs", [value]))

    @jsii.member(jsii_name="putHealthCheck")
    def put_health_check(
        self,
        *,
        healthy_threshold: jsii.Number,
        interval: jsii.Number,
        target: builtins.str,
        timeout: jsii.Number,
        unhealthy_threshold: jsii.Number,
    ) -> None:
        '''
        :param healthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#healthy_threshold Elb#healthy_threshold}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#interval Elb#interval}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#target Elb#target}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#timeout Elb#timeout}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#unhealthy_threshold Elb#unhealthy_threshold}.
        '''
        value = ElbHealthCheck(
            healthy_threshold=healthy_threshold,
            interval=interval,
            target=target,
            timeout=timeout,
            unhealthy_threshold=unhealthy_threshold,
        )

        return typing.cast(None, jsii.invoke(self, "putHealthCheck", [value]))

    @jsii.member(jsii_name="putListener")
    def put_listener(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElbListener", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElbListener, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putListener", [value]))

    @jsii.member(jsii_name="resetAccessLogs")
    def reset_access_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessLogs", []))

    @jsii.member(jsii_name="resetAvailabilityZones")
    def reset_availability_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityZones", []))

    @jsii.member(jsii_name="resetConnectionDraining")
    def reset_connection_draining(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionDraining", []))

    @jsii.member(jsii_name="resetConnectionDrainingTimeout")
    def reset_connection_draining_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionDrainingTimeout", []))

    @jsii.member(jsii_name="resetCrossZoneLoadBalancing")
    def reset_cross_zone_load_balancing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossZoneLoadBalancing", []))

    @jsii.member(jsii_name="resetDesyncMitigationMode")
    def reset_desync_mitigation_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesyncMitigationMode", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdleTimeout")
    def reset_idle_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleTimeout", []))

    @jsii.member(jsii_name="resetInstances")
    def reset_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstances", []))

    @jsii.member(jsii_name="resetInternal")
    def reset_internal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternal", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="resetSecurityGroups")
    def reset_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroups", []))

    @jsii.member(jsii_name="resetSourceSecurityGroup")
    def reset_source_security_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceSecurityGroup", []))

    @jsii.member(jsii_name="resetSubnets")
    def reset_subnets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnets", []))

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
    @jsii.member(jsii_name="accessLogs")
    def access_logs(self) -> "ElbAccessLogsOutputReference":
        return typing.cast("ElbAccessLogsOutputReference", jsii.get(self, "accessLogs"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> "ElbHealthCheckOutputReference":
        return typing.cast("ElbHealthCheckOutputReference", jsii.get(self, "healthCheck"))

    @builtins.property
    @jsii.member(jsii_name="listener")
    def listener(self) -> "ElbListenerList":
        return typing.cast("ElbListenerList", jsii.get(self, "listener"))

    @builtins.property
    @jsii.member(jsii_name="sourceSecurityGroupId")
    def source_security_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceSecurityGroupId"))

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @builtins.property
    @jsii.member(jsii_name="accessLogsInput")
    def access_logs_input(self) -> typing.Optional["ElbAccessLogs"]:
        return typing.cast(typing.Optional["ElbAccessLogs"], jsii.get(self, "accessLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZonesInput")
    def availability_zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "availabilityZonesInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionDrainingInput")
    def connection_draining_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "connectionDrainingInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionDrainingTimeoutInput")
    def connection_draining_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "connectionDrainingTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="crossZoneLoadBalancingInput")
    def cross_zone_load_balancing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "crossZoneLoadBalancingInput"))

    @builtins.property
    @jsii.member(jsii_name="desyncMitigationModeInput")
    def desync_mitigation_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desyncMitigationModeInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(self) -> typing.Optional["ElbHealthCheck"]:
        return typing.cast(typing.Optional["ElbHealthCheck"], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInput")
    def idle_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="instancesInput")
    def instances_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instancesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalInput")
    def internal_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "internalInput"))

    @builtins.property
    @jsii.member(jsii_name="listenerInput")
    def listener_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElbListener"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElbListener"]]], jsii.get(self, "listenerInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceSecurityGroupInput")
    def source_security_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceSecurityGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetsInput")
    def subnets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetsInput"))

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
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "availabilityZones"))

    @availability_zones.setter
    def availability_zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZones", value)

    @builtins.property
    @jsii.member(jsii_name="connectionDraining")
    def connection_draining(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "connectionDraining"))

    @connection_draining.setter
    def connection_draining(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionDraining", value)

    @builtins.property
    @jsii.member(jsii_name="connectionDrainingTimeout")
    def connection_draining_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "connectionDrainingTimeout"))

    @connection_draining_timeout.setter
    def connection_draining_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionDrainingTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="crossZoneLoadBalancing")
    def cross_zone_load_balancing(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "crossZoneLoadBalancing"))

    @cross_zone_load_balancing.setter
    def cross_zone_load_balancing(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossZoneLoadBalancing", value)

    @builtins.property
    @jsii.member(jsii_name="desyncMitigationMode")
    def desync_mitigation_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "desyncMitigationMode"))

    @desync_mitigation_mode.setter
    def desync_mitigation_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desyncMitigationMode", value)

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
    @jsii.member(jsii_name="idleTimeout")
    def idle_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleTimeout"))

    @idle_timeout.setter
    def idle_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="instances")
    def instances(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instances"))

    @instances.setter
    def instances(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instances", value)

    @builtins.property
    @jsii.member(jsii_name="internal")
    def internal(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "internal"))

    @internal.setter
    def internal(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internal", value)

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
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="sourceSecurityGroup")
    def source_security_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceSecurityGroup"))

    @source_security_group.setter
    def source_security_group(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceSecurityGroup", value)

    @builtins.property
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnets", value)

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
    jsii_type="@cdktf/provider-aws.elb.ElbAccessLogs",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "bucket_prefix": "bucketPrefix",
        "enabled": "enabled",
        "interval": "interval",
    },
)
class ElbAccessLogs:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#bucket Elb#bucket}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#bucket_prefix Elb#bucket_prefix}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#enabled Elb#enabled}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#interval Elb#interval}.
        '''
        if __debug__:
            def stub(
                *,
                bucket: builtins.str,
                bucket_prefix: typing.Optional[builtins.str] = None,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                interval: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
        }
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if enabled is not None:
            self._values["enabled"] = enabled
        if interval is not None:
            self._values["interval"] = interval

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#bucket Elb#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#bucket_prefix Elb#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#enabled Elb#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#interval Elb#interval}.'''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElbAccessLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElbAccessLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elb.ElbAccessLogsOutputReference",
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

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElbAccessLogs]:
        return typing.cast(typing.Optional[ElbAccessLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ElbAccessLogs]) -> None:
        if __debug__:
            def stub(value: typing.Optional[ElbAccessLogs]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elb.ElbConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "listener": "listener",
        "access_logs": "accessLogs",
        "availability_zones": "availabilityZones",
        "connection_draining": "connectionDraining",
        "connection_draining_timeout": "connectionDrainingTimeout",
        "cross_zone_load_balancing": "crossZoneLoadBalancing",
        "desync_mitigation_mode": "desyncMitigationMode",
        "health_check": "healthCheck",
        "id": "id",
        "idle_timeout": "idleTimeout",
        "instances": "instances",
        "internal": "internal",
        "name": "name",
        "name_prefix": "namePrefix",
        "security_groups": "securityGroups",
        "source_security_group": "sourceSecurityGroup",
        "subnets": "subnets",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class ElbConfig(cdktf.TerraformMetaArguments):
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
        listener: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElbListener", typing.Dict[str, typing.Any]]]],
        access_logs: typing.Optional[typing.Union[ElbAccessLogs, typing.Dict[str, typing.Any]]] = None,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection_draining: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection_draining_timeout: typing.Optional[jsii.Number] = None,
        cross_zone_load_balancing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        desync_mitigation_mode: typing.Optional[builtins.str] = None,
        health_check: typing.Optional[typing.Union["ElbHealthCheck", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        idle_timeout: typing.Optional[jsii.Number] = None,
        instances: typing.Optional[typing.Sequence[builtins.str]] = None,
        internal: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_security_group: typing.Optional[builtins.str] = None,
        subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
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
        :param listener: listener block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#listener Elb#listener}
        :param access_logs: access_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#access_logs Elb#access_logs}
        :param availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#availability_zones Elb#availability_zones}.
        :param connection_draining: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#connection_draining Elb#connection_draining}.
        :param connection_draining_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#connection_draining_timeout Elb#connection_draining_timeout}.
        :param cross_zone_load_balancing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#cross_zone_load_balancing Elb#cross_zone_load_balancing}.
        :param desync_mitigation_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#desync_mitigation_mode Elb#desync_mitigation_mode}.
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#health_check Elb#health_check}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#id Elb#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idle_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#idle_timeout Elb#idle_timeout}.
        :param instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#instances Elb#instances}.
        :param internal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#internal Elb#internal}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#name Elb#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#name_prefix Elb#name_prefix}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#security_groups Elb#security_groups}.
        :param source_security_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#source_security_group Elb#source_security_group}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#subnets Elb#subnets}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#tags Elb#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#tags_all Elb#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(access_logs, dict):
            access_logs = ElbAccessLogs(**access_logs)
        if isinstance(health_check, dict):
            health_check = ElbHealthCheck(**health_check)
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
                listener: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElbListener, typing.Dict[str, typing.Any]]]],
                access_logs: typing.Optional[typing.Union[ElbAccessLogs, typing.Dict[str, typing.Any]]] = None,
                availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
                connection_draining: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                connection_draining_timeout: typing.Optional[jsii.Number] = None,
                cross_zone_load_balancing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                desync_mitigation_mode: typing.Optional[builtins.str] = None,
                health_check: typing.Optional[typing.Union[ElbHealthCheck, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                idle_timeout: typing.Optional[jsii.Number] = None,
                instances: typing.Optional[typing.Sequence[builtins.str]] = None,
                internal: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                name: typing.Optional[builtins.str] = None,
                name_prefix: typing.Optional[builtins.str] = None,
                security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
                source_security_group: typing.Optional[builtins.str] = None,
                subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
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
            check_type(argname="argument listener", value=listener, expected_type=type_hints["listener"])
            check_type(argname="argument access_logs", value=access_logs, expected_type=type_hints["access_logs"])
            check_type(argname="argument availability_zones", value=availability_zones, expected_type=type_hints["availability_zones"])
            check_type(argname="argument connection_draining", value=connection_draining, expected_type=type_hints["connection_draining"])
            check_type(argname="argument connection_draining_timeout", value=connection_draining_timeout, expected_type=type_hints["connection_draining_timeout"])
            check_type(argname="argument cross_zone_load_balancing", value=cross_zone_load_balancing, expected_type=type_hints["cross_zone_load_balancing"])
            check_type(argname="argument desync_mitigation_mode", value=desync_mitigation_mode, expected_type=type_hints["desync_mitigation_mode"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument idle_timeout", value=idle_timeout, expected_type=type_hints["idle_timeout"])
            check_type(argname="argument instances", value=instances, expected_type=type_hints["instances"])
            check_type(argname="argument internal", value=internal, expected_type=type_hints["internal"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument source_security_group", value=source_security_group, expected_type=type_hints["source_security_group"])
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "listener": listener,
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
        if access_logs is not None:
            self._values["access_logs"] = access_logs
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if connection_draining is not None:
            self._values["connection_draining"] = connection_draining
        if connection_draining_timeout is not None:
            self._values["connection_draining_timeout"] = connection_draining_timeout
        if cross_zone_load_balancing is not None:
            self._values["cross_zone_load_balancing"] = cross_zone_load_balancing
        if desync_mitigation_mode is not None:
            self._values["desync_mitigation_mode"] = desync_mitigation_mode
        if health_check is not None:
            self._values["health_check"] = health_check
        if id is not None:
            self._values["id"] = id
        if idle_timeout is not None:
            self._values["idle_timeout"] = idle_timeout
        if instances is not None:
            self._values["instances"] = instances
        if internal is not None:
            self._values["internal"] = internal
        if name is not None:
            self._values["name"] = name
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if source_security_group is not None:
            self._values["source_security_group"] = source_security_group
        if subnets is not None:
            self._values["subnets"] = subnets
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
    def listener(self) -> typing.Union[cdktf.IResolvable, typing.List["ElbListener"]]:
        '''listener block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#listener Elb#listener}
        '''
        result = self._values.get("listener")
        assert result is not None, "Required property 'listener' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ElbListener"]], result)

    @builtins.property
    def access_logs(self) -> typing.Optional[ElbAccessLogs]:
        '''access_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#access_logs Elb#access_logs}
        '''
        result = self._values.get("access_logs")
        return typing.cast(typing.Optional[ElbAccessLogs], result)

    @builtins.property
    def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#availability_zones Elb#availability_zones}.'''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def connection_draining(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#connection_draining Elb#connection_draining}.'''
        result = self._values.get("connection_draining")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def connection_draining_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#connection_draining_timeout Elb#connection_draining_timeout}.'''
        result = self._values.get("connection_draining_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cross_zone_load_balancing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#cross_zone_load_balancing Elb#cross_zone_load_balancing}.'''
        result = self._values.get("cross_zone_load_balancing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def desync_mitigation_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#desync_mitigation_mode Elb#desync_mitigation_mode}.'''
        result = self._values.get("desync_mitigation_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check(self) -> typing.Optional["ElbHealthCheck"]:
        '''health_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#health_check Elb#health_check}
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional["ElbHealthCheck"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#id Elb#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idle_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#idle_timeout Elb#idle_timeout}.'''
        result = self._values.get("idle_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instances(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#instances Elb#instances}.'''
        result = self._values.get("instances")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def internal(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#internal Elb#internal}.'''
        result = self._values.get("internal")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#name Elb#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#name_prefix Elb#name_prefix}.'''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#security_groups Elb#security_groups}.'''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_security_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#source_security_group Elb#source_security_group}.'''
        result = self._values.get("source_security_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#subnets Elb#subnets}.'''
        result = self._values.get("subnets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#tags Elb#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#tags_all Elb#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElbConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elb.ElbHealthCheck",
    jsii_struct_bases=[],
    name_mapping={
        "healthy_threshold": "healthyThreshold",
        "interval": "interval",
        "target": "target",
        "timeout": "timeout",
        "unhealthy_threshold": "unhealthyThreshold",
    },
)
class ElbHealthCheck:
    def __init__(
        self,
        *,
        healthy_threshold: jsii.Number,
        interval: jsii.Number,
        target: builtins.str,
        timeout: jsii.Number,
        unhealthy_threshold: jsii.Number,
    ) -> None:
        '''
        :param healthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#healthy_threshold Elb#healthy_threshold}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#interval Elb#interval}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#target Elb#target}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#timeout Elb#timeout}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#unhealthy_threshold Elb#unhealthy_threshold}.
        '''
        if __debug__:
            def stub(
                *,
                healthy_threshold: jsii.Number,
                interval: jsii.Number,
                target: builtins.str,
                timeout: jsii.Number,
                unhealthy_threshold: jsii.Number,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument healthy_threshold", value=healthy_threshold, expected_type=type_hints["healthy_threshold"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument unhealthy_threshold", value=unhealthy_threshold, expected_type=type_hints["unhealthy_threshold"])
        self._values: typing.Dict[str, typing.Any] = {
            "healthy_threshold": healthy_threshold,
            "interval": interval,
            "target": target,
            "timeout": timeout,
            "unhealthy_threshold": unhealthy_threshold,
        }

    @builtins.property
    def healthy_threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#healthy_threshold Elb#healthy_threshold}.'''
        result = self._values.get("healthy_threshold")
        assert result is not None, "Required property 'healthy_threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#interval Elb#interval}.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#target Elb#target}.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#timeout Elb#timeout}.'''
        result = self._values.get("timeout")
        assert result is not None, "Required property 'timeout' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def unhealthy_threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#unhealthy_threshold Elb#unhealthy_threshold}.'''
        result = self._values.get("unhealthy_threshold")
        assert result is not None, "Required property 'unhealthy_threshold' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElbHealthCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElbHealthCheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elb.ElbHealthCheckOutputReference",
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
    @jsii.member(jsii_name="healthyThresholdInput")
    def healthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="unhealthyThresholdInput")
    def unhealthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "unhealthyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="healthyThreshold")
    def healthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthyThreshold"))

    @healthy_threshold.setter
    def healthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthyThreshold", value)

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
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="unhealthyThreshold")
    def unhealthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unhealthyThreshold"))

    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unhealthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElbHealthCheck]:
        return typing.cast(typing.Optional[ElbHealthCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ElbHealthCheck]) -> None:
        if __debug__:
            def stub(value: typing.Optional[ElbHealthCheck]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elb.ElbListener",
    jsii_struct_bases=[],
    name_mapping={
        "instance_port": "instancePort",
        "instance_protocol": "instanceProtocol",
        "lb_port": "lbPort",
        "lb_protocol": "lbProtocol",
        "ssl_certificate_id": "sslCertificateId",
    },
)
class ElbListener:
    def __init__(
        self,
        *,
        instance_port: jsii.Number,
        instance_protocol: builtins.str,
        lb_port: jsii.Number,
        lb_protocol: builtins.str,
        ssl_certificate_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#instance_port Elb#instance_port}.
        :param instance_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#instance_protocol Elb#instance_protocol}.
        :param lb_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#lb_port Elb#lb_port}.
        :param lb_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#lb_protocol Elb#lb_protocol}.
        :param ssl_certificate_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#ssl_certificate_id Elb#ssl_certificate_id}.
        '''
        if __debug__:
            def stub(
                *,
                instance_port: jsii.Number,
                instance_protocol: builtins.str,
                lb_port: jsii.Number,
                lb_protocol: builtins.str,
                ssl_certificate_id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_port", value=instance_port, expected_type=type_hints["instance_port"])
            check_type(argname="argument instance_protocol", value=instance_protocol, expected_type=type_hints["instance_protocol"])
            check_type(argname="argument lb_port", value=lb_port, expected_type=type_hints["lb_port"])
            check_type(argname="argument lb_protocol", value=lb_protocol, expected_type=type_hints["lb_protocol"])
            check_type(argname="argument ssl_certificate_id", value=ssl_certificate_id, expected_type=type_hints["ssl_certificate_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_port": instance_port,
            "instance_protocol": instance_protocol,
            "lb_port": lb_port,
            "lb_protocol": lb_protocol,
        }
        if ssl_certificate_id is not None:
            self._values["ssl_certificate_id"] = ssl_certificate_id

    @builtins.property
    def instance_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#instance_port Elb#instance_port}.'''
        result = self._values.get("instance_port")
        assert result is not None, "Required property 'instance_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def instance_protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#instance_protocol Elb#instance_protocol}.'''
        result = self._values.get("instance_protocol")
        assert result is not None, "Required property 'instance_protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lb_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#lb_port Elb#lb_port}.'''
        result = self._values.get("lb_port")
        assert result is not None, "Required property 'lb_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def lb_protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#lb_protocol Elb#lb_protocol}.'''
        result = self._values.get("lb_protocol")
        assert result is not None, "Required property 'lb_protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ssl_certificate_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elb#ssl_certificate_id Elb#ssl_certificate_id}.'''
        result = self._values.get("ssl_certificate_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElbListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElbListenerList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elb.ElbListenerList",
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
    def get(self, index: jsii.Number) -> "ElbListenerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElbListenerOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElbListener]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElbListener]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElbListener]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElbListener]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElbListenerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elb.ElbListenerOutputReference",
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

    @jsii.member(jsii_name="resetSslCertificateId")
    def reset_ssl_certificate_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslCertificateId", []))

    @builtins.property
    @jsii.member(jsii_name="instancePortInput")
    def instance_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instancePortInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceProtocolInput")
    def instance_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="lbPortInput")
    def lb_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lbPortInput"))

    @builtins.property
    @jsii.member(jsii_name="lbProtocolInput")
    def lb_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lbProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="sslCertificateIdInput")
    def ssl_certificate_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslCertificateIdInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePort")
    def instance_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instancePort"))

    @instance_port.setter
    def instance_port(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instancePort", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProtocol")
    def instance_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceProtocol"))

    @instance_protocol.setter
    def instance_protocol(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="lbPort")
    def lb_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lbPort"))

    @lb_port.setter
    def lb_port(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lbPort", value)

    @builtins.property
    @jsii.member(jsii_name="lbProtocol")
    def lb_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lbProtocol"))

    @lb_protocol.setter
    def lb_protocol(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lbProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="sslCertificateId")
    def ssl_certificate_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslCertificateId"))

    @ssl_certificate_id.setter
    def ssl_certificate_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslCertificateId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElbListener, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElbListener, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElbListener, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[ElbListener, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Elb",
    "ElbAccessLogs",
    "ElbAccessLogsOutputReference",
    "ElbConfig",
    "ElbHealthCheck",
    "ElbHealthCheckOutputReference",
    "ElbListener",
    "ElbListenerList",
    "ElbListenerOutputReference",
]

publication.publish()
