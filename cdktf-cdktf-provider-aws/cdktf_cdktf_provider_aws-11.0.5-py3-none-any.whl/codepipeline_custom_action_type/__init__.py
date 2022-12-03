'''
# `aws_codepipeline_custom_action_type`

Refer to the Terraform Registory for docs: [`aws_codepipeline_custom_action_type`](https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type).
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


class CodepipelineCustomActionType(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codepipelineCustomActionType.CodepipelineCustomActionType",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type aws_codepipeline_custom_action_type}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        category: builtins.str,
        input_artifact_details: typing.Union["CodepipelineCustomActionTypeInputArtifactDetails", typing.Dict[str, typing.Any]],
        output_artifact_details: typing.Union["CodepipelineCustomActionTypeOutputArtifactDetails", typing.Dict[str, typing.Any]],
        provider_name: builtins.str,
        version: builtins.str,
        configuration_property: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodepipelineCustomActionTypeConfigurationProperty", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Union["CodepipelineCustomActionTypeSettings", typing.Dict[str, typing.Any]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type aws_codepipeline_custom_action_type} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param category: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#category CodepipelineCustomActionType#category}.
        :param input_artifact_details: input_artifact_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#input_artifact_details CodepipelineCustomActionType#input_artifact_details}
        :param output_artifact_details: output_artifact_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#output_artifact_details CodepipelineCustomActionType#output_artifact_details}
        :param provider_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#provider_name CodepipelineCustomActionType#provider_name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#version CodepipelineCustomActionType#version}.
        :param configuration_property: configuration_property block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#configuration_property CodepipelineCustomActionType#configuration_property}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#id CodepipelineCustomActionType#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param settings: settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#settings CodepipelineCustomActionType#settings}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#tags CodepipelineCustomActionType#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#tags_all CodepipelineCustomActionType#tags_all}.
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
                category: builtins.str,
                input_artifact_details: typing.Union[CodepipelineCustomActionTypeInputArtifactDetails, typing.Dict[str, typing.Any]],
                output_artifact_details: typing.Union[CodepipelineCustomActionTypeOutputArtifactDetails, typing.Dict[str, typing.Any]],
                provider_name: builtins.str,
                version: builtins.str,
                configuration_property: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodepipelineCustomActionTypeConfigurationProperty, typing.Dict[str, typing.Any]]]]] = None,
                id: typing.Optional[builtins.str] = None,
                settings: typing.Optional[typing.Union[CodepipelineCustomActionTypeSettings, typing.Dict[str, typing.Any]]] = None,
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
        config = CodepipelineCustomActionTypeConfig(
            category=category,
            input_artifact_details=input_artifact_details,
            output_artifact_details=output_artifact_details,
            provider_name=provider_name,
            version=version,
            configuration_property=configuration_property,
            id=id,
            settings=settings,
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

    @jsii.member(jsii_name="putConfigurationProperty")
    def put_configuration_property(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodepipelineCustomActionTypeConfigurationProperty", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodepipelineCustomActionTypeConfigurationProperty, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConfigurationProperty", [value]))

    @jsii.member(jsii_name="putInputArtifactDetails")
    def put_input_artifact_details(
        self,
        *,
        maximum_count: jsii.Number,
        minimum_count: jsii.Number,
    ) -> None:
        '''
        :param maximum_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#maximum_count CodepipelineCustomActionType#maximum_count}.
        :param minimum_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#minimum_count CodepipelineCustomActionType#minimum_count}.
        '''
        value = CodepipelineCustomActionTypeInputArtifactDetails(
            maximum_count=maximum_count, minimum_count=minimum_count
        )

        return typing.cast(None, jsii.invoke(self, "putInputArtifactDetails", [value]))

    @jsii.member(jsii_name="putOutputArtifactDetails")
    def put_output_artifact_details(
        self,
        *,
        maximum_count: jsii.Number,
        minimum_count: jsii.Number,
    ) -> None:
        '''
        :param maximum_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#maximum_count CodepipelineCustomActionType#maximum_count}.
        :param minimum_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#minimum_count CodepipelineCustomActionType#minimum_count}.
        '''
        value = CodepipelineCustomActionTypeOutputArtifactDetails(
            maximum_count=maximum_count, minimum_count=minimum_count
        )

        return typing.cast(None, jsii.invoke(self, "putOutputArtifactDetails", [value]))

    @jsii.member(jsii_name="putSettings")
    def put_settings(
        self,
        *,
        entity_url_template: typing.Optional[builtins.str] = None,
        execution_url_template: typing.Optional[builtins.str] = None,
        revision_url_template: typing.Optional[builtins.str] = None,
        third_party_configuration_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param entity_url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#entity_url_template CodepipelineCustomActionType#entity_url_template}.
        :param execution_url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#execution_url_template CodepipelineCustomActionType#execution_url_template}.
        :param revision_url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#revision_url_template CodepipelineCustomActionType#revision_url_template}.
        :param third_party_configuration_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#third_party_configuration_url CodepipelineCustomActionType#third_party_configuration_url}.
        '''
        value = CodepipelineCustomActionTypeSettings(
            entity_url_template=entity_url_template,
            execution_url_template=execution_url_template,
            revision_url_template=revision_url_template,
            third_party_configuration_url=third_party_configuration_url,
        )

        return typing.cast(None, jsii.invoke(self, "putSettings", [value]))

    @jsii.member(jsii_name="resetConfigurationProperty")
    def reset_configuration_property(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurationProperty", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

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
    @jsii.member(jsii_name="configurationProperty")
    def configuration_property(
        self,
    ) -> "CodepipelineCustomActionTypeConfigurationPropertyList":
        return typing.cast("CodepipelineCustomActionTypeConfigurationPropertyList", jsii.get(self, "configurationProperty"))

    @builtins.property
    @jsii.member(jsii_name="inputArtifactDetails")
    def input_artifact_details(
        self,
    ) -> "CodepipelineCustomActionTypeInputArtifactDetailsOutputReference":
        return typing.cast("CodepipelineCustomActionTypeInputArtifactDetailsOutputReference", jsii.get(self, "inputArtifactDetails"))

    @builtins.property
    @jsii.member(jsii_name="outputArtifactDetails")
    def output_artifact_details(
        self,
    ) -> "CodepipelineCustomActionTypeOutputArtifactDetailsOutputReference":
        return typing.cast("CodepipelineCustomActionTypeOutputArtifactDetailsOutputReference", jsii.get(self, "outputArtifactDetails"))

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> "CodepipelineCustomActionTypeSettingsOutputReference":
        return typing.cast("CodepipelineCustomActionTypeSettingsOutputReference", jsii.get(self, "settings"))

    @builtins.property
    @jsii.member(jsii_name="categoryInput")
    def category_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "categoryInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationPropertyInput")
    def configuration_property_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodepipelineCustomActionTypeConfigurationProperty"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodepipelineCustomActionTypeConfigurationProperty"]]], jsii.get(self, "configurationPropertyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inputArtifactDetailsInput")
    def input_artifact_details_input(
        self,
    ) -> typing.Optional["CodepipelineCustomActionTypeInputArtifactDetails"]:
        return typing.cast(typing.Optional["CodepipelineCustomActionTypeInputArtifactDetails"], jsii.get(self, "inputArtifactDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="outputArtifactDetailsInput")
    def output_artifact_details_input(
        self,
    ) -> typing.Optional["CodepipelineCustomActionTypeOutputArtifactDetails"]:
        return typing.cast(typing.Optional["CodepipelineCustomActionTypeOutputArtifactDetails"], jsii.get(self, "outputArtifactDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="providerNameInput")
    def provider_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "providerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(self) -> typing.Optional["CodepipelineCustomActionTypeSettings"]:
        return typing.cast(typing.Optional["CodepipelineCustomActionTypeSettings"], jsii.get(self, "settingsInput"))

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
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="category")
    def category(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "category"))

    @category.setter
    def category(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "category", value)

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
    @jsii.member(jsii_name="providerName")
    def provider_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "providerName"))

    @provider_name.setter
    def provider_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "providerName", value)

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


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codepipelineCustomActionType.CodepipelineCustomActionTypeConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "category": "category",
        "input_artifact_details": "inputArtifactDetails",
        "output_artifact_details": "outputArtifactDetails",
        "provider_name": "providerName",
        "version": "version",
        "configuration_property": "configurationProperty",
        "id": "id",
        "settings": "settings",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class CodepipelineCustomActionTypeConfig(cdktf.TerraformMetaArguments):
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
        category: builtins.str,
        input_artifact_details: typing.Union["CodepipelineCustomActionTypeInputArtifactDetails", typing.Dict[str, typing.Any]],
        output_artifact_details: typing.Union["CodepipelineCustomActionTypeOutputArtifactDetails", typing.Dict[str, typing.Any]],
        provider_name: builtins.str,
        version: builtins.str,
        configuration_property: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodepipelineCustomActionTypeConfigurationProperty", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Union["CodepipelineCustomActionTypeSettings", typing.Dict[str, typing.Any]]] = None,
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
        :param category: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#category CodepipelineCustomActionType#category}.
        :param input_artifact_details: input_artifact_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#input_artifact_details CodepipelineCustomActionType#input_artifact_details}
        :param output_artifact_details: output_artifact_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#output_artifact_details CodepipelineCustomActionType#output_artifact_details}
        :param provider_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#provider_name CodepipelineCustomActionType#provider_name}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#version CodepipelineCustomActionType#version}.
        :param configuration_property: configuration_property block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#configuration_property CodepipelineCustomActionType#configuration_property}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#id CodepipelineCustomActionType#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param settings: settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#settings CodepipelineCustomActionType#settings}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#tags CodepipelineCustomActionType#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#tags_all CodepipelineCustomActionType#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(input_artifact_details, dict):
            input_artifact_details = CodepipelineCustomActionTypeInputArtifactDetails(**input_artifact_details)
        if isinstance(output_artifact_details, dict):
            output_artifact_details = CodepipelineCustomActionTypeOutputArtifactDetails(**output_artifact_details)
        if isinstance(settings, dict):
            settings = CodepipelineCustomActionTypeSettings(**settings)
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
                category: builtins.str,
                input_artifact_details: typing.Union[CodepipelineCustomActionTypeInputArtifactDetails, typing.Dict[str, typing.Any]],
                output_artifact_details: typing.Union[CodepipelineCustomActionTypeOutputArtifactDetails, typing.Dict[str, typing.Any]],
                provider_name: builtins.str,
                version: builtins.str,
                configuration_property: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodepipelineCustomActionTypeConfigurationProperty, typing.Dict[str, typing.Any]]]]] = None,
                id: typing.Optional[builtins.str] = None,
                settings: typing.Optional[typing.Union[CodepipelineCustomActionTypeSettings, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument category", value=category, expected_type=type_hints["category"])
            check_type(argname="argument input_artifact_details", value=input_artifact_details, expected_type=type_hints["input_artifact_details"])
            check_type(argname="argument output_artifact_details", value=output_artifact_details, expected_type=type_hints["output_artifact_details"])
            check_type(argname="argument provider_name", value=provider_name, expected_type=type_hints["provider_name"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument configuration_property", value=configuration_property, expected_type=type_hints["configuration_property"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "category": category,
            "input_artifact_details": input_artifact_details,
            "output_artifact_details": output_artifact_details,
            "provider_name": provider_name,
            "version": version,
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
        if configuration_property is not None:
            self._values["configuration_property"] = configuration_property
        if id is not None:
            self._values["id"] = id
        if settings is not None:
            self._values["settings"] = settings
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
    def category(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#category CodepipelineCustomActionType#category}.'''
        result = self._values.get("category")
        assert result is not None, "Required property 'category' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def input_artifact_details(
        self,
    ) -> "CodepipelineCustomActionTypeInputArtifactDetails":
        '''input_artifact_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#input_artifact_details CodepipelineCustomActionType#input_artifact_details}
        '''
        result = self._values.get("input_artifact_details")
        assert result is not None, "Required property 'input_artifact_details' is missing"
        return typing.cast("CodepipelineCustomActionTypeInputArtifactDetails", result)

    @builtins.property
    def output_artifact_details(
        self,
    ) -> "CodepipelineCustomActionTypeOutputArtifactDetails":
        '''output_artifact_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#output_artifact_details CodepipelineCustomActionType#output_artifact_details}
        '''
        result = self._values.get("output_artifact_details")
        assert result is not None, "Required property 'output_artifact_details' is missing"
        return typing.cast("CodepipelineCustomActionTypeOutputArtifactDetails", result)

    @builtins.property
    def provider_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#provider_name CodepipelineCustomActionType#provider_name}.'''
        result = self._values.get("provider_name")
        assert result is not None, "Required property 'provider_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#version CodepipelineCustomActionType#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_property(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodepipelineCustomActionTypeConfigurationProperty"]]]:
        '''configuration_property block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#configuration_property CodepipelineCustomActionType#configuration_property}
        '''
        result = self._values.get("configuration_property")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodepipelineCustomActionTypeConfigurationProperty"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#id CodepipelineCustomActionType#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(self) -> typing.Optional["CodepipelineCustomActionTypeSettings"]:
        '''settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#settings CodepipelineCustomActionType#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional["CodepipelineCustomActionTypeSettings"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#tags CodepipelineCustomActionType#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#tags_all CodepipelineCustomActionType#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodepipelineCustomActionTypeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codepipelineCustomActionType.CodepipelineCustomActionTypeConfigurationProperty",
    jsii_struct_bases=[],
    name_mapping={
        "key": "key",
        "name": "name",
        "required": "required",
        "secret": "secret",
        "description": "description",
        "queryable": "queryable",
        "type": "type",
    },
)
class CodepipelineCustomActionTypeConfigurationProperty:
    def __init__(
        self,
        *,
        key: typing.Union[builtins.bool, cdktf.IResolvable],
        name: builtins.str,
        required: typing.Union[builtins.bool, cdktf.IResolvable],
        secret: typing.Union[builtins.bool, cdktf.IResolvable],
        description: typing.Optional[builtins.str] = None,
        queryable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#key CodepipelineCustomActionType#key}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#name CodepipelineCustomActionType#name}.
        :param required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#required CodepipelineCustomActionType#required}.
        :param secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#secret CodepipelineCustomActionType#secret}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#description CodepipelineCustomActionType#description}.
        :param queryable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#queryable CodepipelineCustomActionType#queryable}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#type CodepipelineCustomActionType#type}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Union[builtins.bool, cdktf.IResolvable],
                name: builtins.str,
                required: typing.Union[builtins.bool, cdktf.IResolvable],
                secret: typing.Union[builtins.bool, cdktf.IResolvable],
                description: typing.Optional[builtins.str] = None,
                queryable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument queryable", value=queryable, expected_type=type_hints["queryable"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "name": name,
            "required": required,
            "secret": secret,
        }
        if description is not None:
            self._values["description"] = description
        if queryable is not None:
            self._values["queryable"] = queryable
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def key(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#key CodepipelineCustomActionType#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#name CodepipelineCustomActionType#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#required CodepipelineCustomActionType#required}.'''
        result = self._values.get("required")
        assert result is not None, "Required property 'required' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def secret(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#secret CodepipelineCustomActionType#secret}.'''
        result = self._values.get("secret")
        assert result is not None, "Required property 'secret' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#description CodepipelineCustomActionType#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def queryable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#queryable CodepipelineCustomActionType#queryable}.'''
        result = self._values.get("queryable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#type CodepipelineCustomActionType#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodepipelineCustomActionTypeConfigurationProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodepipelineCustomActionTypeConfigurationPropertyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codepipelineCustomActionType.CodepipelineCustomActionTypeConfigurationPropertyList",
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
    ) -> "CodepipelineCustomActionTypeConfigurationPropertyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodepipelineCustomActionTypeConfigurationPropertyOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodepipelineCustomActionTypeConfigurationProperty]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodepipelineCustomActionTypeConfigurationProperty]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodepipelineCustomActionTypeConfigurationProperty]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodepipelineCustomActionTypeConfigurationProperty]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodepipelineCustomActionTypeConfigurationPropertyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codepipelineCustomActionType.CodepipelineCustomActionTypeConfigurationPropertyOutputReference",
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

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetQueryable")
    def reset_queryable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryable", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="queryableInput")
    def queryable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "queryableInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="secretInput")
    def secret_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "secretInput"))

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
    @jsii.member(jsii_name="key")
    def key(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "key"))

    @key.setter
    def key(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

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
    @jsii.member(jsii_name="queryable")
    def queryable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "queryable"))

    @queryable.setter
    def queryable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryable", value)

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "required"))

    @required.setter
    def required(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "required", value)

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "secret"))

    @secret.setter
    def secret(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secret", value)

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
    ) -> typing.Optional[typing.Union[CodepipelineCustomActionTypeConfigurationProperty, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodepipelineCustomActionTypeConfigurationProperty, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodepipelineCustomActionTypeConfigurationProperty, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CodepipelineCustomActionTypeConfigurationProperty, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codepipelineCustomActionType.CodepipelineCustomActionTypeInputArtifactDetails",
    jsii_struct_bases=[],
    name_mapping={"maximum_count": "maximumCount", "minimum_count": "minimumCount"},
)
class CodepipelineCustomActionTypeInputArtifactDetails:
    def __init__(
        self,
        *,
        maximum_count: jsii.Number,
        minimum_count: jsii.Number,
    ) -> None:
        '''
        :param maximum_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#maximum_count CodepipelineCustomActionType#maximum_count}.
        :param minimum_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#minimum_count CodepipelineCustomActionType#minimum_count}.
        '''
        if __debug__:
            def stub(*, maximum_count: jsii.Number, minimum_count: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument maximum_count", value=maximum_count, expected_type=type_hints["maximum_count"])
            check_type(argname="argument minimum_count", value=minimum_count, expected_type=type_hints["minimum_count"])
        self._values: typing.Dict[str, typing.Any] = {
            "maximum_count": maximum_count,
            "minimum_count": minimum_count,
        }

    @builtins.property
    def maximum_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#maximum_count CodepipelineCustomActionType#maximum_count}.'''
        result = self._values.get("maximum_count")
        assert result is not None, "Required property 'maximum_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def minimum_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#minimum_count CodepipelineCustomActionType#minimum_count}.'''
        result = self._values.get("minimum_count")
        assert result is not None, "Required property 'minimum_count' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodepipelineCustomActionTypeInputArtifactDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodepipelineCustomActionTypeInputArtifactDetailsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codepipelineCustomActionType.CodepipelineCustomActionTypeInputArtifactDetailsOutputReference",
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
    @jsii.member(jsii_name="maximumCountInput")
    def maximum_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumCountInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumCountInput")
    def minimum_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumCountInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumCount")
    def maximum_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumCount"))

    @maximum_count.setter
    def maximum_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumCount", value)

    @builtins.property
    @jsii.member(jsii_name="minimumCount")
    def minimum_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumCount"))

    @minimum_count.setter
    def minimum_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodepipelineCustomActionTypeInputArtifactDetails]:
        return typing.cast(typing.Optional[CodepipelineCustomActionTypeInputArtifactDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodepipelineCustomActionTypeInputArtifactDetails],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodepipelineCustomActionTypeInputArtifactDetails],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codepipelineCustomActionType.CodepipelineCustomActionTypeOutputArtifactDetails",
    jsii_struct_bases=[],
    name_mapping={"maximum_count": "maximumCount", "minimum_count": "minimumCount"},
)
class CodepipelineCustomActionTypeOutputArtifactDetails:
    def __init__(
        self,
        *,
        maximum_count: jsii.Number,
        minimum_count: jsii.Number,
    ) -> None:
        '''
        :param maximum_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#maximum_count CodepipelineCustomActionType#maximum_count}.
        :param minimum_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#minimum_count CodepipelineCustomActionType#minimum_count}.
        '''
        if __debug__:
            def stub(*, maximum_count: jsii.Number, minimum_count: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument maximum_count", value=maximum_count, expected_type=type_hints["maximum_count"])
            check_type(argname="argument minimum_count", value=minimum_count, expected_type=type_hints["minimum_count"])
        self._values: typing.Dict[str, typing.Any] = {
            "maximum_count": maximum_count,
            "minimum_count": minimum_count,
        }

    @builtins.property
    def maximum_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#maximum_count CodepipelineCustomActionType#maximum_count}.'''
        result = self._values.get("maximum_count")
        assert result is not None, "Required property 'maximum_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def minimum_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#minimum_count CodepipelineCustomActionType#minimum_count}.'''
        result = self._values.get("minimum_count")
        assert result is not None, "Required property 'minimum_count' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodepipelineCustomActionTypeOutputArtifactDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodepipelineCustomActionTypeOutputArtifactDetailsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codepipelineCustomActionType.CodepipelineCustomActionTypeOutputArtifactDetailsOutputReference",
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
    @jsii.member(jsii_name="maximumCountInput")
    def maximum_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumCountInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumCountInput")
    def minimum_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumCountInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumCount")
    def maximum_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumCount"))

    @maximum_count.setter
    def maximum_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumCount", value)

    @builtins.property
    @jsii.member(jsii_name="minimumCount")
    def minimum_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumCount"))

    @minimum_count.setter
    def minimum_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodepipelineCustomActionTypeOutputArtifactDetails]:
        return typing.cast(typing.Optional[CodepipelineCustomActionTypeOutputArtifactDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodepipelineCustomActionTypeOutputArtifactDetails],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodepipelineCustomActionTypeOutputArtifactDetails],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codepipelineCustomActionType.CodepipelineCustomActionTypeSettings",
    jsii_struct_bases=[],
    name_mapping={
        "entity_url_template": "entityUrlTemplate",
        "execution_url_template": "executionUrlTemplate",
        "revision_url_template": "revisionUrlTemplate",
        "third_party_configuration_url": "thirdPartyConfigurationUrl",
    },
)
class CodepipelineCustomActionTypeSettings:
    def __init__(
        self,
        *,
        entity_url_template: typing.Optional[builtins.str] = None,
        execution_url_template: typing.Optional[builtins.str] = None,
        revision_url_template: typing.Optional[builtins.str] = None,
        third_party_configuration_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param entity_url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#entity_url_template CodepipelineCustomActionType#entity_url_template}.
        :param execution_url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#execution_url_template CodepipelineCustomActionType#execution_url_template}.
        :param revision_url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#revision_url_template CodepipelineCustomActionType#revision_url_template}.
        :param third_party_configuration_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#third_party_configuration_url CodepipelineCustomActionType#third_party_configuration_url}.
        '''
        if __debug__:
            def stub(
                *,
                entity_url_template: typing.Optional[builtins.str] = None,
                execution_url_template: typing.Optional[builtins.str] = None,
                revision_url_template: typing.Optional[builtins.str] = None,
                third_party_configuration_url: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument entity_url_template", value=entity_url_template, expected_type=type_hints["entity_url_template"])
            check_type(argname="argument execution_url_template", value=execution_url_template, expected_type=type_hints["execution_url_template"])
            check_type(argname="argument revision_url_template", value=revision_url_template, expected_type=type_hints["revision_url_template"])
            check_type(argname="argument third_party_configuration_url", value=third_party_configuration_url, expected_type=type_hints["third_party_configuration_url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if entity_url_template is not None:
            self._values["entity_url_template"] = entity_url_template
        if execution_url_template is not None:
            self._values["execution_url_template"] = execution_url_template
        if revision_url_template is not None:
            self._values["revision_url_template"] = revision_url_template
        if third_party_configuration_url is not None:
            self._values["third_party_configuration_url"] = third_party_configuration_url

    @builtins.property
    def entity_url_template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#entity_url_template CodepipelineCustomActionType#entity_url_template}.'''
        result = self._values.get("entity_url_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_url_template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#execution_url_template CodepipelineCustomActionType#execution_url_template}.'''
        result = self._values.get("execution_url_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def revision_url_template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#revision_url_template CodepipelineCustomActionType#revision_url_template}.'''
        result = self._values.get("revision_url_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def third_party_configuration_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codepipeline_custom_action_type#third_party_configuration_url CodepipelineCustomActionType#third_party_configuration_url}.'''
        result = self._values.get("third_party_configuration_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodepipelineCustomActionTypeSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodepipelineCustomActionTypeSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codepipelineCustomActionType.CodepipelineCustomActionTypeSettingsOutputReference",
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

    @jsii.member(jsii_name="resetEntityUrlTemplate")
    def reset_entity_url_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntityUrlTemplate", []))

    @jsii.member(jsii_name="resetExecutionUrlTemplate")
    def reset_execution_url_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutionUrlTemplate", []))

    @jsii.member(jsii_name="resetRevisionUrlTemplate")
    def reset_revision_url_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRevisionUrlTemplate", []))

    @jsii.member(jsii_name="resetThirdPartyConfigurationUrl")
    def reset_third_party_configuration_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThirdPartyConfigurationUrl", []))

    @builtins.property
    @jsii.member(jsii_name="entityUrlTemplateInput")
    def entity_url_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entityUrlTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="executionUrlTemplateInput")
    def execution_url_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionUrlTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="revisionUrlTemplateInput")
    def revision_url_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "revisionUrlTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="thirdPartyConfigurationUrlInput")
    def third_party_configuration_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thirdPartyConfigurationUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="entityUrlTemplate")
    def entity_url_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "entityUrlTemplate"))

    @entity_url_template.setter
    def entity_url_template(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityUrlTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="executionUrlTemplate")
    def execution_url_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionUrlTemplate"))

    @execution_url_template.setter
    def execution_url_template(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionUrlTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="revisionUrlTemplate")
    def revision_url_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "revisionUrlTemplate"))

    @revision_url_template.setter
    def revision_url_template(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revisionUrlTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="thirdPartyConfigurationUrl")
    def third_party_configuration_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thirdPartyConfigurationUrl"))

    @third_party_configuration_url.setter
    def third_party_configuration_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thirdPartyConfigurationUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodepipelineCustomActionTypeSettings]:
        return typing.cast(typing.Optional[CodepipelineCustomActionTypeSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodepipelineCustomActionTypeSettings],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodepipelineCustomActionTypeSettings],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CodepipelineCustomActionType",
    "CodepipelineCustomActionTypeConfig",
    "CodepipelineCustomActionTypeConfigurationProperty",
    "CodepipelineCustomActionTypeConfigurationPropertyList",
    "CodepipelineCustomActionTypeConfigurationPropertyOutputReference",
    "CodepipelineCustomActionTypeInputArtifactDetails",
    "CodepipelineCustomActionTypeInputArtifactDetailsOutputReference",
    "CodepipelineCustomActionTypeOutputArtifactDetails",
    "CodepipelineCustomActionTypeOutputArtifactDetailsOutputReference",
    "CodepipelineCustomActionTypeSettings",
    "CodepipelineCustomActionTypeSettingsOutputReference",
]

publication.publish()
