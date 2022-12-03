'''
# `aws_cloudtrail`

Refer to the Terraform Registory for docs: [`aws_cloudtrail`](https://www.terraform.io/docs/providers/aws/r/cloudtrail).
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


class Cloudtrail(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudtrail.Cloudtrail",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail aws_cloudtrail}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        s3_bucket_name: builtins.str,
        advanced_event_selector: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudtrailAdvancedEventSelector", typing.Dict[str, typing.Any]]]]] = None,
        cloud_watch_logs_group_arn: typing.Optional[builtins.str] = None,
        cloud_watch_logs_role_arn: typing.Optional[builtins.str] = None,
        enable_log_file_validation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_logging: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        event_selector: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudtrailEventSelector", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        include_global_service_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        insight_selector: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudtrailInsightSelector", typing.Dict[str, typing.Any]]]]] = None,
        is_multi_region_trail: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_organization_trail: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        sns_topic_name: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail aws_cloudtrail} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#name Cloudtrail#name}.
        :param s3_bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#s3_bucket_name Cloudtrail#s3_bucket_name}.
        :param advanced_event_selector: advanced_event_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#advanced_event_selector Cloudtrail#advanced_event_selector}
        :param cloud_watch_logs_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#cloud_watch_logs_group_arn Cloudtrail#cloud_watch_logs_group_arn}.
        :param cloud_watch_logs_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#cloud_watch_logs_role_arn Cloudtrail#cloud_watch_logs_role_arn}.
        :param enable_log_file_validation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#enable_log_file_validation Cloudtrail#enable_log_file_validation}.
        :param enable_logging: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#enable_logging Cloudtrail#enable_logging}.
        :param event_selector: event_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#event_selector Cloudtrail#event_selector}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#id Cloudtrail#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param include_global_service_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#include_global_service_events Cloudtrail#include_global_service_events}.
        :param insight_selector: insight_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#insight_selector Cloudtrail#insight_selector}
        :param is_multi_region_trail: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#is_multi_region_trail Cloudtrail#is_multi_region_trail}.
        :param is_organization_trail: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#is_organization_trail Cloudtrail#is_organization_trail}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#kms_key_id Cloudtrail#kms_key_id}.
        :param s3_key_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#s3_key_prefix Cloudtrail#s3_key_prefix}.
        :param sns_topic_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#sns_topic_name Cloudtrail#sns_topic_name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#tags Cloudtrail#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#tags_all Cloudtrail#tags_all}.
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
                s3_bucket_name: builtins.str,
                advanced_event_selector: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudtrailAdvancedEventSelector, typing.Dict[str, typing.Any]]]]] = None,
                cloud_watch_logs_group_arn: typing.Optional[builtins.str] = None,
                cloud_watch_logs_role_arn: typing.Optional[builtins.str] = None,
                enable_log_file_validation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                enable_logging: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                event_selector: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudtrailEventSelector, typing.Dict[str, typing.Any]]]]] = None,
                id: typing.Optional[builtins.str] = None,
                include_global_service_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                insight_selector: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudtrailInsightSelector, typing.Dict[str, typing.Any]]]]] = None,
                is_multi_region_trail: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                is_organization_trail: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                kms_key_id: typing.Optional[builtins.str] = None,
                s3_key_prefix: typing.Optional[builtins.str] = None,
                sns_topic_name: typing.Optional[builtins.str] = None,
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
        config = CloudtrailConfig(
            name=name,
            s3_bucket_name=s3_bucket_name,
            advanced_event_selector=advanced_event_selector,
            cloud_watch_logs_group_arn=cloud_watch_logs_group_arn,
            cloud_watch_logs_role_arn=cloud_watch_logs_role_arn,
            enable_log_file_validation=enable_log_file_validation,
            enable_logging=enable_logging,
            event_selector=event_selector,
            id=id,
            include_global_service_events=include_global_service_events,
            insight_selector=insight_selector,
            is_multi_region_trail=is_multi_region_trail,
            is_organization_trail=is_organization_trail,
            kms_key_id=kms_key_id,
            s3_key_prefix=s3_key_prefix,
            sns_topic_name=sns_topic_name,
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

    @jsii.member(jsii_name="putAdvancedEventSelector")
    def put_advanced_event_selector(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudtrailAdvancedEventSelector", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudtrailAdvancedEventSelector, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdvancedEventSelector", [value]))

    @jsii.member(jsii_name="putEventSelector")
    def put_event_selector(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudtrailEventSelector", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudtrailEventSelector, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEventSelector", [value]))

    @jsii.member(jsii_name="putInsightSelector")
    def put_insight_selector(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudtrailInsightSelector", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudtrailInsightSelector, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInsightSelector", [value]))

    @jsii.member(jsii_name="resetAdvancedEventSelector")
    def reset_advanced_event_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvancedEventSelector", []))

    @jsii.member(jsii_name="resetCloudWatchLogsGroupArn")
    def reset_cloud_watch_logs_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudWatchLogsGroupArn", []))

    @jsii.member(jsii_name="resetCloudWatchLogsRoleArn")
    def reset_cloud_watch_logs_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudWatchLogsRoleArn", []))

    @jsii.member(jsii_name="resetEnableLogFileValidation")
    def reset_enable_log_file_validation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableLogFileValidation", []))

    @jsii.member(jsii_name="resetEnableLogging")
    def reset_enable_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableLogging", []))

    @jsii.member(jsii_name="resetEventSelector")
    def reset_event_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventSelector", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIncludeGlobalServiceEvents")
    def reset_include_global_service_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeGlobalServiceEvents", []))

    @jsii.member(jsii_name="resetInsightSelector")
    def reset_insight_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsightSelector", []))

    @jsii.member(jsii_name="resetIsMultiRegionTrail")
    def reset_is_multi_region_trail(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsMultiRegionTrail", []))

    @jsii.member(jsii_name="resetIsOrganizationTrail")
    def reset_is_organization_trail(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsOrganizationTrail", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetS3KeyPrefix")
    def reset_s3_key_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3KeyPrefix", []))

    @jsii.member(jsii_name="resetSnsTopicName")
    def reset_sns_topic_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnsTopicName", []))

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
    @jsii.member(jsii_name="advancedEventSelector")
    def advanced_event_selector(self) -> "CloudtrailAdvancedEventSelectorList":
        return typing.cast("CloudtrailAdvancedEventSelectorList", jsii.get(self, "advancedEventSelector"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="eventSelector")
    def event_selector(self) -> "CloudtrailEventSelectorList":
        return typing.cast("CloudtrailEventSelectorList", jsii.get(self, "eventSelector"))

    @builtins.property
    @jsii.member(jsii_name="homeRegion")
    def home_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "homeRegion"))

    @builtins.property
    @jsii.member(jsii_name="insightSelector")
    def insight_selector(self) -> "CloudtrailInsightSelectorList":
        return typing.cast("CloudtrailInsightSelectorList", jsii.get(self, "insightSelector"))

    @builtins.property
    @jsii.member(jsii_name="advancedEventSelectorInput")
    def advanced_event_selector_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudtrailAdvancedEventSelector"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudtrailAdvancedEventSelector"]]], jsii.get(self, "advancedEventSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudWatchLogsGroupArnInput")
    def cloud_watch_logs_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudWatchLogsGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudWatchLogsRoleArnInput")
    def cloud_watch_logs_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudWatchLogsRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="enableLogFileValidationInput")
    def enable_log_file_validation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableLogFileValidationInput"))

    @builtins.property
    @jsii.member(jsii_name="enableLoggingInput")
    def enable_logging_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableLoggingInput"))

    @builtins.property
    @jsii.member(jsii_name="eventSelectorInput")
    def event_selector_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudtrailEventSelector"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudtrailEventSelector"]]], jsii.get(self, "eventSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="includeGlobalServiceEventsInput")
    def include_global_service_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeGlobalServiceEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="insightSelectorInput")
    def insight_selector_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudtrailInsightSelector"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudtrailInsightSelector"]]], jsii.get(self, "insightSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="isMultiRegionTrailInput")
    def is_multi_region_trail_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isMultiRegionTrailInput"))

    @builtins.property
    @jsii.member(jsii_name="isOrganizationTrailInput")
    def is_organization_trail_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isOrganizationTrailInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketNameInput")
    def s3_bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="s3KeyPrefixInput")
    def s3_key_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3KeyPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="snsTopicNameInput")
    def sns_topic_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snsTopicNameInput"))

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
    @jsii.member(jsii_name="cloudWatchLogsGroupArn")
    def cloud_watch_logs_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudWatchLogsGroupArn"))

    @cloud_watch_logs_group_arn.setter
    def cloud_watch_logs_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudWatchLogsGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="cloudWatchLogsRoleArn")
    def cloud_watch_logs_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudWatchLogsRoleArn"))

    @cloud_watch_logs_role_arn.setter
    def cloud_watch_logs_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudWatchLogsRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="enableLogFileValidation")
    def enable_log_file_validation(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableLogFileValidation"))

    @enable_log_file_validation.setter
    def enable_log_file_validation(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableLogFileValidation", value)

    @builtins.property
    @jsii.member(jsii_name="enableLogging")
    def enable_logging(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableLogging"))

    @enable_logging.setter
    def enable_logging(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableLogging", value)

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
    @jsii.member(jsii_name="includeGlobalServiceEvents")
    def include_global_service_events(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeGlobalServiceEvents"))

    @include_global_service_events.setter
    def include_global_service_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeGlobalServiceEvents", value)

    @builtins.property
    @jsii.member(jsii_name="isMultiRegionTrail")
    def is_multi_region_trail(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isMultiRegionTrail"))

    @is_multi_region_trail.setter
    def is_multi_region_trail(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isMultiRegionTrail", value)

    @builtins.property
    @jsii.member(jsii_name="isOrganizationTrail")
    def is_organization_trail(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isOrganizationTrail"))

    @is_organization_trail.setter
    def is_organization_trail(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isOrganizationTrail", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

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
    @jsii.member(jsii_name="s3BucketName")
    def s3_bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3BucketName"))

    @s3_bucket_name.setter
    def s3_bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BucketName", value)

    @builtins.property
    @jsii.member(jsii_name="s3KeyPrefix")
    def s3_key_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3KeyPrefix"))

    @s3_key_prefix.setter
    def s3_key_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3KeyPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="snsTopicName")
    def sns_topic_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snsTopicName"))

    @sns_topic_name.setter
    def sns_topic_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsTopicName", value)

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
    jsii_type="@cdktf/provider-aws.cloudtrail.CloudtrailAdvancedEventSelector",
    jsii_struct_bases=[],
    name_mapping={"field_selector": "fieldSelector", "name": "name"},
)
class CloudtrailAdvancedEventSelector:
    def __init__(
        self,
        *,
        field_selector: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudtrailAdvancedEventSelectorFieldSelector", typing.Dict[str, typing.Any]]]],
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param field_selector: field_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#field_selector Cloudtrail#field_selector}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#name Cloudtrail#name}.
        '''
        if __debug__:
            def stub(
                *,
                field_selector: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudtrailAdvancedEventSelectorFieldSelector, typing.Dict[str, typing.Any]]]],
                name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument field_selector", value=field_selector, expected_type=type_hints["field_selector"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "field_selector": field_selector,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def field_selector(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["CloudtrailAdvancedEventSelectorFieldSelector"]]:
        '''field_selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#field_selector Cloudtrail#field_selector}
        '''
        result = self._values.get("field_selector")
        assert result is not None, "Required property 'field_selector' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["CloudtrailAdvancedEventSelectorFieldSelector"]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#name Cloudtrail#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudtrailAdvancedEventSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudtrail.CloudtrailAdvancedEventSelectorFieldSelector",
    jsii_struct_bases=[],
    name_mapping={
        "field": "field",
        "ends_with": "endsWith",
        "equal_to": "equalTo",
        "not_ends_with": "notEndsWith",
        "not_equals": "notEquals",
        "not_starts_with": "notStartsWith",
        "starts_with": "startsWith",
    },
)
class CloudtrailAdvancedEventSelectorFieldSelector:
    def __init__(
        self,
        *,
        field: builtins.str,
        ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
        equal_to: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_equals: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
        starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#field Cloudtrail#field}.
        :param ends_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#ends_with Cloudtrail#ends_with}.
        :param equal_to: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#equals Cloudtrail#equals}.
        :param not_ends_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#not_ends_with Cloudtrail#not_ends_with}.
        :param not_equals: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#not_equals Cloudtrail#not_equals}.
        :param not_starts_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#not_starts_with Cloudtrail#not_starts_with}.
        :param starts_with: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#starts_with Cloudtrail#starts_with}.
        '''
        if __debug__:
            def stub(
                *,
                field: builtins.str,
                ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
                equal_to: typing.Optional[typing.Sequence[builtins.str]] = None,
                not_ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
                not_equals: typing.Optional[typing.Sequence[builtins.str]] = None,
                not_starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
                starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
            check_type(argname="argument ends_with", value=ends_with, expected_type=type_hints["ends_with"])
            check_type(argname="argument equal_to", value=equal_to, expected_type=type_hints["equal_to"])
            check_type(argname="argument not_ends_with", value=not_ends_with, expected_type=type_hints["not_ends_with"])
            check_type(argname="argument not_equals", value=not_equals, expected_type=type_hints["not_equals"])
            check_type(argname="argument not_starts_with", value=not_starts_with, expected_type=type_hints["not_starts_with"])
            check_type(argname="argument starts_with", value=starts_with, expected_type=type_hints["starts_with"])
        self._values: typing.Dict[str, typing.Any] = {
            "field": field,
        }
        if ends_with is not None:
            self._values["ends_with"] = ends_with
        if equal_to is not None:
            self._values["equal_to"] = equal_to
        if not_ends_with is not None:
            self._values["not_ends_with"] = not_ends_with
        if not_equals is not None:
            self._values["not_equals"] = not_equals
        if not_starts_with is not None:
            self._values["not_starts_with"] = not_starts_with
        if starts_with is not None:
            self._values["starts_with"] = starts_with

    @builtins.property
    def field(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#field Cloudtrail#field}.'''
        result = self._values.get("field")
        assert result is not None, "Required property 'field' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ends_with(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#ends_with Cloudtrail#ends_with}.'''
        result = self._values.get("ends_with")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def equal_to(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#equals Cloudtrail#equals}.'''
        result = self._values.get("equal_to")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def not_ends_with(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#not_ends_with Cloudtrail#not_ends_with}.'''
        result = self._values.get("not_ends_with")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def not_equals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#not_equals Cloudtrail#not_equals}.'''
        result = self._values.get("not_equals")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def not_starts_with(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#not_starts_with Cloudtrail#not_starts_with}.'''
        result = self._values.get("not_starts_with")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def starts_with(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#starts_with Cloudtrail#starts_with}.'''
        result = self._values.get("starts_with")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudtrailAdvancedEventSelectorFieldSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudtrailAdvancedEventSelectorFieldSelectorList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudtrail.CloudtrailAdvancedEventSelectorFieldSelectorList",
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
    ) -> "CloudtrailAdvancedEventSelectorFieldSelectorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudtrailAdvancedEventSelectorFieldSelectorOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailAdvancedEventSelectorFieldSelector]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailAdvancedEventSelectorFieldSelector]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailAdvancedEventSelectorFieldSelector]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailAdvancedEventSelectorFieldSelector]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudtrailAdvancedEventSelectorFieldSelectorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudtrail.CloudtrailAdvancedEventSelectorFieldSelectorOutputReference",
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

    @jsii.member(jsii_name="resetEndsWith")
    def reset_ends_with(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndsWith", []))

    @jsii.member(jsii_name="resetEqualTo")
    def reset_equal_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEqualTo", []))

    @jsii.member(jsii_name="resetNotEndsWith")
    def reset_not_ends_with(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotEndsWith", []))

    @jsii.member(jsii_name="resetNotEquals")
    def reset_not_equals(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotEquals", []))

    @jsii.member(jsii_name="resetNotStartsWith")
    def reset_not_starts_with(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotStartsWith", []))

    @jsii.member(jsii_name="resetStartsWith")
    def reset_starts_with(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartsWith", []))

    @builtins.property
    @jsii.member(jsii_name="endsWithInput")
    def ends_with_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "endsWithInput"))

    @builtins.property
    @jsii.member(jsii_name="equalToInput")
    def equal_to_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "equalToInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldInput")
    def field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldInput"))

    @builtins.property
    @jsii.member(jsii_name="notEndsWithInput")
    def not_ends_with_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notEndsWithInput"))

    @builtins.property
    @jsii.member(jsii_name="notEqualsInput")
    def not_equals_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notEqualsInput"))

    @builtins.property
    @jsii.member(jsii_name="notStartsWithInput")
    def not_starts_with_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notStartsWithInput"))

    @builtins.property
    @jsii.member(jsii_name="startsWithInput")
    def starts_with_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "startsWithInput"))

    @builtins.property
    @jsii.member(jsii_name="endsWith")
    def ends_with(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "endsWith"))

    @ends_with.setter
    def ends_with(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endsWith", value)

    @builtins.property
    @jsii.member(jsii_name="equalTo")
    def equal_to(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "equalTo"))

    @equal_to.setter
    def equal_to(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "equalTo", value)

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
    @jsii.member(jsii_name="notEndsWith")
    def not_ends_with(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notEndsWith"))

    @not_ends_with.setter
    def not_ends_with(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notEndsWith", value)

    @builtins.property
    @jsii.member(jsii_name="notEquals")
    def not_equals(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notEquals"))

    @not_equals.setter
    def not_equals(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notEquals", value)

    @builtins.property
    @jsii.member(jsii_name="notStartsWith")
    def not_starts_with(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notStartsWith"))

    @not_starts_with.setter
    def not_starts_with(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notStartsWith", value)

    @builtins.property
    @jsii.member(jsii_name="startsWith")
    def starts_with(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "startsWith"))

    @starts_with.setter
    def starts_with(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startsWith", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudtrailAdvancedEventSelectorFieldSelector, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudtrailAdvancedEventSelectorFieldSelector, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudtrailAdvancedEventSelectorFieldSelector, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CloudtrailAdvancedEventSelectorFieldSelector, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudtrailAdvancedEventSelectorList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudtrail.CloudtrailAdvancedEventSelectorList",
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
    ) -> "CloudtrailAdvancedEventSelectorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudtrailAdvancedEventSelectorOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailAdvancedEventSelector]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailAdvancedEventSelector]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailAdvancedEventSelector]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailAdvancedEventSelector]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudtrailAdvancedEventSelectorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudtrail.CloudtrailAdvancedEventSelectorOutputReference",
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

    @jsii.member(jsii_name="putFieldSelector")
    def put_field_selector(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudtrailAdvancedEventSelectorFieldSelector, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudtrailAdvancedEventSelectorFieldSelector, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFieldSelector", [value]))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="fieldSelector")
    def field_selector(self) -> CloudtrailAdvancedEventSelectorFieldSelectorList:
        return typing.cast(CloudtrailAdvancedEventSelectorFieldSelectorList, jsii.get(self, "fieldSelector"))

    @builtins.property
    @jsii.member(jsii_name="fieldSelectorInput")
    def field_selector_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailAdvancedEventSelectorFieldSelector]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailAdvancedEventSelectorFieldSelector]]], jsii.get(self, "fieldSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudtrailAdvancedEventSelector, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudtrailAdvancedEventSelector, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudtrailAdvancedEventSelector, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CloudtrailAdvancedEventSelector, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudtrail.CloudtrailConfig",
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
        "s3_bucket_name": "s3BucketName",
        "advanced_event_selector": "advancedEventSelector",
        "cloud_watch_logs_group_arn": "cloudWatchLogsGroupArn",
        "cloud_watch_logs_role_arn": "cloudWatchLogsRoleArn",
        "enable_log_file_validation": "enableLogFileValidation",
        "enable_logging": "enableLogging",
        "event_selector": "eventSelector",
        "id": "id",
        "include_global_service_events": "includeGlobalServiceEvents",
        "insight_selector": "insightSelector",
        "is_multi_region_trail": "isMultiRegionTrail",
        "is_organization_trail": "isOrganizationTrail",
        "kms_key_id": "kmsKeyId",
        "s3_key_prefix": "s3KeyPrefix",
        "sns_topic_name": "snsTopicName",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class CloudtrailConfig(cdktf.TerraformMetaArguments):
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
        s3_bucket_name: builtins.str,
        advanced_event_selector: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudtrailAdvancedEventSelector, typing.Dict[str, typing.Any]]]]] = None,
        cloud_watch_logs_group_arn: typing.Optional[builtins.str] = None,
        cloud_watch_logs_role_arn: typing.Optional[builtins.str] = None,
        enable_log_file_validation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_logging: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        event_selector: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudtrailEventSelector", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        include_global_service_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        insight_selector: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudtrailInsightSelector", typing.Dict[str, typing.Any]]]]] = None,
        is_multi_region_trail: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_organization_trail: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        sns_topic_name: typing.Optional[builtins.str] = None,
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#name Cloudtrail#name}.
        :param s3_bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#s3_bucket_name Cloudtrail#s3_bucket_name}.
        :param advanced_event_selector: advanced_event_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#advanced_event_selector Cloudtrail#advanced_event_selector}
        :param cloud_watch_logs_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#cloud_watch_logs_group_arn Cloudtrail#cloud_watch_logs_group_arn}.
        :param cloud_watch_logs_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#cloud_watch_logs_role_arn Cloudtrail#cloud_watch_logs_role_arn}.
        :param enable_log_file_validation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#enable_log_file_validation Cloudtrail#enable_log_file_validation}.
        :param enable_logging: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#enable_logging Cloudtrail#enable_logging}.
        :param event_selector: event_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#event_selector Cloudtrail#event_selector}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#id Cloudtrail#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param include_global_service_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#include_global_service_events Cloudtrail#include_global_service_events}.
        :param insight_selector: insight_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#insight_selector Cloudtrail#insight_selector}
        :param is_multi_region_trail: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#is_multi_region_trail Cloudtrail#is_multi_region_trail}.
        :param is_organization_trail: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#is_organization_trail Cloudtrail#is_organization_trail}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#kms_key_id Cloudtrail#kms_key_id}.
        :param s3_key_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#s3_key_prefix Cloudtrail#s3_key_prefix}.
        :param sns_topic_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#sns_topic_name Cloudtrail#sns_topic_name}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#tags Cloudtrail#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#tags_all Cloudtrail#tags_all}.
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
                name: builtins.str,
                s3_bucket_name: builtins.str,
                advanced_event_selector: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudtrailAdvancedEventSelector, typing.Dict[str, typing.Any]]]]] = None,
                cloud_watch_logs_group_arn: typing.Optional[builtins.str] = None,
                cloud_watch_logs_role_arn: typing.Optional[builtins.str] = None,
                enable_log_file_validation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                enable_logging: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                event_selector: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudtrailEventSelector, typing.Dict[str, typing.Any]]]]] = None,
                id: typing.Optional[builtins.str] = None,
                include_global_service_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                insight_selector: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudtrailInsightSelector, typing.Dict[str, typing.Any]]]]] = None,
                is_multi_region_trail: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                is_organization_trail: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                kms_key_id: typing.Optional[builtins.str] = None,
                s3_key_prefix: typing.Optional[builtins.str] = None,
                sns_topic_name: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
            check_type(argname="argument advanced_event_selector", value=advanced_event_selector, expected_type=type_hints["advanced_event_selector"])
            check_type(argname="argument cloud_watch_logs_group_arn", value=cloud_watch_logs_group_arn, expected_type=type_hints["cloud_watch_logs_group_arn"])
            check_type(argname="argument cloud_watch_logs_role_arn", value=cloud_watch_logs_role_arn, expected_type=type_hints["cloud_watch_logs_role_arn"])
            check_type(argname="argument enable_log_file_validation", value=enable_log_file_validation, expected_type=type_hints["enable_log_file_validation"])
            check_type(argname="argument enable_logging", value=enable_logging, expected_type=type_hints["enable_logging"])
            check_type(argname="argument event_selector", value=event_selector, expected_type=type_hints["event_selector"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument include_global_service_events", value=include_global_service_events, expected_type=type_hints["include_global_service_events"])
            check_type(argname="argument insight_selector", value=insight_selector, expected_type=type_hints["insight_selector"])
            check_type(argname="argument is_multi_region_trail", value=is_multi_region_trail, expected_type=type_hints["is_multi_region_trail"])
            check_type(argname="argument is_organization_trail", value=is_organization_trail, expected_type=type_hints["is_organization_trail"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument s3_key_prefix", value=s3_key_prefix, expected_type=type_hints["s3_key_prefix"])
            check_type(argname="argument sns_topic_name", value=sns_topic_name, expected_type=type_hints["sns_topic_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "s3_bucket_name": s3_bucket_name,
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
        if advanced_event_selector is not None:
            self._values["advanced_event_selector"] = advanced_event_selector
        if cloud_watch_logs_group_arn is not None:
            self._values["cloud_watch_logs_group_arn"] = cloud_watch_logs_group_arn
        if cloud_watch_logs_role_arn is not None:
            self._values["cloud_watch_logs_role_arn"] = cloud_watch_logs_role_arn
        if enable_log_file_validation is not None:
            self._values["enable_log_file_validation"] = enable_log_file_validation
        if enable_logging is not None:
            self._values["enable_logging"] = enable_logging
        if event_selector is not None:
            self._values["event_selector"] = event_selector
        if id is not None:
            self._values["id"] = id
        if include_global_service_events is not None:
            self._values["include_global_service_events"] = include_global_service_events
        if insight_selector is not None:
            self._values["insight_selector"] = insight_selector
        if is_multi_region_trail is not None:
            self._values["is_multi_region_trail"] = is_multi_region_trail
        if is_organization_trail is not None:
            self._values["is_organization_trail"] = is_organization_trail
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if s3_key_prefix is not None:
            self._values["s3_key_prefix"] = s3_key_prefix
        if sns_topic_name is not None:
            self._values["sns_topic_name"] = sns_topic_name
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#name Cloudtrail#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#s3_bucket_name Cloudtrail#s3_bucket_name}.'''
        result = self._values.get("s3_bucket_name")
        assert result is not None, "Required property 's3_bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def advanced_event_selector(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailAdvancedEventSelector]]]:
        '''advanced_event_selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#advanced_event_selector Cloudtrail#advanced_event_selector}
        '''
        result = self._values.get("advanced_event_selector")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailAdvancedEventSelector]]], result)

    @builtins.property
    def cloud_watch_logs_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#cloud_watch_logs_group_arn Cloudtrail#cloud_watch_logs_group_arn}.'''
        result = self._values.get("cloud_watch_logs_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_watch_logs_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#cloud_watch_logs_role_arn Cloudtrail#cloud_watch_logs_role_arn}.'''
        result = self._values.get("cloud_watch_logs_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_log_file_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#enable_log_file_validation Cloudtrail#enable_log_file_validation}.'''
        result = self._values.get("enable_log_file_validation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_logging(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#enable_logging Cloudtrail#enable_logging}.'''
        result = self._values.get("enable_logging")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def event_selector(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudtrailEventSelector"]]]:
        '''event_selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#event_selector Cloudtrail#event_selector}
        '''
        result = self._values.get("event_selector")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudtrailEventSelector"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#id Cloudtrail#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def include_global_service_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#include_global_service_events Cloudtrail#include_global_service_events}.'''
        result = self._values.get("include_global_service_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def insight_selector(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudtrailInsightSelector"]]]:
        '''insight_selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#insight_selector Cloudtrail#insight_selector}
        '''
        result = self._values.get("insight_selector")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudtrailInsightSelector"]]], result)

    @builtins.property
    def is_multi_region_trail(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#is_multi_region_trail Cloudtrail#is_multi_region_trail}.'''
        result = self._values.get("is_multi_region_trail")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def is_organization_trail(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#is_organization_trail Cloudtrail#is_organization_trail}.'''
        result = self._values.get("is_organization_trail")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#kms_key_id Cloudtrail#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#s3_key_prefix Cloudtrail#s3_key_prefix}.'''
        result = self._values.get("s3_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sns_topic_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#sns_topic_name Cloudtrail#sns_topic_name}.'''
        result = self._values.get("sns_topic_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#tags Cloudtrail#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#tags_all Cloudtrail#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudtrailConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudtrail.CloudtrailEventSelector",
    jsii_struct_bases=[],
    name_mapping={
        "data_resource": "dataResource",
        "exclude_management_event_sources": "excludeManagementEventSources",
        "include_management_events": "includeManagementEvents",
        "read_write_type": "readWriteType",
    },
)
class CloudtrailEventSelector:
    def __init__(
        self,
        *,
        data_resource: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CloudtrailEventSelectorDataResource", typing.Dict[str, typing.Any]]]]] = None,
        exclude_management_event_sources: typing.Optional[typing.Sequence[builtins.str]] = None,
        include_management_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        read_write_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param data_resource: data_resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#data_resource Cloudtrail#data_resource}
        :param exclude_management_event_sources: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#exclude_management_event_sources Cloudtrail#exclude_management_event_sources}.
        :param include_management_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#include_management_events Cloudtrail#include_management_events}.
        :param read_write_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#read_write_type Cloudtrail#read_write_type}.
        '''
        if __debug__:
            def stub(
                *,
                data_resource: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudtrailEventSelectorDataResource, typing.Dict[str, typing.Any]]]]] = None,
                exclude_management_event_sources: typing.Optional[typing.Sequence[builtins.str]] = None,
                include_management_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                read_write_type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument data_resource", value=data_resource, expected_type=type_hints["data_resource"])
            check_type(argname="argument exclude_management_event_sources", value=exclude_management_event_sources, expected_type=type_hints["exclude_management_event_sources"])
            check_type(argname="argument include_management_events", value=include_management_events, expected_type=type_hints["include_management_events"])
            check_type(argname="argument read_write_type", value=read_write_type, expected_type=type_hints["read_write_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if data_resource is not None:
            self._values["data_resource"] = data_resource
        if exclude_management_event_sources is not None:
            self._values["exclude_management_event_sources"] = exclude_management_event_sources
        if include_management_events is not None:
            self._values["include_management_events"] = include_management_events
        if read_write_type is not None:
            self._values["read_write_type"] = read_write_type

    @builtins.property
    def data_resource(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudtrailEventSelectorDataResource"]]]:
        '''data_resource block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#data_resource Cloudtrail#data_resource}
        '''
        result = self._values.get("data_resource")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CloudtrailEventSelectorDataResource"]]], result)

    @builtins.property
    def exclude_management_event_sources(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#exclude_management_event_sources Cloudtrail#exclude_management_event_sources}.'''
        result = self._values.get("exclude_management_event_sources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def include_management_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#include_management_events Cloudtrail#include_management_events}.'''
        result = self._values.get("include_management_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def read_write_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#read_write_type Cloudtrail#read_write_type}.'''
        result = self._values.get("read_write_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudtrailEventSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudtrail.CloudtrailEventSelectorDataResource",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "values": "values"},
)
class CloudtrailEventSelectorDataResource:
    def __init__(
        self,
        *,
        type: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#type Cloudtrail#type}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#values Cloudtrail#values}.
        '''
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                values: typing.Sequence[builtins.str],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
            "values": values,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#type Cloudtrail#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#values Cloudtrail#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudtrailEventSelectorDataResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudtrailEventSelectorDataResourceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudtrail.CloudtrailEventSelectorDataResourceList",
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
    ) -> "CloudtrailEventSelectorDataResourceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudtrailEventSelectorDataResourceOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailEventSelectorDataResource]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailEventSelectorDataResource]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailEventSelectorDataResource]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailEventSelectorDataResource]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudtrailEventSelectorDataResourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudtrail.CloudtrailEventSelectorDataResourceOutputReference",
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
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

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
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudtrailEventSelectorDataResource, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudtrailEventSelectorDataResource, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudtrailEventSelectorDataResource, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CloudtrailEventSelectorDataResource, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudtrailEventSelectorList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudtrail.CloudtrailEventSelectorList",
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
    def get(self, index: jsii.Number) -> "CloudtrailEventSelectorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudtrailEventSelectorOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailEventSelector]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailEventSelector]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailEventSelector]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailEventSelector]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudtrailEventSelectorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudtrail.CloudtrailEventSelectorOutputReference",
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

    @jsii.member(jsii_name="putDataResource")
    def put_data_resource(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudtrailEventSelectorDataResource, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CloudtrailEventSelectorDataResource, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDataResource", [value]))

    @jsii.member(jsii_name="resetDataResource")
    def reset_data_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataResource", []))

    @jsii.member(jsii_name="resetExcludeManagementEventSources")
    def reset_exclude_management_event_sources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeManagementEventSources", []))

    @jsii.member(jsii_name="resetIncludeManagementEvents")
    def reset_include_management_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeManagementEvents", []))

    @jsii.member(jsii_name="resetReadWriteType")
    def reset_read_write_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadWriteType", []))

    @builtins.property
    @jsii.member(jsii_name="dataResource")
    def data_resource(self) -> CloudtrailEventSelectorDataResourceList:
        return typing.cast(CloudtrailEventSelectorDataResourceList, jsii.get(self, "dataResource"))

    @builtins.property
    @jsii.member(jsii_name="dataResourceInput")
    def data_resource_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailEventSelectorDataResource]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailEventSelectorDataResource]]], jsii.get(self, "dataResourceInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeManagementEventSourcesInput")
    def exclude_management_event_sources_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludeManagementEventSourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="includeManagementEventsInput")
    def include_management_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeManagementEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="readWriteTypeInput")
    def read_write_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readWriteTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeManagementEventSources")
    def exclude_management_event_sources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "excludeManagementEventSources"))

    @exclude_management_event_sources.setter
    def exclude_management_event_sources(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeManagementEventSources", value)

    @builtins.property
    @jsii.member(jsii_name="includeManagementEvents")
    def include_management_events(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeManagementEvents"))

    @include_management_events.setter
    def include_management_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeManagementEvents", value)

    @builtins.property
    @jsii.member(jsii_name="readWriteType")
    def read_write_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "readWriteType"))

    @read_write_type.setter
    def read_write_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readWriteType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudtrailEventSelector, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudtrailEventSelector, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudtrailEventSelector, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CloudtrailEventSelector, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudtrail.CloudtrailInsightSelector",
    jsii_struct_bases=[],
    name_mapping={"insight_type": "insightType"},
)
class CloudtrailInsightSelector:
    def __init__(self, *, insight_type: builtins.str) -> None:
        '''
        :param insight_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#insight_type Cloudtrail#insight_type}.
        '''
        if __debug__:
            def stub(*, insight_type: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument insight_type", value=insight_type, expected_type=type_hints["insight_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "insight_type": insight_type,
        }

    @builtins.property
    def insight_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudtrail#insight_type Cloudtrail#insight_type}.'''
        result = self._values.get("insight_type")
        assert result is not None, "Required property 'insight_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudtrailInsightSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudtrailInsightSelectorList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudtrail.CloudtrailInsightSelectorList",
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
    def get(self, index: jsii.Number) -> "CloudtrailInsightSelectorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudtrailInsightSelectorOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailInsightSelector]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailInsightSelector]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailInsightSelector]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CloudtrailInsightSelector]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudtrailInsightSelectorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudtrail.CloudtrailInsightSelectorOutputReference",
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
    @jsii.member(jsii_name="insightTypeInput")
    def insight_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "insightTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="insightType")
    def insight_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "insightType"))

    @insight_type.setter
    def insight_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insightType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudtrailInsightSelector, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudtrailInsightSelector, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudtrailInsightSelector, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CloudtrailInsightSelector, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Cloudtrail",
    "CloudtrailAdvancedEventSelector",
    "CloudtrailAdvancedEventSelectorFieldSelector",
    "CloudtrailAdvancedEventSelectorFieldSelectorList",
    "CloudtrailAdvancedEventSelectorFieldSelectorOutputReference",
    "CloudtrailAdvancedEventSelectorList",
    "CloudtrailAdvancedEventSelectorOutputReference",
    "CloudtrailConfig",
    "CloudtrailEventSelector",
    "CloudtrailEventSelectorDataResource",
    "CloudtrailEventSelectorDataResourceList",
    "CloudtrailEventSelectorDataResourceOutputReference",
    "CloudtrailEventSelectorList",
    "CloudtrailEventSelectorOutputReference",
    "CloudtrailInsightSelector",
    "CloudtrailInsightSelectorList",
    "CloudtrailInsightSelectorOutputReference",
]

publication.publish()
