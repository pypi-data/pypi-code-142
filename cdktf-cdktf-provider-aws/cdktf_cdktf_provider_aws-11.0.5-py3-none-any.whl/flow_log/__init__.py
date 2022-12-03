'''
# `aws_flow_log`

Refer to the Terraform Registory for docs: [`aws_flow_log`](https://www.terraform.io/docs/providers/aws/r/flow_log).
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


class FlowLog(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.flowLog.FlowLog",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/flow_log aws_flow_log}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        destination_options: typing.Optional[typing.Union["FlowLogDestinationOptions", typing.Dict[str, typing.Any]]] = None,
        eni_id: typing.Optional[builtins.str] = None,
        iam_role_arn: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        log_destination: typing.Optional[builtins.str] = None,
        log_destination_type: typing.Optional[builtins.str] = None,
        log_format: typing.Optional[builtins.str] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        max_aggregation_interval: typing.Optional[jsii.Number] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        traffic_type: typing.Optional[builtins.str] = None,
        transit_gateway_attachment_id: typing.Optional[builtins.str] = None,
        transit_gateway_id: typing.Optional[builtins.str] = None,
        vpc_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/flow_log aws_flow_log} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param destination_options: destination_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#destination_options FlowLog#destination_options}
        :param eni_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#eni_id FlowLog#eni_id}.
        :param iam_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#iam_role_arn FlowLog#iam_role_arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#id FlowLog#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#log_destination FlowLog#log_destination}.
        :param log_destination_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#log_destination_type FlowLog#log_destination_type}.
        :param log_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#log_format FlowLog#log_format}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#log_group_name FlowLog#log_group_name}.
        :param max_aggregation_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#max_aggregation_interval FlowLog#max_aggregation_interval}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#subnet_id FlowLog#subnet_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#tags FlowLog#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#tags_all FlowLog#tags_all}.
        :param traffic_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#traffic_type FlowLog#traffic_type}.
        :param transit_gateway_attachment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#transit_gateway_attachment_id FlowLog#transit_gateway_attachment_id}.
        :param transit_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#transit_gateway_id FlowLog#transit_gateway_id}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#vpc_id FlowLog#vpc_id}.
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
                destination_options: typing.Optional[typing.Union[FlowLogDestinationOptions, typing.Dict[str, typing.Any]]] = None,
                eni_id: typing.Optional[builtins.str] = None,
                iam_role_arn: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                log_destination: typing.Optional[builtins.str] = None,
                log_destination_type: typing.Optional[builtins.str] = None,
                log_format: typing.Optional[builtins.str] = None,
                log_group_name: typing.Optional[builtins.str] = None,
                max_aggregation_interval: typing.Optional[jsii.Number] = None,
                subnet_id: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                traffic_type: typing.Optional[builtins.str] = None,
                transit_gateway_attachment_id: typing.Optional[builtins.str] = None,
                transit_gateway_id: typing.Optional[builtins.str] = None,
                vpc_id: typing.Optional[builtins.str] = None,
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
        config = FlowLogConfig(
            destination_options=destination_options,
            eni_id=eni_id,
            iam_role_arn=iam_role_arn,
            id=id,
            log_destination=log_destination,
            log_destination_type=log_destination_type,
            log_format=log_format,
            log_group_name=log_group_name,
            max_aggregation_interval=max_aggregation_interval,
            subnet_id=subnet_id,
            tags=tags,
            tags_all=tags_all,
            traffic_type=traffic_type,
            transit_gateway_attachment_id=transit_gateway_attachment_id,
            transit_gateway_id=transit_gateway_id,
            vpc_id=vpc_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDestinationOptions")
    def put_destination_options(
        self,
        *,
        file_format: typing.Optional[builtins.str] = None,
        hive_compatible_partitions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        per_hour_partition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param file_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#file_format FlowLog#file_format}.
        :param hive_compatible_partitions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#hive_compatible_partitions FlowLog#hive_compatible_partitions}.
        :param per_hour_partition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#per_hour_partition FlowLog#per_hour_partition}.
        '''
        value = FlowLogDestinationOptions(
            file_format=file_format,
            hive_compatible_partitions=hive_compatible_partitions,
            per_hour_partition=per_hour_partition,
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationOptions", [value]))

    @jsii.member(jsii_name="resetDestinationOptions")
    def reset_destination_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationOptions", []))

    @jsii.member(jsii_name="resetEniId")
    def reset_eni_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEniId", []))

    @jsii.member(jsii_name="resetIamRoleArn")
    def reset_iam_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamRoleArn", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogDestination")
    def reset_log_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogDestination", []))

    @jsii.member(jsii_name="resetLogDestinationType")
    def reset_log_destination_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogDestinationType", []))

    @jsii.member(jsii_name="resetLogFormat")
    def reset_log_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogFormat", []))

    @jsii.member(jsii_name="resetLogGroupName")
    def reset_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupName", []))

    @jsii.member(jsii_name="resetMaxAggregationInterval")
    def reset_max_aggregation_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAggregationInterval", []))

    @jsii.member(jsii_name="resetSubnetId")
    def reset_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTrafficType")
    def reset_traffic_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrafficType", []))

    @jsii.member(jsii_name="resetTransitGatewayAttachmentId")
    def reset_transit_gateway_attachment_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransitGatewayAttachmentId", []))

    @jsii.member(jsii_name="resetTransitGatewayId")
    def reset_transit_gateway_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransitGatewayId", []))

    @jsii.member(jsii_name="resetVpcId")
    def reset_vpc_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcId", []))

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
    @jsii.member(jsii_name="destinationOptions")
    def destination_options(self) -> "FlowLogDestinationOptionsOutputReference":
        return typing.cast("FlowLogDestinationOptionsOutputReference", jsii.get(self, "destinationOptions"))

    @builtins.property
    @jsii.member(jsii_name="destinationOptionsInput")
    def destination_options_input(self) -> typing.Optional["FlowLogDestinationOptions"]:
        return typing.cast(typing.Optional["FlowLogDestinationOptions"], jsii.get(self, "destinationOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="eniIdInput")
    def eni_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eniIdInput"))

    @builtins.property
    @jsii.member(jsii_name="iamRoleArnInput")
    def iam_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logDestinationInput")
    def log_destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logDestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="logDestinationTypeInput")
    def log_destination_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logDestinationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="logFormatInput")
    def log_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAggregationIntervalInput")
    def max_aggregation_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAggregationIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

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
    @jsii.member(jsii_name="trafficTypeInput")
    def traffic_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trafficTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="transitGatewayAttachmentIdInput")
    def transit_gateway_attachment_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transitGatewayAttachmentIdInput"))

    @builtins.property
    @jsii.member(jsii_name="transitGatewayIdInput")
    def transit_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transitGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcIdInput")
    def vpc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcIdInput"))

    @builtins.property
    @jsii.member(jsii_name="eniId")
    def eni_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eniId"))

    @eni_id.setter
    def eni_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eniId", value)

    @builtins.property
    @jsii.member(jsii_name="iamRoleArn")
    def iam_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamRoleArn"))

    @iam_role_arn.setter
    def iam_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoleArn", value)

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
    @jsii.member(jsii_name="logDestination")
    def log_destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logDestination"))

    @log_destination.setter
    def log_destination(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logDestination", value)

    @builtins.property
    @jsii.member(jsii_name="logDestinationType")
    def log_destination_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logDestinationType"))

    @log_destination_type.setter
    def log_destination_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logDestinationType", value)

    @builtins.property
    @jsii.member(jsii_name="logFormat")
    def log_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logFormat"))

    @log_format.setter
    def log_format(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logFormat", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="maxAggregationInterval")
    def max_aggregation_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAggregationInterval"))

    @max_aggregation_interval.setter
    def max_aggregation_interval(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAggregationInterval", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

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
    @jsii.member(jsii_name="trafficType")
    def traffic_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trafficType"))

    @traffic_type.setter
    def traffic_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trafficType", value)

    @builtins.property
    @jsii.member(jsii_name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transitGatewayAttachmentId"))

    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitGatewayAttachmentId", value)

    @builtins.property
    @jsii.member(jsii_name="transitGatewayId")
    def transit_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transitGatewayId"))

    @transit_gateway_id.setter
    def transit_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitGatewayId", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.flowLog.FlowLogConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "destination_options": "destinationOptions",
        "eni_id": "eniId",
        "iam_role_arn": "iamRoleArn",
        "id": "id",
        "log_destination": "logDestination",
        "log_destination_type": "logDestinationType",
        "log_format": "logFormat",
        "log_group_name": "logGroupName",
        "max_aggregation_interval": "maxAggregationInterval",
        "subnet_id": "subnetId",
        "tags": "tags",
        "tags_all": "tagsAll",
        "traffic_type": "trafficType",
        "transit_gateway_attachment_id": "transitGatewayAttachmentId",
        "transit_gateway_id": "transitGatewayId",
        "vpc_id": "vpcId",
    },
)
class FlowLogConfig(cdktf.TerraformMetaArguments):
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
        destination_options: typing.Optional[typing.Union["FlowLogDestinationOptions", typing.Dict[str, typing.Any]]] = None,
        eni_id: typing.Optional[builtins.str] = None,
        iam_role_arn: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        log_destination: typing.Optional[builtins.str] = None,
        log_destination_type: typing.Optional[builtins.str] = None,
        log_format: typing.Optional[builtins.str] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        max_aggregation_interval: typing.Optional[jsii.Number] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        traffic_type: typing.Optional[builtins.str] = None,
        transit_gateway_attachment_id: typing.Optional[builtins.str] = None,
        transit_gateway_id: typing.Optional[builtins.str] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param destination_options: destination_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#destination_options FlowLog#destination_options}
        :param eni_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#eni_id FlowLog#eni_id}.
        :param iam_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#iam_role_arn FlowLog#iam_role_arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#id FlowLog#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#log_destination FlowLog#log_destination}.
        :param log_destination_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#log_destination_type FlowLog#log_destination_type}.
        :param log_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#log_format FlowLog#log_format}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#log_group_name FlowLog#log_group_name}.
        :param max_aggregation_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#max_aggregation_interval FlowLog#max_aggregation_interval}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#subnet_id FlowLog#subnet_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#tags FlowLog#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#tags_all FlowLog#tags_all}.
        :param traffic_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#traffic_type FlowLog#traffic_type}.
        :param transit_gateway_attachment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#transit_gateway_attachment_id FlowLog#transit_gateway_attachment_id}.
        :param transit_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#transit_gateway_id FlowLog#transit_gateway_id}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#vpc_id FlowLog#vpc_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(destination_options, dict):
            destination_options = FlowLogDestinationOptions(**destination_options)
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
                destination_options: typing.Optional[typing.Union[FlowLogDestinationOptions, typing.Dict[str, typing.Any]]] = None,
                eni_id: typing.Optional[builtins.str] = None,
                iam_role_arn: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                log_destination: typing.Optional[builtins.str] = None,
                log_destination_type: typing.Optional[builtins.str] = None,
                log_format: typing.Optional[builtins.str] = None,
                log_group_name: typing.Optional[builtins.str] = None,
                max_aggregation_interval: typing.Optional[jsii.Number] = None,
                subnet_id: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                traffic_type: typing.Optional[builtins.str] = None,
                transit_gateway_attachment_id: typing.Optional[builtins.str] = None,
                transit_gateway_id: typing.Optional[builtins.str] = None,
                vpc_id: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument destination_options", value=destination_options, expected_type=type_hints["destination_options"])
            check_type(argname="argument eni_id", value=eni_id, expected_type=type_hints["eni_id"])
            check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log_destination", value=log_destination, expected_type=type_hints["log_destination"])
            check_type(argname="argument log_destination_type", value=log_destination_type, expected_type=type_hints["log_destination_type"])
            check_type(argname="argument log_format", value=log_format, expected_type=type_hints["log_format"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument max_aggregation_interval", value=max_aggregation_interval, expected_type=type_hints["max_aggregation_interval"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument traffic_type", value=traffic_type, expected_type=type_hints["traffic_type"])
            check_type(argname="argument transit_gateway_attachment_id", value=transit_gateway_attachment_id, expected_type=type_hints["transit_gateway_attachment_id"])
            check_type(argname="argument transit_gateway_id", value=transit_gateway_id, expected_type=type_hints["transit_gateway_id"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
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
        if destination_options is not None:
            self._values["destination_options"] = destination_options
        if eni_id is not None:
            self._values["eni_id"] = eni_id
        if iam_role_arn is not None:
            self._values["iam_role_arn"] = iam_role_arn
        if id is not None:
            self._values["id"] = id
        if log_destination is not None:
            self._values["log_destination"] = log_destination
        if log_destination_type is not None:
            self._values["log_destination_type"] = log_destination_type
        if log_format is not None:
            self._values["log_format"] = log_format
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if max_aggregation_interval is not None:
            self._values["max_aggregation_interval"] = max_aggregation_interval
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if traffic_type is not None:
            self._values["traffic_type"] = traffic_type
        if transit_gateway_attachment_id is not None:
            self._values["transit_gateway_attachment_id"] = transit_gateway_attachment_id
        if transit_gateway_id is not None:
            self._values["transit_gateway_id"] = transit_gateway_id
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id

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
    def destination_options(self) -> typing.Optional["FlowLogDestinationOptions"]:
        '''destination_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#destination_options FlowLog#destination_options}
        '''
        result = self._values.get("destination_options")
        return typing.cast(typing.Optional["FlowLogDestinationOptions"], result)

    @builtins.property
    def eni_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#eni_id FlowLog#eni_id}.'''
        result = self._values.get("eni_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#iam_role_arn FlowLog#iam_role_arn}.'''
        result = self._values.get("iam_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#id FlowLog#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_destination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#log_destination FlowLog#log_destination}.'''
        result = self._values.get("log_destination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_destination_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#log_destination_type FlowLog#log_destination_type}.'''
        result = self._values.get("log_destination_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#log_format FlowLog#log_format}.'''
        result = self._values.get("log_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#log_group_name FlowLog#log_group_name}.'''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_aggregation_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#max_aggregation_interval FlowLog#max_aggregation_interval}.'''
        result = self._values.get("max_aggregation_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#subnet_id FlowLog#subnet_id}.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#tags FlowLog#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#tags_all FlowLog#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def traffic_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#traffic_type FlowLog#traffic_type}.'''
        result = self._values.get("traffic_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transit_gateway_attachment_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#transit_gateway_attachment_id FlowLog#transit_gateway_attachment_id}.'''
        result = self._values.get("transit_gateway_attachment_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transit_gateway_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#transit_gateway_id FlowLog#transit_gateway_id}.'''
        result = self._values.get("transit_gateway_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#vpc_id FlowLog#vpc_id}.'''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FlowLogConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.flowLog.FlowLogDestinationOptions",
    jsii_struct_bases=[],
    name_mapping={
        "file_format": "fileFormat",
        "hive_compatible_partitions": "hiveCompatiblePartitions",
        "per_hour_partition": "perHourPartition",
    },
)
class FlowLogDestinationOptions:
    def __init__(
        self,
        *,
        file_format: typing.Optional[builtins.str] = None,
        hive_compatible_partitions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        per_hour_partition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param file_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#file_format FlowLog#file_format}.
        :param hive_compatible_partitions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#hive_compatible_partitions FlowLog#hive_compatible_partitions}.
        :param per_hour_partition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#per_hour_partition FlowLog#per_hour_partition}.
        '''
        if __debug__:
            def stub(
                *,
                file_format: typing.Optional[builtins.str] = None,
                hive_compatible_partitions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                per_hour_partition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument file_format", value=file_format, expected_type=type_hints["file_format"])
            check_type(argname="argument hive_compatible_partitions", value=hive_compatible_partitions, expected_type=type_hints["hive_compatible_partitions"])
            check_type(argname="argument per_hour_partition", value=per_hour_partition, expected_type=type_hints["per_hour_partition"])
        self._values: typing.Dict[str, typing.Any] = {}
        if file_format is not None:
            self._values["file_format"] = file_format
        if hive_compatible_partitions is not None:
            self._values["hive_compatible_partitions"] = hive_compatible_partitions
        if per_hour_partition is not None:
            self._values["per_hour_partition"] = per_hour_partition

    @builtins.property
    def file_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#file_format FlowLog#file_format}.'''
        result = self._values.get("file_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hive_compatible_partitions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#hive_compatible_partitions FlowLog#hive_compatible_partitions}.'''
        result = self._values.get("hive_compatible_partitions")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def per_hour_partition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/flow_log#per_hour_partition FlowLog#per_hour_partition}.'''
        result = self._values.get("per_hour_partition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FlowLogDestinationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FlowLogDestinationOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.flowLog.FlowLogDestinationOptionsOutputReference",
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

    @jsii.member(jsii_name="resetFileFormat")
    def reset_file_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileFormat", []))

    @jsii.member(jsii_name="resetHiveCompatiblePartitions")
    def reset_hive_compatible_partitions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHiveCompatiblePartitions", []))

    @jsii.member(jsii_name="resetPerHourPartition")
    def reset_per_hour_partition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerHourPartition", []))

    @builtins.property
    @jsii.member(jsii_name="fileFormatInput")
    def file_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="hiveCompatiblePartitionsInput")
    def hive_compatible_partitions_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "hiveCompatiblePartitionsInput"))

    @builtins.property
    @jsii.member(jsii_name="perHourPartitionInput")
    def per_hour_partition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "perHourPartitionInput"))

    @builtins.property
    @jsii.member(jsii_name="fileFormat")
    def file_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileFormat"))

    @file_format.setter
    def file_format(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileFormat", value)

    @builtins.property
    @jsii.member(jsii_name="hiveCompatiblePartitions")
    def hive_compatible_partitions(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hiveCompatiblePartitions"))

    @hive_compatible_partitions.setter
    def hive_compatible_partitions(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hiveCompatiblePartitions", value)

    @builtins.property
    @jsii.member(jsii_name="perHourPartition")
    def per_hour_partition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "perHourPartition"))

    @per_hour_partition.setter
    def per_hour_partition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "perHourPartition", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[FlowLogDestinationOptions]:
        return typing.cast(typing.Optional[FlowLogDestinationOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[FlowLogDestinationOptions]) -> None:
        if __debug__:
            def stub(value: typing.Optional[FlowLogDestinationOptions]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "FlowLog",
    "FlowLogConfig",
    "FlowLogDestinationOptions",
    "FlowLogDestinationOptionsOutputReference",
]

publication.publish()
