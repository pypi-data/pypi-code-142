'''
# `aws_ecs_service`

Refer to the Terraform Registory for docs: [`aws_ecs_service`](https://www.terraform.io/docs/providers/aws/r/ecs_service).
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


class EcsService(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsService",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ecs_service aws_ecs_service}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        capacity_provider_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceCapacityProviderStrategy", typing.Dict[str, typing.Any]]]]] = None,
        cluster: typing.Optional[builtins.str] = None,
        deployment_circuit_breaker: typing.Optional[typing.Union["EcsServiceDeploymentCircuitBreaker", typing.Dict[str, typing.Any]]] = None,
        deployment_controller: typing.Optional[typing.Union["EcsServiceDeploymentController", typing.Dict[str, typing.Any]]] = None,
        deployment_maximum_percent: typing.Optional[jsii.Number] = None,
        deployment_minimum_healthy_percent: typing.Optional[jsii.Number] = None,
        desired_count: typing.Optional[jsii.Number] = None,
        enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_execute_command: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        force_new_deployment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_check_grace_period_seconds: typing.Optional[jsii.Number] = None,
        iam_role: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        launch_type: typing.Optional[builtins.str] = None,
        load_balancer: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceLoadBalancer", typing.Dict[str, typing.Any]]]]] = None,
        network_configuration: typing.Optional[typing.Union["EcsServiceNetworkConfiguration", typing.Dict[str, typing.Any]]] = None,
        ordered_placement_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceOrderedPlacementStrategy", typing.Dict[str, typing.Any]]]]] = None,
        placement_constraints: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServicePlacementConstraints", typing.Dict[str, typing.Any]]]]] = None,
        platform_version: typing.Optional[builtins.str] = None,
        propagate_tags: typing.Optional[builtins.str] = None,
        scheduling_strategy: typing.Optional[builtins.str] = None,
        service_connect_configuration: typing.Optional[typing.Union["EcsServiceServiceConnectConfiguration", typing.Dict[str, typing.Any]]] = None,
        service_registries: typing.Optional[typing.Union["EcsServiceServiceRegistries", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        task_definition: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["EcsServiceTimeouts", typing.Dict[str, typing.Any]]] = None,
        triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        wait_for_steady_state: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ecs_service aws_ecs_service} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#name EcsService#name}.
        :param capacity_provider_strategy: capacity_provider_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#capacity_provider_strategy EcsService#capacity_provider_strategy}
        :param cluster: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#cluster EcsService#cluster}.
        :param deployment_circuit_breaker: deployment_circuit_breaker block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_circuit_breaker EcsService#deployment_circuit_breaker}
        :param deployment_controller: deployment_controller block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_controller EcsService#deployment_controller}
        :param deployment_maximum_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_maximum_percent EcsService#deployment_maximum_percent}.
        :param deployment_minimum_healthy_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_minimum_healthy_percent EcsService#deployment_minimum_healthy_percent}.
        :param desired_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#desired_count EcsService#desired_count}.
        :param enable_ecs_managed_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enable_ecs_managed_tags EcsService#enable_ecs_managed_tags}.
        :param enable_execute_command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enable_execute_command EcsService#enable_execute_command}.
        :param force_new_deployment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#force_new_deployment EcsService#force_new_deployment}.
        :param health_check_grace_period_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#health_check_grace_period_seconds EcsService#health_check_grace_period_seconds}.
        :param iam_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#iam_role EcsService#iam_role}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#id EcsService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param launch_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#launch_type EcsService#launch_type}.
        :param load_balancer: load_balancer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#load_balancer EcsService#load_balancer}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#network_configuration EcsService#network_configuration}
        :param ordered_placement_strategy: ordered_placement_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#ordered_placement_strategy EcsService#ordered_placement_strategy}
        :param placement_constraints: placement_constraints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#placement_constraints EcsService#placement_constraints}
        :param platform_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#platform_version EcsService#platform_version}.
        :param propagate_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#propagate_tags EcsService#propagate_tags}.
        :param scheduling_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#scheduling_strategy EcsService#scheduling_strategy}.
        :param service_connect_configuration: service_connect_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#service_connect_configuration EcsService#service_connect_configuration}
        :param service_registries: service_registries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#service_registries EcsService#service_registries}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#tags EcsService#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#tags_all EcsService#tags_all}.
        :param task_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#task_definition EcsService#task_definition}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#timeouts EcsService#timeouts}
        :param triggers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#triggers EcsService#triggers}.
        :param wait_for_steady_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#wait_for_steady_state EcsService#wait_for_steady_state}.
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
                name: builtins.str,
                capacity_provider_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServiceCapacityProviderStrategy, typing.Dict[str, typing.Any]]]]] = None,
                cluster: typing.Optional[builtins.str] = None,
                deployment_circuit_breaker: typing.Optional[typing.Union[EcsServiceDeploymentCircuitBreaker, typing.Dict[str, typing.Any]]] = None,
                deployment_controller: typing.Optional[typing.Union[EcsServiceDeploymentController, typing.Dict[str, typing.Any]]] = None,
                deployment_maximum_percent: typing.Optional[jsii.Number] = None,
                deployment_minimum_healthy_percent: typing.Optional[jsii.Number] = None,
                desired_count: typing.Optional[jsii.Number] = None,
                enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                enable_execute_command: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                force_new_deployment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                health_check_grace_period_seconds: typing.Optional[jsii.Number] = None,
                iam_role: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                launch_type: typing.Optional[builtins.str] = None,
                load_balancer: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServiceLoadBalancer, typing.Dict[str, typing.Any]]]]] = None,
                network_configuration: typing.Optional[typing.Union[EcsServiceNetworkConfiguration, typing.Dict[str, typing.Any]]] = None,
                ordered_placement_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServiceOrderedPlacementStrategy, typing.Dict[str, typing.Any]]]]] = None,
                placement_constraints: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServicePlacementConstraints, typing.Dict[str, typing.Any]]]]] = None,
                platform_version: typing.Optional[builtins.str] = None,
                propagate_tags: typing.Optional[builtins.str] = None,
                scheduling_strategy: typing.Optional[builtins.str] = None,
                service_connect_configuration: typing.Optional[typing.Union[EcsServiceServiceConnectConfiguration, typing.Dict[str, typing.Any]]] = None,
                service_registries: typing.Optional[typing.Union[EcsServiceServiceRegistries, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                task_definition: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[EcsServiceTimeouts, typing.Dict[str, typing.Any]]] = None,
                triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                wait_for_steady_state: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
        config = EcsServiceConfig(
            name=name,
            capacity_provider_strategy=capacity_provider_strategy,
            cluster=cluster,
            deployment_circuit_breaker=deployment_circuit_breaker,
            deployment_controller=deployment_controller,
            deployment_maximum_percent=deployment_maximum_percent,
            deployment_minimum_healthy_percent=deployment_minimum_healthy_percent,
            desired_count=desired_count,
            enable_ecs_managed_tags=enable_ecs_managed_tags,
            enable_execute_command=enable_execute_command,
            force_new_deployment=force_new_deployment,
            health_check_grace_period_seconds=health_check_grace_period_seconds,
            iam_role=iam_role,
            id=id,
            launch_type=launch_type,
            load_balancer=load_balancer,
            network_configuration=network_configuration,
            ordered_placement_strategy=ordered_placement_strategy,
            placement_constraints=placement_constraints,
            platform_version=platform_version,
            propagate_tags=propagate_tags,
            scheduling_strategy=scheduling_strategy,
            service_connect_configuration=service_connect_configuration,
            service_registries=service_registries,
            tags=tags,
            tags_all=tags_all,
            task_definition=task_definition,
            timeouts=timeouts,
            triggers=triggers,
            wait_for_steady_state=wait_for_steady_state,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCapacityProviderStrategy")
    def put_capacity_provider_strategy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceCapacityProviderStrategy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServiceCapacityProviderStrategy, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCapacityProviderStrategy", [value]))

    @jsii.member(jsii_name="putDeploymentCircuitBreaker")
    def put_deployment_circuit_breaker(
        self,
        *,
        enable: typing.Union[builtins.bool, cdktf.IResolvable],
        rollback: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enable EcsService#enable}.
        :param rollback: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#rollback EcsService#rollback}.
        '''
        value = EcsServiceDeploymentCircuitBreaker(enable=enable, rollback=rollback)

        return typing.cast(None, jsii.invoke(self, "putDeploymentCircuitBreaker", [value]))

    @jsii.member(jsii_name="putDeploymentController")
    def put_deployment_controller(
        self,
        *,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#type EcsService#type}.
        '''
        value = EcsServiceDeploymentController(type=type)

        return typing.cast(None, jsii.invoke(self, "putDeploymentController", [value]))

    @jsii.member(jsii_name="putLoadBalancer")
    def put_load_balancer(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceLoadBalancer", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServiceLoadBalancer, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLoadBalancer", [value]))

    @jsii.member(jsii_name="putNetworkConfiguration")
    def put_network_configuration(
        self,
        *,
        subnets: typing.Sequence[builtins.str],
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#subnets EcsService#subnets}.
        :param assign_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#assign_public_ip EcsService#assign_public_ip}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#security_groups EcsService#security_groups}.
        '''
        value = EcsServiceNetworkConfiguration(
            subnets=subnets,
            assign_public_ip=assign_public_ip,
            security_groups=security_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkConfiguration", [value]))

    @jsii.member(jsii_name="putOrderedPlacementStrategy")
    def put_ordered_placement_strategy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceOrderedPlacementStrategy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServiceOrderedPlacementStrategy, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOrderedPlacementStrategy", [value]))

    @jsii.member(jsii_name="putPlacementConstraints")
    def put_placement_constraints(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServicePlacementConstraints", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServicePlacementConstraints, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPlacementConstraints", [value]))

    @jsii.member(jsii_name="putServiceConnectConfiguration")
    def put_service_connect_configuration(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        log_configuration: typing.Optional[typing.Union["EcsServiceServiceConnectConfigurationLogConfiguration", typing.Dict[str, typing.Any]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        service: typing.Optional[typing.Union["EcsServiceServiceConnectConfigurationService", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enabled EcsService#enabled}.
        :param log_configuration: log_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#log_configuration EcsService#log_configuration}
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#namespace EcsService#namespace}.
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#service EcsService#service}
        '''
        value = EcsServiceServiceConnectConfiguration(
            enabled=enabled,
            log_configuration=log_configuration,
            namespace=namespace,
            service=service,
        )

        return typing.cast(None, jsii.invoke(self, "putServiceConnectConfiguration", [value]))

    @jsii.member(jsii_name="putServiceRegistries")
    def put_service_registries(
        self,
        *,
        registry_arn: builtins.str,
        container_name: typing.Optional[builtins.str] = None,
        container_port: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param registry_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#registry_arn EcsService#registry_arn}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_name EcsService#container_name}.
        :param container_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_port EcsService#container_port}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#port EcsService#port}.
        '''
        value = EcsServiceServiceRegistries(
            registry_arn=registry_arn,
            container_name=container_name,
            container_port=container_port,
            port=port,
        )

        return typing.cast(None, jsii.invoke(self, "putServiceRegistries", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#create EcsService#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#delete EcsService#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#update EcsService#update}.
        '''
        value = EcsServiceTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCapacityProviderStrategy")
    def reset_capacity_provider_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityProviderStrategy", []))

    @jsii.member(jsii_name="resetCluster")
    def reset_cluster(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCluster", []))

    @jsii.member(jsii_name="resetDeploymentCircuitBreaker")
    def reset_deployment_circuit_breaker(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentCircuitBreaker", []))

    @jsii.member(jsii_name="resetDeploymentController")
    def reset_deployment_controller(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentController", []))

    @jsii.member(jsii_name="resetDeploymentMaximumPercent")
    def reset_deployment_maximum_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentMaximumPercent", []))

    @jsii.member(jsii_name="resetDeploymentMinimumHealthyPercent")
    def reset_deployment_minimum_healthy_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentMinimumHealthyPercent", []))

    @jsii.member(jsii_name="resetDesiredCount")
    def reset_desired_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredCount", []))

    @jsii.member(jsii_name="resetEnableEcsManagedTags")
    def reset_enable_ecs_managed_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableEcsManagedTags", []))

    @jsii.member(jsii_name="resetEnableExecuteCommand")
    def reset_enable_execute_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableExecuteCommand", []))

    @jsii.member(jsii_name="resetForceNewDeployment")
    def reset_force_new_deployment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceNewDeployment", []))

    @jsii.member(jsii_name="resetHealthCheckGracePeriodSeconds")
    def reset_health_check_grace_period_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckGracePeriodSeconds", []))

    @jsii.member(jsii_name="resetIamRole")
    def reset_iam_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamRole", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLaunchType")
    def reset_launch_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchType", []))

    @jsii.member(jsii_name="resetLoadBalancer")
    def reset_load_balancer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancer", []))

    @jsii.member(jsii_name="resetNetworkConfiguration")
    def reset_network_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkConfiguration", []))

    @jsii.member(jsii_name="resetOrderedPlacementStrategy")
    def reset_ordered_placement_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrderedPlacementStrategy", []))

    @jsii.member(jsii_name="resetPlacementConstraints")
    def reset_placement_constraints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacementConstraints", []))

    @jsii.member(jsii_name="resetPlatformVersion")
    def reset_platform_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlatformVersion", []))

    @jsii.member(jsii_name="resetPropagateTags")
    def reset_propagate_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPropagateTags", []))

    @jsii.member(jsii_name="resetSchedulingStrategy")
    def reset_scheduling_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedulingStrategy", []))

    @jsii.member(jsii_name="resetServiceConnectConfiguration")
    def reset_service_connect_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceConnectConfiguration", []))

    @jsii.member(jsii_name="resetServiceRegistries")
    def reset_service_registries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRegistries", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTaskDefinition")
    def reset_task_definition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskDefinition", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTriggers")
    def reset_triggers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggers", []))

    @jsii.member(jsii_name="resetWaitForSteadyState")
    def reset_wait_for_steady_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForSteadyState", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="capacityProviderStrategy")
    def capacity_provider_strategy(self) -> "EcsServiceCapacityProviderStrategyList":
        return typing.cast("EcsServiceCapacityProviderStrategyList", jsii.get(self, "capacityProviderStrategy"))

    @builtins.property
    @jsii.member(jsii_name="deploymentCircuitBreaker")
    def deployment_circuit_breaker(
        self,
    ) -> "EcsServiceDeploymentCircuitBreakerOutputReference":
        return typing.cast("EcsServiceDeploymentCircuitBreakerOutputReference", jsii.get(self, "deploymentCircuitBreaker"))

    @builtins.property
    @jsii.member(jsii_name="deploymentController")
    def deployment_controller(self) -> "EcsServiceDeploymentControllerOutputReference":
        return typing.cast("EcsServiceDeploymentControllerOutputReference", jsii.get(self, "deploymentController"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancer")
    def load_balancer(self) -> "EcsServiceLoadBalancerList":
        return typing.cast("EcsServiceLoadBalancerList", jsii.get(self, "loadBalancer"))

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(self) -> "EcsServiceNetworkConfigurationOutputReference":
        return typing.cast("EcsServiceNetworkConfigurationOutputReference", jsii.get(self, "networkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="orderedPlacementStrategy")
    def ordered_placement_strategy(self) -> "EcsServiceOrderedPlacementStrategyList":
        return typing.cast("EcsServiceOrderedPlacementStrategyList", jsii.get(self, "orderedPlacementStrategy"))

    @builtins.property
    @jsii.member(jsii_name="placementConstraints")
    def placement_constraints(self) -> "EcsServicePlacementConstraintsList":
        return typing.cast("EcsServicePlacementConstraintsList", jsii.get(self, "placementConstraints"))

    @builtins.property
    @jsii.member(jsii_name="serviceConnectConfiguration")
    def service_connect_configuration(
        self,
    ) -> "EcsServiceServiceConnectConfigurationOutputReference":
        return typing.cast("EcsServiceServiceConnectConfigurationOutputReference", jsii.get(self, "serviceConnectConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="serviceRegistries")
    def service_registries(self) -> "EcsServiceServiceRegistriesOutputReference":
        return typing.cast("EcsServiceServiceRegistriesOutputReference", jsii.get(self, "serviceRegistries"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "EcsServiceTimeoutsOutputReference":
        return typing.cast("EcsServiceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="capacityProviderStrategyInput")
    def capacity_provider_strategy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceCapacityProviderStrategy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceCapacityProviderStrategy"]]], jsii.get(self, "capacityProviderStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterInput")
    def cluster_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentCircuitBreakerInput")
    def deployment_circuit_breaker_input(
        self,
    ) -> typing.Optional["EcsServiceDeploymentCircuitBreaker"]:
        return typing.cast(typing.Optional["EcsServiceDeploymentCircuitBreaker"], jsii.get(self, "deploymentCircuitBreakerInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentControllerInput")
    def deployment_controller_input(
        self,
    ) -> typing.Optional["EcsServiceDeploymentController"]:
        return typing.cast(typing.Optional["EcsServiceDeploymentController"], jsii.get(self, "deploymentControllerInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentMaximumPercentInput")
    def deployment_maximum_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deploymentMaximumPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentMinimumHealthyPercentInput")
    def deployment_minimum_healthy_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deploymentMinimumHealthyPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredCountInput")
    def desired_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "desiredCountInput"))

    @builtins.property
    @jsii.member(jsii_name="enableEcsManagedTagsInput")
    def enable_ecs_managed_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableEcsManagedTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="enableExecuteCommandInput")
    def enable_execute_command_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableExecuteCommandInput"))

    @builtins.property
    @jsii.member(jsii_name="forceNewDeploymentInput")
    def force_new_deployment_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceNewDeploymentInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckGracePeriodSecondsInput")
    def health_check_grace_period_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthCheckGracePeriodSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="iamRoleInput")
    def iam_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTypeInput")
    def launch_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerInput")
    def load_balancer_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceLoadBalancer"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceLoadBalancer"]]], jsii.get(self, "loadBalancerInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkConfigurationInput")
    def network_configuration_input(
        self,
    ) -> typing.Optional["EcsServiceNetworkConfiguration"]:
        return typing.cast(typing.Optional["EcsServiceNetworkConfiguration"], jsii.get(self, "networkConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="orderedPlacementStrategyInput")
    def ordered_placement_strategy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceOrderedPlacementStrategy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceOrderedPlacementStrategy"]]], jsii.get(self, "orderedPlacementStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="placementConstraintsInput")
    def placement_constraints_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServicePlacementConstraints"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServicePlacementConstraints"]]], jsii.get(self, "placementConstraintsInput"))

    @builtins.property
    @jsii.member(jsii_name="platformVersionInput")
    def platform_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="propagateTagsInput")
    def propagate_tags_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "propagateTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="schedulingStrategyInput")
    def scheduling_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schedulingStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceConnectConfigurationInput")
    def service_connect_configuration_input(
        self,
    ) -> typing.Optional["EcsServiceServiceConnectConfiguration"]:
        return typing.cast(typing.Optional["EcsServiceServiceConnectConfiguration"], jsii.get(self, "serviceConnectConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRegistriesInput")
    def service_registries_input(
        self,
    ) -> typing.Optional["EcsServiceServiceRegistries"]:
        return typing.cast(typing.Optional["EcsServiceServiceRegistries"], jsii.get(self, "serviceRegistriesInput"))

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
    @jsii.member(jsii_name="taskDefinitionInput")
    def task_definition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["EcsServiceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["EcsServiceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="triggersInput")
    def triggers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "triggersInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForSteadyStateInput")
    def wait_for_steady_state_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "waitForSteadyStateInput"))

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cluster"))

    @cluster.setter
    def cluster(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cluster", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentMaximumPercent")
    def deployment_maximum_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deploymentMaximumPercent"))

    @deployment_maximum_percent.setter
    def deployment_maximum_percent(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentMaximumPercent", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentMinimumHealthyPercent")
    def deployment_minimum_healthy_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deploymentMinimumHealthyPercent"))

    @deployment_minimum_healthy_percent.setter
    def deployment_minimum_healthy_percent(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentMinimumHealthyPercent", value)

    @builtins.property
    @jsii.member(jsii_name="desiredCount")
    def desired_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredCount"))

    @desired_count.setter
    def desired_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredCount", value)

    @builtins.property
    @jsii.member(jsii_name="enableEcsManagedTags")
    def enable_ecs_managed_tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableEcsManagedTags"))

    @enable_ecs_managed_tags.setter
    def enable_ecs_managed_tags(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableEcsManagedTags", value)

    @builtins.property
    @jsii.member(jsii_name="enableExecuteCommand")
    def enable_execute_command(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableExecuteCommand"))

    @enable_execute_command.setter
    def enable_execute_command(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableExecuteCommand", value)

    @builtins.property
    @jsii.member(jsii_name="forceNewDeployment")
    def force_new_deployment(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forceNewDeployment"))

    @force_new_deployment.setter
    def force_new_deployment(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceNewDeployment", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckGracePeriodSeconds")
    def health_check_grace_period_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthCheckGracePeriodSeconds"))

    @health_check_grace_period_seconds.setter
    def health_check_grace_period_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckGracePeriodSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="iamRole")
    def iam_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamRole"))

    @iam_role.setter
    def iam_role(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRole", value)

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
    @jsii.member(jsii_name="launchType")
    def launch_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchType"))

    @launch_type.setter
    def launch_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchType", value)

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
    @jsii.member(jsii_name="platformVersion")
    def platform_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platformVersion"))

    @platform_version.setter
    def platform_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformVersion", value)

    @builtins.property
    @jsii.member(jsii_name="propagateTags")
    def propagate_tags(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propagateTags"))

    @propagate_tags.setter
    def propagate_tags(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagateTags", value)

    @builtins.property
    @jsii.member(jsii_name="schedulingStrategy")
    def scheduling_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedulingStrategy"))

    @scheduling_strategy.setter
    def scheduling_strategy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedulingStrategy", value)

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

    @builtins.property
    @jsii.member(jsii_name="taskDefinition")
    def task_definition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskDefinition"))

    @task_definition.setter
    def task_definition(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskDefinition", value)

    @builtins.property
    @jsii.member(jsii_name="triggers")
    def triggers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "triggers"))

    @triggers.setter
    def triggers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggers", value)

    @builtins.property
    @jsii.member(jsii_name="waitForSteadyState")
    def wait_for_steady_state(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "waitForSteadyState"))

    @wait_for_steady_state.setter
    def wait_for_steady_state(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForSteadyState", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceCapacityProviderStrategy",
    jsii_struct_bases=[],
    name_mapping={
        "capacity_provider": "capacityProvider",
        "base": "base",
        "weight": "weight",
    },
)
class EcsServiceCapacityProviderStrategy:
    def __init__(
        self,
        *,
        capacity_provider: builtins.str,
        base: typing.Optional[jsii.Number] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param capacity_provider: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#capacity_provider EcsService#capacity_provider}.
        :param base: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#base EcsService#base}.
        :param weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#weight EcsService#weight}.
        '''
        if __debug__:
            def stub(
                *,
                capacity_provider: builtins.str,
                base: typing.Optional[jsii.Number] = None,
                weight: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument capacity_provider", value=capacity_provider, expected_type=type_hints["capacity_provider"])
            check_type(argname="argument base", value=base, expected_type=type_hints["base"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[str, typing.Any] = {
            "capacity_provider": capacity_provider,
        }
        if base is not None:
            self._values["base"] = base
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def capacity_provider(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#capacity_provider EcsService#capacity_provider}.'''
        result = self._values.get("capacity_provider")
        assert result is not None, "Required property 'capacity_provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#base EcsService#base}.'''
        result = self._values.get("base")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#weight EcsService#weight}.'''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceCapacityProviderStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceCapacityProviderStrategyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceCapacityProviderStrategyList",
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
    ) -> "EcsServiceCapacityProviderStrategyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsServiceCapacityProviderStrategyOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceCapacityProviderStrategy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceCapacityProviderStrategy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceCapacityProviderStrategy]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceCapacityProviderStrategy]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsServiceCapacityProviderStrategyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceCapacityProviderStrategyOutputReference",
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

    @jsii.member(jsii_name="resetBase")
    def reset_base(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBase", []))

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

    @builtins.property
    @jsii.member(jsii_name="baseInput")
    def base_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "baseInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityProviderInput")
    def capacity_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "capacityProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="base")
    def base(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "base"))

    @base.setter
    def base(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "base", value)

    @builtins.property
    @jsii.member(jsii_name="capacityProvider")
    def capacity_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityProvider"))

    @capacity_provider.setter
    def capacity_provider(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityProvider", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsServiceCapacityProviderStrategy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsServiceCapacityProviderStrategy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsServiceCapacityProviderStrategy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EcsServiceCapacityProviderStrategy, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "capacity_provider_strategy": "capacityProviderStrategy",
        "cluster": "cluster",
        "deployment_circuit_breaker": "deploymentCircuitBreaker",
        "deployment_controller": "deploymentController",
        "deployment_maximum_percent": "deploymentMaximumPercent",
        "deployment_minimum_healthy_percent": "deploymentMinimumHealthyPercent",
        "desired_count": "desiredCount",
        "enable_ecs_managed_tags": "enableEcsManagedTags",
        "enable_execute_command": "enableExecuteCommand",
        "force_new_deployment": "forceNewDeployment",
        "health_check_grace_period_seconds": "healthCheckGracePeriodSeconds",
        "iam_role": "iamRole",
        "id": "id",
        "launch_type": "launchType",
        "load_balancer": "loadBalancer",
        "network_configuration": "networkConfiguration",
        "ordered_placement_strategy": "orderedPlacementStrategy",
        "placement_constraints": "placementConstraints",
        "platform_version": "platformVersion",
        "propagate_tags": "propagateTags",
        "scheduling_strategy": "schedulingStrategy",
        "service_connect_configuration": "serviceConnectConfiguration",
        "service_registries": "serviceRegistries",
        "tags": "tags",
        "tags_all": "tagsAll",
        "task_definition": "taskDefinition",
        "timeouts": "timeouts",
        "triggers": "triggers",
        "wait_for_steady_state": "waitForSteadyState",
    },
)
class EcsServiceConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        capacity_provider_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServiceCapacityProviderStrategy, typing.Dict[str, typing.Any]]]]] = None,
        cluster: typing.Optional[builtins.str] = None,
        deployment_circuit_breaker: typing.Optional[typing.Union["EcsServiceDeploymentCircuitBreaker", typing.Dict[str, typing.Any]]] = None,
        deployment_controller: typing.Optional[typing.Union["EcsServiceDeploymentController", typing.Dict[str, typing.Any]]] = None,
        deployment_maximum_percent: typing.Optional[jsii.Number] = None,
        deployment_minimum_healthy_percent: typing.Optional[jsii.Number] = None,
        desired_count: typing.Optional[jsii.Number] = None,
        enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_execute_command: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        force_new_deployment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_check_grace_period_seconds: typing.Optional[jsii.Number] = None,
        iam_role: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        launch_type: typing.Optional[builtins.str] = None,
        load_balancer: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceLoadBalancer", typing.Dict[str, typing.Any]]]]] = None,
        network_configuration: typing.Optional[typing.Union["EcsServiceNetworkConfiguration", typing.Dict[str, typing.Any]]] = None,
        ordered_placement_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceOrderedPlacementStrategy", typing.Dict[str, typing.Any]]]]] = None,
        placement_constraints: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServicePlacementConstraints", typing.Dict[str, typing.Any]]]]] = None,
        platform_version: typing.Optional[builtins.str] = None,
        propagate_tags: typing.Optional[builtins.str] = None,
        scheduling_strategy: typing.Optional[builtins.str] = None,
        service_connect_configuration: typing.Optional[typing.Union["EcsServiceServiceConnectConfiguration", typing.Dict[str, typing.Any]]] = None,
        service_registries: typing.Optional[typing.Union["EcsServiceServiceRegistries", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        task_definition: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["EcsServiceTimeouts", typing.Dict[str, typing.Any]]] = None,
        triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        wait_for_steady_state: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#name EcsService#name}.
        :param capacity_provider_strategy: capacity_provider_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#capacity_provider_strategy EcsService#capacity_provider_strategy}
        :param cluster: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#cluster EcsService#cluster}.
        :param deployment_circuit_breaker: deployment_circuit_breaker block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_circuit_breaker EcsService#deployment_circuit_breaker}
        :param deployment_controller: deployment_controller block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_controller EcsService#deployment_controller}
        :param deployment_maximum_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_maximum_percent EcsService#deployment_maximum_percent}.
        :param deployment_minimum_healthy_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_minimum_healthy_percent EcsService#deployment_minimum_healthy_percent}.
        :param desired_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#desired_count EcsService#desired_count}.
        :param enable_ecs_managed_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enable_ecs_managed_tags EcsService#enable_ecs_managed_tags}.
        :param enable_execute_command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enable_execute_command EcsService#enable_execute_command}.
        :param force_new_deployment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#force_new_deployment EcsService#force_new_deployment}.
        :param health_check_grace_period_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#health_check_grace_period_seconds EcsService#health_check_grace_period_seconds}.
        :param iam_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#iam_role EcsService#iam_role}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#id EcsService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param launch_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#launch_type EcsService#launch_type}.
        :param load_balancer: load_balancer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#load_balancer EcsService#load_balancer}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#network_configuration EcsService#network_configuration}
        :param ordered_placement_strategy: ordered_placement_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#ordered_placement_strategy EcsService#ordered_placement_strategy}
        :param placement_constraints: placement_constraints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#placement_constraints EcsService#placement_constraints}
        :param platform_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#platform_version EcsService#platform_version}.
        :param propagate_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#propagate_tags EcsService#propagate_tags}.
        :param scheduling_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#scheduling_strategy EcsService#scheduling_strategy}.
        :param service_connect_configuration: service_connect_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#service_connect_configuration EcsService#service_connect_configuration}
        :param service_registries: service_registries block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#service_registries EcsService#service_registries}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#tags EcsService#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#tags_all EcsService#tags_all}.
        :param task_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#task_definition EcsService#task_definition}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#timeouts EcsService#timeouts}
        :param triggers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#triggers EcsService#triggers}.
        :param wait_for_steady_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#wait_for_steady_state EcsService#wait_for_steady_state}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(deployment_circuit_breaker, dict):
            deployment_circuit_breaker = EcsServiceDeploymentCircuitBreaker(**deployment_circuit_breaker)
        if isinstance(deployment_controller, dict):
            deployment_controller = EcsServiceDeploymentController(**deployment_controller)
        if isinstance(network_configuration, dict):
            network_configuration = EcsServiceNetworkConfiguration(**network_configuration)
        if isinstance(service_connect_configuration, dict):
            service_connect_configuration = EcsServiceServiceConnectConfiguration(**service_connect_configuration)
        if isinstance(service_registries, dict):
            service_registries = EcsServiceServiceRegistries(**service_registries)
        if isinstance(timeouts, dict):
            timeouts = EcsServiceTimeouts(**timeouts)
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
                name: builtins.str,
                capacity_provider_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServiceCapacityProviderStrategy, typing.Dict[str, typing.Any]]]]] = None,
                cluster: typing.Optional[builtins.str] = None,
                deployment_circuit_breaker: typing.Optional[typing.Union[EcsServiceDeploymentCircuitBreaker, typing.Dict[str, typing.Any]]] = None,
                deployment_controller: typing.Optional[typing.Union[EcsServiceDeploymentController, typing.Dict[str, typing.Any]]] = None,
                deployment_maximum_percent: typing.Optional[jsii.Number] = None,
                deployment_minimum_healthy_percent: typing.Optional[jsii.Number] = None,
                desired_count: typing.Optional[jsii.Number] = None,
                enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                enable_execute_command: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                force_new_deployment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                health_check_grace_period_seconds: typing.Optional[jsii.Number] = None,
                iam_role: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                launch_type: typing.Optional[builtins.str] = None,
                load_balancer: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServiceLoadBalancer, typing.Dict[str, typing.Any]]]]] = None,
                network_configuration: typing.Optional[typing.Union[EcsServiceNetworkConfiguration, typing.Dict[str, typing.Any]]] = None,
                ordered_placement_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServiceOrderedPlacementStrategy, typing.Dict[str, typing.Any]]]]] = None,
                placement_constraints: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServicePlacementConstraints, typing.Dict[str, typing.Any]]]]] = None,
                platform_version: typing.Optional[builtins.str] = None,
                propagate_tags: typing.Optional[builtins.str] = None,
                scheduling_strategy: typing.Optional[builtins.str] = None,
                service_connect_configuration: typing.Optional[typing.Union[EcsServiceServiceConnectConfiguration, typing.Dict[str, typing.Any]]] = None,
                service_registries: typing.Optional[typing.Union[EcsServiceServiceRegistries, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                task_definition: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[EcsServiceTimeouts, typing.Dict[str, typing.Any]]] = None,
                triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                wait_for_steady_state: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument capacity_provider_strategy", value=capacity_provider_strategy, expected_type=type_hints["capacity_provider_strategy"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument deployment_circuit_breaker", value=deployment_circuit_breaker, expected_type=type_hints["deployment_circuit_breaker"])
            check_type(argname="argument deployment_controller", value=deployment_controller, expected_type=type_hints["deployment_controller"])
            check_type(argname="argument deployment_maximum_percent", value=deployment_maximum_percent, expected_type=type_hints["deployment_maximum_percent"])
            check_type(argname="argument deployment_minimum_healthy_percent", value=deployment_minimum_healthy_percent, expected_type=type_hints["deployment_minimum_healthy_percent"])
            check_type(argname="argument desired_count", value=desired_count, expected_type=type_hints["desired_count"])
            check_type(argname="argument enable_ecs_managed_tags", value=enable_ecs_managed_tags, expected_type=type_hints["enable_ecs_managed_tags"])
            check_type(argname="argument enable_execute_command", value=enable_execute_command, expected_type=type_hints["enable_execute_command"])
            check_type(argname="argument force_new_deployment", value=force_new_deployment, expected_type=type_hints["force_new_deployment"])
            check_type(argname="argument health_check_grace_period_seconds", value=health_check_grace_period_seconds, expected_type=type_hints["health_check_grace_period_seconds"])
            check_type(argname="argument iam_role", value=iam_role, expected_type=type_hints["iam_role"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument launch_type", value=launch_type, expected_type=type_hints["launch_type"])
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument ordered_placement_strategy", value=ordered_placement_strategy, expected_type=type_hints["ordered_placement_strategy"])
            check_type(argname="argument placement_constraints", value=placement_constraints, expected_type=type_hints["placement_constraints"])
            check_type(argname="argument platform_version", value=platform_version, expected_type=type_hints["platform_version"])
            check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
            check_type(argname="argument scheduling_strategy", value=scheduling_strategy, expected_type=type_hints["scheduling_strategy"])
            check_type(argname="argument service_connect_configuration", value=service_connect_configuration, expected_type=type_hints["service_connect_configuration"])
            check_type(argname="argument service_registries", value=service_registries, expected_type=type_hints["service_registries"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument triggers", value=triggers, expected_type=type_hints["triggers"])
            check_type(argname="argument wait_for_steady_state", value=wait_for_steady_state, expected_type=type_hints["wait_for_steady_state"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
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
        if capacity_provider_strategy is not None:
            self._values["capacity_provider_strategy"] = capacity_provider_strategy
        if cluster is not None:
            self._values["cluster"] = cluster
        if deployment_circuit_breaker is not None:
            self._values["deployment_circuit_breaker"] = deployment_circuit_breaker
        if deployment_controller is not None:
            self._values["deployment_controller"] = deployment_controller
        if deployment_maximum_percent is not None:
            self._values["deployment_maximum_percent"] = deployment_maximum_percent
        if deployment_minimum_healthy_percent is not None:
            self._values["deployment_minimum_healthy_percent"] = deployment_minimum_healthy_percent
        if desired_count is not None:
            self._values["desired_count"] = desired_count
        if enable_ecs_managed_tags is not None:
            self._values["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            self._values["enable_execute_command"] = enable_execute_command
        if force_new_deployment is not None:
            self._values["force_new_deployment"] = force_new_deployment
        if health_check_grace_period_seconds is not None:
            self._values["health_check_grace_period_seconds"] = health_check_grace_period_seconds
        if iam_role is not None:
            self._values["iam_role"] = iam_role
        if id is not None:
            self._values["id"] = id
        if launch_type is not None:
            self._values["launch_type"] = launch_type
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if ordered_placement_strategy is not None:
            self._values["ordered_placement_strategy"] = ordered_placement_strategy
        if placement_constraints is not None:
            self._values["placement_constraints"] = placement_constraints
        if platform_version is not None:
            self._values["platform_version"] = platform_version
        if propagate_tags is not None:
            self._values["propagate_tags"] = propagate_tags
        if scheduling_strategy is not None:
            self._values["scheduling_strategy"] = scheduling_strategy
        if service_connect_configuration is not None:
            self._values["service_connect_configuration"] = service_connect_configuration
        if service_registries is not None:
            self._values["service_registries"] = service_registries
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if task_definition is not None:
            self._values["task_definition"] = task_definition
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if triggers is not None:
            self._values["triggers"] = triggers
        if wait_for_steady_state is not None:
            self._values["wait_for_steady_state"] = wait_for_steady_state

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#name EcsService#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity_provider_strategy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceCapacityProviderStrategy]]]:
        '''capacity_provider_strategy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#capacity_provider_strategy EcsService#capacity_provider_strategy}
        '''
        result = self._values.get("capacity_provider_strategy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceCapacityProviderStrategy]]], result)

    @builtins.property
    def cluster(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#cluster EcsService#cluster}.'''
        result = self._values.get("cluster")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deployment_circuit_breaker(
        self,
    ) -> typing.Optional["EcsServiceDeploymentCircuitBreaker"]:
        '''deployment_circuit_breaker block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_circuit_breaker EcsService#deployment_circuit_breaker}
        '''
        result = self._values.get("deployment_circuit_breaker")
        return typing.cast(typing.Optional["EcsServiceDeploymentCircuitBreaker"], result)

    @builtins.property
    def deployment_controller(
        self,
    ) -> typing.Optional["EcsServiceDeploymentController"]:
        '''deployment_controller block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_controller EcsService#deployment_controller}
        '''
        result = self._values.get("deployment_controller")
        return typing.cast(typing.Optional["EcsServiceDeploymentController"], result)

    @builtins.property
    def deployment_maximum_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_maximum_percent EcsService#deployment_maximum_percent}.'''
        result = self._values.get("deployment_maximum_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def deployment_minimum_healthy_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#deployment_minimum_healthy_percent EcsService#deployment_minimum_healthy_percent}.'''
        result = self._values.get("deployment_minimum_healthy_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def desired_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#desired_count EcsService#desired_count}.'''
        result = self._values.get("desired_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enable_ecs_managed_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enable_ecs_managed_tags EcsService#enable_ecs_managed_tags}.'''
        result = self._values.get("enable_ecs_managed_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_execute_command(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enable_execute_command EcsService#enable_execute_command}.'''
        result = self._values.get("enable_execute_command")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def force_new_deployment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#force_new_deployment EcsService#force_new_deployment}.'''
        result = self._values.get("force_new_deployment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def health_check_grace_period_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#health_check_grace_period_seconds EcsService#health_check_grace_period_seconds}.'''
        result = self._values.get("health_check_grace_period_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def iam_role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#iam_role EcsService#iam_role}.'''
        result = self._values.get("iam_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#id EcsService#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#launch_type EcsService#launch_type}.'''
        result = self._values.get("launch_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceLoadBalancer"]]]:
        '''load_balancer block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#load_balancer EcsService#load_balancer}
        '''
        result = self._values.get("load_balancer")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceLoadBalancer"]]], result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Optional["EcsServiceNetworkConfiguration"]:
        '''network_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#network_configuration EcsService#network_configuration}
        '''
        result = self._values.get("network_configuration")
        return typing.cast(typing.Optional["EcsServiceNetworkConfiguration"], result)

    @builtins.property
    def ordered_placement_strategy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceOrderedPlacementStrategy"]]]:
        '''ordered_placement_strategy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#ordered_placement_strategy EcsService#ordered_placement_strategy}
        '''
        result = self._values.get("ordered_placement_strategy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceOrderedPlacementStrategy"]]], result)

    @builtins.property
    def placement_constraints(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServicePlacementConstraints"]]]:
        '''placement_constraints block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#placement_constraints EcsService#placement_constraints}
        '''
        result = self._values.get("placement_constraints")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServicePlacementConstraints"]]], result)

    @builtins.property
    def platform_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#platform_version EcsService#platform_version}.'''
        result = self._values.get("platform_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def propagate_tags(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#propagate_tags EcsService#propagate_tags}.'''
        result = self._values.get("propagate_tags")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheduling_strategy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#scheduling_strategy EcsService#scheduling_strategy}.'''
        result = self._values.get("scheduling_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_connect_configuration(
        self,
    ) -> typing.Optional["EcsServiceServiceConnectConfiguration"]:
        '''service_connect_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#service_connect_configuration EcsService#service_connect_configuration}
        '''
        result = self._values.get("service_connect_configuration")
        return typing.cast(typing.Optional["EcsServiceServiceConnectConfiguration"], result)

    @builtins.property
    def service_registries(self) -> typing.Optional["EcsServiceServiceRegistries"]:
        '''service_registries block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#service_registries EcsService#service_registries}
        '''
        result = self._values.get("service_registries")
        return typing.cast(typing.Optional["EcsServiceServiceRegistries"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#tags EcsService#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#tags_all EcsService#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def task_definition(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#task_definition EcsService#task_definition}.'''
        result = self._values.get("task_definition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["EcsServiceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#timeouts EcsService#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["EcsServiceTimeouts"], result)

    @builtins.property
    def triggers(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#triggers EcsService#triggers}.'''
        result = self._values.get("triggers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def wait_for_steady_state(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#wait_for_steady_state EcsService#wait_for_steady_state}.'''
        result = self._values.get("wait_for_steady_state")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceDeploymentCircuitBreaker",
    jsii_struct_bases=[],
    name_mapping={"enable": "enable", "rollback": "rollback"},
)
class EcsServiceDeploymentCircuitBreaker:
    def __init__(
        self,
        *,
        enable: typing.Union[builtins.bool, cdktf.IResolvable],
        rollback: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enable EcsService#enable}.
        :param rollback: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#rollback EcsService#rollback}.
        '''
        if __debug__:
            def stub(
                *,
                enable: typing.Union[builtins.bool, cdktf.IResolvable],
                rollback: typing.Union[builtins.bool, cdktf.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            check_type(argname="argument rollback", value=rollback, expected_type=type_hints["rollback"])
        self._values: typing.Dict[str, typing.Any] = {
            "enable": enable,
            "rollback": rollback,
        }

    @builtins.property
    def enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enable EcsService#enable}.'''
        result = self._values.get("enable")
        assert result is not None, "Required property 'enable' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def rollback(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#rollback EcsService#rollback}.'''
        result = self._values.get("rollback")
        assert result is not None, "Required property 'rollback' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceDeploymentCircuitBreaker(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceDeploymentCircuitBreakerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceDeploymentCircuitBreakerOutputReference",
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
    @jsii.member(jsii_name="rollbackInput")
    def rollback_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "rollbackInput"))

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
    @jsii.member(jsii_name="rollback")
    def rollback(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "rollback"))

    @rollback.setter
    def rollback(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rollback", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsServiceDeploymentCircuitBreaker]:
        return typing.cast(typing.Optional[EcsServiceDeploymentCircuitBreaker], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceDeploymentCircuitBreaker],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[EcsServiceDeploymentCircuitBreaker],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceDeploymentController",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class EcsServiceDeploymentController:
    def __init__(self, *, type: typing.Optional[builtins.str] = None) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#type EcsService#type}.
        '''
        if __debug__:
            def stub(*, type: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#type EcsService#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceDeploymentController(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceDeploymentControllerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceDeploymentControllerOutputReference",
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
    def internal_value(self) -> typing.Optional[EcsServiceDeploymentController]:
        return typing.cast(typing.Optional[EcsServiceDeploymentController], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceDeploymentController],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[EcsServiceDeploymentController]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={
        "container_name": "containerName",
        "container_port": "containerPort",
        "elb_name": "elbName",
        "target_group_arn": "targetGroupArn",
    },
)
class EcsServiceLoadBalancer:
    def __init__(
        self,
        *,
        container_name: builtins.str,
        container_port: jsii.Number,
        elb_name: typing.Optional[builtins.str] = None,
        target_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_name EcsService#container_name}.
        :param container_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_port EcsService#container_port}.
        :param elb_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#elb_name EcsService#elb_name}.
        :param target_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#target_group_arn EcsService#target_group_arn}.
        '''
        if __debug__:
            def stub(
                *,
                container_name: builtins.str,
                container_port: jsii.Number,
                elb_name: typing.Optional[builtins.str] = None,
                target_group_arn: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument container_port", value=container_port, expected_type=type_hints["container_port"])
            check_type(argname="argument elb_name", value=elb_name, expected_type=type_hints["elb_name"])
            check_type(argname="argument target_group_arn", value=target_group_arn, expected_type=type_hints["target_group_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "container_name": container_name,
            "container_port": container_port,
        }
        if elb_name is not None:
            self._values["elb_name"] = elb_name
        if target_group_arn is not None:
            self._values["target_group_arn"] = target_group_arn

    @builtins.property
    def container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_name EcsService#container_name}.'''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_port EcsService#container_port}.'''
        result = self._values.get("container_port")
        assert result is not None, "Required property 'container_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def elb_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#elb_name EcsService#elb_name}.'''
        result = self._values.get("elb_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#target_group_arn EcsService#target_group_arn}.'''
        result = self._values.get("target_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceLoadBalancerList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceLoadBalancerList",
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
    def get(self, index: jsii.Number) -> "EcsServiceLoadBalancerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsServiceLoadBalancerOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceLoadBalancer]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceLoadBalancer]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceLoadBalancer]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceLoadBalancer]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsServiceLoadBalancerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceLoadBalancerOutputReference",
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

    @jsii.member(jsii_name="resetElbName")
    def reset_elb_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElbName", []))

    @jsii.member(jsii_name="resetTargetGroupArn")
    def reset_target_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetGroupArn", []))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="containerPortInput")
    def container_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "containerPortInput"))

    @builtins.property
    @jsii.member(jsii_name="elbNameInput")
    def elb_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elbNameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupArnInput")
    def target_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="containerPort")
    def container_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerPort"))

    @container_port.setter
    def container_port(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerPort", value)

    @builtins.property
    @jsii.member(jsii_name="elbName")
    def elb_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elbName"))

    @elb_name.setter
    def elb_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elbName", value)

    @builtins.property
    @jsii.member(jsii_name="targetGroupArn")
    def target_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetGroupArn"))

    @target_group_arn.setter
    def target_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsServiceLoadBalancer, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsServiceLoadBalancer, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsServiceLoadBalancer, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EcsServiceLoadBalancer, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceNetworkConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "subnets": "subnets",
        "assign_public_ip": "assignPublicIp",
        "security_groups": "securityGroups",
    },
)
class EcsServiceNetworkConfiguration:
    def __init__(
        self,
        *,
        subnets: typing.Sequence[builtins.str],
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#subnets EcsService#subnets}.
        :param assign_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#assign_public_ip EcsService#assign_public_ip}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#security_groups EcsService#security_groups}.
        '''
        if __debug__:
            def stub(
                *,
                subnets: typing.Sequence[builtins.str],
                assign_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
        self._values: typing.Dict[str, typing.Any] = {
            "subnets": subnets,
        }
        if assign_public_ip is not None:
            self._values["assign_public_ip"] = assign_public_ip
        if security_groups is not None:
            self._values["security_groups"] = security_groups

    @builtins.property
    def subnets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#subnets EcsService#subnets}.'''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def assign_public_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#assign_public_ip EcsService#assign_public_ip}.'''
        result = self._values.get("assign_public_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#security_groups EcsService#security_groups}.'''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceNetworkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceNetworkConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceNetworkConfigurationOutputReference",
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

    @jsii.member(jsii_name="resetAssignPublicIp")
    def reset_assign_public_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssignPublicIp", []))

    @jsii.member(jsii_name="resetSecurityGroups")
    def reset_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroups", []))

    @builtins.property
    @jsii.member(jsii_name="assignPublicIpInput")
    def assign_public_ip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "assignPublicIpInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetsInput")
    def subnets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetsInput"))

    @builtins.property
    @jsii.member(jsii_name="assignPublicIp")
    def assign_public_ip(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "assignPublicIp"))

    @assign_public_ip.setter
    def assign_public_ip(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assignPublicIp", value)

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsServiceNetworkConfiguration]:
        return typing.cast(typing.Optional[EcsServiceNetworkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceNetworkConfiguration],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[EcsServiceNetworkConfiguration]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceOrderedPlacementStrategy",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "field": "field"},
)
class EcsServiceOrderedPlacementStrategy:
    def __init__(
        self,
        *,
        type: builtins.str,
        field: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#type EcsService#type}.
        :param field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#field EcsService#field}.
        '''
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                field: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if field is not None:
            self._values["field"] = field

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#type EcsService#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def field(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#field EcsService#field}.'''
        result = self._values.get("field")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceOrderedPlacementStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceOrderedPlacementStrategyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceOrderedPlacementStrategyList",
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
    ) -> "EcsServiceOrderedPlacementStrategyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsServiceOrderedPlacementStrategyOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceOrderedPlacementStrategy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceOrderedPlacementStrategy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceOrderedPlacementStrategy]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceOrderedPlacementStrategy]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsServiceOrderedPlacementStrategyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceOrderedPlacementStrategyOutputReference",
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

    @jsii.member(jsii_name="resetField")
    def reset_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetField", []))

    @builtins.property
    @jsii.member(jsii_name="fieldInput")
    def field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="field")
    def field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "field"))

    @field.setter
    def field(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "field", value)

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
    ) -> typing.Optional[typing.Union[EcsServiceOrderedPlacementStrategy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsServiceOrderedPlacementStrategy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsServiceOrderedPlacementStrategy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EcsServiceOrderedPlacementStrategy, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecsService.EcsServicePlacementConstraints",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "expression": "expression"},
)
class EcsServicePlacementConstraints:
    def __init__(
        self,
        *,
        type: builtins.str,
        expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#type EcsService#type}.
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#expression EcsService#expression}.
        '''
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                expression: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if expression is not None:
            self._values["expression"] = expression

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#type EcsService#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#expression EcsService#expression}.'''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServicePlacementConstraints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServicePlacementConstraintsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServicePlacementConstraintsList",
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
    ) -> "EcsServicePlacementConstraintsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsServicePlacementConstraintsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServicePlacementConstraints]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServicePlacementConstraints]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServicePlacementConstraints]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServicePlacementConstraints]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsServicePlacementConstraintsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServicePlacementConstraintsOutputReference",
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

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

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
    ) -> typing.Optional[typing.Union[EcsServicePlacementConstraints, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsServicePlacementConstraints, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsServicePlacementConstraints, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EcsServicePlacementConstraints, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceServiceConnectConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "log_configuration": "logConfiguration",
        "namespace": "namespace",
        "service": "service",
    },
)
class EcsServiceServiceConnectConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        log_configuration: typing.Optional[typing.Union["EcsServiceServiceConnectConfigurationLogConfiguration", typing.Dict[str, typing.Any]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        service: typing.Optional[typing.Union["EcsServiceServiceConnectConfigurationService", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enabled EcsService#enabled}.
        :param log_configuration: log_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#log_configuration EcsService#log_configuration}
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#namespace EcsService#namespace}.
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#service EcsService#service}
        '''
        if isinstance(log_configuration, dict):
            log_configuration = EcsServiceServiceConnectConfigurationLogConfiguration(**log_configuration)
        if isinstance(service, dict):
            service = EcsServiceServiceConnectConfigurationService(**service)
        if __debug__:
            def stub(
                *,
                enabled: typing.Union[builtins.bool, cdktf.IResolvable],
                log_configuration: typing.Optional[typing.Union[EcsServiceServiceConnectConfigurationLogConfiguration, typing.Dict[str, typing.Any]]] = None,
                namespace: typing.Optional[builtins.str] = None,
                service: typing.Optional[typing.Union[EcsServiceServiceConnectConfigurationService, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_configuration", value=log_configuration, expected_type=type_hints["log_configuration"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if log_configuration is not None:
            self._values["log_configuration"] = log_configuration
        if namespace is not None:
            self._values["namespace"] = namespace
        if service is not None:
            self._values["service"] = service

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#enabled EcsService#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def log_configuration(
        self,
    ) -> typing.Optional["EcsServiceServiceConnectConfigurationLogConfiguration"]:
        '''log_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#log_configuration EcsService#log_configuration}
        '''
        result = self._values.get("log_configuration")
        return typing.cast(typing.Optional["EcsServiceServiceConnectConfigurationLogConfiguration"], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#namespace EcsService#namespace}.'''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service(
        self,
    ) -> typing.Optional["EcsServiceServiceConnectConfigurationService"]:
        '''service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#service EcsService#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional["EcsServiceServiceConnectConfigurationService"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceServiceConnectConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceServiceConnectConfigurationLogConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "log_driver": "logDriver",
        "options": "options",
        "secret_option": "secretOption",
    },
)
class EcsServiceServiceConnectConfigurationLogConfiguration:
    def __init__(
        self,
        *,
        log_driver: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        secret_option: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceServiceConnectConfigurationLogConfigurationSecretOption", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param log_driver: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#log_driver EcsService#log_driver}.
        :param options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#options EcsService#options}.
        :param secret_option: secret_option block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#secret_option EcsService#secret_option}
        '''
        if __debug__:
            def stub(
                *,
                log_driver: typing.Optional[builtins.str] = None,
                options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                secret_option: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServiceServiceConnectConfigurationLogConfigurationSecretOption, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument log_driver", value=log_driver, expected_type=type_hints["log_driver"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument secret_option", value=secret_option, expected_type=type_hints["secret_option"])
        self._values: typing.Dict[str, typing.Any] = {}
        if log_driver is not None:
            self._values["log_driver"] = log_driver
        if options is not None:
            self._values["options"] = options
        if secret_option is not None:
            self._values["secret_option"] = secret_option

    @builtins.property
    def log_driver(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#log_driver EcsService#log_driver}.'''
        result = self._values.get("log_driver")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#options EcsService#options}.'''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def secret_option(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceServiceConnectConfigurationLogConfigurationSecretOption"]]]:
        '''secret_option block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#secret_option EcsService#secret_option}
        '''
        result = self._values.get("secret_option")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceServiceConnectConfigurationLogConfigurationSecretOption"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceServiceConnectConfigurationLogConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceServiceConnectConfigurationLogConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceServiceConnectConfigurationLogConfigurationOutputReference",
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

    @jsii.member(jsii_name="putSecretOption")
    def put_secret_option(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceServiceConnectConfigurationLogConfigurationSecretOption", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServiceServiceConnectConfigurationLogConfigurationSecretOption, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecretOption", [value]))

    @jsii.member(jsii_name="resetLogDriver")
    def reset_log_driver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogDriver", []))

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @jsii.member(jsii_name="resetSecretOption")
    def reset_secret_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretOption", []))

    @builtins.property
    @jsii.member(jsii_name="secretOption")
    def secret_option(
        self,
    ) -> "EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionList":
        return typing.cast("EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionList", jsii.get(self, "secretOption"))

    @builtins.property
    @jsii.member(jsii_name="logDriverInput")
    def log_driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logDriverInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="secretOptionInput")
    def secret_option_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceServiceConnectConfigurationLogConfigurationSecretOption"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EcsServiceServiceConnectConfigurationLogConfigurationSecretOption"]]], jsii.get(self, "secretOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="logDriver")
    def log_driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logDriver"))

    @log_driver.setter
    def log_driver(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logDriver", value)

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsServiceServiceConnectConfigurationLogConfiguration]:
        return typing.cast(typing.Optional[EcsServiceServiceConnectConfigurationLogConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceServiceConnectConfigurationLogConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[EcsServiceServiceConnectConfigurationLogConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceServiceConnectConfigurationLogConfigurationSecretOption",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value_from": "valueFrom"},
)
class EcsServiceServiceConnectConfigurationLogConfigurationSecretOption:
    def __init__(self, *, name: builtins.str, value_from: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#name EcsService#name}.
        :param value_from: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#value_from EcsService#value_from}.
        '''
        if __debug__:
            def stub(*, name: builtins.str, value_from: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value_from", value=value_from, expected_type=type_hints["value_from"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value_from": value_from,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#name EcsService#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value_from(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#value_from EcsService#value_from}.'''
        result = self._values.get("value_from")
        assert result is not None, "Required property 'value_from' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceServiceConnectConfigurationLogConfigurationSecretOption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionList",
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
    ) -> "EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceServiceConnectConfigurationLogConfigurationSecretOption]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceServiceConnectConfigurationLogConfigurationSecretOption]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceServiceConnectConfigurationLogConfigurationSecretOption]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceServiceConnectConfigurationLogConfigurationSecretOption]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionOutputReference",
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

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueFromInput")
    def value_from_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueFromInput"))

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
    @jsii.member(jsii_name="valueFrom")
    def value_from(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "valueFrom"))

    @value_from.setter
    def value_from(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueFrom", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsServiceServiceConnectConfigurationLogConfigurationSecretOption, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsServiceServiceConnectConfigurationLogConfigurationSecretOption, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsServiceServiceConnectConfigurationLogConfigurationSecretOption, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EcsServiceServiceConnectConfigurationLogConfigurationSecretOption, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsServiceServiceConnectConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceServiceConnectConfigurationOutputReference",
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

    @jsii.member(jsii_name="putLogConfiguration")
    def put_log_configuration(
        self,
        *,
        log_driver: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        secret_option: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServiceServiceConnectConfigurationLogConfigurationSecretOption, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param log_driver: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#log_driver EcsService#log_driver}.
        :param options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#options EcsService#options}.
        :param secret_option: secret_option block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#secret_option EcsService#secret_option}
        '''
        value = EcsServiceServiceConnectConfigurationLogConfiguration(
            log_driver=log_driver, options=options, secret_option=secret_option
        )

        return typing.cast(None, jsii.invoke(self, "putLogConfiguration", [value]))

    @jsii.member(jsii_name="putService")
    def put_service(
        self,
        *,
        client_alias: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceServiceConnectConfigurationServiceClientAlias", typing.Dict[str, typing.Any]]]],
        port_name: builtins.str,
        discovery_name: typing.Optional[builtins.str] = None,
        ingress_port_override: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param client_alias: client_alias block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#client_alias EcsService#client_alias}
        :param port_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#port_name EcsService#port_name}.
        :param discovery_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#discovery_name EcsService#discovery_name}.
        :param ingress_port_override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#ingress_port_override EcsService#ingress_port_override}.
        '''
        value = EcsServiceServiceConnectConfigurationService(
            client_alias=client_alias,
            port_name=port_name,
            discovery_name=discovery_name,
            ingress_port_override=ingress_port_override,
        )

        return typing.cast(None, jsii.invoke(self, "putService", [value]))

    @jsii.member(jsii_name="resetLogConfiguration")
    def reset_log_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogConfiguration", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @builtins.property
    @jsii.member(jsii_name="logConfiguration")
    def log_configuration(
        self,
    ) -> EcsServiceServiceConnectConfigurationLogConfigurationOutputReference:
        return typing.cast(EcsServiceServiceConnectConfigurationLogConfigurationOutputReference, jsii.get(self, "logConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> "EcsServiceServiceConnectConfigurationServiceOutputReference":
        return typing.cast("EcsServiceServiceConnectConfigurationServiceOutputReference", jsii.get(self, "service"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logConfigurationInput")
    def log_configuration_input(
        self,
    ) -> typing.Optional[EcsServiceServiceConnectConfigurationLogConfiguration]:
        return typing.cast(typing.Optional[EcsServiceServiceConnectConfigurationLogConfiguration], jsii.get(self, "logConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(
        self,
    ) -> typing.Optional["EcsServiceServiceConnectConfigurationService"]:
        return typing.cast(typing.Optional["EcsServiceServiceConnectConfigurationService"], jsii.get(self, "serviceInput"))

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
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsServiceServiceConnectConfiguration]:
        return typing.cast(typing.Optional[EcsServiceServiceConnectConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceServiceConnectConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[EcsServiceServiceConnectConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceServiceConnectConfigurationService",
    jsii_struct_bases=[],
    name_mapping={
        "client_alias": "clientAlias",
        "port_name": "portName",
        "discovery_name": "discoveryName",
        "ingress_port_override": "ingressPortOverride",
    },
)
class EcsServiceServiceConnectConfigurationService:
    def __init__(
        self,
        *,
        client_alias: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EcsServiceServiceConnectConfigurationServiceClientAlias", typing.Dict[str, typing.Any]]]],
        port_name: builtins.str,
        discovery_name: typing.Optional[builtins.str] = None,
        ingress_port_override: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param client_alias: client_alias block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#client_alias EcsService#client_alias}
        :param port_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#port_name EcsService#port_name}.
        :param discovery_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#discovery_name EcsService#discovery_name}.
        :param ingress_port_override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#ingress_port_override EcsService#ingress_port_override}.
        '''
        if __debug__:
            def stub(
                *,
                client_alias: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServiceServiceConnectConfigurationServiceClientAlias, typing.Dict[str, typing.Any]]]],
                port_name: builtins.str,
                discovery_name: typing.Optional[builtins.str] = None,
                ingress_port_override: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument client_alias", value=client_alias, expected_type=type_hints["client_alias"])
            check_type(argname="argument port_name", value=port_name, expected_type=type_hints["port_name"])
            check_type(argname="argument discovery_name", value=discovery_name, expected_type=type_hints["discovery_name"])
            check_type(argname="argument ingress_port_override", value=ingress_port_override, expected_type=type_hints["ingress_port_override"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_alias": client_alias,
            "port_name": port_name,
        }
        if discovery_name is not None:
            self._values["discovery_name"] = discovery_name
        if ingress_port_override is not None:
            self._values["ingress_port_override"] = ingress_port_override

    @builtins.property
    def client_alias(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["EcsServiceServiceConnectConfigurationServiceClientAlias"]]:
        '''client_alias block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#client_alias EcsService#client_alias}
        '''
        result = self._values.get("client_alias")
        assert result is not None, "Required property 'client_alias' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["EcsServiceServiceConnectConfigurationServiceClientAlias"]], result)

    @builtins.property
    def port_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#port_name EcsService#port_name}.'''
        result = self._values.get("port_name")
        assert result is not None, "Required property 'port_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def discovery_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#discovery_name EcsService#discovery_name}.'''
        result = self._values.get("discovery_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingress_port_override(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#ingress_port_override EcsService#ingress_port_override}.'''
        result = self._values.get("ingress_port_override")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceServiceConnectConfigurationService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceServiceConnectConfigurationServiceClientAlias",
    jsii_struct_bases=[],
    name_mapping={"port": "port", "dns_name": "dnsName"},
)
class EcsServiceServiceConnectConfigurationServiceClientAlias:
    def __init__(
        self,
        *,
        port: jsii.Number,
        dns_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#port EcsService#port}.
        :param dns_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#dns_name EcsService#dns_name}.
        '''
        if __debug__:
            def stub(
                *,
                port: jsii.Number,
                dns_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument dns_name", value=dns_name, expected_type=type_hints["dns_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "port": port,
        }
        if dns_name is not None:
            self._values["dns_name"] = dns_name

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#port EcsService#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def dns_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#dns_name EcsService#dns_name}.'''
        result = self._values.get("dns_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceServiceConnectConfigurationServiceClientAlias(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceServiceConnectConfigurationServiceClientAliasList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceServiceConnectConfigurationServiceClientAliasList",
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
    ) -> "EcsServiceServiceConnectConfigurationServiceClientAliasOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsServiceServiceConnectConfigurationServiceClientAliasOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceServiceConnectConfigurationServiceClientAlias]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceServiceConnectConfigurationServiceClientAlias]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceServiceConnectConfigurationServiceClientAlias]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceServiceConnectConfigurationServiceClientAlias]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsServiceServiceConnectConfigurationServiceClientAliasOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceServiceConnectConfigurationServiceClientAliasOutputReference",
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

    @jsii.member(jsii_name="resetDnsName")
    def reset_dns_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsName", []))

    @builtins.property
    @jsii.member(jsii_name="dnsNameInput")
    def dns_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsNameInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

    @dns_name.setter
    def dns_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsName", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsServiceServiceConnectConfigurationServiceClientAlias, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsServiceServiceConnectConfigurationServiceClientAlias, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsServiceServiceConnectConfigurationServiceClientAlias, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EcsServiceServiceConnectConfigurationServiceClientAlias, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EcsServiceServiceConnectConfigurationServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceServiceConnectConfigurationServiceOutputReference",
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

    @jsii.member(jsii_name="putClientAlias")
    def put_client_alias(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServiceServiceConnectConfigurationServiceClientAlias, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EcsServiceServiceConnectConfigurationServiceClientAlias, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putClientAlias", [value]))

    @jsii.member(jsii_name="resetDiscoveryName")
    def reset_discovery_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiscoveryName", []))

    @jsii.member(jsii_name="resetIngressPortOverride")
    def reset_ingress_port_override(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressPortOverride", []))

    @builtins.property
    @jsii.member(jsii_name="clientAlias")
    def client_alias(
        self,
    ) -> EcsServiceServiceConnectConfigurationServiceClientAliasList:
        return typing.cast(EcsServiceServiceConnectConfigurationServiceClientAliasList, jsii.get(self, "clientAlias"))

    @builtins.property
    @jsii.member(jsii_name="clientAliasInput")
    def client_alias_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceServiceConnectConfigurationServiceClientAlias]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EcsServiceServiceConnectConfigurationServiceClientAlias]]], jsii.get(self, "clientAliasInput"))

    @builtins.property
    @jsii.member(jsii_name="discoveryNameInput")
    def discovery_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "discoveryNameInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressPortOverrideInput")
    def ingress_port_override_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ingressPortOverrideInput"))

    @builtins.property
    @jsii.member(jsii_name="portNameInput")
    def port_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portNameInput"))

    @builtins.property
    @jsii.member(jsii_name="discoveryName")
    def discovery_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "discoveryName"))

    @discovery_name.setter
    def discovery_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "discoveryName", value)

    @builtins.property
    @jsii.member(jsii_name="ingressPortOverride")
    def ingress_port_override(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ingressPortOverride"))

    @ingress_port_override.setter
    def ingress_port_override(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressPortOverride", value)

    @builtins.property
    @jsii.member(jsii_name="portName")
    def port_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portName"))

    @port_name.setter
    def port_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsServiceServiceConnectConfigurationService]:
        return typing.cast(typing.Optional[EcsServiceServiceConnectConfigurationService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceServiceConnectConfigurationService],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[EcsServiceServiceConnectConfigurationService],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceServiceRegistries",
    jsii_struct_bases=[],
    name_mapping={
        "registry_arn": "registryArn",
        "container_name": "containerName",
        "container_port": "containerPort",
        "port": "port",
    },
)
class EcsServiceServiceRegistries:
    def __init__(
        self,
        *,
        registry_arn: builtins.str,
        container_name: typing.Optional[builtins.str] = None,
        container_port: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param registry_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#registry_arn EcsService#registry_arn}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_name EcsService#container_name}.
        :param container_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_port EcsService#container_port}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#port EcsService#port}.
        '''
        if __debug__:
            def stub(
                *,
                registry_arn: builtins.str,
                container_name: typing.Optional[builtins.str] = None,
                container_port: typing.Optional[jsii.Number] = None,
                port: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument registry_arn", value=registry_arn, expected_type=type_hints["registry_arn"])
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument container_port", value=container_port, expected_type=type_hints["container_port"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[str, typing.Any] = {
            "registry_arn": registry_arn,
        }
        if container_name is not None:
            self._values["container_name"] = container_name
        if container_port is not None:
            self._values["container_port"] = container_port
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def registry_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#registry_arn EcsService#registry_arn}.'''
        result = self._values.get("registry_arn")
        assert result is not None, "Required property 'registry_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_name EcsService#container_name}.'''
        result = self._values.get("container_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#container_port EcsService#container_port}.'''
        result = self._values.get("container_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#port EcsService#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceServiceRegistries(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceServiceRegistriesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceServiceRegistriesOutputReference",
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

    @jsii.member(jsii_name="resetContainerName")
    def reset_container_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerName", []))

    @jsii.member(jsii_name="resetContainerPort")
    def reset_container_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerPort", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="containerPortInput")
    def container_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "containerPortInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="registryArnInput")
    def registry_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryArnInput"))

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="containerPort")
    def container_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerPort"))

    @container_port.setter
    def container_port(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerPort", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="registryArn")
    def registry_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registryArn"))

    @registry_arn.setter
    def registry_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsServiceServiceRegistries]:
        return typing.cast(typing.Optional[EcsServiceServiceRegistries], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceServiceRegistries],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[EcsServiceServiceRegistries]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class EcsServiceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#create EcsService#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#delete EcsService#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#update EcsService#update}.
        '''
        if __debug__:
            def stub(
                *,
                create: typing.Optional[builtins.str] = None,
                delete: typing.Optional[builtins.str] = None,
                update: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#create EcsService#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#delete EcsService#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ecs_service#update EcsService#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.ecsService.EcsServiceTimeoutsOutputReference",
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

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EcsServiceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EcsServiceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EcsServiceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[EcsServiceTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "EcsService",
    "EcsServiceCapacityProviderStrategy",
    "EcsServiceCapacityProviderStrategyList",
    "EcsServiceCapacityProviderStrategyOutputReference",
    "EcsServiceConfig",
    "EcsServiceDeploymentCircuitBreaker",
    "EcsServiceDeploymentCircuitBreakerOutputReference",
    "EcsServiceDeploymentController",
    "EcsServiceDeploymentControllerOutputReference",
    "EcsServiceLoadBalancer",
    "EcsServiceLoadBalancerList",
    "EcsServiceLoadBalancerOutputReference",
    "EcsServiceNetworkConfiguration",
    "EcsServiceNetworkConfigurationOutputReference",
    "EcsServiceOrderedPlacementStrategy",
    "EcsServiceOrderedPlacementStrategyList",
    "EcsServiceOrderedPlacementStrategyOutputReference",
    "EcsServicePlacementConstraints",
    "EcsServicePlacementConstraintsList",
    "EcsServicePlacementConstraintsOutputReference",
    "EcsServiceServiceConnectConfiguration",
    "EcsServiceServiceConnectConfigurationLogConfiguration",
    "EcsServiceServiceConnectConfigurationLogConfigurationOutputReference",
    "EcsServiceServiceConnectConfigurationLogConfigurationSecretOption",
    "EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionList",
    "EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionOutputReference",
    "EcsServiceServiceConnectConfigurationOutputReference",
    "EcsServiceServiceConnectConfigurationService",
    "EcsServiceServiceConnectConfigurationServiceClientAlias",
    "EcsServiceServiceConnectConfigurationServiceClientAliasList",
    "EcsServiceServiceConnectConfigurationServiceClientAliasOutputReference",
    "EcsServiceServiceConnectConfigurationServiceOutputReference",
    "EcsServiceServiceRegistries",
    "EcsServiceServiceRegistriesOutputReference",
    "EcsServiceTimeouts",
    "EcsServiceTimeoutsOutputReference",
]

publication.publish()
