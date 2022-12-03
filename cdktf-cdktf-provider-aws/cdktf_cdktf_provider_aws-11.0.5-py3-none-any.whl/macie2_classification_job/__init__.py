'''
# `aws_macie2_classification_job`

Refer to the Terraform Registory for docs: [`aws_macie2_classification_job`](https://www.terraform.io/docs/providers/aws/r/macie2_classification_job).
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


class Macie2ClassificationJob(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJob",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job aws_macie2_classification_job}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        job_type: builtins.str,
        s3_job_definition: typing.Union["Macie2ClassificationJobS3JobDefinition", typing.Dict[str, typing.Any]],
        custom_data_identifier_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        initial_run: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        job_status: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        sampling_percentage: typing.Optional[jsii.Number] = None,
        schedule_frequency: typing.Optional[typing.Union["Macie2ClassificationJobScheduleFrequency", typing.Dict[str, typing.Any]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job aws_macie2_classification_job} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param job_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#job_type Macie2ClassificationJob#job_type}.
        :param s3_job_definition: s3_job_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#s3_job_definition Macie2ClassificationJob#s3_job_definition}
        :param custom_data_identifier_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#custom_data_identifier_ids Macie2ClassificationJob#custom_data_identifier_ids}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#description Macie2ClassificationJob#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#id Macie2ClassificationJob#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_run: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#initial_run Macie2ClassificationJob#initial_run}.
        :param job_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#job_status Macie2ClassificationJob#job_status}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#name Macie2ClassificationJob#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#name_prefix Macie2ClassificationJob#name_prefix}.
        :param sampling_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#sampling_percentage Macie2ClassificationJob#sampling_percentage}.
        :param schedule_frequency: schedule_frequency block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#schedule_frequency Macie2ClassificationJob#schedule_frequency}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tags Macie2ClassificationJob#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tags_all Macie2ClassificationJob#tags_all}.
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
                job_type: builtins.str,
                s3_job_definition: typing.Union[Macie2ClassificationJobS3JobDefinition, typing.Dict[str, typing.Any]],
                custom_data_identifier_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                initial_run: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                job_status: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                name_prefix: typing.Optional[builtins.str] = None,
                sampling_percentage: typing.Optional[jsii.Number] = None,
                schedule_frequency: typing.Optional[typing.Union[Macie2ClassificationJobScheduleFrequency, typing.Dict[str, typing.Any]]] = None,
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
        config = Macie2ClassificationJobConfig(
            job_type=job_type,
            s3_job_definition=s3_job_definition,
            custom_data_identifier_ids=custom_data_identifier_ids,
            description=description,
            id=id,
            initial_run=initial_run,
            job_status=job_status,
            name=name,
            name_prefix=name_prefix,
            sampling_percentage=sampling_percentage,
            schedule_frequency=schedule_frequency,
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

    @jsii.member(jsii_name="putS3JobDefinition")
    def put_s3_job_definition(
        self,
        *,
        bucket_criteria: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteria", typing.Dict[str, typing.Any]]] = None,
        bucket_definitions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketDefinitions", typing.Dict[str, typing.Any]]]]] = None,
        scoping: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScoping", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_criteria: bucket_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#bucket_criteria Macie2ClassificationJob#bucket_criteria}
        :param bucket_definitions: bucket_definitions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#bucket_definitions Macie2ClassificationJob#bucket_definitions}
        :param scoping: scoping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#scoping Macie2ClassificationJob#scoping}
        '''
        value = Macie2ClassificationJobS3JobDefinition(
            bucket_criteria=bucket_criteria,
            bucket_definitions=bucket_definitions,
            scoping=scoping,
        )

        return typing.cast(None, jsii.invoke(self, "putS3JobDefinition", [value]))

    @jsii.member(jsii_name="putScheduleFrequency")
    def put_schedule_frequency(
        self,
        *,
        daily_schedule: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        monthly_schedule: typing.Optional[jsii.Number] = None,
        weekly_schedule: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param daily_schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#daily_schedule Macie2ClassificationJob#daily_schedule}.
        :param monthly_schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#monthly_schedule Macie2ClassificationJob#monthly_schedule}.
        :param weekly_schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#weekly_schedule Macie2ClassificationJob#weekly_schedule}.
        '''
        value = Macie2ClassificationJobScheduleFrequency(
            daily_schedule=daily_schedule,
            monthly_schedule=monthly_schedule,
            weekly_schedule=weekly_schedule,
        )

        return typing.cast(None, jsii.invoke(self, "putScheduleFrequency", [value]))

    @jsii.member(jsii_name="resetCustomDataIdentifierIds")
    def reset_custom_data_identifier_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomDataIdentifierIds", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInitialRun")
    def reset_initial_run(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialRun", []))

    @jsii.member(jsii_name="resetJobStatus")
    def reset_job_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobStatus", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="resetSamplingPercentage")
    def reset_sampling_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSamplingPercentage", []))

    @jsii.member(jsii_name="resetScheduleFrequency")
    def reset_schedule_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduleFrequency", []))

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
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="jobArn")
    def job_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobArn"))

    @builtins.property
    @jsii.member(jsii_name="jobId")
    def job_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobId"))

    @builtins.property
    @jsii.member(jsii_name="s3JobDefinition")
    def s3_job_definition(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionOutputReference", jsii.get(self, "s3JobDefinition"))

    @builtins.property
    @jsii.member(jsii_name="scheduleFrequency")
    def schedule_frequency(
        self,
    ) -> "Macie2ClassificationJobScheduleFrequencyOutputReference":
        return typing.cast("Macie2ClassificationJobScheduleFrequencyOutputReference", jsii.get(self, "scheduleFrequency"))

    @builtins.property
    @jsii.member(jsii_name="userPausedDetails")
    def user_paused_details(self) -> "Macie2ClassificationJobUserPausedDetailsList":
        return typing.cast("Macie2ClassificationJobUserPausedDetailsList", jsii.get(self, "userPausedDetails"))

    @builtins.property
    @jsii.member(jsii_name="customDataIdentifierIdsInput")
    def custom_data_identifier_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "customDataIdentifierIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="initialRunInput")
    def initial_run_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "initialRunInput"))

    @builtins.property
    @jsii.member(jsii_name="jobStatusInput")
    def job_status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="jobTypeInput")
    def job_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="s3JobDefinitionInput")
    def s3_job_definition_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinition"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinition"], jsii.get(self, "s3JobDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="samplingPercentageInput")
    def sampling_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "samplingPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleFrequencyInput")
    def schedule_frequency_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobScheduleFrequency"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobScheduleFrequency"], jsii.get(self, "scheduleFrequencyInput"))

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
    @jsii.member(jsii_name="customDataIdentifierIds")
    def custom_data_identifier_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customDataIdentifierIds"))

    @custom_data_identifier_ids.setter
    def custom_data_identifier_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customDataIdentifierIds", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

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
    @jsii.member(jsii_name="initialRun")
    def initial_run(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "initialRun"))

    @initial_run.setter
    def initial_run(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialRun", value)

    @builtins.property
    @jsii.member(jsii_name="jobStatus")
    def job_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobStatus"))

    @job_status.setter
    def job_status(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobStatus", value)

    @builtins.property
    @jsii.member(jsii_name="jobType")
    def job_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobType"))

    @job_type.setter
    def job_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobType", value)

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
    @jsii.member(jsii_name="samplingPercentage")
    def sampling_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "samplingPercentage"))

    @sampling_percentage.setter
    def sampling_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samplingPercentage", value)

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
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "job_type": "jobType",
        "s3_job_definition": "s3JobDefinition",
        "custom_data_identifier_ids": "customDataIdentifierIds",
        "description": "description",
        "id": "id",
        "initial_run": "initialRun",
        "job_status": "jobStatus",
        "name": "name",
        "name_prefix": "namePrefix",
        "sampling_percentage": "samplingPercentage",
        "schedule_frequency": "scheduleFrequency",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class Macie2ClassificationJobConfig(cdktf.TerraformMetaArguments):
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
        job_type: builtins.str,
        s3_job_definition: typing.Union["Macie2ClassificationJobS3JobDefinition", typing.Dict[str, typing.Any]],
        custom_data_identifier_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        initial_run: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        job_status: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        sampling_percentage: typing.Optional[jsii.Number] = None,
        schedule_frequency: typing.Optional[typing.Union["Macie2ClassificationJobScheduleFrequency", typing.Dict[str, typing.Any]]] = None,
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
        :param job_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#job_type Macie2ClassificationJob#job_type}.
        :param s3_job_definition: s3_job_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#s3_job_definition Macie2ClassificationJob#s3_job_definition}
        :param custom_data_identifier_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#custom_data_identifier_ids Macie2ClassificationJob#custom_data_identifier_ids}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#description Macie2ClassificationJob#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#id Macie2ClassificationJob#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_run: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#initial_run Macie2ClassificationJob#initial_run}.
        :param job_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#job_status Macie2ClassificationJob#job_status}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#name Macie2ClassificationJob#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#name_prefix Macie2ClassificationJob#name_prefix}.
        :param sampling_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#sampling_percentage Macie2ClassificationJob#sampling_percentage}.
        :param schedule_frequency: schedule_frequency block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#schedule_frequency Macie2ClassificationJob#schedule_frequency}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tags Macie2ClassificationJob#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tags_all Macie2ClassificationJob#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(s3_job_definition, dict):
            s3_job_definition = Macie2ClassificationJobS3JobDefinition(**s3_job_definition)
        if isinstance(schedule_frequency, dict):
            schedule_frequency = Macie2ClassificationJobScheduleFrequency(**schedule_frequency)
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
                job_type: builtins.str,
                s3_job_definition: typing.Union[Macie2ClassificationJobS3JobDefinition, typing.Dict[str, typing.Any]],
                custom_data_identifier_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                initial_run: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                job_status: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                name_prefix: typing.Optional[builtins.str] = None,
                sampling_percentage: typing.Optional[jsii.Number] = None,
                schedule_frequency: typing.Optional[typing.Union[Macie2ClassificationJobScheduleFrequency, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument job_type", value=job_type, expected_type=type_hints["job_type"])
            check_type(argname="argument s3_job_definition", value=s3_job_definition, expected_type=type_hints["s3_job_definition"])
            check_type(argname="argument custom_data_identifier_ids", value=custom_data_identifier_ids, expected_type=type_hints["custom_data_identifier_ids"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument initial_run", value=initial_run, expected_type=type_hints["initial_run"])
            check_type(argname="argument job_status", value=job_status, expected_type=type_hints["job_status"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument sampling_percentage", value=sampling_percentage, expected_type=type_hints["sampling_percentage"])
            check_type(argname="argument schedule_frequency", value=schedule_frequency, expected_type=type_hints["schedule_frequency"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "job_type": job_type,
            "s3_job_definition": s3_job_definition,
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
        if custom_data_identifier_ids is not None:
            self._values["custom_data_identifier_ids"] = custom_data_identifier_ids
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if initial_run is not None:
            self._values["initial_run"] = initial_run
        if job_status is not None:
            self._values["job_status"] = job_status
        if name is not None:
            self._values["name"] = name
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
        if sampling_percentage is not None:
            self._values["sampling_percentage"] = sampling_percentage
        if schedule_frequency is not None:
            self._values["schedule_frequency"] = schedule_frequency
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
    def job_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#job_type Macie2ClassificationJob#job_type}.'''
        result = self._values.get("job_type")
        assert result is not None, "Required property 'job_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_job_definition(self) -> "Macie2ClassificationJobS3JobDefinition":
        '''s3_job_definition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#s3_job_definition Macie2ClassificationJob#s3_job_definition}
        '''
        result = self._values.get("s3_job_definition")
        assert result is not None, "Required property 's3_job_definition' is missing"
        return typing.cast("Macie2ClassificationJobS3JobDefinition", result)

    @builtins.property
    def custom_data_identifier_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#custom_data_identifier_ids Macie2ClassificationJob#custom_data_identifier_ids}.'''
        result = self._values.get("custom_data_identifier_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#description Macie2ClassificationJob#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#id Macie2ClassificationJob#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_run(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#initial_run Macie2ClassificationJob#initial_run}.'''
        result = self._values.get("initial_run")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def job_status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#job_status Macie2ClassificationJob#job_status}.'''
        result = self._values.get("job_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#name Macie2ClassificationJob#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#name_prefix Macie2ClassificationJob#name_prefix}.'''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sampling_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#sampling_percentage Macie2ClassificationJob#sampling_percentage}.'''
        result = self._values.get("sampling_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def schedule_frequency(
        self,
    ) -> typing.Optional["Macie2ClassificationJobScheduleFrequency"]:
        '''schedule_frequency block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#schedule_frequency Macie2ClassificationJob#schedule_frequency}
        '''
        result = self._values.get("schedule_frequency")
        return typing.cast(typing.Optional["Macie2ClassificationJobScheduleFrequency"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tags Macie2ClassificationJob#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tags_all Macie2ClassificationJob#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_criteria": "bucketCriteria",
        "bucket_definitions": "bucketDefinitions",
        "scoping": "scoping",
    },
)
class Macie2ClassificationJobS3JobDefinition:
    def __init__(
        self,
        *,
        bucket_criteria: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteria", typing.Dict[str, typing.Any]]] = None,
        bucket_definitions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketDefinitions", typing.Dict[str, typing.Any]]]]] = None,
        scoping: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScoping", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_criteria: bucket_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#bucket_criteria Macie2ClassificationJob#bucket_criteria}
        :param bucket_definitions: bucket_definitions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#bucket_definitions Macie2ClassificationJob#bucket_definitions}
        :param scoping: scoping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#scoping Macie2ClassificationJob#scoping}
        '''
        if isinstance(bucket_criteria, dict):
            bucket_criteria = Macie2ClassificationJobS3JobDefinitionBucketCriteria(**bucket_criteria)
        if isinstance(scoping, dict):
            scoping = Macie2ClassificationJobS3JobDefinitionScoping(**scoping)
        if __debug__:
            def stub(
                *,
                bucket_criteria: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteria, typing.Dict[str, typing.Any]]] = None,
                bucket_definitions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketDefinitions, typing.Dict[str, typing.Any]]]]] = None,
                scoping: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScoping, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_criteria", value=bucket_criteria, expected_type=type_hints["bucket_criteria"])
            check_type(argname="argument bucket_definitions", value=bucket_definitions, expected_type=type_hints["bucket_definitions"])
            check_type(argname="argument scoping", value=scoping, expected_type=type_hints["scoping"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_criteria is not None:
            self._values["bucket_criteria"] = bucket_criteria
        if bucket_definitions is not None:
            self._values["bucket_definitions"] = bucket_definitions
        if scoping is not None:
            self._values["scoping"] = scoping

    @builtins.property
    def bucket_criteria(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteria"]:
        '''bucket_criteria block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#bucket_criteria Macie2ClassificationJob#bucket_criteria}
        '''
        result = self._values.get("bucket_criteria")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteria"], result)

    @builtins.property
    def bucket_definitions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketDefinitions"]]]:
        '''bucket_definitions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#bucket_definitions Macie2ClassificationJob#bucket_definitions}
        '''
        result = self._values.get("bucket_definitions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketDefinitions"]]], result)

    @builtins.property
    def scoping(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScoping"]:
        '''scoping block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#scoping Macie2ClassificationJob#scoping}
        '''
        result = self._values.get("scoping")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScoping"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteria",
    jsii_struct_bases=[],
    name_mapping={"excludes": "excludes", "includes": "includes"},
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteria:
    def __init__(
        self,
        *,
        excludes: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes", typing.Dict[str, typing.Any]]] = None,
        includes: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param excludes: excludes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#excludes Macie2ClassificationJob#excludes}
        :param includes: includes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#includes Macie2ClassificationJob#includes}
        '''
        if isinstance(excludes, dict):
            excludes = Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes(**excludes)
        if isinstance(includes, dict):
            includes = Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes(**includes)
        if __debug__:
            def stub(
                *,
                excludes: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes, typing.Dict[str, typing.Any]]] = None,
                includes: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument excludes", value=excludes, expected_type=type_hints["excludes"])
            check_type(argname="argument includes", value=includes, expected_type=type_hints["includes"])
        self._values: typing.Dict[str, typing.Any] = {}
        if excludes is not None:
            self._values["excludes"] = excludes
        if includes is not None:
            self._values["includes"] = includes

    @builtins.property
    def excludes(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes"]:
        '''excludes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#excludes Macie2ClassificationJob#excludes}
        '''
        result = self._values.get("excludes")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes"], result)

    @builtins.property
    def includes(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes"]:
        '''includes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#includes Macie2ClassificationJob#includes}
        '''
        result = self._values.get("includes")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteria(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes",
    jsii_struct_bases=[],
    name_mapping={"and_": "and"},
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes:
    def __init__(
        self,
        *,
        and_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        if __debug__:
            def stub(
                *,
                and_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument and_", value=and_, expected_type=type_hints["and_"])
        self._values: typing.Dict[str, typing.Any] = {}
        if and_ is not None:
            self._values["and_"] = and_

    @builtins.property
    def and_(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd"]]]:
        '''and block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        result = self._values.get("and_")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd",
    jsii_struct_bases=[],
    name_mapping={
        "simple_criterion": "simpleCriterion",
        "tag_criterion": "tagCriterion",
    },
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd:
    def __init__(
        self,
        *,
        simple_criterion: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion", typing.Dict[str, typing.Any]]] = None,
        tag_criterion: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param simple_criterion: simple_criterion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#simple_criterion Macie2ClassificationJob#simple_criterion}
        :param tag_criterion: tag_criterion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_criterion Macie2ClassificationJob#tag_criterion}
        '''
        if isinstance(simple_criterion, dict):
            simple_criterion = Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion(**simple_criterion)
        if isinstance(tag_criterion, dict):
            tag_criterion = Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion(**tag_criterion)
        if __debug__:
            def stub(
                *,
                simple_criterion: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion, typing.Dict[str, typing.Any]]] = None,
                tag_criterion: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument simple_criterion", value=simple_criterion, expected_type=type_hints["simple_criterion"])
            check_type(argname="argument tag_criterion", value=tag_criterion, expected_type=type_hints["tag_criterion"])
        self._values: typing.Dict[str, typing.Any] = {}
        if simple_criterion is not None:
            self._values["simple_criterion"] = simple_criterion
        if tag_criterion is not None:
            self._values["tag_criterion"] = tag_criterion

    @builtins.property
    def simple_criterion(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion"]:
        '''simple_criterion block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#simple_criterion Macie2ClassificationJob#simple_criterion}
        '''
        result = self._values.get("simple_criterion")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion"], result)

    @builtins.property
    def tag_criterion(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion"]:
        '''tag_criterion block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_criterion Macie2ClassificationJob#tag_criterion}
        '''
        result = self._values.get("tag_criterion")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndList",
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
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndOutputReference",
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

    @jsii.member(jsii_name="putSimpleCriterion")
    def put_simple_criterion(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.
        '''
        value = Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion(
            comparator=comparator, key=key, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putSimpleCriterion", [value]))

    @jsii.member(jsii_name="putTagCriterion")
    def put_tag_criterion(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        tag_values: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param tag_values: tag_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        '''
        value = Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion(
            comparator=comparator, tag_values=tag_values
        )

        return typing.cast(None, jsii.invoke(self, "putTagCriterion", [value]))

    @jsii.member(jsii_name="resetSimpleCriterion")
    def reset_simple_criterion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSimpleCriterion", []))

    @jsii.member(jsii_name="resetTagCriterion")
    def reset_tag_criterion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagCriterion", []))

    @builtins.property
    @jsii.member(jsii_name="simpleCriterion")
    def simple_criterion(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterionOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterionOutputReference", jsii.get(self, "simpleCriterion"))

    @builtins.property
    @jsii.member(jsii_name="tagCriterion")
    def tag_criterion(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionOutputReference", jsii.get(self, "tagCriterion"))

    @builtins.property
    @jsii.member(jsii_name="simpleCriterionInput")
    def simple_criterion_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion"], jsii.get(self, "simpleCriterionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagCriterionInput")
    def tag_criterion_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion"], jsii.get(self, "tagCriterionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion",
    jsii_struct_bases=[],
    name_mapping={"comparator": "comparator", "key": "key", "values": "values"},
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion:
    def __init__(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.
        '''
        if __debug__:
            def stub(
                *,
                comparator: typing.Optional[builtins.str] = None,
                key: typing.Optional[builtins.str] = None,
                values: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument comparator", value=comparator, expected_type=type_hints["comparator"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if comparator is not None:
            self._values["comparator"] = comparator
        if key is not None:
            self._values["key"] = key
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def comparator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.'''
        result = self._values.get("comparator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterionOutputReference",
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

    @jsii.member(jsii_name="resetComparator")
    def reset_comparator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComparator", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="comparatorInput")
    def comparator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparatorInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="comparator")
    def comparator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparator"))

    @comparator.setter
    def comparator(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparator", value)

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
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion",
    jsii_struct_bases=[],
    name_mapping={"comparator": "comparator", "tag_values": "tagValues"},
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion:
    def __init__(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        tag_values: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param tag_values: tag_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        '''
        if __debug__:
            def stub(
                *,
                comparator: typing.Optional[builtins.str] = None,
                tag_values: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument comparator", value=comparator, expected_type=type_hints["comparator"])
            check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if comparator is not None:
            self._values["comparator"] = comparator
        if tag_values is not None:
            self._values["tag_values"] = tag_values

    @builtins.property
    def comparator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.'''
        result = self._values.get("comparator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_values(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues"]]]:
        '''tag_values block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        '''
        result = self._values.get("tag_values")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionOutputReference",
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

    @jsii.member(jsii_name="putTagValues")
    def put_tag_values(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTagValues", [value]))

    @jsii.member(jsii_name="resetComparator")
    def reset_comparator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComparator", []))

    @jsii.member(jsii_name="resetTagValues")
    def reset_tag_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagValues", []))

    @builtins.property
    @jsii.member(jsii_name="tagValues")
    def tag_values(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesList":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesList", jsii.get(self, "tagValues"))

    @builtins.property
    @jsii.member(jsii_name="comparatorInput")
    def comparator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparatorInput"))

    @builtins.property
    @jsii.member(jsii_name="tagValuesInput")
    def tag_values_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues"]]], jsii.get(self, "tagValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="comparator")
    def comparator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparator"))

    @comparator.setter
    def comparator(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#value Macie2ClassificationJob#value}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                value: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#value Macie2ClassificationJob#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesList",
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
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesOutputReference",
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

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

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
    ) -> typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesOutputReference",
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

    @jsii.member(jsii_name="putAnd")
    def put_and(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAnd", [value]))

    @jsii.member(jsii_name="resetAnd")
    def reset_and(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnd", []))

    @builtins.property
    @jsii.member(jsii_name="and")
    def and_(
        self,
    ) -> Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndList:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndList, jsii.get(self, "and"))

    @builtins.property
    @jsii.member(jsii_name="andInput")
    def and_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd]]], jsii.get(self, "andInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes",
    jsii_struct_bases=[],
    name_mapping={"and_": "and"},
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes:
    def __init__(
        self,
        *,
        and_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        if __debug__:
            def stub(
                *,
                and_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument and_", value=and_, expected_type=type_hints["and_"])
        self._values: typing.Dict[str, typing.Any] = {}
        if and_ is not None:
            self._values["and_"] = and_

    @builtins.property
    def and_(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd"]]]:
        '''and block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        result = self._values.get("and_")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd",
    jsii_struct_bases=[],
    name_mapping={
        "simple_criterion": "simpleCriterion",
        "tag_criterion": "tagCriterion",
    },
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd:
    def __init__(
        self,
        *,
        simple_criterion: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion", typing.Dict[str, typing.Any]]] = None,
        tag_criterion: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param simple_criterion: simple_criterion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#simple_criterion Macie2ClassificationJob#simple_criterion}
        :param tag_criterion: tag_criterion block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_criterion Macie2ClassificationJob#tag_criterion}
        '''
        if isinstance(simple_criterion, dict):
            simple_criterion = Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion(**simple_criterion)
        if isinstance(tag_criterion, dict):
            tag_criterion = Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion(**tag_criterion)
        if __debug__:
            def stub(
                *,
                simple_criterion: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion, typing.Dict[str, typing.Any]]] = None,
                tag_criterion: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument simple_criterion", value=simple_criterion, expected_type=type_hints["simple_criterion"])
            check_type(argname="argument tag_criterion", value=tag_criterion, expected_type=type_hints["tag_criterion"])
        self._values: typing.Dict[str, typing.Any] = {}
        if simple_criterion is not None:
            self._values["simple_criterion"] = simple_criterion
        if tag_criterion is not None:
            self._values["tag_criterion"] = tag_criterion

    @builtins.property
    def simple_criterion(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion"]:
        '''simple_criterion block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#simple_criterion Macie2ClassificationJob#simple_criterion}
        '''
        result = self._values.get("simple_criterion")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion"], result)

    @builtins.property
    def tag_criterion(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion"]:
        '''tag_criterion block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_criterion Macie2ClassificationJob#tag_criterion}
        '''
        result = self._values.get("tag_criterion")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndList",
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
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndOutputReference",
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

    @jsii.member(jsii_name="putSimpleCriterion")
    def put_simple_criterion(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.
        '''
        value = Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion(
            comparator=comparator, key=key, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putSimpleCriterion", [value]))

    @jsii.member(jsii_name="putTagCriterion")
    def put_tag_criterion(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        tag_values: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param tag_values: tag_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        '''
        value = Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion(
            comparator=comparator, tag_values=tag_values
        )

        return typing.cast(None, jsii.invoke(self, "putTagCriterion", [value]))

    @jsii.member(jsii_name="resetSimpleCriterion")
    def reset_simple_criterion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSimpleCriterion", []))

    @jsii.member(jsii_name="resetTagCriterion")
    def reset_tag_criterion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagCriterion", []))

    @builtins.property
    @jsii.member(jsii_name="simpleCriterion")
    def simple_criterion(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterionOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterionOutputReference", jsii.get(self, "simpleCriterion"))

    @builtins.property
    @jsii.member(jsii_name="tagCriterion")
    def tag_criterion(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionOutputReference", jsii.get(self, "tagCriterion"))

    @builtins.property
    @jsii.member(jsii_name="simpleCriterionInput")
    def simple_criterion_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion"], jsii.get(self, "simpleCriterionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagCriterionInput")
    def tag_criterion_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion"], jsii.get(self, "tagCriterionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion",
    jsii_struct_bases=[],
    name_mapping={"comparator": "comparator", "key": "key", "values": "values"},
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion:
    def __init__(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.
        '''
        if __debug__:
            def stub(
                *,
                comparator: typing.Optional[builtins.str] = None,
                key: typing.Optional[builtins.str] = None,
                values: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument comparator", value=comparator, expected_type=type_hints["comparator"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if comparator is not None:
            self._values["comparator"] = comparator
        if key is not None:
            self._values["key"] = key
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def comparator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.'''
        result = self._values.get("comparator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterionOutputReference",
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

    @jsii.member(jsii_name="resetComparator")
    def reset_comparator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComparator", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="comparatorInput")
    def comparator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparatorInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="comparator")
    def comparator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparator"))

    @comparator.setter
    def comparator(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparator", value)

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
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion",
    jsii_struct_bases=[],
    name_mapping={"comparator": "comparator", "tag_values": "tagValues"},
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion:
    def __init__(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        tag_values: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param tag_values: tag_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        '''
        if __debug__:
            def stub(
                *,
                comparator: typing.Optional[builtins.str] = None,
                tag_values: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument comparator", value=comparator, expected_type=type_hints["comparator"])
            check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if comparator is not None:
            self._values["comparator"] = comparator
        if tag_values is not None:
            self._values["tag_values"] = tag_values

    @builtins.property
    def comparator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.'''
        result = self._values.get("comparator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_values(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues"]]]:
        '''tag_values block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        '''
        result = self._values.get("tag_values")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionOutputReference",
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

    @jsii.member(jsii_name="putTagValues")
    def put_tag_values(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTagValues", [value]))

    @jsii.member(jsii_name="resetComparator")
    def reset_comparator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComparator", []))

    @jsii.member(jsii_name="resetTagValues")
    def reset_tag_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagValues", []))

    @builtins.property
    @jsii.member(jsii_name="tagValues")
    def tag_values(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesList":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesList", jsii.get(self, "tagValues"))

    @builtins.property
    @jsii.member(jsii_name="comparatorInput")
    def comparator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparatorInput"))

    @builtins.property
    @jsii.member(jsii_name="tagValuesInput")
    def tag_values_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues"]]], jsii.get(self, "tagValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="comparator")
    def comparator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparator"))

    @comparator.setter
    def comparator(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#value Macie2ClassificationJob#value}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                value: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#value Macie2ClassificationJob#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesList",
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
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesOutputReference",
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

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

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
    ) -> typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesOutputReference",
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

    @jsii.member(jsii_name="putAnd")
    def put_and(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAnd", [value]))

    @jsii.member(jsii_name="resetAnd")
    def reset_and(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnd", []))

    @builtins.property
    @jsii.member(jsii_name="and")
    def and_(
        self,
    ) -> Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndList:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndList, jsii.get(self, "and"))

    @builtins.property
    @jsii.member(jsii_name="andInput")
    def and_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd]]], jsii.get(self, "andInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionBucketCriteriaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketCriteriaOutputReference",
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

    @jsii.member(jsii_name="putExcludes")
    def put_excludes(
        self,
        *,
        and_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        value = Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes(and_=and_)

        return typing.cast(None, jsii.invoke(self, "putExcludes", [value]))

    @jsii.member(jsii_name="putIncludes")
    def put_includes(
        self,
        *,
        and_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        value = Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes(and_=and_)

        return typing.cast(None, jsii.invoke(self, "putIncludes", [value]))

    @jsii.member(jsii_name="resetExcludes")
    def reset_excludes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludes", []))

    @jsii.member(jsii_name="resetIncludes")
    def reset_includes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludes", []))

    @builtins.property
    @jsii.member(jsii_name="excludes")
    def excludes(
        self,
    ) -> Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesOutputReference:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesOutputReference, jsii.get(self, "excludes"))

    @builtins.property
    @jsii.member(jsii_name="includes")
    def includes(
        self,
    ) -> Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesOutputReference:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesOutputReference, jsii.get(self, "includes"))

    @builtins.property
    @jsii.member(jsii_name="excludesInput")
    def excludes_input(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes], jsii.get(self, "excludesInput"))

    @builtins.property
    @jsii.member(jsii_name="includesInput")
    def includes_input(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes], jsii.get(self, "includesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteria]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteria], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteria],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteria],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketDefinitions",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId", "buckets": "buckets"},
)
class Macie2ClassificationJobS3JobDefinitionBucketDefinitions:
    def __init__(
        self,
        *,
        account_id: builtins.str,
        buckets: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#account_id Macie2ClassificationJob#account_id}.
        :param buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#buckets Macie2ClassificationJob#buckets}.
        '''
        if __debug__:
            def stub(
                *,
                account_id: builtins.str,
                buckets: typing.Sequence[builtins.str],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument buckets", value=buckets, expected_type=type_hints["buckets"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_id": account_id,
            "buckets": buckets,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#account_id Macie2ClassificationJob#account_id}.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def buckets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#buckets Macie2ClassificationJob#buckets}.'''
        result = self._values.get("buckets")
        assert result is not None, "Required property 'buckets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionBucketDefinitions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionBucketDefinitionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketDefinitionsList",
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
    ) -> "Macie2ClassificationJobS3JobDefinitionBucketDefinitionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobS3JobDefinitionBucketDefinitionsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketDefinitions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketDefinitions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketDefinitions]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketDefinitions]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionBucketDefinitionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionBucketDefinitionsOutputReference",
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
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketsInput")
    def buckets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "bucketsInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="buckets")
    def buckets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "buckets"))

    @buckets.setter
    def buckets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buckets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketDefinitions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketDefinitions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketDefinitions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketDefinitions, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionOutputReference",
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

    @jsii.member(jsii_name="putBucketCriteria")
    def put_bucket_criteria(
        self,
        *,
        excludes: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes, typing.Dict[str, typing.Any]]] = None,
        includes: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param excludes: excludes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#excludes Macie2ClassificationJob#excludes}
        :param includes: includes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#includes Macie2ClassificationJob#includes}
        '''
        value = Macie2ClassificationJobS3JobDefinitionBucketCriteria(
            excludes=excludes, includes=includes
        )

        return typing.cast(None, jsii.invoke(self, "putBucketCriteria", [value]))

    @jsii.member(jsii_name="putBucketDefinitions")
    def put_bucket_definitions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketDefinitions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionBucketDefinitions, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBucketDefinitions", [value]))

    @jsii.member(jsii_name="putScoping")
    def put_scoping(
        self,
        *,
        excludes: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingExcludes", typing.Dict[str, typing.Any]]] = None,
        includes: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingIncludes", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param excludes: excludes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#excludes Macie2ClassificationJob#excludes}
        :param includes: includes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#includes Macie2ClassificationJob#includes}
        '''
        value = Macie2ClassificationJobS3JobDefinitionScoping(
            excludes=excludes, includes=includes
        )

        return typing.cast(None, jsii.invoke(self, "putScoping", [value]))

    @jsii.member(jsii_name="resetBucketCriteria")
    def reset_bucket_criteria(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketCriteria", []))

    @jsii.member(jsii_name="resetBucketDefinitions")
    def reset_bucket_definitions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketDefinitions", []))

    @jsii.member(jsii_name="resetScoping")
    def reset_scoping(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScoping", []))

    @builtins.property
    @jsii.member(jsii_name="bucketCriteria")
    def bucket_criteria(
        self,
    ) -> Macie2ClassificationJobS3JobDefinitionBucketCriteriaOutputReference:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionBucketCriteriaOutputReference, jsii.get(self, "bucketCriteria"))

    @builtins.property
    @jsii.member(jsii_name="bucketDefinitions")
    def bucket_definitions(
        self,
    ) -> Macie2ClassificationJobS3JobDefinitionBucketDefinitionsList:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionBucketDefinitionsList, jsii.get(self, "bucketDefinitions"))

    @builtins.property
    @jsii.member(jsii_name="scoping")
    def scoping(self) -> "Macie2ClassificationJobS3JobDefinitionScopingOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingOutputReference", jsii.get(self, "scoping"))

    @builtins.property
    @jsii.member(jsii_name="bucketCriteriaInput")
    def bucket_criteria_input(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteria]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionBucketCriteria], jsii.get(self, "bucketCriteriaInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketDefinitionsInput")
    def bucket_definitions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketDefinitions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionBucketDefinitions]]], jsii.get(self, "bucketDefinitionsInput"))

    @builtins.property
    @jsii.member(jsii_name="scopingInput")
    def scoping_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScoping"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScoping"], jsii.get(self, "scopingInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Macie2ClassificationJobS3JobDefinition]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinition],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Macie2ClassificationJobS3JobDefinition],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScoping",
    jsii_struct_bases=[],
    name_mapping={"excludes": "excludes", "includes": "includes"},
)
class Macie2ClassificationJobS3JobDefinitionScoping:
    def __init__(
        self,
        *,
        excludes: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingExcludes", typing.Dict[str, typing.Any]]] = None,
        includes: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingIncludes", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param excludes: excludes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#excludes Macie2ClassificationJob#excludes}
        :param includes: includes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#includes Macie2ClassificationJob#includes}
        '''
        if isinstance(excludes, dict):
            excludes = Macie2ClassificationJobS3JobDefinitionScopingExcludes(**excludes)
        if isinstance(includes, dict):
            includes = Macie2ClassificationJobS3JobDefinitionScopingIncludes(**includes)
        if __debug__:
            def stub(
                *,
                excludes: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludes, typing.Dict[str, typing.Any]]] = None,
                includes: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludes, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument excludes", value=excludes, expected_type=type_hints["excludes"])
            check_type(argname="argument includes", value=includes, expected_type=type_hints["includes"])
        self._values: typing.Dict[str, typing.Any] = {}
        if excludes is not None:
            self._values["excludes"] = excludes
        if includes is not None:
            self._values["includes"] = includes

    @builtins.property
    def excludes(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludes"]:
        '''excludes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#excludes Macie2ClassificationJob#excludes}
        '''
        result = self._values.get("excludes")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludes"], result)

    @builtins.property
    def includes(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludes"]:
        '''includes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#includes Macie2ClassificationJob#includes}
        '''
        result = self._values.get("includes")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludes"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScoping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludes",
    jsii_struct_bases=[],
    name_mapping={"and_": "and"},
)
class Macie2ClassificationJobS3JobDefinitionScopingExcludes:
    def __init__(
        self,
        *,
        and_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        if __debug__:
            def stub(
                *,
                and_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument and_", value=and_, expected_type=type_hints["and_"])
        self._values: typing.Dict[str, typing.Any] = {}
        if and_ is not None:
            self._values["and_"] = and_

    @builtins.property
    def and_(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd"]]]:
        '''and block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        result = self._values.get("and_")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingExcludes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd",
    jsii_struct_bases=[],
    name_mapping={
        "simple_scope_term": "simpleScopeTerm",
        "tag_scope_term": "tagScopeTerm",
    },
)
class Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd:
    def __init__(
        self,
        *,
        simple_scope_term: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm", typing.Dict[str, typing.Any]]] = None,
        tag_scope_term: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param simple_scope_term: simple_scope_term block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#simple_scope_term Macie2ClassificationJob#simple_scope_term}
        :param tag_scope_term: tag_scope_term block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_scope_term Macie2ClassificationJob#tag_scope_term}
        '''
        if isinstance(simple_scope_term, dict):
            simple_scope_term = Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm(**simple_scope_term)
        if isinstance(tag_scope_term, dict):
            tag_scope_term = Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm(**tag_scope_term)
        if __debug__:
            def stub(
                *,
                simple_scope_term: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm, typing.Dict[str, typing.Any]]] = None,
                tag_scope_term: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument simple_scope_term", value=simple_scope_term, expected_type=type_hints["simple_scope_term"])
            check_type(argname="argument tag_scope_term", value=tag_scope_term, expected_type=type_hints["tag_scope_term"])
        self._values: typing.Dict[str, typing.Any] = {}
        if simple_scope_term is not None:
            self._values["simple_scope_term"] = simple_scope_term
        if tag_scope_term is not None:
            self._values["tag_scope_term"] = tag_scope_term

    @builtins.property
    def simple_scope_term(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm"]:
        '''simple_scope_term block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#simple_scope_term Macie2ClassificationJob#simple_scope_term}
        '''
        result = self._values.get("simple_scope_term")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm"], result)

    @builtins.property
    def tag_scope_term(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm"]:
        '''tag_scope_term block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_scope_term Macie2ClassificationJob#tag_scope_term}
        '''
        result = self._values.get("tag_scope_term")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionScopingExcludesAndList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAndList",
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
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingExcludesAndOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionScopingExcludesAndOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAndOutputReference",
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

    @jsii.member(jsii_name="putSimpleScopeTerm")
    def put_simple_scope_term(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.
        '''
        value = Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm(
            comparator=comparator, key=key, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putSimpleScopeTerm", [value]))

    @jsii.member(jsii_name="putTagScopeTerm")
    def put_tag_scope_term(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        tag_values: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues", typing.Dict[str, typing.Any]]]]] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param tag_values: tag_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#target Macie2ClassificationJob#target}.
        '''
        value = Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm(
            comparator=comparator, key=key, tag_values=tag_values, target=target
        )

        return typing.cast(None, jsii.invoke(self, "putTagScopeTerm", [value]))

    @jsii.member(jsii_name="resetSimpleScopeTerm")
    def reset_simple_scope_term(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSimpleScopeTerm", []))

    @jsii.member(jsii_name="resetTagScopeTerm")
    def reset_tag_scope_term(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagScopeTerm", []))

    @builtins.property
    @jsii.member(jsii_name="simpleScopeTerm")
    def simple_scope_term(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTermOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTermOutputReference", jsii.get(self, "simpleScopeTerm"))

    @builtins.property
    @jsii.member(jsii_name="tagScopeTerm")
    def tag_scope_term(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermOutputReference", jsii.get(self, "tagScopeTerm"))

    @builtins.property
    @jsii.member(jsii_name="simpleScopeTermInput")
    def simple_scope_term_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm"], jsii.get(self, "simpleScopeTermInput"))

    @builtins.property
    @jsii.member(jsii_name="tagScopeTermInput")
    def tag_scope_term_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm"], jsii.get(self, "tagScopeTermInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm",
    jsii_struct_bases=[],
    name_mapping={"comparator": "comparator", "key": "key", "values": "values"},
)
class Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm:
    def __init__(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.
        '''
        if __debug__:
            def stub(
                *,
                comparator: typing.Optional[builtins.str] = None,
                key: typing.Optional[builtins.str] = None,
                values: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument comparator", value=comparator, expected_type=type_hints["comparator"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if comparator is not None:
            self._values["comparator"] = comparator
        if key is not None:
            self._values["key"] = key
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def comparator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.'''
        result = self._values.get("comparator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTermOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTermOutputReference",
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

    @jsii.member(jsii_name="resetComparator")
    def reset_comparator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComparator", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="comparatorInput")
    def comparator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparatorInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="comparator")
    def comparator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparator"))

    @comparator.setter
    def comparator(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparator", value)

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
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm",
    jsii_struct_bases=[],
    name_mapping={
        "comparator": "comparator",
        "key": "key",
        "tag_values": "tagValues",
        "target": "target",
    },
)
class Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm:
    def __init__(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        tag_values: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues", typing.Dict[str, typing.Any]]]]] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param tag_values: tag_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#target Macie2ClassificationJob#target}.
        '''
        if __debug__:
            def stub(
                *,
                comparator: typing.Optional[builtins.str] = None,
                key: typing.Optional[builtins.str] = None,
                tag_values: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues, typing.Dict[str, typing.Any]]]]] = None,
                target: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument comparator", value=comparator, expected_type=type_hints["comparator"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[str, typing.Any] = {}
        if comparator is not None:
            self._values["comparator"] = comparator
        if key is not None:
            self._values["key"] = key
        if tag_values is not None:
            self._values["tag_values"] = tag_values
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def comparator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.'''
        result = self._values.get("comparator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_values(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues"]]]:
        '''tag_values block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        '''
        result = self._values.get("tag_values")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues"]]], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#target Macie2ClassificationJob#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermOutputReference",
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

    @jsii.member(jsii_name="putTagValues")
    def put_tag_values(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTagValues", [value]))

    @jsii.member(jsii_name="resetComparator")
    def reset_comparator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComparator", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetTagValues")
    def reset_tag_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagValues", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="tagValues")
    def tag_values(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesList":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesList", jsii.get(self, "tagValues"))

    @builtins.property
    @jsii.member(jsii_name="comparatorInput")
    def comparator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparatorInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagValuesInput")
    def tag_values_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues"]]], jsii.get(self, "tagValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="comparator")
    def comparator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparator"))

    @comparator.setter
    def comparator(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparator", value)

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#value Macie2ClassificationJob#value}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                value: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#value Macie2ClassificationJob#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesList",
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
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesOutputReference",
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

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

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
    ) -> typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionScopingExcludesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingExcludesOutputReference",
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

    @jsii.member(jsii_name="putAnd")
    def put_and(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAnd", [value]))

    @jsii.member(jsii_name="resetAnd")
    def reset_and(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnd", []))

    @builtins.property
    @jsii.member(jsii_name="and")
    def and_(self) -> Macie2ClassificationJobS3JobDefinitionScopingExcludesAndList:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionScopingExcludesAndList, jsii.get(self, "and"))

    @builtins.property
    @jsii.member(jsii_name="andInput")
    def and_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd]]], jsii.get(self, "andInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludes]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludes],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludes],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludes",
    jsii_struct_bases=[],
    name_mapping={"and_": "and"},
)
class Macie2ClassificationJobS3JobDefinitionScopingIncludes:
    def __init__(
        self,
        *,
        and_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        if __debug__:
            def stub(
                *,
                and_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument and_", value=and_, expected_type=type_hints["and_"])
        self._values: typing.Dict[str, typing.Any] = {}
        if and_ is not None:
            self._values["and_"] = and_

    @builtins.property
    def and_(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd"]]]:
        '''and block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        result = self._values.get("and_")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingIncludes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd",
    jsii_struct_bases=[],
    name_mapping={
        "simple_scope_term": "simpleScopeTerm",
        "tag_scope_term": "tagScopeTerm",
    },
)
class Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd:
    def __init__(
        self,
        *,
        simple_scope_term: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm", typing.Dict[str, typing.Any]]] = None,
        tag_scope_term: typing.Optional[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param simple_scope_term: simple_scope_term block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#simple_scope_term Macie2ClassificationJob#simple_scope_term}
        :param tag_scope_term: tag_scope_term block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_scope_term Macie2ClassificationJob#tag_scope_term}
        '''
        if isinstance(simple_scope_term, dict):
            simple_scope_term = Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm(**simple_scope_term)
        if isinstance(tag_scope_term, dict):
            tag_scope_term = Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm(**tag_scope_term)
        if __debug__:
            def stub(
                *,
                simple_scope_term: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm, typing.Dict[str, typing.Any]]] = None,
                tag_scope_term: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument simple_scope_term", value=simple_scope_term, expected_type=type_hints["simple_scope_term"])
            check_type(argname="argument tag_scope_term", value=tag_scope_term, expected_type=type_hints["tag_scope_term"])
        self._values: typing.Dict[str, typing.Any] = {}
        if simple_scope_term is not None:
            self._values["simple_scope_term"] = simple_scope_term
        if tag_scope_term is not None:
            self._values["tag_scope_term"] = tag_scope_term

    @builtins.property
    def simple_scope_term(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm"]:
        '''simple_scope_term block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#simple_scope_term Macie2ClassificationJob#simple_scope_term}
        '''
        result = self._values.get("simple_scope_term")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm"], result)

    @builtins.property
    def tag_scope_term(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm"]:
        '''tag_scope_term block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_scope_term Macie2ClassificationJob#tag_scope_term}
        '''
        result = self._values.get("tag_scope_term")
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionScopingIncludesAndList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAndList",
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
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingIncludesAndOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionScopingIncludesAndOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAndOutputReference",
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

    @jsii.member(jsii_name="putSimpleScopeTerm")
    def put_simple_scope_term(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.
        '''
        value = Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm(
            comparator=comparator, key=key, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putSimpleScopeTerm", [value]))

    @jsii.member(jsii_name="putTagScopeTerm")
    def put_tag_scope_term(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        tag_values: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues", typing.Dict[str, typing.Any]]]]] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param tag_values: tag_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#target Macie2ClassificationJob#target}.
        '''
        value = Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm(
            comparator=comparator, key=key, tag_values=tag_values, target=target
        )

        return typing.cast(None, jsii.invoke(self, "putTagScopeTerm", [value]))

    @jsii.member(jsii_name="resetSimpleScopeTerm")
    def reset_simple_scope_term(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSimpleScopeTerm", []))

    @jsii.member(jsii_name="resetTagScopeTerm")
    def reset_tag_scope_term(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagScopeTerm", []))

    @builtins.property
    @jsii.member(jsii_name="simpleScopeTerm")
    def simple_scope_term(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTermOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTermOutputReference", jsii.get(self, "simpleScopeTerm"))

    @builtins.property
    @jsii.member(jsii_name="tagScopeTerm")
    def tag_scope_term(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermOutputReference":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermOutputReference", jsii.get(self, "tagScopeTerm"))

    @builtins.property
    @jsii.member(jsii_name="simpleScopeTermInput")
    def simple_scope_term_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm"], jsii.get(self, "simpleScopeTermInput"))

    @builtins.property
    @jsii.member(jsii_name="tagScopeTermInput")
    def tag_scope_term_input(
        self,
    ) -> typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm"]:
        return typing.cast(typing.Optional["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm"], jsii.get(self, "tagScopeTermInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm",
    jsii_struct_bases=[],
    name_mapping={"comparator": "comparator", "key": "key", "values": "values"},
)
class Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm:
    def __init__(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.
        '''
        if __debug__:
            def stub(
                *,
                comparator: typing.Optional[builtins.str] = None,
                key: typing.Optional[builtins.str] = None,
                values: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument comparator", value=comparator, expected_type=type_hints["comparator"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if comparator is not None:
            self._values["comparator"] = comparator
        if key is not None:
            self._values["key"] = key
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def comparator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.'''
        result = self._values.get("comparator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#values Macie2ClassificationJob#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTermOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTermOutputReference",
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

    @jsii.member(jsii_name="resetComparator")
    def reset_comparator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComparator", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="comparatorInput")
    def comparator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparatorInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="comparator")
    def comparator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparator"))

    @comparator.setter
    def comparator(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparator", value)

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
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm",
    jsii_struct_bases=[],
    name_mapping={
        "comparator": "comparator",
        "key": "key",
        "tag_values": "tagValues",
        "target": "target",
    },
)
class Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm:
    def __init__(
        self,
        *,
        comparator: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        tag_values: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues", typing.Dict[str, typing.Any]]]]] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param comparator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param tag_values: tag_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#target Macie2ClassificationJob#target}.
        '''
        if __debug__:
            def stub(
                *,
                comparator: typing.Optional[builtins.str] = None,
                key: typing.Optional[builtins.str] = None,
                tag_values: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues, typing.Dict[str, typing.Any]]]]] = None,
                target: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument comparator", value=comparator, expected_type=type_hints["comparator"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[str, typing.Any] = {}
        if comparator is not None:
            self._values["comparator"] = comparator
        if key is not None:
            self._values["key"] = key
        if tag_values is not None:
            self._values["tag_values"] = tag_values
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def comparator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#comparator Macie2ClassificationJob#comparator}.'''
        result = self._values.get("comparator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_values(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues"]]]:
        '''tag_values block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#tag_values Macie2ClassificationJob#tag_values}
        '''
        result = self._values.get("tag_values")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues"]]], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#target Macie2ClassificationJob#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermOutputReference",
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

    @jsii.member(jsii_name="putTagValues")
    def put_tag_values(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTagValues", [value]))

    @jsii.member(jsii_name="resetComparator")
    def reset_comparator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComparator", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetTagValues")
    def reset_tag_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagValues", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="tagValues")
    def tag_values(
        self,
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesList":
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesList", jsii.get(self, "tagValues"))

    @builtins.property
    @jsii.member(jsii_name="comparatorInput")
    def comparator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparatorInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagValuesInput")
    def tag_values_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues"]]], jsii.get(self, "tagValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="comparator")
    def comparator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparator"))

    @comparator.setter
    def comparator(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparator", value)

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#value Macie2ClassificationJob#value}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                value: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#key Macie2ClassificationJob#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#value Macie2ClassificationJob#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesList",
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
    ) -> "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesOutputReference",
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

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

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
    ) -> typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionScopingIncludesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingIncludesOutputReference",
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

    @jsii.member(jsii_name="putAnd")
    def put_and(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAnd", [value]))

    @jsii.member(jsii_name="resetAnd")
    def reset_and(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnd", []))

    @builtins.property
    @jsii.member(jsii_name="and")
    def and_(self) -> Macie2ClassificationJobS3JobDefinitionScopingIncludesAndList:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionScopingIncludesAndList, jsii.get(self, "and"))

    @builtins.property
    @jsii.member(jsii_name="andInput")
    def and_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd]]], jsii.get(self, "andInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludes]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludes],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludes],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Macie2ClassificationJobS3JobDefinitionScopingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobS3JobDefinitionScopingOutputReference",
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

    @jsii.member(jsii_name="putExcludes")
    def put_excludes(
        self,
        *,
        and_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        value = Macie2ClassificationJobS3JobDefinitionScopingExcludes(and_=and_)

        return typing.cast(None, jsii.invoke(self, "putExcludes", [value]))

    @jsii.member(jsii_name="putIncludes")
    def put_includes(
        self,
        *,
        and_: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param and_: and block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#and Macie2ClassificationJob#and}
        '''
        value = Macie2ClassificationJobS3JobDefinitionScopingIncludes(and_=and_)

        return typing.cast(None, jsii.invoke(self, "putIncludes", [value]))

    @jsii.member(jsii_name="resetExcludes")
    def reset_excludes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludes", []))

    @jsii.member(jsii_name="resetIncludes")
    def reset_includes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludes", []))

    @builtins.property
    @jsii.member(jsii_name="excludes")
    def excludes(
        self,
    ) -> Macie2ClassificationJobS3JobDefinitionScopingExcludesOutputReference:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionScopingExcludesOutputReference, jsii.get(self, "excludes"))

    @builtins.property
    @jsii.member(jsii_name="includes")
    def includes(
        self,
    ) -> Macie2ClassificationJobS3JobDefinitionScopingIncludesOutputReference:
        return typing.cast(Macie2ClassificationJobS3JobDefinitionScopingIncludesOutputReference, jsii.get(self, "includes"))

    @builtins.property
    @jsii.member(jsii_name="excludesInput")
    def excludes_input(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludes]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingExcludes], jsii.get(self, "excludesInput"))

    @builtins.property
    @jsii.member(jsii_name="includesInput")
    def includes_input(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludes]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionScopingIncludes], jsii.get(self, "includesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobS3JobDefinitionScoping]:
        return typing.cast(typing.Optional[Macie2ClassificationJobS3JobDefinitionScoping], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScoping],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Macie2ClassificationJobS3JobDefinitionScoping],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobScheduleFrequency",
    jsii_struct_bases=[],
    name_mapping={
        "daily_schedule": "dailySchedule",
        "monthly_schedule": "monthlySchedule",
        "weekly_schedule": "weeklySchedule",
    },
)
class Macie2ClassificationJobScheduleFrequency:
    def __init__(
        self,
        *,
        daily_schedule: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        monthly_schedule: typing.Optional[jsii.Number] = None,
        weekly_schedule: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param daily_schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#daily_schedule Macie2ClassificationJob#daily_schedule}.
        :param monthly_schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#monthly_schedule Macie2ClassificationJob#monthly_schedule}.
        :param weekly_schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#weekly_schedule Macie2ClassificationJob#weekly_schedule}.
        '''
        if __debug__:
            def stub(
                *,
                daily_schedule: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                monthly_schedule: typing.Optional[jsii.Number] = None,
                weekly_schedule: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument daily_schedule", value=daily_schedule, expected_type=type_hints["daily_schedule"])
            check_type(argname="argument monthly_schedule", value=monthly_schedule, expected_type=type_hints["monthly_schedule"])
            check_type(argname="argument weekly_schedule", value=weekly_schedule, expected_type=type_hints["weekly_schedule"])
        self._values: typing.Dict[str, typing.Any] = {}
        if daily_schedule is not None:
            self._values["daily_schedule"] = daily_schedule
        if monthly_schedule is not None:
            self._values["monthly_schedule"] = monthly_schedule
        if weekly_schedule is not None:
            self._values["weekly_schedule"] = weekly_schedule

    @builtins.property
    def daily_schedule(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#daily_schedule Macie2ClassificationJob#daily_schedule}.'''
        result = self._values.get("daily_schedule")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def monthly_schedule(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#monthly_schedule Macie2ClassificationJob#monthly_schedule}.'''
        result = self._values.get("monthly_schedule")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weekly_schedule(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/macie2_classification_job#weekly_schedule Macie2ClassificationJob#weekly_schedule}.'''
        result = self._values.get("weekly_schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobScheduleFrequency(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobScheduleFrequencyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobScheduleFrequencyOutputReference",
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

    @jsii.member(jsii_name="resetDailySchedule")
    def reset_daily_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDailySchedule", []))

    @jsii.member(jsii_name="resetMonthlySchedule")
    def reset_monthly_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonthlySchedule", []))

    @jsii.member(jsii_name="resetWeeklySchedule")
    def reset_weekly_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeeklySchedule", []))

    @builtins.property
    @jsii.member(jsii_name="dailyScheduleInput")
    def daily_schedule_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dailyScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="monthlyScheduleInput")
    def monthly_schedule_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "monthlyScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="weeklyScheduleInput")
    def weekly_schedule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "weeklyScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="dailySchedule")
    def daily_schedule(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dailySchedule"))

    @daily_schedule.setter
    def daily_schedule(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dailySchedule", value)

    @builtins.property
    @jsii.member(jsii_name="monthlySchedule")
    def monthly_schedule(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "monthlySchedule"))

    @monthly_schedule.setter
    def monthly_schedule(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monthlySchedule", value)

    @builtins.property
    @jsii.member(jsii_name="weeklySchedule")
    def weekly_schedule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "weeklySchedule"))

    @weekly_schedule.setter
    def weekly_schedule(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weeklySchedule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobScheduleFrequency]:
        return typing.cast(typing.Optional[Macie2ClassificationJobScheduleFrequency], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobScheduleFrequency],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Macie2ClassificationJobScheduleFrequency],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobUserPausedDetails",
    jsii_struct_bases=[],
    name_mapping={},
)
class Macie2ClassificationJobUserPausedDetails:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Macie2ClassificationJobUserPausedDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Macie2ClassificationJobUserPausedDetailsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobUserPausedDetailsList",
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
    ) -> "Macie2ClassificationJobUserPausedDetailsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Macie2ClassificationJobUserPausedDetailsOutputReference", jsii.invoke(self, "get", [index]))

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


class Macie2ClassificationJobUserPausedDetailsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.macie2ClassificationJob.Macie2ClassificationJobUserPausedDetailsOutputReference",
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
    @jsii.member(jsii_name="jobExpiresAt")
    def job_expires_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobExpiresAt"))

    @builtins.property
    @jsii.member(jsii_name="jobImminentExpirationHealthEventArn")
    def job_imminent_expiration_health_event_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobImminentExpirationHealthEventArn"))

    @builtins.property
    @jsii.member(jsii_name="jobPausedAt")
    def job_paused_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobPausedAt"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[Macie2ClassificationJobUserPausedDetails]:
        return typing.cast(typing.Optional[Macie2ClassificationJobUserPausedDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Macie2ClassificationJobUserPausedDetails],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[Macie2ClassificationJobUserPausedDetails],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Macie2ClassificationJob",
    "Macie2ClassificationJobConfig",
    "Macie2ClassificationJobS3JobDefinition",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteria",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludes",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndList",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterionOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValues",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesList",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValuesOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaExcludesOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludes",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndList",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterionOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValues",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesList",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValuesOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaIncludesOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketCriteriaOutputReference",
    "Macie2ClassificationJobS3JobDefinitionBucketDefinitions",
    "Macie2ClassificationJobS3JobDefinitionBucketDefinitionsList",
    "Macie2ClassificationJobS3JobDefinitionBucketDefinitionsOutputReference",
    "Macie2ClassificationJobS3JobDefinitionOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScoping",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludes",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAnd",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndList",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTermOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValues",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesList",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValuesOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingExcludesOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludes",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAnd",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndList",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTermOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValues",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesList",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValuesOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingIncludesOutputReference",
    "Macie2ClassificationJobS3JobDefinitionScopingOutputReference",
    "Macie2ClassificationJobScheduleFrequency",
    "Macie2ClassificationJobScheduleFrequencyOutputReference",
    "Macie2ClassificationJobUserPausedDetails",
    "Macie2ClassificationJobUserPausedDetailsList",
    "Macie2ClassificationJobUserPausedDetailsOutputReference",
]

publication.publish()
