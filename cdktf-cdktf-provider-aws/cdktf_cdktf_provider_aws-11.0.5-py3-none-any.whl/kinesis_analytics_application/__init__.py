'''
# `aws_kinesis_analytics_application`

Refer to the Terraform Registory for docs: [`aws_kinesis_analytics_application`](https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application).
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


class KinesisAnalyticsApplication(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplication",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application aws_kinesis_analytics_application}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisAnalyticsApplicationCloudwatchLoggingOptions", typing.Dict[str, typing.Any]]] = None,
        code: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        inputs: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputs", typing.Dict[str, typing.Any]]] = None,
        outputs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationOutputs", typing.Dict[str, typing.Any]]]]] = None,
        reference_data_sources: typing.Optional[typing.Union["KinesisAnalyticsApplicationReferenceDataSources", typing.Dict[str, typing.Any]]] = None,
        start_application: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application aws_kinesis_analytics_application} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name KinesisAnalyticsApplication#name}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#cloudwatch_logging_options KinesisAnalyticsApplication#cloudwatch_logging_options}
        :param code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#code KinesisAnalyticsApplication#code}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#description KinesisAnalyticsApplication#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#id KinesisAnalyticsApplication#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inputs: inputs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#inputs KinesisAnalyticsApplication#inputs}
        :param outputs: outputs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#outputs KinesisAnalyticsApplication#outputs}
        :param reference_data_sources: reference_data_sources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#reference_data_sources KinesisAnalyticsApplication#reference_data_sources}
        :param start_application: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#start_application KinesisAnalyticsApplication#start_application}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#tags KinesisAnalyticsApplication#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#tags_all KinesisAnalyticsApplication#tags_all}.
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
                cloudwatch_logging_options: typing.Optional[typing.Union[KinesisAnalyticsApplicationCloudwatchLoggingOptions, typing.Dict[str, typing.Any]]] = None,
                code: typing.Optional[builtins.str] = None,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                inputs: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputs, typing.Dict[str, typing.Any]]] = None,
                outputs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisAnalyticsApplicationOutputs, typing.Dict[str, typing.Any]]]]] = None,
                reference_data_sources: typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSources, typing.Dict[str, typing.Any]]] = None,
                start_application: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
        config = KinesisAnalyticsApplicationConfig(
            name=name,
            cloudwatch_logging_options=cloudwatch_logging_options,
            code=code,
            description=description,
            id=id,
            inputs=inputs,
            outputs=outputs,
            reference_data_sources=reference_data_sources,
            start_application=start_application,
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

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(
        self,
        *,
        log_stream_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param log_stream_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#log_stream_arn KinesisAnalyticsApplication#log_stream_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        value = KinesisAnalyticsApplicationCloudwatchLoggingOptions(
            log_stream_arn=log_stream_arn, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="putInputs")
    def put_inputs(
        self,
        *,
        name_prefix: builtins.str,
        schema: typing.Union["KinesisAnalyticsApplicationInputsSchema", typing.Dict[str, typing.Any]],
        kinesis_firehose: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsKinesisFirehose", typing.Dict[str, typing.Any]]] = None,
        kinesis_stream: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsKinesisStream", typing.Dict[str, typing.Any]]] = None,
        parallelism: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsParallelism", typing.Dict[str, typing.Any]]] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsProcessingConfiguration", typing.Dict[str, typing.Any]]] = None,
        starting_position_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationInputsStartingPositionConfiguration", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name_prefix KinesisAnalyticsApplication#name_prefix}.
        :param schema: schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#schema KinesisAnalyticsApplication#schema}
        :param kinesis_firehose: kinesis_firehose block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_firehose KinesisAnalyticsApplication#kinesis_firehose}
        :param kinesis_stream: kinesis_stream block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_stream KinesisAnalyticsApplication#kinesis_stream}
        :param parallelism: parallelism block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#parallelism KinesisAnalyticsApplication#parallelism}
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#processing_configuration KinesisAnalyticsApplication#processing_configuration}
        :param starting_position_configuration: starting_position_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#starting_position_configuration KinesisAnalyticsApplication#starting_position_configuration}
        '''
        value = KinesisAnalyticsApplicationInputs(
            name_prefix=name_prefix,
            schema=schema,
            kinesis_firehose=kinesis_firehose,
            kinesis_stream=kinesis_stream,
            parallelism=parallelism,
            processing_configuration=processing_configuration,
            starting_position_configuration=starting_position_configuration,
        )

        return typing.cast(None, jsii.invoke(self, "putInputs", [value]))

    @jsii.member(jsii_name="putOutputs")
    def put_outputs(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationOutputs", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisAnalyticsApplicationOutputs, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOutputs", [value]))

    @jsii.member(jsii_name="putReferenceDataSources")
    def put_reference_data_sources(
        self,
        *,
        s3: typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesS3", typing.Dict[str, typing.Any]],
        schema: typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchema", typing.Dict[str, typing.Any]],
        table_name: builtins.str,
    ) -> None:
        '''
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#s3 KinesisAnalyticsApplication#s3}
        :param schema: schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#schema KinesisAnalyticsApplication#schema}
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#table_name KinesisAnalyticsApplication#table_name}.
        '''
        value = KinesisAnalyticsApplicationReferenceDataSources(
            s3=s3, schema=schema, table_name=table_name
        )

        return typing.cast(None, jsii.invoke(self, "putReferenceDataSources", [value]))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetCode")
    def reset_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCode", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInputs")
    def reset_inputs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInputs", []))

    @jsii.member(jsii_name="resetOutputs")
    def reset_outputs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputs", []))

    @jsii.member(jsii_name="resetReferenceDataSources")
    def reset_reference_data_sources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReferenceDataSources", []))

    @jsii.member(jsii_name="resetStartApplication")
    def reset_start_application(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartApplication", []))

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
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> "KinesisAnalyticsApplicationCloudwatchLoggingOptionsOutputReference":
        return typing.cast("KinesisAnalyticsApplicationCloudwatchLoggingOptionsOutputReference", jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="createTimestamp")
    def create_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="inputs")
    def inputs(self) -> "KinesisAnalyticsApplicationInputsOutputReference":
        return typing.cast("KinesisAnalyticsApplicationInputsOutputReference", jsii.get(self, "inputs"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdateTimestamp")
    def last_update_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdateTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="outputs")
    def outputs(self) -> "KinesisAnalyticsApplicationOutputsList":
        return typing.cast("KinesisAnalyticsApplicationOutputsList", jsii.get(self, "outputs"))

    @builtins.property
    @jsii.member(jsii_name="referenceDataSources")
    def reference_data_sources(
        self,
    ) -> "KinesisAnalyticsApplicationReferenceDataSourcesOutputReference":
        return typing.cast("KinesisAnalyticsApplicationReferenceDataSourcesOutputReference", jsii.get(self, "referenceDataSources"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationCloudwatchLoggingOptions"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationCloudwatchLoggingOptions"], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="codeInput")
    def code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codeInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inputsInput")
    def inputs_input(self) -> typing.Optional["KinesisAnalyticsApplicationInputs"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputs"], jsii.get(self, "inputsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="outputsInput")
    def outputs_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisAnalyticsApplicationOutputs"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisAnalyticsApplicationOutputs"]]], jsii.get(self, "outputsInput"))

    @builtins.property
    @jsii.member(jsii_name="referenceDataSourcesInput")
    def reference_data_sources_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationReferenceDataSources"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationReferenceDataSources"], jsii.get(self, "referenceDataSourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="startApplicationInput")
    def start_application_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "startApplicationInput"))

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
    @jsii.member(jsii_name="code")
    def code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "code"))

    @code.setter
    def code(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "code", value)

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
    @jsii.member(jsii_name="startApplication")
    def start_application(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "startApplication"))

    @start_application.setter
    def start_application(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startApplication", value)

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
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={"log_stream_arn": "logStreamArn", "role_arn": "roleArn"},
)
class KinesisAnalyticsApplicationCloudwatchLoggingOptions:
    def __init__(self, *, log_stream_arn: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param log_stream_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#log_stream_arn KinesisAnalyticsApplication#log_stream_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        if __debug__:
            def stub(*, log_stream_arn: builtins.str, role_arn: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument log_stream_arn", value=log_stream_arn, expected_type=type_hints["log_stream_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "log_stream_arn": log_stream_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def log_stream_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#log_stream_arn KinesisAnalyticsApplication#log_stream_arn}.'''
        result = self._values.get("log_stream_arn")
        assert result is not None, "Required property 'log_stream_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationCloudwatchLoggingOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationCloudwatchLoggingOptionsOutputReference",
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
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="logStreamArnInput")
    def log_stream_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamArn")
    def log_stream_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamArn"))

    @log_stream_arn.setter
    def log_stream_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamArn", value)

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
    ) -> typing.Optional[KinesisAnalyticsApplicationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationCloudwatchLoggingOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationConfig",
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
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "code": "code",
        "description": "description",
        "id": "id",
        "inputs": "inputs",
        "outputs": "outputs",
        "reference_data_sources": "referenceDataSources",
        "start_application": "startApplication",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class KinesisAnalyticsApplicationConfig(cdktf.TerraformMetaArguments):
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
        cloudwatch_logging_options: typing.Optional[typing.Union[KinesisAnalyticsApplicationCloudwatchLoggingOptions, typing.Dict[str, typing.Any]]] = None,
        code: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        inputs: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputs", typing.Dict[str, typing.Any]]] = None,
        outputs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationOutputs", typing.Dict[str, typing.Any]]]]] = None,
        reference_data_sources: typing.Optional[typing.Union["KinesisAnalyticsApplicationReferenceDataSources", typing.Dict[str, typing.Any]]] = None,
        start_application: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name KinesisAnalyticsApplication#name}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#cloudwatch_logging_options KinesisAnalyticsApplication#cloudwatch_logging_options}
        :param code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#code KinesisAnalyticsApplication#code}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#description KinesisAnalyticsApplication#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#id KinesisAnalyticsApplication#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inputs: inputs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#inputs KinesisAnalyticsApplication#inputs}
        :param outputs: outputs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#outputs KinesisAnalyticsApplication#outputs}
        :param reference_data_sources: reference_data_sources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#reference_data_sources KinesisAnalyticsApplication#reference_data_sources}
        :param start_application: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#start_application KinesisAnalyticsApplication#start_application}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#tags KinesisAnalyticsApplication#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#tags_all KinesisAnalyticsApplication#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = KinesisAnalyticsApplicationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if isinstance(inputs, dict):
            inputs = KinesisAnalyticsApplicationInputs(**inputs)
        if isinstance(reference_data_sources, dict):
            reference_data_sources = KinesisAnalyticsApplicationReferenceDataSources(**reference_data_sources)
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
                cloudwatch_logging_options: typing.Optional[typing.Union[KinesisAnalyticsApplicationCloudwatchLoggingOptions, typing.Dict[str, typing.Any]]] = None,
                code: typing.Optional[builtins.str] = None,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                inputs: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputs, typing.Dict[str, typing.Any]]] = None,
                outputs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisAnalyticsApplicationOutputs, typing.Dict[str, typing.Any]]]]] = None,
                reference_data_sources: typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSources, typing.Dict[str, typing.Any]]] = None,
                start_application: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
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
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument inputs", value=inputs, expected_type=type_hints["inputs"])
            check_type(argname="argument outputs", value=outputs, expected_type=type_hints["outputs"])
            check_type(argname="argument reference_data_sources", value=reference_data_sources, expected_type=type_hints["reference_data_sources"])
            check_type(argname="argument start_application", value=start_application, expected_type=type_hints["start_application"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
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
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if code is not None:
            self._values["code"] = code
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if inputs is not None:
            self._values["inputs"] = inputs
        if outputs is not None:
            self._values["outputs"] = outputs
        if reference_data_sources is not None:
            self._values["reference_data_sources"] = reference_data_sources
        if start_application is not None:
            self._values["start_application"] = start_application
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name KinesisAnalyticsApplication#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationCloudwatchLoggingOptions]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#cloudwatch_logging_options KinesisAnalyticsApplication#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationCloudwatchLoggingOptions], result)

    @builtins.property
    def code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#code KinesisAnalyticsApplication#code}.'''
        result = self._values.get("code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#description KinesisAnalyticsApplication#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#id KinesisAnalyticsApplication#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inputs(self) -> typing.Optional["KinesisAnalyticsApplicationInputs"]:
        '''inputs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#inputs KinesisAnalyticsApplication#inputs}
        '''
        result = self._values.get("inputs")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputs"], result)

    @builtins.property
    def outputs(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisAnalyticsApplicationOutputs"]]]:
        '''outputs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#outputs KinesisAnalyticsApplication#outputs}
        '''
        result = self._values.get("outputs")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisAnalyticsApplicationOutputs"]]], result)

    @builtins.property
    def reference_data_sources(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationReferenceDataSources"]:
        '''reference_data_sources block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#reference_data_sources KinesisAnalyticsApplication#reference_data_sources}
        '''
        result = self._values.get("reference_data_sources")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationReferenceDataSources"], result)

    @builtins.property
    def start_application(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#start_application KinesisAnalyticsApplication#start_application}.'''
        result = self._values.get("start_application")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#tags KinesisAnalyticsApplication#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#tags_all KinesisAnalyticsApplication#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputs",
    jsii_struct_bases=[],
    name_mapping={
        "name_prefix": "namePrefix",
        "schema": "schema",
        "kinesis_firehose": "kinesisFirehose",
        "kinesis_stream": "kinesisStream",
        "parallelism": "parallelism",
        "processing_configuration": "processingConfiguration",
        "starting_position_configuration": "startingPositionConfiguration",
    },
)
class KinesisAnalyticsApplicationInputs:
    def __init__(
        self,
        *,
        name_prefix: builtins.str,
        schema: typing.Union["KinesisAnalyticsApplicationInputsSchema", typing.Dict[str, typing.Any]],
        kinesis_firehose: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsKinesisFirehose", typing.Dict[str, typing.Any]]] = None,
        kinesis_stream: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsKinesisStream", typing.Dict[str, typing.Any]]] = None,
        parallelism: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsParallelism", typing.Dict[str, typing.Any]]] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsProcessingConfiguration", typing.Dict[str, typing.Any]]] = None,
        starting_position_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationInputsStartingPositionConfiguration", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name_prefix KinesisAnalyticsApplication#name_prefix}.
        :param schema: schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#schema KinesisAnalyticsApplication#schema}
        :param kinesis_firehose: kinesis_firehose block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_firehose KinesisAnalyticsApplication#kinesis_firehose}
        :param kinesis_stream: kinesis_stream block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_stream KinesisAnalyticsApplication#kinesis_stream}
        :param parallelism: parallelism block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#parallelism KinesisAnalyticsApplication#parallelism}
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#processing_configuration KinesisAnalyticsApplication#processing_configuration}
        :param starting_position_configuration: starting_position_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#starting_position_configuration KinesisAnalyticsApplication#starting_position_configuration}
        '''
        if isinstance(schema, dict):
            schema = KinesisAnalyticsApplicationInputsSchema(**schema)
        if isinstance(kinesis_firehose, dict):
            kinesis_firehose = KinesisAnalyticsApplicationInputsKinesisFirehose(**kinesis_firehose)
        if isinstance(kinesis_stream, dict):
            kinesis_stream = KinesisAnalyticsApplicationInputsKinesisStream(**kinesis_stream)
        if isinstance(parallelism, dict):
            parallelism = KinesisAnalyticsApplicationInputsParallelism(**parallelism)
        if isinstance(processing_configuration, dict):
            processing_configuration = KinesisAnalyticsApplicationInputsProcessingConfiguration(**processing_configuration)
        if __debug__:
            def stub(
                *,
                name_prefix: builtins.str,
                schema: typing.Union[KinesisAnalyticsApplicationInputsSchema, typing.Dict[str, typing.Any]],
                kinesis_firehose: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsKinesisFirehose, typing.Dict[str, typing.Any]]] = None,
                kinesis_stream: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsKinesisStream, typing.Dict[str, typing.Any]]] = None,
                parallelism: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsParallelism, typing.Dict[str, typing.Any]]] = None,
                processing_configuration: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsProcessingConfiguration, typing.Dict[str, typing.Any]]] = None,
                starting_position_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisAnalyticsApplicationInputsStartingPositionConfiguration, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument kinesis_firehose", value=kinesis_firehose, expected_type=type_hints["kinesis_firehose"])
            check_type(argname="argument kinesis_stream", value=kinesis_stream, expected_type=type_hints["kinesis_stream"])
            check_type(argname="argument parallelism", value=parallelism, expected_type=type_hints["parallelism"])
            check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
            check_type(argname="argument starting_position_configuration", value=starting_position_configuration, expected_type=type_hints["starting_position_configuration"])
        self._values: typing.Dict[str, typing.Any] = {
            "name_prefix": name_prefix,
            "schema": schema,
        }
        if kinesis_firehose is not None:
            self._values["kinesis_firehose"] = kinesis_firehose
        if kinesis_stream is not None:
            self._values["kinesis_stream"] = kinesis_stream
        if parallelism is not None:
            self._values["parallelism"] = parallelism
        if processing_configuration is not None:
            self._values["processing_configuration"] = processing_configuration
        if starting_position_configuration is not None:
            self._values["starting_position_configuration"] = starting_position_configuration

    @builtins.property
    def name_prefix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name_prefix KinesisAnalyticsApplication#name_prefix}.'''
        result = self._values.get("name_prefix")
        assert result is not None, "Required property 'name_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema(self) -> "KinesisAnalyticsApplicationInputsSchema":
        '''schema block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#schema KinesisAnalyticsApplication#schema}
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast("KinesisAnalyticsApplicationInputsSchema", result)

    @builtins.property
    def kinesis_firehose(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsKinesisFirehose"]:
        '''kinesis_firehose block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_firehose KinesisAnalyticsApplication#kinesis_firehose}
        '''
        result = self._values.get("kinesis_firehose")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsKinesisFirehose"], result)

    @builtins.property
    def kinesis_stream(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsKinesisStream"]:
        '''kinesis_stream block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_stream KinesisAnalyticsApplication#kinesis_stream}
        '''
        result = self._values.get("kinesis_stream")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsKinesisStream"], result)

    @builtins.property
    def parallelism(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsParallelism"]:
        '''parallelism block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#parallelism KinesisAnalyticsApplication#parallelism}
        '''
        result = self._values.get("parallelism")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsParallelism"], result)

    @builtins.property
    def processing_configuration(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsProcessingConfiguration"]:
        '''processing_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#processing_configuration KinesisAnalyticsApplication#processing_configuration}
        '''
        result = self._values.get("processing_configuration")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsProcessingConfiguration"], result)

    @builtins.property
    def starting_position_configuration(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisAnalyticsApplicationInputsStartingPositionConfiguration"]]]:
        '''starting_position_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#starting_position_configuration KinesisAnalyticsApplication#starting_position_configuration}
        '''
        result = self._values.get("starting_position_configuration")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisAnalyticsApplicationInputsStartingPositionConfiguration"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsKinesisFirehose",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn", "role_arn": "roleArn"},
)
class KinesisAnalyticsApplicationInputsKinesisFirehose:
    def __init__(self, *, resource_arn: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        if __debug__:
            def stub(*, resource_arn: builtins.str, role_arn: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "resource_arn": resource_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsKinesisFirehose(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationInputsKinesisFirehoseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsKinesisFirehoseOutputReference",
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
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

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
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsKinesisFirehose]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsKinesisFirehose], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsKinesisFirehose],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationInputsKinesisFirehose],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsKinesisStream",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn", "role_arn": "roleArn"},
)
class KinesisAnalyticsApplicationInputsKinesisStream:
    def __init__(self, *, resource_arn: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        if __debug__:
            def stub(*, resource_arn: builtins.str, role_arn: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "resource_arn": resource_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsKinesisStream(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationInputsKinesisStreamOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsKinesisStreamOutputReference",
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
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

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
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsKinesisStream]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsKinesisStream], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsKinesisStream],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationInputsKinesisStream],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationInputsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsOutputReference",
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

    @jsii.member(jsii_name="putKinesisFirehose")
    def put_kinesis_firehose(
        self,
        *,
        resource_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        value = KinesisAnalyticsApplicationInputsKinesisFirehose(
            resource_arn=resource_arn, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisFirehose", [value]))

    @jsii.member(jsii_name="putKinesisStream")
    def put_kinesis_stream(
        self,
        *,
        resource_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        value = KinesisAnalyticsApplicationInputsKinesisStream(
            resource_arn=resource_arn, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisStream", [value]))

    @jsii.member(jsii_name="putParallelism")
    def put_parallelism(self, *, count: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#count KinesisAnalyticsApplication#count}.
        '''
        value = KinesisAnalyticsApplicationInputsParallelism(count=count)

        return typing.cast(None, jsii.invoke(self, "putParallelism", [value]))

    @jsii.member(jsii_name="putProcessingConfiguration")
    def put_processing_configuration(
        self,
        *,
        lambda_: typing.Union["KinesisAnalyticsApplicationInputsProcessingConfigurationLambda", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param lambda_: lambda block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#lambda KinesisAnalyticsApplication#lambda}
        '''
        value = KinesisAnalyticsApplicationInputsProcessingConfiguration(
            lambda_=lambda_
        )

        return typing.cast(None, jsii.invoke(self, "putProcessingConfiguration", [value]))

    @jsii.member(jsii_name="putSchema")
    def put_schema(
        self,
        *,
        record_columns: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationInputsSchemaRecordColumns", typing.Dict[str, typing.Any]]]],
        record_format: typing.Union["KinesisAnalyticsApplicationInputsSchemaRecordFormat", typing.Dict[str, typing.Any]],
        record_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param record_columns: record_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_columns KinesisAnalyticsApplication#record_columns}
        :param record_format: record_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_format KinesisAnalyticsApplication#record_format}
        :param record_encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_encoding KinesisAnalyticsApplication#record_encoding}.
        '''
        value = KinesisAnalyticsApplicationInputsSchema(
            record_columns=record_columns,
            record_format=record_format,
            record_encoding=record_encoding,
        )

        return typing.cast(None, jsii.invoke(self, "putSchema", [value]))

    @jsii.member(jsii_name="putStartingPositionConfiguration")
    def put_starting_position_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationInputsStartingPositionConfiguration", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisAnalyticsApplicationInputsStartingPositionConfiguration, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStartingPositionConfiguration", [value]))

    @jsii.member(jsii_name="resetKinesisFirehose")
    def reset_kinesis_firehose(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisFirehose", []))

    @jsii.member(jsii_name="resetKinesisStream")
    def reset_kinesis_stream(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisStream", []))

    @jsii.member(jsii_name="resetParallelism")
    def reset_parallelism(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParallelism", []))

    @jsii.member(jsii_name="resetProcessingConfiguration")
    def reset_processing_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessingConfiguration", []))

    @jsii.member(jsii_name="resetStartingPositionConfiguration")
    def reset_starting_position_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartingPositionConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="kinesisFirehose")
    def kinesis_firehose(
        self,
    ) -> KinesisAnalyticsApplicationInputsKinesisFirehoseOutputReference:
        return typing.cast(KinesisAnalyticsApplicationInputsKinesisFirehoseOutputReference, jsii.get(self, "kinesisFirehose"))

    @builtins.property
    @jsii.member(jsii_name="kinesisStream")
    def kinesis_stream(
        self,
    ) -> KinesisAnalyticsApplicationInputsKinesisStreamOutputReference:
        return typing.cast(KinesisAnalyticsApplicationInputsKinesisStreamOutputReference, jsii.get(self, "kinesisStream"))

    @builtins.property
    @jsii.member(jsii_name="parallelism")
    def parallelism(
        self,
    ) -> "KinesisAnalyticsApplicationInputsParallelismOutputReference":
        return typing.cast("KinesisAnalyticsApplicationInputsParallelismOutputReference", jsii.get(self, "parallelism"))

    @builtins.property
    @jsii.member(jsii_name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> "KinesisAnalyticsApplicationInputsProcessingConfigurationOutputReference":
        return typing.cast("KinesisAnalyticsApplicationInputsProcessingConfigurationOutputReference", jsii.get(self, "processingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> "KinesisAnalyticsApplicationInputsSchemaOutputReference":
        return typing.cast("KinesisAnalyticsApplicationInputsSchemaOutputReference", jsii.get(self, "schema"))

    @builtins.property
    @jsii.member(jsii_name="startingPositionConfiguration")
    def starting_position_configuration(
        self,
    ) -> "KinesisAnalyticsApplicationInputsStartingPositionConfigurationList":
        return typing.cast("KinesisAnalyticsApplicationInputsStartingPositionConfigurationList", jsii.get(self, "startingPositionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="streamNames")
    def stream_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "streamNames"))

    @builtins.property
    @jsii.member(jsii_name="kinesisFirehoseInput")
    def kinesis_firehose_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsKinesisFirehose]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsKinesisFirehose], jsii.get(self, "kinesisFirehoseInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisStreamInput")
    def kinesis_stream_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsKinesisStream]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsKinesisStream], jsii.get(self, "kinesisStreamInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="parallelismInput")
    def parallelism_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsParallelism"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsParallelism"], jsii.get(self, "parallelismInput"))

    @builtins.property
    @jsii.member(jsii_name="processingConfigurationInput")
    def processing_configuration_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsProcessingConfiguration"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsProcessingConfiguration"], jsii.get(self, "processingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsSchema"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsSchema"], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="startingPositionConfigurationInput")
    def starting_position_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisAnalyticsApplicationInputsStartingPositionConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisAnalyticsApplicationInputsStartingPositionConfiguration"]]], jsii.get(self, "startingPositionConfigurationInput"))

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KinesisAnalyticsApplicationInputs]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputs],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[KinesisAnalyticsApplicationInputs]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsParallelism",
    jsii_struct_bases=[],
    name_mapping={"count": "count"},
)
class KinesisAnalyticsApplicationInputsParallelism:
    def __init__(self, *, count: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#count KinesisAnalyticsApplication#count}.
        '''
        if __debug__:
            def stub(*, count: typing.Optional[jsii.Number] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#count KinesisAnalyticsApplication#count}.'''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsParallelism(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationInputsParallelismOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsParallelismOutputReference",
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

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsParallelism]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsParallelism], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsParallelism],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationInputsParallelism],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsProcessingConfiguration",
    jsii_struct_bases=[],
    name_mapping={"lambda_": "lambda"},
)
class KinesisAnalyticsApplicationInputsProcessingConfiguration:
    def __init__(
        self,
        *,
        lambda_: typing.Union["KinesisAnalyticsApplicationInputsProcessingConfigurationLambda", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param lambda_: lambda block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#lambda KinesisAnalyticsApplication#lambda}
        '''
        if isinstance(lambda_, dict):
            lambda_ = KinesisAnalyticsApplicationInputsProcessingConfigurationLambda(**lambda_)
        if __debug__:
            def stub(
                *,
                lambda_: typing.Union[KinesisAnalyticsApplicationInputsProcessingConfigurationLambda, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
        self._values: typing.Dict[str, typing.Any] = {
            "lambda_": lambda_,
        }

    @builtins.property
    def lambda_(
        self,
    ) -> "KinesisAnalyticsApplicationInputsProcessingConfigurationLambda":
        '''lambda block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#lambda KinesisAnalyticsApplication#lambda}
        '''
        result = self._values.get("lambda_")
        assert result is not None, "Required property 'lambda_' is missing"
        return typing.cast("KinesisAnalyticsApplicationInputsProcessingConfigurationLambda", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsProcessingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsProcessingConfigurationLambda",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn", "role_arn": "roleArn"},
)
class KinesisAnalyticsApplicationInputsProcessingConfigurationLambda:
    def __init__(self, *, resource_arn: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        if __debug__:
            def stub(*, resource_arn: builtins.str, role_arn: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "resource_arn": resource_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsProcessingConfigurationLambda(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationInputsProcessingConfigurationLambdaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsProcessingConfigurationLambdaOutputReference",
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
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

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
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfigurationLambda]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfigurationLambda], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfigurationLambda],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfigurationLambda],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationInputsProcessingConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsProcessingConfigurationOutputReference",
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

    @jsii.member(jsii_name="putLambda")
    def put_lambda(self, *, resource_arn: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        value = KinesisAnalyticsApplicationInputsProcessingConfigurationLambda(
            resource_arn=resource_arn, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putLambda", [value]))

    @builtins.property
    @jsii.member(jsii_name="lambda")
    def lambda_(
        self,
    ) -> KinesisAnalyticsApplicationInputsProcessingConfigurationLambdaOutputReference:
        return typing.cast(KinesisAnalyticsApplicationInputsProcessingConfigurationLambdaOutputReference, jsii.get(self, "lambda"))

    @builtins.property
    @jsii.member(jsii_name="lambdaInput")
    def lambda_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfigurationLambda]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfigurationLambda], jsii.get(self, "lambdaInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfiguration]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationInputsProcessingConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchema",
    jsii_struct_bases=[],
    name_mapping={
        "record_columns": "recordColumns",
        "record_format": "recordFormat",
        "record_encoding": "recordEncoding",
    },
)
class KinesisAnalyticsApplicationInputsSchema:
    def __init__(
        self,
        *,
        record_columns: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationInputsSchemaRecordColumns", typing.Dict[str, typing.Any]]]],
        record_format: typing.Union["KinesisAnalyticsApplicationInputsSchemaRecordFormat", typing.Dict[str, typing.Any]],
        record_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param record_columns: record_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_columns KinesisAnalyticsApplication#record_columns}
        :param record_format: record_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_format KinesisAnalyticsApplication#record_format}
        :param record_encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_encoding KinesisAnalyticsApplication#record_encoding}.
        '''
        if isinstance(record_format, dict):
            record_format = KinesisAnalyticsApplicationInputsSchemaRecordFormat(**record_format)
        if __debug__:
            def stub(
                *,
                record_columns: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordColumns, typing.Dict[str, typing.Any]]]],
                record_format: typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordFormat, typing.Dict[str, typing.Any]],
                record_encoding: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument record_columns", value=record_columns, expected_type=type_hints["record_columns"])
            check_type(argname="argument record_format", value=record_format, expected_type=type_hints["record_format"])
            check_type(argname="argument record_encoding", value=record_encoding, expected_type=type_hints["record_encoding"])
        self._values: typing.Dict[str, typing.Any] = {
            "record_columns": record_columns,
            "record_format": record_format,
        }
        if record_encoding is not None:
            self._values["record_encoding"] = record_encoding

    @builtins.property
    def record_columns(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["KinesisAnalyticsApplicationInputsSchemaRecordColumns"]]:
        '''record_columns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_columns KinesisAnalyticsApplication#record_columns}
        '''
        result = self._values.get("record_columns")
        assert result is not None, "Required property 'record_columns' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["KinesisAnalyticsApplicationInputsSchemaRecordColumns"]], result)

    @builtins.property
    def record_format(self) -> "KinesisAnalyticsApplicationInputsSchemaRecordFormat":
        '''record_format block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_format KinesisAnalyticsApplication#record_format}
        '''
        result = self._values.get("record_format")
        assert result is not None, "Required property 'record_format' is missing"
        return typing.cast("KinesisAnalyticsApplicationInputsSchemaRecordFormat", result)

    @builtins.property
    def record_encoding(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_encoding KinesisAnalyticsApplication#record_encoding}.'''
        result = self._values.get("record_encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationInputsSchemaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaOutputReference",
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

    @jsii.member(jsii_name="putRecordColumns")
    def put_record_columns(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationInputsSchemaRecordColumns", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordColumns, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRecordColumns", [value]))

    @jsii.member(jsii_name="putRecordFormat")
    def put_record_format(
        self,
        *,
        mapping_parameters: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param mapping_parameters: mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping_parameters KinesisAnalyticsApplication#mapping_parameters}
        '''
        value = KinesisAnalyticsApplicationInputsSchemaRecordFormat(
            mapping_parameters=mapping_parameters
        )

        return typing.cast(None, jsii.invoke(self, "putRecordFormat", [value]))

    @jsii.member(jsii_name="resetRecordEncoding")
    def reset_record_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordEncoding", []))

    @builtins.property
    @jsii.member(jsii_name="recordColumns")
    def record_columns(
        self,
    ) -> "KinesisAnalyticsApplicationInputsSchemaRecordColumnsList":
        return typing.cast("KinesisAnalyticsApplicationInputsSchemaRecordColumnsList", jsii.get(self, "recordColumns"))

    @builtins.property
    @jsii.member(jsii_name="recordFormat")
    def record_format(
        self,
    ) -> "KinesisAnalyticsApplicationInputsSchemaRecordFormatOutputReference":
        return typing.cast("KinesisAnalyticsApplicationInputsSchemaRecordFormatOutputReference", jsii.get(self, "recordFormat"))

    @builtins.property
    @jsii.member(jsii_name="recordColumnsInput")
    def record_columns_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisAnalyticsApplicationInputsSchemaRecordColumns"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisAnalyticsApplicationInputsSchemaRecordColumns"]]], jsii.get(self, "recordColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="recordEncodingInput")
    def record_encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordEncodingInput"))

    @builtins.property
    @jsii.member(jsii_name="recordFormatInput")
    def record_format_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsSchemaRecordFormat"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsSchemaRecordFormat"], jsii.get(self, "recordFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="recordEncoding")
    def record_encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordEncoding"))

    @record_encoding.setter
    def record_encoding(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordEncoding", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsSchema]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsSchema], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsSchema],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationInputsSchema],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordColumns",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "sql_type": "sqlType", "mapping": "mapping"},
)
class KinesisAnalyticsApplicationInputsSchemaRecordColumns:
    def __init__(
        self,
        *,
        name: builtins.str,
        sql_type: builtins.str,
        mapping: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name KinesisAnalyticsApplication#name}.
        :param sql_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#sql_type KinesisAnalyticsApplication#sql_type}.
        :param mapping: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping KinesisAnalyticsApplication#mapping}.
        '''
        if __debug__:
            def stub(
                *,
                name: builtins.str,
                sql_type: builtins.str,
                mapping: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument sql_type", value=sql_type, expected_type=type_hints["sql_type"])
            check_type(argname="argument mapping", value=mapping, expected_type=type_hints["mapping"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "sql_type": sql_type,
        }
        if mapping is not None:
            self._values["mapping"] = mapping

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name KinesisAnalyticsApplication#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sql_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#sql_type KinesisAnalyticsApplication#sql_type}.'''
        result = self._values.get("sql_type")
        assert result is not None, "Required property 'sql_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mapping(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping KinesisAnalyticsApplication#mapping}.'''
        result = self._values.get("mapping")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsSchemaRecordColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationInputsSchemaRecordColumnsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordColumnsList",
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
    ) -> "KinesisAnalyticsApplicationInputsSchemaRecordColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisAnalyticsApplicationInputsSchemaRecordColumnsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisAnalyticsApplicationInputsSchemaRecordColumns]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisAnalyticsApplicationInputsSchemaRecordColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisAnalyticsApplicationInputsSchemaRecordColumns]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisAnalyticsApplicationInputsSchemaRecordColumns]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationInputsSchemaRecordColumnsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordColumnsOutputReference",
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

    @jsii.member(jsii_name="resetMapping")
    def reset_mapping(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMapping", []))

    @builtins.property
    @jsii.member(jsii_name="mappingInput")
    def mapping_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mappingInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlTypeInput")
    def sql_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="mapping")
    def mapping(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mapping"))

    @mapping.setter
    def mapping(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mapping", value)

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
    @jsii.member(jsii_name="sqlType")
    def sql_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlType"))

    @sql_type.setter
    def sql_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordColumns, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordColumns, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordColumns, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordColumns, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordFormat",
    jsii_struct_bases=[],
    name_mapping={"mapping_parameters": "mappingParameters"},
)
class KinesisAnalyticsApplicationInputsSchemaRecordFormat:
    def __init__(
        self,
        *,
        mapping_parameters: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param mapping_parameters: mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping_parameters KinesisAnalyticsApplication#mapping_parameters}
        '''
        if isinstance(mapping_parameters, dict):
            mapping_parameters = KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters(**mapping_parameters)
        if __debug__:
            def stub(
                *,
                mapping_parameters: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument mapping_parameters", value=mapping_parameters, expected_type=type_hints["mapping_parameters"])
        self._values: typing.Dict[str, typing.Any] = {}
        if mapping_parameters is not None:
            self._values["mapping_parameters"] = mapping_parameters

    @builtins.property
    def mapping_parameters(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters"]:
        '''mapping_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping_parameters KinesisAnalyticsApplication#mapping_parameters}
        '''
        result = self._values.get("mapping_parameters")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsSchemaRecordFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters",
    jsii_struct_bases=[],
    name_mapping={"csv": "csv", "json": "json"},
)
class KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters:
    def __init__(
        self,
        *,
        csv: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv", typing.Dict[str, typing.Any]]] = None,
        json: typing.Optional[typing.Union["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param csv: csv block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#csv KinesisAnalyticsApplication#csv}
        :param json: json block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#json KinesisAnalyticsApplication#json}
        '''
        if isinstance(csv, dict):
            csv = KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv(**csv)
        if isinstance(json, dict):
            json = KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson(**json)
        if __debug__:
            def stub(
                *,
                csv: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv, typing.Dict[str, typing.Any]]] = None,
                json: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument csv", value=csv, expected_type=type_hints["csv"])
            check_type(argname="argument json", value=json, expected_type=type_hints["json"])
        self._values: typing.Dict[str, typing.Any] = {}
        if csv is not None:
            self._values["csv"] = csv
        if json is not None:
            self._values["json"] = json

    @builtins.property
    def csv(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv"]:
        '''csv block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#csv KinesisAnalyticsApplication#csv}
        '''
        result = self._values.get("csv")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv"], result)

    @builtins.property
    def json(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson"]:
        '''json block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#json KinesisAnalyticsApplication#json}
        '''
        result = self._values.get("json")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv",
    jsii_struct_bases=[],
    name_mapping={
        "record_column_delimiter": "recordColumnDelimiter",
        "record_row_delimiter": "recordRowDelimiter",
    },
)
class KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv:
    def __init__(
        self,
        *,
        record_column_delimiter: builtins.str,
        record_row_delimiter: builtins.str,
    ) -> None:
        '''
        :param record_column_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_column_delimiter KinesisAnalyticsApplication#record_column_delimiter}.
        :param record_row_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_delimiter KinesisAnalyticsApplication#record_row_delimiter}.
        '''
        if __debug__:
            def stub(
                *,
                record_column_delimiter: builtins.str,
                record_row_delimiter: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument record_column_delimiter", value=record_column_delimiter, expected_type=type_hints["record_column_delimiter"])
            check_type(argname="argument record_row_delimiter", value=record_row_delimiter, expected_type=type_hints["record_row_delimiter"])
        self._values: typing.Dict[str, typing.Any] = {
            "record_column_delimiter": record_column_delimiter,
            "record_row_delimiter": record_row_delimiter,
        }

    @builtins.property
    def record_column_delimiter(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_column_delimiter KinesisAnalyticsApplication#record_column_delimiter}.'''
        result = self._values.get("record_column_delimiter")
        assert result is not None, "Required property 'record_column_delimiter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def record_row_delimiter(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_delimiter KinesisAnalyticsApplication#record_row_delimiter}.'''
        result = self._values.get("record_row_delimiter")
        assert result is not None, "Required property 'record_row_delimiter' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsvOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsvOutputReference",
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
    @jsii.member(jsii_name="recordColumnDelimiterInput")
    def record_column_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordColumnDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="recordRowDelimiterInput")
    def record_row_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordRowDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="recordColumnDelimiter")
    def record_column_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordColumnDelimiter"))

    @record_column_delimiter.setter
    def record_column_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordColumnDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="recordRowDelimiter")
    def record_row_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordRowDelimiter"))

    @record_row_delimiter.setter
    def record_row_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordRowDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson",
    jsii_struct_bases=[],
    name_mapping={"record_row_path": "recordRowPath"},
)
class KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson:
    def __init__(self, *, record_row_path: builtins.str) -> None:
        '''
        :param record_row_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_path KinesisAnalyticsApplication#record_row_path}.
        '''
        if __debug__:
            def stub(*, record_row_path: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument record_row_path", value=record_row_path, expected_type=type_hints["record_row_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "record_row_path": record_row_path,
        }

    @builtins.property
    def record_row_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_path KinesisAnalyticsApplication#record_row_path}.'''
        result = self._values.get("record_row_path")
        assert result is not None, "Required property 'record_row_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonOutputReference",
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
    @jsii.member(jsii_name="recordRowPathInput")
    def record_row_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordRowPathInput"))

    @builtins.property
    @jsii.member(jsii_name="recordRowPath")
    def record_row_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordRowPath"))

    @record_row_path.setter
    def record_row_path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordRowPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersOutputReference",
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

    @jsii.member(jsii_name="putCsv")
    def put_csv(
        self,
        *,
        record_column_delimiter: builtins.str,
        record_row_delimiter: builtins.str,
    ) -> None:
        '''
        :param record_column_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_column_delimiter KinesisAnalyticsApplication#record_column_delimiter}.
        :param record_row_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_delimiter KinesisAnalyticsApplication#record_row_delimiter}.
        '''
        value = KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv(
            record_column_delimiter=record_column_delimiter,
            record_row_delimiter=record_row_delimiter,
        )

        return typing.cast(None, jsii.invoke(self, "putCsv", [value]))

    @jsii.member(jsii_name="putJson")
    def put_json(self, *, record_row_path: builtins.str) -> None:
        '''
        :param record_row_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_path KinesisAnalyticsApplication#record_row_path}.
        '''
        value = KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson(
            record_row_path=record_row_path
        )

        return typing.cast(None, jsii.invoke(self, "putJson", [value]))

    @jsii.member(jsii_name="resetCsv")
    def reset_csv(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsv", []))

    @jsii.member(jsii_name="resetJson")
    def reset_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJson", []))

    @builtins.property
    @jsii.member(jsii_name="csv")
    def csv(
        self,
    ) -> KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsvOutputReference:
        return typing.cast(KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsvOutputReference, jsii.get(self, "csv"))

    @builtins.property
    @jsii.member(jsii_name="json")
    def json(
        self,
    ) -> KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonOutputReference:
        return typing.cast(KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonOutputReference, jsii.get(self, "json"))

    @builtins.property
    @jsii.member(jsii_name="csvInput")
    def csv_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv], jsii.get(self, "csvInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonInput")
    def json_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson], jsii.get(self, "jsonInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationInputsSchemaRecordFormatOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsSchemaRecordFormatOutputReference",
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

    @jsii.member(jsii_name="putMappingParameters")
    def put_mapping_parameters(
        self,
        *,
        csv: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv, typing.Dict[str, typing.Any]]] = None,
        json: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param csv: csv block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#csv KinesisAnalyticsApplication#csv}
        :param json: json block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#json KinesisAnalyticsApplication#json}
        '''
        value = KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters(
            csv=csv, json=json
        )

        return typing.cast(None, jsii.invoke(self, "putMappingParameters", [value]))

    @jsii.member(jsii_name="resetMappingParameters")
    def reset_mapping_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMappingParameters", []))

    @builtins.property
    @jsii.member(jsii_name="mappingParameters")
    def mapping_parameters(
        self,
    ) -> KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersOutputReference:
        return typing.cast(KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersOutputReference, jsii.get(self, "mappingParameters"))

    @builtins.property
    @jsii.member(jsii_name="recordFormatType")
    def record_format_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordFormatType"))

    @builtins.property
    @jsii.member(jsii_name="mappingParametersInput")
    def mapping_parameters_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters], jsii.get(self, "mappingParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormat]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormat],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationInputsSchemaRecordFormat],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsStartingPositionConfiguration",
    jsii_struct_bases=[],
    name_mapping={"starting_position": "startingPosition"},
)
class KinesisAnalyticsApplicationInputsStartingPositionConfiguration:
    def __init__(
        self,
        *,
        starting_position: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param starting_position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#starting_position KinesisAnalyticsApplication#starting_position}.
        '''
        if __debug__:
            def stub(
                *,
                starting_position: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument starting_position", value=starting_position, expected_type=type_hints["starting_position"])
        self._values: typing.Dict[str, typing.Any] = {}
        if starting_position is not None:
            self._values["starting_position"] = starting_position

    @builtins.property
    def starting_position(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#starting_position KinesisAnalyticsApplication#starting_position}.'''
        result = self._values.get("starting_position")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationInputsStartingPositionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationInputsStartingPositionConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsStartingPositionConfigurationList",
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
    ) -> "KinesisAnalyticsApplicationInputsStartingPositionConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisAnalyticsApplicationInputsStartingPositionConfigurationOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisAnalyticsApplicationInputsStartingPositionConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisAnalyticsApplicationInputsStartingPositionConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisAnalyticsApplicationInputsStartingPositionConfiguration]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisAnalyticsApplicationInputsStartingPositionConfiguration]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationInputsStartingPositionConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationInputsStartingPositionConfigurationOutputReference",
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

    @jsii.member(jsii_name="resetStartingPosition")
    def reset_starting_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartingPosition", []))

    @builtins.property
    @jsii.member(jsii_name="startingPositionInput")
    def starting_position_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startingPositionInput"))

    @builtins.property
    @jsii.member(jsii_name="startingPosition")
    def starting_position(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startingPosition"))

    @starting_position.setter
    def starting_position(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startingPosition", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsStartingPositionConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsStartingPositionConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsStartingPositionConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KinesisAnalyticsApplicationInputsStartingPositionConfiguration, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputs",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "schema": "schema",
        "kinesis_firehose": "kinesisFirehose",
        "kinesis_stream": "kinesisStream",
        "lambda_": "lambda",
    },
)
class KinesisAnalyticsApplicationOutputs:
    def __init__(
        self,
        *,
        name: builtins.str,
        schema: typing.Union["KinesisAnalyticsApplicationOutputsSchema", typing.Dict[str, typing.Any]],
        kinesis_firehose: typing.Optional[typing.Union["KinesisAnalyticsApplicationOutputsKinesisFirehose", typing.Dict[str, typing.Any]]] = None,
        kinesis_stream: typing.Optional[typing.Union["KinesisAnalyticsApplicationOutputsKinesisStream", typing.Dict[str, typing.Any]]] = None,
        lambda_: typing.Optional[typing.Union["KinesisAnalyticsApplicationOutputsLambda", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name KinesisAnalyticsApplication#name}.
        :param schema: schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#schema KinesisAnalyticsApplication#schema}
        :param kinesis_firehose: kinesis_firehose block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_firehose KinesisAnalyticsApplication#kinesis_firehose}
        :param kinesis_stream: kinesis_stream block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_stream KinesisAnalyticsApplication#kinesis_stream}
        :param lambda_: lambda block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#lambda KinesisAnalyticsApplication#lambda}
        '''
        if isinstance(schema, dict):
            schema = KinesisAnalyticsApplicationOutputsSchema(**schema)
        if isinstance(kinesis_firehose, dict):
            kinesis_firehose = KinesisAnalyticsApplicationOutputsKinesisFirehose(**kinesis_firehose)
        if isinstance(kinesis_stream, dict):
            kinesis_stream = KinesisAnalyticsApplicationOutputsKinesisStream(**kinesis_stream)
        if isinstance(lambda_, dict):
            lambda_ = KinesisAnalyticsApplicationOutputsLambda(**lambda_)
        if __debug__:
            def stub(
                *,
                name: builtins.str,
                schema: typing.Union[KinesisAnalyticsApplicationOutputsSchema, typing.Dict[str, typing.Any]],
                kinesis_firehose: typing.Optional[typing.Union[KinesisAnalyticsApplicationOutputsKinesisFirehose, typing.Dict[str, typing.Any]]] = None,
                kinesis_stream: typing.Optional[typing.Union[KinesisAnalyticsApplicationOutputsKinesisStream, typing.Dict[str, typing.Any]]] = None,
                lambda_: typing.Optional[typing.Union[KinesisAnalyticsApplicationOutputsLambda, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument kinesis_firehose", value=kinesis_firehose, expected_type=type_hints["kinesis_firehose"])
            check_type(argname="argument kinesis_stream", value=kinesis_stream, expected_type=type_hints["kinesis_stream"])
            check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "schema": schema,
        }
        if kinesis_firehose is not None:
            self._values["kinesis_firehose"] = kinesis_firehose
        if kinesis_stream is not None:
            self._values["kinesis_stream"] = kinesis_stream
        if lambda_ is not None:
            self._values["lambda_"] = lambda_

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name KinesisAnalyticsApplication#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema(self) -> "KinesisAnalyticsApplicationOutputsSchema":
        '''schema block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#schema KinesisAnalyticsApplication#schema}
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast("KinesisAnalyticsApplicationOutputsSchema", result)

    @builtins.property
    def kinesis_firehose(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationOutputsKinesisFirehose"]:
        '''kinesis_firehose block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_firehose KinesisAnalyticsApplication#kinesis_firehose}
        '''
        result = self._values.get("kinesis_firehose")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationOutputsKinesisFirehose"], result)

    @builtins.property
    def kinesis_stream(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationOutputsKinesisStream"]:
        '''kinesis_stream block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#kinesis_stream KinesisAnalyticsApplication#kinesis_stream}
        '''
        result = self._values.get("kinesis_stream")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationOutputsKinesisStream"], result)

    @builtins.property
    def lambda_(self) -> typing.Optional["KinesisAnalyticsApplicationOutputsLambda"]:
        '''lambda block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#lambda KinesisAnalyticsApplication#lambda}
        '''
        result = self._values.get("lambda_")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationOutputsLambda"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationOutputs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsKinesisFirehose",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn", "role_arn": "roleArn"},
)
class KinesisAnalyticsApplicationOutputsKinesisFirehose:
    def __init__(self, *, resource_arn: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        if __debug__:
            def stub(*, resource_arn: builtins.str, role_arn: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "resource_arn": resource_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationOutputsKinesisFirehose(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationOutputsKinesisFirehoseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsKinesisFirehoseOutputReference",
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
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

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
    ) -> typing.Optional[KinesisAnalyticsApplicationOutputsKinesisFirehose]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationOutputsKinesisFirehose], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationOutputsKinesisFirehose],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationOutputsKinesisFirehose],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsKinesisStream",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn", "role_arn": "roleArn"},
)
class KinesisAnalyticsApplicationOutputsKinesisStream:
    def __init__(self, *, resource_arn: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        if __debug__:
            def stub(*, resource_arn: builtins.str, role_arn: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "resource_arn": resource_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationOutputsKinesisStream(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationOutputsKinesisStreamOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsKinesisStreamOutputReference",
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
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

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
    ) -> typing.Optional[KinesisAnalyticsApplicationOutputsKinesisStream]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationOutputsKinesisStream], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationOutputsKinesisStream],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationOutputsKinesisStream],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsLambda",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn", "role_arn": "roleArn"},
)
class KinesisAnalyticsApplicationOutputsLambda:
    def __init__(self, *, resource_arn: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        if __debug__:
            def stub(*, resource_arn: builtins.str, role_arn: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "resource_arn": resource_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationOutputsLambda(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationOutputsLambdaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsLambdaOutputReference",
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
    @jsii.member(jsii_name="resourceArnInput")
    def resource_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

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
    ) -> typing.Optional[KinesisAnalyticsApplicationOutputsLambda]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationOutputsLambda], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationOutputsLambda],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationOutputsLambda],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationOutputsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsList",
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
    ) -> "KinesisAnalyticsApplicationOutputsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisAnalyticsApplicationOutputsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisAnalyticsApplicationOutputs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisAnalyticsApplicationOutputs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisAnalyticsApplicationOutputs]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisAnalyticsApplicationOutputs]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationOutputsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsOutputReference",
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

    @jsii.member(jsii_name="putKinesisFirehose")
    def put_kinesis_firehose(
        self,
        *,
        resource_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        value = KinesisAnalyticsApplicationOutputsKinesisFirehose(
            resource_arn=resource_arn, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisFirehose", [value]))

    @jsii.member(jsii_name="putKinesisStream")
    def put_kinesis_stream(
        self,
        *,
        resource_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        value = KinesisAnalyticsApplicationOutputsKinesisStream(
            resource_arn=resource_arn, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisStream", [value]))

    @jsii.member(jsii_name="putLambda")
    def put_lambda(self, *, resource_arn: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param resource_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#resource_arn KinesisAnalyticsApplication#resource_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        value = KinesisAnalyticsApplicationOutputsLambda(
            resource_arn=resource_arn, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putLambda", [value]))

    @jsii.member(jsii_name="putSchema")
    def put_schema(self, *, record_format_type: builtins.str) -> None:
        '''
        :param record_format_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_format_type KinesisAnalyticsApplication#record_format_type}.
        '''
        value = KinesisAnalyticsApplicationOutputsSchema(
            record_format_type=record_format_type
        )

        return typing.cast(None, jsii.invoke(self, "putSchema", [value]))

    @jsii.member(jsii_name="resetKinesisFirehose")
    def reset_kinesis_firehose(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisFirehose", []))

    @jsii.member(jsii_name="resetKinesisStream")
    def reset_kinesis_stream(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisStream", []))

    @jsii.member(jsii_name="resetLambda")
    def reset_lambda(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambda", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="kinesisFirehose")
    def kinesis_firehose(
        self,
    ) -> KinesisAnalyticsApplicationOutputsKinesisFirehoseOutputReference:
        return typing.cast(KinesisAnalyticsApplicationOutputsKinesisFirehoseOutputReference, jsii.get(self, "kinesisFirehose"))

    @builtins.property
    @jsii.member(jsii_name="kinesisStream")
    def kinesis_stream(
        self,
    ) -> KinesisAnalyticsApplicationOutputsKinesisStreamOutputReference:
        return typing.cast(KinesisAnalyticsApplicationOutputsKinesisStreamOutputReference, jsii.get(self, "kinesisStream"))

    @builtins.property
    @jsii.member(jsii_name="lambda")
    def lambda_(self) -> KinesisAnalyticsApplicationOutputsLambdaOutputReference:
        return typing.cast(KinesisAnalyticsApplicationOutputsLambdaOutputReference, jsii.get(self, "lambda"))

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> "KinesisAnalyticsApplicationOutputsSchemaOutputReference":
        return typing.cast("KinesisAnalyticsApplicationOutputsSchemaOutputReference", jsii.get(self, "schema"))

    @builtins.property
    @jsii.member(jsii_name="kinesisFirehoseInput")
    def kinesis_firehose_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationOutputsKinesisFirehose]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationOutputsKinesisFirehose], jsii.get(self, "kinesisFirehoseInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisStreamInput")
    def kinesis_stream_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationOutputsKinesisStream]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationOutputsKinesisStream], jsii.get(self, "kinesisStreamInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaInput")
    def lambda_input(self) -> typing.Optional[KinesisAnalyticsApplicationOutputsLambda]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationOutputsLambda], jsii.get(self, "lambdaInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationOutputsSchema"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationOutputsSchema"], jsii.get(self, "schemaInput"))

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
    ) -> typing.Optional[typing.Union[KinesisAnalyticsApplicationOutputs, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisAnalyticsApplicationOutputs, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisAnalyticsApplicationOutputs, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KinesisAnalyticsApplicationOutputs, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsSchema",
    jsii_struct_bases=[],
    name_mapping={"record_format_type": "recordFormatType"},
)
class KinesisAnalyticsApplicationOutputsSchema:
    def __init__(self, *, record_format_type: builtins.str) -> None:
        '''
        :param record_format_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_format_type KinesisAnalyticsApplication#record_format_type}.
        '''
        if __debug__:
            def stub(*, record_format_type: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument record_format_type", value=record_format_type, expected_type=type_hints["record_format_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "record_format_type": record_format_type,
        }

    @builtins.property
    def record_format_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_format_type KinesisAnalyticsApplication#record_format_type}.'''
        result = self._values.get("record_format_type")
        assert result is not None, "Required property 'record_format_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationOutputsSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationOutputsSchemaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationOutputsSchemaOutputReference",
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
    @jsii.member(jsii_name="recordFormatTypeInput")
    def record_format_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordFormatTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="recordFormatType")
    def record_format_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordFormatType"))

    @record_format_type.setter
    def record_format_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordFormatType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationOutputsSchema]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationOutputsSchema], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationOutputsSchema],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationOutputsSchema],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSources",
    jsii_struct_bases=[],
    name_mapping={"s3": "s3", "schema": "schema", "table_name": "tableName"},
)
class KinesisAnalyticsApplicationReferenceDataSources:
    def __init__(
        self,
        *,
        s3: typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesS3", typing.Dict[str, typing.Any]],
        schema: typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchema", typing.Dict[str, typing.Any]],
        table_name: builtins.str,
    ) -> None:
        '''
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#s3 KinesisAnalyticsApplication#s3}
        :param schema: schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#schema KinesisAnalyticsApplication#schema}
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#table_name KinesisAnalyticsApplication#table_name}.
        '''
        if isinstance(s3, dict):
            s3 = KinesisAnalyticsApplicationReferenceDataSourcesS3(**s3)
        if isinstance(schema, dict):
            schema = KinesisAnalyticsApplicationReferenceDataSourcesSchema(**schema)
        if __debug__:
            def stub(
                *,
                s3: typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesS3, typing.Dict[str, typing.Any]],
                schema: typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchema, typing.Dict[str, typing.Any]],
                table_name: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "s3": s3,
            "schema": schema,
            "table_name": table_name,
        }

    @builtins.property
    def s3(self) -> "KinesisAnalyticsApplicationReferenceDataSourcesS3":
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#s3 KinesisAnalyticsApplication#s3}
        '''
        result = self._values.get("s3")
        assert result is not None, "Required property 's3' is missing"
        return typing.cast("KinesisAnalyticsApplicationReferenceDataSourcesS3", result)

    @builtins.property
    def schema(self) -> "KinesisAnalyticsApplicationReferenceDataSourcesSchema":
        '''schema block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#schema KinesisAnalyticsApplication#schema}
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast("KinesisAnalyticsApplicationReferenceDataSourcesSchema", result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#table_name KinesisAnalyticsApplication#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationReferenceDataSources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationReferenceDataSourcesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesOutputReference",
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

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        bucket_arn: builtins.str,
        file_key: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#bucket_arn KinesisAnalyticsApplication#bucket_arn}.
        :param file_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#file_key KinesisAnalyticsApplication#file_key}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        value = KinesisAnalyticsApplicationReferenceDataSourcesS3(
            bucket_arn=bucket_arn, file_key=file_key, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="putSchema")
    def put_schema(
        self,
        *,
        record_columns: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns", typing.Dict[str, typing.Any]]]],
        record_format: typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat", typing.Dict[str, typing.Any]],
        record_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param record_columns: record_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_columns KinesisAnalyticsApplication#record_columns}
        :param record_format: record_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_format KinesisAnalyticsApplication#record_format}
        :param record_encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_encoding KinesisAnalyticsApplication#record_encoding}.
        '''
        value = KinesisAnalyticsApplicationReferenceDataSourcesSchema(
            record_columns=record_columns,
            record_format=record_format,
            record_encoding=record_encoding,
        )

        return typing.cast(None, jsii.invoke(self, "putSchema", [value]))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "KinesisAnalyticsApplicationReferenceDataSourcesS3OutputReference":
        return typing.cast("KinesisAnalyticsApplicationReferenceDataSourcesS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(
        self,
    ) -> "KinesisAnalyticsApplicationReferenceDataSourcesSchemaOutputReference":
        return typing.cast("KinesisAnalyticsApplicationReferenceDataSourcesSchemaOutputReference", jsii.get(self, "schema"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesS3"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchema"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchema"], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSources]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSources], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSources],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSources],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesS3",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_arn": "bucketArn",
        "file_key": "fileKey",
        "role_arn": "roleArn",
    },
)
class KinesisAnalyticsApplicationReferenceDataSourcesS3:
    def __init__(
        self,
        *,
        bucket_arn: builtins.str,
        file_key: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#bucket_arn KinesisAnalyticsApplication#bucket_arn}.
        :param file_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#file_key KinesisAnalyticsApplication#file_key}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.
        '''
        if __debug__:
            def stub(
                *,
                bucket_arn: builtins.str,
                file_key: builtins.str,
                role_arn: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
            check_type(argname="argument file_key", value=file_key, expected_type=type_hints["file_key"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_arn": bucket_arn,
            "file_key": file_key,
            "role_arn": role_arn,
        }

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#bucket_arn KinesisAnalyticsApplication#bucket_arn}.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def file_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#file_key KinesisAnalyticsApplication#file_key}.'''
        result = self._values.get("file_key")
        assert result is not None, "Required property 'file_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#role_arn KinesisAnalyticsApplication#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationReferenceDataSourcesS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationReferenceDataSourcesS3OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesS3OutputReference",
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
    @jsii.member(jsii_name="bucketArnInput")
    def bucket_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketArnInput"))

    @builtins.property
    @jsii.member(jsii_name="fileKeyInput")
    def file_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketArn")
    def bucket_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketArn"))

    @bucket_arn.setter
    def bucket_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="fileKey")
    def file_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileKey"))

    @file_key.setter
    def file_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileKey", value)

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
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesS3]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesS3],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesS3],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchema",
    jsii_struct_bases=[],
    name_mapping={
        "record_columns": "recordColumns",
        "record_format": "recordFormat",
        "record_encoding": "recordEncoding",
    },
)
class KinesisAnalyticsApplicationReferenceDataSourcesSchema:
    def __init__(
        self,
        *,
        record_columns: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns", typing.Dict[str, typing.Any]]]],
        record_format: typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat", typing.Dict[str, typing.Any]],
        record_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param record_columns: record_columns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_columns KinesisAnalyticsApplication#record_columns}
        :param record_format: record_format block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_format KinesisAnalyticsApplication#record_format}
        :param record_encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_encoding KinesisAnalyticsApplication#record_encoding}.
        '''
        if isinstance(record_format, dict):
            record_format = KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat(**record_format)
        if __debug__:
            def stub(
                *,
                record_columns: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns, typing.Dict[str, typing.Any]]]],
                record_format: typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat, typing.Dict[str, typing.Any]],
                record_encoding: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument record_columns", value=record_columns, expected_type=type_hints["record_columns"])
            check_type(argname="argument record_format", value=record_format, expected_type=type_hints["record_format"])
            check_type(argname="argument record_encoding", value=record_encoding, expected_type=type_hints["record_encoding"])
        self._values: typing.Dict[str, typing.Any] = {
            "record_columns": record_columns,
            "record_format": record_format,
        }
        if record_encoding is not None:
            self._values["record_encoding"] = record_encoding

    @builtins.property
    def record_columns(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns"]]:
        '''record_columns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_columns KinesisAnalyticsApplication#record_columns}
        '''
        result = self._values.get("record_columns")
        assert result is not None, "Required property 'record_columns' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns"]], result)

    @builtins.property
    def record_format(
        self,
    ) -> "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat":
        '''record_format block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_format KinesisAnalyticsApplication#record_format}
        '''
        result = self._values.get("record_format")
        assert result is not None, "Required property 'record_format' is missing"
        return typing.cast("KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat", result)

    @builtins.property
    def record_encoding(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_encoding KinesisAnalyticsApplication#record_encoding}.'''
        result = self._values.get("record_encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationReferenceDataSourcesSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationReferenceDataSourcesSchemaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaOutputReference",
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

    @jsii.member(jsii_name="putRecordColumns")
    def put_record_columns(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRecordColumns", [value]))

    @jsii.member(jsii_name="putRecordFormat")
    def put_record_format(
        self,
        *,
        mapping_parameters: typing.Optional[typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param mapping_parameters: mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping_parameters KinesisAnalyticsApplication#mapping_parameters}
        '''
        value = KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat(
            mapping_parameters=mapping_parameters
        )

        return typing.cast(None, jsii.invoke(self, "putRecordFormat", [value]))

    @jsii.member(jsii_name="resetRecordEncoding")
    def reset_record_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordEncoding", []))

    @builtins.property
    @jsii.member(jsii_name="recordColumns")
    def record_columns(
        self,
    ) -> "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsList":
        return typing.cast("KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsList", jsii.get(self, "recordColumns"))

    @builtins.property
    @jsii.member(jsii_name="recordFormat")
    def record_format(
        self,
    ) -> "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatOutputReference":
        return typing.cast("KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatOutputReference", jsii.get(self, "recordFormat"))

    @builtins.property
    @jsii.member(jsii_name="recordColumnsInput")
    def record_columns_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns"]]], jsii.get(self, "recordColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="recordEncodingInput")
    def record_encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordEncodingInput"))

    @builtins.property
    @jsii.member(jsii_name="recordFormatInput")
    def record_format_input(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat"]:
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat"], jsii.get(self, "recordFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="recordEncoding")
    def record_encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordEncoding"))

    @record_encoding.setter
    def record_encoding(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordEncoding", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchema]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchema], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchema],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchema],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "sql_type": "sqlType", "mapping": "mapping"},
)
class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns:
    def __init__(
        self,
        *,
        name: builtins.str,
        sql_type: builtins.str,
        mapping: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name KinesisAnalyticsApplication#name}.
        :param sql_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#sql_type KinesisAnalyticsApplication#sql_type}.
        :param mapping: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping KinesisAnalyticsApplication#mapping}.
        '''
        if __debug__:
            def stub(
                *,
                name: builtins.str,
                sql_type: builtins.str,
                mapping: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument sql_type", value=sql_type, expected_type=type_hints["sql_type"])
            check_type(argname="argument mapping", value=mapping, expected_type=type_hints["mapping"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "sql_type": sql_type,
        }
        if mapping is not None:
            self._values["mapping"] = mapping

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#name KinesisAnalyticsApplication#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sql_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#sql_type KinesisAnalyticsApplication#sql_type}.'''
        result = self._values.get("sql_type")
        assert result is not None, "Required property 'sql_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mapping(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping KinesisAnalyticsApplication#mapping}.'''
        result = self._values.get("mapping")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsList",
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
    ) -> "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsOutputReference",
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

    @jsii.member(jsii_name="resetMapping")
    def reset_mapping(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMapping", []))

    @builtins.property
    @jsii.member(jsii_name="mappingInput")
    def mapping_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mappingInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlTypeInput")
    def sql_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="mapping")
    def mapping(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mapping"))

    @mapping.setter
    def mapping(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mapping", value)

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
    @jsii.member(jsii_name="sqlType")
    def sql_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlType"))

    @sql_type.setter
    def sql_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat",
    jsii_struct_bases=[],
    name_mapping={"mapping_parameters": "mappingParameters"},
)
class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat:
    def __init__(
        self,
        *,
        mapping_parameters: typing.Optional[typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param mapping_parameters: mapping_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping_parameters KinesisAnalyticsApplication#mapping_parameters}
        '''
        if isinstance(mapping_parameters, dict):
            mapping_parameters = KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters(**mapping_parameters)
        if __debug__:
            def stub(
                *,
                mapping_parameters: typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument mapping_parameters", value=mapping_parameters, expected_type=type_hints["mapping_parameters"])
        self._values: typing.Dict[str, typing.Any] = {}
        if mapping_parameters is not None:
            self._values["mapping_parameters"] = mapping_parameters

    @builtins.property
    def mapping_parameters(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters"]:
        '''mapping_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#mapping_parameters KinesisAnalyticsApplication#mapping_parameters}
        '''
        result = self._values.get("mapping_parameters")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters",
    jsii_struct_bases=[],
    name_mapping={"csv": "csv", "json": "json"},
)
class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters:
    def __init__(
        self,
        *,
        csv: typing.Optional[typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv", typing.Dict[str, typing.Any]]] = None,
        json: typing.Optional[typing.Union["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param csv: csv block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#csv KinesisAnalyticsApplication#csv}
        :param json: json block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#json KinesisAnalyticsApplication#json}
        '''
        if isinstance(csv, dict):
            csv = KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv(**csv)
        if isinstance(json, dict):
            json = KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson(**json)
        if __debug__:
            def stub(
                *,
                csv: typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv, typing.Dict[str, typing.Any]]] = None,
                json: typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument csv", value=csv, expected_type=type_hints["csv"])
            check_type(argname="argument json", value=json, expected_type=type_hints["json"])
        self._values: typing.Dict[str, typing.Any] = {}
        if csv is not None:
            self._values["csv"] = csv
        if json is not None:
            self._values["json"] = json

    @builtins.property
    def csv(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv"]:
        '''csv block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#csv KinesisAnalyticsApplication#csv}
        '''
        result = self._values.get("csv")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv"], result)

    @builtins.property
    def json(
        self,
    ) -> typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson"]:
        '''json block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#json KinesisAnalyticsApplication#json}
        '''
        result = self._values.get("json")
        return typing.cast(typing.Optional["KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv",
    jsii_struct_bases=[],
    name_mapping={
        "record_column_delimiter": "recordColumnDelimiter",
        "record_row_delimiter": "recordRowDelimiter",
    },
)
class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv:
    def __init__(
        self,
        *,
        record_column_delimiter: builtins.str,
        record_row_delimiter: builtins.str,
    ) -> None:
        '''
        :param record_column_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_column_delimiter KinesisAnalyticsApplication#record_column_delimiter}.
        :param record_row_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_delimiter KinesisAnalyticsApplication#record_row_delimiter}.
        '''
        if __debug__:
            def stub(
                *,
                record_column_delimiter: builtins.str,
                record_row_delimiter: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument record_column_delimiter", value=record_column_delimiter, expected_type=type_hints["record_column_delimiter"])
            check_type(argname="argument record_row_delimiter", value=record_row_delimiter, expected_type=type_hints["record_row_delimiter"])
        self._values: typing.Dict[str, typing.Any] = {
            "record_column_delimiter": record_column_delimiter,
            "record_row_delimiter": record_row_delimiter,
        }

    @builtins.property
    def record_column_delimiter(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_column_delimiter KinesisAnalyticsApplication#record_column_delimiter}.'''
        result = self._values.get("record_column_delimiter")
        assert result is not None, "Required property 'record_column_delimiter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def record_row_delimiter(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_delimiter KinesisAnalyticsApplication#record_row_delimiter}.'''
        result = self._values.get("record_row_delimiter")
        assert result is not None, "Required property 'record_row_delimiter' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsvOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsvOutputReference",
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
    @jsii.member(jsii_name="recordColumnDelimiterInput")
    def record_column_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordColumnDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="recordRowDelimiterInput")
    def record_row_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordRowDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="recordColumnDelimiter")
    def record_column_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordColumnDelimiter"))

    @record_column_delimiter.setter
    def record_column_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordColumnDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="recordRowDelimiter")
    def record_row_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordRowDelimiter"))

    @record_row_delimiter.setter
    def record_row_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordRowDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson",
    jsii_struct_bases=[],
    name_mapping={"record_row_path": "recordRowPath"},
)
class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson:
    def __init__(self, *, record_row_path: builtins.str) -> None:
        '''
        :param record_row_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_path KinesisAnalyticsApplication#record_row_path}.
        '''
        if __debug__:
            def stub(*, record_row_path: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument record_row_path", value=record_row_path, expected_type=type_hints["record_row_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "record_row_path": record_row_path,
        }

    @builtins.property
    def record_row_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_path KinesisAnalyticsApplication#record_row_path}.'''
        result = self._values.get("record_row_path")
        assert result is not None, "Required property 'record_row_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJsonOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJsonOutputReference",
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
    @jsii.member(jsii_name="recordRowPathInput")
    def record_row_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordRowPathInput"))

    @builtins.property
    @jsii.member(jsii_name="recordRowPath")
    def record_row_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordRowPath"))

    @record_row_path.setter
    def record_row_path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordRowPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersOutputReference",
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

    @jsii.member(jsii_name="putCsv")
    def put_csv(
        self,
        *,
        record_column_delimiter: builtins.str,
        record_row_delimiter: builtins.str,
    ) -> None:
        '''
        :param record_column_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_column_delimiter KinesisAnalyticsApplication#record_column_delimiter}.
        :param record_row_delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_delimiter KinesisAnalyticsApplication#record_row_delimiter}.
        '''
        value = KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv(
            record_column_delimiter=record_column_delimiter,
            record_row_delimiter=record_row_delimiter,
        )

        return typing.cast(None, jsii.invoke(self, "putCsv", [value]))

    @jsii.member(jsii_name="putJson")
    def put_json(self, *, record_row_path: builtins.str) -> None:
        '''
        :param record_row_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#record_row_path KinesisAnalyticsApplication#record_row_path}.
        '''
        value = KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson(
            record_row_path=record_row_path
        )

        return typing.cast(None, jsii.invoke(self, "putJson", [value]))

    @jsii.member(jsii_name="resetCsv")
    def reset_csv(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsv", []))

    @jsii.member(jsii_name="resetJson")
    def reset_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJson", []))

    @builtins.property
    @jsii.member(jsii_name="csv")
    def csv(
        self,
    ) -> KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsvOutputReference:
        return typing.cast(KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsvOutputReference, jsii.get(self, "csv"))

    @builtins.property
    @jsii.member(jsii_name="json")
    def json(
        self,
    ) -> KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJsonOutputReference:
        return typing.cast(KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJsonOutputReference, jsii.get(self, "json"))

    @builtins.property
    @jsii.member(jsii_name="csvInput")
    def csv_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv], jsii.get(self, "csvInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonInput")
    def json_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson], jsii.get(self, "jsonInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisAnalyticsApplication.KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatOutputReference",
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

    @jsii.member(jsii_name="putMappingParameters")
    def put_mapping_parameters(
        self,
        *,
        csv: typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv, typing.Dict[str, typing.Any]]] = None,
        json: typing.Optional[typing.Union[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param csv: csv block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#csv KinesisAnalyticsApplication#csv}
        :param json: json block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application#json KinesisAnalyticsApplication#json}
        '''
        value = KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters(
            csv=csv, json=json
        )

        return typing.cast(None, jsii.invoke(self, "putMappingParameters", [value]))

    @jsii.member(jsii_name="resetMappingParameters")
    def reset_mapping_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMappingParameters", []))

    @builtins.property
    @jsii.member(jsii_name="mappingParameters")
    def mapping_parameters(
        self,
    ) -> KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersOutputReference:
        return typing.cast(KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersOutputReference, jsii.get(self, "mappingParameters"))

    @builtins.property
    @jsii.member(jsii_name="recordFormatType")
    def record_format_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordFormatType"))

    @builtins.property
    @jsii.member(jsii_name="mappingParametersInput")
    def mapping_parameters_input(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters], jsii.get(self, "mappingParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat]:
        return typing.cast(typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KinesisAnalyticsApplication",
    "KinesisAnalyticsApplicationCloudwatchLoggingOptions",
    "KinesisAnalyticsApplicationCloudwatchLoggingOptionsOutputReference",
    "KinesisAnalyticsApplicationConfig",
    "KinesisAnalyticsApplicationInputs",
    "KinesisAnalyticsApplicationInputsKinesisFirehose",
    "KinesisAnalyticsApplicationInputsKinesisFirehoseOutputReference",
    "KinesisAnalyticsApplicationInputsKinesisStream",
    "KinesisAnalyticsApplicationInputsKinesisStreamOutputReference",
    "KinesisAnalyticsApplicationInputsOutputReference",
    "KinesisAnalyticsApplicationInputsParallelism",
    "KinesisAnalyticsApplicationInputsParallelismOutputReference",
    "KinesisAnalyticsApplicationInputsProcessingConfiguration",
    "KinesisAnalyticsApplicationInputsProcessingConfigurationLambda",
    "KinesisAnalyticsApplicationInputsProcessingConfigurationLambdaOutputReference",
    "KinesisAnalyticsApplicationInputsProcessingConfigurationOutputReference",
    "KinesisAnalyticsApplicationInputsSchema",
    "KinesisAnalyticsApplicationInputsSchemaOutputReference",
    "KinesisAnalyticsApplicationInputsSchemaRecordColumns",
    "KinesisAnalyticsApplicationInputsSchemaRecordColumnsList",
    "KinesisAnalyticsApplicationInputsSchemaRecordColumnsOutputReference",
    "KinesisAnalyticsApplicationInputsSchemaRecordFormat",
    "KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParameters",
    "KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv",
    "KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsvOutputReference",
    "KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson",
    "KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonOutputReference",
    "KinesisAnalyticsApplicationInputsSchemaRecordFormatMappingParametersOutputReference",
    "KinesisAnalyticsApplicationInputsSchemaRecordFormatOutputReference",
    "KinesisAnalyticsApplicationInputsStartingPositionConfiguration",
    "KinesisAnalyticsApplicationInputsStartingPositionConfigurationList",
    "KinesisAnalyticsApplicationInputsStartingPositionConfigurationOutputReference",
    "KinesisAnalyticsApplicationOutputs",
    "KinesisAnalyticsApplicationOutputsKinesisFirehose",
    "KinesisAnalyticsApplicationOutputsKinesisFirehoseOutputReference",
    "KinesisAnalyticsApplicationOutputsKinesisStream",
    "KinesisAnalyticsApplicationOutputsKinesisStreamOutputReference",
    "KinesisAnalyticsApplicationOutputsLambda",
    "KinesisAnalyticsApplicationOutputsLambdaOutputReference",
    "KinesisAnalyticsApplicationOutputsList",
    "KinesisAnalyticsApplicationOutputsOutputReference",
    "KinesisAnalyticsApplicationOutputsSchema",
    "KinesisAnalyticsApplicationOutputsSchemaOutputReference",
    "KinesisAnalyticsApplicationReferenceDataSources",
    "KinesisAnalyticsApplicationReferenceDataSourcesOutputReference",
    "KinesisAnalyticsApplicationReferenceDataSourcesS3",
    "KinesisAnalyticsApplicationReferenceDataSourcesS3OutputReference",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchema",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaOutputReference",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumns",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsList",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordColumnsOutputReference",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormat",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsvOutputReference",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJsonOutputReference",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersOutputReference",
    "KinesisAnalyticsApplicationReferenceDataSourcesSchemaRecordFormatOutputReference",
]

publication.publish()
