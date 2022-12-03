'''
# `aws_appautoscaling_policy`

Refer to the Terraform Registory for docs: [`aws_appautoscaling_policy`](https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy).
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


class AppautoscalingPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appautoscalingPolicy.AppautoscalingPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy aws_appautoscaling_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        resource_id: builtins.str,
        scalable_dimension: builtins.str,
        service_namespace: builtins.str,
        id: typing.Optional[builtins.str] = None,
        policy_type: typing.Optional[builtins.str] = None,
        step_scaling_policy_configuration: typing.Optional[typing.Union["AppautoscalingPolicyStepScalingPolicyConfiguration", typing.Dict[str, typing.Any]]] = None,
        target_tracking_scaling_policy_configuration: typing.Optional[typing.Union["AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy aws_appautoscaling_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#name AppautoscalingPolicy#name}.
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#resource_id AppautoscalingPolicy#resource_id}.
        :param scalable_dimension: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scalable_dimension AppautoscalingPolicy#scalable_dimension}.
        :param service_namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#service_namespace AppautoscalingPolicy#service_namespace}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#id AppautoscalingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param policy_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#policy_type AppautoscalingPolicy#policy_type}.
        :param step_scaling_policy_configuration: step_scaling_policy_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#step_scaling_policy_configuration AppautoscalingPolicy#step_scaling_policy_configuration}
        :param target_tracking_scaling_policy_configuration: target_tracking_scaling_policy_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#target_tracking_scaling_policy_configuration AppautoscalingPolicy#target_tracking_scaling_policy_configuration}
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
                resource_id: builtins.str,
                scalable_dimension: builtins.str,
                service_namespace: builtins.str,
                id: typing.Optional[builtins.str] = None,
                policy_type: typing.Optional[builtins.str] = None,
                step_scaling_policy_configuration: typing.Optional[typing.Union[AppautoscalingPolicyStepScalingPolicyConfiguration, typing.Dict[str, typing.Any]]] = None,
                target_tracking_scaling_policy_configuration: typing.Optional[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration, typing.Dict[str, typing.Any]]] = None,
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
        config = AppautoscalingPolicyConfig(
            name=name,
            resource_id=resource_id,
            scalable_dimension=scalable_dimension,
            service_namespace=service_namespace,
            id=id,
            policy_type=policy_type,
            step_scaling_policy_configuration=step_scaling_policy_configuration,
            target_tracking_scaling_policy_configuration=target_tracking_scaling_policy_configuration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putStepScalingPolicyConfiguration")
    def put_step_scaling_policy_configuration(
        self,
        *,
        adjustment_type: typing.Optional[builtins.str] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        metric_aggregation_type: typing.Optional[builtins.str] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
        step_adjustment: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param adjustment_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#adjustment_type AppautoscalingPolicy#adjustment_type}.
        :param cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#cooldown AppautoscalingPolicy#cooldown}.
        :param metric_aggregation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_aggregation_type AppautoscalingPolicy#metric_aggregation_type}.
        :param min_adjustment_magnitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#min_adjustment_magnitude AppautoscalingPolicy#min_adjustment_magnitude}.
        :param step_adjustment: step_adjustment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#step_adjustment AppautoscalingPolicy#step_adjustment}
        '''
        value = AppautoscalingPolicyStepScalingPolicyConfiguration(
            adjustment_type=adjustment_type,
            cooldown=cooldown,
            metric_aggregation_type=metric_aggregation_type,
            min_adjustment_magnitude=min_adjustment_magnitude,
            step_adjustment=step_adjustment,
        )

        return typing.cast(None, jsii.invoke(self, "putStepScalingPolicyConfiguration", [value]))

    @jsii.member(jsii_name="putTargetTrackingScalingPolicyConfiguration")
    def put_target_tracking_scaling_policy_configuration(
        self,
        *,
        target_value: jsii.Number,
        customized_metric_specification: typing.Optional[typing.Union["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification", typing.Dict[str, typing.Any]]] = None,
        disable_scale_in: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        predefined_metric_specification: typing.Optional[typing.Union["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification", typing.Dict[str, typing.Any]]] = None,
        scale_in_cooldown: typing.Optional[jsii.Number] = None,
        scale_out_cooldown: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param target_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#target_value AppautoscalingPolicy#target_value}.
        :param customized_metric_specification: customized_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#customized_metric_specification AppautoscalingPolicy#customized_metric_specification}
        :param disable_scale_in: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#disable_scale_in AppautoscalingPolicy#disable_scale_in}.
        :param predefined_metric_specification: predefined_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#predefined_metric_specification AppautoscalingPolicy#predefined_metric_specification}
        :param scale_in_cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scale_in_cooldown AppautoscalingPolicy#scale_in_cooldown}.
        :param scale_out_cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scale_out_cooldown AppautoscalingPolicy#scale_out_cooldown}.
        '''
        value = AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration(
            target_value=target_value,
            customized_metric_specification=customized_metric_specification,
            disable_scale_in=disable_scale_in,
            predefined_metric_specification=predefined_metric_specification,
            scale_in_cooldown=scale_in_cooldown,
            scale_out_cooldown=scale_out_cooldown,
        )

        return typing.cast(None, jsii.invoke(self, "putTargetTrackingScalingPolicyConfiguration", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPolicyType")
    def reset_policy_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyType", []))

    @jsii.member(jsii_name="resetStepScalingPolicyConfiguration")
    def reset_step_scaling_policy_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStepScalingPolicyConfiguration", []))

    @jsii.member(jsii_name="resetTargetTrackingScalingPolicyConfiguration")
    def reset_target_tracking_scaling_policy_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetTrackingScalingPolicyConfiguration", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="alarmArns")
    def alarm_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "alarmArns"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="stepScalingPolicyConfiguration")
    def step_scaling_policy_configuration(
        self,
    ) -> "AppautoscalingPolicyStepScalingPolicyConfigurationOutputReference":
        return typing.cast("AppautoscalingPolicyStepScalingPolicyConfigurationOutputReference", jsii.get(self, "stepScalingPolicyConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="targetTrackingScalingPolicyConfiguration")
    def target_tracking_scaling_policy_configuration(
        self,
    ) -> "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationOutputReference":
        return typing.cast("AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationOutputReference", jsii.get(self, "targetTrackingScalingPolicyConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="policyTypeInput")
    def policy_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceIdInput")
    def resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="scalableDimensionInput")
    def scalable_dimension_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scalableDimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNamespaceInput")
    def service_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="stepScalingPolicyConfigurationInput")
    def step_scaling_policy_configuration_input(
        self,
    ) -> typing.Optional["AppautoscalingPolicyStepScalingPolicyConfiguration"]:
        return typing.cast(typing.Optional["AppautoscalingPolicyStepScalingPolicyConfiguration"], jsii.get(self, "stepScalingPolicyConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="targetTrackingScalingPolicyConfigurationInput")
    def target_tracking_scaling_policy_configuration_input(
        self,
    ) -> typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration"]:
        return typing.cast(typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration"], jsii.get(self, "targetTrackingScalingPolicyConfigurationInput"))

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
    @jsii.member(jsii_name="policyType")
    def policy_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyType"))

    @policy_type.setter
    def policy_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)

    @builtins.property
    @jsii.member(jsii_name="scalableDimension")
    def scalable_dimension(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scalableDimension"))

    @scalable_dimension.setter
    def scalable_dimension(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalableDimension", value)

    @builtins.property
    @jsii.member(jsii_name="serviceNamespace")
    def service_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceNamespace"))

    @service_namespace.setter
    def service_namespace(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceNamespace", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appautoscalingPolicy.AppautoscalingPolicyConfig",
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
        "resource_id": "resourceId",
        "scalable_dimension": "scalableDimension",
        "service_namespace": "serviceNamespace",
        "id": "id",
        "policy_type": "policyType",
        "step_scaling_policy_configuration": "stepScalingPolicyConfiguration",
        "target_tracking_scaling_policy_configuration": "targetTrackingScalingPolicyConfiguration",
    },
)
class AppautoscalingPolicyConfig(cdktf.TerraformMetaArguments):
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
        resource_id: builtins.str,
        scalable_dimension: builtins.str,
        service_namespace: builtins.str,
        id: typing.Optional[builtins.str] = None,
        policy_type: typing.Optional[builtins.str] = None,
        step_scaling_policy_configuration: typing.Optional[typing.Union["AppautoscalingPolicyStepScalingPolicyConfiguration", typing.Dict[str, typing.Any]]] = None,
        target_tracking_scaling_policy_configuration: typing.Optional[typing.Union["AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#name AppautoscalingPolicy#name}.
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#resource_id AppautoscalingPolicy#resource_id}.
        :param scalable_dimension: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scalable_dimension AppautoscalingPolicy#scalable_dimension}.
        :param service_namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#service_namespace AppautoscalingPolicy#service_namespace}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#id AppautoscalingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param policy_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#policy_type AppautoscalingPolicy#policy_type}.
        :param step_scaling_policy_configuration: step_scaling_policy_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#step_scaling_policy_configuration AppautoscalingPolicy#step_scaling_policy_configuration}
        :param target_tracking_scaling_policy_configuration: target_tracking_scaling_policy_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#target_tracking_scaling_policy_configuration AppautoscalingPolicy#target_tracking_scaling_policy_configuration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(step_scaling_policy_configuration, dict):
            step_scaling_policy_configuration = AppautoscalingPolicyStepScalingPolicyConfiguration(**step_scaling_policy_configuration)
        if isinstance(target_tracking_scaling_policy_configuration, dict):
            target_tracking_scaling_policy_configuration = AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration(**target_tracking_scaling_policy_configuration)
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
                resource_id: builtins.str,
                scalable_dimension: builtins.str,
                service_namespace: builtins.str,
                id: typing.Optional[builtins.str] = None,
                policy_type: typing.Optional[builtins.str] = None,
                step_scaling_policy_configuration: typing.Optional[typing.Union[AppautoscalingPolicyStepScalingPolicyConfiguration, typing.Dict[str, typing.Any]]] = None,
                target_tracking_scaling_policy_configuration: typing.Optional[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument scalable_dimension", value=scalable_dimension, expected_type=type_hints["scalable_dimension"])
            check_type(argname="argument service_namespace", value=service_namespace, expected_type=type_hints["service_namespace"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument policy_type", value=policy_type, expected_type=type_hints["policy_type"])
            check_type(argname="argument step_scaling_policy_configuration", value=step_scaling_policy_configuration, expected_type=type_hints["step_scaling_policy_configuration"])
            check_type(argname="argument target_tracking_scaling_policy_configuration", value=target_tracking_scaling_policy_configuration, expected_type=type_hints["target_tracking_scaling_policy_configuration"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "resource_id": resource_id,
            "scalable_dimension": scalable_dimension,
            "service_namespace": service_namespace,
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
        if policy_type is not None:
            self._values["policy_type"] = policy_type
        if step_scaling_policy_configuration is not None:
            self._values["step_scaling_policy_configuration"] = step_scaling_policy_configuration
        if target_tracking_scaling_policy_configuration is not None:
            self._values["target_tracking_scaling_policy_configuration"] = target_tracking_scaling_policy_configuration

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#name AppautoscalingPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#resource_id AppautoscalingPolicy#resource_id}.'''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scalable_dimension(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scalable_dimension AppautoscalingPolicy#scalable_dimension}.'''
        result = self._values.get("scalable_dimension")
        assert result is not None, "Required property 'scalable_dimension' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#service_namespace AppautoscalingPolicy#service_namespace}.'''
        result = self._values.get("service_namespace")
        assert result is not None, "Required property 'service_namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#id AppautoscalingPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#policy_type AppautoscalingPolicy#policy_type}.'''
        result = self._values.get("policy_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def step_scaling_policy_configuration(
        self,
    ) -> typing.Optional["AppautoscalingPolicyStepScalingPolicyConfiguration"]:
        '''step_scaling_policy_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#step_scaling_policy_configuration AppautoscalingPolicy#step_scaling_policy_configuration}
        '''
        result = self._values.get("step_scaling_policy_configuration")
        return typing.cast(typing.Optional["AppautoscalingPolicyStepScalingPolicyConfiguration"], result)

    @builtins.property
    def target_tracking_scaling_policy_configuration(
        self,
    ) -> typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration"]:
        '''target_tracking_scaling_policy_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#target_tracking_scaling_policy_configuration AppautoscalingPolicy#target_tracking_scaling_policy_configuration}
        '''
        result = self._values.get("target_tracking_scaling_policy_configuration")
        return typing.cast(typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppautoscalingPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appautoscalingPolicy.AppautoscalingPolicyStepScalingPolicyConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "adjustment_type": "adjustmentType",
        "cooldown": "cooldown",
        "metric_aggregation_type": "metricAggregationType",
        "min_adjustment_magnitude": "minAdjustmentMagnitude",
        "step_adjustment": "stepAdjustment",
    },
)
class AppautoscalingPolicyStepScalingPolicyConfiguration:
    def __init__(
        self,
        *,
        adjustment_type: typing.Optional[builtins.str] = None,
        cooldown: typing.Optional[jsii.Number] = None,
        metric_aggregation_type: typing.Optional[builtins.str] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
        step_adjustment: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param adjustment_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#adjustment_type AppautoscalingPolicy#adjustment_type}.
        :param cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#cooldown AppautoscalingPolicy#cooldown}.
        :param metric_aggregation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_aggregation_type AppautoscalingPolicy#metric_aggregation_type}.
        :param min_adjustment_magnitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#min_adjustment_magnitude AppautoscalingPolicy#min_adjustment_magnitude}.
        :param step_adjustment: step_adjustment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#step_adjustment AppautoscalingPolicy#step_adjustment}
        '''
        if __debug__:
            def stub(
                *,
                adjustment_type: typing.Optional[builtins.str] = None,
                cooldown: typing.Optional[jsii.Number] = None,
                metric_aggregation_type: typing.Optional[builtins.str] = None,
                min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
                step_adjustment: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument adjustment_type", value=adjustment_type, expected_type=type_hints["adjustment_type"])
            check_type(argname="argument cooldown", value=cooldown, expected_type=type_hints["cooldown"])
            check_type(argname="argument metric_aggregation_type", value=metric_aggregation_type, expected_type=type_hints["metric_aggregation_type"])
            check_type(argname="argument min_adjustment_magnitude", value=min_adjustment_magnitude, expected_type=type_hints["min_adjustment_magnitude"])
            check_type(argname="argument step_adjustment", value=step_adjustment, expected_type=type_hints["step_adjustment"])
        self._values: typing.Dict[str, typing.Any] = {}
        if adjustment_type is not None:
            self._values["adjustment_type"] = adjustment_type
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if metric_aggregation_type is not None:
            self._values["metric_aggregation_type"] = metric_aggregation_type
        if min_adjustment_magnitude is not None:
            self._values["min_adjustment_magnitude"] = min_adjustment_magnitude
        if step_adjustment is not None:
            self._values["step_adjustment"] = step_adjustment

    @builtins.property
    def adjustment_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#adjustment_type AppautoscalingPolicy#adjustment_type}.'''
        result = self._values.get("adjustment_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#cooldown AppautoscalingPolicy#cooldown}.'''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metric_aggregation_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_aggregation_type AppautoscalingPolicy#metric_aggregation_type}.'''
        result = self._values.get("metric_aggregation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_adjustment_magnitude(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#min_adjustment_magnitude AppautoscalingPolicy#min_adjustment_magnitude}.'''
        result = self._values.get("min_adjustment_magnitude")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def step_adjustment(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment"]]]:
        '''step_adjustment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#step_adjustment AppautoscalingPolicy#step_adjustment}
        '''
        result = self._values.get("step_adjustment")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppautoscalingPolicyStepScalingPolicyConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppautoscalingPolicyStepScalingPolicyConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appautoscalingPolicy.AppautoscalingPolicyStepScalingPolicyConfigurationOutputReference",
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

    @jsii.member(jsii_name="putStepAdjustment")
    def put_step_adjustment(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStepAdjustment", [value]))

    @jsii.member(jsii_name="resetAdjustmentType")
    def reset_adjustment_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdjustmentType", []))

    @jsii.member(jsii_name="resetCooldown")
    def reset_cooldown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCooldown", []))

    @jsii.member(jsii_name="resetMetricAggregationType")
    def reset_metric_aggregation_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricAggregationType", []))

    @jsii.member(jsii_name="resetMinAdjustmentMagnitude")
    def reset_min_adjustment_magnitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinAdjustmentMagnitude", []))

    @jsii.member(jsii_name="resetStepAdjustment")
    def reset_step_adjustment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStepAdjustment", []))

    @builtins.property
    @jsii.member(jsii_name="stepAdjustment")
    def step_adjustment(
        self,
    ) -> "AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentList":
        return typing.cast("AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentList", jsii.get(self, "stepAdjustment"))

    @builtins.property
    @jsii.member(jsii_name="adjustmentTypeInput")
    def adjustment_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adjustmentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="cooldownInput")
    def cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="metricAggregationTypeInput")
    def metric_aggregation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricAggregationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="minAdjustmentMagnitudeInput")
    def min_adjustment_magnitude_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minAdjustmentMagnitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="stepAdjustmentInput")
    def step_adjustment_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment"]]], jsii.get(self, "stepAdjustmentInput"))

    @builtins.property
    @jsii.member(jsii_name="adjustmentType")
    def adjustment_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adjustmentType"))

    @adjustment_type.setter
    def adjustment_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adjustmentType", value)

    @builtins.property
    @jsii.member(jsii_name="cooldown")
    def cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cooldown"))

    @cooldown.setter
    def cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cooldown", value)

    @builtins.property
    @jsii.member(jsii_name="metricAggregationType")
    def metric_aggregation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricAggregationType"))

    @metric_aggregation_type.setter
    def metric_aggregation_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricAggregationType", value)

    @builtins.property
    @jsii.member(jsii_name="minAdjustmentMagnitude")
    def min_adjustment_magnitude(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minAdjustmentMagnitude"))

    @min_adjustment_magnitude.setter
    def min_adjustment_magnitude(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minAdjustmentMagnitude", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppautoscalingPolicyStepScalingPolicyConfiguration]:
        return typing.cast(typing.Optional[AppautoscalingPolicyStepScalingPolicyConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppautoscalingPolicyStepScalingPolicyConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppautoscalingPolicyStepScalingPolicyConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appautoscalingPolicy.AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment",
    jsii_struct_bases=[],
    name_mapping={
        "scaling_adjustment": "scalingAdjustment",
        "metric_interval_lower_bound": "metricIntervalLowerBound",
        "metric_interval_upper_bound": "metricIntervalUpperBound",
    },
)
class AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment:
    def __init__(
        self,
        *,
        scaling_adjustment: jsii.Number,
        metric_interval_lower_bound: typing.Optional[builtins.str] = None,
        metric_interval_upper_bound: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scaling_adjustment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scaling_adjustment AppautoscalingPolicy#scaling_adjustment}.
        :param metric_interval_lower_bound: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_interval_lower_bound AppautoscalingPolicy#metric_interval_lower_bound}.
        :param metric_interval_upper_bound: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_interval_upper_bound AppautoscalingPolicy#metric_interval_upper_bound}.
        '''
        if __debug__:
            def stub(
                *,
                scaling_adjustment: jsii.Number,
                metric_interval_lower_bound: typing.Optional[builtins.str] = None,
                metric_interval_upper_bound: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scaling_adjustment", value=scaling_adjustment, expected_type=type_hints["scaling_adjustment"])
            check_type(argname="argument metric_interval_lower_bound", value=metric_interval_lower_bound, expected_type=type_hints["metric_interval_lower_bound"])
            check_type(argname="argument metric_interval_upper_bound", value=metric_interval_upper_bound, expected_type=type_hints["metric_interval_upper_bound"])
        self._values: typing.Dict[str, typing.Any] = {
            "scaling_adjustment": scaling_adjustment,
        }
        if metric_interval_lower_bound is not None:
            self._values["metric_interval_lower_bound"] = metric_interval_lower_bound
        if metric_interval_upper_bound is not None:
            self._values["metric_interval_upper_bound"] = metric_interval_upper_bound

    @builtins.property
    def scaling_adjustment(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scaling_adjustment AppautoscalingPolicy#scaling_adjustment}.'''
        result = self._values.get("scaling_adjustment")
        assert result is not None, "Required property 'scaling_adjustment' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def metric_interval_lower_bound(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_interval_lower_bound AppautoscalingPolicy#metric_interval_lower_bound}.'''
        result = self._values.get("metric_interval_lower_bound")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_interval_upper_bound(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_interval_upper_bound AppautoscalingPolicy#metric_interval_upper_bound}.'''
        result = self._values.get("metric_interval_upper_bound")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appautoscalingPolicy.AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentList",
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
    ) -> "AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appautoscalingPolicy.AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentOutputReference",
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

    @jsii.member(jsii_name="resetMetricIntervalLowerBound")
    def reset_metric_interval_lower_bound(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricIntervalLowerBound", []))

    @jsii.member(jsii_name="resetMetricIntervalUpperBound")
    def reset_metric_interval_upper_bound(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricIntervalUpperBound", []))

    @builtins.property
    @jsii.member(jsii_name="metricIntervalLowerBoundInput")
    def metric_interval_lower_bound_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricIntervalLowerBoundInput"))

    @builtins.property
    @jsii.member(jsii_name="metricIntervalUpperBoundInput")
    def metric_interval_upper_bound_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricIntervalUpperBoundInput"))

    @builtins.property
    @jsii.member(jsii_name="scalingAdjustmentInput")
    def scaling_adjustment_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scalingAdjustmentInput"))

    @builtins.property
    @jsii.member(jsii_name="metricIntervalLowerBound")
    def metric_interval_lower_bound(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricIntervalLowerBound"))

    @metric_interval_lower_bound.setter
    def metric_interval_lower_bound(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricIntervalLowerBound", value)

    @builtins.property
    @jsii.member(jsii_name="metricIntervalUpperBound")
    def metric_interval_upper_bound(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricIntervalUpperBound"))

    @metric_interval_upper_bound.setter
    def metric_interval_upper_bound(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricIntervalUpperBound", value)

    @builtins.property
    @jsii.member(jsii_name="scalingAdjustment")
    def scaling_adjustment(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scalingAdjustment"))

    @scaling_adjustment.setter
    def scaling_adjustment(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalingAdjustment", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appautoscalingPolicy.AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "target_value": "targetValue",
        "customized_metric_specification": "customizedMetricSpecification",
        "disable_scale_in": "disableScaleIn",
        "predefined_metric_specification": "predefinedMetricSpecification",
        "scale_in_cooldown": "scaleInCooldown",
        "scale_out_cooldown": "scaleOutCooldown",
    },
)
class AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration:
    def __init__(
        self,
        *,
        target_value: jsii.Number,
        customized_metric_specification: typing.Optional[typing.Union["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification", typing.Dict[str, typing.Any]]] = None,
        disable_scale_in: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        predefined_metric_specification: typing.Optional[typing.Union["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification", typing.Dict[str, typing.Any]]] = None,
        scale_in_cooldown: typing.Optional[jsii.Number] = None,
        scale_out_cooldown: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param target_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#target_value AppautoscalingPolicy#target_value}.
        :param customized_metric_specification: customized_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#customized_metric_specification AppautoscalingPolicy#customized_metric_specification}
        :param disable_scale_in: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#disable_scale_in AppautoscalingPolicy#disable_scale_in}.
        :param predefined_metric_specification: predefined_metric_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#predefined_metric_specification AppautoscalingPolicy#predefined_metric_specification}
        :param scale_in_cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scale_in_cooldown AppautoscalingPolicy#scale_in_cooldown}.
        :param scale_out_cooldown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scale_out_cooldown AppautoscalingPolicy#scale_out_cooldown}.
        '''
        if isinstance(customized_metric_specification, dict):
            customized_metric_specification = AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification(**customized_metric_specification)
        if isinstance(predefined_metric_specification, dict):
            predefined_metric_specification = AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification(**predefined_metric_specification)
        if __debug__:
            def stub(
                *,
                target_value: jsii.Number,
                customized_metric_specification: typing.Optional[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification, typing.Dict[str, typing.Any]]] = None,
                disable_scale_in: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                predefined_metric_specification: typing.Optional[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification, typing.Dict[str, typing.Any]]] = None,
                scale_in_cooldown: typing.Optional[jsii.Number] = None,
                scale_out_cooldown: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument target_value", value=target_value, expected_type=type_hints["target_value"])
            check_type(argname="argument customized_metric_specification", value=customized_metric_specification, expected_type=type_hints["customized_metric_specification"])
            check_type(argname="argument disable_scale_in", value=disable_scale_in, expected_type=type_hints["disable_scale_in"])
            check_type(argname="argument predefined_metric_specification", value=predefined_metric_specification, expected_type=type_hints["predefined_metric_specification"])
            check_type(argname="argument scale_in_cooldown", value=scale_in_cooldown, expected_type=type_hints["scale_in_cooldown"])
            check_type(argname="argument scale_out_cooldown", value=scale_out_cooldown, expected_type=type_hints["scale_out_cooldown"])
        self._values: typing.Dict[str, typing.Any] = {
            "target_value": target_value,
        }
        if customized_metric_specification is not None:
            self._values["customized_metric_specification"] = customized_metric_specification
        if disable_scale_in is not None:
            self._values["disable_scale_in"] = disable_scale_in
        if predefined_metric_specification is not None:
            self._values["predefined_metric_specification"] = predefined_metric_specification
        if scale_in_cooldown is not None:
            self._values["scale_in_cooldown"] = scale_in_cooldown
        if scale_out_cooldown is not None:
            self._values["scale_out_cooldown"] = scale_out_cooldown

    @builtins.property
    def target_value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#target_value AppautoscalingPolicy#target_value}.'''
        result = self._values.get("target_value")
        assert result is not None, "Required property 'target_value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def customized_metric_specification(
        self,
    ) -> typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification"]:
        '''customized_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#customized_metric_specification AppautoscalingPolicy#customized_metric_specification}
        '''
        result = self._values.get("customized_metric_specification")
        return typing.cast(typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification"], result)

    @builtins.property
    def disable_scale_in(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#disable_scale_in AppautoscalingPolicy#disable_scale_in}.'''
        result = self._values.get("disable_scale_in")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def predefined_metric_specification(
        self,
    ) -> typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification"]:
        '''predefined_metric_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#predefined_metric_specification AppautoscalingPolicy#predefined_metric_specification}
        '''
        result = self._values.get("predefined_metric_specification")
        return typing.cast(typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification"], result)

    @builtins.property
    def scale_in_cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scale_in_cooldown AppautoscalingPolicy#scale_in_cooldown}.'''
        result = self._values.get("scale_in_cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scale_out_cooldown(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#scale_out_cooldown AppautoscalingPolicy#scale_out_cooldown}.'''
        result = self._values.get("scale_out_cooldown")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appautoscalingPolicy.AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "statistic": "statistic",
        "dimensions": "dimensions",
        "unit": "unit",
    },
)
class AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        statistic: builtins.str,
        dimensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions", typing.Dict[str, typing.Any]]]]] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_name AppautoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#namespace AppautoscalingPolicy#namespace}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#statistic AppautoscalingPolicy#statistic}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#dimensions AppautoscalingPolicy#dimensions}
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#unit AppautoscalingPolicy#unit}.
        '''
        if __debug__:
            def stub(
                *,
                metric_name: builtins.str,
                namespace: builtins.str,
                statistic: builtins.str,
                dimensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions, typing.Dict[str, typing.Any]]]]] = None,
                unit: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
            "statistic": statistic,
        }
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_name AppautoscalingPolicy#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#namespace AppautoscalingPolicy#namespace}.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statistic(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#statistic AppautoscalingPolicy#statistic}.'''
        result = self._values.get("statistic")
        assert result is not None, "Required property 'statistic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions"]]]:
        '''dimensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#dimensions AppautoscalingPolicy#dimensions}
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions"]]], result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#unit AppautoscalingPolicy#unit}.'''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appautoscalingPolicy.AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#name AppautoscalingPolicy#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#value AppautoscalingPolicy#value}.
        '''
        if __debug__:
            def stub(*, name: builtins.str, value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#name AppautoscalingPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#value AppautoscalingPolicy#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appautoscalingPolicy.AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsList",
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
    ) -> "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appautoscalingPolicy.AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsOutputReference",
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
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

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
    ) -> typing.Optional[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appautoscalingPolicy.AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationOutputReference",
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

    @jsii.member(jsii_name="putDimensions")
    def put_dimensions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDimensions", [value]))

    @jsii.member(jsii_name="resetDimensions")
    def reset_dimensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimensions", []))

    @jsii.member(jsii_name="resetUnit")
    def reset_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnit", []))

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(
        self,
    ) -> AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsList:
        return typing.cast(AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsList, jsii.get(self, "dimensions"))

    @builtins.property
    @jsii.member(jsii_name="dimensionsInput")
    def dimensions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions]]], jsii.get(self, "dimensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="statisticInput")
    def statistic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statisticInput"))

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

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
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statistic", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification]:
        return typing.cast(typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appautoscalingPolicy.AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationOutputReference",
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

    @jsii.member(jsii_name="putCustomizedMetricSpecification")
    def put_customized_metric_specification(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        statistic: builtins.str,
        dimensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions, typing.Dict[str, typing.Any]]]]] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#metric_name AppautoscalingPolicy#metric_name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#namespace AppautoscalingPolicy#namespace}.
        :param statistic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#statistic AppautoscalingPolicy#statistic}.
        :param dimensions: dimensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#dimensions AppautoscalingPolicy#dimensions}
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#unit AppautoscalingPolicy#unit}.
        '''
        value = AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification(
            metric_name=metric_name,
            namespace=namespace,
            statistic=statistic,
            dimensions=dimensions,
            unit=unit,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomizedMetricSpecification", [value]))

    @jsii.member(jsii_name="putPredefinedMetricSpecification")
    def put_predefined_metric_specification(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#predefined_metric_type AppautoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#resource_label AppautoscalingPolicy#resource_label}.
        '''
        value = AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification(
            predefined_metric_type=predefined_metric_type,
            resource_label=resource_label,
        )

        return typing.cast(None, jsii.invoke(self, "putPredefinedMetricSpecification", [value]))

    @jsii.member(jsii_name="resetCustomizedMetricSpecification")
    def reset_customized_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomizedMetricSpecification", []))

    @jsii.member(jsii_name="resetDisableScaleIn")
    def reset_disable_scale_in(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableScaleIn", []))

    @jsii.member(jsii_name="resetPredefinedMetricSpecification")
    def reset_predefined_metric_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredefinedMetricSpecification", []))

    @jsii.member(jsii_name="resetScaleInCooldown")
    def reset_scale_in_cooldown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleInCooldown", []))

    @jsii.member(jsii_name="resetScaleOutCooldown")
    def reset_scale_out_cooldown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleOutCooldown", []))

    @builtins.property
    @jsii.member(jsii_name="customizedMetricSpecification")
    def customized_metric_specification(
        self,
    ) -> AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationOutputReference:
        return typing.cast(AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationOutputReference, jsii.get(self, "customizedMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricSpecification")
    def predefined_metric_specification(
        self,
    ) -> "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationOutputReference":
        return typing.cast("AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationOutputReference", jsii.get(self, "predefinedMetricSpecification"))

    @builtins.property
    @jsii.member(jsii_name="customizedMetricSpecificationInput")
    def customized_metric_specification_input(
        self,
    ) -> typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification]:
        return typing.cast(typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification], jsii.get(self, "customizedMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="disableScaleInInput")
    def disable_scale_in_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableScaleInInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricSpecificationInput")
    def predefined_metric_specification_input(
        self,
    ) -> typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification"]:
        return typing.cast(typing.Optional["AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification"], jsii.get(self, "predefinedMetricSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleInCooldownInput")
    def scale_in_cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scaleInCooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleOutCooldownInput")
    def scale_out_cooldown_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scaleOutCooldownInput"))

    @builtins.property
    @jsii.member(jsii_name="targetValueInput")
    def target_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetValueInput"))

    @builtins.property
    @jsii.member(jsii_name="disableScaleIn")
    def disable_scale_in(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableScaleIn"))

    @disable_scale_in.setter
    def disable_scale_in(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableScaleIn", value)

    @builtins.property
    @jsii.member(jsii_name="scaleInCooldown")
    def scale_in_cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scaleInCooldown"))

    @scale_in_cooldown.setter
    def scale_in_cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleInCooldown", value)

    @builtins.property
    @jsii.member(jsii_name="scaleOutCooldown")
    def scale_out_cooldown(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scaleOutCooldown"))

    @scale_out_cooldown.setter
    def scale_out_cooldown(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleOutCooldown", value)

    @builtins.property
    @jsii.member(jsii_name="targetValue")
    def target_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetValue"))

    @target_value.setter
    def target_value(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration]:
        return typing.cast(typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appautoscalingPolicy.AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification",
    jsii_struct_bases=[],
    name_mapping={
        "predefined_metric_type": "predefinedMetricType",
        "resource_label": "resourceLabel",
    },
)
class AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification:
    def __init__(
        self,
        *,
        predefined_metric_type: builtins.str,
        resource_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param predefined_metric_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#predefined_metric_type AppautoscalingPolicy#predefined_metric_type}.
        :param resource_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#resource_label AppautoscalingPolicy#resource_label}.
        '''
        if __debug__:
            def stub(
                *,
                predefined_metric_type: builtins.str,
                resource_label: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument predefined_metric_type", value=predefined_metric_type, expected_type=type_hints["predefined_metric_type"])
            check_type(argname="argument resource_label", value=resource_label, expected_type=type_hints["resource_label"])
        self._values: typing.Dict[str, typing.Any] = {
            "predefined_metric_type": predefined_metric_type,
        }
        if resource_label is not None:
            self._values["resource_label"] = resource_label

    @builtins.property
    def predefined_metric_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#predefined_metric_type AppautoscalingPolicy#predefined_metric_type}.'''
        result = self._values.get("predefined_metric_type")
        assert result is not None, "Required property 'predefined_metric_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy#resource_label AppautoscalingPolicy#resource_label}.'''
        result = self._values.get("resource_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appautoscalingPolicy.AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationOutputReference",
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

    @jsii.member(jsii_name="resetResourceLabel")
    def reset_resource_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceLabel", []))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricTypeInput")
    def predefined_metric_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "predefinedMetricTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceLabelInput")
    def resource_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedMetricType")
    def predefined_metric_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "predefinedMetricType"))

    @predefined_metric_type.setter
    def predefined_metric_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "predefinedMetricType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceLabel")
    def resource_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceLabel"))

    @resource_label.setter
    def resource_label(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceLabel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification]:
        return typing.cast(typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppautoscalingPolicy",
    "AppautoscalingPolicyConfig",
    "AppautoscalingPolicyStepScalingPolicyConfiguration",
    "AppautoscalingPolicyStepScalingPolicyConfigurationOutputReference",
    "AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustment",
    "AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentList",
    "AppautoscalingPolicyStepScalingPolicyConfigurationStepAdjustmentOutputReference",
    "AppautoscalingPolicyTargetTrackingScalingPolicyConfiguration",
    "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecification",
    "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensions",
    "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsList",
    "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionsOutputReference",
    "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationOutputReference",
    "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationOutputReference",
    "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecification",
    "AppautoscalingPolicyTargetTrackingScalingPolicyConfigurationPredefinedMetricSpecificationOutputReference",
]

publication.publish()
