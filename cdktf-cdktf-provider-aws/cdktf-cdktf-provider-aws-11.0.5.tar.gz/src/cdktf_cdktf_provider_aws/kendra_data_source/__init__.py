'''
# `aws_kendra_data_source`

Refer to the Terraform Registory for docs: [`aws_kendra_data_source`](https://www.terraform.io/docs/providers/aws/r/kendra_data_source).
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


class KendraDataSource(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSource",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source aws_kendra_data_source}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        index_id: builtins.str,
        name: builtins.str,
        type: builtins.str,
        configuration: typing.Optional[typing.Union["KendraDataSourceConfiguration", typing.Dict[str, typing.Any]]] = None,
        custom_document_enrichment_configuration: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfiguration", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        language_code: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KendraDataSourceTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source aws_kendra_data_source} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param index_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#index_id KendraDataSource#index_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#name KendraDataSource#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#type KendraDataSource#type}.
        :param configuration: configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#configuration KendraDataSource#configuration}
        :param custom_document_enrichment_configuration: custom_document_enrichment_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#custom_document_enrichment_configuration KendraDataSource#custom_document_enrichment_configuration}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#description KendraDataSource#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#id KendraDataSource#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param language_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#language_code KendraDataSource#language_code}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#role_arn KendraDataSource#role_arn}.
        :param schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#schedule KendraDataSource#schedule}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#tags KendraDataSource#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#tags_all KendraDataSource#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#timeouts KendraDataSource#timeouts}
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
                index_id: builtins.str,
                name: builtins.str,
                type: builtins.str,
                configuration: typing.Optional[typing.Union[KendraDataSourceConfiguration, typing.Dict[str, typing.Any]]] = None,
                custom_document_enrichment_configuration: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfiguration, typing.Dict[str, typing.Any]]] = None,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                language_code: typing.Optional[builtins.str] = None,
                role_arn: typing.Optional[builtins.str] = None,
                schedule: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[KendraDataSourceTimeouts, typing.Dict[str, typing.Any]]] = None,
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
        config = KendraDataSourceConfig(
            index_id=index_id,
            name=name,
            type=type,
            configuration=configuration,
            custom_document_enrichment_configuration=custom_document_enrichment_configuration,
            description=description,
            id=id,
            language_code=language_code,
            role_arn=role_arn,
            schedule=schedule,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putConfiguration")
    def put_configuration(
        self,
        *,
        s3_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationS3Configuration", typing.Dict[str, typing.Any]]] = None,
        web_crawler_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_configuration: s3_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_configuration KendraDataSource#s3_configuration}
        :param web_crawler_configuration: web_crawler_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#web_crawler_configuration KendraDataSource#web_crawler_configuration}
        '''
        value = KendraDataSourceConfiguration(
            s3_configuration=s3_configuration,
            web_crawler_configuration=web_crawler_configuration,
        )

        return typing.cast(None, jsii.invoke(self, "putConfiguration", [value]))

    @jsii.member(jsii_name="putCustomDocumentEnrichmentConfiguration")
    def put_custom_document_enrichment_configuration(
        self,
        *,
        inline_configurations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations", typing.Dict[str, typing.Any]]]]] = None,
        post_extraction_hook_configuration: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration", typing.Dict[str, typing.Any]]] = None,
        pre_extraction_hook_configuration: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration", typing.Dict[str, typing.Any]]] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param inline_configurations: inline_configurations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#inline_configurations KendraDataSource#inline_configurations}
        :param post_extraction_hook_configuration: post_extraction_hook_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#post_extraction_hook_configuration KendraDataSource#post_extraction_hook_configuration}
        :param pre_extraction_hook_configuration: pre_extraction_hook_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#pre_extraction_hook_configuration KendraDataSource#pre_extraction_hook_configuration}
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#role_arn KendraDataSource#role_arn}.
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfiguration(
            inline_configurations=inline_configurations,
            post_extraction_hook_configuration=post_extraction_hook_configuration,
            pre_extraction_hook_configuration=pre_extraction_hook_configuration,
            role_arn=role_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomDocumentEnrichmentConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#create KendraDataSource#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#delete KendraDataSource#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#update KendraDataSource#update}.
        '''
        value = KendraDataSourceTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetConfiguration")
    def reset_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfiguration", []))

    @jsii.member(jsii_name="resetCustomDocumentEnrichmentConfiguration")
    def reset_custom_document_enrichment_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomDocumentEnrichmentConfiguration", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLanguageCode")
    def reset_language_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLanguageCode", []))

    @jsii.member(jsii_name="resetRoleArn")
    def reset_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleArn", []))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

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
    @jsii.member(jsii_name="configuration")
    def configuration(self) -> "KendraDataSourceConfigurationOutputReference":
        return typing.cast("KendraDataSourceConfigurationOutputReference", jsii.get(self, "configuration"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="customDocumentEnrichmentConfiguration")
    def custom_document_enrichment_configuration(
        self,
    ) -> "KendraDataSourceCustomDocumentEnrichmentConfigurationOutputReference":
        return typing.cast("KendraDataSourceCustomDocumentEnrichmentConfigurationOutputReference", jsii.get(self, "customDocumentEnrichmentConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceId")
    def data_source_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSourceId"))

    @builtins.property
    @jsii.member(jsii_name="errorMessage")
    def error_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorMessage"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "KendraDataSourceTimeoutsOutputReference":
        return typing.cast("KendraDataSourceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updatedAt")
    def updated_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedAt"))

    @builtins.property
    @jsii.member(jsii_name="configurationInput")
    def configuration_input(self) -> typing.Optional["KendraDataSourceConfiguration"]:
        return typing.cast(typing.Optional["KendraDataSourceConfiguration"], jsii.get(self, "configurationInput"))

    @builtins.property
    @jsii.member(jsii_name="customDocumentEnrichmentConfigurationInput")
    def custom_document_enrichment_configuration_input(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfiguration"]:
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfiguration"], jsii.get(self, "customDocumentEnrichmentConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="indexIdInput")
    def index_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "indexIdInput"))

    @builtins.property
    @jsii.member(jsii_name="languageCodeInput")
    def language_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "languageCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleInput"))

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
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["KendraDataSourceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["KendraDataSourceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

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
    @jsii.member(jsii_name="indexId")
    def index_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "indexId"))

    @index_id.setter
    def index_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexId", value)

    @builtins.property
    @jsii.member(jsii_name="languageCode")
    def language_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "languageCode"))

    @language_code.setter
    def language_code(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "languageCode", value)

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
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

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


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "index_id": "indexId",
        "name": "name",
        "type": "type",
        "configuration": "configuration",
        "custom_document_enrichment_configuration": "customDocumentEnrichmentConfiguration",
        "description": "description",
        "id": "id",
        "language_code": "languageCode",
        "role_arn": "roleArn",
        "schedule": "schedule",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class KendraDataSourceConfig(cdktf.TerraformMetaArguments):
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
        index_id: builtins.str,
        name: builtins.str,
        type: builtins.str,
        configuration: typing.Optional[typing.Union["KendraDataSourceConfiguration", typing.Dict[str, typing.Any]]] = None,
        custom_document_enrichment_configuration: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfiguration", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        language_code: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KendraDataSourceTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param index_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#index_id KendraDataSource#index_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#name KendraDataSource#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#type KendraDataSource#type}.
        :param configuration: configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#configuration KendraDataSource#configuration}
        :param custom_document_enrichment_configuration: custom_document_enrichment_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#custom_document_enrichment_configuration KendraDataSource#custom_document_enrichment_configuration}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#description KendraDataSource#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#id KendraDataSource#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param language_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#language_code KendraDataSource#language_code}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#role_arn KendraDataSource#role_arn}.
        :param schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#schedule KendraDataSource#schedule}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#tags KendraDataSource#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#tags_all KendraDataSource#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#timeouts KendraDataSource#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(configuration, dict):
            configuration = KendraDataSourceConfiguration(**configuration)
        if isinstance(custom_document_enrichment_configuration, dict):
            custom_document_enrichment_configuration = KendraDataSourceCustomDocumentEnrichmentConfiguration(**custom_document_enrichment_configuration)
        if isinstance(timeouts, dict):
            timeouts = KendraDataSourceTimeouts(**timeouts)
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
                index_id: builtins.str,
                name: builtins.str,
                type: builtins.str,
                configuration: typing.Optional[typing.Union[KendraDataSourceConfiguration, typing.Dict[str, typing.Any]]] = None,
                custom_document_enrichment_configuration: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfiguration, typing.Dict[str, typing.Any]]] = None,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                language_code: typing.Optional[builtins.str] = None,
                role_arn: typing.Optional[builtins.str] = None,
                schedule: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[KendraDataSourceTimeouts, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument index_id", value=index_id, expected_type=type_hints["index_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument custom_document_enrichment_configuration", value=custom_document_enrichment_configuration, expected_type=type_hints["custom_document_enrichment_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument language_code", value=language_code, expected_type=type_hints["language_code"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "index_id": index_id,
            "name": name,
            "type": type,
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
        if configuration is not None:
            self._values["configuration"] = configuration
        if custom_document_enrichment_configuration is not None:
            self._values["custom_document_enrichment_configuration"] = custom_document_enrichment_configuration
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if language_code is not None:
            self._values["language_code"] = language_code
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if schedule is not None:
            self._values["schedule"] = schedule
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def index_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#index_id KendraDataSource#index_id}.'''
        result = self._values.get("index_id")
        assert result is not None, "Required property 'index_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#name KendraDataSource#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#type KendraDataSource#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration(self) -> typing.Optional["KendraDataSourceConfiguration"]:
        '''configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#configuration KendraDataSource#configuration}
        '''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional["KendraDataSourceConfiguration"], result)

    @builtins.property
    def custom_document_enrichment_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfiguration"]:
        '''custom_document_enrichment_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#custom_document_enrichment_configuration KendraDataSource#custom_document_enrichment_configuration}
        '''
        result = self._values.get("custom_document_enrichment_configuration")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfiguration"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#description KendraDataSource#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#id KendraDataSource#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def language_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#language_code KendraDataSource#language_code}.'''
        result = self._values.get("language_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#role_arn KendraDataSource#role_arn}.'''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#schedule KendraDataSource#schedule}.'''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#tags KendraDataSource#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#tags_all KendraDataSource#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["KendraDataSourceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#timeouts KendraDataSource#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["KendraDataSourceTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "s3_configuration": "s3Configuration",
        "web_crawler_configuration": "webCrawlerConfiguration",
    },
)
class KendraDataSourceConfiguration:
    def __init__(
        self,
        *,
        s3_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationS3Configuration", typing.Dict[str, typing.Any]]] = None,
        web_crawler_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_configuration: s3_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_configuration KendraDataSource#s3_configuration}
        :param web_crawler_configuration: web_crawler_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#web_crawler_configuration KendraDataSource#web_crawler_configuration}
        '''
        if isinstance(s3_configuration, dict):
            s3_configuration = KendraDataSourceConfigurationS3Configuration(**s3_configuration)
        if isinstance(web_crawler_configuration, dict):
            web_crawler_configuration = KendraDataSourceConfigurationWebCrawlerConfiguration(**web_crawler_configuration)
        if __debug__:
            def stub(
                *,
                s3_configuration: typing.Optional[typing.Union[KendraDataSourceConfigurationS3Configuration, typing.Dict[str, typing.Any]]] = None,
                web_crawler_configuration: typing.Optional[typing.Union[KendraDataSourceConfigurationWebCrawlerConfiguration, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
            check_type(argname="argument web_crawler_configuration", value=web_crawler_configuration, expected_type=type_hints["web_crawler_configuration"])
        self._values: typing.Dict[str, typing.Any] = {}
        if s3_configuration is not None:
            self._values["s3_configuration"] = s3_configuration
        if web_crawler_configuration is not None:
            self._values["web_crawler_configuration"] = web_crawler_configuration

    @builtins.property
    def s3_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationS3Configuration"]:
        '''s3_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_configuration KendraDataSource#s3_configuration}
        '''
        result = self._values.get("s3_configuration")
        return typing.cast(typing.Optional["KendraDataSourceConfigurationS3Configuration"], result)

    @builtins.property
    def web_crawler_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfiguration"]:
        '''web_crawler_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#web_crawler_configuration KendraDataSource#web_crawler_configuration}
        '''
        result = self._values.get("web_crawler_configuration")
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationOutputReference",
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

    @jsii.member(jsii_name="putS3Configuration")
    def put_s3_configuration(
        self,
        *,
        bucket_name: builtins.str,
        access_control_list_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration", typing.Dict[str, typing.Any]]] = None,
        documents_metadata_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration", typing.Dict[str, typing.Any]]] = None,
        exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        inclusion_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#bucket_name KendraDataSource#bucket_name}.
        :param access_control_list_configuration: access_control_list_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#access_control_list_configuration KendraDataSource#access_control_list_configuration}
        :param documents_metadata_configuration: documents_metadata_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#documents_metadata_configuration KendraDataSource#documents_metadata_configuration}
        :param exclusion_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#exclusion_patterns KendraDataSource#exclusion_patterns}.
        :param inclusion_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#inclusion_patterns KendraDataSource#inclusion_patterns}.
        :param inclusion_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#inclusion_prefixes KendraDataSource#inclusion_prefixes}.
        '''
        value = KendraDataSourceConfigurationS3Configuration(
            bucket_name=bucket_name,
            access_control_list_configuration=access_control_list_configuration,
            documents_metadata_configuration=documents_metadata_configuration,
            exclusion_patterns=exclusion_patterns,
            inclusion_patterns=inclusion_patterns,
            inclusion_prefixes=inclusion_prefixes,
        )

        return typing.cast(None, jsii.invoke(self, "putS3Configuration", [value]))

    @jsii.member(jsii_name="putWebCrawlerConfiguration")
    def put_web_crawler_configuration(
        self,
        *,
        urls: typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationUrls", typing.Dict[str, typing.Any]],
        authentication_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration", typing.Dict[str, typing.Any]]] = None,
        crawl_depth: typing.Optional[jsii.Number] = None,
        max_content_size_per_page_in_mega_bytes: typing.Optional[jsii.Number] = None,
        max_links_per_page: typing.Optional[jsii.Number] = None,
        max_urls_per_minute_crawl_rate: typing.Optional[jsii.Number] = None,
        proxy_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration", typing.Dict[str, typing.Any]]] = None,
        url_exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        url_inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param urls: urls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#urls KendraDataSource#urls}
        :param authentication_configuration: authentication_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#authentication_configuration KendraDataSource#authentication_configuration}
        :param crawl_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#crawl_depth KendraDataSource#crawl_depth}.
        :param max_content_size_per_page_in_mega_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#max_content_size_per_page_in_mega_bytes KendraDataSource#max_content_size_per_page_in_mega_bytes}.
        :param max_links_per_page: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#max_links_per_page KendraDataSource#max_links_per_page}.
        :param max_urls_per_minute_crawl_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#max_urls_per_minute_crawl_rate KendraDataSource#max_urls_per_minute_crawl_rate}.
        :param proxy_configuration: proxy_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#proxy_configuration KendraDataSource#proxy_configuration}
        :param url_exclusion_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#url_exclusion_patterns KendraDataSource#url_exclusion_patterns}.
        :param url_inclusion_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#url_inclusion_patterns KendraDataSource#url_inclusion_patterns}.
        '''
        value = KendraDataSourceConfigurationWebCrawlerConfiguration(
            urls=urls,
            authentication_configuration=authentication_configuration,
            crawl_depth=crawl_depth,
            max_content_size_per_page_in_mega_bytes=max_content_size_per_page_in_mega_bytes,
            max_links_per_page=max_links_per_page,
            max_urls_per_minute_crawl_rate=max_urls_per_minute_crawl_rate,
            proxy_configuration=proxy_configuration,
            url_exclusion_patterns=url_exclusion_patterns,
            url_inclusion_patterns=url_inclusion_patterns,
        )

        return typing.cast(None, jsii.invoke(self, "putWebCrawlerConfiguration", [value]))

    @jsii.member(jsii_name="resetS3Configuration")
    def reset_s3_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Configuration", []))

    @jsii.member(jsii_name="resetWebCrawlerConfiguration")
    def reset_web_crawler_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebCrawlerConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="s3Configuration")
    def s3_configuration(
        self,
    ) -> "KendraDataSourceConfigurationS3ConfigurationOutputReference":
        return typing.cast("KendraDataSourceConfigurationS3ConfigurationOutputReference", jsii.get(self, "s3Configuration"))

    @builtins.property
    @jsii.member(jsii_name="webCrawlerConfiguration")
    def web_crawler_configuration(
        self,
    ) -> "KendraDataSourceConfigurationWebCrawlerConfigurationOutputReference":
        return typing.cast("KendraDataSourceConfigurationWebCrawlerConfigurationOutputReference", jsii.get(self, "webCrawlerConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="s3ConfigurationInput")
    def s3_configuration_input(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationS3Configuration"]:
        return typing.cast(typing.Optional["KendraDataSourceConfigurationS3Configuration"], jsii.get(self, "s3ConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="webCrawlerConfigurationInput")
    def web_crawler_configuration_input(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfiguration"]:
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfiguration"], jsii.get(self, "webCrawlerConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KendraDataSourceConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfiguration],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[KendraDataSourceConfiguration]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationS3Configuration",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "access_control_list_configuration": "accessControlListConfiguration",
        "documents_metadata_configuration": "documentsMetadataConfiguration",
        "exclusion_patterns": "exclusionPatterns",
        "inclusion_patterns": "inclusionPatterns",
        "inclusion_prefixes": "inclusionPrefixes",
    },
)
class KendraDataSourceConfigurationS3Configuration:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        access_control_list_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration", typing.Dict[str, typing.Any]]] = None,
        documents_metadata_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration", typing.Dict[str, typing.Any]]] = None,
        exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        inclusion_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#bucket_name KendraDataSource#bucket_name}.
        :param access_control_list_configuration: access_control_list_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#access_control_list_configuration KendraDataSource#access_control_list_configuration}
        :param documents_metadata_configuration: documents_metadata_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#documents_metadata_configuration KendraDataSource#documents_metadata_configuration}
        :param exclusion_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#exclusion_patterns KendraDataSource#exclusion_patterns}.
        :param inclusion_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#inclusion_patterns KendraDataSource#inclusion_patterns}.
        :param inclusion_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#inclusion_prefixes KendraDataSource#inclusion_prefixes}.
        '''
        if isinstance(access_control_list_configuration, dict):
            access_control_list_configuration = KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration(**access_control_list_configuration)
        if isinstance(documents_metadata_configuration, dict):
            documents_metadata_configuration = KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration(**documents_metadata_configuration)
        if __debug__:
            def stub(
                *,
                bucket_name: builtins.str,
                access_control_list_configuration: typing.Optional[typing.Union[KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration, typing.Dict[str, typing.Any]]] = None,
                documents_metadata_configuration: typing.Optional[typing.Union[KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration, typing.Dict[str, typing.Any]]] = None,
                exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
                inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
                inclusion_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument access_control_list_configuration", value=access_control_list_configuration, expected_type=type_hints["access_control_list_configuration"])
            check_type(argname="argument documents_metadata_configuration", value=documents_metadata_configuration, expected_type=type_hints["documents_metadata_configuration"])
            check_type(argname="argument exclusion_patterns", value=exclusion_patterns, expected_type=type_hints["exclusion_patterns"])
            check_type(argname="argument inclusion_patterns", value=inclusion_patterns, expected_type=type_hints["inclusion_patterns"])
            check_type(argname="argument inclusion_prefixes", value=inclusion_prefixes, expected_type=type_hints["inclusion_prefixes"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
        }
        if access_control_list_configuration is not None:
            self._values["access_control_list_configuration"] = access_control_list_configuration
        if documents_metadata_configuration is not None:
            self._values["documents_metadata_configuration"] = documents_metadata_configuration
        if exclusion_patterns is not None:
            self._values["exclusion_patterns"] = exclusion_patterns
        if inclusion_patterns is not None:
            self._values["inclusion_patterns"] = inclusion_patterns
        if inclusion_prefixes is not None:
            self._values["inclusion_prefixes"] = inclusion_prefixes

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#bucket_name KendraDataSource#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_control_list_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration"]:
        '''access_control_list_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#access_control_list_configuration KendraDataSource#access_control_list_configuration}
        '''
        result = self._values.get("access_control_list_configuration")
        return typing.cast(typing.Optional["KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration"], result)

    @builtins.property
    def documents_metadata_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration"]:
        '''documents_metadata_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#documents_metadata_configuration KendraDataSource#documents_metadata_configuration}
        '''
        result = self._values.get("documents_metadata_configuration")
        return typing.cast(typing.Optional["KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration"], result)

    @builtins.property
    def exclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#exclusion_patterns KendraDataSource#exclusion_patterns}.'''
        result = self._values.get("exclusion_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def inclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#inclusion_patterns KendraDataSource#inclusion_patterns}.'''
        result = self._values.get("inclusion_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def inclusion_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#inclusion_prefixes KendraDataSource#inclusion_prefixes}.'''
        result = self._values.get("inclusion_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationS3Configuration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration",
    jsii_struct_bases=[],
    name_mapping={"key_path": "keyPath"},
)
class KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration:
    def __init__(self, *, key_path: typing.Optional[builtins.str] = None) -> None:
        '''
        :param key_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#key_path KendraDataSource#key_path}.
        '''
        if __debug__:
            def stub(*, key_path: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key_path", value=key_path, expected_type=type_hints["key_path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key_path is not None:
            self._values["key_path"] = key_path

    @builtins.property
    def key_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#key_path KendraDataSource#key_path}.'''
        result = self._values.get("key_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceConfigurationS3ConfigurationAccessControlListConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationS3ConfigurationAccessControlListConfigurationOutputReference",
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

    @jsii.member(jsii_name="resetKeyPath")
    def reset_key_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyPath", []))

    @builtins.property
    @jsii.member(jsii_name="keyPathInput")
    def key_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyPathInput"))

    @builtins.property
    @jsii.member(jsii_name="keyPath")
    def key_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyPath"))

    @key_path.setter
    def key_path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration",
    jsii_struct_bases=[],
    name_mapping={"s3_prefix": "s3Prefix"},
)
class KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration:
    def __init__(self, *, s3_prefix: typing.Optional[builtins.str] = None) -> None:
        '''
        :param s3_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_prefix KendraDataSource#s3_prefix}.
        '''
        if __debug__:
            def stub(*, s3_prefix: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument s3_prefix", value=s3_prefix, expected_type=type_hints["s3_prefix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if s3_prefix is not None:
            self._values["s3_prefix"] = s3_prefix

    @builtins.property
    def s3_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_prefix KendraDataSource#s3_prefix}.'''
        result = self._values.get("s3_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationOutputReference",
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

    @jsii.member(jsii_name="resetS3Prefix")
    def reset_s3_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Prefix", []))

    @builtins.property
    @jsii.member(jsii_name="s3PrefixInput")
    def s3_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3PrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Prefix")
    def s3_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Prefix"))

    @s3_prefix.setter
    def s3_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Prefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceConfigurationS3ConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationS3ConfigurationOutputReference",
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

    @jsii.member(jsii_name="putAccessControlListConfiguration")
    def put_access_control_list_configuration(
        self,
        *,
        key_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#key_path KendraDataSource#key_path}.
        '''
        value = KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration(
            key_path=key_path
        )

        return typing.cast(None, jsii.invoke(self, "putAccessControlListConfiguration", [value]))

    @jsii.member(jsii_name="putDocumentsMetadataConfiguration")
    def put_documents_metadata_configuration(
        self,
        *,
        s3_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_prefix KendraDataSource#s3_prefix}.
        '''
        value = KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration(
            s3_prefix=s3_prefix
        )

        return typing.cast(None, jsii.invoke(self, "putDocumentsMetadataConfiguration", [value]))

    @jsii.member(jsii_name="resetAccessControlListConfiguration")
    def reset_access_control_list_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessControlListConfiguration", []))

    @jsii.member(jsii_name="resetDocumentsMetadataConfiguration")
    def reset_documents_metadata_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentsMetadataConfiguration", []))

    @jsii.member(jsii_name="resetExclusionPatterns")
    def reset_exclusion_patterns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusionPatterns", []))

    @jsii.member(jsii_name="resetInclusionPatterns")
    def reset_inclusion_patterns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInclusionPatterns", []))

    @jsii.member(jsii_name="resetInclusionPrefixes")
    def reset_inclusion_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInclusionPrefixes", []))

    @builtins.property
    @jsii.member(jsii_name="accessControlListConfiguration")
    def access_control_list_configuration(
        self,
    ) -> KendraDataSourceConfigurationS3ConfigurationAccessControlListConfigurationOutputReference:
        return typing.cast(KendraDataSourceConfigurationS3ConfigurationAccessControlListConfigurationOutputReference, jsii.get(self, "accessControlListConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="documentsMetadataConfiguration")
    def documents_metadata_configuration(
        self,
    ) -> KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationOutputReference:
        return typing.cast(KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationOutputReference, jsii.get(self, "documentsMetadataConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="accessControlListConfigurationInput")
    def access_control_list_configuration_input(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration], jsii.get(self, "accessControlListConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="documentsMetadataConfigurationInput")
    def documents_metadata_configuration_input(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration], jsii.get(self, "documentsMetadataConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusionPatternsInput")
    def exclusion_patterns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exclusionPatternsInput"))

    @builtins.property
    @jsii.member(jsii_name="inclusionPatternsInput")
    def inclusion_patterns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "inclusionPatternsInput"))

    @builtins.property
    @jsii.member(jsii_name="inclusionPrefixesInput")
    def inclusion_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "inclusionPrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="exclusionPatterns")
    def exclusion_patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclusionPatterns"))

    @exclusion_patterns.setter
    def exclusion_patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusionPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="inclusionPatterns")
    def inclusion_patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "inclusionPatterns"))

    @inclusion_patterns.setter
    def inclusion_patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inclusionPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="inclusionPrefixes")
    def inclusion_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "inclusionPrefixes"))

    @inclusion_prefixes.setter
    def inclusion_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inclusionPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationS3Configuration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationS3Configuration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfigurationS3Configuration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceConfigurationS3Configuration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "urls": "urls",
        "authentication_configuration": "authenticationConfiguration",
        "crawl_depth": "crawlDepth",
        "max_content_size_per_page_in_mega_bytes": "maxContentSizePerPageInMegaBytes",
        "max_links_per_page": "maxLinksPerPage",
        "max_urls_per_minute_crawl_rate": "maxUrlsPerMinuteCrawlRate",
        "proxy_configuration": "proxyConfiguration",
        "url_exclusion_patterns": "urlExclusionPatterns",
        "url_inclusion_patterns": "urlInclusionPatterns",
    },
)
class KendraDataSourceConfigurationWebCrawlerConfiguration:
    def __init__(
        self,
        *,
        urls: typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationUrls", typing.Dict[str, typing.Any]],
        authentication_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration", typing.Dict[str, typing.Any]]] = None,
        crawl_depth: typing.Optional[jsii.Number] = None,
        max_content_size_per_page_in_mega_bytes: typing.Optional[jsii.Number] = None,
        max_links_per_page: typing.Optional[jsii.Number] = None,
        max_urls_per_minute_crawl_rate: typing.Optional[jsii.Number] = None,
        proxy_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration", typing.Dict[str, typing.Any]]] = None,
        url_exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        url_inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param urls: urls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#urls KendraDataSource#urls}
        :param authentication_configuration: authentication_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#authentication_configuration KendraDataSource#authentication_configuration}
        :param crawl_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#crawl_depth KendraDataSource#crawl_depth}.
        :param max_content_size_per_page_in_mega_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#max_content_size_per_page_in_mega_bytes KendraDataSource#max_content_size_per_page_in_mega_bytes}.
        :param max_links_per_page: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#max_links_per_page KendraDataSource#max_links_per_page}.
        :param max_urls_per_minute_crawl_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#max_urls_per_minute_crawl_rate KendraDataSource#max_urls_per_minute_crawl_rate}.
        :param proxy_configuration: proxy_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#proxy_configuration KendraDataSource#proxy_configuration}
        :param url_exclusion_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#url_exclusion_patterns KendraDataSource#url_exclusion_patterns}.
        :param url_inclusion_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#url_inclusion_patterns KendraDataSource#url_inclusion_patterns}.
        '''
        if isinstance(urls, dict):
            urls = KendraDataSourceConfigurationWebCrawlerConfigurationUrls(**urls)
        if isinstance(authentication_configuration, dict):
            authentication_configuration = KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration(**authentication_configuration)
        if isinstance(proxy_configuration, dict):
            proxy_configuration = KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration(**proxy_configuration)
        if __debug__:
            def stub(
                *,
                urls: typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationUrls, typing.Dict[str, typing.Any]],
                authentication_configuration: typing.Optional[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration, typing.Dict[str, typing.Any]]] = None,
                crawl_depth: typing.Optional[jsii.Number] = None,
                max_content_size_per_page_in_mega_bytes: typing.Optional[jsii.Number] = None,
                max_links_per_page: typing.Optional[jsii.Number] = None,
                max_urls_per_minute_crawl_rate: typing.Optional[jsii.Number] = None,
                proxy_configuration: typing.Optional[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration, typing.Dict[str, typing.Any]]] = None,
                url_exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
                url_inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument urls", value=urls, expected_type=type_hints["urls"])
            check_type(argname="argument authentication_configuration", value=authentication_configuration, expected_type=type_hints["authentication_configuration"])
            check_type(argname="argument crawl_depth", value=crawl_depth, expected_type=type_hints["crawl_depth"])
            check_type(argname="argument max_content_size_per_page_in_mega_bytes", value=max_content_size_per_page_in_mega_bytes, expected_type=type_hints["max_content_size_per_page_in_mega_bytes"])
            check_type(argname="argument max_links_per_page", value=max_links_per_page, expected_type=type_hints["max_links_per_page"])
            check_type(argname="argument max_urls_per_minute_crawl_rate", value=max_urls_per_minute_crawl_rate, expected_type=type_hints["max_urls_per_minute_crawl_rate"])
            check_type(argname="argument proxy_configuration", value=proxy_configuration, expected_type=type_hints["proxy_configuration"])
            check_type(argname="argument url_exclusion_patterns", value=url_exclusion_patterns, expected_type=type_hints["url_exclusion_patterns"])
            check_type(argname="argument url_inclusion_patterns", value=url_inclusion_patterns, expected_type=type_hints["url_inclusion_patterns"])
        self._values: typing.Dict[str, typing.Any] = {
            "urls": urls,
        }
        if authentication_configuration is not None:
            self._values["authentication_configuration"] = authentication_configuration
        if crawl_depth is not None:
            self._values["crawl_depth"] = crawl_depth
        if max_content_size_per_page_in_mega_bytes is not None:
            self._values["max_content_size_per_page_in_mega_bytes"] = max_content_size_per_page_in_mega_bytes
        if max_links_per_page is not None:
            self._values["max_links_per_page"] = max_links_per_page
        if max_urls_per_minute_crawl_rate is not None:
            self._values["max_urls_per_minute_crawl_rate"] = max_urls_per_minute_crawl_rate
        if proxy_configuration is not None:
            self._values["proxy_configuration"] = proxy_configuration
        if url_exclusion_patterns is not None:
            self._values["url_exclusion_patterns"] = url_exclusion_patterns
        if url_inclusion_patterns is not None:
            self._values["url_inclusion_patterns"] = url_inclusion_patterns

    @builtins.property
    def urls(self) -> "KendraDataSourceConfigurationWebCrawlerConfigurationUrls":
        '''urls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#urls KendraDataSource#urls}
        '''
        result = self._values.get("urls")
        assert result is not None, "Required property 'urls' is missing"
        return typing.cast("KendraDataSourceConfigurationWebCrawlerConfigurationUrls", result)

    @builtins.property
    def authentication_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration"]:
        '''authentication_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#authentication_configuration KendraDataSource#authentication_configuration}
        '''
        result = self._values.get("authentication_configuration")
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration"], result)

    @builtins.property
    def crawl_depth(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#crawl_depth KendraDataSource#crawl_depth}.'''
        result = self._values.get("crawl_depth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_content_size_per_page_in_mega_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#max_content_size_per_page_in_mega_bytes KendraDataSource#max_content_size_per_page_in_mega_bytes}.'''
        result = self._values.get("max_content_size_per_page_in_mega_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_links_per_page(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#max_links_per_page KendraDataSource#max_links_per_page}.'''
        result = self._values.get("max_links_per_page")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_urls_per_minute_crawl_rate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#max_urls_per_minute_crawl_rate KendraDataSource#max_urls_per_minute_crawl_rate}.'''
        result = self._values.get("max_urls_per_minute_crawl_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def proxy_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration"]:
        '''proxy_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#proxy_configuration KendraDataSource#proxy_configuration}
        '''
        result = self._values.get("proxy_configuration")
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration"], result)

    @builtins.property
    def url_exclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#url_exclusion_patterns KendraDataSource#url_exclusion_patterns}.'''
        result = self._values.get("url_exclusion_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def url_inclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#url_inclusion_patterns KendraDataSource#url_inclusion_patterns}.'''
        result = self._values.get("url_inclusion_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationWebCrawlerConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration",
    jsii_struct_bases=[],
    name_mapping={"basic_authentication": "basicAuthentication"},
)
class KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration:
    def __init__(
        self,
        *,
        basic_authentication: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param basic_authentication: basic_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#basic_authentication KendraDataSource#basic_authentication}
        '''
        if __debug__:
            def stub(
                *,
                basic_authentication: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument basic_authentication", value=basic_authentication, expected_type=type_hints["basic_authentication"])
        self._values: typing.Dict[str, typing.Any] = {}
        if basic_authentication is not None:
            self._values["basic_authentication"] = basic_authentication

    @builtins.property
    def basic_authentication(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication"]]]:
        '''basic_authentication block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#basic_authentication KendraDataSource#basic_authentication}
        '''
        result = self._values.get("basic_authentication")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication",
    jsii_struct_bases=[],
    name_mapping={"credentials": "credentials", "host": "host", "port": "port"},
)
class KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication:
    def __init__(
        self,
        *,
        credentials: builtins.str,
        host: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''
        :param credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#credentials KendraDataSource#credentials}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#host KendraDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#port KendraDataSource#port}.
        '''
        if __debug__:
            def stub(
                *,
                credentials: builtins.str,
                host: builtins.str,
                port: jsii.Number,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[str, typing.Any] = {
            "credentials": credentials,
            "host": host,
            "port": port,
        }

    @builtins.property
    def credentials(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#credentials KendraDataSource#credentials}.'''
        result = self._values.get("credentials")
        assert result is not None, "Required property 'credentials' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#host KendraDataSource#host}.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#port KendraDataSource#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationList",
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
    ) -> "KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationOutputReference",
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
    @jsii.member(jsii_name="credentialsInput")
    def credentials_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="credentials")
    def credentials(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentials"))

    @credentials.setter
    def credentials(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentials", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

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
    ) -> typing.Optional[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationOutputReference",
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

    @jsii.member(jsii_name="putBasicAuthentication")
    def put_basic_authentication(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBasicAuthentication", [value]))

    @jsii.member(jsii_name="resetBasicAuthentication")
    def reset_basic_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuthentication", []))

    @builtins.property
    @jsii.member(jsii_name="basicAuthentication")
    def basic_authentication(
        self,
    ) -> KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationList:
        return typing.cast(KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationList, jsii.get(self, "basicAuthentication"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthenticationInput")
    def basic_authentication_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication]]], jsii.get(self, "basicAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceConfigurationWebCrawlerConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationOutputReference",
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

    @jsii.member(jsii_name="putAuthenticationConfiguration")
    def put_authentication_configuration(
        self,
        *,
        basic_authentication: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param basic_authentication: basic_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#basic_authentication KendraDataSource#basic_authentication}
        '''
        value = KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration(
            basic_authentication=basic_authentication
        )

        return typing.cast(None, jsii.invoke(self, "putAuthenticationConfiguration", [value]))

    @jsii.member(jsii_name="putProxyConfiguration")
    def put_proxy_configuration(
        self,
        *,
        host: builtins.str,
        port: jsii.Number,
        credentials: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#host KendraDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#port KendraDataSource#port}.
        :param credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#credentials KendraDataSource#credentials}.
        '''
        value = KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration(
            host=host, port=port, credentials=credentials
        )

        return typing.cast(None, jsii.invoke(self, "putProxyConfiguration", [value]))

    @jsii.member(jsii_name="putUrls")
    def put_urls(
        self,
        *,
        seed_url_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration", typing.Dict[str, typing.Any]]] = None,
        site_maps_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param seed_url_configuration: seed_url_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#seed_url_configuration KendraDataSource#seed_url_configuration}
        :param site_maps_configuration: site_maps_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#site_maps_configuration KendraDataSource#site_maps_configuration}
        '''
        value = KendraDataSourceConfigurationWebCrawlerConfigurationUrls(
            seed_url_configuration=seed_url_configuration,
            site_maps_configuration=site_maps_configuration,
        )

        return typing.cast(None, jsii.invoke(self, "putUrls", [value]))

    @jsii.member(jsii_name="resetAuthenticationConfiguration")
    def reset_authentication_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationConfiguration", []))

    @jsii.member(jsii_name="resetCrawlDepth")
    def reset_crawl_depth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrawlDepth", []))

    @jsii.member(jsii_name="resetMaxContentSizePerPageInMegaBytes")
    def reset_max_content_size_per_page_in_mega_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxContentSizePerPageInMegaBytes", []))

    @jsii.member(jsii_name="resetMaxLinksPerPage")
    def reset_max_links_per_page(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxLinksPerPage", []))

    @jsii.member(jsii_name="resetMaxUrlsPerMinuteCrawlRate")
    def reset_max_urls_per_minute_crawl_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxUrlsPerMinuteCrawlRate", []))

    @jsii.member(jsii_name="resetProxyConfiguration")
    def reset_proxy_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyConfiguration", []))

    @jsii.member(jsii_name="resetUrlExclusionPatterns")
    def reset_url_exclusion_patterns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlExclusionPatterns", []))

    @jsii.member(jsii_name="resetUrlInclusionPatterns")
    def reset_url_inclusion_patterns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlInclusionPatterns", []))

    @builtins.property
    @jsii.member(jsii_name="authenticationConfiguration")
    def authentication_configuration(
        self,
    ) -> KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationOutputReference:
        return typing.cast(KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationOutputReference, jsii.get(self, "authenticationConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="proxyConfiguration")
    def proxy_configuration(
        self,
    ) -> "KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfigurationOutputReference":
        return typing.cast("KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfigurationOutputReference", jsii.get(self, "proxyConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="urls")
    def urls(
        self,
    ) -> "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsOutputReference":
        return typing.cast("KendraDataSourceConfigurationWebCrawlerConfigurationUrlsOutputReference", jsii.get(self, "urls"))

    @builtins.property
    @jsii.member(jsii_name="authenticationConfigurationInput")
    def authentication_configuration_input(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration], jsii.get(self, "authenticationConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="crawlDepthInput")
    def crawl_depth_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "crawlDepthInput"))

    @builtins.property
    @jsii.member(jsii_name="maxContentSizePerPageInMegaBytesInput")
    def max_content_size_per_page_in_mega_bytes_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxContentSizePerPageInMegaBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="maxLinksPerPageInput")
    def max_links_per_page_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxLinksPerPageInput"))

    @builtins.property
    @jsii.member(jsii_name="maxUrlsPerMinuteCrawlRateInput")
    def max_urls_per_minute_crawl_rate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxUrlsPerMinuteCrawlRateInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyConfigurationInput")
    def proxy_configuration_input(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration"]:
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration"], jsii.get(self, "proxyConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="urlExclusionPatternsInput")
    def url_exclusion_patterns_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "urlExclusionPatternsInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInclusionPatternsInput")
    def url_inclusion_patterns_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "urlInclusionPatternsInput"))

    @builtins.property
    @jsii.member(jsii_name="urlsInput")
    def urls_input(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrls"]:
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrls"], jsii.get(self, "urlsInput"))

    @builtins.property
    @jsii.member(jsii_name="crawlDepth")
    def crawl_depth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "crawlDepth"))

    @crawl_depth.setter
    def crawl_depth(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crawlDepth", value)

    @builtins.property
    @jsii.member(jsii_name="maxContentSizePerPageInMegaBytes")
    def max_content_size_per_page_in_mega_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxContentSizePerPageInMegaBytes"))

    @max_content_size_per_page_in_mega_bytes.setter
    def max_content_size_per_page_in_mega_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxContentSizePerPageInMegaBytes", value)

    @builtins.property
    @jsii.member(jsii_name="maxLinksPerPage")
    def max_links_per_page(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxLinksPerPage"))

    @max_links_per_page.setter
    def max_links_per_page(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxLinksPerPage", value)

    @builtins.property
    @jsii.member(jsii_name="maxUrlsPerMinuteCrawlRate")
    def max_urls_per_minute_crawl_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUrlsPerMinuteCrawlRate"))

    @max_urls_per_minute_crawl_rate.setter
    def max_urls_per_minute_crawl_rate(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUrlsPerMinuteCrawlRate", value)

    @builtins.property
    @jsii.member(jsii_name="urlExclusionPatterns")
    def url_exclusion_patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "urlExclusionPatterns"))

    @url_exclusion_patterns.setter
    def url_exclusion_patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlExclusionPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="urlInclusionPatterns")
    def url_inclusion_patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "urlInclusionPatterns"))

    @url_inclusion_patterns.setter
    def url_inclusion_patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlInclusionPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationWebCrawlerConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationWebCrawlerConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port", "credentials": "credentials"},
)
class KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration:
    def __init__(
        self,
        *,
        host: builtins.str,
        port: jsii.Number,
        credentials: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#host KendraDataSource#host}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#port KendraDataSource#port}.
        :param credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#credentials KendraDataSource#credentials}.
        '''
        if __debug__:
            def stub(
                *,
                host: builtins.str,
                port: jsii.Number,
                credentials: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
        self._values: typing.Dict[str, typing.Any] = {
            "host": host,
            "port": port,
        }
        if credentials is not None:
            self._values["credentials"] = credentials

    @builtins.property
    def host(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#host KendraDataSource#host}.'''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#port KendraDataSource#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def credentials(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#credentials KendraDataSource#credentials}.'''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfigurationOutputReference",
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

    @jsii.member(jsii_name="resetCredentials")
    def reset_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentials", []))

    @builtins.property
    @jsii.member(jsii_name="credentialsInput")
    def credentials_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="credentials")
    def credentials(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentials"))

    @credentials.setter
    def credentials(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentials", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

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
    ) -> typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationUrls",
    jsii_struct_bases=[],
    name_mapping={
        "seed_url_configuration": "seedUrlConfiguration",
        "site_maps_configuration": "siteMapsConfiguration",
    },
)
class KendraDataSourceConfigurationWebCrawlerConfigurationUrls:
    def __init__(
        self,
        *,
        seed_url_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration", typing.Dict[str, typing.Any]]] = None,
        site_maps_configuration: typing.Optional[typing.Union["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param seed_url_configuration: seed_url_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#seed_url_configuration KendraDataSource#seed_url_configuration}
        :param site_maps_configuration: site_maps_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#site_maps_configuration KendraDataSource#site_maps_configuration}
        '''
        if isinstance(seed_url_configuration, dict):
            seed_url_configuration = KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration(**seed_url_configuration)
        if isinstance(site_maps_configuration, dict):
            site_maps_configuration = KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration(**site_maps_configuration)
        if __debug__:
            def stub(
                *,
                seed_url_configuration: typing.Optional[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration, typing.Dict[str, typing.Any]]] = None,
                site_maps_configuration: typing.Optional[typing.Union[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument seed_url_configuration", value=seed_url_configuration, expected_type=type_hints["seed_url_configuration"])
            check_type(argname="argument site_maps_configuration", value=site_maps_configuration, expected_type=type_hints["site_maps_configuration"])
        self._values: typing.Dict[str, typing.Any] = {}
        if seed_url_configuration is not None:
            self._values["seed_url_configuration"] = seed_url_configuration
        if site_maps_configuration is not None:
            self._values["site_maps_configuration"] = site_maps_configuration

    @builtins.property
    def seed_url_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration"]:
        '''seed_url_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#seed_url_configuration KendraDataSource#seed_url_configuration}
        '''
        result = self._values.get("seed_url_configuration")
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration"], result)

    @builtins.property
    def site_maps_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration"]:
        '''site_maps_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#site_maps_configuration KendraDataSource#site_maps_configuration}
        '''
        result = self._values.get("site_maps_configuration")
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationWebCrawlerConfigurationUrls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceConfigurationWebCrawlerConfigurationUrlsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationUrlsOutputReference",
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

    @jsii.member(jsii_name="putSeedUrlConfiguration")
    def put_seed_url_configuration(
        self,
        *,
        seed_urls: typing.Sequence[builtins.str],
        web_crawler_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param seed_urls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#seed_urls KendraDataSource#seed_urls}.
        :param web_crawler_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#web_crawler_mode KendraDataSource#web_crawler_mode}.
        '''
        value = KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration(
            seed_urls=seed_urls, web_crawler_mode=web_crawler_mode
        )

        return typing.cast(None, jsii.invoke(self, "putSeedUrlConfiguration", [value]))

    @jsii.member(jsii_name="putSiteMapsConfiguration")
    def put_site_maps_configuration(
        self,
        *,
        site_maps: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param site_maps: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#site_maps KendraDataSource#site_maps}.
        '''
        value = KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration(
            site_maps=site_maps
        )

        return typing.cast(None, jsii.invoke(self, "putSiteMapsConfiguration", [value]))

    @jsii.member(jsii_name="resetSeedUrlConfiguration")
    def reset_seed_url_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeedUrlConfiguration", []))

    @jsii.member(jsii_name="resetSiteMapsConfiguration")
    def reset_site_maps_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSiteMapsConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="seedUrlConfiguration")
    def seed_url_configuration(
        self,
    ) -> "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfigurationOutputReference":
        return typing.cast("KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfigurationOutputReference", jsii.get(self, "seedUrlConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="siteMapsConfiguration")
    def site_maps_configuration(
        self,
    ) -> "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfigurationOutputReference":
        return typing.cast("KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfigurationOutputReference", jsii.get(self, "siteMapsConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="seedUrlConfigurationInput")
    def seed_url_configuration_input(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration"]:
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration"], jsii.get(self, "seedUrlConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="siteMapsConfigurationInput")
    def site_maps_configuration_input(
        self,
    ) -> typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration"]:
        return typing.cast(typing.Optional["KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration"], jsii.get(self, "siteMapsConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrls]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrls],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrls],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration",
    jsii_struct_bases=[],
    name_mapping={"seed_urls": "seedUrls", "web_crawler_mode": "webCrawlerMode"},
)
class KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration:
    def __init__(
        self,
        *,
        seed_urls: typing.Sequence[builtins.str],
        web_crawler_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param seed_urls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#seed_urls KendraDataSource#seed_urls}.
        :param web_crawler_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#web_crawler_mode KendraDataSource#web_crawler_mode}.
        '''
        if __debug__:
            def stub(
                *,
                seed_urls: typing.Sequence[builtins.str],
                web_crawler_mode: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument seed_urls", value=seed_urls, expected_type=type_hints["seed_urls"])
            check_type(argname="argument web_crawler_mode", value=web_crawler_mode, expected_type=type_hints["web_crawler_mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "seed_urls": seed_urls,
        }
        if web_crawler_mode is not None:
            self._values["web_crawler_mode"] = web_crawler_mode

    @builtins.property
    def seed_urls(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#seed_urls KendraDataSource#seed_urls}.'''
        result = self._values.get("seed_urls")
        assert result is not None, "Required property 'seed_urls' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def web_crawler_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#web_crawler_mode KendraDataSource#web_crawler_mode}.'''
        result = self._values.get("web_crawler_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfigurationOutputReference",
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

    @jsii.member(jsii_name="resetWebCrawlerMode")
    def reset_web_crawler_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebCrawlerMode", []))

    @builtins.property
    @jsii.member(jsii_name="seedUrlsInput")
    def seed_urls_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "seedUrlsInput"))

    @builtins.property
    @jsii.member(jsii_name="webCrawlerModeInput")
    def web_crawler_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webCrawlerModeInput"))

    @builtins.property
    @jsii.member(jsii_name="seedUrls")
    def seed_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "seedUrls"))

    @seed_urls.setter
    def seed_urls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seedUrls", value)

    @builtins.property
    @jsii.member(jsii_name="webCrawlerMode")
    def web_crawler_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webCrawlerMode"))

    @web_crawler_mode.setter
    def web_crawler_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webCrawlerMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration",
    jsii_struct_bases=[],
    name_mapping={"site_maps": "siteMaps"},
)
class KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration:
    def __init__(self, *, site_maps: typing.Sequence[builtins.str]) -> None:
        '''
        :param site_maps: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#site_maps KendraDataSource#site_maps}.
        '''
        if __debug__:
            def stub(*, site_maps: typing.Sequence[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument site_maps", value=site_maps, expected_type=type_hints["site_maps"])
        self._values: typing.Dict[str, typing.Any] = {
            "site_maps": site_maps,
        }

    @builtins.property
    def site_maps(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#site_maps KendraDataSource#site_maps}.'''
        result = self._values.get("site_maps")
        assert result is not None, "Required property 'site_maps' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfigurationOutputReference",
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
    @jsii.member(jsii_name="siteMapsInput")
    def site_maps_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "siteMapsInput"))

    @builtins.property
    @jsii.member(jsii_name="siteMaps")
    def site_maps(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "siteMaps"))

    @site_maps.setter
    def site_maps(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "siteMaps", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "inline_configurations": "inlineConfigurations",
        "post_extraction_hook_configuration": "postExtractionHookConfiguration",
        "pre_extraction_hook_configuration": "preExtractionHookConfiguration",
        "role_arn": "roleArn",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfiguration:
    def __init__(
        self,
        *,
        inline_configurations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations", typing.Dict[str, typing.Any]]]]] = None,
        post_extraction_hook_configuration: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration", typing.Dict[str, typing.Any]]] = None,
        pre_extraction_hook_configuration: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration", typing.Dict[str, typing.Any]]] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param inline_configurations: inline_configurations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#inline_configurations KendraDataSource#inline_configurations}
        :param post_extraction_hook_configuration: post_extraction_hook_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#post_extraction_hook_configuration KendraDataSource#post_extraction_hook_configuration}
        :param pre_extraction_hook_configuration: pre_extraction_hook_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#pre_extraction_hook_configuration KendraDataSource#pre_extraction_hook_configuration}
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#role_arn KendraDataSource#role_arn}.
        '''
        if isinstance(post_extraction_hook_configuration, dict):
            post_extraction_hook_configuration = KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration(**post_extraction_hook_configuration)
        if isinstance(pre_extraction_hook_configuration, dict):
            pre_extraction_hook_configuration = KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration(**pre_extraction_hook_configuration)
        if __debug__:
            def stub(
                *,
                inline_configurations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations, typing.Dict[str, typing.Any]]]]] = None,
                post_extraction_hook_configuration: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration, typing.Dict[str, typing.Any]]] = None,
                pre_extraction_hook_configuration: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration, typing.Dict[str, typing.Any]]] = None,
                role_arn: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument inline_configurations", value=inline_configurations, expected_type=type_hints["inline_configurations"])
            check_type(argname="argument post_extraction_hook_configuration", value=post_extraction_hook_configuration, expected_type=type_hints["post_extraction_hook_configuration"])
            check_type(argname="argument pre_extraction_hook_configuration", value=pre_extraction_hook_configuration, expected_type=type_hints["pre_extraction_hook_configuration"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {}
        if inline_configurations is not None:
            self._values["inline_configurations"] = inline_configurations
        if post_extraction_hook_configuration is not None:
            self._values["post_extraction_hook_configuration"] = post_extraction_hook_configuration
        if pre_extraction_hook_configuration is not None:
            self._values["pre_extraction_hook_configuration"] = pre_extraction_hook_configuration
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def inline_configurations(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations"]]]:
        '''inline_configurations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#inline_configurations KendraDataSource#inline_configurations}
        '''
        result = self._values.get("inline_configurations")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations"]]], result)

    @builtins.property
    def post_extraction_hook_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration"]:
        '''post_extraction_hook_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#post_extraction_hook_configuration KendraDataSource#post_extraction_hook_configuration}
        '''
        result = self._values.get("post_extraction_hook_configuration")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration"], result)

    @builtins.property
    def pre_extraction_hook_configuration(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration"]:
        '''pre_extraction_hook_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#pre_extraction_hook_configuration KendraDataSource#pre_extraction_hook_configuration}
        '''
        result = self._values.get("pre_extraction_hook_configuration")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration"], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#role_arn KendraDataSource#role_arn}.'''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations",
    jsii_struct_bases=[],
    name_mapping={
        "condition": "condition",
        "document_content_deletion": "documentContentDeletion",
        "target": "target",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations:
    def __init__(
        self,
        *,
        condition: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition", typing.Dict[str, typing.Any]]] = None,
        document_content_deletion: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        target: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition KendraDataSource#condition}
        :param document_content_deletion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#document_content_deletion KendraDataSource#document_content_deletion}.
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target KendraDataSource#target}
        '''
        if isinstance(condition, dict):
            condition = KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition(**condition)
        if isinstance(target, dict):
            target = KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget(**target)
        if __debug__:
            def stub(
                *,
                condition: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition, typing.Dict[str, typing.Any]]] = None,
                document_content_deletion: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                target: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument document_content_deletion", value=document_content_deletion, expected_type=type_hints["document_content_deletion"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[str, typing.Any] = {}
        if condition is not None:
            self._values["condition"] = condition
        if document_content_deletion is not None:
            self._values["document_content_deletion"] = document_content_deletion
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def condition(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition"]:
        '''condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition KendraDataSource#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition"], result)

    @builtins.property
    def document_content_deletion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#document_content_deletion KendraDataSource#document_content_deletion}.'''
        result = self._values.get("document_content_deletion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def target(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget"]:
        '''target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target KendraDataSource#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition",
    jsii_struct_bases=[],
    name_mapping={
        "condition_document_attribute_key": "conditionDocumentAttributeKey",
        "operator": "operator",
        "condition_on_value": "conditionOnValue",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition:
    def __init__(
        self,
        *,
        condition_document_attribute_key: builtins.str,
        operator: builtins.str,
        condition_on_value: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param condition_document_attribute_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_document_attribute_key KendraDataSource#condition_document_attribute_key}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#operator KendraDataSource#operator}.
        :param condition_on_value: condition_on_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_on_value KendraDataSource#condition_on_value}
        '''
        if isinstance(condition_on_value, dict):
            condition_on_value = KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue(**condition_on_value)
        if __debug__:
            def stub(
                *,
                condition_document_attribute_key: builtins.str,
                operator: builtins.str,
                condition_on_value: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument condition_document_attribute_key", value=condition_document_attribute_key, expected_type=type_hints["condition_document_attribute_key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument condition_on_value", value=condition_on_value, expected_type=type_hints["condition_on_value"])
        self._values: typing.Dict[str, typing.Any] = {
            "condition_document_attribute_key": condition_document_attribute_key,
            "operator": operator,
        }
        if condition_on_value is not None:
            self._values["condition_on_value"] = condition_on_value

    @builtins.property
    def condition_document_attribute_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_document_attribute_key KendraDataSource#condition_document_attribute_key}.'''
        result = self._values.get("condition_document_attribute_key")
        assert result is not None, "Required property 'condition_document_attribute_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#operator KendraDataSource#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition_on_value(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue"]:
        '''condition_on_value block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_on_value KendraDataSource#condition_on_value}
        '''
        result = self._values.get("condition_on_value")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue",
    jsii_struct_bases=[],
    name_mapping={
        "date_value": "dateValue",
        "long_value": "longValue",
        "string_list_value": "stringListValue",
        "string_value": "stringValue",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue:
    def __init__(
        self,
        *,
        date_value: typing.Optional[builtins.str] = None,
        long_value: typing.Optional[jsii.Number] = None,
        string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param date_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.
        :param long_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.
        :param string_list_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.
        '''
        if __debug__:
            def stub(
                *,
                date_value: typing.Optional[builtins.str] = None,
                long_value: typing.Optional[jsii.Number] = None,
                string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
                string_value: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument date_value", value=date_value, expected_type=type_hints["date_value"])
            check_type(argname="argument long_value", value=long_value, expected_type=type_hints["long_value"])
            check_type(argname="argument string_list_value", value=string_list_value, expected_type=type_hints["string_list_value"])
            check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if date_value is not None:
            self._values["date_value"] = date_value
        if long_value is not None:
            self._values["long_value"] = long_value
        if string_list_value is not None:
            self._values["string_list_value"] = string_list_value
        if string_value is not None:
            self._values["string_value"] = string_value

    @builtins.property
    def date_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.'''
        result = self._values.get("date_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def long_value(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.'''
        result = self._values.get("long_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def string_list_value(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.'''
        result = self._values.get("string_list_value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def string_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.'''
        result = self._values.get("string_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValueOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValueOutputReference",
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

    @jsii.member(jsii_name="resetDateValue")
    def reset_date_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDateValue", []))

    @jsii.member(jsii_name="resetLongValue")
    def reset_long_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongValue", []))

    @jsii.member(jsii_name="resetStringListValue")
    def reset_string_list_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringListValue", []))

    @jsii.member(jsii_name="resetStringValue")
    def reset_string_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringValue", []))

    @builtins.property
    @jsii.member(jsii_name="dateValueInput")
    def date_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dateValueInput"))

    @builtins.property
    @jsii.member(jsii_name="longValueInput")
    def long_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "longValueInput"))

    @builtins.property
    @jsii.member(jsii_name="stringListValueInput")
    def string_list_value_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "stringListValueInput"))

    @builtins.property
    @jsii.member(jsii_name="stringValueInput")
    def string_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stringValueInput"))

    @builtins.property
    @jsii.member(jsii_name="dateValue")
    def date_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dateValue"))

    @date_value.setter
    def date_value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dateValue", value)

    @builtins.property
    @jsii.member(jsii_name="longValue")
    def long_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "longValue"))

    @long_value.setter
    def long_value(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longValue", value)

    @builtins.property
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stringListValue"))

    @string_list_value.setter
    def string_list_value(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringListValue", value)

    @builtins.property
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stringValue"))

    @string_value.setter
    def string_value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionOutputReference",
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

    @jsii.member(jsii_name="putConditionOnValue")
    def put_condition_on_value(
        self,
        *,
        date_value: typing.Optional[builtins.str] = None,
        long_value: typing.Optional[jsii.Number] = None,
        string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param date_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.
        :param long_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.
        :param string_list_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue(
            date_value=date_value,
            long_value=long_value,
            string_list_value=string_list_value,
            string_value=string_value,
        )

        return typing.cast(None, jsii.invoke(self, "putConditionOnValue", [value]))

    @jsii.member(jsii_name="resetConditionOnValue")
    def reset_condition_on_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionOnValue", []))

    @builtins.property
    @jsii.member(jsii_name="conditionOnValue")
    def condition_on_value(
        self,
    ) -> KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValueOutputReference:
        return typing.cast(KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValueOutputReference, jsii.get(self, "conditionOnValue"))

    @builtins.property
    @jsii.member(jsii_name="conditionDocumentAttributeKeyInput")
    def condition_document_attribute_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conditionDocumentAttributeKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionOnValueInput")
    def condition_on_value_input(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue], jsii.get(self, "conditionOnValueInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionDocumentAttributeKey")
    def condition_document_attribute_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conditionDocumentAttributeKey"))

    @condition_document_attribute_key.setter
    def condition_document_attribute_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conditionDocumentAttributeKey", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsList",
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
    ) -> "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsOutputReference",
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

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        *,
        condition_document_attribute_key: builtins.str,
        operator: builtins.str,
        condition_on_value: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param condition_document_attribute_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_document_attribute_key KendraDataSource#condition_document_attribute_key}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#operator KendraDataSource#operator}.
        :param condition_on_value: condition_on_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_on_value KendraDataSource#condition_on_value}
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition(
            condition_document_attribute_key=condition_document_attribute_key,
            operator=operator,
            condition_on_value=condition_on_value,
        )

        return typing.cast(None, jsii.invoke(self, "putCondition", [value]))

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        *,
        target_document_attribute_key: typing.Optional[builtins.str] = None,
        target_document_attribute_value: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue", typing.Dict[str, typing.Any]]] = None,
        target_document_attribute_value_deletion: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param target_document_attribute_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target_document_attribute_key KendraDataSource#target_document_attribute_key}.
        :param target_document_attribute_value: target_document_attribute_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target_document_attribute_value KendraDataSource#target_document_attribute_value}
        :param target_document_attribute_value_deletion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target_document_attribute_value_deletion KendraDataSource#target_document_attribute_value_deletion}.
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget(
            target_document_attribute_key=target_document_attribute_key,
            target_document_attribute_value=target_document_attribute_value,
            target_document_attribute_value_deletion=target_document_attribute_value_deletion,
        )

        return typing.cast(None, jsii.invoke(self, "putTarget", [value]))

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @jsii.member(jsii_name="resetDocumentContentDeletion")
    def reset_document_content_deletion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentContentDeletion", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(
        self,
    ) -> KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionOutputReference:
        return typing.cast(KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionOutputReference, jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(
        self,
    ) -> "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetOutputReference":
        return typing.cast("KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="documentContentDeletionInput")
    def document_content_deletion_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "documentContentDeletionInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget"]:
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="documentContentDeletion")
    def document_content_deletion(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "documentContentDeletion"))

    @document_content_deletion.setter
    def document_content_deletion(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentContentDeletion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget",
    jsii_struct_bases=[],
    name_mapping={
        "target_document_attribute_key": "targetDocumentAttributeKey",
        "target_document_attribute_value": "targetDocumentAttributeValue",
        "target_document_attribute_value_deletion": "targetDocumentAttributeValueDeletion",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget:
    def __init__(
        self,
        *,
        target_document_attribute_key: typing.Optional[builtins.str] = None,
        target_document_attribute_value: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue", typing.Dict[str, typing.Any]]] = None,
        target_document_attribute_value_deletion: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param target_document_attribute_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target_document_attribute_key KendraDataSource#target_document_attribute_key}.
        :param target_document_attribute_value: target_document_attribute_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target_document_attribute_value KendraDataSource#target_document_attribute_value}
        :param target_document_attribute_value_deletion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target_document_attribute_value_deletion KendraDataSource#target_document_attribute_value_deletion}.
        '''
        if isinstance(target_document_attribute_value, dict):
            target_document_attribute_value = KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue(**target_document_attribute_value)
        if __debug__:
            def stub(
                *,
                target_document_attribute_key: typing.Optional[builtins.str] = None,
                target_document_attribute_value: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue, typing.Dict[str, typing.Any]]] = None,
                target_document_attribute_value_deletion: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument target_document_attribute_key", value=target_document_attribute_key, expected_type=type_hints["target_document_attribute_key"])
            check_type(argname="argument target_document_attribute_value", value=target_document_attribute_value, expected_type=type_hints["target_document_attribute_value"])
            check_type(argname="argument target_document_attribute_value_deletion", value=target_document_attribute_value_deletion, expected_type=type_hints["target_document_attribute_value_deletion"])
        self._values: typing.Dict[str, typing.Any] = {}
        if target_document_attribute_key is not None:
            self._values["target_document_attribute_key"] = target_document_attribute_key
        if target_document_attribute_value is not None:
            self._values["target_document_attribute_value"] = target_document_attribute_value
        if target_document_attribute_value_deletion is not None:
            self._values["target_document_attribute_value_deletion"] = target_document_attribute_value_deletion

    @builtins.property
    def target_document_attribute_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target_document_attribute_key KendraDataSource#target_document_attribute_key}.'''
        result = self._values.get("target_document_attribute_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_document_attribute_value(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue"]:
        '''target_document_attribute_value block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target_document_attribute_value KendraDataSource#target_document_attribute_value}
        '''
        result = self._values.get("target_document_attribute_value")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue"], result)

    @builtins.property
    def target_document_attribute_value_deletion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#target_document_attribute_value_deletion KendraDataSource#target_document_attribute_value_deletion}.'''
        result = self._values.get("target_document_attribute_value_deletion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetOutputReference",
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

    @jsii.member(jsii_name="putTargetDocumentAttributeValue")
    def put_target_document_attribute_value(
        self,
        *,
        date_value: typing.Optional[builtins.str] = None,
        long_value: typing.Optional[jsii.Number] = None,
        string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param date_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.
        :param long_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.
        :param string_list_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue(
            date_value=date_value,
            long_value=long_value,
            string_list_value=string_list_value,
            string_value=string_value,
        )

        return typing.cast(None, jsii.invoke(self, "putTargetDocumentAttributeValue", [value]))

    @jsii.member(jsii_name="resetTargetDocumentAttributeKey")
    def reset_target_document_attribute_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetDocumentAttributeKey", []))

    @jsii.member(jsii_name="resetTargetDocumentAttributeValue")
    def reset_target_document_attribute_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetDocumentAttributeValue", []))

    @jsii.member(jsii_name="resetTargetDocumentAttributeValueDeletion")
    def reset_target_document_attribute_value_deletion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetDocumentAttributeValueDeletion", []))

    @builtins.property
    @jsii.member(jsii_name="targetDocumentAttributeValue")
    def target_document_attribute_value(
        self,
    ) -> "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValueOutputReference":
        return typing.cast("KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValueOutputReference", jsii.get(self, "targetDocumentAttributeValue"))

    @builtins.property
    @jsii.member(jsii_name="targetDocumentAttributeKeyInput")
    def target_document_attribute_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetDocumentAttributeKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="targetDocumentAttributeValueDeletionInput")
    def target_document_attribute_value_deletion_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "targetDocumentAttributeValueDeletionInput"))

    @builtins.property
    @jsii.member(jsii_name="targetDocumentAttributeValueInput")
    def target_document_attribute_value_input(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue"]:
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue"], jsii.get(self, "targetDocumentAttributeValueInput"))

    @builtins.property
    @jsii.member(jsii_name="targetDocumentAttributeKey")
    def target_document_attribute_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetDocumentAttributeKey"))

    @target_document_attribute_key.setter
    def target_document_attribute_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetDocumentAttributeKey", value)

    @builtins.property
    @jsii.member(jsii_name="targetDocumentAttributeValueDeletion")
    def target_document_attribute_value_deletion(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "targetDocumentAttributeValueDeletion"))

    @target_document_attribute_value_deletion.setter
    def target_document_attribute_value_deletion(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetDocumentAttributeValueDeletion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue",
    jsii_struct_bases=[],
    name_mapping={
        "date_value": "dateValue",
        "long_value": "longValue",
        "string_list_value": "stringListValue",
        "string_value": "stringValue",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue:
    def __init__(
        self,
        *,
        date_value: typing.Optional[builtins.str] = None,
        long_value: typing.Optional[jsii.Number] = None,
        string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param date_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.
        :param long_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.
        :param string_list_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.
        '''
        if __debug__:
            def stub(
                *,
                date_value: typing.Optional[builtins.str] = None,
                long_value: typing.Optional[jsii.Number] = None,
                string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
                string_value: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument date_value", value=date_value, expected_type=type_hints["date_value"])
            check_type(argname="argument long_value", value=long_value, expected_type=type_hints["long_value"])
            check_type(argname="argument string_list_value", value=string_list_value, expected_type=type_hints["string_list_value"])
            check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if date_value is not None:
            self._values["date_value"] = date_value
        if long_value is not None:
            self._values["long_value"] = long_value
        if string_list_value is not None:
            self._values["string_list_value"] = string_list_value
        if string_value is not None:
            self._values["string_value"] = string_value

    @builtins.property
    def date_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.'''
        result = self._values.get("date_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def long_value(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.'''
        result = self._values.get("long_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def string_list_value(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.'''
        result = self._values.get("string_list_value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def string_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.'''
        result = self._values.get("string_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValueOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValueOutputReference",
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

    @jsii.member(jsii_name="resetDateValue")
    def reset_date_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDateValue", []))

    @jsii.member(jsii_name="resetLongValue")
    def reset_long_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongValue", []))

    @jsii.member(jsii_name="resetStringListValue")
    def reset_string_list_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringListValue", []))

    @jsii.member(jsii_name="resetStringValue")
    def reset_string_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringValue", []))

    @builtins.property
    @jsii.member(jsii_name="dateValueInput")
    def date_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dateValueInput"))

    @builtins.property
    @jsii.member(jsii_name="longValueInput")
    def long_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "longValueInput"))

    @builtins.property
    @jsii.member(jsii_name="stringListValueInput")
    def string_list_value_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "stringListValueInput"))

    @builtins.property
    @jsii.member(jsii_name="stringValueInput")
    def string_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stringValueInput"))

    @builtins.property
    @jsii.member(jsii_name="dateValue")
    def date_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dateValue"))

    @date_value.setter
    def date_value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dateValue", value)

    @builtins.property
    @jsii.member(jsii_name="longValue")
    def long_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "longValue"))

    @long_value.setter
    def long_value(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longValue", value)

    @builtins.property
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stringListValue"))

    @string_list_value.setter
    def string_list_value(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringListValue", value)

    @builtins.property
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stringValue"))

    @string_value.setter
    def string_value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceCustomDocumentEnrichmentConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationOutputReference",
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

    @jsii.member(jsii_name="putInlineConfigurations")
    def put_inline_configurations(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInlineConfigurations", [value]))

    @jsii.member(jsii_name="putPostExtractionHookConfiguration")
    def put_post_extraction_hook_configuration(
        self,
        *,
        lambda_arn: builtins.str,
        s3_bucket: builtins.str,
        invocation_condition: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param lambda_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#lambda_arn KendraDataSource#lambda_arn}.
        :param s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_bucket KendraDataSource#s3_bucket}.
        :param invocation_condition: invocation_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#invocation_condition KendraDataSource#invocation_condition}
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration(
            lambda_arn=lambda_arn,
            s3_bucket=s3_bucket,
            invocation_condition=invocation_condition,
        )

        return typing.cast(None, jsii.invoke(self, "putPostExtractionHookConfiguration", [value]))

    @jsii.member(jsii_name="putPreExtractionHookConfiguration")
    def put_pre_extraction_hook_configuration(
        self,
        *,
        lambda_arn: builtins.str,
        s3_bucket: builtins.str,
        invocation_condition: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param lambda_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#lambda_arn KendraDataSource#lambda_arn}.
        :param s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_bucket KendraDataSource#s3_bucket}.
        :param invocation_condition: invocation_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#invocation_condition KendraDataSource#invocation_condition}
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration(
            lambda_arn=lambda_arn,
            s3_bucket=s3_bucket,
            invocation_condition=invocation_condition,
        )

        return typing.cast(None, jsii.invoke(self, "putPreExtractionHookConfiguration", [value]))

    @jsii.member(jsii_name="resetInlineConfigurations")
    def reset_inline_configurations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInlineConfigurations", []))

    @jsii.member(jsii_name="resetPostExtractionHookConfiguration")
    def reset_post_extraction_hook_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostExtractionHookConfiguration", []))

    @jsii.member(jsii_name="resetPreExtractionHookConfiguration")
    def reset_pre_extraction_hook_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreExtractionHookConfiguration", []))

    @jsii.member(jsii_name="resetRoleArn")
    def reset_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleArn", []))

    @builtins.property
    @jsii.member(jsii_name="inlineConfigurations")
    def inline_configurations(
        self,
    ) -> KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsList:
        return typing.cast(KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsList, jsii.get(self, "inlineConfigurations"))

    @builtins.property
    @jsii.member(jsii_name="postExtractionHookConfiguration")
    def post_extraction_hook_configuration(
        self,
    ) -> "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationOutputReference":
        return typing.cast("KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationOutputReference", jsii.get(self, "postExtractionHookConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="preExtractionHookConfiguration")
    def pre_extraction_hook_configuration(
        self,
    ) -> "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationOutputReference":
        return typing.cast("KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationOutputReference", jsii.get(self, "preExtractionHookConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="inlineConfigurationsInput")
    def inline_configurations_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations]]], jsii.get(self, "inlineConfigurationsInput"))

    @builtins.property
    @jsii.member(jsii_name="postExtractionHookConfigurationInput")
    def post_extraction_hook_configuration_input(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration"]:
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration"], jsii.get(self, "postExtractionHookConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="preExtractionHookConfigurationInput")
    def pre_extraction_hook_configuration_input(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration"]:
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration"], jsii.get(self, "preExtractionHookConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

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
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "lambda_arn": "lambdaArn",
        "s3_bucket": "s3Bucket",
        "invocation_condition": "invocationCondition",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration:
    def __init__(
        self,
        *,
        lambda_arn: builtins.str,
        s3_bucket: builtins.str,
        invocation_condition: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param lambda_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#lambda_arn KendraDataSource#lambda_arn}.
        :param s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_bucket KendraDataSource#s3_bucket}.
        :param invocation_condition: invocation_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#invocation_condition KendraDataSource#invocation_condition}
        '''
        if isinstance(invocation_condition, dict):
            invocation_condition = KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition(**invocation_condition)
        if __debug__:
            def stub(
                *,
                lambda_arn: builtins.str,
                s3_bucket: builtins.str,
                invocation_condition: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument lambda_arn", value=lambda_arn, expected_type=type_hints["lambda_arn"])
            check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
            check_type(argname="argument invocation_condition", value=invocation_condition, expected_type=type_hints["invocation_condition"])
        self._values: typing.Dict[str, typing.Any] = {
            "lambda_arn": lambda_arn,
            "s3_bucket": s3_bucket,
        }
        if invocation_condition is not None:
            self._values["invocation_condition"] = invocation_condition

    @builtins.property
    def lambda_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#lambda_arn KendraDataSource#lambda_arn}.'''
        result = self._values.get("lambda_arn")
        assert result is not None, "Required property 'lambda_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_bucket KendraDataSource#s3_bucket}.'''
        result = self._values.get("s3_bucket")
        assert result is not None, "Required property 's3_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invocation_condition(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition"]:
        '''invocation_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#invocation_condition KendraDataSource#invocation_condition}
        '''
        result = self._values.get("invocation_condition")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition",
    jsii_struct_bases=[],
    name_mapping={
        "condition_document_attribute_key": "conditionDocumentAttributeKey",
        "operator": "operator",
        "condition_on_value": "conditionOnValue",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition:
    def __init__(
        self,
        *,
        condition_document_attribute_key: builtins.str,
        operator: builtins.str,
        condition_on_value: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param condition_document_attribute_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_document_attribute_key KendraDataSource#condition_document_attribute_key}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#operator KendraDataSource#operator}.
        :param condition_on_value: condition_on_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_on_value KendraDataSource#condition_on_value}
        '''
        if isinstance(condition_on_value, dict):
            condition_on_value = KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue(**condition_on_value)
        if __debug__:
            def stub(
                *,
                condition_document_attribute_key: builtins.str,
                operator: builtins.str,
                condition_on_value: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument condition_document_attribute_key", value=condition_document_attribute_key, expected_type=type_hints["condition_document_attribute_key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument condition_on_value", value=condition_on_value, expected_type=type_hints["condition_on_value"])
        self._values: typing.Dict[str, typing.Any] = {
            "condition_document_attribute_key": condition_document_attribute_key,
            "operator": operator,
        }
        if condition_on_value is not None:
            self._values["condition_on_value"] = condition_on_value

    @builtins.property
    def condition_document_attribute_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_document_attribute_key KendraDataSource#condition_document_attribute_key}.'''
        result = self._values.get("condition_document_attribute_key")
        assert result is not None, "Required property 'condition_document_attribute_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#operator KendraDataSource#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition_on_value(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue"]:
        '''condition_on_value block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_on_value KendraDataSource#condition_on_value}
        '''
        result = self._values.get("condition_on_value")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue",
    jsii_struct_bases=[],
    name_mapping={
        "date_value": "dateValue",
        "long_value": "longValue",
        "string_list_value": "stringListValue",
        "string_value": "stringValue",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue:
    def __init__(
        self,
        *,
        date_value: typing.Optional[builtins.str] = None,
        long_value: typing.Optional[jsii.Number] = None,
        string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param date_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.
        :param long_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.
        :param string_list_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.
        '''
        if __debug__:
            def stub(
                *,
                date_value: typing.Optional[builtins.str] = None,
                long_value: typing.Optional[jsii.Number] = None,
                string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
                string_value: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument date_value", value=date_value, expected_type=type_hints["date_value"])
            check_type(argname="argument long_value", value=long_value, expected_type=type_hints["long_value"])
            check_type(argname="argument string_list_value", value=string_list_value, expected_type=type_hints["string_list_value"])
            check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if date_value is not None:
            self._values["date_value"] = date_value
        if long_value is not None:
            self._values["long_value"] = long_value
        if string_list_value is not None:
            self._values["string_list_value"] = string_list_value
        if string_value is not None:
            self._values["string_value"] = string_value

    @builtins.property
    def date_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.'''
        result = self._values.get("date_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def long_value(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.'''
        result = self._values.get("long_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def string_list_value(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.'''
        result = self._values.get("string_list_value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def string_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.'''
        result = self._values.get("string_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference",
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

    @jsii.member(jsii_name="resetDateValue")
    def reset_date_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDateValue", []))

    @jsii.member(jsii_name="resetLongValue")
    def reset_long_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongValue", []))

    @jsii.member(jsii_name="resetStringListValue")
    def reset_string_list_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringListValue", []))

    @jsii.member(jsii_name="resetStringValue")
    def reset_string_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringValue", []))

    @builtins.property
    @jsii.member(jsii_name="dateValueInput")
    def date_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dateValueInput"))

    @builtins.property
    @jsii.member(jsii_name="longValueInput")
    def long_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "longValueInput"))

    @builtins.property
    @jsii.member(jsii_name="stringListValueInput")
    def string_list_value_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "stringListValueInput"))

    @builtins.property
    @jsii.member(jsii_name="stringValueInput")
    def string_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stringValueInput"))

    @builtins.property
    @jsii.member(jsii_name="dateValue")
    def date_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dateValue"))

    @date_value.setter
    def date_value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dateValue", value)

    @builtins.property
    @jsii.member(jsii_name="longValue")
    def long_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "longValue"))

    @long_value.setter
    def long_value(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longValue", value)

    @builtins.property
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stringListValue"))

    @string_list_value.setter
    def string_list_value(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringListValue", value)

    @builtins.property
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stringValue"))

    @string_value.setter
    def string_value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionOutputReference",
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

    @jsii.member(jsii_name="putConditionOnValue")
    def put_condition_on_value(
        self,
        *,
        date_value: typing.Optional[builtins.str] = None,
        long_value: typing.Optional[jsii.Number] = None,
        string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param date_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.
        :param long_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.
        :param string_list_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue(
            date_value=date_value,
            long_value=long_value,
            string_list_value=string_list_value,
            string_value=string_value,
        )

        return typing.cast(None, jsii.invoke(self, "putConditionOnValue", [value]))

    @jsii.member(jsii_name="resetConditionOnValue")
    def reset_condition_on_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionOnValue", []))

    @builtins.property
    @jsii.member(jsii_name="conditionOnValue")
    def condition_on_value(
        self,
    ) -> KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference:
        return typing.cast(KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference, jsii.get(self, "conditionOnValue"))

    @builtins.property
    @jsii.member(jsii_name="conditionDocumentAttributeKeyInput")
    def condition_document_attribute_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conditionDocumentAttributeKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionOnValueInput")
    def condition_on_value_input(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue], jsii.get(self, "conditionOnValueInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionDocumentAttributeKey")
    def condition_document_attribute_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conditionDocumentAttributeKey"))

    @condition_document_attribute_key.setter
    def condition_document_attribute_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conditionDocumentAttributeKey", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationOutputReference",
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

    @jsii.member(jsii_name="putInvocationCondition")
    def put_invocation_condition(
        self,
        *,
        condition_document_attribute_key: builtins.str,
        operator: builtins.str,
        condition_on_value: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param condition_document_attribute_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_document_attribute_key KendraDataSource#condition_document_attribute_key}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#operator KendraDataSource#operator}.
        :param condition_on_value: condition_on_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_on_value KendraDataSource#condition_on_value}
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition(
            condition_document_attribute_key=condition_document_attribute_key,
            operator=operator,
            condition_on_value=condition_on_value,
        )

        return typing.cast(None, jsii.invoke(self, "putInvocationCondition", [value]))

    @jsii.member(jsii_name="resetInvocationCondition")
    def reset_invocation_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvocationCondition", []))

    @builtins.property
    @jsii.member(jsii_name="invocationCondition")
    def invocation_condition(
        self,
    ) -> KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionOutputReference:
        return typing.cast(KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionOutputReference, jsii.get(self, "invocationCondition"))

    @builtins.property
    @jsii.member(jsii_name="invocationConditionInput")
    def invocation_condition_input(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition], jsii.get(self, "invocationConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaArnInput")
    def lambda_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lambdaArnInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketInput")
    def s3_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BucketInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaArn")
    def lambda_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lambdaArn"))

    @lambda_arn.setter
    def lambda_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaArn", value)

    @builtins.property
    @jsii.member(jsii_name="s3Bucket")
    def s3_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Bucket"))

    @s3_bucket.setter
    def s3_bucket(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Bucket", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "lambda_arn": "lambdaArn",
        "s3_bucket": "s3Bucket",
        "invocation_condition": "invocationCondition",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration:
    def __init__(
        self,
        *,
        lambda_arn: builtins.str,
        s3_bucket: builtins.str,
        invocation_condition: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param lambda_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#lambda_arn KendraDataSource#lambda_arn}.
        :param s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_bucket KendraDataSource#s3_bucket}.
        :param invocation_condition: invocation_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#invocation_condition KendraDataSource#invocation_condition}
        '''
        if isinstance(invocation_condition, dict):
            invocation_condition = KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition(**invocation_condition)
        if __debug__:
            def stub(
                *,
                lambda_arn: builtins.str,
                s3_bucket: builtins.str,
                invocation_condition: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument lambda_arn", value=lambda_arn, expected_type=type_hints["lambda_arn"])
            check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
            check_type(argname="argument invocation_condition", value=invocation_condition, expected_type=type_hints["invocation_condition"])
        self._values: typing.Dict[str, typing.Any] = {
            "lambda_arn": lambda_arn,
            "s3_bucket": s3_bucket,
        }
        if invocation_condition is not None:
            self._values["invocation_condition"] = invocation_condition

    @builtins.property
    def lambda_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#lambda_arn KendraDataSource#lambda_arn}.'''
        result = self._values.get("lambda_arn")
        assert result is not None, "Required property 'lambda_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#s3_bucket KendraDataSource#s3_bucket}.'''
        result = self._values.get("s3_bucket")
        assert result is not None, "Required property 's3_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invocation_condition(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition"]:
        '''invocation_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#invocation_condition KendraDataSource#invocation_condition}
        '''
        result = self._values.get("invocation_condition")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition",
    jsii_struct_bases=[],
    name_mapping={
        "condition_document_attribute_key": "conditionDocumentAttributeKey",
        "operator": "operator",
        "condition_on_value": "conditionOnValue",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition:
    def __init__(
        self,
        *,
        condition_document_attribute_key: builtins.str,
        operator: builtins.str,
        condition_on_value: typing.Optional[typing.Union["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param condition_document_attribute_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_document_attribute_key KendraDataSource#condition_document_attribute_key}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#operator KendraDataSource#operator}.
        :param condition_on_value: condition_on_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_on_value KendraDataSource#condition_on_value}
        '''
        if isinstance(condition_on_value, dict):
            condition_on_value = KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue(**condition_on_value)
        if __debug__:
            def stub(
                *,
                condition_document_attribute_key: builtins.str,
                operator: builtins.str,
                condition_on_value: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument condition_document_attribute_key", value=condition_document_attribute_key, expected_type=type_hints["condition_document_attribute_key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument condition_on_value", value=condition_on_value, expected_type=type_hints["condition_on_value"])
        self._values: typing.Dict[str, typing.Any] = {
            "condition_document_attribute_key": condition_document_attribute_key,
            "operator": operator,
        }
        if condition_on_value is not None:
            self._values["condition_on_value"] = condition_on_value

    @builtins.property
    def condition_document_attribute_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_document_attribute_key KendraDataSource#condition_document_attribute_key}.'''
        result = self._values.get("condition_document_attribute_key")
        assert result is not None, "Required property 'condition_document_attribute_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#operator KendraDataSource#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition_on_value(
        self,
    ) -> typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue"]:
        '''condition_on_value block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_on_value KendraDataSource#condition_on_value}
        '''
        result = self._values.get("condition_on_value")
        return typing.cast(typing.Optional["KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue",
    jsii_struct_bases=[],
    name_mapping={
        "date_value": "dateValue",
        "long_value": "longValue",
        "string_list_value": "stringListValue",
        "string_value": "stringValue",
    },
)
class KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue:
    def __init__(
        self,
        *,
        date_value: typing.Optional[builtins.str] = None,
        long_value: typing.Optional[jsii.Number] = None,
        string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param date_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.
        :param long_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.
        :param string_list_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.
        '''
        if __debug__:
            def stub(
                *,
                date_value: typing.Optional[builtins.str] = None,
                long_value: typing.Optional[jsii.Number] = None,
                string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
                string_value: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument date_value", value=date_value, expected_type=type_hints["date_value"])
            check_type(argname="argument long_value", value=long_value, expected_type=type_hints["long_value"])
            check_type(argname="argument string_list_value", value=string_list_value, expected_type=type_hints["string_list_value"])
            check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if date_value is not None:
            self._values["date_value"] = date_value
        if long_value is not None:
            self._values["long_value"] = long_value
        if string_list_value is not None:
            self._values["string_list_value"] = string_list_value
        if string_value is not None:
            self._values["string_value"] = string_value

    @builtins.property
    def date_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.'''
        result = self._values.get("date_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def long_value(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.'''
        result = self._values.get("long_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def string_list_value(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.'''
        result = self._values.get("string_list_value")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def string_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.'''
        result = self._values.get("string_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference",
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

    @jsii.member(jsii_name="resetDateValue")
    def reset_date_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDateValue", []))

    @jsii.member(jsii_name="resetLongValue")
    def reset_long_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongValue", []))

    @jsii.member(jsii_name="resetStringListValue")
    def reset_string_list_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringListValue", []))

    @jsii.member(jsii_name="resetStringValue")
    def reset_string_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringValue", []))

    @builtins.property
    @jsii.member(jsii_name="dateValueInput")
    def date_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dateValueInput"))

    @builtins.property
    @jsii.member(jsii_name="longValueInput")
    def long_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "longValueInput"))

    @builtins.property
    @jsii.member(jsii_name="stringListValueInput")
    def string_list_value_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "stringListValueInput"))

    @builtins.property
    @jsii.member(jsii_name="stringValueInput")
    def string_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stringValueInput"))

    @builtins.property
    @jsii.member(jsii_name="dateValue")
    def date_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dateValue"))

    @date_value.setter
    def date_value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dateValue", value)

    @builtins.property
    @jsii.member(jsii_name="longValue")
    def long_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "longValue"))

    @long_value.setter
    def long_value(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longValue", value)

    @builtins.property
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stringListValue"))

    @string_list_value.setter
    def string_list_value(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringListValue", value)

    @builtins.property
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stringValue"))

    @string_value.setter
    def string_value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionOutputReference",
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

    @jsii.member(jsii_name="putConditionOnValue")
    def put_condition_on_value(
        self,
        *,
        date_value: typing.Optional[builtins.str] = None,
        long_value: typing.Optional[jsii.Number] = None,
        string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param date_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#date_value KendraDataSource#date_value}.
        :param long_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#long_value KendraDataSource#long_value}.
        :param string_list_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_list_value KendraDataSource#string_list_value}.
        :param string_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#string_value KendraDataSource#string_value}.
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue(
            date_value=date_value,
            long_value=long_value,
            string_list_value=string_list_value,
            string_value=string_value,
        )

        return typing.cast(None, jsii.invoke(self, "putConditionOnValue", [value]))

    @jsii.member(jsii_name="resetConditionOnValue")
    def reset_condition_on_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionOnValue", []))

    @builtins.property
    @jsii.member(jsii_name="conditionOnValue")
    def condition_on_value(
        self,
    ) -> KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference:
        return typing.cast(KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference, jsii.get(self, "conditionOnValue"))

    @builtins.property
    @jsii.member(jsii_name="conditionDocumentAttributeKeyInput")
    def condition_document_attribute_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conditionDocumentAttributeKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionOnValueInput")
    def condition_on_value_input(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue], jsii.get(self, "conditionOnValueInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionDocumentAttributeKey")
    def condition_document_attribute_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conditionDocumentAttributeKey"))

    @condition_document_attribute_key.setter
    def condition_document_attribute_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conditionDocumentAttributeKey", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationOutputReference",
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

    @jsii.member(jsii_name="putInvocationCondition")
    def put_invocation_condition(
        self,
        *,
        condition_document_attribute_key: builtins.str,
        operator: builtins.str,
        condition_on_value: typing.Optional[typing.Union[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param condition_document_attribute_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_document_attribute_key KendraDataSource#condition_document_attribute_key}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#operator KendraDataSource#operator}.
        :param condition_on_value: condition_on_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#condition_on_value KendraDataSource#condition_on_value}
        '''
        value = KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition(
            condition_document_attribute_key=condition_document_attribute_key,
            operator=operator,
            condition_on_value=condition_on_value,
        )

        return typing.cast(None, jsii.invoke(self, "putInvocationCondition", [value]))

    @jsii.member(jsii_name="resetInvocationCondition")
    def reset_invocation_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvocationCondition", []))

    @builtins.property
    @jsii.member(jsii_name="invocationCondition")
    def invocation_condition(
        self,
    ) -> KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionOutputReference:
        return typing.cast(KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionOutputReference, jsii.get(self, "invocationCondition"))

    @builtins.property
    @jsii.member(jsii_name="invocationConditionInput")
    def invocation_condition_input(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition], jsii.get(self, "invocationConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaArnInput")
    def lambda_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lambdaArnInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketInput")
    def s3_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BucketInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaArn")
    def lambda_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lambdaArn"))

    @lambda_arn.setter
    def lambda_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaArn", value)

    @builtins.property
    @jsii.member(jsii_name="s3Bucket")
    def s3_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Bucket"))

    @s3_bucket.setter
    def s3_bucket(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Bucket", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration]:
        return typing.cast(typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class KendraDataSourceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#create KendraDataSource#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#delete KendraDataSource#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#update KendraDataSource#update}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#create KendraDataSource#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#delete KendraDataSource#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_data_source#update KendraDataSource#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraDataSourceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraDataSourceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraDataSource.KendraDataSourceTimeoutsOutputReference",
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
    ) -> typing.Optional[typing.Union[KendraDataSourceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KendraDataSourceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KendraDataSourceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KendraDataSourceTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KendraDataSource",
    "KendraDataSourceConfig",
    "KendraDataSourceConfiguration",
    "KendraDataSourceConfigurationOutputReference",
    "KendraDataSourceConfigurationS3Configuration",
    "KendraDataSourceConfigurationS3ConfigurationAccessControlListConfiguration",
    "KendraDataSourceConfigurationS3ConfigurationAccessControlListConfigurationOutputReference",
    "KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfiguration",
    "KendraDataSourceConfigurationS3ConfigurationDocumentsMetadataConfigurationOutputReference",
    "KendraDataSourceConfigurationS3ConfigurationOutputReference",
    "KendraDataSourceConfigurationWebCrawlerConfiguration",
    "KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfiguration",
    "KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthentication",
    "KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationList",
    "KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationBasicAuthenticationOutputReference",
    "KendraDataSourceConfigurationWebCrawlerConfigurationAuthenticationConfigurationOutputReference",
    "KendraDataSourceConfigurationWebCrawlerConfigurationOutputReference",
    "KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfiguration",
    "KendraDataSourceConfigurationWebCrawlerConfigurationProxyConfigurationOutputReference",
    "KendraDataSourceConfigurationWebCrawlerConfigurationUrls",
    "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsOutputReference",
    "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfiguration",
    "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSeedUrlConfigurationOutputReference",
    "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfiguration",
    "KendraDataSourceConfigurationWebCrawlerConfigurationUrlsSiteMapsConfigurationOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfiguration",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurations",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsCondition",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValue",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionConditionOnValueOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsConditionOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsList",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTarget",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValue",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationInlineConfigurationsTargetTargetDocumentAttributeValueOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfiguration",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationCondition",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValue",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationInvocationConditionOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPostExtractionHookConfigurationOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfiguration",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationCondition",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValue",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionConditionOnValueOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationInvocationConditionOutputReference",
    "KendraDataSourceCustomDocumentEnrichmentConfigurationPreExtractionHookConfigurationOutputReference",
    "KendraDataSourceTimeouts",
    "KendraDataSourceTimeoutsOutputReference",
]

publication.publish()
