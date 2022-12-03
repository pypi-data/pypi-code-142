'''
# `aws_sns_sms_preferences`

Refer to the Terraform Registory for docs: [`aws_sns_sms_preferences`](https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences).
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


class SnsSmsPreferences(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.snsSmsPreferences.SnsSmsPreferences",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences aws_sns_sms_preferences}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        default_sender_id: typing.Optional[builtins.str] = None,
        default_sms_type: typing.Optional[builtins.str] = None,
        delivery_status_iam_role_arn: typing.Optional[builtins.str] = None,
        delivery_status_success_sampling_rate: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        monthly_spend_limit: typing.Optional[jsii.Number] = None,
        usage_report_s3_bucket: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences aws_sns_sms_preferences} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param default_sender_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#default_sender_id SnsSmsPreferences#default_sender_id}.
        :param default_sms_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#default_sms_type SnsSmsPreferences#default_sms_type}.
        :param delivery_status_iam_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#delivery_status_iam_role_arn SnsSmsPreferences#delivery_status_iam_role_arn}.
        :param delivery_status_success_sampling_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#delivery_status_success_sampling_rate SnsSmsPreferences#delivery_status_success_sampling_rate}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#id SnsSmsPreferences#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param monthly_spend_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#monthly_spend_limit SnsSmsPreferences#monthly_spend_limit}.
        :param usage_report_s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#usage_report_s3_bucket SnsSmsPreferences#usage_report_s3_bucket}.
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
                default_sender_id: typing.Optional[builtins.str] = None,
                default_sms_type: typing.Optional[builtins.str] = None,
                delivery_status_iam_role_arn: typing.Optional[builtins.str] = None,
                delivery_status_success_sampling_rate: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                monthly_spend_limit: typing.Optional[jsii.Number] = None,
                usage_report_s3_bucket: typing.Optional[builtins.str] = None,
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
        config = SnsSmsPreferencesConfig(
            default_sender_id=default_sender_id,
            default_sms_type=default_sms_type,
            delivery_status_iam_role_arn=delivery_status_iam_role_arn,
            delivery_status_success_sampling_rate=delivery_status_success_sampling_rate,
            id=id,
            monthly_spend_limit=monthly_spend_limit,
            usage_report_s3_bucket=usage_report_s3_bucket,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDefaultSenderId")
    def reset_default_sender_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultSenderId", []))

    @jsii.member(jsii_name="resetDefaultSmsType")
    def reset_default_sms_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultSmsType", []))

    @jsii.member(jsii_name="resetDeliveryStatusIamRoleArn")
    def reset_delivery_status_iam_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeliveryStatusIamRoleArn", []))

    @jsii.member(jsii_name="resetDeliveryStatusSuccessSamplingRate")
    def reset_delivery_status_success_sampling_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeliveryStatusSuccessSamplingRate", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMonthlySpendLimit")
    def reset_monthly_spend_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonthlySpendLimit", []))

    @jsii.member(jsii_name="resetUsageReportS3Bucket")
    def reset_usage_report_s3_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsageReportS3Bucket", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="defaultSenderIdInput")
    def default_sender_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSenderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultSmsTypeInput")
    def default_sms_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSmsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryStatusIamRoleArnInput")
    def delivery_status_iam_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryStatusIamRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryStatusSuccessSamplingRateInput")
    def delivery_status_success_sampling_rate_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryStatusSuccessSamplingRateInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="monthlySpendLimitInput")
    def monthly_spend_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "monthlySpendLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="usageReportS3BucketInput")
    def usage_report_s3_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usageReportS3BucketInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultSenderId")
    def default_sender_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultSenderId"))

    @default_sender_id.setter
    def default_sender_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSenderId", value)

    @builtins.property
    @jsii.member(jsii_name="defaultSmsType")
    def default_sms_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultSmsType"))

    @default_sms_type.setter
    def default_sms_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSmsType", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryStatusIamRoleArn")
    def delivery_status_iam_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deliveryStatusIamRoleArn"))

    @delivery_status_iam_role_arn.setter
    def delivery_status_iam_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryStatusIamRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryStatusSuccessSamplingRate")
    def delivery_status_success_sampling_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deliveryStatusSuccessSamplingRate"))

    @delivery_status_success_sampling_rate.setter
    def delivery_status_success_sampling_rate(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryStatusSuccessSamplingRate", value)

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
    @jsii.member(jsii_name="monthlySpendLimit")
    def monthly_spend_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "monthlySpendLimit"))

    @monthly_spend_limit.setter
    def monthly_spend_limit(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monthlySpendLimit", value)

    @builtins.property
    @jsii.member(jsii_name="usageReportS3Bucket")
    def usage_report_s3_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usageReportS3Bucket"))

    @usage_report_s3_bucket.setter
    def usage_report_s3_bucket(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usageReportS3Bucket", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.snsSmsPreferences.SnsSmsPreferencesConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "default_sender_id": "defaultSenderId",
        "default_sms_type": "defaultSmsType",
        "delivery_status_iam_role_arn": "deliveryStatusIamRoleArn",
        "delivery_status_success_sampling_rate": "deliveryStatusSuccessSamplingRate",
        "id": "id",
        "monthly_spend_limit": "monthlySpendLimit",
        "usage_report_s3_bucket": "usageReportS3Bucket",
    },
)
class SnsSmsPreferencesConfig(cdktf.TerraformMetaArguments):
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
        default_sender_id: typing.Optional[builtins.str] = None,
        default_sms_type: typing.Optional[builtins.str] = None,
        delivery_status_iam_role_arn: typing.Optional[builtins.str] = None,
        delivery_status_success_sampling_rate: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        monthly_spend_limit: typing.Optional[jsii.Number] = None,
        usage_report_s3_bucket: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param default_sender_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#default_sender_id SnsSmsPreferences#default_sender_id}.
        :param default_sms_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#default_sms_type SnsSmsPreferences#default_sms_type}.
        :param delivery_status_iam_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#delivery_status_iam_role_arn SnsSmsPreferences#delivery_status_iam_role_arn}.
        :param delivery_status_success_sampling_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#delivery_status_success_sampling_rate SnsSmsPreferences#delivery_status_success_sampling_rate}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#id SnsSmsPreferences#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param monthly_spend_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#monthly_spend_limit SnsSmsPreferences#monthly_spend_limit}.
        :param usage_report_s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#usage_report_s3_bucket SnsSmsPreferences#usage_report_s3_bucket}.
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
                default_sender_id: typing.Optional[builtins.str] = None,
                default_sms_type: typing.Optional[builtins.str] = None,
                delivery_status_iam_role_arn: typing.Optional[builtins.str] = None,
                delivery_status_success_sampling_rate: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                monthly_spend_limit: typing.Optional[jsii.Number] = None,
                usage_report_s3_bucket: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument default_sender_id", value=default_sender_id, expected_type=type_hints["default_sender_id"])
            check_type(argname="argument default_sms_type", value=default_sms_type, expected_type=type_hints["default_sms_type"])
            check_type(argname="argument delivery_status_iam_role_arn", value=delivery_status_iam_role_arn, expected_type=type_hints["delivery_status_iam_role_arn"])
            check_type(argname="argument delivery_status_success_sampling_rate", value=delivery_status_success_sampling_rate, expected_type=type_hints["delivery_status_success_sampling_rate"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument monthly_spend_limit", value=monthly_spend_limit, expected_type=type_hints["monthly_spend_limit"])
            check_type(argname="argument usage_report_s3_bucket", value=usage_report_s3_bucket, expected_type=type_hints["usage_report_s3_bucket"])
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
        if default_sender_id is not None:
            self._values["default_sender_id"] = default_sender_id
        if default_sms_type is not None:
            self._values["default_sms_type"] = default_sms_type
        if delivery_status_iam_role_arn is not None:
            self._values["delivery_status_iam_role_arn"] = delivery_status_iam_role_arn
        if delivery_status_success_sampling_rate is not None:
            self._values["delivery_status_success_sampling_rate"] = delivery_status_success_sampling_rate
        if id is not None:
            self._values["id"] = id
        if monthly_spend_limit is not None:
            self._values["monthly_spend_limit"] = monthly_spend_limit
        if usage_report_s3_bucket is not None:
            self._values["usage_report_s3_bucket"] = usage_report_s3_bucket

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
    def default_sender_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#default_sender_id SnsSmsPreferences#default_sender_id}.'''
        result = self._values.get("default_sender_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_sms_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#default_sms_type SnsSmsPreferences#default_sms_type}.'''
        result = self._values.get("default_sms_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delivery_status_iam_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#delivery_status_iam_role_arn SnsSmsPreferences#delivery_status_iam_role_arn}.'''
        result = self._values.get("delivery_status_iam_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delivery_status_success_sampling_rate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#delivery_status_success_sampling_rate SnsSmsPreferences#delivery_status_success_sampling_rate}.'''
        result = self._values.get("delivery_status_success_sampling_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#id SnsSmsPreferences#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monthly_spend_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#monthly_spend_limit SnsSmsPreferences#monthly_spend_limit}.'''
        result = self._values.get("monthly_spend_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def usage_report_s3_bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#usage_report_s3_bucket SnsSmsPreferences#usage_report_s3_bucket}.'''
        result = self._values.get("usage_report_s3_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SnsSmsPreferencesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SnsSmsPreferences",
    "SnsSmsPreferencesConfig",
]

publication.publish()
