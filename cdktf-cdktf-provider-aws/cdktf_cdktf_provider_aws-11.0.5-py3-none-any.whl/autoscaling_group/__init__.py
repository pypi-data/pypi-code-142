'''
# `aws_autoscaling_group`

Refer to the Terraform Registory for docs: [`aws_autoscaling_group`](https://www.terraform.io/docs/providers/aws/r/autoscaling_group).
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


class AutoscalingGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group aws_autoscaling_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        max_size: jsii.Number,
        min_size: jsii.Number,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        capacity_rebalance: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        context: typing.Optional[builtins.str] = None,
        default_cooldown: typing.Optional[jsii.Number] = None,
        default_instance_warmup: typing.Optional[jsii.Number] = None,
        desired_capacity: typing.Optional[jsii.Number] = None,
        enabled_metrics: typing.Optional[typing.Sequence[builtins.str]] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        force_delete_warm_pool: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_check_grace_period: typing.Optional[jsii.Number] = None,
        health_check_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        initial_lifecycle_hook: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingGroupInitialLifecycleHook", typing.Dict[str, typing.Any]]]]] = None,
        instance_refresh: typing.Optional[typing.Union["AutoscalingGroupInstanceRefresh", typing.Dict[str, typing.Any]]] = None,
        launch_configuration: typing.Optional[builtins.str] = None,
        launch_template: typing.Optional[typing.Union["AutoscalingGroupLaunchTemplate", typing.Dict[str, typing.Any]]] = None,
        load_balancers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_instance_lifetime: typing.Optional[jsii.Number] = None,
        metrics_granularity: typing.Optional[builtins.str] = None,
        min_elb_capacity: typing.Optional[jsii.Number] = None,
        mixed_instances_policy: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicy", typing.Dict[str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        placement_group: typing.Optional[builtins.str] = None,
        protect_from_scale_in: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        service_linked_role_arn: typing.Optional[builtins.str] = None,
        suspended_processes: typing.Optional[typing.Sequence[builtins.str]] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingGroupTag", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target_group_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        termination_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["AutoscalingGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpc_zone_identifier: typing.Optional[typing.Sequence[builtins.str]] = None,
        wait_for_capacity_timeout: typing.Optional[builtins.str] = None,
        wait_for_elb_capacity: typing.Optional[jsii.Number] = None,
        warm_pool: typing.Optional[typing.Union["AutoscalingGroupWarmPool", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group aws_autoscaling_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max_size AutoscalingGroup#max_size}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_size AutoscalingGroup#min_size}.
        :param availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#availability_zones AutoscalingGroup#availability_zones}.
        :param capacity_rebalance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#capacity_rebalance AutoscalingGroup#capacity_rebalance}.
        :param context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#context AutoscalingGroup#context}.
        :param default_cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#default_cooldown AutoscalingGroup#default_cooldown}.
        :param default_instance_warmup: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#default_instance_warmup AutoscalingGroup#default_instance_warmup}.
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#desired_capacity AutoscalingGroup#desired_capacity}.
        :param enabled_metrics: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#enabled_metrics AutoscalingGroup#enabled_metrics}.
        :param force_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#force_delete AutoscalingGroup#force_delete}.
        :param force_delete_warm_pool: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#force_delete_warm_pool AutoscalingGroup#force_delete_warm_pool}.
        :param health_check_grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#health_check_grace_period AutoscalingGroup#health_check_grace_period}.
        :param health_check_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#health_check_type AutoscalingGroup#health_check_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#id AutoscalingGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_lifecycle_hook: initial_lifecycle_hook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#initial_lifecycle_hook AutoscalingGroup#initial_lifecycle_hook}
        :param instance_refresh: instance_refresh block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_refresh AutoscalingGroup#instance_refresh}
        :param launch_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_configuration AutoscalingGroup#launch_configuration}.
        :param launch_template: launch_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template AutoscalingGroup#launch_template}
        :param load_balancers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#load_balancers AutoscalingGroup#load_balancers}.
        :param max_instance_lifetime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max_instance_lifetime AutoscalingGroup#max_instance_lifetime}.
        :param metrics_granularity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#metrics_granularity AutoscalingGroup#metrics_granularity}.
        :param min_elb_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_elb_capacity AutoscalingGroup#min_elb_capacity}.
        :param mixed_instances_policy: mixed_instances_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#mixed_instances_policy AutoscalingGroup#mixed_instances_policy}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name AutoscalingGroup#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name_prefix AutoscalingGroup#name_prefix}.
        :param placement_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#placement_group AutoscalingGroup#placement_group}.
        :param protect_from_scale_in: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#protect_from_scale_in AutoscalingGroup#protect_from_scale_in}.
        :param service_linked_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#service_linked_role_arn AutoscalingGroup#service_linked_role_arn}.
        :param suspended_processes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#suspended_processes AutoscalingGroup#suspended_processes}.
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#tag AutoscalingGroup#tag}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#tags AutoscalingGroup#tags}.
        :param target_group_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#target_group_arns AutoscalingGroup#target_group_arns}.
        :param termination_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#termination_policies AutoscalingGroup#termination_policies}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#timeouts AutoscalingGroup#timeouts}
        :param vpc_zone_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#vpc_zone_identifier AutoscalingGroup#vpc_zone_identifier}.
        :param wait_for_capacity_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#wait_for_capacity_timeout AutoscalingGroup#wait_for_capacity_timeout}.
        :param wait_for_elb_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#wait_for_elb_capacity AutoscalingGroup#wait_for_elb_capacity}.
        :param warm_pool: warm_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#warm_pool AutoscalingGroup#warm_pool}
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
                max_size: jsii.Number,
                min_size: jsii.Number,
                availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
                capacity_rebalance: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                context: typing.Optional[builtins.str] = None,
                default_cooldown: typing.Optional[jsii.Number] = None,
                default_instance_warmup: typing.Optional[jsii.Number] = None,
                desired_capacity: typing.Optional[jsii.Number] = None,
                enabled_metrics: typing.Optional[typing.Sequence[builtins.str]] = None,
                force_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                force_delete_warm_pool: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                health_check_grace_period: typing.Optional[jsii.Number] = None,
                health_check_type: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                initial_lifecycle_hook: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingGroupInitialLifecycleHook, typing.Dict[str, typing.Any]]]]] = None,
                instance_refresh: typing.Optional[typing.Union[AutoscalingGroupInstanceRefresh, typing.Dict[str, typing.Any]]] = None,
                launch_configuration: typing.Optional[builtins.str] = None,
                launch_template: typing.Optional[typing.Union[AutoscalingGroupLaunchTemplate, typing.Dict[str, typing.Any]]] = None,
                load_balancers: typing.Optional[typing.Sequence[builtins.str]] = None,
                max_instance_lifetime: typing.Optional[jsii.Number] = None,
                metrics_granularity: typing.Optional[builtins.str] = None,
                min_elb_capacity: typing.Optional[jsii.Number] = None,
                mixed_instances_policy: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicy, typing.Dict[str, typing.Any]]] = None,
                name: typing.Optional[builtins.str] = None,
                name_prefix: typing.Optional[builtins.str] = None,
                placement_group: typing.Optional[builtins.str] = None,
                protect_from_scale_in: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                service_linked_role_arn: typing.Optional[builtins.str] = None,
                suspended_processes: typing.Optional[typing.Sequence[builtins.str]] = None,
                tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingGroupTag, typing.Dict[str, typing.Any]]]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                target_group_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
                termination_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[AutoscalingGroupTimeouts, typing.Dict[str, typing.Any]]] = None,
                vpc_zone_identifier: typing.Optional[typing.Sequence[builtins.str]] = None,
                wait_for_capacity_timeout: typing.Optional[builtins.str] = None,
                wait_for_elb_capacity: typing.Optional[jsii.Number] = None,
                warm_pool: typing.Optional[typing.Union[AutoscalingGroupWarmPool, typing.Dict[str, typing.Any]]] = None,
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
        config = AutoscalingGroupConfig(
            max_size=max_size,
            min_size=min_size,
            availability_zones=availability_zones,
            capacity_rebalance=capacity_rebalance,
            context=context,
            default_cooldown=default_cooldown,
            default_instance_warmup=default_instance_warmup,
            desired_capacity=desired_capacity,
            enabled_metrics=enabled_metrics,
            force_delete=force_delete,
            force_delete_warm_pool=force_delete_warm_pool,
            health_check_grace_period=health_check_grace_period,
            health_check_type=health_check_type,
            id=id,
            initial_lifecycle_hook=initial_lifecycle_hook,
            instance_refresh=instance_refresh,
            launch_configuration=launch_configuration,
            launch_template=launch_template,
            load_balancers=load_balancers,
            max_instance_lifetime=max_instance_lifetime,
            metrics_granularity=metrics_granularity,
            min_elb_capacity=min_elb_capacity,
            mixed_instances_policy=mixed_instances_policy,
            name=name,
            name_prefix=name_prefix,
            placement_group=placement_group,
            protect_from_scale_in=protect_from_scale_in,
            service_linked_role_arn=service_linked_role_arn,
            suspended_processes=suspended_processes,
            tag=tag,
            tags=tags,
            target_group_arns=target_group_arns,
            termination_policies=termination_policies,
            timeouts=timeouts,
            vpc_zone_identifier=vpc_zone_identifier,
            wait_for_capacity_timeout=wait_for_capacity_timeout,
            wait_for_elb_capacity=wait_for_elb_capacity,
            warm_pool=warm_pool,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putInitialLifecycleHook")
    def put_initial_lifecycle_hook(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingGroupInitialLifecycleHook", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingGroupInitialLifecycleHook, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInitialLifecycleHook", [value]))

    @jsii.member(jsii_name="putInstanceRefresh")
    def put_instance_refresh(
        self,
        *,
        strategy: builtins.str,
        preferences: typing.Optional[typing.Union["AutoscalingGroupInstanceRefreshPreferences", typing.Dict[str, typing.Any]]] = None,
        triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#strategy AutoscalingGroup#strategy}.
        :param preferences: preferences block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#preferences AutoscalingGroup#preferences}
        :param triggers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#triggers AutoscalingGroup#triggers}.
        '''
        value = AutoscalingGroupInstanceRefresh(
            strategy=strategy, preferences=preferences, triggers=triggers
        )

        return typing.cast(None, jsii.invoke(self, "putInstanceRefresh", [value]))

    @jsii.member(jsii_name="putLaunchTemplate")
    def put_launch_template(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#id AutoscalingGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name AutoscalingGroup#name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#version AutoscalingGroup#version}.
        '''
        value = AutoscalingGroupLaunchTemplate(id=id, name=name, version=version)

        return typing.cast(None, jsii.invoke(self, "putLaunchTemplate", [value]))

    @jsii.member(jsii_name="putMixedInstancesPolicy")
    def put_mixed_instances_policy(
        self,
        *,
        launch_template: typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplate", typing.Dict[str, typing.Any]],
        instances_distribution: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyInstancesDistribution", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param launch_template: launch_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template AutoscalingGroup#launch_template}
        :param instances_distribution: instances_distribution block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instances_distribution AutoscalingGroup#instances_distribution}
        '''
        value = AutoscalingGroupMixedInstancesPolicy(
            launch_template=launch_template,
            instances_distribution=instances_distribution,
        )

        return typing.cast(None, jsii.invoke(self, "putMixedInstancesPolicy", [value]))

    @jsii.member(jsii_name="putTag")
    def put_tag(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingGroupTag", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingGroupTag, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTag", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#delete AutoscalingGroup#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#update AutoscalingGroup#update}.
        '''
        value = AutoscalingGroupTimeouts(delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWarmPool")
    def put_warm_pool(
        self,
        *,
        instance_reuse_policy: typing.Optional[typing.Union["AutoscalingGroupWarmPoolInstanceReusePolicy", typing.Dict[str, typing.Any]]] = None,
        max_group_prepared_capacity: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        pool_state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_reuse_policy: instance_reuse_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_reuse_policy AutoscalingGroup#instance_reuse_policy}
        :param max_group_prepared_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max_group_prepared_capacity AutoscalingGroup#max_group_prepared_capacity}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_size AutoscalingGroup#min_size}.
        :param pool_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#pool_state AutoscalingGroup#pool_state}.
        '''
        value = AutoscalingGroupWarmPool(
            instance_reuse_policy=instance_reuse_policy,
            max_group_prepared_capacity=max_group_prepared_capacity,
            min_size=min_size,
            pool_state=pool_state,
        )

        return typing.cast(None, jsii.invoke(self, "putWarmPool", [value]))

    @jsii.member(jsii_name="resetAvailabilityZones")
    def reset_availability_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityZones", []))

    @jsii.member(jsii_name="resetCapacityRebalance")
    def reset_capacity_rebalance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityRebalance", []))

    @jsii.member(jsii_name="resetContext")
    def reset_context(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContext", []))

    @jsii.member(jsii_name="resetDefaultCooldown")
    def reset_default_cooldown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultCooldown", []))

    @jsii.member(jsii_name="resetDefaultInstanceWarmup")
    def reset_default_instance_warmup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultInstanceWarmup", []))

    @jsii.member(jsii_name="resetDesiredCapacity")
    def reset_desired_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredCapacity", []))

    @jsii.member(jsii_name="resetEnabledMetrics")
    def reset_enabled_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabledMetrics", []))

    @jsii.member(jsii_name="resetForceDelete")
    def reset_force_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDelete", []))

    @jsii.member(jsii_name="resetForceDeleteWarmPool")
    def reset_force_delete_warm_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDeleteWarmPool", []))

    @jsii.member(jsii_name="resetHealthCheckGracePeriod")
    def reset_health_check_grace_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckGracePeriod", []))

    @jsii.member(jsii_name="resetHealthCheckType")
    def reset_health_check_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckType", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInitialLifecycleHook")
    def reset_initial_lifecycle_hook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialLifecycleHook", []))

    @jsii.member(jsii_name="resetInstanceRefresh")
    def reset_instance_refresh(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceRefresh", []))

    @jsii.member(jsii_name="resetLaunchConfiguration")
    def reset_launch_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchConfiguration", []))

    @jsii.member(jsii_name="resetLaunchTemplate")
    def reset_launch_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplate", []))

    @jsii.member(jsii_name="resetLoadBalancers")
    def reset_load_balancers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancers", []))

    @jsii.member(jsii_name="resetMaxInstanceLifetime")
    def reset_max_instance_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxInstanceLifetime", []))

    @jsii.member(jsii_name="resetMetricsGranularity")
    def reset_metrics_granularity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsGranularity", []))

    @jsii.member(jsii_name="resetMinElbCapacity")
    def reset_min_elb_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinElbCapacity", []))

    @jsii.member(jsii_name="resetMixedInstancesPolicy")
    def reset_mixed_instances_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMixedInstancesPolicy", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="resetPlacementGroup")
    def reset_placement_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacementGroup", []))

    @jsii.member(jsii_name="resetProtectFromScaleIn")
    def reset_protect_from_scale_in(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtectFromScaleIn", []))

    @jsii.member(jsii_name="resetServiceLinkedRoleArn")
    def reset_service_linked_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceLinkedRoleArn", []))

    @jsii.member(jsii_name="resetSuspendedProcesses")
    def reset_suspended_processes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuspendedProcesses", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTargetGroupArns")
    def reset_target_group_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetGroupArns", []))

    @jsii.member(jsii_name="resetTerminationPolicies")
    def reset_termination_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminationPolicies", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVpcZoneIdentifier")
    def reset_vpc_zone_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcZoneIdentifier", []))

    @jsii.member(jsii_name="resetWaitForCapacityTimeout")
    def reset_wait_for_capacity_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForCapacityTimeout", []))

    @jsii.member(jsii_name="resetWaitForElbCapacity")
    def reset_wait_for_elb_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForElbCapacity", []))

    @jsii.member(jsii_name="resetWarmPool")
    def reset_warm_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarmPool", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="initialLifecycleHook")
    def initial_lifecycle_hook(self) -> "AutoscalingGroupInitialLifecycleHookList":
        return typing.cast("AutoscalingGroupInitialLifecycleHookList", jsii.get(self, "initialLifecycleHook"))

    @builtins.property
    @jsii.member(jsii_name="instanceRefresh")
    def instance_refresh(self) -> "AutoscalingGroupInstanceRefreshOutputReference":
        return typing.cast("AutoscalingGroupInstanceRefreshOutputReference", jsii.get(self, "instanceRefresh"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplate")
    def launch_template(self) -> "AutoscalingGroupLaunchTemplateOutputReference":
        return typing.cast("AutoscalingGroupLaunchTemplateOutputReference", jsii.get(self, "launchTemplate"))

    @builtins.property
    @jsii.member(jsii_name="mixedInstancesPolicy")
    def mixed_instances_policy(
        self,
    ) -> "AutoscalingGroupMixedInstancesPolicyOutputReference":
        return typing.cast("AutoscalingGroupMixedInstancesPolicyOutputReference", jsii.get(self, "mixedInstancesPolicy"))

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> "AutoscalingGroupTagList":
        return typing.cast("AutoscalingGroupTagList", jsii.get(self, "tag"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "AutoscalingGroupTimeoutsOutputReference":
        return typing.cast("AutoscalingGroupTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="warmPool")
    def warm_pool(self) -> "AutoscalingGroupWarmPoolOutputReference":
        return typing.cast("AutoscalingGroupWarmPoolOutputReference", jsii.get(self, "warmPool"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZonesInput")
    def availability_zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "availabilityZonesInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityRebalanceInput")
    def capacity_rebalance_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "capacityRebalanceInput"))

    @builtins.property
    @jsii.member(jsii_name="contextInput")
    def context_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contextInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultCooldownInput")
    def default_cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultCooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultInstanceWarmupInput")
    def default_instance_warmup_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultInstanceWarmupInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredCapacityInput")
    def desired_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "desiredCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledMetricsInput")
    def enabled_metrics_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "enabledMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDeleteInput")
    def force_delete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceDeleteInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDeleteWarmPoolInput")
    def force_delete_warm_pool_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceDeleteWarmPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckGracePeriodInput")
    def health_check_grace_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthCheckGracePeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckTypeInput")
    def health_check_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="initialLifecycleHookInput")
    def initial_lifecycle_hook_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupInitialLifecycleHook"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupInitialLifecycleHook"]]], jsii.get(self, "initialLifecycleHookInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceRefreshInput")
    def instance_refresh_input(
        self,
    ) -> typing.Optional["AutoscalingGroupInstanceRefresh"]:
        return typing.cast(typing.Optional["AutoscalingGroupInstanceRefresh"], jsii.get(self, "instanceRefreshInput"))

    @builtins.property
    @jsii.member(jsii_name="launchConfigurationInput")
    def launch_configuration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateInput")
    def launch_template_input(
        self,
    ) -> typing.Optional["AutoscalingGroupLaunchTemplate"]:
        return typing.cast(typing.Optional["AutoscalingGroupLaunchTemplate"], jsii.get(self, "launchTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancersInput")
    def load_balancers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loadBalancersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxInstanceLifetimeInput")
    def max_instance_lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInstanceLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSizeInput")
    def max_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsGranularityInput")
    def metrics_granularity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricsGranularityInput"))

    @builtins.property
    @jsii.member(jsii_name="minElbCapacityInput")
    def min_elb_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minElbCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="minSizeInput")
    def min_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="mixedInstancesPolicyInput")
    def mixed_instances_policy_input(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicy"]:
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicy"], jsii.get(self, "mixedInstancesPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="placementGroupInput")
    def placement_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "placementGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="protectFromScaleInInput")
    def protect_from_scale_in_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "protectFromScaleInInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceLinkedRoleArnInput")
    def service_linked_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceLinkedRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="suspendedProcessesInput")
    def suspended_processes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "suspendedProcessesInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupTag"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupTag"]]], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupArnsInput")
    def target_group_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetGroupArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="terminationPoliciesInput")
    def termination_policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "terminationPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["AutoscalingGroupTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["AutoscalingGroupTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcZoneIdentifierInput")
    def vpc_zone_identifier_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcZoneIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForCapacityTimeoutInput")
    def wait_for_capacity_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "waitForCapacityTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForElbCapacityInput")
    def wait_for_elb_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "waitForElbCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="warmPoolInput")
    def warm_pool_input(self) -> typing.Optional["AutoscalingGroupWarmPool"]:
        return typing.cast(typing.Optional["AutoscalingGroupWarmPool"], jsii.get(self, "warmPoolInput"))

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
    @jsii.member(jsii_name="capacityRebalance")
    def capacity_rebalance(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "capacityRebalance"))

    @capacity_rebalance.setter
    def capacity_rebalance(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityRebalance", value)

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "context"))

    @context.setter
    def context(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "context", value)

    @builtins.property
    @jsii.member(jsii_name="defaultCooldown")
    def default_cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultCooldown"))

    @default_cooldown.setter
    def default_cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultCooldown", value)

    @builtins.property
    @jsii.member(jsii_name="defaultInstanceWarmup")
    def default_instance_warmup(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultInstanceWarmup"))

    @default_instance_warmup.setter
    def default_instance_warmup(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultInstanceWarmup", value)

    @builtins.property
    @jsii.member(jsii_name="desiredCapacity")
    def desired_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredCapacity"))

    @desired_capacity.setter
    def desired_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="enabledMetrics")
    def enabled_metrics(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "enabledMetrics"))

    @enabled_metrics.setter
    def enabled_metrics(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledMetrics", value)

    @builtins.property
    @jsii.member(jsii_name="forceDelete")
    def force_delete(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forceDelete"))

    @force_delete.setter
    def force_delete(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDelete", value)

    @builtins.property
    @jsii.member(jsii_name="forceDeleteWarmPool")
    def force_delete_warm_pool(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forceDeleteWarmPool"))

    @force_delete_warm_pool.setter
    def force_delete_warm_pool(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDeleteWarmPool", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckGracePeriod")
    def health_check_grace_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthCheckGracePeriod"))

    @health_check_grace_period.setter
    def health_check_grace_period(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckGracePeriod", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckType")
    def health_check_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckType"))

    @health_check_type.setter
    def health_check_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckType", value)

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
    @jsii.member(jsii_name="launchConfiguration")
    def launch_configuration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchConfiguration"))

    @launch_configuration.setter
    def launch_configuration(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancers")
    def load_balancers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loadBalancers"))

    @load_balancers.setter
    def load_balancers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancers", value)

    @builtins.property
    @jsii.member(jsii_name="maxInstanceLifetime")
    def max_instance_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxInstanceLifetime"))

    @max_instance_lifetime.setter
    def max_instance_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxInstanceLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSize"))

    @max_size.setter
    def max_size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSize", value)

    @builtins.property
    @jsii.member(jsii_name="metricsGranularity")
    def metrics_granularity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricsGranularity"))

    @metrics_granularity.setter
    def metrics_granularity(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsGranularity", value)

    @builtins.property
    @jsii.member(jsii_name="minElbCapacity")
    def min_elb_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minElbCapacity"))

    @min_elb_capacity.setter
    def min_elb_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minElbCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minSize"))

    @min_size.setter
    def min_size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minSize", value)

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
    @jsii.member(jsii_name="placementGroup")
    def placement_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "placementGroup"))

    @placement_group.setter
    def placement_group(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placementGroup", value)

    @builtins.property
    @jsii.member(jsii_name="protectFromScaleIn")
    def protect_from_scale_in(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "protectFromScaleIn"))

    @protect_from_scale_in.setter
    def protect_from_scale_in(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectFromScaleIn", value)

    @builtins.property
    @jsii.member(jsii_name="serviceLinkedRoleArn")
    def service_linked_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceLinkedRoleArn"))

    @service_linked_role_arn.setter
    def service_linked_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceLinkedRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="suspendedProcesses")
    def suspended_processes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "suspendedProcesses"))

    @suspended_processes.setter
    def suspended_processes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suspendedProcesses", value)

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
    @jsii.member(jsii_name="targetGroupArns")
    def target_group_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetGroupArns"))

    @target_group_arns.setter
    def target_group_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetGroupArns", value)

    @builtins.property
    @jsii.member(jsii_name="terminationPolicies")
    def termination_policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "terminationPolicies"))

    @termination_policies.setter
    def termination_policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terminationPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="vpcZoneIdentifier")
    def vpc_zone_identifier(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vpcZoneIdentifier"))

    @vpc_zone_identifier.setter
    def vpc_zone_identifier(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcZoneIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="waitForCapacityTimeout")
    def wait_for_capacity_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "waitForCapacityTimeout"))

    @wait_for_capacity_timeout.setter
    def wait_for_capacity_timeout(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForCapacityTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="waitForElbCapacity")
    def wait_for_elb_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "waitForElbCapacity"))

    @wait_for_elb_capacity.setter
    def wait_for_elb_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForElbCapacity", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "max_size": "maxSize",
        "min_size": "minSize",
        "availability_zones": "availabilityZones",
        "capacity_rebalance": "capacityRebalance",
        "context": "context",
        "default_cooldown": "defaultCooldown",
        "default_instance_warmup": "defaultInstanceWarmup",
        "desired_capacity": "desiredCapacity",
        "enabled_metrics": "enabledMetrics",
        "force_delete": "forceDelete",
        "force_delete_warm_pool": "forceDeleteWarmPool",
        "health_check_grace_period": "healthCheckGracePeriod",
        "health_check_type": "healthCheckType",
        "id": "id",
        "initial_lifecycle_hook": "initialLifecycleHook",
        "instance_refresh": "instanceRefresh",
        "launch_configuration": "launchConfiguration",
        "launch_template": "launchTemplate",
        "load_balancers": "loadBalancers",
        "max_instance_lifetime": "maxInstanceLifetime",
        "metrics_granularity": "metricsGranularity",
        "min_elb_capacity": "minElbCapacity",
        "mixed_instances_policy": "mixedInstancesPolicy",
        "name": "name",
        "name_prefix": "namePrefix",
        "placement_group": "placementGroup",
        "protect_from_scale_in": "protectFromScaleIn",
        "service_linked_role_arn": "serviceLinkedRoleArn",
        "suspended_processes": "suspendedProcesses",
        "tag": "tag",
        "tags": "tags",
        "target_group_arns": "targetGroupArns",
        "termination_policies": "terminationPolicies",
        "timeouts": "timeouts",
        "vpc_zone_identifier": "vpcZoneIdentifier",
        "wait_for_capacity_timeout": "waitForCapacityTimeout",
        "wait_for_elb_capacity": "waitForElbCapacity",
        "warm_pool": "warmPool",
    },
)
class AutoscalingGroupConfig(cdktf.TerraformMetaArguments):
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
        max_size: jsii.Number,
        min_size: jsii.Number,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        capacity_rebalance: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        context: typing.Optional[builtins.str] = None,
        default_cooldown: typing.Optional[jsii.Number] = None,
        default_instance_warmup: typing.Optional[jsii.Number] = None,
        desired_capacity: typing.Optional[jsii.Number] = None,
        enabled_metrics: typing.Optional[typing.Sequence[builtins.str]] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        force_delete_warm_pool: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_check_grace_period: typing.Optional[jsii.Number] = None,
        health_check_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        initial_lifecycle_hook: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingGroupInitialLifecycleHook", typing.Dict[str, typing.Any]]]]] = None,
        instance_refresh: typing.Optional[typing.Union["AutoscalingGroupInstanceRefresh", typing.Dict[str, typing.Any]]] = None,
        launch_configuration: typing.Optional[builtins.str] = None,
        launch_template: typing.Optional[typing.Union["AutoscalingGroupLaunchTemplate", typing.Dict[str, typing.Any]]] = None,
        load_balancers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_instance_lifetime: typing.Optional[jsii.Number] = None,
        metrics_granularity: typing.Optional[builtins.str] = None,
        min_elb_capacity: typing.Optional[jsii.Number] = None,
        mixed_instances_policy: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicy", typing.Dict[str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        placement_group: typing.Optional[builtins.str] = None,
        protect_from_scale_in: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        service_linked_role_arn: typing.Optional[builtins.str] = None,
        suspended_processes: typing.Optional[typing.Sequence[builtins.str]] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingGroupTag", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target_group_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        termination_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["AutoscalingGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpc_zone_identifier: typing.Optional[typing.Sequence[builtins.str]] = None,
        wait_for_capacity_timeout: typing.Optional[builtins.str] = None,
        wait_for_elb_capacity: typing.Optional[jsii.Number] = None,
        warm_pool: typing.Optional[typing.Union["AutoscalingGroupWarmPool", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param max_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max_size AutoscalingGroup#max_size}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_size AutoscalingGroup#min_size}.
        :param availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#availability_zones AutoscalingGroup#availability_zones}.
        :param capacity_rebalance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#capacity_rebalance AutoscalingGroup#capacity_rebalance}.
        :param context: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#context AutoscalingGroup#context}.
        :param default_cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#default_cooldown AutoscalingGroup#default_cooldown}.
        :param default_instance_warmup: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#default_instance_warmup AutoscalingGroup#default_instance_warmup}.
        :param desired_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#desired_capacity AutoscalingGroup#desired_capacity}.
        :param enabled_metrics: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#enabled_metrics AutoscalingGroup#enabled_metrics}.
        :param force_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#force_delete AutoscalingGroup#force_delete}.
        :param force_delete_warm_pool: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#force_delete_warm_pool AutoscalingGroup#force_delete_warm_pool}.
        :param health_check_grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#health_check_grace_period AutoscalingGroup#health_check_grace_period}.
        :param health_check_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#health_check_type AutoscalingGroup#health_check_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#id AutoscalingGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_lifecycle_hook: initial_lifecycle_hook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#initial_lifecycle_hook AutoscalingGroup#initial_lifecycle_hook}
        :param instance_refresh: instance_refresh block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_refresh AutoscalingGroup#instance_refresh}
        :param launch_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_configuration AutoscalingGroup#launch_configuration}.
        :param launch_template: launch_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template AutoscalingGroup#launch_template}
        :param load_balancers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#load_balancers AutoscalingGroup#load_balancers}.
        :param max_instance_lifetime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max_instance_lifetime AutoscalingGroup#max_instance_lifetime}.
        :param metrics_granularity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#metrics_granularity AutoscalingGroup#metrics_granularity}.
        :param min_elb_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_elb_capacity AutoscalingGroup#min_elb_capacity}.
        :param mixed_instances_policy: mixed_instances_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#mixed_instances_policy AutoscalingGroup#mixed_instances_policy}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name AutoscalingGroup#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name_prefix AutoscalingGroup#name_prefix}.
        :param placement_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#placement_group AutoscalingGroup#placement_group}.
        :param protect_from_scale_in: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#protect_from_scale_in AutoscalingGroup#protect_from_scale_in}.
        :param service_linked_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#service_linked_role_arn AutoscalingGroup#service_linked_role_arn}.
        :param suspended_processes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#suspended_processes AutoscalingGroup#suspended_processes}.
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#tag AutoscalingGroup#tag}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#tags AutoscalingGroup#tags}.
        :param target_group_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#target_group_arns AutoscalingGroup#target_group_arns}.
        :param termination_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#termination_policies AutoscalingGroup#termination_policies}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#timeouts AutoscalingGroup#timeouts}
        :param vpc_zone_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#vpc_zone_identifier AutoscalingGroup#vpc_zone_identifier}.
        :param wait_for_capacity_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#wait_for_capacity_timeout AutoscalingGroup#wait_for_capacity_timeout}.
        :param wait_for_elb_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#wait_for_elb_capacity AutoscalingGroup#wait_for_elb_capacity}.
        :param warm_pool: warm_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#warm_pool AutoscalingGroup#warm_pool}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(instance_refresh, dict):
            instance_refresh = AutoscalingGroupInstanceRefresh(**instance_refresh)
        if isinstance(launch_template, dict):
            launch_template = AutoscalingGroupLaunchTemplate(**launch_template)
        if isinstance(mixed_instances_policy, dict):
            mixed_instances_policy = AutoscalingGroupMixedInstancesPolicy(**mixed_instances_policy)
        if isinstance(timeouts, dict):
            timeouts = AutoscalingGroupTimeouts(**timeouts)
        if isinstance(warm_pool, dict):
            warm_pool = AutoscalingGroupWarmPool(**warm_pool)
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
                max_size: jsii.Number,
                min_size: jsii.Number,
                availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
                capacity_rebalance: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                context: typing.Optional[builtins.str] = None,
                default_cooldown: typing.Optional[jsii.Number] = None,
                default_instance_warmup: typing.Optional[jsii.Number] = None,
                desired_capacity: typing.Optional[jsii.Number] = None,
                enabled_metrics: typing.Optional[typing.Sequence[builtins.str]] = None,
                force_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                force_delete_warm_pool: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                health_check_grace_period: typing.Optional[jsii.Number] = None,
                health_check_type: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                initial_lifecycle_hook: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingGroupInitialLifecycleHook, typing.Dict[str, typing.Any]]]]] = None,
                instance_refresh: typing.Optional[typing.Union[AutoscalingGroupInstanceRefresh, typing.Dict[str, typing.Any]]] = None,
                launch_configuration: typing.Optional[builtins.str] = None,
                launch_template: typing.Optional[typing.Union[AutoscalingGroupLaunchTemplate, typing.Dict[str, typing.Any]]] = None,
                load_balancers: typing.Optional[typing.Sequence[builtins.str]] = None,
                max_instance_lifetime: typing.Optional[jsii.Number] = None,
                metrics_granularity: typing.Optional[builtins.str] = None,
                min_elb_capacity: typing.Optional[jsii.Number] = None,
                mixed_instances_policy: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicy, typing.Dict[str, typing.Any]]] = None,
                name: typing.Optional[builtins.str] = None,
                name_prefix: typing.Optional[builtins.str] = None,
                placement_group: typing.Optional[builtins.str] = None,
                protect_from_scale_in: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                service_linked_role_arn: typing.Optional[builtins.str] = None,
                suspended_processes: typing.Optional[typing.Sequence[builtins.str]] = None,
                tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingGroupTag, typing.Dict[str, typing.Any]]]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                target_group_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
                termination_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[AutoscalingGroupTimeouts, typing.Dict[str, typing.Any]]] = None,
                vpc_zone_identifier: typing.Optional[typing.Sequence[builtins.str]] = None,
                wait_for_capacity_timeout: typing.Optional[builtins.str] = None,
                wait_for_elb_capacity: typing.Optional[jsii.Number] = None,
                warm_pool: typing.Optional[typing.Union[AutoscalingGroupWarmPool, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
            check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            check_type(argname="argument availability_zones", value=availability_zones, expected_type=type_hints["availability_zones"])
            check_type(argname="argument capacity_rebalance", value=capacity_rebalance, expected_type=type_hints["capacity_rebalance"])
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
            check_type(argname="argument default_cooldown", value=default_cooldown, expected_type=type_hints["default_cooldown"])
            check_type(argname="argument default_instance_warmup", value=default_instance_warmup, expected_type=type_hints["default_instance_warmup"])
            check_type(argname="argument desired_capacity", value=desired_capacity, expected_type=type_hints["desired_capacity"])
            check_type(argname="argument enabled_metrics", value=enabled_metrics, expected_type=type_hints["enabled_metrics"])
            check_type(argname="argument force_delete", value=force_delete, expected_type=type_hints["force_delete"])
            check_type(argname="argument force_delete_warm_pool", value=force_delete_warm_pool, expected_type=type_hints["force_delete_warm_pool"])
            check_type(argname="argument health_check_grace_period", value=health_check_grace_period, expected_type=type_hints["health_check_grace_period"])
            check_type(argname="argument health_check_type", value=health_check_type, expected_type=type_hints["health_check_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument initial_lifecycle_hook", value=initial_lifecycle_hook, expected_type=type_hints["initial_lifecycle_hook"])
            check_type(argname="argument instance_refresh", value=instance_refresh, expected_type=type_hints["instance_refresh"])
            check_type(argname="argument launch_configuration", value=launch_configuration, expected_type=type_hints["launch_configuration"])
            check_type(argname="argument launch_template", value=launch_template, expected_type=type_hints["launch_template"])
            check_type(argname="argument load_balancers", value=load_balancers, expected_type=type_hints["load_balancers"])
            check_type(argname="argument max_instance_lifetime", value=max_instance_lifetime, expected_type=type_hints["max_instance_lifetime"])
            check_type(argname="argument metrics_granularity", value=metrics_granularity, expected_type=type_hints["metrics_granularity"])
            check_type(argname="argument min_elb_capacity", value=min_elb_capacity, expected_type=type_hints["min_elb_capacity"])
            check_type(argname="argument mixed_instances_policy", value=mixed_instances_policy, expected_type=type_hints["mixed_instances_policy"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument placement_group", value=placement_group, expected_type=type_hints["placement_group"])
            check_type(argname="argument protect_from_scale_in", value=protect_from_scale_in, expected_type=type_hints["protect_from_scale_in"])
            check_type(argname="argument service_linked_role_arn", value=service_linked_role_arn, expected_type=type_hints["service_linked_role_arn"])
            check_type(argname="argument suspended_processes", value=suspended_processes, expected_type=type_hints["suspended_processes"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument target_group_arns", value=target_group_arns, expected_type=type_hints["target_group_arns"])
            check_type(argname="argument termination_policies", value=termination_policies, expected_type=type_hints["termination_policies"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vpc_zone_identifier", value=vpc_zone_identifier, expected_type=type_hints["vpc_zone_identifier"])
            check_type(argname="argument wait_for_capacity_timeout", value=wait_for_capacity_timeout, expected_type=type_hints["wait_for_capacity_timeout"])
            check_type(argname="argument wait_for_elb_capacity", value=wait_for_elb_capacity, expected_type=type_hints["wait_for_elb_capacity"])
            check_type(argname="argument warm_pool", value=warm_pool, expected_type=type_hints["warm_pool"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_size": max_size,
            "min_size": min_size,
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
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if capacity_rebalance is not None:
            self._values["capacity_rebalance"] = capacity_rebalance
        if context is not None:
            self._values["context"] = context
        if default_cooldown is not None:
            self._values["default_cooldown"] = default_cooldown
        if default_instance_warmup is not None:
            self._values["default_instance_warmup"] = default_instance_warmup
        if desired_capacity is not None:
            self._values["desired_capacity"] = desired_capacity
        if enabled_metrics is not None:
            self._values["enabled_metrics"] = enabled_metrics
        if force_delete is not None:
            self._values["force_delete"] = force_delete
        if force_delete_warm_pool is not None:
            self._values["force_delete_warm_pool"] = force_delete_warm_pool
        if health_check_grace_period is not None:
            self._values["health_check_grace_period"] = health_check_grace_period
        if health_check_type is not None:
            self._values["health_check_type"] = health_check_type
        if id is not None:
            self._values["id"] = id
        if initial_lifecycle_hook is not None:
            self._values["initial_lifecycle_hook"] = initial_lifecycle_hook
        if instance_refresh is not None:
            self._values["instance_refresh"] = instance_refresh
        if launch_configuration is not None:
            self._values["launch_configuration"] = launch_configuration
        if launch_template is not None:
            self._values["launch_template"] = launch_template
        if load_balancers is not None:
            self._values["load_balancers"] = load_balancers
        if max_instance_lifetime is not None:
            self._values["max_instance_lifetime"] = max_instance_lifetime
        if metrics_granularity is not None:
            self._values["metrics_granularity"] = metrics_granularity
        if min_elb_capacity is not None:
            self._values["min_elb_capacity"] = min_elb_capacity
        if mixed_instances_policy is not None:
            self._values["mixed_instances_policy"] = mixed_instances_policy
        if name is not None:
            self._values["name"] = name
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
        if placement_group is not None:
            self._values["placement_group"] = placement_group
        if protect_from_scale_in is not None:
            self._values["protect_from_scale_in"] = protect_from_scale_in
        if service_linked_role_arn is not None:
            self._values["service_linked_role_arn"] = service_linked_role_arn
        if suspended_processes is not None:
            self._values["suspended_processes"] = suspended_processes
        if tag is not None:
            self._values["tag"] = tag
        if tags is not None:
            self._values["tags"] = tags
        if target_group_arns is not None:
            self._values["target_group_arns"] = target_group_arns
        if termination_policies is not None:
            self._values["termination_policies"] = termination_policies
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vpc_zone_identifier is not None:
            self._values["vpc_zone_identifier"] = vpc_zone_identifier
        if wait_for_capacity_timeout is not None:
            self._values["wait_for_capacity_timeout"] = wait_for_capacity_timeout
        if wait_for_elb_capacity is not None:
            self._values["wait_for_elb_capacity"] = wait_for_elb_capacity
        if warm_pool is not None:
            self._values["warm_pool"] = warm_pool

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
    def max_size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max_size AutoscalingGroup#max_size}.'''
        result = self._values.get("max_size")
        assert result is not None, "Required property 'max_size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_size AutoscalingGroup#min_size}.'''
        result = self._values.get("min_size")
        assert result is not None, "Required property 'min_size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#availability_zones AutoscalingGroup#availability_zones}.'''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def capacity_rebalance(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#capacity_rebalance AutoscalingGroup#capacity_rebalance}.'''
        result = self._values.get("capacity_rebalance")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def context(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#context AutoscalingGroup#context}.'''
        result = self._values.get("context")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#default_cooldown AutoscalingGroup#default_cooldown}.'''
        result = self._values.get("default_cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def default_instance_warmup(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#default_instance_warmup AutoscalingGroup#default_instance_warmup}.'''
        result = self._values.get("default_instance_warmup")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def desired_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#desired_capacity AutoscalingGroup#desired_capacity}.'''
        result = self._values.get("desired_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enabled_metrics(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#enabled_metrics AutoscalingGroup#enabled_metrics}.'''
        result = self._values.get("enabled_metrics")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def force_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#force_delete AutoscalingGroup#force_delete}.'''
        result = self._values.get("force_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def force_delete_warm_pool(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#force_delete_warm_pool AutoscalingGroup#force_delete_warm_pool}.'''
        result = self._values.get("force_delete_warm_pool")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def health_check_grace_period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#health_check_grace_period AutoscalingGroup#health_check_grace_period}.'''
        result = self._values.get("health_check_grace_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def health_check_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#health_check_type AutoscalingGroup#health_check_type}.'''
        result = self._values.get("health_check_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#id AutoscalingGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_lifecycle_hook(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupInitialLifecycleHook"]]]:
        '''initial_lifecycle_hook block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#initial_lifecycle_hook AutoscalingGroup#initial_lifecycle_hook}
        '''
        result = self._values.get("initial_lifecycle_hook")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupInitialLifecycleHook"]]], result)

    @builtins.property
    def instance_refresh(self) -> typing.Optional["AutoscalingGroupInstanceRefresh"]:
        '''instance_refresh block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_refresh AutoscalingGroup#instance_refresh}
        '''
        result = self._values.get("instance_refresh")
        return typing.cast(typing.Optional["AutoscalingGroupInstanceRefresh"], result)

    @builtins.property
    def launch_configuration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_configuration AutoscalingGroup#launch_configuration}.'''
        result = self._values.get("launch_configuration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_template(self) -> typing.Optional["AutoscalingGroupLaunchTemplate"]:
        '''launch_template block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template AutoscalingGroup#launch_template}
        '''
        result = self._values.get("launch_template")
        return typing.cast(typing.Optional["AutoscalingGroupLaunchTemplate"], result)

    @builtins.property
    def load_balancers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#load_balancers AutoscalingGroup#load_balancers}.'''
        result = self._values.get("load_balancers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_instance_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max_instance_lifetime AutoscalingGroup#max_instance_lifetime}.'''
        result = self._values.get("max_instance_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metrics_granularity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#metrics_granularity AutoscalingGroup#metrics_granularity}.'''
        result = self._values.get("metrics_granularity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_elb_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_elb_capacity AutoscalingGroup#min_elb_capacity}.'''
        result = self._values.get("min_elb_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def mixed_instances_policy(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicy"]:
        '''mixed_instances_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#mixed_instances_policy AutoscalingGroup#mixed_instances_policy}
        '''
        result = self._values.get("mixed_instances_policy")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicy"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name AutoscalingGroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name_prefix AutoscalingGroup#name_prefix}.'''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def placement_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#placement_group AutoscalingGroup#placement_group}.'''
        result = self._values.get("placement_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protect_from_scale_in(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#protect_from_scale_in AutoscalingGroup#protect_from_scale_in}.'''
        result = self._values.get("protect_from_scale_in")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def service_linked_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#service_linked_role_arn AutoscalingGroup#service_linked_role_arn}.'''
        result = self._values.get("service_linked_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suspended_processes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#suspended_processes AutoscalingGroup#suspended_processes}.'''
        result = self._values.get("suspended_processes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tag(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupTag"]]]:
        '''tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#tag AutoscalingGroup#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupTag"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#tags AutoscalingGroup#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def target_group_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#target_group_arns AutoscalingGroup#target_group_arns}.'''
        result = self._values.get("target_group_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def termination_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#termination_policies AutoscalingGroup#termination_policies}.'''
        result = self._values.get("termination_policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["AutoscalingGroupTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#timeouts AutoscalingGroup#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["AutoscalingGroupTimeouts"], result)

    @builtins.property
    def vpc_zone_identifier(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#vpc_zone_identifier AutoscalingGroup#vpc_zone_identifier}.'''
        result = self._values.get("vpc_zone_identifier")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def wait_for_capacity_timeout(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#wait_for_capacity_timeout AutoscalingGroup#wait_for_capacity_timeout}.'''
        result = self._values.get("wait_for_capacity_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_for_elb_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#wait_for_elb_capacity AutoscalingGroup#wait_for_elb_capacity}.'''
        result = self._values.get("wait_for_elb_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def warm_pool(self) -> typing.Optional["AutoscalingGroupWarmPool"]:
        '''warm_pool block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#warm_pool AutoscalingGroup#warm_pool}
        '''
        result = self._values.get("warm_pool")
        return typing.cast(typing.Optional["AutoscalingGroupWarmPool"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupInitialLifecycleHook",
    jsii_struct_bases=[],
    name_mapping={
        "lifecycle_transition": "lifecycleTransition",
        "name": "name",
        "default_result": "defaultResult",
        "heartbeat_timeout": "heartbeatTimeout",
        "notification_metadata": "notificationMetadata",
        "notification_target_arn": "notificationTargetArn",
        "role_arn": "roleArn",
    },
)
class AutoscalingGroupInitialLifecycleHook:
    def __init__(
        self,
        *,
        lifecycle_transition: builtins.str,
        name: builtins.str,
        default_result: typing.Optional[builtins.str] = None,
        heartbeat_timeout: typing.Optional[jsii.Number] = None,
        notification_metadata: typing.Optional[builtins.str] = None,
        notification_target_arn: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param lifecycle_transition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#lifecycle_transition AutoscalingGroup#lifecycle_transition}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name AutoscalingGroup#name}.
        :param default_result: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#default_result AutoscalingGroup#default_result}.
        :param heartbeat_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#heartbeat_timeout AutoscalingGroup#heartbeat_timeout}.
        :param notification_metadata: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#notification_metadata AutoscalingGroup#notification_metadata}.
        :param notification_target_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#notification_target_arn AutoscalingGroup#notification_target_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#role_arn AutoscalingGroup#role_arn}.
        '''
        if __debug__:
            def stub(
                *,
                lifecycle_transition: builtins.str,
                name: builtins.str,
                default_result: typing.Optional[builtins.str] = None,
                heartbeat_timeout: typing.Optional[jsii.Number] = None,
                notification_metadata: typing.Optional[builtins.str] = None,
                notification_target_arn: typing.Optional[builtins.str] = None,
                role_arn: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument lifecycle_transition", value=lifecycle_transition, expected_type=type_hints["lifecycle_transition"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument default_result", value=default_result, expected_type=type_hints["default_result"])
            check_type(argname="argument heartbeat_timeout", value=heartbeat_timeout, expected_type=type_hints["heartbeat_timeout"])
            check_type(argname="argument notification_metadata", value=notification_metadata, expected_type=type_hints["notification_metadata"])
            check_type(argname="argument notification_target_arn", value=notification_target_arn, expected_type=type_hints["notification_target_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "lifecycle_transition": lifecycle_transition,
            "name": name,
        }
        if default_result is not None:
            self._values["default_result"] = default_result
        if heartbeat_timeout is not None:
            self._values["heartbeat_timeout"] = heartbeat_timeout
        if notification_metadata is not None:
            self._values["notification_metadata"] = notification_metadata
        if notification_target_arn is not None:
            self._values["notification_target_arn"] = notification_target_arn
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def lifecycle_transition(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#lifecycle_transition AutoscalingGroup#lifecycle_transition}.'''
        result = self._values.get("lifecycle_transition")
        assert result is not None, "Required property 'lifecycle_transition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name AutoscalingGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_result(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#default_result AutoscalingGroup#default_result}.'''
        result = self._values.get("default_result")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def heartbeat_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#heartbeat_timeout AutoscalingGroup#heartbeat_timeout}.'''
        result = self._values.get("heartbeat_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def notification_metadata(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#notification_metadata AutoscalingGroup#notification_metadata}.'''
        result = self._values.get("notification_metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_target_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#notification_target_arn AutoscalingGroup#notification_target_arn}.'''
        result = self._values.get("notification_target_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#role_arn AutoscalingGroup#role_arn}.'''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupInitialLifecycleHook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupInitialLifecycleHookList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupInitialLifecycleHookList",
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
    ) -> "AutoscalingGroupInitialLifecycleHookOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingGroupInitialLifecycleHookOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupInitialLifecycleHook]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupInitialLifecycleHook]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupInitialLifecycleHook]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupInitialLifecycleHook]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingGroupInitialLifecycleHookOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupInitialLifecycleHookOutputReference",
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

    @jsii.member(jsii_name="resetDefaultResult")
    def reset_default_result(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultResult", []))

    @jsii.member(jsii_name="resetHeartbeatTimeout")
    def reset_heartbeat_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeartbeatTimeout", []))

    @jsii.member(jsii_name="resetNotificationMetadata")
    def reset_notification_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationMetadata", []))

    @jsii.member(jsii_name="resetNotificationTargetArn")
    def reset_notification_target_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationTargetArn", []))

    @jsii.member(jsii_name="resetRoleArn")
    def reset_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleArn", []))

    @builtins.property
    @jsii.member(jsii_name="defaultResultInput")
    def default_result_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultResultInput"))

    @builtins.property
    @jsii.member(jsii_name="heartbeatTimeoutInput")
    def heartbeat_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "heartbeatTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleTransitionInput")
    def lifecycle_transition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleTransitionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationMetadataInput")
    def notification_metadata_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationMetadataInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationTargetArnInput")
    def notification_target_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTargetArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultResult")
    def default_result(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultResult"))

    @default_result.setter
    def default_result(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultResult", value)

    @builtins.property
    @jsii.member(jsii_name="heartbeatTimeout")
    def heartbeat_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "heartbeatTimeout"))

    @heartbeat_timeout.setter
    def heartbeat_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "heartbeatTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="lifecycleTransition")
    def lifecycle_transition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleTransition"))

    @lifecycle_transition.setter
    def lifecycle_transition(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleTransition", value)

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
    @jsii.member(jsii_name="notificationMetadata")
    def notification_metadata(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationMetadata"))

    @notification_metadata.setter
    def notification_metadata(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationMetadata", value)

    @builtins.property
    @jsii.member(jsii_name="notificationTargetArn")
    def notification_target_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationTargetArn"))

    @notification_target_arn.setter
    def notification_target_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationTargetArn", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingGroupInitialLifecycleHook, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingGroupInitialLifecycleHook, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingGroupInitialLifecycleHook, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[AutoscalingGroupInitialLifecycleHook, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupInstanceRefresh",
    jsii_struct_bases=[],
    name_mapping={
        "strategy": "strategy",
        "preferences": "preferences",
        "triggers": "triggers",
    },
)
class AutoscalingGroupInstanceRefresh:
    def __init__(
        self,
        *,
        strategy: builtins.str,
        preferences: typing.Optional[typing.Union["AutoscalingGroupInstanceRefreshPreferences", typing.Dict[str, typing.Any]]] = None,
        triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#strategy AutoscalingGroup#strategy}.
        :param preferences: preferences block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#preferences AutoscalingGroup#preferences}
        :param triggers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#triggers AutoscalingGroup#triggers}.
        '''
        if isinstance(preferences, dict):
            preferences = AutoscalingGroupInstanceRefreshPreferences(**preferences)
        if __debug__:
            def stub(
                *,
                strategy: builtins.str,
                preferences: typing.Optional[typing.Union[AutoscalingGroupInstanceRefreshPreferences, typing.Dict[str, typing.Any]]] = None,
                triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument strategy", value=strategy, expected_type=type_hints["strategy"])
            check_type(argname="argument preferences", value=preferences, expected_type=type_hints["preferences"])
            check_type(argname="argument triggers", value=triggers, expected_type=type_hints["triggers"])
        self._values: typing.Dict[str, typing.Any] = {
            "strategy": strategy,
        }
        if preferences is not None:
            self._values["preferences"] = preferences
        if triggers is not None:
            self._values["triggers"] = triggers

    @builtins.property
    def strategy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#strategy AutoscalingGroup#strategy}.'''
        result = self._values.get("strategy")
        assert result is not None, "Required property 'strategy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def preferences(
        self,
    ) -> typing.Optional["AutoscalingGroupInstanceRefreshPreferences"]:
        '''preferences block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#preferences AutoscalingGroup#preferences}
        '''
        result = self._values.get("preferences")
        return typing.cast(typing.Optional["AutoscalingGroupInstanceRefreshPreferences"], result)

    @builtins.property
    def triggers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#triggers AutoscalingGroup#triggers}.'''
        result = self._values.get("triggers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupInstanceRefresh(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupInstanceRefreshOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupInstanceRefreshOutputReference",
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

    @jsii.member(jsii_name="putPreferences")
    def put_preferences(
        self,
        *,
        checkpoint_delay: typing.Optional[builtins.str] = None,
        checkpoint_percentages: typing.Optional[typing.Sequence[jsii.Number]] = None,
        instance_warmup: typing.Optional[builtins.str] = None,
        min_healthy_percentage: typing.Optional[jsii.Number] = None,
        skip_matching: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param checkpoint_delay: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#checkpoint_delay AutoscalingGroup#checkpoint_delay}.
        :param checkpoint_percentages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#checkpoint_percentages AutoscalingGroup#checkpoint_percentages}.
        :param instance_warmup: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_warmup AutoscalingGroup#instance_warmup}.
        :param min_healthy_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_healthy_percentage AutoscalingGroup#min_healthy_percentage}.
        :param skip_matching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#skip_matching AutoscalingGroup#skip_matching}.
        '''
        value = AutoscalingGroupInstanceRefreshPreferences(
            checkpoint_delay=checkpoint_delay,
            checkpoint_percentages=checkpoint_percentages,
            instance_warmup=instance_warmup,
            min_healthy_percentage=min_healthy_percentage,
            skip_matching=skip_matching,
        )

        return typing.cast(None, jsii.invoke(self, "putPreferences", [value]))

    @jsii.member(jsii_name="resetPreferences")
    def reset_preferences(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferences", []))

    @jsii.member(jsii_name="resetTriggers")
    def reset_triggers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggers", []))

    @builtins.property
    @jsii.member(jsii_name="preferences")
    def preferences(
        self,
    ) -> "AutoscalingGroupInstanceRefreshPreferencesOutputReference":
        return typing.cast("AutoscalingGroupInstanceRefreshPreferencesOutputReference", jsii.get(self, "preferences"))

    @builtins.property
    @jsii.member(jsii_name="preferencesInput")
    def preferences_input(
        self,
    ) -> typing.Optional["AutoscalingGroupInstanceRefreshPreferences"]:
        return typing.cast(typing.Optional["AutoscalingGroupInstanceRefreshPreferences"], jsii.get(self, "preferencesInput"))

    @builtins.property
    @jsii.member(jsii_name="strategyInput")
    def strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "strategyInput"))

    @builtins.property
    @jsii.member(jsii_name="triggersInput")
    def triggers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "triggersInput"))

    @builtins.property
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "strategy"))

    @strategy.setter
    def strategy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "strategy", value)

    @builtins.property
    @jsii.member(jsii_name="triggers")
    def triggers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "triggers"))

    @triggers.setter
    def triggers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AutoscalingGroupInstanceRefresh]:
        return typing.cast(typing.Optional[AutoscalingGroupInstanceRefresh], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupInstanceRefresh],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[AutoscalingGroupInstanceRefresh]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupInstanceRefreshPreferences",
    jsii_struct_bases=[],
    name_mapping={
        "checkpoint_delay": "checkpointDelay",
        "checkpoint_percentages": "checkpointPercentages",
        "instance_warmup": "instanceWarmup",
        "min_healthy_percentage": "minHealthyPercentage",
        "skip_matching": "skipMatching",
    },
)
class AutoscalingGroupInstanceRefreshPreferences:
    def __init__(
        self,
        *,
        checkpoint_delay: typing.Optional[builtins.str] = None,
        checkpoint_percentages: typing.Optional[typing.Sequence[jsii.Number]] = None,
        instance_warmup: typing.Optional[builtins.str] = None,
        min_healthy_percentage: typing.Optional[jsii.Number] = None,
        skip_matching: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param checkpoint_delay: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#checkpoint_delay AutoscalingGroup#checkpoint_delay}.
        :param checkpoint_percentages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#checkpoint_percentages AutoscalingGroup#checkpoint_percentages}.
        :param instance_warmup: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_warmup AutoscalingGroup#instance_warmup}.
        :param min_healthy_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_healthy_percentage AutoscalingGroup#min_healthy_percentage}.
        :param skip_matching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#skip_matching AutoscalingGroup#skip_matching}.
        '''
        if __debug__:
            def stub(
                *,
                checkpoint_delay: typing.Optional[builtins.str] = None,
                checkpoint_percentages: typing.Optional[typing.Sequence[jsii.Number]] = None,
                instance_warmup: typing.Optional[builtins.str] = None,
                min_healthy_percentage: typing.Optional[jsii.Number] = None,
                skip_matching: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument checkpoint_delay", value=checkpoint_delay, expected_type=type_hints["checkpoint_delay"])
            check_type(argname="argument checkpoint_percentages", value=checkpoint_percentages, expected_type=type_hints["checkpoint_percentages"])
            check_type(argname="argument instance_warmup", value=instance_warmup, expected_type=type_hints["instance_warmup"])
            check_type(argname="argument min_healthy_percentage", value=min_healthy_percentage, expected_type=type_hints["min_healthy_percentage"])
            check_type(argname="argument skip_matching", value=skip_matching, expected_type=type_hints["skip_matching"])
        self._values: typing.Dict[str, typing.Any] = {}
        if checkpoint_delay is not None:
            self._values["checkpoint_delay"] = checkpoint_delay
        if checkpoint_percentages is not None:
            self._values["checkpoint_percentages"] = checkpoint_percentages
        if instance_warmup is not None:
            self._values["instance_warmup"] = instance_warmup
        if min_healthy_percentage is not None:
            self._values["min_healthy_percentage"] = min_healthy_percentage
        if skip_matching is not None:
            self._values["skip_matching"] = skip_matching

    @builtins.property
    def checkpoint_delay(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#checkpoint_delay AutoscalingGroup#checkpoint_delay}.'''
        result = self._values.get("checkpoint_delay")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def checkpoint_percentages(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#checkpoint_percentages AutoscalingGroup#checkpoint_percentages}.'''
        result = self._values.get("checkpoint_percentages")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def instance_warmup(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_warmup AutoscalingGroup#instance_warmup}.'''
        result = self._values.get("instance_warmup")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_healthy_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_healthy_percentage AutoscalingGroup#min_healthy_percentage}.'''
        result = self._values.get("min_healthy_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def skip_matching(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#skip_matching AutoscalingGroup#skip_matching}.'''
        result = self._values.get("skip_matching")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupInstanceRefreshPreferences(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupInstanceRefreshPreferencesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupInstanceRefreshPreferencesOutputReference",
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

    @jsii.member(jsii_name="resetCheckpointDelay")
    def reset_checkpoint_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckpointDelay", []))

    @jsii.member(jsii_name="resetCheckpointPercentages")
    def reset_checkpoint_percentages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckpointPercentages", []))

    @jsii.member(jsii_name="resetInstanceWarmup")
    def reset_instance_warmup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceWarmup", []))

    @jsii.member(jsii_name="resetMinHealthyPercentage")
    def reset_min_healthy_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinHealthyPercentage", []))

    @jsii.member(jsii_name="resetSkipMatching")
    def reset_skip_matching(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipMatching", []))

    @builtins.property
    @jsii.member(jsii_name="checkpointDelayInput")
    def checkpoint_delay_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "checkpointDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="checkpointPercentagesInput")
    def checkpoint_percentages_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "checkpointPercentagesInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceWarmupInput")
    def instance_warmup_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceWarmupInput"))

    @builtins.property
    @jsii.member(jsii_name="minHealthyPercentageInput")
    def min_healthy_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minHealthyPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="skipMatchingInput")
    def skip_matching_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipMatchingInput"))

    @builtins.property
    @jsii.member(jsii_name="checkpointDelay")
    def checkpoint_delay(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checkpointDelay"))

    @checkpoint_delay.setter
    def checkpoint_delay(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkpointDelay", value)

    @builtins.property
    @jsii.member(jsii_name="checkpointPercentages")
    def checkpoint_percentages(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "checkpointPercentages"))

    @checkpoint_percentages.setter
    def checkpoint_percentages(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            def stub(value: typing.List[jsii.Number]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkpointPercentages", value)

    @builtins.property
    @jsii.member(jsii_name="instanceWarmup")
    def instance_warmup(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceWarmup"))

    @instance_warmup.setter
    def instance_warmup(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceWarmup", value)

    @builtins.property
    @jsii.member(jsii_name="minHealthyPercentage")
    def min_healthy_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minHealthyPercentage"))

    @min_healthy_percentage.setter
    def min_healthy_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minHealthyPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="skipMatching")
    def skip_matching(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "skipMatching"))

    @skip_matching.setter
    def skip_matching(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipMatching", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupInstanceRefreshPreferences]:
        return typing.cast(typing.Optional[AutoscalingGroupInstanceRefreshPreferences], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupInstanceRefreshPreferences],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AutoscalingGroupInstanceRefreshPreferences],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupLaunchTemplate",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name", "version": "version"},
)
class AutoscalingGroupLaunchTemplate:
    def __init__(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#id AutoscalingGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name AutoscalingGroup#name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#version AutoscalingGroup#version}.
        '''
        if __debug__:
            def stub(
                *,
                id: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                version: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#id AutoscalingGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#name AutoscalingGroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#version AutoscalingGroup#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupLaunchTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupLaunchTemplateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupLaunchTemplateOutputReference",
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

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

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

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AutoscalingGroupLaunchTemplate]:
        return typing.cast(typing.Optional[AutoscalingGroupLaunchTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupLaunchTemplate],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[AutoscalingGroupLaunchTemplate]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "launch_template": "launchTemplate",
        "instances_distribution": "instancesDistribution",
    },
)
class AutoscalingGroupMixedInstancesPolicy:
    def __init__(
        self,
        *,
        launch_template: typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplate", typing.Dict[str, typing.Any]],
        instances_distribution: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyInstancesDistribution", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param launch_template: launch_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template AutoscalingGroup#launch_template}
        :param instances_distribution: instances_distribution block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instances_distribution AutoscalingGroup#instances_distribution}
        '''
        if isinstance(launch_template, dict):
            launch_template = AutoscalingGroupMixedInstancesPolicyLaunchTemplate(**launch_template)
        if isinstance(instances_distribution, dict):
            instances_distribution = AutoscalingGroupMixedInstancesPolicyInstancesDistribution(**instances_distribution)
        if __debug__:
            def stub(
                *,
                launch_template: typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplate, typing.Dict[str, typing.Any]],
                instances_distribution: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyInstancesDistribution, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument launch_template", value=launch_template, expected_type=type_hints["launch_template"])
            check_type(argname="argument instances_distribution", value=instances_distribution, expected_type=type_hints["instances_distribution"])
        self._values: typing.Dict[str, typing.Any] = {
            "launch_template": launch_template,
        }
        if instances_distribution is not None:
            self._values["instances_distribution"] = instances_distribution

    @builtins.property
    def launch_template(self) -> "AutoscalingGroupMixedInstancesPolicyLaunchTemplate":
        '''launch_template block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template AutoscalingGroup#launch_template}
        '''
        result = self._values.get("launch_template")
        assert result is not None, "Required property 'launch_template' is missing"
        return typing.cast("AutoscalingGroupMixedInstancesPolicyLaunchTemplate", result)

    @builtins.property
    def instances_distribution(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyInstancesDistribution"]:
        '''instances_distribution block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instances_distribution AutoscalingGroup#instances_distribution}
        '''
        result = self._values.get("instances_distribution")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyInstancesDistribution"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyInstancesDistribution",
    jsii_struct_bases=[],
    name_mapping={
        "on_demand_allocation_strategy": "onDemandAllocationStrategy",
        "on_demand_base_capacity": "onDemandBaseCapacity",
        "on_demand_percentage_above_base_capacity": "onDemandPercentageAboveBaseCapacity",
        "spot_allocation_strategy": "spotAllocationStrategy",
        "spot_instance_pools": "spotInstancePools",
        "spot_max_price": "spotMaxPrice",
    },
)
class AutoscalingGroupMixedInstancesPolicyInstancesDistribution:
    def __init__(
        self,
        *,
        on_demand_allocation_strategy: typing.Optional[builtins.str] = None,
        on_demand_base_capacity: typing.Optional[jsii.Number] = None,
        on_demand_percentage_above_base_capacity: typing.Optional[jsii.Number] = None,
        spot_allocation_strategy: typing.Optional[builtins.str] = None,
        spot_instance_pools: typing.Optional[jsii.Number] = None,
        spot_max_price: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param on_demand_allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_allocation_strategy AutoscalingGroup#on_demand_allocation_strategy}.
        :param on_demand_base_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_base_capacity AutoscalingGroup#on_demand_base_capacity}.
        :param on_demand_percentage_above_base_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_percentage_above_base_capacity AutoscalingGroup#on_demand_percentage_above_base_capacity}.
        :param spot_allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_allocation_strategy AutoscalingGroup#spot_allocation_strategy}.
        :param spot_instance_pools: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_instance_pools AutoscalingGroup#spot_instance_pools}.
        :param spot_max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_max_price AutoscalingGroup#spot_max_price}.
        '''
        if __debug__:
            def stub(
                *,
                on_demand_allocation_strategy: typing.Optional[builtins.str] = None,
                on_demand_base_capacity: typing.Optional[jsii.Number] = None,
                on_demand_percentage_above_base_capacity: typing.Optional[jsii.Number] = None,
                spot_allocation_strategy: typing.Optional[builtins.str] = None,
                spot_instance_pools: typing.Optional[jsii.Number] = None,
                spot_max_price: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument on_demand_allocation_strategy", value=on_demand_allocation_strategy, expected_type=type_hints["on_demand_allocation_strategy"])
            check_type(argname="argument on_demand_base_capacity", value=on_demand_base_capacity, expected_type=type_hints["on_demand_base_capacity"])
            check_type(argname="argument on_demand_percentage_above_base_capacity", value=on_demand_percentage_above_base_capacity, expected_type=type_hints["on_demand_percentage_above_base_capacity"])
            check_type(argname="argument spot_allocation_strategy", value=spot_allocation_strategy, expected_type=type_hints["spot_allocation_strategy"])
            check_type(argname="argument spot_instance_pools", value=spot_instance_pools, expected_type=type_hints["spot_instance_pools"])
            check_type(argname="argument spot_max_price", value=spot_max_price, expected_type=type_hints["spot_max_price"])
        self._values: typing.Dict[str, typing.Any] = {}
        if on_demand_allocation_strategy is not None:
            self._values["on_demand_allocation_strategy"] = on_demand_allocation_strategy
        if on_demand_base_capacity is not None:
            self._values["on_demand_base_capacity"] = on_demand_base_capacity
        if on_demand_percentage_above_base_capacity is not None:
            self._values["on_demand_percentage_above_base_capacity"] = on_demand_percentage_above_base_capacity
        if spot_allocation_strategy is not None:
            self._values["spot_allocation_strategy"] = spot_allocation_strategy
        if spot_instance_pools is not None:
            self._values["spot_instance_pools"] = spot_instance_pools
        if spot_max_price is not None:
            self._values["spot_max_price"] = spot_max_price

    @builtins.property
    def on_demand_allocation_strategy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_allocation_strategy AutoscalingGroup#on_demand_allocation_strategy}.'''
        result = self._values.get("on_demand_allocation_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_demand_base_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_base_capacity AutoscalingGroup#on_demand_base_capacity}.'''
        result = self._values.get("on_demand_base_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def on_demand_percentage_above_base_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_percentage_above_base_capacity AutoscalingGroup#on_demand_percentage_above_base_capacity}.'''
        result = self._values.get("on_demand_percentage_above_base_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def spot_allocation_strategy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_allocation_strategy AutoscalingGroup#spot_allocation_strategy}.'''
        result = self._values.get("spot_allocation_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_instance_pools(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_instance_pools AutoscalingGroup#spot_instance_pools}.'''
        result = self._values.get("spot_instance_pools")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def spot_max_price(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_max_price AutoscalingGroup#spot_max_price}.'''
        result = self._values.get("spot_max_price")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyInstancesDistribution(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyInstancesDistributionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyInstancesDistributionOutputReference",
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

    @jsii.member(jsii_name="resetOnDemandAllocationStrategy")
    def reset_on_demand_allocation_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnDemandAllocationStrategy", []))

    @jsii.member(jsii_name="resetOnDemandBaseCapacity")
    def reset_on_demand_base_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnDemandBaseCapacity", []))

    @jsii.member(jsii_name="resetOnDemandPercentageAboveBaseCapacity")
    def reset_on_demand_percentage_above_base_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnDemandPercentageAboveBaseCapacity", []))

    @jsii.member(jsii_name="resetSpotAllocationStrategy")
    def reset_spot_allocation_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotAllocationStrategy", []))

    @jsii.member(jsii_name="resetSpotInstancePools")
    def reset_spot_instance_pools(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotInstancePools", []))

    @jsii.member(jsii_name="resetSpotMaxPrice")
    def reset_spot_max_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotMaxPrice", []))

    @builtins.property
    @jsii.member(jsii_name="onDemandAllocationStrategyInput")
    def on_demand_allocation_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "onDemandAllocationStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="onDemandBaseCapacityInput")
    def on_demand_base_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "onDemandBaseCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="onDemandPercentageAboveBaseCapacityInput")
    def on_demand_percentage_above_base_capacity_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "onDemandPercentageAboveBaseCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="spotAllocationStrategyInput")
    def spot_allocation_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spotAllocationStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="spotInstancePoolsInput")
    def spot_instance_pools_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "spotInstancePoolsInput"))

    @builtins.property
    @jsii.member(jsii_name="spotMaxPriceInput")
    def spot_max_price_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spotMaxPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="onDemandAllocationStrategy")
    def on_demand_allocation_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onDemandAllocationStrategy"))

    @on_demand_allocation_strategy.setter
    def on_demand_allocation_strategy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onDemandAllocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="onDemandBaseCapacity")
    def on_demand_base_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "onDemandBaseCapacity"))

    @on_demand_base_capacity.setter
    def on_demand_base_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onDemandBaseCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="onDemandPercentageAboveBaseCapacity")
    def on_demand_percentage_above_base_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "onDemandPercentageAboveBaseCapacity"))

    @on_demand_percentage_above_base_capacity.setter
    def on_demand_percentage_above_base_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onDemandPercentageAboveBaseCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="spotAllocationStrategy")
    def spot_allocation_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spotAllocationStrategy"))

    @spot_allocation_strategy.setter
    def spot_allocation_strategy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotAllocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="spotInstancePools")
    def spot_instance_pools(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotInstancePools"))

    @spot_instance_pools.setter
    def spot_instance_pools(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotInstancePools", value)

    @builtins.property
    @jsii.member(jsii_name="spotMaxPrice")
    def spot_max_price(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spotMaxPrice"))

    @spot_max_price.setter
    def spot_max_price(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotMaxPrice", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyInstancesDistribution]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyInstancesDistribution], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyInstancesDistribution],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AutoscalingGroupMixedInstancesPolicyInstancesDistribution],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplate",
    jsii_struct_bases=[],
    name_mapping={
        "launch_template_specification": "launchTemplateSpecification",
        "override": "override",
    },
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplate:
    def __init__(
        self,
        *,
        launch_template_specification: typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification", typing.Dict[str, typing.Any]],
        override: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param launch_template_specification: launch_template_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_specification AutoscalingGroup#launch_template_specification}
        :param override: override block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#override AutoscalingGroup#override}
        '''
        if isinstance(launch_template_specification, dict):
            launch_template_specification = AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification(**launch_template_specification)
        if __debug__:
            def stub(
                *,
                launch_template_specification: typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification, typing.Dict[str, typing.Any]],
                override: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument launch_template_specification", value=launch_template_specification, expected_type=type_hints["launch_template_specification"])
            check_type(argname="argument override", value=override, expected_type=type_hints["override"])
        self._values: typing.Dict[str, typing.Any] = {
            "launch_template_specification": launch_template_specification,
        }
        if override is not None:
            self._values["override"] = override

    @builtins.property
    def launch_template_specification(
        self,
    ) -> "AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification":
        '''launch_template_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_specification AutoscalingGroup#launch_template_specification}
        '''
        result = self._values.get("launch_template_specification")
        assert result is not None, "Required property 'launch_template_specification' is missing"
        return typing.cast("AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification", result)

    @builtins.property
    def override(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride"]]]:
        '''override block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#override AutoscalingGroup#override}
        '''
        result = self._values.get("override")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "launch_template_id": "launchTemplateId",
        "launch_template_name": "launchTemplateName",
        "version": "version",
    },
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification:
    def __init__(
        self,
        *,
        launch_template_id: typing.Optional[builtins.str] = None,
        launch_template_name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param launch_template_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_id AutoscalingGroup#launch_template_id}.
        :param launch_template_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_name AutoscalingGroup#launch_template_name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#version AutoscalingGroup#version}.
        '''
        if __debug__:
            def stub(
                *,
                launch_template_id: typing.Optional[builtins.str] = None,
                launch_template_name: typing.Optional[builtins.str] = None,
                version: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument launch_template_id", value=launch_template_id, expected_type=type_hints["launch_template_id"])
            check_type(argname="argument launch_template_name", value=launch_template_name, expected_type=type_hints["launch_template_name"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if launch_template_id is not None:
            self._values["launch_template_id"] = launch_template_id
        if launch_template_name is not None:
            self._values["launch_template_name"] = launch_template_name
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def launch_template_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_id AutoscalingGroup#launch_template_id}.'''
        result = self._values.get("launch_template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_template_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_name AutoscalingGroup#launch_template_name}.'''
        result = self._values.get("launch_template_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#version AutoscalingGroup#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputReference",
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

    @jsii.member(jsii_name="resetLaunchTemplateId")
    def reset_launch_template_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplateId", []))

    @jsii.member(jsii_name="resetLaunchTemplateName")
    def reset_launch_template_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplateName", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateIdInput")
    def launch_template_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTemplateIdInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateNameInput")
    def launch_template_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTemplateNameInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateId")
    def launch_template_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchTemplateId"))

    @launch_template_id.setter
    def launch_template_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchTemplateId", value)

    @builtins.property
    @jsii.member(jsii_name="launchTemplateName")
    def launch_template_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchTemplateName"))

    @launch_template_name.setter
    def launch_template_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchTemplateName", value)

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

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOutputReference",
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

    @jsii.member(jsii_name="putLaunchTemplateSpecification")
    def put_launch_template_specification(
        self,
        *,
        launch_template_id: typing.Optional[builtins.str] = None,
        launch_template_name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param launch_template_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_id AutoscalingGroup#launch_template_id}.
        :param launch_template_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_name AutoscalingGroup#launch_template_name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#version AutoscalingGroup#version}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification(
            launch_template_id=launch_template_id,
            launch_template_name=launch_template_name,
            version=version,
        )

        return typing.cast(None, jsii.invoke(self, "putLaunchTemplateSpecification", [value]))

    @jsii.member(jsii_name="putOverride")
    def put_override(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOverride", [value]))

    @jsii.member(jsii_name="resetOverride")
    def reset_override(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverride", []))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateSpecification")
    def launch_template_specification(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputReference, jsii.get(self, "launchTemplateSpecification"))

    @builtins.property
    @jsii.member(jsii_name="override")
    def override(
        self,
    ) -> "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideList":
        return typing.cast("AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideList", jsii.get(self, "override"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateSpecificationInput")
    def launch_template_specification_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification], jsii.get(self, "launchTemplateSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideInput")
    def override_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride"]]], jsii.get(self, "overrideInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplate]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplate],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplate],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride",
    jsii_struct_bases=[],
    name_mapping={
        "instance_requirements": "instanceRequirements",
        "instance_type": "instanceType",
        "launch_template_specification": "launchTemplateSpecification",
        "weighted_capacity": "weightedCapacity",
    },
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride:
    def __init__(
        self,
        *,
        instance_requirements: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements", typing.Dict[str, typing.Any]]] = None,
        instance_type: typing.Optional[builtins.str] = None,
        launch_template_specification: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification", typing.Dict[str, typing.Any]]] = None,
        weighted_capacity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_requirements: instance_requirements block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_requirements AutoscalingGroup#instance_requirements}
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_type AutoscalingGroup#instance_type}.
        :param launch_template_specification: launch_template_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_specification AutoscalingGroup#launch_template_specification}
        :param weighted_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#weighted_capacity AutoscalingGroup#weighted_capacity}.
        '''
        if isinstance(instance_requirements, dict):
            instance_requirements = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements(**instance_requirements)
        if isinstance(launch_template_specification, dict):
            launch_template_specification = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification(**launch_template_specification)
        if __debug__:
            def stub(
                *,
                instance_requirements: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements, typing.Dict[str, typing.Any]]] = None,
                instance_type: typing.Optional[builtins.str] = None,
                launch_template_specification: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification, typing.Dict[str, typing.Any]]] = None,
                weighted_capacity: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_requirements", value=instance_requirements, expected_type=type_hints["instance_requirements"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument launch_template_specification", value=launch_template_specification, expected_type=type_hints["launch_template_specification"])
            check_type(argname="argument weighted_capacity", value=weighted_capacity, expected_type=type_hints["weighted_capacity"])
        self._values: typing.Dict[str, typing.Any] = {}
        if instance_requirements is not None:
            self._values["instance_requirements"] = instance_requirements
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if launch_template_specification is not None:
            self._values["launch_template_specification"] = launch_template_specification
        if weighted_capacity is not None:
            self._values["weighted_capacity"] = weighted_capacity

    @builtins.property
    def instance_requirements(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements"]:
        '''instance_requirements block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_requirements AutoscalingGroup#instance_requirements}
        '''
        result = self._values.get("instance_requirements")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements"], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_type AutoscalingGroup#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_template_specification(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification"]:
        '''launch_template_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_specification AutoscalingGroup#launch_template_specification}
        '''
        result = self._values.get("launch_template_specification")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification"], result)

    @builtins.property
    def weighted_capacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#weighted_capacity AutoscalingGroup#weighted_capacity}.'''
        result = self._values.get("weighted_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements",
    jsii_struct_bases=[],
    name_mapping={
        "accelerator_count": "acceleratorCount",
        "accelerator_manufacturers": "acceleratorManufacturers",
        "accelerator_names": "acceleratorNames",
        "accelerator_total_memory_mib": "acceleratorTotalMemoryMib",
        "accelerator_types": "acceleratorTypes",
        "bare_metal": "bareMetal",
        "baseline_ebs_bandwidth_mbps": "baselineEbsBandwidthMbps",
        "burstable_performance": "burstablePerformance",
        "cpu_manufacturers": "cpuManufacturers",
        "excluded_instance_types": "excludedInstanceTypes",
        "instance_generations": "instanceGenerations",
        "local_storage": "localStorage",
        "local_storage_types": "localStorageTypes",
        "memory_gib_per_vcpu": "memoryGibPerVcpu",
        "memory_mib": "memoryMib",
        "network_interface_count": "networkInterfaceCount",
        "on_demand_max_price_percentage_over_lowest_price": "onDemandMaxPricePercentageOverLowestPrice",
        "require_hibernate_support": "requireHibernateSupport",
        "spot_max_price_percentage_over_lowest_price": "spotMaxPricePercentageOverLowestPrice",
        "total_local_storage_gb": "totalLocalStorageGb",
        "vcpu_count": "vcpuCount",
    },
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements:
    def __init__(
        self,
        *,
        accelerator_count: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount", typing.Dict[str, typing.Any]]] = None,
        accelerator_manufacturers: typing.Optional[typing.Sequence[builtins.str]] = None,
        accelerator_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        accelerator_total_memory_mib: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib", typing.Dict[str, typing.Any]]] = None,
        accelerator_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        bare_metal: typing.Optional[builtins.str] = None,
        baseline_ebs_bandwidth_mbps: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps", typing.Dict[str, typing.Any]]] = None,
        burstable_performance: typing.Optional[builtins.str] = None,
        cpu_manufacturers: typing.Optional[typing.Sequence[builtins.str]] = None,
        excluded_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        instance_generations: typing.Optional[typing.Sequence[builtins.str]] = None,
        local_storage: typing.Optional[builtins.str] = None,
        local_storage_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        memory_gib_per_vcpu: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu", typing.Dict[str, typing.Any]]] = None,
        memory_mib: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib", typing.Dict[str, typing.Any]]] = None,
        network_interface_count: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount", typing.Dict[str, typing.Any]]] = None,
        on_demand_max_price_percentage_over_lowest_price: typing.Optional[jsii.Number] = None,
        require_hibernate_support: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        spot_max_price_percentage_over_lowest_price: typing.Optional[jsii.Number] = None,
        total_local_storage_gb: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb", typing.Dict[str, typing.Any]]] = None,
        vcpu_count: typing.Optional[typing.Union["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param accelerator_count: accelerator_count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_count AutoscalingGroup#accelerator_count}
        :param accelerator_manufacturers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_manufacturers AutoscalingGroup#accelerator_manufacturers}.
        :param accelerator_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_names AutoscalingGroup#accelerator_names}.
        :param accelerator_total_memory_mib: accelerator_total_memory_mib block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_total_memory_mib AutoscalingGroup#accelerator_total_memory_mib}
        :param accelerator_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_types AutoscalingGroup#accelerator_types}.
        :param bare_metal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#bare_metal AutoscalingGroup#bare_metal}.
        :param baseline_ebs_bandwidth_mbps: baseline_ebs_bandwidth_mbps block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#baseline_ebs_bandwidth_mbps AutoscalingGroup#baseline_ebs_bandwidth_mbps}
        :param burstable_performance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#burstable_performance AutoscalingGroup#burstable_performance}.
        :param cpu_manufacturers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#cpu_manufacturers AutoscalingGroup#cpu_manufacturers}.
        :param excluded_instance_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#excluded_instance_types AutoscalingGroup#excluded_instance_types}.
        :param instance_generations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_generations AutoscalingGroup#instance_generations}.
        :param local_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#local_storage AutoscalingGroup#local_storage}.
        :param local_storage_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#local_storage_types AutoscalingGroup#local_storage_types}.
        :param memory_gib_per_vcpu: memory_gib_per_vcpu block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#memory_gib_per_vcpu AutoscalingGroup#memory_gib_per_vcpu}
        :param memory_mib: memory_mib block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#memory_mib AutoscalingGroup#memory_mib}
        :param network_interface_count: network_interface_count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#network_interface_count AutoscalingGroup#network_interface_count}
        :param on_demand_max_price_percentage_over_lowest_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_max_price_percentage_over_lowest_price AutoscalingGroup#on_demand_max_price_percentage_over_lowest_price}.
        :param require_hibernate_support: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#require_hibernate_support AutoscalingGroup#require_hibernate_support}.
        :param spot_max_price_percentage_over_lowest_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_max_price_percentage_over_lowest_price AutoscalingGroup#spot_max_price_percentage_over_lowest_price}.
        :param total_local_storage_gb: total_local_storage_gb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#total_local_storage_gb AutoscalingGroup#total_local_storage_gb}
        :param vcpu_count: vcpu_count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#vcpu_count AutoscalingGroup#vcpu_count}
        '''
        if isinstance(accelerator_count, dict):
            accelerator_count = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount(**accelerator_count)
        if isinstance(accelerator_total_memory_mib, dict):
            accelerator_total_memory_mib = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib(**accelerator_total_memory_mib)
        if isinstance(baseline_ebs_bandwidth_mbps, dict):
            baseline_ebs_bandwidth_mbps = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps(**baseline_ebs_bandwidth_mbps)
        if isinstance(memory_gib_per_vcpu, dict):
            memory_gib_per_vcpu = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu(**memory_gib_per_vcpu)
        if isinstance(memory_mib, dict):
            memory_mib = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib(**memory_mib)
        if isinstance(network_interface_count, dict):
            network_interface_count = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount(**network_interface_count)
        if isinstance(total_local_storage_gb, dict):
            total_local_storage_gb = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb(**total_local_storage_gb)
        if isinstance(vcpu_count, dict):
            vcpu_count = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount(**vcpu_count)
        if __debug__:
            def stub(
                *,
                accelerator_count: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount, typing.Dict[str, typing.Any]]] = None,
                accelerator_manufacturers: typing.Optional[typing.Sequence[builtins.str]] = None,
                accelerator_names: typing.Optional[typing.Sequence[builtins.str]] = None,
                accelerator_total_memory_mib: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib, typing.Dict[str, typing.Any]]] = None,
                accelerator_types: typing.Optional[typing.Sequence[builtins.str]] = None,
                bare_metal: typing.Optional[builtins.str] = None,
                baseline_ebs_bandwidth_mbps: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps, typing.Dict[str, typing.Any]]] = None,
                burstable_performance: typing.Optional[builtins.str] = None,
                cpu_manufacturers: typing.Optional[typing.Sequence[builtins.str]] = None,
                excluded_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
                instance_generations: typing.Optional[typing.Sequence[builtins.str]] = None,
                local_storage: typing.Optional[builtins.str] = None,
                local_storage_types: typing.Optional[typing.Sequence[builtins.str]] = None,
                memory_gib_per_vcpu: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu, typing.Dict[str, typing.Any]]] = None,
                memory_mib: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib, typing.Dict[str, typing.Any]]] = None,
                network_interface_count: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount, typing.Dict[str, typing.Any]]] = None,
                on_demand_max_price_percentage_over_lowest_price: typing.Optional[jsii.Number] = None,
                require_hibernate_support: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                spot_max_price_percentage_over_lowest_price: typing.Optional[jsii.Number] = None,
                total_local_storage_gb: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb, typing.Dict[str, typing.Any]]] = None,
                vcpu_count: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument accelerator_count", value=accelerator_count, expected_type=type_hints["accelerator_count"])
            check_type(argname="argument accelerator_manufacturers", value=accelerator_manufacturers, expected_type=type_hints["accelerator_manufacturers"])
            check_type(argname="argument accelerator_names", value=accelerator_names, expected_type=type_hints["accelerator_names"])
            check_type(argname="argument accelerator_total_memory_mib", value=accelerator_total_memory_mib, expected_type=type_hints["accelerator_total_memory_mib"])
            check_type(argname="argument accelerator_types", value=accelerator_types, expected_type=type_hints["accelerator_types"])
            check_type(argname="argument bare_metal", value=bare_metal, expected_type=type_hints["bare_metal"])
            check_type(argname="argument baseline_ebs_bandwidth_mbps", value=baseline_ebs_bandwidth_mbps, expected_type=type_hints["baseline_ebs_bandwidth_mbps"])
            check_type(argname="argument burstable_performance", value=burstable_performance, expected_type=type_hints["burstable_performance"])
            check_type(argname="argument cpu_manufacturers", value=cpu_manufacturers, expected_type=type_hints["cpu_manufacturers"])
            check_type(argname="argument excluded_instance_types", value=excluded_instance_types, expected_type=type_hints["excluded_instance_types"])
            check_type(argname="argument instance_generations", value=instance_generations, expected_type=type_hints["instance_generations"])
            check_type(argname="argument local_storage", value=local_storage, expected_type=type_hints["local_storage"])
            check_type(argname="argument local_storage_types", value=local_storage_types, expected_type=type_hints["local_storage_types"])
            check_type(argname="argument memory_gib_per_vcpu", value=memory_gib_per_vcpu, expected_type=type_hints["memory_gib_per_vcpu"])
            check_type(argname="argument memory_mib", value=memory_mib, expected_type=type_hints["memory_mib"])
            check_type(argname="argument network_interface_count", value=network_interface_count, expected_type=type_hints["network_interface_count"])
            check_type(argname="argument on_demand_max_price_percentage_over_lowest_price", value=on_demand_max_price_percentage_over_lowest_price, expected_type=type_hints["on_demand_max_price_percentage_over_lowest_price"])
            check_type(argname="argument require_hibernate_support", value=require_hibernate_support, expected_type=type_hints["require_hibernate_support"])
            check_type(argname="argument spot_max_price_percentage_over_lowest_price", value=spot_max_price_percentage_over_lowest_price, expected_type=type_hints["spot_max_price_percentage_over_lowest_price"])
            check_type(argname="argument total_local_storage_gb", value=total_local_storage_gb, expected_type=type_hints["total_local_storage_gb"])
            check_type(argname="argument vcpu_count", value=vcpu_count, expected_type=type_hints["vcpu_count"])
        self._values: typing.Dict[str, typing.Any] = {}
        if accelerator_count is not None:
            self._values["accelerator_count"] = accelerator_count
        if accelerator_manufacturers is not None:
            self._values["accelerator_manufacturers"] = accelerator_manufacturers
        if accelerator_names is not None:
            self._values["accelerator_names"] = accelerator_names
        if accelerator_total_memory_mib is not None:
            self._values["accelerator_total_memory_mib"] = accelerator_total_memory_mib
        if accelerator_types is not None:
            self._values["accelerator_types"] = accelerator_types
        if bare_metal is not None:
            self._values["bare_metal"] = bare_metal
        if baseline_ebs_bandwidth_mbps is not None:
            self._values["baseline_ebs_bandwidth_mbps"] = baseline_ebs_bandwidth_mbps
        if burstable_performance is not None:
            self._values["burstable_performance"] = burstable_performance
        if cpu_manufacturers is not None:
            self._values["cpu_manufacturers"] = cpu_manufacturers
        if excluded_instance_types is not None:
            self._values["excluded_instance_types"] = excluded_instance_types
        if instance_generations is not None:
            self._values["instance_generations"] = instance_generations
        if local_storage is not None:
            self._values["local_storage"] = local_storage
        if local_storage_types is not None:
            self._values["local_storage_types"] = local_storage_types
        if memory_gib_per_vcpu is not None:
            self._values["memory_gib_per_vcpu"] = memory_gib_per_vcpu
        if memory_mib is not None:
            self._values["memory_mib"] = memory_mib
        if network_interface_count is not None:
            self._values["network_interface_count"] = network_interface_count
        if on_demand_max_price_percentage_over_lowest_price is not None:
            self._values["on_demand_max_price_percentage_over_lowest_price"] = on_demand_max_price_percentage_over_lowest_price
        if require_hibernate_support is not None:
            self._values["require_hibernate_support"] = require_hibernate_support
        if spot_max_price_percentage_over_lowest_price is not None:
            self._values["spot_max_price_percentage_over_lowest_price"] = spot_max_price_percentage_over_lowest_price
        if total_local_storage_gb is not None:
            self._values["total_local_storage_gb"] = total_local_storage_gb
        if vcpu_count is not None:
            self._values["vcpu_count"] = vcpu_count

    @builtins.property
    def accelerator_count(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount"]:
        '''accelerator_count block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_count AutoscalingGroup#accelerator_count}
        '''
        result = self._values.get("accelerator_count")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount"], result)

    @builtins.property
    def accelerator_manufacturers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_manufacturers AutoscalingGroup#accelerator_manufacturers}.'''
        result = self._values.get("accelerator_manufacturers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def accelerator_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_names AutoscalingGroup#accelerator_names}.'''
        result = self._values.get("accelerator_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def accelerator_total_memory_mib(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib"]:
        '''accelerator_total_memory_mib block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_total_memory_mib AutoscalingGroup#accelerator_total_memory_mib}
        '''
        result = self._values.get("accelerator_total_memory_mib")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib"], result)

    @builtins.property
    def accelerator_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_types AutoscalingGroup#accelerator_types}.'''
        result = self._values.get("accelerator_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def bare_metal(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#bare_metal AutoscalingGroup#bare_metal}.'''
        result = self._values.get("bare_metal")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def baseline_ebs_bandwidth_mbps(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps"]:
        '''baseline_ebs_bandwidth_mbps block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#baseline_ebs_bandwidth_mbps AutoscalingGroup#baseline_ebs_bandwidth_mbps}
        '''
        result = self._values.get("baseline_ebs_bandwidth_mbps")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps"], result)

    @builtins.property
    def burstable_performance(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#burstable_performance AutoscalingGroup#burstable_performance}.'''
        result = self._values.get("burstable_performance")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cpu_manufacturers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#cpu_manufacturers AutoscalingGroup#cpu_manufacturers}.'''
        result = self._values.get("cpu_manufacturers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def excluded_instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#excluded_instance_types AutoscalingGroup#excluded_instance_types}.'''
        result = self._values.get("excluded_instance_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def instance_generations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_generations AutoscalingGroup#instance_generations}.'''
        result = self._values.get("instance_generations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def local_storage(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#local_storage AutoscalingGroup#local_storage}.'''
        result = self._values.get("local_storage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_storage_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#local_storage_types AutoscalingGroup#local_storage_types}.'''
        result = self._values.get("local_storage_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def memory_gib_per_vcpu(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu"]:
        '''memory_gib_per_vcpu block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#memory_gib_per_vcpu AutoscalingGroup#memory_gib_per_vcpu}
        '''
        result = self._values.get("memory_gib_per_vcpu")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu"], result)

    @builtins.property
    def memory_mib(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib"]:
        '''memory_mib block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#memory_mib AutoscalingGroup#memory_mib}
        '''
        result = self._values.get("memory_mib")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib"], result)

    @builtins.property
    def network_interface_count(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount"]:
        '''network_interface_count block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#network_interface_count AutoscalingGroup#network_interface_count}
        '''
        result = self._values.get("network_interface_count")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount"], result)

    @builtins.property
    def on_demand_max_price_percentage_over_lowest_price(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_max_price_percentage_over_lowest_price AutoscalingGroup#on_demand_max_price_percentage_over_lowest_price}.'''
        result = self._values.get("on_demand_max_price_percentage_over_lowest_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def require_hibernate_support(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#require_hibernate_support AutoscalingGroup#require_hibernate_support}.'''
        result = self._values.get("require_hibernate_support")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def spot_max_price_percentage_over_lowest_price(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_max_price_percentage_over_lowest_price AutoscalingGroup#spot_max_price_percentage_over_lowest_price}.'''
        result = self._values.get("spot_max_price_percentage_over_lowest_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def total_local_storage_gb(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb"]:
        '''total_local_storage_gb block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#total_local_storage_gb AutoscalingGroup#total_local_storage_gb}
        '''
        result = self._values.get("total_local_storage_gb")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb"], result)

    @builtins.property
    def vcpu_count(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount"]:
        '''vcpu_count block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#vcpu_count AutoscalingGroup#vcpu_count}
        '''
        result = self._values.get("vcpu_count")
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        if __debug__:
            def stub(
                *,
                max: typing.Optional[jsii.Number] = None,
                min: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountOutputReference",
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

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        if __debug__:
            def stub(
                *,
                max: typing.Optional[jsii.Number] = None,
                min: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibOutputReference",
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

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        if __debug__:
            def stub(
                *,
                max: typing.Optional[jsii.Number] = None,
                min: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference",
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

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        if __debug__:
            def stub(
                *,
                max: typing.Optional[jsii.Number] = None,
                min: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuOutputReference",
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

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        if __debug__:
            def stub(
                *,
                max: typing.Optional[jsii.Number] = None,
                min: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibOutputReference",
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

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        if __debug__:
            def stub(
                *,
                max: typing.Optional[jsii.Number] = None,
                min: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountOutputReference",
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

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference",
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

    @jsii.member(jsii_name="putAcceleratorCount")
    def put_accelerator_count(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putAcceleratorCount", [value]))

    @jsii.member(jsii_name="putAcceleratorTotalMemoryMib")
    def put_accelerator_total_memory_mib(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putAcceleratorTotalMemoryMib", [value]))

    @jsii.member(jsii_name="putBaselineEbsBandwidthMbps")
    def put_baseline_ebs_bandwidth_mbps(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putBaselineEbsBandwidthMbps", [value]))

    @jsii.member(jsii_name="putMemoryGibPerVcpu")
    def put_memory_gib_per_vcpu(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putMemoryGibPerVcpu", [value]))

    @jsii.member(jsii_name="putMemoryMib")
    def put_memory_mib(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putMemoryMib", [value]))

    @jsii.member(jsii_name="putNetworkInterfaceCount")
    def put_network_interface_count(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkInterfaceCount", [value]))

    @jsii.member(jsii_name="putTotalLocalStorageGb")
    def put_total_local_storage_gb(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putTotalLocalStorageGb", [value]))

    @jsii.member(jsii_name="putVcpuCount")
    def put_vcpu_count(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount(
            max=max, min=min
        )

        return typing.cast(None, jsii.invoke(self, "putVcpuCount", [value]))

    @jsii.member(jsii_name="resetAcceleratorCount")
    def reset_accelerator_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorCount", []))

    @jsii.member(jsii_name="resetAcceleratorManufacturers")
    def reset_accelerator_manufacturers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorManufacturers", []))

    @jsii.member(jsii_name="resetAcceleratorNames")
    def reset_accelerator_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorNames", []))

    @jsii.member(jsii_name="resetAcceleratorTotalMemoryMib")
    def reset_accelerator_total_memory_mib(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorTotalMemoryMib", []))

    @jsii.member(jsii_name="resetAcceleratorTypes")
    def reset_accelerator_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorTypes", []))

    @jsii.member(jsii_name="resetBareMetal")
    def reset_bare_metal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBareMetal", []))

    @jsii.member(jsii_name="resetBaselineEbsBandwidthMbps")
    def reset_baseline_ebs_bandwidth_mbps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaselineEbsBandwidthMbps", []))

    @jsii.member(jsii_name="resetBurstablePerformance")
    def reset_burstable_performance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBurstablePerformance", []))

    @jsii.member(jsii_name="resetCpuManufacturers")
    def reset_cpu_manufacturers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuManufacturers", []))

    @jsii.member(jsii_name="resetExcludedInstanceTypes")
    def reset_excluded_instance_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludedInstanceTypes", []))

    @jsii.member(jsii_name="resetInstanceGenerations")
    def reset_instance_generations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceGenerations", []))

    @jsii.member(jsii_name="resetLocalStorage")
    def reset_local_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalStorage", []))

    @jsii.member(jsii_name="resetLocalStorageTypes")
    def reset_local_storage_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalStorageTypes", []))

    @jsii.member(jsii_name="resetMemoryGibPerVcpu")
    def reset_memory_gib_per_vcpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryGibPerVcpu", []))

    @jsii.member(jsii_name="resetMemoryMib")
    def reset_memory_mib(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryMib", []))

    @jsii.member(jsii_name="resetNetworkInterfaceCount")
    def reset_network_interface_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkInterfaceCount", []))

    @jsii.member(jsii_name="resetOnDemandMaxPricePercentageOverLowestPrice")
    def reset_on_demand_max_price_percentage_over_lowest_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnDemandMaxPricePercentageOverLowestPrice", []))

    @jsii.member(jsii_name="resetRequireHibernateSupport")
    def reset_require_hibernate_support(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireHibernateSupport", []))

    @jsii.member(jsii_name="resetSpotMaxPricePercentageOverLowestPrice")
    def reset_spot_max_price_percentage_over_lowest_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotMaxPricePercentageOverLowestPrice", []))

    @jsii.member(jsii_name="resetTotalLocalStorageGb")
    def reset_total_local_storage_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTotalLocalStorageGb", []))

    @jsii.member(jsii_name="resetVcpuCount")
    def reset_vcpu_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVcpuCount", []))

    @builtins.property
    @jsii.member(jsii_name="acceleratorCount")
    def accelerator_count(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountOutputReference, jsii.get(self, "acceleratorCount"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorTotalMemoryMib")
    def accelerator_total_memory_mib(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibOutputReference, jsii.get(self, "acceleratorTotalMemoryMib"))

    @builtins.property
    @jsii.member(jsii_name="baselineEbsBandwidthMbps")
    def baseline_ebs_bandwidth_mbps(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference, jsii.get(self, "baselineEbsBandwidthMbps"))

    @builtins.property
    @jsii.member(jsii_name="memoryGibPerVcpu")
    def memory_gib_per_vcpu(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuOutputReference, jsii.get(self, "memoryGibPerVcpu"))

    @builtins.property
    @jsii.member(jsii_name="memoryMib")
    def memory_mib(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibOutputReference, jsii.get(self, "memoryMib"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceCount")
    def network_interface_count(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountOutputReference, jsii.get(self, "networkInterfaceCount"))

    @builtins.property
    @jsii.member(jsii_name="totalLocalStorageGb")
    def total_local_storage_gb(
        self,
    ) -> "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbOutputReference":
        return typing.cast("AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbOutputReference", jsii.get(self, "totalLocalStorageGb"))

    @builtins.property
    @jsii.member(jsii_name="vcpuCount")
    def vcpu_count(
        self,
    ) -> "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountOutputReference":
        return typing.cast("AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountOutputReference", jsii.get(self, "vcpuCount"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorCountInput")
    def accelerator_count_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount], jsii.get(self, "acceleratorCountInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorManufacturersInput")
    def accelerator_manufacturers_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "acceleratorManufacturersInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorNamesInput")
    def accelerator_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "acceleratorNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorTotalMemoryMibInput")
    def accelerator_total_memory_mib_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib], jsii.get(self, "acceleratorTotalMemoryMibInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorTypesInput")
    def accelerator_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "acceleratorTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="bareMetalInput")
    def bare_metal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bareMetalInput"))

    @builtins.property
    @jsii.member(jsii_name="baselineEbsBandwidthMbpsInput")
    def baseline_ebs_bandwidth_mbps_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps], jsii.get(self, "baselineEbsBandwidthMbpsInput"))

    @builtins.property
    @jsii.member(jsii_name="burstablePerformanceInput")
    def burstable_performance_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "burstablePerformanceInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuManufacturersInput")
    def cpu_manufacturers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cpuManufacturersInput"))

    @builtins.property
    @jsii.member(jsii_name="excludedInstanceTypesInput")
    def excluded_instance_types_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludedInstanceTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceGenerationsInput")
    def instance_generations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instanceGenerationsInput"))

    @builtins.property
    @jsii.member(jsii_name="localStorageInput")
    def local_storage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="localStorageTypesInput")
    def local_storage_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "localStorageTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryGibPerVcpuInput")
    def memory_gib_per_vcpu_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu], jsii.get(self, "memoryGibPerVcpuInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryMibInput")
    def memory_mib_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib], jsii.get(self, "memoryMibInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceCountInput")
    def network_interface_count_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount], jsii.get(self, "networkInterfaceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="onDemandMaxPricePercentageOverLowestPriceInput")
    def on_demand_max_price_percentage_over_lowest_price_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "onDemandMaxPricePercentageOverLowestPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="requireHibernateSupportInput")
    def require_hibernate_support_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireHibernateSupportInput"))

    @builtins.property
    @jsii.member(jsii_name="spotMaxPricePercentageOverLowestPriceInput")
    def spot_max_price_percentage_over_lowest_price_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "spotMaxPricePercentageOverLowestPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="totalLocalStorageGbInput")
    def total_local_storage_gb_input(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb"]:
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb"], jsii.get(self, "totalLocalStorageGbInput"))

    @builtins.property
    @jsii.member(jsii_name="vcpuCountInput")
    def vcpu_count_input(
        self,
    ) -> typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount"]:
        return typing.cast(typing.Optional["AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount"], jsii.get(self, "vcpuCountInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorManufacturers")
    def accelerator_manufacturers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "acceleratorManufacturers"))

    @accelerator_manufacturers.setter
    def accelerator_manufacturers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorManufacturers", value)

    @builtins.property
    @jsii.member(jsii_name="acceleratorNames")
    def accelerator_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "acceleratorNames"))

    @accelerator_names.setter
    def accelerator_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorNames", value)

    @builtins.property
    @jsii.member(jsii_name="acceleratorTypes")
    def accelerator_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "acceleratorTypes"))

    @accelerator_types.setter
    def accelerator_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorTypes", value)

    @builtins.property
    @jsii.member(jsii_name="bareMetal")
    def bare_metal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bareMetal"))

    @bare_metal.setter
    def bare_metal(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bareMetal", value)

    @builtins.property
    @jsii.member(jsii_name="burstablePerformance")
    def burstable_performance(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "burstablePerformance"))

    @burstable_performance.setter
    def burstable_performance(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "burstablePerformance", value)

    @builtins.property
    @jsii.member(jsii_name="cpuManufacturers")
    def cpu_manufacturers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cpuManufacturers"))

    @cpu_manufacturers.setter
    def cpu_manufacturers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuManufacturers", value)

    @builtins.property
    @jsii.member(jsii_name="excludedInstanceTypes")
    def excluded_instance_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludedInstanceTypes"))

    @excluded_instance_types.setter
    def excluded_instance_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedInstanceTypes", value)

    @builtins.property
    @jsii.member(jsii_name="instanceGenerations")
    def instance_generations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceGenerations"))

    @instance_generations.setter
    def instance_generations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceGenerations", value)

    @builtins.property
    @jsii.member(jsii_name="localStorage")
    def local_storage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localStorage"))

    @local_storage.setter
    def local_storage(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localStorage", value)

    @builtins.property
    @jsii.member(jsii_name="localStorageTypes")
    def local_storage_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "localStorageTypes"))

    @local_storage_types.setter
    def local_storage_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localStorageTypes", value)

    @builtins.property
    @jsii.member(jsii_name="onDemandMaxPricePercentageOverLowestPrice")
    def on_demand_max_price_percentage_over_lowest_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "onDemandMaxPricePercentageOverLowestPrice"))

    @on_demand_max_price_percentage_over_lowest_price.setter
    def on_demand_max_price_percentage_over_lowest_price(
        self,
        value: jsii.Number,
    ) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onDemandMaxPricePercentageOverLowestPrice", value)

    @builtins.property
    @jsii.member(jsii_name="requireHibernateSupport")
    def require_hibernate_support(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireHibernateSupport"))

    @require_hibernate_support.setter
    def require_hibernate_support(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireHibernateSupport", value)

    @builtins.property
    @jsii.member(jsii_name="spotMaxPricePercentageOverLowestPrice")
    def spot_max_price_percentage_over_lowest_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotMaxPricePercentageOverLowestPrice"))

    @spot_max_price_percentage_over_lowest_price.setter
    def spot_max_price_percentage_over_lowest_price(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotMaxPricePercentageOverLowestPrice", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        if __debug__:
            def stub(
                *,
                max: typing.Optional[jsii.Number] = None,
                min: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbOutputReference",
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

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount:
    def __init__(
        self,
        *,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.
        :param min: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.
        '''
        if __debug__:
            def stub(
                *,
                max: typing.Optional[jsii.Number] = None,
                min: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max AutoscalingGroup#max}.'''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min AutoscalingGroup#min}.'''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountOutputReference",
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

    @jsii.member(jsii_name="resetMax")
    def reset_max(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMax", []))

    @jsii.member(jsii_name="resetMin")
    def reset_min(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMin", []))

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "launch_template_id": "launchTemplateId",
        "launch_template_name": "launchTemplateName",
        "version": "version",
    },
)
class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification:
    def __init__(
        self,
        *,
        launch_template_id: typing.Optional[builtins.str] = None,
        launch_template_name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param launch_template_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_id AutoscalingGroup#launch_template_id}.
        :param launch_template_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_name AutoscalingGroup#launch_template_name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#version AutoscalingGroup#version}.
        '''
        if __debug__:
            def stub(
                *,
                launch_template_id: typing.Optional[builtins.str] = None,
                launch_template_name: typing.Optional[builtins.str] = None,
                version: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument launch_template_id", value=launch_template_id, expected_type=type_hints["launch_template_id"])
            check_type(argname="argument launch_template_name", value=launch_template_name, expected_type=type_hints["launch_template_name"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if launch_template_id is not None:
            self._values["launch_template_id"] = launch_template_id
        if launch_template_name is not None:
            self._values["launch_template_name"] = launch_template_name
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def launch_template_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_id AutoscalingGroup#launch_template_id}.'''
        result = self._values.get("launch_template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_template_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_name AutoscalingGroup#launch_template_name}.'''
        result = self._values.get("launch_template_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#version AutoscalingGroup#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationOutputReference",
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

    @jsii.member(jsii_name="resetLaunchTemplateId")
    def reset_launch_template_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplateId", []))

    @jsii.member(jsii_name="resetLaunchTemplateName")
    def reset_launch_template_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplateName", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateIdInput")
    def launch_template_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTemplateIdInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateNameInput")
    def launch_template_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTemplateNameInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateId")
    def launch_template_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchTemplateId"))

    @launch_template_id.setter
    def launch_template_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchTemplateId", value)

    @builtins.property
    @jsii.member(jsii_name="launchTemplateName")
    def launch_template_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchTemplateName"))

    @launch_template_name.setter
    def launch_template_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchTemplateName", value)

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

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideList",
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
    ) -> "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideOutputReference",
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

    @jsii.member(jsii_name="putInstanceRequirements")
    def put_instance_requirements(
        self,
        *,
        accelerator_count: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount, typing.Dict[str, typing.Any]]] = None,
        accelerator_manufacturers: typing.Optional[typing.Sequence[builtins.str]] = None,
        accelerator_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        accelerator_total_memory_mib: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib, typing.Dict[str, typing.Any]]] = None,
        accelerator_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        bare_metal: typing.Optional[builtins.str] = None,
        baseline_ebs_bandwidth_mbps: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps, typing.Dict[str, typing.Any]]] = None,
        burstable_performance: typing.Optional[builtins.str] = None,
        cpu_manufacturers: typing.Optional[typing.Sequence[builtins.str]] = None,
        excluded_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        instance_generations: typing.Optional[typing.Sequence[builtins.str]] = None,
        local_storage: typing.Optional[builtins.str] = None,
        local_storage_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        memory_gib_per_vcpu: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu, typing.Dict[str, typing.Any]]] = None,
        memory_mib: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib, typing.Dict[str, typing.Any]]] = None,
        network_interface_count: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount, typing.Dict[str, typing.Any]]] = None,
        on_demand_max_price_percentage_over_lowest_price: typing.Optional[jsii.Number] = None,
        require_hibernate_support: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        spot_max_price_percentage_over_lowest_price: typing.Optional[jsii.Number] = None,
        total_local_storage_gb: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb, typing.Dict[str, typing.Any]]] = None,
        vcpu_count: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param accelerator_count: accelerator_count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_count AutoscalingGroup#accelerator_count}
        :param accelerator_manufacturers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_manufacturers AutoscalingGroup#accelerator_manufacturers}.
        :param accelerator_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_names AutoscalingGroup#accelerator_names}.
        :param accelerator_total_memory_mib: accelerator_total_memory_mib block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_total_memory_mib AutoscalingGroup#accelerator_total_memory_mib}
        :param accelerator_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#accelerator_types AutoscalingGroup#accelerator_types}.
        :param bare_metal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#bare_metal AutoscalingGroup#bare_metal}.
        :param baseline_ebs_bandwidth_mbps: baseline_ebs_bandwidth_mbps block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#baseline_ebs_bandwidth_mbps AutoscalingGroup#baseline_ebs_bandwidth_mbps}
        :param burstable_performance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#burstable_performance AutoscalingGroup#burstable_performance}.
        :param cpu_manufacturers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#cpu_manufacturers AutoscalingGroup#cpu_manufacturers}.
        :param excluded_instance_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#excluded_instance_types AutoscalingGroup#excluded_instance_types}.
        :param instance_generations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_generations AutoscalingGroup#instance_generations}.
        :param local_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#local_storage AutoscalingGroup#local_storage}.
        :param local_storage_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#local_storage_types AutoscalingGroup#local_storage_types}.
        :param memory_gib_per_vcpu: memory_gib_per_vcpu block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#memory_gib_per_vcpu AutoscalingGroup#memory_gib_per_vcpu}
        :param memory_mib: memory_mib block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#memory_mib AutoscalingGroup#memory_mib}
        :param network_interface_count: network_interface_count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#network_interface_count AutoscalingGroup#network_interface_count}
        :param on_demand_max_price_percentage_over_lowest_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_max_price_percentage_over_lowest_price AutoscalingGroup#on_demand_max_price_percentage_over_lowest_price}.
        :param require_hibernate_support: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#require_hibernate_support AutoscalingGroup#require_hibernate_support}.
        :param spot_max_price_percentage_over_lowest_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_max_price_percentage_over_lowest_price AutoscalingGroup#spot_max_price_percentage_over_lowest_price}.
        :param total_local_storage_gb: total_local_storage_gb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#total_local_storage_gb AutoscalingGroup#total_local_storage_gb}
        :param vcpu_count: vcpu_count block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#vcpu_count AutoscalingGroup#vcpu_count}
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements(
            accelerator_count=accelerator_count,
            accelerator_manufacturers=accelerator_manufacturers,
            accelerator_names=accelerator_names,
            accelerator_total_memory_mib=accelerator_total_memory_mib,
            accelerator_types=accelerator_types,
            bare_metal=bare_metal,
            baseline_ebs_bandwidth_mbps=baseline_ebs_bandwidth_mbps,
            burstable_performance=burstable_performance,
            cpu_manufacturers=cpu_manufacturers,
            excluded_instance_types=excluded_instance_types,
            instance_generations=instance_generations,
            local_storage=local_storage,
            local_storage_types=local_storage_types,
            memory_gib_per_vcpu=memory_gib_per_vcpu,
            memory_mib=memory_mib,
            network_interface_count=network_interface_count,
            on_demand_max_price_percentage_over_lowest_price=on_demand_max_price_percentage_over_lowest_price,
            require_hibernate_support=require_hibernate_support,
            spot_max_price_percentage_over_lowest_price=spot_max_price_percentage_over_lowest_price,
            total_local_storage_gb=total_local_storage_gb,
            vcpu_count=vcpu_count,
        )

        return typing.cast(None, jsii.invoke(self, "putInstanceRequirements", [value]))

    @jsii.member(jsii_name="putLaunchTemplateSpecification")
    def put_launch_template_specification(
        self,
        *,
        launch_template_id: typing.Optional[builtins.str] = None,
        launch_template_name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param launch_template_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_id AutoscalingGroup#launch_template_id}.
        :param launch_template_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_name AutoscalingGroup#launch_template_name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#version AutoscalingGroup#version}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification(
            launch_template_id=launch_template_id,
            launch_template_name=launch_template_name,
            version=version,
        )

        return typing.cast(None, jsii.invoke(self, "putLaunchTemplateSpecification", [value]))

    @jsii.member(jsii_name="resetInstanceRequirements")
    def reset_instance_requirements(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceRequirements", []))

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLaunchTemplateSpecification")
    def reset_launch_template_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchTemplateSpecification", []))

    @jsii.member(jsii_name="resetWeightedCapacity")
    def reset_weighted_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeightedCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="instanceRequirements")
    def instance_requirements(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference, jsii.get(self, "instanceRequirements"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateSpecification")
    def launch_template_specification(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationOutputReference, jsii.get(self, "launchTemplateSpecification"))

    @builtins.property
    @jsii.member(jsii_name="instanceRequirementsInput")
    def instance_requirements_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements], jsii.get(self, "instanceRequirementsInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateSpecificationInput")
    def launch_template_specification_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification], jsii.get(self, "launchTemplateSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="weightedCapacityInput")
    def weighted_capacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "weightedCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="weightedCapacity")
    def weighted_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "weightedCapacity"))

    @weighted_capacity.setter
    def weighted_capacity(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weightedCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingGroupMixedInstancesPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupMixedInstancesPolicyOutputReference",
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

    @jsii.member(jsii_name="putInstancesDistribution")
    def put_instances_distribution(
        self,
        *,
        on_demand_allocation_strategy: typing.Optional[builtins.str] = None,
        on_demand_base_capacity: typing.Optional[jsii.Number] = None,
        on_demand_percentage_above_base_capacity: typing.Optional[jsii.Number] = None,
        spot_allocation_strategy: typing.Optional[builtins.str] = None,
        spot_instance_pools: typing.Optional[jsii.Number] = None,
        spot_max_price: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param on_demand_allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_allocation_strategy AutoscalingGroup#on_demand_allocation_strategy}.
        :param on_demand_base_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_base_capacity AutoscalingGroup#on_demand_base_capacity}.
        :param on_demand_percentage_above_base_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#on_demand_percentage_above_base_capacity AutoscalingGroup#on_demand_percentage_above_base_capacity}.
        :param spot_allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_allocation_strategy AutoscalingGroup#spot_allocation_strategy}.
        :param spot_instance_pools: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_instance_pools AutoscalingGroup#spot_instance_pools}.
        :param spot_max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#spot_max_price AutoscalingGroup#spot_max_price}.
        '''
        value = AutoscalingGroupMixedInstancesPolicyInstancesDistribution(
            on_demand_allocation_strategy=on_demand_allocation_strategy,
            on_demand_base_capacity=on_demand_base_capacity,
            on_demand_percentage_above_base_capacity=on_demand_percentage_above_base_capacity,
            spot_allocation_strategy=spot_allocation_strategy,
            spot_instance_pools=spot_instance_pools,
            spot_max_price=spot_max_price,
        )

        return typing.cast(None, jsii.invoke(self, "putInstancesDistribution", [value]))

    @jsii.member(jsii_name="putLaunchTemplate")
    def put_launch_template(
        self,
        *,
        launch_template_specification: typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification, typing.Dict[str, typing.Any]],
        override: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param launch_template_specification: launch_template_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#launch_template_specification AutoscalingGroup#launch_template_specification}
        :param override: override block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#override AutoscalingGroup#override}
        '''
        value = AutoscalingGroupMixedInstancesPolicyLaunchTemplate(
            launch_template_specification=launch_template_specification,
            override=override,
        )

        return typing.cast(None, jsii.invoke(self, "putLaunchTemplate", [value]))

    @jsii.member(jsii_name="resetInstancesDistribution")
    def reset_instances_distribution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstancesDistribution", []))

    @builtins.property
    @jsii.member(jsii_name="instancesDistribution")
    def instances_distribution(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyInstancesDistributionOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyInstancesDistributionOutputReference, jsii.get(self, "instancesDistribution"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplate")
    def launch_template(
        self,
    ) -> AutoscalingGroupMixedInstancesPolicyLaunchTemplateOutputReference:
        return typing.cast(AutoscalingGroupMixedInstancesPolicyLaunchTemplateOutputReference, jsii.get(self, "launchTemplate"))

    @builtins.property
    @jsii.member(jsii_name="instancesDistributionInput")
    def instances_distribution_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyInstancesDistribution]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyInstancesDistribution], jsii.get(self, "instancesDistributionInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateInput")
    def launch_template_input(
        self,
    ) -> typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplate]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicyLaunchTemplate], jsii.get(self, "launchTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AutoscalingGroupMixedInstancesPolicy]:
        return typing.cast(typing.Optional[AutoscalingGroupMixedInstancesPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupMixedInstancesPolicy],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AutoscalingGroupMixedInstancesPolicy],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupTag",
    jsii_struct_bases=[],
    name_mapping={
        "key": "key",
        "propagate_at_launch": "propagateAtLaunch",
        "value": "value",
    },
)
class AutoscalingGroupTag:
    def __init__(
        self,
        *,
        key: builtins.str,
        propagate_at_launch: typing.Union[builtins.bool, cdktf.IResolvable],
        value: builtins.str,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#key AutoscalingGroup#key}.
        :param propagate_at_launch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#propagate_at_launch AutoscalingGroup#propagate_at_launch}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#value AutoscalingGroup#value}.
        '''
        if __debug__:
            def stub(
                *,
                key: builtins.str,
                propagate_at_launch: typing.Union[builtins.bool, cdktf.IResolvable],
                value: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument propagate_at_launch", value=propagate_at_launch, expected_type=type_hints["propagate_at_launch"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "propagate_at_launch": propagate_at_launch,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#key AutoscalingGroup#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def propagate_at_launch(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#propagate_at_launch AutoscalingGroup#propagate_at_launch}.'''
        result = self._values.get("propagate_at_launch")
        assert result is not None, "Required property 'propagate_at_launch' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#value AutoscalingGroup#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupTagList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupTagList",
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
    def get(self, index: jsii.Number) -> "AutoscalingGroupTagOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutoscalingGroupTagOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupTag]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupTag]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupTag]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutoscalingGroupTag]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingGroupTagOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupTagOutputReference",
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
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="propagateAtLaunchInput")
    def propagate_at_launch_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "propagateAtLaunchInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="propagateAtLaunch")
    def propagate_at_launch(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "propagateAtLaunch"))

    @propagate_at_launch.setter
    def propagate_at_launch(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagateAtLaunch", value)

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
    ) -> typing.Optional[typing.Union[AutoscalingGroupTag, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingGroupTag, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingGroupTag, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[AutoscalingGroupTag, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupTimeouts",
    jsii_struct_bases=[],
    name_mapping={"delete": "delete", "update": "update"},
)
class AutoscalingGroupTimeouts:
    def __init__(
        self,
        *,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#delete AutoscalingGroup#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#update AutoscalingGroup#update}.
        '''
        if __debug__:
            def stub(
                *,
                delete: typing.Optional[builtins.str] = None,
                update: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#delete AutoscalingGroup#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#update AutoscalingGroup#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupTimeoutsOutputReference",
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

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

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
    ) -> typing.Optional[typing.Union[AutoscalingGroupTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutoscalingGroupTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutoscalingGroupTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[AutoscalingGroupTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupWarmPool",
    jsii_struct_bases=[],
    name_mapping={
        "instance_reuse_policy": "instanceReusePolicy",
        "max_group_prepared_capacity": "maxGroupPreparedCapacity",
        "min_size": "minSize",
        "pool_state": "poolState",
    },
)
class AutoscalingGroupWarmPool:
    def __init__(
        self,
        *,
        instance_reuse_policy: typing.Optional[typing.Union["AutoscalingGroupWarmPoolInstanceReusePolicy", typing.Dict[str, typing.Any]]] = None,
        max_group_prepared_capacity: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        pool_state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_reuse_policy: instance_reuse_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_reuse_policy AutoscalingGroup#instance_reuse_policy}
        :param max_group_prepared_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max_group_prepared_capacity AutoscalingGroup#max_group_prepared_capacity}.
        :param min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_size AutoscalingGroup#min_size}.
        :param pool_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#pool_state AutoscalingGroup#pool_state}.
        '''
        if isinstance(instance_reuse_policy, dict):
            instance_reuse_policy = AutoscalingGroupWarmPoolInstanceReusePolicy(**instance_reuse_policy)
        if __debug__:
            def stub(
                *,
                instance_reuse_policy: typing.Optional[typing.Union[AutoscalingGroupWarmPoolInstanceReusePolicy, typing.Dict[str, typing.Any]]] = None,
                max_group_prepared_capacity: typing.Optional[jsii.Number] = None,
                min_size: typing.Optional[jsii.Number] = None,
                pool_state: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_reuse_policy", value=instance_reuse_policy, expected_type=type_hints["instance_reuse_policy"])
            check_type(argname="argument max_group_prepared_capacity", value=max_group_prepared_capacity, expected_type=type_hints["max_group_prepared_capacity"])
            check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            check_type(argname="argument pool_state", value=pool_state, expected_type=type_hints["pool_state"])
        self._values: typing.Dict[str, typing.Any] = {}
        if instance_reuse_policy is not None:
            self._values["instance_reuse_policy"] = instance_reuse_policy
        if max_group_prepared_capacity is not None:
            self._values["max_group_prepared_capacity"] = max_group_prepared_capacity
        if min_size is not None:
            self._values["min_size"] = min_size
        if pool_state is not None:
            self._values["pool_state"] = pool_state

    @builtins.property
    def instance_reuse_policy(
        self,
    ) -> typing.Optional["AutoscalingGroupWarmPoolInstanceReusePolicy"]:
        '''instance_reuse_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#instance_reuse_policy AutoscalingGroup#instance_reuse_policy}
        '''
        result = self._values.get("instance_reuse_policy")
        return typing.cast(typing.Optional["AutoscalingGroupWarmPoolInstanceReusePolicy"], result)

    @builtins.property
    def max_group_prepared_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#max_group_prepared_capacity AutoscalingGroup#max_group_prepared_capacity}.'''
        result = self._values.get("max_group_prepared_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#min_size AutoscalingGroup#min_size}.'''
        result = self._values.get("min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pool_state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#pool_state AutoscalingGroup#pool_state}.'''
        result = self._values.get("pool_state")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupWarmPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupWarmPoolInstanceReusePolicy",
    jsii_struct_bases=[],
    name_mapping={"reuse_on_scale_in": "reuseOnScaleIn"},
)
class AutoscalingGroupWarmPoolInstanceReusePolicy:
    def __init__(
        self,
        *,
        reuse_on_scale_in: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param reuse_on_scale_in: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#reuse_on_scale_in AutoscalingGroup#reuse_on_scale_in}.
        '''
        if __debug__:
            def stub(
                *,
                reuse_on_scale_in: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument reuse_on_scale_in", value=reuse_on_scale_in, expected_type=type_hints["reuse_on_scale_in"])
        self._values: typing.Dict[str, typing.Any] = {}
        if reuse_on_scale_in is not None:
            self._values["reuse_on_scale_in"] = reuse_on_scale_in

    @builtins.property
    def reuse_on_scale_in(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#reuse_on_scale_in AutoscalingGroup#reuse_on_scale_in}.'''
        result = self._values.get("reuse_on_scale_in")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoscalingGroupWarmPoolInstanceReusePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoscalingGroupWarmPoolInstanceReusePolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupWarmPoolInstanceReusePolicyOutputReference",
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

    @jsii.member(jsii_name="resetReuseOnScaleIn")
    def reset_reuse_on_scale_in(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReuseOnScaleIn", []))

    @builtins.property
    @jsii.member(jsii_name="reuseOnScaleInInput")
    def reuse_on_scale_in_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "reuseOnScaleInInput"))

    @builtins.property
    @jsii.member(jsii_name="reuseOnScaleIn")
    def reuse_on_scale_in(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "reuseOnScaleIn"))

    @reuse_on_scale_in.setter
    def reuse_on_scale_in(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reuseOnScaleIn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutoscalingGroupWarmPoolInstanceReusePolicy]:
        return typing.cast(typing.Optional[AutoscalingGroupWarmPoolInstanceReusePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutoscalingGroupWarmPoolInstanceReusePolicy],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AutoscalingGroupWarmPoolInstanceReusePolicy],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutoscalingGroupWarmPoolOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.autoscalingGroup.AutoscalingGroupWarmPoolOutputReference",
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

    @jsii.member(jsii_name="putInstanceReusePolicy")
    def put_instance_reuse_policy(
        self,
        *,
        reuse_on_scale_in: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param reuse_on_scale_in: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/autoscaling_group#reuse_on_scale_in AutoscalingGroup#reuse_on_scale_in}.
        '''
        value = AutoscalingGroupWarmPoolInstanceReusePolicy(
            reuse_on_scale_in=reuse_on_scale_in
        )

        return typing.cast(None, jsii.invoke(self, "putInstanceReusePolicy", [value]))

    @jsii.member(jsii_name="resetInstanceReusePolicy")
    def reset_instance_reuse_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceReusePolicy", []))

    @jsii.member(jsii_name="resetMaxGroupPreparedCapacity")
    def reset_max_group_prepared_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxGroupPreparedCapacity", []))

    @jsii.member(jsii_name="resetMinSize")
    def reset_min_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinSize", []))

    @jsii.member(jsii_name="resetPoolState")
    def reset_pool_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPoolState", []))

    @builtins.property
    @jsii.member(jsii_name="instanceReusePolicy")
    def instance_reuse_policy(
        self,
    ) -> AutoscalingGroupWarmPoolInstanceReusePolicyOutputReference:
        return typing.cast(AutoscalingGroupWarmPoolInstanceReusePolicyOutputReference, jsii.get(self, "instanceReusePolicy"))

    @builtins.property
    @jsii.member(jsii_name="instanceReusePolicyInput")
    def instance_reuse_policy_input(
        self,
    ) -> typing.Optional[AutoscalingGroupWarmPoolInstanceReusePolicy]:
        return typing.cast(typing.Optional[AutoscalingGroupWarmPoolInstanceReusePolicy], jsii.get(self, "instanceReusePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="maxGroupPreparedCapacityInput")
    def max_group_prepared_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxGroupPreparedCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="minSizeInput")
    def min_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="poolStateInput")
    def pool_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "poolStateInput"))

    @builtins.property
    @jsii.member(jsii_name="maxGroupPreparedCapacity")
    def max_group_prepared_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxGroupPreparedCapacity"))

    @max_group_prepared_capacity.setter
    def max_group_prepared_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxGroupPreparedCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minSize"))

    @min_size.setter
    def min_size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minSize", value)

    @builtins.property
    @jsii.member(jsii_name="poolState")
    def pool_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "poolState"))

    @pool_state.setter
    def pool_state(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolState", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AutoscalingGroupWarmPool]:
        return typing.cast(typing.Optional[AutoscalingGroupWarmPool], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AutoscalingGroupWarmPool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[AutoscalingGroupWarmPool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AutoscalingGroup",
    "AutoscalingGroupConfig",
    "AutoscalingGroupInitialLifecycleHook",
    "AutoscalingGroupInitialLifecycleHookList",
    "AutoscalingGroupInitialLifecycleHookOutputReference",
    "AutoscalingGroupInstanceRefresh",
    "AutoscalingGroupInstanceRefreshOutputReference",
    "AutoscalingGroupInstanceRefreshPreferences",
    "AutoscalingGroupInstanceRefreshPreferencesOutputReference",
    "AutoscalingGroupLaunchTemplate",
    "AutoscalingGroupLaunchTemplateOutputReference",
    "AutoscalingGroupMixedInstancesPolicy",
    "AutoscalingGroupMixedInstancesPolicyInstancesDistribution",
    "AutoscalingGroupMixedInstancesPolicyInstancesDistributionOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplate",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverride",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirements",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCount",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorCountOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMib",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsAcceleratorTotalMemoryMibOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbps",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsBaselineEbsBandwidthMbpsOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpu",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryGibPerVcpuOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMib",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsMemoryMibOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCount",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsNetworkInterfaceCountOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGb",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsTotalLocalStorageGbOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCount",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideInstanceRequirementsVcpuCountOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecification",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideLaunchTemplateSpecificationOutputReference",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideList",
    "AutoscalingGroupMixedInstancesPolicyLaunchTemplateOverrideOutputReference",
    "AutoscalingGroupMixedInstancesPolicyOutputReference",
    "AutoscalingGroupTag",
    "AutoscalingGroupTagList",
    "AutoscalingGroupTagOutputReference",
    "AutoscalingGroupTimeouts",
    "AutoscalingGroupTimeoutsOutputReference",
    "AutoscalingGroupWarmPool",
    "AutoscalingGroupWarmPoolInstanceReusePolicy",
    "AutoscalingGroupWarmPoolInstanceReusePolicyOutputReference",
    "AutoscalingGroupWarmPoolOutputReference",
]

publication.publish()
