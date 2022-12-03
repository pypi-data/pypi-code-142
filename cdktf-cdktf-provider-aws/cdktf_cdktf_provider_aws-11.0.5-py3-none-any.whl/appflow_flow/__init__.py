'''
# `aws_appflow_flow`

Refer to the Terraform Registory for docs: [`aws_appflow_flow`](https://www.terraform.io/docs/providers/aws/r/appflow_flow).
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


class AppflowFlow(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlow",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow aws_appflow_flow}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        destination_flow_config: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppflowFlowDestinationFlowConfig", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        source_flow_config: typing.Union["AppflowFlowSourceFlowConfig", typing.Dict[str, typing.Any]],
        task: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppflowFlowTask", typing.Dict[str, typing.Any]]]],
        trigger_config: typing.Union["AppflowFlowTriggerConfig", typing.Dict[str, typing.Any]],
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_arn: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow aws_appflow_flow} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param destination_flow_config: destination_flow_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#destination_flow_config AppflowFlow#destination_flow_config}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#name AppflowFlow#name}.
        :param source_flow_config: source_flow_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#source_flow_config AppflowFlow#source_flow_config}
        :param task: task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#task AppflowFlow#task}
        :param trigger_config: trigger_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trigger_config AppflowFlow#trigger_config}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#description AppflowFlow#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id AppflowFlow#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#kms_arn AppflowFlow#kms_arn}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#tags AppflowFlow#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#tags_all AppflowFlow#tags_all}.
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
                destination_flow_config: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppflowFlowDestinationFlowConfig, typing.Dict[str, typing.Any]]]],
                name: builtins.str,
                source_flow_config: typing.Union[AppflowFlowSourceFlowConfig, typing.Dict[str, typing.Any]],
                task: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppflowFlowTask, typing.Dict[str, typing.Any]]]],
                trigger_config: typing.Union[AppflowFlowTriggerConfig, typing.Dict[str, typing.Any]],
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                kms_arn: typing.Optional[builtins.str] = None,
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
        config = AppflowFlowConfig(
            destination_flow_config=destination_flow_config,
            name=name,
            source_flow_config=source_flow_config,
            task=task,
            trigger_config=trigger_config,
            description=description,
            id=id,
            kms_arn=kms_arn,
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

    @jsii.member(jsii_name="putDestinationFlowConfig")
    def put_destination_flow_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppflowFlowDestinationFlowConfig", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppflowFlowDestinationFlowConfig, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDestinationFlowConfig", [value]))

    @jsii.member(jsii_name="putSourceFlowConfig")
    def put_source_flow_config(
        self,
        *,
        connector_type: builtins.str,
        source_connector_properties: typing.Union["AppflowFlowSourceFlowConfigSourceConnectorProperties", typing.Dict[str, typing.Any]],
        api_version: typing.Optional[builtins.str] = None,
        connector_profile_name: typing.Optional[builtins.str] = None,
        incremental_pull_config: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigIncrementalPullConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connector_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_type AppflowFlow#connector_type}.
        :param source_connector_properties: source_connector_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#source_connector_properties AppflowFlow#source_connector_properties}
        :param api_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#api_version AppflowFlow#api_version}.
        :param connector_profile_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_profile_name AppflowFlow#connector_profile_name}.
        :param incremental_pull_config: incremental_pull_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#incremental_pull_config AppflowFlow#incremental_pull_config}
        '''
        value = AppflowFlowSourceFlowConfig(
            connector_type=connector_type,
            source_connector_properties=source_connector_properties,
            api_version=api_version,
            connector_profile_name=connector_profile_name,
            incremental_pull_config=incremental_pull_config,
        )

        return typing.cast(None, jsii.invoke(self, "putSourceFlowConfig", [value]))

    @jsii.member(jsii_name="putTask")
    def put_task(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppflowFlowTask", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppflowFlowTask, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTask", [value]))

    @jsii.member(jsii_name="putTriggerConfig")
    def put_trigger_config(
        self,
        *,
        trigger_type: builtins.str,
        trigger_properties: typing.Optional[typing.Union["AppflowFlowTriggerConfigTriggerProperties", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trigger_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trigger_type AppflowFlow#trigger_type}.
        :param trigger_properties: trigger_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trigger_properties AppflowFlow#trigger_properties}
        '''
        value = AppflowFlowTriggerConfig(
            trigger_type=trigger_type, trigger_properties=trigger_properties
        )

        return typing.cast(None, jsii.invoke(self, "putTriggerConfig", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsArn")
    def reset_kms_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsArn", []))

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
    @jsii.member(jsii_name="destinationFlowConfig")
    def destination_flow_config(self) -> "AppflowFlowDestinationFlowConfigList":
        return typing.cast("AppflowFlowDestinationFlowConfigList", jsii.get(self, "destinationFlowConfig"))

    @builtins.property
    @jsii.member(jsii_name="sourceFlowConfig")
    def source_flow_config(self) -> "AppflowFlowSourceFlowConfigOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigOutputReference", jsii.get(self, "sourceFlowConfig"))

    @builtins.property
    @jsii.member(jsii_name="task")
    def task(self) -> "AppflowFlowTaskList":
        return typing.cast("AppflowFlowTaskList", jsii.get(self, "task"))

    @builtins.property
    @jsii.member(jsii_name="triggerConfig")
    def trigger_config(self) -> "AppflowFlowTriggerConfigOutputReference":
        return typing.cast("AppflowFlowTriggerConfigOutputReference", jsii.get(self, "triggerConfig"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationFlowConfigInput")
    def destination_flow_config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppflowFlowDestinationFlowConfig"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppflowFlowDestinationFlowConfig"]]], jsii.get(self, "destinationFlowConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsArnInput")
    def kms_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsArnInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFlowConfigInput")
    def source_flow_config_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfig"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfig"], jsii.get(self, "sourceFlowConfigInput"))

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
    @jsii.member(jsii_name="taskInput")
    def task_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppflowFlowTask"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppflowFlowTask"]]], jsii.get(self, "taskInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerConfigInput")
    def trigger_config_input(self) -> typing.Optional["AppflowFlowTriggerConfig"]:
        return typing.cast(typing.Optional["AppflowFlowTriggerConfig"], jsii.get(self, "triggerConfigInput"))

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
    @jsii.member(jsii_name="kmsArn")
    def kms_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsArn"))

    @kms_arn.setter
    def kms_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsArn", value)

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
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "destination_flow_config": "destinationFlowConfig",
        "name": "name",
        "source_flow_config": "sourceFlowConfig",
        "task": "task",
        "trigger_config": "triggerConfig",
        "description": "description",
        "id": "id",
        "kms_arn": "kmsArn",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class AppflowFlowConfig(cdktf.TerraformMetaArguments):
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
        destination_flow_config: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppflowFlowDestinationFlowConfig", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        source_flow_config: typing.Union["AppflowFlowSourceFlowConfig", typing.Dict[str, typing.Any]],
        task: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppflowFlowTask", typing.Dict[str, typing.Any]]]],
        trigger_config: typing.Union["AppflowFlowTriggerConfig", typing.Dict[str, typing.Any]],
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_arn: typing.Optional[builtins.str] = None,
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
        :param destination_flow_config: destination_flow_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#destination_flow_config AppflowFlow#destination_flow_config}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#name AppflowFlow#name}.
        :param source_flow_config: source_flow_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#source_flow_config AppflowFlow#source_flow_config}
        :param task: task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#task AppflowFlow#task}
        :param trigger_config: trigger_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trigger_config AppflowFlow#trigger_config}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#description AppflowFlow#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id AppflowFlow#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#kms_arn AppflowFlow#kms_arn}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#tags AppflowFlow#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#tags_all AppflowFlow#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(source_flow_config, dict):
            source_flow_config = AppflowFlowSourceFlowConfig(**source_flow_config)
        if isinstance(trigger_config, dict):
            trigger_config = AppflowFlowTriggerConfig(**trigger_config)
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
                destination_flow_config: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppflowFlowDestinationFlowConfig, typing.Dict[str, typing.Any]]]],
                name: builtins.str,
                source_flow_config: typing.Union[AppflowFlowSourceFlowConfig, typing.Dict[str, typing.Any]],
                task: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppflowFlowTask, typing.Dict[str, typing.Any]]]],
                trigger_config: typing.Union[AppflowFlowTriggerConfig, typing.Dict[str, typing.Any]],
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                kms_arn: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument destination_flow_config", value=destination_flow_config, expected_type=type_hints["destination_flow_config"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_flow_config", value=source_flow_config, expected_type=type_hints["source_flow_config"])
            check_type(argname="argument task", value=task, expected_type=type_hints["task"])
            check_type(argname="argument trigger_config", value=trigger_config, expected_type=type_hints["trigger_config"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_arn", value=kms_arn, expected_type=type_hints["kms_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination_flow_config": destination_flow_config,
            "name": name,
            "source_flow_config": source_flow_config,
            "task": task,
            "trigger_config": trigger_config,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if kms_arn is not None:
            self._values["kms_arn"] = kms_arn
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
    def destination_flow_config(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["AppflowFlowDestinationFlowConfig"]]:
        '''destination_flow_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#destination_flow_config AppflowFlow#destination_flow_config}
        '''
        result = self._values.get("destination_flow_config")
        assert result is not None, "Required property 'destination_flow_config' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["AppflowFlowDestinationFlowConfig"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#name AppflowFlow#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_flow_config(self) -> "AppflowFlowSourceFlowConfig":
        '''source_flow_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#source_flow_config AppflowFlow#source_flow_config}
        '''
        result = self._values.get("source_flow_config")
        assert result is not None, "Required property 'source_flow_config' is missing"
        return typing.cast("AppflowFlowSourceFlowConfig", result)

    @builtins.property
    def task(self) -> typing.Union[cdktf.IResolvable, typing.List["AppflowFlowTask"]]:
        '''task block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#task AppflowFlow#task}
        '''
        result = self._values.get("task")
        assert result is not None, "Required property 'task' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["AppflowFlowTask"]], result)

    @builtins.property
    def trigger_config(self) -> "AppflowFlowTriggerConfig":
        '''trigger_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trigger_config AppflowFlow#trigger_config}
        '''
        result = self._values.get("trigger_config")
        assert result is not None, "Required property 'trigger_config' is missing"
        return typing.cast("AppflowFlowTriggerConfig", result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#description AppflowFlow#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id AppflowFlow#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#kms_arn AppflowFlow#kms_arn}.'''
        result = self._values.get("kms_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#tags AppflowFlow#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#tags_all AppflowFlow#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfig",
    jsii_struct_bases=[],
    name_mapping={
        "connector_type": "connectorType",
        "destination_connector_properties": "destinationConnectorProperties",
        "api_version": "apiVersion",
        "connector_profile_name": "connectorProfileName",
    },
)
class AppflowFlowDestinationFlowConfig:
    def __init__(
        self,
        *,
        connector_type: builtins.str,
        destination_connector_properties: typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorProperties", typing.Dict[str, typing.Any]],
        api_version: typing.Optional[builtins.str] = None,
        connector_profile_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connector_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_type AppflowFlow#connector_type}.
        :param destination_connector_properties: destination_connector_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#destination_connector_properties AppflowFlow#destination_connector_properties}
        :param api_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#api_version AppflowFlow#api_version}.
        :param connector_profile_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_profile_name AppflowFlow#connector_profile_name}.
        '''
        if isinstance(destination_connector_properties, dict):
            destination_connector_properties = AppflowFlowDestinationFlowConfigDestinationConnectorProperties(**destination_connector_properties)
        if __debug__:
            def stub(
                *,
                connector_type: builtins.str,
                destination_connector_properties: typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorProperties, typing.Dict[str, typing.Any]],
                api_version: typing.Optional[builtins.str] = None,
                connector_profile_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument connector_type", value=connector_type, expected_type=type_hints["connector_type"])
            check_type(argname="argument destination_connector_properties", value=destination_connector_properties, expected_type=type_hints["destination_connector_properties"])
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument connector_profile_name", value=connector_profile_name, expected_type=type_hints["connector_profile_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "connector_type": connector_type,
            "destination_connector_properties": destination_connector_properties,
        }
        if api_version is not None:
            self._values["api_version"] = api_version
        if connector_profile_name is not None:
            self._values["connector_profile_name"] = connector_profile_name

    @builtins.property
    def connector_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_type AppflowFlow#connector_type}.'''
        result = self._values.get("connector_type")
        assert result is not None, "Required property 'connector_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_connector_properties(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorProperties":
        '''destination_connector_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#destination_connector_properties AppflowFlow#destination_connector_properties}
        '''
        result = self._values.get("destination_connector_properties")
        assert result is not None, "Required property 'destination_connector_properties' is missing"
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorProperties", result)

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#api_version AppflowFlow#api_version}.'''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connector_profile_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_profile_name AppflowFlow#connector_profile_name}.'''
        result = self._values.get("connector_profile_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorProperties",
    jsii_struct_bases=[],
    name_mapping={
        "custom_connector": "customConnector",
        "customer_profiles": "customerProfiles",
        "event_bridge": "eventBridge",
        "honeycode": "honeycode",
        "lookout_metrics": "lookoutMetrics",
        "marketo": "marketo",
        "redshift": "redshift",
        "s3": "s3",
        "salesforce": "salesforce",
        "sapo_data": "sapoData",
        "snowflake": "snowflake",
        "upsolver": "upsolver",
        "zendesk": "zendesk",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorProperties:
    def __init__(
        self,
        *,
        custom_connector: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector", typing.Dict[str, typing.Any]]] = None,
        customer_profiles: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles", typing.Dict[str, typing.Any]]] = None,
        event_bridge: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge", typing.Dict[str, typing.Any]]] = None,
        honeycode: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode", typing.Dict[str, typing.Any]]] = None,
        lookout_metrics: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics", typing.Dict[str, typing.Any]]] = None,
        marketo: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo", typing.Dict[str, typing.Any]]] = None,
        redshift: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift", typing.Dict[str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3", typing.Dict[str, typing.Any]]] = None,
        salesforce: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce", typing.Dict[str, typing.Any]]] = None,
        sapo_data: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData", typing.Dict[str, typing.Any]]] = None,
        snowflake: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake", typing.Dict[str, typing.Any]]] = None,
        upsolver: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver", typing.Dict[str, typing.Any]]] = None,
        zendesk: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param custom_connector: custom_connector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_connector AppflowFlow#custom_connector}
        :param customer_profiles: customer_profiles block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#customer_profiles AppflowFlow#customer_profiles}
        :param event_bridge: event_bridge block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#event_bridge AppflowFlow#event_bridge}
        :param honeycode: honeycode block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#honeycode AppflowFlow#honeycode}
        :param lookout_metrics: lookout_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#lookout_metrics AppflowFlow#lookout_metrics}
        :param marketo: marketo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#marketo AppflowFlow#marketo}
        :param redshift: redshift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#redshift AppflowFlow#redshift}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3 AppflowFlow#s3}
        :param salesforce: salesforce block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#salesforce AppflowFlow#salesforce}
        :param sapo_data: sapo_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#sapo_data AppflowFlow#sapo_data}
        :param snowflake: snowflake block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#snowflake AppflowFlow#snowflake}
        :param upsolver: upsolver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#upsolver AppflowFlow#upsolver}
        :param zendesk: zendesk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#zendesk AppflowFlow#zendesk}
        '''
        if isinstance(custom_connector, dict):
            custom_connector = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector(**custom_connector)
        if isinstance(customer_profiles, dict):
            customer_profiles = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles(**customer_profiles)
        if isinstance(event_bridge, dict):
            event_bridge = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge(**event_bridge)
        if isinstance(honeycode, dict):
            honeycode = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode(**honeycode)
        if isinstance(lookout_metrics, dict):
            lookout_metrics = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics(**lookout_metrics)
        if isinstance(marketo, dict):
            marketo = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo(**marketo)
        if isinstance(redshift, dict):
            redshift = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift(**redshift)
        if isinstance(s3, dict):
            s3 = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3(**s3)
        if isinstance(salesforce, dict):
            salesforce = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce(**salesforce)
        if isinstance(sapo_data, dict):
            sapo_data = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData(**sapo_data)
        if isinstance(snowflake, dict):
            snowflake = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake(**snowflake)
        if isinstance(upsolver, dict):
            upsolver = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver(**upsolver)
        if isinstance(zendesk, dict):
            zendesk = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk(**zendesk)
        if __debug__:
            def stub(
                *,
                custom_connector: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector, typing.Dict[str, typing.Any]]] = None,
                customer_profiles: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles, typing.Dict[str, typing.Any]]] = None,
                event_bridge: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge, typing.Dict[str, typing.Any]]] = None,
                honeycode: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode, typing.Dict[str, typing.Any]]] = None,
                lookout_metrics: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics, typing.Dict[str, typing.Any]]] = None,
                marketo: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo, typing.Dict[str, typing.Any]]] = None,
                redshift: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift, typing.Dict[str, typing.Any]]] = None,
                s3: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3, typing.Dict[str, typing.Any]]] = None,
                salesforce: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce, typing.Dict[str, typing.Any]]] = None,
                sapo_data: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData, typing.Dict[str, typing.Any]]] = None,
                snowflake: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake, typing.Dict[str, typing.Any]]] = None,
                upsolver: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver, typing.Dict[str, typing.Any]]] = None,
                zendesk: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument custom_connector", value=custom_connector, expected_type=type_hints["custom_connector"])
            check_type(argname="argument customer_profiles", value=customer_profiles, expected_type=type_hints["customer_profiles"])
            check_type(argname="argument event_bridge", value=event_bridge, expected_type=type_hints["event_bridge"])
            check_type(argname="argument honeycode", value=honeycode, expected_type=type_hints["honeycode"])
            check_type(argname="argument lookout_metrics", value=lookout_metrics, expected_type=type_hints["lookout_metrics"])
            check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
            check_type(argname="argument redshift", value=redshift, expected_type=type_hints["redshift"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
            check_type(argname="argument sapo_data", value=sapo_data, expected_type=type_hints["sapo_data"])
            check_type(argname="argument snowflake", value=snowflake, expected_type=type_hints["snowflake"])
            check_type(argname="argument upsolver", value=upsolver, expected_type=type_hints["upsolver"])
            check_type(argname="argument zendesk", value=zendesk, expected_type=type_hints["zendesk"])
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_connector is not None:
            self._values["custom_connector"] = custom_connector
        if customer_profiles is not None:
            self._values["customer_profiles"] = customer_profiles
        if event_bridge is not None:
            self._values["event_bridge"] = event_bridge
        if honeycode is not None:
            self._values["honeycode"] = honeycode
        if lookout_metrics is not None:
            self._values["lookout_metrics"] = lookout_metrics
        if marketo is not None:
            self._values["marketo"] = marketo
        if redshift is not None:
            self._values["redshift"] = redshift
        if s3 is not None:
            self._values["s3"] = s3
        if salesforce is not None:
            self._values["salesforce"] = salesforce
        if sapo_data is not None:
            self._values["sapo_data"] = sapo_data
        if snowflake is not None:
            self._values["snowflake"] = snowflake
        if upsolver is not None:
            self._values["upsolver"] = upsolver
        if zendesk is not None:
            self._values["zendesk"] = zendesk

    @builtins.property
    def custom_connector(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector"]:
        '''custom_connector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_connector AppflowFlow#custom_connector}
        '''
        result = self._values.get("custom_connector")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector"], result)

    @builtins.property
    def customer_profiles(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles"]:
        '''customer_profiles block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#customer_profiles AppflowFlow#customer_profiles}
        '''
        result = self._values.get("customer_profiles")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles"], result)

    @builtins.property
    def event_bridge(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge"]:
        '''event_bridge block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#event_bridge AppflowFlow#event_bridge}
        '''
        result = self._values.get("event_bridge")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge"], result)

    @builtins.property
    def honeycode(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode"]:
        '''honeycode block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#honeycode AppflowFlow#honeycode}
        '''
        result = self._values.get("honeycode")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode"], result)

    @builtins.property
    def lookout_metrics(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics"]:
        '''lookout_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#lookout_metrics AppflowFlow#lookout_metrics}
        '''
        result = self._values.get("lookout_metrics")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics"], result)

    @builtins.property
    def marketo(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo"]:
        '''marketo block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#marketo AppflowFlow#marketo}
        '''
        result = self._values.get("marketo")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo"], result)

    @builtins.property
    def redshift(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift"]:
        '''redshift block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#redshift AppflowFlow#redshift}
        '''
        result = self._values.get("redshift")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift"], result)

    @builtins.property
    def s3(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3 AppflowFlow#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3"], result)

    @builtins.property
    def salesforce(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce"]:
        '''salesforce block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#salesforce AppflowFlow#salesforce}
        '''
        result = self._values.get("salesforce")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce"], result)

    @builtins.property
    def sapo_data(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData"]:
        '''sapo_data block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#sapo_data AppflowFlow#sapo_data}
        '''
        result = self._values.get("sapo_data")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData"], result)

    @builtins.property
    def snowflake(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake"]:
        '''snowflake block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#snowflake AppflowFlow#snowflake}
        '''
        result = self._values.get("snowflake")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake"], result)

    @builtins.property
    def upsolver(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver"]:
        '''upsolver block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#upsolver AppflowFlow#upsolver}
        '''
        result = self._values.get("upsolver")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver"], result)

    @builtins.property
    def zendesk(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk"]:
        '''zendesk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#zendesk AppflowFlow#zendesk}
        '''
        result = self._values.get("zendesk")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector",
    jsii_struct_bases=[],
    name_mapping={
        "entity_name": "entityName",
        "custom_properties": "customProperties",
        "error_handling_config": "errorHandlingConfig",
        "id_field_names": "idFieldNames",
        "write_operation_type": "writeOperationType",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector:
    def __init__(
        self,
        *,
        entity_name: builtins.str,
        custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig", typing.Dict[str, typing.Any]]] = None,
        id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        write_operation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param entity_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#entity_name AppflowFlow#entity_name}.
        :param custom_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_properties AppflowFlow#custom_properties}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        :param id_field_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.
        :param write_operation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.
        '''
        if isinstance(error_handling_config, dict):
            error_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig(**error_handling_config)
        if __debug__:
            def stub(
                *,
                entity_name: builtins.str,
                custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig, typing.Dict[str, typing.Any]]] = None,
                id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
                write_operation_type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument entity_name", value=entity_name, expected_type=type_hints["entity_name"])
            check_type(argname="argument custom_properties", value=custom_properties, expected_type=type_hints["custom_properties"])
            check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
            check_type(argname="argument id_field_names", value=id_field_names, expected_type=type_hints["id_field_names"])
            check_type(argname="argument write_operation_type", value=write_operation_type, expected_type=type_hints["write_operation_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "entity_name": entity_name,
        }
        if custom_properties is not None:
            self._values["custom_properties"] = custom_properties
        if error_handling_config is not None:
            self._values["error_handling_config"] = error_handling_config
        if id_field_names is not None:
            self._values["id_field_names"] = id_field_names
        if write_operation_type is not None:
            self._values["write_operation_type"] = write_operation_type

    @builtins.property
    def entity_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#entity_name AppflowFlow#entity_name}.'''
        result = self._values.get("entity_name")
        assert result is not None, "Required property 'entity_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_properties AppflowFlow#custom_properties}.'''
        result = self._values.get("custom_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def error_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig"]:
        '''error_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        result = self._values.get("error_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig"], result)

    @builtins.property
    def id_field_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.'''
        result = self._values.get("id_field_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def write_operation_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.'''
        result = self._values.get("write_operation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "fail_on_first_destination_error": "failOnFirstDestinationError",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        if __debug__:
            def stub(
                *,
                bucket_name: typing.Optional[builtins.str] = None,
                bucket_prefix: typing.Optional[builtins.str] = None,
                fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument fail_on_first_destination_error", value=fail_on_first_destination_error, expected_type=type_hints["fail_on_first_destination_error"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if fail_on_first_destination_error is not None:
            self._values["fail_on_first_destination_error"] = fail_on_first_destination_error

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_on_first_destination_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.'''
        result = self._values.get("fail_on_first_destination_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfigOutputReference",
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

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetFailOnFirstDestinationError")
    def reset_fail_on_first_destination_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailOnFirstDestinationError", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationErrorInput")
    def fail_on_first_destination_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "failOnFirstDestinationErrorInput"))

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
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationError")
    def fail_on_first_destination_error(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "failOnFirstDestinationError"))

    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnFirstDestinationError", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorOutputReference",
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

    @jsii.member(jsii_name="putErrorHandlingConfig")
    def put_error_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            fail_on_first_destination_error=fail_on_first_destination_error,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorHandlingConfig", [value]))

    @jsii.member(jsii_name="resetCustomProperties")
    def reset_custom_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomProperties", []))

    @jsii.member(jsii_name="resetErrorHandlingConfig")
    def reset_error_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorHandlingConfig", []))

    @jsii.member(jsii_name="resetIdFieldNames")
    def reset_id_field_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdFieldNames", []))

    @jsii.member(jsii_name="resetWriteOperationType")
    def reset_write_operation_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteOperationType", []))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfigOutputReference, jsii.get(self, "errorHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="customPropertiesInput")
    def custom_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="entityNameInput")
    def entity_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entityNameInput"))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfigInput")
    def error_handling_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig], jsii.get(self, "errorHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idFieldNamesInput")
    def id_field_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "idFieldNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="writeOperationTypeInput")
    def write_operation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "writeOperationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="customProperties")
    def custom_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "customProperties"))

    @custom_properties.setter
    def custom_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customProperties", value)

    @builtins.property
    @jsii.member(jsii_name="entityName")
    def entity_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "entityName"))

    @entity_name.setter
    def entity_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityName", value)

    @builtins.property
    @jsii.member(jsii_name="idFieldNames")
    def id_field_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "idFieldNames"))

    @id_field_names.setter
    def id_field_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idFieldNames", value)

    @builtins.property
    @jsii.member(jsii_name="writeOperationType")
    def write_operation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "writeOperationType"))

    @write_operation_type.setter
    def write_operation_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeOperationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles",
    jsii_struct_bases=[],
    name_mapping={"domain_name": "domainName", "object_type_name": "objectTypeName"},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        object_type_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#domain_name AppflowFlow#domain_name}.
        :param object_type_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object_type_name AppflowFlow#object_type_name}.
        '''
        if __debug__:
            def stub(
                *,
                domain_name: builtins.str,
                object_type_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument object_type_name", value=object_type_name, expected_type=type_hints["object_type_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
        }
        if object_type_name is not None:
            self._values["object_type_name"] = object_type_name

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#domain_name AppflowFlow#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object_type_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object_type_name AppflowFlow#object_type_name}.'''
        result = self._values.get("object_type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfilesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfilesOutputReference",
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

    @jsii.member(jsii_name="resetObjectTypeName")
    def reset_object_type_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectTypeName", []))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="objectTypeNameInput")
    def object_type_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectTypeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="objectTypeName")
    def object_type_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectTypeName"))

    @object_type_name.setter
    def object_type_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectTypeName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge",
    jsii_struct_bases=[],
    name_mapping={"object": "object", "error_handling_config": "errorHandlingConfig"},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge:
    def __init__(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        if isinstance(error_handling_config, dict):
            error_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig(**error_handling_config)
        if __debug__:
            def stub(
                *,
                object: builtins.str,
                error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }
        if error_handling_config is not None:
            self._values["error_handling_config"] = error_handling_config

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig"]:
        '''error_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        result = self._values.get("error_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "fail_on_first_destination_error": "failOnFirstDestinationError",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        if __debug__:
            def stub(
                *,
                bucket_name: typing.Optional[builtins.str] = None,
                bucket_prefix: typing.Optional[builtins.str] = None,
                fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument fail_on_first_destination_error", value=fail_on_first_destination_error, expected_type=type_hints["fail_on_first_destination_error"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if fail_on_first_destination_error is not None:
            self._values["fail_on_first_destination_error"] = fail_on_first_destination_error

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_on_first_destination_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.'''
        result = self._values.get("fail_on_first_destination_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfigOutputReference",
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

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetFailOnFirstDestinationError")
    def reset_fail_on_first_destination_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailOnFirstDestinationError", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationErrorInput")
    def fail_on_first_destination_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "failOnFirstDestinationErrorInput"))

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
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationError")
    def fail_on_first_destination_error(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "failOnFirstDestinationError"))

    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnFirstDestinationError", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeOutputReference",
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

    @jsii.member(jsii_name="putErrorHandlingConfig")
    def put_error_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            fail_on_first_destination_error=fail_on_first_destination_error,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorHandlingConfig", [value]))

    @jsii.member(jsii_name="resetErrorHandlingConfig")
    def reset_error_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorHandlingConfig", []))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfigOutputReference, jsii.get(self, "errorHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfigInput")
    def error_handling_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig], jsii.get(self, "errorHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode",
    jsii_struct_bases=[],
    name_mapping={"object": "object", "error_handling_config": "errorHandlingConfig"},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode:
    def __init__(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        if isinstance(error_handling_config, dict):
            error_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig(**error_handling_config)
        if __debug__:
            def stub(
                *,
                object: builtins.str,
                error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }
        if error_handling_config is not None:
            self._values["error_handling_config"] = error_handling_config

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig"]:
        '''error_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        result = self._values.get("error_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "fail_on_first_destination_error": "failOnFirstDestinationError",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        if __debug__:
            def stub(
                *,
                bucket_name: typing.Optional[builtins.str] = None,
                bucket_prefix: typing.Optional[builtins.str] = None,
                fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument fail_on_first_destination_error", value=fail_on_first_destination_error, expected_type=type_hints["fail_on_first_destination_error"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if fail_on_first_destination_error is not None:
            self._values["fail_on_first_destination_error"] = fail_on_first_destination_error

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_on_first_destination_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.'''
        result = self._values.get("fail_on_first_destination_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfigOutputReference",
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

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetFailOnFirstDestinationError")
    def reset_fail_on_first_destination_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailOnFirstDestinationError", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationErrorInput")
    def fail_on_first_destination_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "failOnFirstDestinationErrorInput"))

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
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationError")
    def fail_on_first_destination_error(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "failOnFirstDestinationError"))

    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnFirstDestinationError", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeOutputReference",
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

    @jsii.member(jsii_name="putErrorHandlingConfig")
    def put_error_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            fail_on_first_destination_error=fail_on_first_destination_error,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorHandlingConfig", [value]))

    @jsii.member(jsii_name="resetErrorHandlingConfig")
    def reset_error_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorHandlingConfig", []))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfigOutputReference, jsii.get(self, "errorHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfigInput")
    def error_handling_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig], jsii.get(self, "errorHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics",
    jsii_struct_bases=[],
    name_mapping={},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetricsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetricsOutputReference",
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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo",
    jsii_struct_bases=[],
    name_mapping={"object": "object", "error_handling_config": "errorHandlingConfig"},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo:
    def __init__(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        if isinstance(error_handling_config, dict):
            error_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig(**error_handling_config)
        if __debug__:
            def stub(
                *,
                object: builtins.str,
                error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }
        if error_handling_config is not None:
            self._values["error_handling_config"] = error_handling_config

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig"]:
        '''error_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        result = self._values.get("error_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "fail_on_first_destination_error": "failOnFirstDestinationError",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        if __debug__:
            def stub(
                *,
                bucket_name: typing.Optional[builtins.str] = None,
                bucket_prefix: typing.Optional[builtins.str] = None,
                fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument fail_on_first_destination_error", value=fail_on_first_destination_error, expected_type=type_hints["fail_on_first_destination_error"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if fail_on_first_destination_error is not None:
            self._values["fail_on_first_destination_error"] = fail_on_first_destination_error

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_on_first_destination_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.'''
        result = self._values.get("fail_on_first_destination_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfigOutputReference",
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

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetFailOnFirstDestinationError")
    def reset_fail_on_first_destination_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailOnFirstDestinationError", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationErrorInput")
    def fail_on_first_destination_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "failOnFirstDestinationErrorInput"))

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
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationError")
    def fail_on_first_destination_error(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "failOnFirstDestinationError"))

    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnFirstDestinationError", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoOutputReference",
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

    @jsii.member(jsii_name="putErrorHandlingConfig")
    def put_error_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            fail_on_first_destination_error=fail_on_first_destination_error,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorHandlingConfig", [value]))

    @jsii.member(jsii_name="resetErrorHandlingConfig")
    def reset_error_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorHandlingConfig", []))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfigOutputReference, jsii.get(self, "errorHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfigInput")
    def error_handling_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig], jsii.get(self, "errorHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesOutputReference",
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

    @jsii.member(jsii_name="putCustomConnector")
    def put_custom_connector(
        self,
        *,
        entity_name: builtins.str,
        custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig, typing.Dict[str, typing.Any]]] = None,
        id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        write_operation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param entity_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#entity_name AppflowFlow#entity_name}.
        :param custom_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_properties AppflowFlow#custom_properties}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        :param id_field_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.
        :param write_operation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector(
            entity_name=entity_name,
            custom_properties=custom_properties,
            error_handling_config=error_handling_config,
            id_field_names=id_field_names,
            write_operation_type=write_operation_type,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomConnector", [value]))

    @jsii.member(jsii_name="putCustomerProfiles")
    def put_customer_profiles(
        self,
        *,
        domain_name: builtins.str,
        object_type_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#domain_name AppflowFlow#domain_name}.
        :param object_type_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object_type_name AppflowFlow#object_type_name}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles(
            domain_name=domain_name, object_type_name=object_type_name
        )

        return typing.cast(None, jsii.invoke(self, "putCustomerProfiles", [value]))

    @jsii.member(jsii_name="putEventBridge")
    def put_event_bridge(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge(
            object=object, error_handling_config=error_handling_config
        )

        return typing.cast(None, jsii.invoke(self, "putEventBridge", [value]))

    @jsii.member(jsii_name="putHoneycode")
    def put_honeycode(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode(
            object=object, error_handling_config=error_handling_config
        )

        return typing.cast(None, jsii.invoke(self, "putHoneycode", [value]))

    @jsii.member(jsii_name="putLookoutMetrics")
    def put_lookout_metrics(self) -> None:
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics()

        return typing.cast(None, jsii.invoke(self, "putLookoutMetrics", [value]))

    @jsii.member(jsii_name="putMarketo")
    def put_marketo(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo(
            object=object, error_handling_config=error_handling_config
        )

        return typing.cast(None, jsii.invoke(self, "putMarketo", [value]))

    @jsii.member(jsii_name="putRedshift")
    def put_redshift(
        self,
        *,
        intermediate_bucket_name: builtins.str,
        object: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param intermediate_bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#intermediate_bucket_name AppflowFlow#intermediate_bucket_name}.
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift(
            intermediate_bucket_name=intermediate_bucket_name,
            object=object,
            bucket_prefix=bucket_prefix,
            error_handling_config=error_handling_config,
        )

        return typing.cast(None, jsii.invoke(self, "putRedshift", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        bucket_name: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        s3_output_format_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param s3_output_format_config: s3_output_format_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_output_format_config AppflowFlow#s3_output_format_config}
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            s3_output_format_config=s3_output_format_config,
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="putSalesforce")
    def put_salesforce(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig", typing.Dict[str, typing.Any]]] = None,
        id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        write_operation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        :param id_field_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.
        :param write_operation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce(
            object=object,
            error_handling_config=error_handling_config,
            id_field_names=id_field_names,
            write_operation_type=write_operation_type,
        )

        return typing.cast(None, jsii.invoke(self, "putSalesforce", [value]))

    @jsii.member(jsii_name="putSapoData")
    def put_sapo_data(
        self,
        *,
        object_path: builtins.str,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig", typing.Dict[str, typing.Any]]] = None,
        id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        success_response_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig", typing.Dict[str, typing.Any]]] = None,
        write_operation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param object_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object_path AppflowFlow#object_path}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        :param id_field_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.
        :param success_response_handling_config: success_response_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#success_response_handling_config AppflowFlow#success_response_handling_config}
        :param write_operation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData(
            object_path=object_path,
            error_handling_config=error_handling_config,
            id_field_names=id_field_names,
            success_response_handling_config=success_response_handling_config,
            write_operation_type=write_operation_type,
        )

        return typing.cast(None, jsii.invoke(self, "putSapoData", [value]))

    @jsii.member(jsii_name="putSnowflake")
    def put_snowflake(
        self,
        *,
        intermediate_bucket_name: builtins.str,
        object: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param intermediate_bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#intermediate_bucket_name AppflowFlow#intermediate_bucket_name}.
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake(
            intermediate_bucket_name=intermediate_bucket_name,
            object=object,
            bucket_prefix=bucket_prefix,
            error_handling_config=error_handling_config,
        )

        return typing.cast(None, jsii.invoke(self, "putSnowflake", [value]))

    @jsii.member(jsii_name="putUpsolver")
    def put_upsolver(
        self,
        *,
        bucket_name: builtins.str,
        s3_output_format_config: typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig", typing.Dict[str, typing.Any]],
        bucket_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param s3_output_format_config: s3_output_format_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_output_format_config AppflowFlow#s3_output_format_config}
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver(
            bucket_name=bucket_name,
            s3_output_format_config=s3_output_format_config,
            bucket_prefix=bucket_prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putUpsolver", [value]))

    @jsii.member(jsii_name="putZendesk")
    def put_zendesk(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig", typing.Dict[str, typing.Any]]] = None,
        id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        write_operation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        :param id_field_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.
        :param write_operation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk(
            object=object,
            error_handling_config=error_handling_config,
            id_field_names=id_field_names,
            write_operation_type=write_operation_type,
        )

        return typing.cast(None, jsii.invoke(self, "putZendesk", [value]))

    @jsii.member(jsii_name="resetCustomConnector")
    def reset_custom_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomConnector", []))

    @jsii.member(jsii_name="resetCustomerProfiles")
    def reset_customer_profiles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomerProfiles", []))

    @jsii.member(jsii_name="resetEventBridge")
    def reset_event_bridge(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventBridge", []))

    @jsii.member(jsii_name="resetHoneycode")
    def reset_honeycode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHoneycode", []))

    @jsii.member(jsii_name="resetLookoutMetrics")
    def reset_lookout_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLookoutMetrics", []))

    @jsii.member(jsii_name="resetMarketo")
    def reset_marketo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMarketo", []))

    @jsii.member(jsii_name="resetRedshift")
    def reset_redshift(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedshift", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @jsii.member(jsii_name="resetSalesforce")
    def reset_salesforce(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSalesforce", []))

    @jsii.member(jsii_name="resetSapoData")
    def reset_sapo_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSapoData", []))

    @jsii.member(jsii_name="resetSnowflake")
    def reset_snowflake(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnowflake", []))

    @jsii.member(jsii_name="resetUpsolver")
    def reset_upsolver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpsolver", []))

    @jsii.member(jsii_name="resetZendesk")
    def reset_zendesk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZendesk", []))

    @builtins.property
    @jsii.member(jsii_name="customConnector")
    def custom_connector(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorOutputReference, jsii.get(self, "customConnector"))

    @builtins.property
    @jsii.member(jsii_name="customerProfiles")
    def customer_profiles(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfilesOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfilesOutputReference, jsii.get(self, "customerProfiles"))

    @builtins.property
    @jsii.member(jsii_name="eventBridge")
    def event_bridge(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeOutputReference, jsii.get(self, "eventBridge"))

    @builtins.property
    @jsii.member(jsii_name="honeycode")
    def honeycode(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeOutputReference, jsii.get(self, "honeycode"))

    @builtins.property
    @jsii.member(jsii_name="lookoutMetrics")
    def lookout_metrics(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetricsOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetricsOutputReference, jsii.get(self, "lookoutMetrics"))

    @builtins.property
    @jsii.member(jsii_name="marketo")
    def marketo(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoOutputReference, jsii.get(self, "marketo"))

    @builtins.property
    @jsii.member(jsii_name="redshift")
    def redshift(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftOutputReference", jsii.get(self, "redshift"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3OutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="salesforce")
    def salesforce(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceOutputReference", jsii.get(self, "salesforce"))

    @builtins.property
    @jsii.member(jsii_name="sapoData")
    def sapo_data(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataOutputReference", jsii.get(self, "sapoData"))

    @builtins.property
    @jsii.member(jsii_name="snowflake")
    def snowflake(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeOutputReference", jsii.get(self, "snowflake"))

    @builtins.property
    @jsii.member(jsii_name="upsolver")
    def upsolver(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverOutputReference", jsii.get(self, "upsolver"))

    @builtins.property
    @jsii.member(jsii_name="zendesk")
    def zendesk(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskOutputReference", jsii.get(self, "zendesk"))

    @builtins.property
    @jsii.member(jsii_name="customConnectorInput")
    def custom_connector_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector], jsii.get(self, "customConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="customerProfilesInput")
    def customer_profiles_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles], jsii.get(self, "customerProfilesInput"))

    @builtins.property
    @jsii.member(jsii_name="eventBridgeInput")
    def event_bridge_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge], jsii.get(self, "eventBridgeInput"))

    @builtins.property
    @jsii.member(jsii_name="honeycodeInput")
    def honeycode_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode], jsii.get(self, "honeycodeInput"))

    @builtins.property
    @jsii.member(jsii_name="lookoutMetricsInput")
    def lookout_metrics_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics], jsii.get(self, "lookoutMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="marketoInput")
    def marketo_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo], jsii.get(self, "marketoInput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftInput")
    def redshift_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift"], jsii.get(self, "redshiftInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="salesforceInput")
    def salesforce_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce"], jsii.get(self, "salesforceInput"))

    @builtins.property
    @jsii.member(jsii_name="sapoDataInput")
    def sapo_data_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData"], jsii.get(self, "sapoDataInput"))

    @builtins.property
    @jsii.member(jsii_name="snowflakeInput")
    def snowflake_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake"], jsii.get(self, "snowflakeInput"))

    @builtins.property
    @jsii.member(jsii_name="upsolverInput")
    def upsolver_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver"], jsii.get(self, "upsolverInput"))

    @builtins.property
    @jsii.member(jsii_name="zendeskInput")
    def zendesk_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk"], jsii.get(self, "zendeskInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorProperties]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorProperties],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorProperties],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift",
    jsii_struct_bases=[],
    name_mapping={
        "intermediate_bucket_name": "intermediateBucketName",
        "object": "object",
        "bucket_prefix": "bucketPrefix",
        "error_handling_config": "errorHandlingConfig",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift:
    def __init__(
        self,
        *,
        intermediate_bucket_name: builtins.str,
        object: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param intermediate_bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#intermediate_bucket_name AppflowFlow#intermediate_bucket_name}.
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        if isinstance(error_handling_config, dict):
            error_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig(**error_handling_config)
        if __debug__:
            def stub(
                *,
                intermediate_bucket_name: builtins.str,
                object: builtins.str,
                bucket_prefix: typing.Optional[builtins.str] = None,
                error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument intermediate_bucket_name", value=intermediate_bucket_name, expected_type=type_hints["intermediate_bucket_name"])
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "intermediate_bucket_name": intermediate_bucket_name,
            "object": object,
        }
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if error_handling_config is not None:
            self._values["error_handling_config"] = error_handling_config

    @builtins.property
    def intermediate_bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#intermediate_bucket_name AppflowFlow#intermediate_bucket_name}.'''
        result = self._values.get("intermediate_bucket_name")
        assert result is not None, "Required property 'intermediate_bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig"]:
        '''error_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        result = self._values.get("error_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "fail_on_first_destination_error": "failOnFirstDestinationError",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        if __debug__:
            def stub(
                *,
                bucket_name: typing.Optional[builtins.str] = None,
                bucket_prefix: typing.Optional[builtins.str] = None,
                fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument fail_on_first_destination_error", value=fail_on_first_destination_error, expected_type=type_hints["fail_on_first_destination_error"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if fail_on_first_destination_error is not None:
            self._values["fail_on_first_destination_error"] = fail_on_first_destination_error

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_on_first_destination_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.'''
        result = self._values.get("fail_on_first_destination_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfigOutputReference",
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

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetFailOnFirstDestinationError")
    def reset_fail_on_first_destination_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailOnFirstDestinationError", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationErrorInput")
    def fail_on_first_destination_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "failOnFirstDestinationErrorInput"))

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
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationError")
    def fail_on_first_destination_error(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "failOnFirstDestinationError"))

    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnFirstDestinationError", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftOutputReference",
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

    @jsii.member(jsii_name="putErrorHandlingConfig")
    def put_error_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            fail_on_first_destination_error=fail_on_first_destination_error,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorHandlingConfig", [value]))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetErrorHandlingConfig")
    def reset_error_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorHandlingConfig", []))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfigOutputReference, jsii.get(self, "errorHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfigInput")
    def error_handling_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig], jsii.get(self, "errorHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="intermediateBucketNameInput")
    def intermediate_bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intermediateBucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="intermediateBucketName")
    def intermediate_bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intermediateBucketName"))

    @intermediate_bucket_name.setter
    def intermediate_bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intermediateBucketName", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "s3_output_format_config": "s3OutputFormatConfig",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        s3_output_format_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param s3_output_format_config: s3_output_format_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_output_format_config AppflowFlow#s3_output_format_config}
        '''
        if isinstance(s3_output_format_config, dict):
            s3_output_format_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig(**s3_output_format_config)
        if __debug__:
            def stub(
                *,
                bucket_name: builtins.str,
                bucket_prefix: typing.Optional[builtins.str] = None,
                s3_output_format_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument s3_output_format_config", value=s3_output_format_config, expected_type=type_hints["s3_output_format_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
        }
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if s3_output_format_config is not None:
            self._values["s3_output_format_config"] = s3_output_format_config

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_output_format_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig"]:
        '''s3_output_format_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_output_format_config AppflowFlow#s3_output_format_config}
        '''
        result = self._values.get("s3_output_format_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3OutputReference",
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

    @jsii.member(jsii_name="putS3OutputFormatConfig")
    def put_s3_output_format_config(
        self,
        *,
        aggregation_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig", typing.Dict[str, typing.Any]]] = None,
        file_type: typing.Optional[builtins.str] = None,
        prefix_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aggregation_config: aggregation_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_config AppflowFlow#aggregation_config}
        :param file_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#file_type AppflowFlow#file_type}.
        :param prefix_config: prefix_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_config AppflowFlow#prefix_config}
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig(
            aggregation_config=aggregation_config,
            file_type=file_type,
            prefix_config=prefix_config,
        )

        return typing.cast(None, jsii.invoke(self, "putS3OutputFormatConfig", [value]))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetS3OutputFormatConfig")
    def reset_s3_output_format_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3OutputFormatConfig", []))

    @builtins.property
    @jsii.member(jsii_name="s3OutputFormatConfig")
    def s3_output_format_config(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigOutputReference", jsii.get(self, "s3OutputFormatConfig"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="s3OutputFormatConfigInput")
    def s3_output_format_config_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig"], jsii.get(self, "s3OutputFormatConfigInput"))

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
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig",
    jsii_struct_bases=[],
    name_mapping={
        "aggregation_config": "aggregationConfig",
        "file_type": "fileType",
        "prefix_config": "prefixConfig",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig:
    def __init__(
        self,
        *,
        aggregation_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig", typing.Dict[str, typing.Any]]] = None,
        file_type: typing.Optional[builtins.str] = None,
        prefix_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aggregation_config: aggregation_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_config AppflowFlow#aggregation_config}
        :param file_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#file_type AppflowFlow#file_type}.
        :param prefix_config: prefix_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_config AppflowFlow#prefix_config}
        '''
        if isinstance(aggregation_config, dict):
            aggregation_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig(**aggregation_config)
        if isinstance(prefix_config, dict):
            prefix_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig(**prefix_config)
        if __debug__:
            def stub(
                *,
                aggregation_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig, typing.Dict[str, typing.Any]]] = None,
                file_type: typing.Optional[builtins.str] = None,
                prefix_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument aggregation_config", value=aggregation_config, expected_type=type_hints["aggregation_config"])
            check_type(argname="argument file_type", value=file_type, expected_type=type_hints["file_type"])
            check_type(argname="argument prefix_config", value=prefix_config, expected_type=type_hints["prefix_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aggregation_config is not None:
            self._values["aggregation_config"] = aggregation_config
        if file_type is not None:
            self._values["file_type"] = file_type
        if prefix_config is not None:
            self._values["prefix_config"] = prefix_config

    @builtins.property
    def aggregation_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig"]:
        '''aggregation_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_config AppflowFlow#aggregation_config}
        '''
        result = self._values.get("aggregation_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig"], result)

    @builtins.property
    def file_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#file_type AppflowFlow#file_type}.'''
        result = self._values.get("file_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig"]:
        '''prefix_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_config AppflowFlow#prefix_config}
        '''
        result = self._values.get("prefix_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig",
    jsii_struct_bases=[],
    name_mapping={"aggregation_type": "aggregationType"},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig:
    def __init__(
        self,
        *,
        aggregation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aggregation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_type AppflowFlow#aggregation_type}.
        '''
        if __debug__:
            def stub(*, aggregation_type: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument aggregation_type", value=aggregation_type, expected_type=type_hints["aggregation_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aggregation_type is not None:
            self._values["aggregation_type"] = aggregation_type

    @builtins.property
    def aggregation_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_type AppflowFlow#aggregation_type}.'''
        result = self._values.get("aggregation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfigOutputReference",
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

    @jsii.member(jsii_name="resetAggregationType")
    def reset_aggregation_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregationType", []))

    @builtins.property
    @jsii.member(jsii_name="aggregationTypeInput")
    def aggregation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregationType")
    def aggregation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aggregationType"))

    @aggregation_type.setter
    def aggregation_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigOutputReference",
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

    @jsii.member(jsii_name="putAggregationConfig")
    def put_aggregation_config(
        self,
        *,
        aggregation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aggregation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_type AppflowFlow#aggregation_type}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig(
            aggregation_type=aggregation_type
        )

        return typing.cast(None, jsii.invoke(self, "putAggregationConfig", [value]))

    @jsii.member(jsii_name="putPrefixConfig")
    def put_prefix_config(
        self,
        *,
        prefix_format: typing.Optional[builtins.str] = None,
        prefix_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param prefix_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_format AppflowFlow#prefix_format}.
        :param prefix_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_type AppflowFlow#prefix_type}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig(
            prefix_format=prefix_format, prefix_type=prefix_type
        )

        return typing.cast(None, jsii.invoke(self, "putPrefixConfig", [value]))

    @jsii.member(jsii_name="resetAggregationConfig")
    def reset_aggregation_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregationConfig", []))

    @jsii.member(jsii_name="resetFileType")
    def reset_file_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileType", []))

    @jsii.member(jsii_name="resetPrefixConfig")
    def reset_prefix_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixConfig", []))

    @builtins.property
    @jsii.member(jsii_name="aggregationConfig")
    def aggregation_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfigOutputReference, jsii.get(self, "aggregationConfig"))

    @builtins.property
    @jsii.member(jsii_name="prefixConfig")
    def prefix_config(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfigOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfigOutputReference", jsii.get(self, "prefixConfig"))

    @builtins.property
    @jsii.member(jsii_name="aggregationConfigInput")
    def aggregation_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig], jsii.get(self, "aggregationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="fileTypeInput")
    def file_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixConfigInput")
    def prefix_config_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig"], jsii.get(self, "prefixConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="fileType")
    def file_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileType"))

    @file_type.setter
    def file_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig",
    jsii_struct_bases=[],
    name_mapping={"prefix_format": "prefixFormat", "prefix_type": "prefixType"},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig:
    def __init__(
        self,
        *,
        prefix_format: typing.Optional[builtins.str] = None,
        prefix_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param prefix_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_format AppflowFlow#prefix_format}.
        :param prefix_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_type AppflowFlow#prefix_type}.
        '''
        if __debug__:
            def stub(
                *,
                prefix_format: typing.Optional[builtins.str] = None,
                prefix_type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument prefix_format", value=prefix_format, expected_type=type_hints["prefix_format"])
            check_type(argname="argument prefix_type", value=prefix_type, expected_type=type_hints["prefix_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if prefix_format is not None:
            self._values["prefix_format"] = prefix_format
        if prefix_type is not None:
            self._values["prefix_type"] = prefix_type

    @builtins.property
    def prefix_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_format AppflowFlow#prefix_format}.'''
        result = self._values.get("prefix_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_type AppflowFlow#prefix_type}.'''
        result = self._values.get("prefix_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfigOutputReference",
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

    @jsii.member(jsii_name="resetPrefixFormat")
    def reset_prefix_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixFormat", []))

    @jsii.member(jsii_name="resetPrefixType")
    def reset_prefix_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixType", []))

    @builtins.property
    @jsii.member(jsii_name="prefixFormatInput")
    def prefix_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixTypeInput")
    def prefix_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixFormat")
    def prefix_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixFormat"))

    @prefix_format.setter
    def prefix_format(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixFormat", value)

    @builtins.property
    @jsii.member(jsii_name="prefixType")
    def prefix_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixType"))

    @prefix_type.setter
    def prefix_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce",
    jsii_struct_bases=[],
    name_mapping={
        "object": "object",
        "error_handling_config": "errorHandlingConfig",
        "id_field_names": "idFieldNames",
        "write_operation_type": "writeOperationType",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce:
    def __init__(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig", typing.Dict[str, typing.Any]]] = None,
        id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        write_operation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        :param id_field_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.
        :param write_operation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.
        '''
        if isinstance(error_handling_config, dict):
            error_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig(**error_handling_config)
        if __debug__:
            def stub(
                *,
                object: builtins.str,
                error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig, typing.Dict[str, typing.Any]]] = None,
                id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
                write_operation_type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
            check_type(argname="argument id_field_names", value=id_field_names, expected_type=type_hints["id_field_names"])
            check_type(argname="argument write_operation_type", value=write_operation_type, expected_type=type_hints["write_operation_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }
        if error_handling_config is not None:
            self._values["error_handling_config"] = error_handling_config
        if id_field_names is not None:
            self._values["id_field_names"] = id_field_names
        if write_operation_type is not None:
            self._values["write_operation_type"] = write_operation_type

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig"]:
        '''error_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        result = self._values.get("error_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig"], result)

    @builtins.property
    def id_field_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.'''
        result = self._values.get("id_field_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def write_operation_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.'''
        result = self._values.get("write_operation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "fail_on_first_destination_error": "failOnFirstDestinationError",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        if __debug__:
            def stub(
                *,
                bucket_name: typing.Optional[builtins.str] = None,
                bucket_prefix: typing.Optional[builtins.str] = None,
                fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument fail_on_first_destination_error", value=fail_on_first_destination_error, expected_type=type_hints["fail_on_first_destination_error"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if fail_on_first_destination_error is not None:
            self._values["fail_on_first_destination_error"] = fail_on_first_destination_error

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_on_first_destination_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.'''
        result = self._values.get("fail_on_first_destination_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfigOutputReference",
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

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetFailOnFirstDestinationError")
    def reset_fail_on_first_destination_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailOnFirstDestinationError", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationErrorInput")
    def fail_on_first_destination_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "failOnFirstDestinationErrorInput"))

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
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationError")
    def fail_on_first_destination_error(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "failOnFirstDestinationError"))

    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnFirstDestinationError", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceOutputReference",
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

    @jsii.member(jsii_name="putErrorHandlingConfig")
    def put_error_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            fail_on_first_destination_error=fail_on_first_destination_error,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorHandlingConfig", [value]))

    @jsii.member(jsii_name="resetErrorHandlingConfig")
    def reset_error_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorHandlingConfig", []))

    @jsii.member(jsii_name="resetIdFieldNames")
    def reset_id_field_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdFieldNames", []))

    @jsii.member(jsii_name="resetWriteOperationType")
    def reset_write_operation_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteOperationType", []))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfigOutputReference, jsii.get(self, "errorHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfigInput")
    def error_handling_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig], jsii.get(self, "errorHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idFieldNamesInput")
    def id_field_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "idFieldNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="writeOperationTypeInput")
    def write_operation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "writeOperationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idFieldNames")
    def id_field_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "idFieldNames"))

    @id_field_names.setter
    def id_field_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idFieldNames", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="writeOperationType")
    def write_operation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "writeOperationType"))

    @write_operation_type.setter
    def write_operation_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeOperationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData",
    jsii_struct_bases=[],
    name_mapping={
        "object_path": "objectPath",
        "error_handling_config": "errorHandlingConfig",
        "id_field_names": "idFieldNames",
        "success_response_handling_config": "successResponseHandlingConfig",
        "write_operation_type": "writeOperationType",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData:
    def __init__(
        self,
        *,
        object_path: builtins.str,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig", typing.Dict[str, typing.Any]]] = None,
        id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        success_response_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig", typing.Dict[str, typing.Any]]] = None,
        write_operation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param object_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object_path AppflowFlow#object_path}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        :param id_field_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.
        :param success_response_handling_config: success_response_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#success_response_handling_config AppflowFlow#success_response_handling_config}
        :param write_operation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.
        '''
        if isinstance(error_handling_config, dict):
            error_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig(**error_handling_config)
        if isinstance(success_response_handling_config, dict):
            success_response_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig(**success_response_handling_config)
        if __debug__:
            def stub(
                *,
                object_path: builtins.str,
                error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig, typing.Dict[str, typing.Any]]] = None,
                id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
                success_response_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig, typing.Dict[str, typing.Any]]] = None,
                write_operation_type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object_path", value=object_path, expected_type=type_hints["object_path"])
            check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
            check_type(argname="argument id_field_names", value=id_field_names, expected_type=type_hints["id_field_names"])
            check_type(argname="argument success_response_handling_config", value=success_response_handling_config, expected_type=type_hints["success_response_handling_config"])
            check_type(argname="argument write_operation_type", value=write_operation_type, expected_type=type_hints["write_operation_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_path": object_path,
        }
        if error_handling_config is not None:
            self._values["error_handling_config"] = error_handling_config
        if id_field_names is not None:
            self._values["id_field_names"] = id_field_names
        if success_response_handling_config is not None:
            self._values["success_response_handling_config"] = success_response_handling_config
        if write_operation_type is not None:
            self._values["write_operation_type"] = write_operation_type

    @builtins.property
    def object_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object_path AppflowFlow#object_path}.'''
        result = self._values.get("object_path")
        assert result is not None, "Required property 'object_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig"]:
        '''error_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        result = self._values.get("error_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig"], result)

    @builtins.property
    def id_field_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.'''
        result = self._values.get("id_field_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def success_response_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig"]:
        '''success_response_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#success_response_handling_config AppflowFlow#success_response_handling_config}
        '''
        result = self._values.get("success_response_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig"], result)

    @builtins.property
    def write_operation_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.'''
        result = self._values.get("write_operation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "fail_on_first_destination_error": "failOnFirstDestinationError",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        if __debug__:
            def stub(
                *,
                bucket_name: typing.Optional[builtins.str] = None,
                bucket_prefix: typing.Optional[builtins.str] = None,
                fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument fail_on_first_destination_error", value=fail_on_first_destination_error, expected_type=type_hints["fail_on_first_destination_error"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if fail_on_first_destination_error is not None:
            self._values["fail_on_first_destination_error"] = fail_on_first_destination_error

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_on_first_destination_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.'''
        result = self._values.get("fail_on_first_destination_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfigOutputReference",
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

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetFailOnFirstDestinationError")
    def reset_fail_on_first_destination_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailOnFirstDestinationError", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationErrorInput")
    def fail_on_first_destination_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "failOnFirstDestinationErrorInput"))

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
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationError")
    def fail_on_first_destination_error(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "failOnFirstDestinationError"))

    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnFirstDestinationError", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataOutputReference",
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

    @jsii.member(jsii_name="putErrorHandlingConfig")
    def put_error_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            fail_on_first_destination_error=fail_on_first_destination_error,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorHandlingConfig", [value]))

    @jsii.member(jsii_name="putSuccessResponseHandlingConfig")
    def put_success_response_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig(
            bucket_name=bucket_name, bucket_prefix=bucket_prefix
        )

        return typing.cast(None, jsii.invoke(self, "putSuccessResponseHandlingConfig", [value]))

    @jsii.member(jsii_name="resetErrorHandlingConfig")
    def reset_error_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorHandlingConfig", []))

    @jsii.member(jsii_name="resetIdFieldNames")
    def reset_id_field_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdFieldNames", []))

    @jsii.member(jsii_name="resetSuccessResponseHandlingConfig")
    def reset_success_response_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuccessResponseHandlingConfig", []))

    @jsii.member(jsii_name="resetWriteOperationType")
    def reset_write_operation_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteOperationType", []))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfigOutputReference, jsii.get(self, "errorHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="successResponseHandlingConfig")
    def success_response_handling_config(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfigOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfigOutputReference", jsii.get(self, "successResponseHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfigInput")
    def error_handling_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig], jsii.get(self, "errorHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idFieldNamesInput")
    def id_field_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "idFieldNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="objectPathInput")
    def object_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectPathInput"))

    @builtins.property
    @jsii.member(jsii_name="successResponseHandlingConfigInput")
    def success_response_handling_config_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig"], jsii.get(self, "successResponseHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="writeOperationTypeInput")
    def write_operation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "writeOperationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idFieldNames")
    def id_field_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "idFieldNames"))

    @id_field_names.setter
    def id_field_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idFieldNames", value)

    @builtins.property
    @jsii.member(jsii_name="objectPath")
    def object_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectPath"))

    @object_path.setter
    def object_path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectPath", value)

    @builtins.property
    @jsii.member(jsii_name="writeOperationType")
    def write_operation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "writeOperationType"))

    @write_operation_type.setter
    def write_operation_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeOperationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={"bucket_name": "bucketName", "bucket_prefix": "bucketPrefix"},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        '''
        if __debug__:
            def stub(
                *,
                bucket_name: typing.Optional[builtins.str] = None,
                bucket_prefix: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfigOutputReference",
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

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

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
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake",
    jsii_struct_bases=[],
    name_mapping={
        "intermediate_bucket_name": "intermediateBucketName",
        "object": "object",
        "bucket_prefix": "bucketPrefix",
        "error_handling_config": "errorHandlingConfig",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake:
    def __init__(
        self,
        *,
        intermediate_bucket_name: builtins.str,
        object: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param intermediate_bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#intermediate_bucket_name AppflowFlow#intermediate_bucket_name}.
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        if isinstance(error_handling_config, dict):
            error_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig(**error_handling_config)
        if __debug__:
            def stub(
                *,
                intermediate_bucket_name: builtins.str,
                object: builtins.str,
                bucket_prefix: typing.Optional[builtins.str] = None,
                error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument intermediate_bucket_name", value=intermediate_bucket_name, expected_type=type_hints["intermediate_bucket_name"])
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "intermediate_bucket_name": intermediate_bucket_name,
            "object": object,
        }
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if error_handling_config is not None:
            self._values["error_handling_config"] = error_handling_config

    @builtins.property
    def intermediate_bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#intermediate_bucket_name AppflowFlow#intermediate_bucket_name}.'''
        result = self._values.get("intermediate_bucket_name")
        assert result is not None, "Required property 'intermediate_bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig"]:
        '''error_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        result = self._values.get("error_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "fail_on_first_destination_error": "failOnFirstDestinationError",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        if __debug__:
            def stub(
                *,
                bucket_name: typing.Optional[builtins.str] = None,
                bucket_prefix: typing.Optional[builtins.str] = None,
                fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument fail_on_first_destination_error", value=fail_on_first_destination_error, expected_type=type_hints["fail_on_first_destination_error"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if fail_on_first_destination_error is not None:
            self._values["fail_on_first_destination_error"] = fail_on_first_destination_error

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_on_first_destination_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.'''
        result = self._values.get("fail_on_first_destination_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfigOutputReference",
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

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetFailOnFirstDestinationError")
    def reset_fail_on_first_destination_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailOnFirstDestinationError", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationErrorInput")
    def fail_on_first_destination_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "failOnFirstDestinationErrorInput"))

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
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationError")
    def fail_on_first_destination_error(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "failOnFirstDestinationError"))

    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnFirstDestinationError", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeOutputReference",
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

    @jsii.member(jsii_name="putErrorHandlingConfig")
    def put_error_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            fail_on_first_destination_error=fail_on_first_destination_error,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorHandlingConfig", [value]))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetErrorHandlingConfig")
    def reset_error_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorHandlingConfig", []))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfigOutputReference, jsii.get(self, "errorHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfigInput")
    def error_handling_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig], jsii.get(self, "errorHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="intermediateBucketNameInput")
    def intermediate_bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intermediateBucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="intermediateBucketName")
    def intermediate_bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intermediateBucketName"))

    @intermediate_bucket_name.setter
    def intermediate_bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intermediateBucketName", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "s3_output_format_config": "s3OutputFormatConfig",
        "bucket_prefix": "bucketPrefix",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        s3_output_format_config: typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig", typing.Dict[str, typing.Any]],
        bucket_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param s3_output_format_config: s3_output_format_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_output_format_config AppflowFlow#s3_output_format_config}
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        '''
        if isinstance(s3_output_format_config, dict):
            s3_output_format_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig(**s3_output_format_config)
        if __debug__:
            def stub(
                *,
                bucket_name: builtins.str,
                s3_output_format_config: typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig, typing.Dict[str, typing.Any]],
                bucket_prefix: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument s3_output_format_config", value=s3_output_format_config, expected_type=type_hints["s3_output_format_config"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
            "s3_output_format_config": s3_output_format_config,
        }
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_output_format_config(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig":
        '''s3_output_format_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_output_format_config AppflowFlow#s3_output_format_config}
        '''
        result = self._values.get("s3_output_format_config")
        assert result is not None, "Required property 's3_output_format_config' is missing"
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig", result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverOutputReference",
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

    @jsii.member(jsii_name="putS3OutputFormatConfig")
    def put_s3_output_format_config(
        self,
        *,
        prefix_config: typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig", typing.Dict[str, typing.Any]],
        aggregation_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig", typing.Dict[str, typing.Any]]] = None,
        file_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param prefix_config: prefix_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_config AppflowFlow#prefix_config}
        :param aggregation_config: aggregation_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_config AppflowFlow#aggregation_config}
        :param file_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#file_type AppflowFlow#file_type}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig(
            prefix_config=prefix_config,
            aggregation_config=aggregation_config,
            file_type=file_type,
        )

        return typing.cast(None, jsii.invoke(self, "putS3OutputFormatConfig", [value]))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="s3OutputFormatConfig")
    def s3_output_format_config(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigOutputReference", jsii.get(self, "s3OutputFormatConfig"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="s3OutputFormatConfigInput")
    def s3_output_format_config_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig"], jsii.get(self, "s3OutputFormatConfigInput"))

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
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig",
    jsii_struct_bases=[],
    name_mapping={
        "prefix_config": "prefixConfig",
        "aggregation_config": "aggregationConfig",
        "file_type": "fileType",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig:
    def __init__(
        self,
        *,
        prefix_config: typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig", typing.Dict[str, typing.Any]],
        aggregation_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig", typing.Dict[str, typing.Any]]] = None,
        file_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param prefix_config: prefix_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_config AppflowFlow#prefix_config}
        :param aggregation_config: aggregation_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_config AppflowFlow#aggregation_config}
        :param file_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#file_type AppflowFlow#file_type}.
        '''
        if isinstance(prefix_config, dict):
            prefix_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig(**prefix_config)
        if isinstance(aggregation_config, dict):
            aggregation_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig(**aggregation_config)
        if __debug__:
            def stub(
                *,
                prefix_config: typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig, typing.Dict[str, typing.Any]],
                aggregation_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig, typing.Dict[str, typing.Any]]] = None,
                file_type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument prefix_config", value=prefix_config, expected_type=type_hints["prefix_config"])
            check_type(argname="argument aggregation_config", value=aggregation_config, expected_type=type_hints["aggregation_config"])
            check_type(argname="argument file_type", value=file_type, expected_type=type_hints["file_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "prefix_config": prefix_config,
        }
        if aggregation_config is not None:
            self._values["aggregation_config"] = aggregation_config
        if file_type is not None:
            self._values["file_type"] = file_type

    @builtins.property
    def prefix_config(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig":
        '''prefix_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_config AppflowFlow#prefix_config}
        '''
        result = self._values.get("prefix_config")
        assert result is not None, "Required property 'prefix_config' is missing"
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig", result)

    @builtins.property
    def aggregation_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig"]:
        '''aggregation_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_config AppflowFlow#aggregation_config}
        '''
        result = self._values.get("aggregation_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig"], result)

    @builtins.property
    def file_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#file_type AppflowFlow#file_type}.'''
        result = self._values.get("file_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig",
    jsii_struct_bases=[],
    name_mapping={"aggregation_type": "aggregationType"},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig:
    def __init__(
        self,
        *,
        aggregation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aggregation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_type AppflowFlow#aggregation_type}.
        '''
        if __debug__:
            def stub(*, aggregation_type: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument aggregation_type", value=aggregation_type, expected_type=type_hints["aggregation_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aggregation_type is not None:
            self._values["aggregation_type"] = aggregation_type

    @builtins.property
    def aggregation_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_type AppflowFlow#aggregation_type}.'''
        result = self._values.get("aggregation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfigOutputReference",
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

    @jsii.member(jsii_name="resetAggregationType")
    def reset_aggregation_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregationType", []))

    @builtins.property
    @jsii.member(jsii_name="aggregationTypeInput")
    def aggregation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregationType")
    def aggregation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aggregationType"))

    @aggregation_type.setter
    def aggregation_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigOutputReference",
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

    @jsii.member(jsii_name="putAggregationConfig")
    def put_aggregation_config(
        self,
        *,
        aggregation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aggregation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#aggregation_type AppflowFlow#aggregation_type}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig(
            aggregation_type=aggregation_type
        )

        return typing.cast(None, jsii.invoke(self, "putAggregationConfig", [value]))

    @jsii.member(jsii_name="putPrefixConfig")
    def put_prefix_config(
        self,
        *,
        prefix_type: builtins.str,
        prefix_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param prefix_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_type AppflowFlow#prefix_type}.
        :param prefix_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_format AppflowFlow#prefix_format}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig(
            prefix_type=prefix_type, prefix_format=prefix_format
        )

        return typing.cast(None, jsii.invoke(self, "putPrefixConfig", [value]))

    @jsii.member(jsii_name="resetAggregationConfig")
    def reset_aggregation_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregationConfig", []))

    @jsii.member(jsii_name="resetFileType")
    def reset_file_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileType", []))

    @builtins.property
    @jsii.member(jsii_name="aggregationConfig")
    def aggregation_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfigOutputReference, jsii.get(self, "aggregationConfig"))

    @builtins.property
    @jsii.member(jsii_name="prefixConfig")
    def prefix_config(
        self,
    ) -> "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfigOutputReference":
        return typing.cast("AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfigOutputReference", jsii.get(self, "prefixConfig"))

    @builtins.property
    @jsii.member(jsii_name="aggregationConfigInput")
    def aggregation_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig], jsii.get(self, "aggregationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="fileTypeInput")
    def file_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixConfigInput")
    def prefix_config_input(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig"]:
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig"], jsii.get(self, "prefixConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="fileType")
    def file_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileType"))

    @file_type.setter
    def file_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig",
    jsii_struct_bases=[],
    name_mapping={"prefix_type": "prefixType", "prefix_format": "prefixFormat"},
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig:
    def __init__(
        self,
        *,
        prefix_type: builtins.str,
        prefix_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param prefix_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_type AppflowFlow#prefix_type}.
        :param prefix_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_format AppflowFlow#prefix_format}.
        '''
        if __debug__:
            def stub(
                *,
                prefix_type: builtins.str,
                prefix_format: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument prefix_type", value=prefix_type, expected_type=type_hints["prefix_type"])
            check_type(argname="argument prefix_format", value=prefix_format, expected_type=type_hints["prefix_format"])
        self._values: typing.Dict[str, typing.Any] = {
            "prefix_type": prefix_type,
        }
        if prefix_format is not None:
            self._values["prefix_format"] = prefix_format

    @builtins.property
    def prefix_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_type AppflowFlow#prefix_type}.'''
        result = self._values.get("prefix_type")
        assert result is not None, "Required property 'prefix_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def prefix_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#prefix_format AppflowFlow#prefix_format}.'''
        result = self._values.get("prefix_format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfigOutputReference",
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

    @jsii.member(jsii_name="resetPrefixFormat")
    def reset_prefix_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixFormat", []))

    @builtins.property
    @jsii.member(jsii_name="prefixFormatInput")
    def prefix_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixTypeInput")
    def prefix_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixFormat")
    def prefix_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixFormat"))

    @prefix_format.setter
    def prefix_format(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixFormat", value)

    @builtins.property
    @jsii.member(jsii_name="prefixType")
    def prefix_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefixType"))

    @prefix_type.setter
    def prefix_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefixType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk",
    jsii_struct_bases=[],
    name_mapping={
        "object": "object",
        "error_handling_config": "errorHandlingConfig",
        "id_field_names": "idFieldNames",
        "write_operation_type": "writeOperationType",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk:
    def __init__(
        self,
        *,
        object: builtins.str,
        error_handling_config: typing.Optional[typing.Union["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig", typing.Dict[str, typing.Any]]] = None,
        id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        write_operation_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param error_handling_config: error_handling_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        :param id_field_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.
        :param write_operation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.
        '''
        if isinstance(error_handling_config, dict):
            error_handling_config = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig(**error_handling_config)
        if __debug__:
            def stub(
                *,
                object: builtins.str,
                error_handling_config: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig, typing.Dict[str, typing.Any]]] = None,
                id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
                write_operation_type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
            check_type(argname="argument id_field_names", value=id_field_names, expected_type=type_hints["id_field_names"])
            check_type(argname="argument write_operation_type", value=write_operation_type, expected_type=type_hints["write_operation_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }
        if error_handling_config is not None:
            self._values["error_handling_config"] = error_handling_config
        if id_field_names is not None:
            self._values["id_field_names"] = id_field_names
        if write_operation_type is not None:
            self._values["write_operation_type"] = write_operation_type

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def error_handling_config(
        self,
    ) -> typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig"]:
        '''error_handling_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#error_handling_config AppflowFlow#error_handling_config}
        '''
        result = self._values.get("error_handling_config")
        return typing.cast(typing.Optional["AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig"], result)

    @builtins.property
    def id_field_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#id_field_names AppflowFlow#id_field_names}.'''
        result = self._values.get("id_field_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def write_operation_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#write_operation_type AppflowFlow#write_operation_type}.'''
        result = self._values.get("write_operation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "fail_on_first_destination_error": "failOnFirstDestinationError",
    },
)
class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        if __debug__:
            def stub(
                *,
                bucket_name: typing.Optional[builtins.str] = None,
                bucket_prefix: typing.Optional[builtins.str] = None,
                fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument fail_on_first_destination_error", value=fail_on_first_destination_error, expected_type=type_hints["fail_on_first_destination_error"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if fail_on_first_destination_error is not None:
            self._values["fail_on_first_destination_error"] = fail_on_first_destination_error

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_on_first_destination_error(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.'''
        result = self._values.get("fail_on_first_destination_error")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfigOutputReference",
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

    @jsii.member(jsii_name="resetBucketName")
    def reset_bucket_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketName", []))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetFailOnFirstDestinationError")
    def reset_fail_on_first_destination_error(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailOnFirstDestinationError", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationErrorInput")
    def fail_on_first_destination_error_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "failOnFirstDestinationErrorInput"))

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
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="failOnFirstDestinationError")
    def fail_on_first_destination_error(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "failOnFirstDestinationError"))

    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnFirstDestinationError", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskOutputReference",
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

    @jsii.member(jsii_name="putErrorHandlingConfig")
    def put_error_handling_config(
        self,
        *,
        bucket_name: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        fail_on_first_destination_error: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param fail_on_first_destination_error: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#fail_on_first_destination_error AppflowFlow#fail_on_first_destination_error}.
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            fail_on_first_destination_error=fail_on_first_destination_error,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorHandlingConfig", [value]))

    @jsii.member(jsii_name="resetErrorHandlingConfig")
    def reset_error_handling_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorHandlingConfig", []))

    @jsii.member(jsii_name="resetIdFieldNames")
    def reset_id_field_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdFieldNames", []))

    @jsii.member(jsii_name="resetWriteOperationType")
    def reset_write_operation_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteOperationType", []))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfigOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfigOutputReference, jsii.get(self, "errorHandlingConfig"))

    @builtins.property
    @jsii.member(jsii_name="errorHandlingConfigInput")
    def error_handling_config_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig], jsii.get(self, "errorHandlingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idFieldNamesInput")
    def id_field_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "idFieldNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="writeOperationTypeInput")
    def write_operation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "writeOperationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idFieldNames")
    def id_field_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "idFieldNames"))

    @id_field_names.setter
    def id_field_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idFieldNames", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="writeOperationType")
    def write_operation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "writeOperationType"))

    @write_operation_type.setter
    def write_operation_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeOperationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigList",
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
    ) -> "AppflowFlowDestinationFlowConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppflowFlowDestinationFlowConfigOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppflowFlowDestinationFlowConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppflowFlowDestinationFlowConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppflowFlowDestinationFlowConfig]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppflowFlowDestinationFlowConfig]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowDestinationFlowConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowDestinationFlowConfigOutputReference",
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

    @jsii.member(jsii_name="putDestinationConnectorProperties")
    def put_destination_connector_properties(
        self,
        *,
        custom_connector: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector, typing.Dict[str, typing.Any]]] = None,
        customer_profiles: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles, typing.Dict[str, typing.Any]]] = None,
        event_bridge: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge, typing.Dict[str, typing.Any]]] = None,
        honeycode: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode, typing.Dict[str, typing.Any]]] = None,
        lookout_metrics: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics, typing.Dict[str, typing.Any]]] = None,
        marketo: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo, typing.Dict[str, typing.Any]]] = None,
        redshift: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift, typing.Dict[str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3, typing.Dict[str, typing.Any]]] = None,
        salesforce: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce, typing.Dict[str, typing.Any]]] = None,
        sapo_data: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData, typing.Dict[str, typing.Any]]] = None,
        snowflake: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake, typing.Dict[str, typing.Any]]] = None,
        upsolver: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver, typing.Dict[str, typing.Any]]] = None,
        zendesk: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param custom_connector: custom_connector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_connector AppflowFlow#custom_connector}
        :param customer_profiles: customer_profiles block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#customer_profiles AppflowFlow#customer_profiles}
        :param event_bridge: event_bridge block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#event_bridge AppflowFlow#event_bridge}
        :param honeycode: honeycode block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#honeycode AppflowFlow#honeycode}
        :param lookout_metrics: lookout_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#lookout_metrics AppflowFlow#lookout_metrics}
        :param marketo: marketo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#marketo AppflowFlow#marketo}
        :param redshift: redshift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#redshift AppflowFlow#redshift}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3 AppflowFlow#s3}
        :param salesforce: salesforce block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#salesforce AppflowFlow#salesforce}
        :param sapo_data: sapo_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#sapo_data AppflowFlow#sapo_data}
        :param snowflake: snowflake block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#snowflake AppflowFlow#snowflake}
        :param upsolver: upsolver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#upsolver AppflowFlow#upsolver}
        :param zendesk: zendesk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#zendesk AppflowFlow#zendesk}
        '''
        value = AppflowFlowDestinationFlowConfigDestinationConnectorProperties(
            custom_connector=custom_connector,
            customer_profiles=customer_profiles,
            event_bridge=event_bridge,
            honeycode=honeycode,
            lookout_metrics=lookout_metrics,
            marketo=marketo,
            redshift=redshift,
            s3=s3,
            salesforce=salesforce,
            sapo_data=sapo_data,
            snowflake=snowflake,
            upsolver=upsolver,
            zendesk=zendesk,
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationConnectorProperties", [value]))

    @jsii.member(jsii_name="resetApiVersion")
    def reset_api_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiVersion", []))

    @jsii.member(jsii_name="resetConnectorProfileName")
    def reset_connector_profile_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectorProfileName", []))

    @builtins.property
    @jsii.member(jsii_name="destinationConnectorProperties")
    def destination_connector_properties(
        self,
    ) -> AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesOutputReference:
        return typing.cast(AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesOutputReference, jsii.get(self, "destinationConnectorProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiVersionInput")
    def api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorProfileNameInput")
    def connector_profile_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorProfileNameInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorTypeInput")
    def connector_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationConnectorPropertiesInput")
    def destination_connector_properties_input(
        self,
    ) -> typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorProperties]:
        return typing.cast(typing.Optional[AppflowFlowDestinationFlowConfigDestinationConnectorProperties], jsii.get(self, "destinationConnectorPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @api_version.setter
    def api_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="connectorProfileName")
    def connector_profile_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectorProfileName"))

    @connector_profile_name.setter
    def connector_profile_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorProfileName", value)

    @builtins.property
    @jsii.member(jsii_name="connectorType")
    def connector_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectorType"))

    @connector_type.setter
    def connector_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppflowFlowDestinationFlowConfig, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppflowFlowDestinationFlowConfig, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfig, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[AppflowFlowDestinationFlowConfig, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfig",
    jsii_struct_bases=[],
    name_mapping={
        "connector_type": "connectorType",
        "source_connector_properties": "sourceConnectorProperties",
        "api_version": "apiVersion",
        "connector_profile_name": "connectorProfileName",
        "incremental_pull_config": "incrementalPullConfig",
    },
)
class AppflowFlowSourceFlowConfig:
    def __init__(
        self,
        *,
        connector_type: builtins.str,
        source_connector_properties: typing.Union["AppflowFlowSourceFlowConfigSourceConnectorProperties", typing.Dict[str, typing.Any]],
        api_version: typing.Optional[builtins.str] = None,
        connector_profile_name: typing.Optional[builtins.str] = None,
        incremental_pull_config: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigIncrementalPullConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connector_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_type AppflowFlow#connector_type}.
        :param source_connector_properties: source_connector_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#source_connector_properties AppflowFlow#source_connector_properties}
        :param api_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#api_version AppflowFlow#api_version}.
        :param connector_profile_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_profile_name AppflowFlow#connector_profile_name}.
        :param incremental_pull_config: incremental_pull_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#incremental_pull_config AppflowFlow#incremental_pull_config}
        '''
        if isinstance(source_connector_properties, dict):
            source_connector_properties = AppflowFlowSourceFlowConfigSourceConnectorProperties(**source_connector_properties)
        if isinstance(incremental_pull_config, dict):
            incremental_pull_config = AppflowFlowSourceFlowConfigIncrementalPullConfig(**incremental_pull_config)
        if __debug__:
            def stub(
                *,
                connector_type: builtins.str,
                source_connector_properties: typing.Union[AppflowFlowSourceFlowConfigSourceConnectorProperties, typing.Dict[str, typing.Any]],
                api_version: typing.Optional[builtins.str] = None,
                connector_profile_name: typing.Optional[builtins.str] = None,
                incremental_pull_config: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigIncrementalPullConfig, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument connector_type", value=connector_type, expected_type=type_hints["connector_type"])
            check_type(argname="argument source_connector_properties", value=source_connector_properties, expected_type=type_hints["source_connector_properties"])
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument connector_profile_name", value=connector_profile_name, expected_type=type_hints["connector_profile_name"])
            check_type(argname="argument incremental_pull_config", value=incremental_pull_config, expected_type=type_hints["incremental_pull_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "connector_type": connector_type,
            "source_connector_properties": source_connector_properties,
        }
        if api_version is not None:
            self._values["api_version"] = api_version
        if connector_profile_name is not None:
            self._values["connector_profile_name"] = connector_profile_name
        if incremental_pull_config is not None:
            self._values["incremental_pull_config"] = incremental_pull_config

    @builtins.property
    def connector_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_type AppflowFlow#connector_type}.'''
        result = self._values.get("connector_type")
        assert result is not None, "Required property 'connector_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_connector_properties(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorProperties":
        '''source_connector_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#source_connector_properties AppflowFlow#source_connector_properties}
        '''
        result = self._values.get("source_connector_properties")
        assert result is not None, "Required property 'source_connector_properties' is missing"
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorProperties", result)

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#api_version AppflowFlow#api_version}.'''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connector_profile_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_profile_name AppflowFlow#connector_profile_name}.'''
        result = self._values.get("connector_profile_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def incremental_pull_config(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigIncrementalPullConfig"]:
        '''incremental_pull_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#incremental_pull_config AppflowFlow#incremental_pull_config}
        '''
        result = self._values.get("incremental_pull_config")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigIncrementalPullConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigIncrementalPullConfig",
    jsii_struct_bases=[],
    name_mapping={"datetime_type_field_name": "datetimeTypeFieldName"},
)
class AppflowFlowSourceFlowConfigIncrementalPullConfig:
    def __init__(
        self,
        *,
        datetime_type_field_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param datetime_type_field_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#datetime_type_field_name AppflowFlow#datetime_type_field_name}.
        '''
        if __debug__:
            def stub(
                *,
                datetime_type_field_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument datetime_type_field_name", value=datetime_type_field_name, expected_type=type_hints["datetime_type_field_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if datetime_type_field_name is not None:
            self._values["datetime_type_field_name"] = datetime_type_field_name

    @builtins.property
    def datetime_type_field_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#datetime_type_field_name AppflowFlow#datetime_type_field_name}.'''
        result = self._values.get("datetime_type_field_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigIncrementalPullConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigIncrementalPullConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigIncrementalPullConfigOutputReference",
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

    @jsii.member(jsii_name="resetDatetimeTypeFieldName")
    def reset_datetime_type_field_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatetimeTypeFieldName", []))

    @builtins.property
    @jsii.member(jsii_name="datetimeTypeFieldNameInput")
    def datetime_type_field_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datetimeTypeFieldNameInput"))

    @builtins.property
    @jsii.member(jsii_name="datetimeTypeFieldName")
    def datetime_type_field_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datetimeTypeFieldName"))

    @datetime_type_field_name.setter
    def datetime_type_field_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datetimeTypeFieldName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigIncrementalPullConfig]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigIncrementalPullConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigIncrementalPullConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigIncrementalPullConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowSourceFlowConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigOutputReference",
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

    @jsii.member(jsii_name="putIncrementalPullConfig")
    def put_incremental_pull_config(
        self,
        *,
        datetime_type_field_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param datetime_type_field_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#datetime_type_field_name AppflowFlow#datetime_type_field_name}.
        '''
        value = AppflowFlowSourceFlowConfigIncrementalPullConfig(
            datetime_type_field_name=datetime_type_field_name
        )

        return typing.cast(None, jsii.invoke(self, "putIncrementalPullConfig", [value]))

    @jsii.member(jsii_name="putSourceConnectorProperties")
    def put_source_connector_properties(
        self,
        *,
        amplitude: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude", typing.Dict[str, typing.Any]]] = None,
        custom_connector: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector", typing.Dict[str, typing.Any]]] = None,
        datadog: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog", typing.Dict[str, typing.Any]]] = None,
        dynatrace: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace", typing.Dict[str, typing.Any]]] = None,
        google_analytics: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics", typing.Dict[str, typing.Any]]] = None,
        infor_nexus: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus", typing.Dict[str, typing.Any]]] = None,
        marketo: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo", typing.Dict[str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3", typing.Dict[str, typing.Any]]] = None,
        salesforce: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce", typing.Dict[str, typing.Any]]] = None,
        sapo_data: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData", typing.Dict[str, typing.Any]]] = None,
        service_now: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow", typing.Dict[str, typing.Any]]] = None,
        singular: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular", typing.Dict[str, typing.Any]]] = None,
        slack: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack", typing.Dict[str, typing.Any]]] = None,
        trendmicro: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro", typing.Dict[str, typing.Any]]] = None,
        veeva: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva", typing.Dict[str, typing.Any]]] = None,
        zendesk: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param amplitude: amplitude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#amplitude AppflowFlow#amplitude}
        :param custom_connector: custom_connector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_connector AppflowFlow#custom_connector}
        :param datadog: datadog block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#datadog AppflowFlow#datadog}
        :param dynatrace: dynatrace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#dynatrace AppflowFlow#dynatrace}
        :param google_analytics: google_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#google_analytics AppflowFlow#google_analytics}
        :param infor_nexus: infor_nexus block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#infor_nexus AppflowFlow#infor_nexus}
        :param marketo: marketo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#marketo AppflowFlow#marketo}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3 AppflowFlow#s3}
        :param salesforce: salesforce block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#salesforce AppflowFlow#salesforce}
        :param sapo_data: sapo_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#sapo_data AppflowFlow#sapo_data}
        :param service_now: service_now block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#service_now AppflowFlow#service_now}
        :param singular: singular block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#singular AppflowFlow#singular}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#slack AppflowFlow#slack}
        :param trendmicro: trendmicro block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trendmicro AppflowFlow#trendmicro}
        :param veeva: veeva block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#veeva AppflowFlow#veeva}
        :param zendesk: zendesk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#zendesk AppflowFlow#zendesk}
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorProperties(
            amplitude=amplitude,
            custom_connector=custom_connector,
            datadog=datadog,
            dynatrace=dynatrace,
            google_analytics=google_analytics,
            infor_nexus=infor_nexus,
            marketo=marketo,
            s3=s3,
            salesforce=salesforce,
            sapo_data=sapo_data,
            service_now=service_now,
            singular=singular,
            slack=slack,
            trendmicro=trendmicro,
            veeva=veeva,
            zendesk=zendesk,
        )

        return typing.cast(None, jsii.invoke(self, "putSourceConnectorProperties", [value]))

    @jsii.member(jsii_name="resetApiVersion")
    def reset_api_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiVersion", []))

    @jsii.member(jsii_name="resetConnectorProfileName")
    def reset_connector_profile_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectorProfileName", []))

    @jsii.member(jsii_name="resetIncrementalPullConfig")
    def reset_incremental_pull_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncrementalPullConfig", []))

    @builtins.property
    @jsii.member(jsii_name="incrementalPullConfig")
    def incremental_pull_config(
        self,
    ) -> AppflowFlowSourceFlowConfigIncrementalPullConfigOutputReference:
        return typing.cast(AppflowFlowSourceFlowConfigIncrementalPullConfigOutputReference, jsii.get(self, "incrementalPullConfig"))

    @builtins.property
    @jsii.member(jsii_name="sourceConnectorProperties")
    def source_connector_properties(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesOutputReference", jsii.get(self, "sourceConnectorProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiVersionInput")
    def api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorProfileNameInput")
    def connector_profile_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorProfileNameInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorTypeInput")
    def connector_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="incrementalPullConfigInput")
    def incremental_pull_config_input(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigIncrementalPullConfig]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigIncrementalPullConfig], jsii.get(self, "incrementalPullConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceConnectorPropertiesInput")
    def source_connector_properties_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorProperties"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorProperties"], jsii.get(self, "sourceConnectorPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @api_version.setter
    def api_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="connectorProfileName")
    def connector_profile_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectorProfileName"))

    @connector_profile_name.setter
    def connector_profile_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorProfileName", value)

    @builtins.property
    @jsii.member(jsii_name="connectorType")
    def connector_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectorType"))

    @connector_type.setter
    def connector_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppflowFlowSourceFlowConfig]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfig],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[AppflowFlowSourceFlowConfig]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorProperties",
    jsii_struct_bases=[],
    name_mapping={
        "amplitude": "amplitude",
        "custom_connector": "customConnector",
        "datadog": "datadog",
        "dynatrace": "dynatrace",
        "google_analytics": "googleAnalytics",
        "infor_nexus": "inforNexus",
        "marketo": "marketo",
        "s3": "s3",
        "salesforce": "salesforce",
        "sapo_data": "sapoData",
        "service_now": "serviceNow",
        "singular": "singular",
        "slack": "slack",
        "trendmicro": "trendmicro",
        "veeva": "veeva",
        "zendesk": "zendesk",
    },
)
class AppflowFlowSourceFlowConfigSourceConnectorProperties:
    def __init__(
        self,
        *,
        amplitude: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude", typing.Dict[str, typing.Any]]] = None,
        custom_connector: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector", typing.Dict[str, typing.Any]]] = None,
        datadog: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog", typing.Dict[str, typing.Any]]] = None,
        dynatrace: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace", typing.Dict[str, typing.Any]]] = None,
        google_analytics: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics", typing.Dict[str, typing.Any]]] = None,
        infor_nexus: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus", typing.Dict[str, typing.Any]]] = None,
        marketo: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo", typing.Dict[str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3", typing.Dict[str, typing.Any]]] = None,
        salesforce: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce", typing.Dict[str, typing.Any]]] = None,
        sapo_data: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData", typing.Dict[str, typing.Any]]] = None,
        service_now: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow", typing.Dict[str, typing.Any]]] = None,
        singular: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular", typing.Dict[str, typing.Any]]] = None,
        slack: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack", typing.Dict[str, typing.Any]]] = None,
        trendmicro: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro", typing.Dict[str, typing.Any]]] = None,
        veeva: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva", typing.Dict[str, typing.Any]]] = None,
        zendesk: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param amplitude: amplitude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#amplitude AppflowFlow#amplitude}
        :param custom_connector: custom_connector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_connector AppflowFlow#custom_connector}
        :param datadog: datadog block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#datadog AppflowFlow#datadog}
        :param dynatrace: dynatrace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#dynatrace AppflowFlow#dynatrace}
        :param google_analytics: google_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#google_analytics AppflowFlow#google_analytics}
        :param infor_nexus: infor_nexus block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#infor_nexus AppflowFlow#infor_nexus}
        :param marketo: marketo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#marketo AppflowFlow#marketo}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3 AppflowFlow#s3}
        :param salesforce: salesforce block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#salesforce AppflowFlow#salesforce}
        :param sapo_data: sapo_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#sapo_data AppflowFlow#sapo_data}
        :param service_now: service_now block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#service_now AppflowFlow#service_now}
        :param singular: singular block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#singular AppflowFlow#singular}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#slack AppflowFlow#slack}
        :param trendmicro: trendmicro block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trendmicro AppflowFlow#trendmicro}
        :param veeva: veeva block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#veeva AppflowFlow#veeva}
        :param zendesk: zendesk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#zendesk AppflowFlow#zendesk}
        '''
        if isinstance(amplitude, dict):
            amplitude = AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude(**amplitude)
        if isinstance(custom_connector, dict):
            custom_connector = AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector(**custom_connector)
        if isinstance(datadog, dict):
            datadog = AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog(**datadog)
        if isinstance(dynatrace, dict):
            dynatrace = AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace(**dynatrace)
        if isinstance(google_analytics, dict):
            google_analytics = AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics(**google_analytics)
        if isinstance(infor_nexus, dict):
            infor_nexus = AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus(**infor_nexus)
        if isinstance(marketo, dict):
            marketo = AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo(**marketo)
        if isinstance(s3, dict):
            s3 = AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3(**s3)
        if isinstance(salesforce, dict):
            salesforce = AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce(**salesforce)
        if isinstance(sapo_data, dict):
            sapo_data = AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData(**sapo_data)
        if isinstance(service_now, dict):
            service_now = AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow(**service_now)
        if isinstance(singular, dict):
            singular = AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular(**singular)
        if isinstance(slack, dict):
            slack = AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack(**slack)
        if isinstance(trendmicro, dict):
            trendmicro = AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro(**trendmicro)
        if isinstance(veeva, dict):
            veeva = AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva(**veeva)
        if isinstance(zendesk, dict):
            zendesk = AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk(**zendesk)
        if __debug__:
            def stub(
                *,
                amplitude: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude, typing.Dict[str, typing.Any]]] = None,
                custom_connector: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector, typing.Dict[str, typing.Any]]] = None,
                datadog: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog, typing.Dict[str, typing.Any]]] = None,
                dynatrace: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace, typing.Dict[str, typing.Any]]] = None,
                google_analytics: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics, typing.Dict[str, typing.Any]]] = None,
                infor_nexus: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus, typing.Dict[str, typing.Any]]] = None,
                marketo: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo, typing.Dict[str, typing.Any]]] = None,
                s3: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3, typing.Dict[str, typing.Any]]] = None,
                salesforce: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce, typing.Dict[str, typing.Any]]] = None,
                sapo_data: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData, typing.Dict[str, typing.Any]]] = None,
                service_now: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow, typing.Dict[str, typing.Any]]] = None,
                singular: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular, typing.Dict[str, typing.Any]]] = None,
                slack: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack, typing.Dict[str, typing.Any]]] = None,
                trendmicro: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro, typing.Dict[str, typing.Any]]] = None,
                veeva: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva, typing.Dict[str, typing.Any]]] = None,
                zendesk: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument amplitude", value=amplitude, expected_type=type_hints["amplitude"])
            check_type(argname="argument custom_connector", value=custom_connector, expected_type=type_hints["custom_connector"])
            check_type(argname="argument datadog", value=datadog, expected_type=type_hints["datadog"])
            check_type(argname="argument dynatrace", value=dynatrace, expected_type=type_hints["dynatrace"])
            check_type(argname="argument google_analytics", value=google_analytics, expected_type=type_hints["google_analytics"])
            check_type(argname="argument infor_nexus", value=infor_nexus, expected_type=type_hints["infor_nexus"])
            check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
            check_type(argname="argument sapo_data", value=sapo_data, expected_type=type_hints["sapo_data"])
            check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
            check_type(argname="argument singular", value=singular, expected_type=type_hints["singular"])
            check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
            check_type(argname="argument trendmicro", value=trendmicro, expected_type=type_hints["trendmicro"])
            check_type(argname="argument veeva", value=veeva, expected_type=type_hints["veeva"])
            check_type(argname="argument zendesk", value=zendesk, expected_type=type_hints["zendesk"])
        self._values: typing.Dict[str, typing.Any] = {}
        if amplitude is not None:
            self._values["amplitude"] = amplitude
        if custom_connector is not None:
            self._values["custom_connector"] = custom_connector
        if datadog is not None:
            self._values["datadog"] = datadog
        if dynatrace is not None:
            self._values["dynatrace"] = dynatrace
        if google_analytics is not None:
            self._values["google_analytics"] = google_analytics
        if infor_nexus is not None:
            self._values["infor_nexus"] = infor_nexus
        if marketo is not None:
            self._values["marketo"] = marketo
        if s3 is not None:
            self._values["s3"] = s3
        if salesforce is not None:
            self._values["salesforce"] = salesforce
        if sapo_data is not None:
            self._values["sapo_data"] = sapo_data
        if service_now is not None:
            self._values["service_now"] = service_now
        if singular is not None:
            self._values["singular"] = singular
        if slack is not None:
            self._values["slack"] = slack
        if trendmicro is not None:
            self._values["trendmicro"] = trendmicro
        if veeva is not None:
            self._values["veeva"] = veeva
        if zendesk is not None:
            self._values["zendesk"] = zendesk

    @builtins.property
    def amplitude(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude"]:
        '''amplitude block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#amplitude AppflowFlow#amplitude}
        '''
        result = self._values.get("amplitude")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude"], result)

    @builtins.property
    def custom_connector(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector"]:
        '''custom_connector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_connector AppflowFlow#custom_connector}
        '''
        result = self._values.get("custom_connector")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector"], result)

    @builtins.property
    def datadog(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog"]:
        '''datadog block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#datadog AppflowFlow#datadog}
        '''
        result = self._values.get("datadog")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog"], result)

    @builtins.property
    def dynatrace(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace"]:
        '''dynatrace block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#dynatrace AppflowFlow#dynatrace}
        '''
        result = self._values.get("dynatrace")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace"], result)

    @builtins.property
    def google_analytics(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics"]:
        '''google_analytics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#google_analytics AppflowFlow#google_analytics}
        '''
        result = self._values.get("google_analytics")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics"], result)

    @builtins.property
    def infor_nexus(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus"]:
        '''infor_nexus block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#infor_nexus AppflowFlow#infor_nexus}
        '''
        result = self._values.get("infor_nexus")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus"], result)

    @builtins.property
    def marketo(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo"]:
        '''marketo block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#marketo AppflowFlow#marketo}
        '''
        result = self._values.get("marketo")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo"], result)

    @builtins.property
    def s3(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3 AppflowFlow#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3"], result)

    @builtins.property
    def salesforce(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce"]:
        '''salesforce block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#salesforce AppflowFlow#salesforce}
        '''
        result = self._values.get("salesforce")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce"], result)

    @builtins.property
    def sapo_data(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData"]:
        '''sapo_data block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#sapo_data AppflowFlow#sapo_data}
        '''
        result = self._values.get("sapo_data")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData"], result)

    @builtins.property
    def service_now(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow"]:
        '''service_now block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#service_now AppflowFlow#service_now}
        '''
        result = self._values.get("service_now")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow"], result)

    @builtins.property
    def singular(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular"]:
        '''singular block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#singular AppflowFlow#singular}
        '''
        result = self._values.get("singular")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular"], result)

    @builtins.property
    def slack(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack"]:
        '''slack block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#slack AppflowFlow#slack}
        '''
        result = self._values.get("slack")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack"], result)

    @builtins.property
    def trendmicro(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro"]:
        '''trendmicro block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trendmicro AppflowFlow#trendmicro}
        '''
        result = self._values.get("trendmicro")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro"], result)

    @builtins.property
    def veeva(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva"]:
        '''veeva block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#veeva AppflowFlow#veeva}
        '''
        result = self._values.get("veeva")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva"], result)

    @builtins.property
    def zendesk(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk"]:
        '''zendesk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#zendesk AppflowFlow#zendesk}
        '''
        result = self._values.get("zendesk")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            def stub(*, object: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitudeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitudeOutputReference",
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
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector",
    jsii_struct_bases=[],
    name_mapping={
        "entity_name": "entityName",
        "custom_properties": "customProperties",
    },
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector:
    def __init__(
        self,
        *,
        entity_name: builtins.str,
        custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param entity_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#entity_name AppflowFlow#entity_name}.
        :param custom_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_properties AppflowFlow#custom_properties}.
        '''
        if __debug__:
            def stub(
                *,
                entity_name: builtins.str,
                custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument entity_name", value=entity_name, expected_type=type_hints["entity_name"])
            check_type(argname="argument custom_properties", value=custom_properties, expected_type=type_hints["custom_properties"])
        self._values: typing.Dict[str, typing.Any] = {
            "entity_name": entity_name,
        }
        if custom_properties is not None:
            self._values["custom_properties"] = custom_properties

    @builtins.property
    def entity_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#entity_name AppflowFlow#entity_name}.'''
        result = self._values.get("entity_name")
        assert result is not None, "Required property 'entity_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_properties AppflowFlow#custom_properties}.'''
        result = self._values.get("custom_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnectorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnectorOutputReference",
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

    @jsii.member(jsii_name="resetCustomProperties")
    def reset_custom_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomProperties", []))

    @builtins.property
    @jsii.member(jsii_name="customPropertiesInput")
    def custom_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="entityNameInput")
    def entity_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entityNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customProperties")
    def custom_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "customProperties"))

    @custom_properties.setter
    def custom_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customProperties", value)

    @builtins.property
    @jsii.member(jsii_name="entityName")
    def entity_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "entityName"))

    @entity_name.setter
    def entity_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            def stub(*, object: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadogOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadogOutputReference",
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
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            def stub(*, object: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatraceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatraceOutputReference",
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
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            def stub(*, object: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalyticsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalyticsOutputReference",
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
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            def stub(*, object: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexusOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexusOutputReference",
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
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            def stub(*, object: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketoOutputReference",
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
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesOutputReference",
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

    @jsii.member(jsii_name="putAmplitude")
    def put_amplitude(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putAmplitude", [value]))

    @jsii.member(jsii_name="putCustomConnector")
    def put_custom_connector(
        self,
        *,
        entity_name: builtins.str,
        custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param entity_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#entity_name AppflowFlow#entity_name}.
        :param custom_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_properties AppflowFlow#custom_properties}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector(
            entity_name=entity_name, custom_properties=custom_properties
        )

        return typing.cast(None, jsii.invoke(self, "putCustomConnector", [value]))

    @jsii.member(jsii_name="putDatadog")
    def put_datadog(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putDatadog", [value]))

    @jsii.member(jsii_name="putDynatrace")
    def put_dynatrace(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putDynatrace", [value]))

    @jsii.member(jsii_name="putGoogleAnalytics")
    def put_google_analytics(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putGoogleAnalytics", [value]))

    @jsii.member(jsii_name="putInforNexus")
    def put_infor_nexus(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putInforNexus", [value]))

    @jsii.member(jsii_name="putMarketo")
    def put_marketo(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putMarketo", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        bucket_name: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        s3_input_format_config: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param s3_input_format_config: s3_input_format_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_input_format_config AppflowFlow#s3_input_format_config}
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            s3_input_format_config=s3_input_format_config,
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="putSalesforce")
    def put_salesforce(
        self,
        *,
        object: builtins.str,
        enable_dynamic_field_update: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_deleted_records: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param enable_dynamic_field_update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#enable_dynamic_field_update AppflowFlow#enable_dynamic_field_update}.
        :param include_deleted_records: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_deleted_records AppflowFlow#include_deleted_records}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce(
            object=object,
            enable_dynamic_field_update=enable_dynamic_field_update,
            include_deleted_records=include_deleted_records,
        )

        return typing.cast(None, jsii.invoke(self, "putSalesforce", [value]))

    @jsii.member(jsii_name="putSapoData")
    def put_sapo_data(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putSapoData", [value]))

    @jsii.member(jsii_name="putServiceNow")
    def put_service_now(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putServiceNow", [value]))

    @jsii.member(jsii_name="putSingular")
    def put_singular(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putSingular", [value]))

    @jsii.member(jsii_name="putSlack")
    def put_slack(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putSlack", [value]))

    @jsii.member(jsii_name="putTrendmicro")
    def put_trendmicro(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putTrendmicro", [value]))

    @jsii.member(jsii_name="putVeeva")
    def put_veeva(
        self,
        *,
        object: builtins.str,
        document_type: typing.Optional[builtins.str] = None,
        include_all_versions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_renditions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_source_files: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param document_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#document_type AppflowFlow#document_type}.
        :param include_all_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_all_versions AppflowFlow#include_all_versions}.
        :param include_renditions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_renditions AppflowFlow#include_renditions}.
        :param include_source_files: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_source_files AppflowFlow#include_source_files}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva(
            object=object,
            document_type=document_type,
            include_all_versions=include_all_versions,
            include_renditions=include_renditions,
            include_source_files=include_source_files,
        )

        return typing.cast(None, jsii.invoke(self, "putVeeva", [value]))

    @jsii.member(jsii_name="putZendesk")
    def put_zendesk(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk(
            object=object
        )

        return typing.cast(None, jsii.invoke(self, "putZendesk", [value]))

    @jsii.member(jsii_name="resetAmplitude")
    def reset_amplitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAmplitude", []))

    @jsii.member(jsii_name="resetCustomConnector")
    def reset_custom_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomConnector", []))

    @jsii.member(jsii_name="resetDatadog")
    def reset_datadog(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatadog", []))

    @jsii.member(jsii_name="resetDynatrace")
    def reset_dynatrace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynatrace", []))

    @jsii.member(jsii_name="resetGoogleAnalytics")
    def reset_google_analytics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleAnalytics", []))

    @jsii.member(jsii_name="resetInforNexus")
    def reset_infor_nexus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInforNexus", []))

    @jsii.member(jsii_name="resetMarketo")
    def reset_marketo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMarketo", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @jsii.member(jsii_name="resetSalesforce")
    def reset_salesforce(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSalesforce", []))

    @jsii.member(jsii_name="resetSapoData")
    def reset_sapo_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSapoData", []))

    @jsii.member(jsii_name="resetServiceNow")
    def reset_service_now(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceNow", []))

    @jsii.member(jsii_name="resetSingular")
    def reset_singular(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingular", []))

    @jsii.member(jsii_name="resetSlack")
    def reset_slack(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlack", []))

    @jsii.member(jsii_name="resetTrendmicro")
    def reset_trendmicro(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrendmicro", []))

    @jsii.member(jsii_name="resetVeeva")
    def reset_veeva(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVeeva", []))

    @jsii.member(jsii_name="resetZendesk")
    def reset_zendesk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZendesk", []))

    @builtins.property
    @jsii.member(jsii_name="amplitude")
    def amplitude(
        self,
    ) -> AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitudeOutputReference:
        return typing.cast(AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitudeOutputReference, jsii.get(self, "amplitude"))

    @builtins.property
    @jsii.member(jsii_name="customConnector")
    def custom_connector(
        self,
    ) -> AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnectorOutputReference:
        return typing.cast(AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnectorOutputReference, jsii.get(self, "customConnector"))

    @builtins.property
    @jsii.member(jsii_name="datadog")
    def datadog(
        self,
    ) -> AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadogOutputReference:
        return typing.cast(AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadogOutputReference, jsii.get(self, "datadog"))

    @builtins.property
    @jsii.member(jsii_name="dynatrace")
    def dynatrace(
        self,
    ) -> AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatraceOutputReference:
        return typing.cast(AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatraceOutputReference, jsii.get(self, "dynatrace"))

    @builtins.property
    @jsii.member(jsii_name="googleAnalytics")
    def google_analytics(
        self,
    ) -> AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalyticsOutputReference:
        return typing.cast(AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalyticsOutputReference, jsii.get(self, "googleAnalytics"))

    @builtins.property
    @jsii.member(jsii_name="inforNexus")
    def infor_nexus(
        self,
    ) -> AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexusOutputReference:
        return typing.cast(AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexusOutputReference, jsii.get(self, "inforNexus"))

    @builtins.property
    @jsii.member(jsii_name="marketo")
    def marketo(
        self,
    ) -> AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketoOutputReference:
        return typing.cast(AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketoOutputReference, jsii.get(self, "marketo"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3OutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="salesforce")
    def salesforce(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforceOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforceOutputReference", jsii.get(self, "salesforce"))

    @builtins.property
    @jsii.member(jsii_name="sapoData")
    def sapo_data(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoDataOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoDataOutputReference", jsii.get(self, "sapoData"))

    @builtins.property
    @jsii.member(jsii_name="serviceNow")
    def service_now(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNowOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNowOutputReference", jsii.get(self, "serviceNow"))

    @builtins.property
    @jsii.member(jsii_name="singular")
    def singular(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingularOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingularOutputReference", jsii.get(self, "singular"))

    @builtins.property
    @jsii.member(jsii_name="slack")
    def slack(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlackOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlackOutputReference", jsii.get(self, "slack"))

    @builtins.property
    @jsii.member(jsii_name="trendmicro")
    def trendmicro(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicroOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicroOutputReference", jsii.get(self, "trendmicro"))

    @builtins.property
    @jsii.member(jsii_name="veeva")
    def veeva(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeevaOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeevaOutputReference", jsii.get(self, "veeva"))

    @builtins.property
    @jsii.member(jsii_name="zendesk")
    def zendesk(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendeskOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendeskOutputReference", jsii.get(self, "zendesk"))

    @builtins.property
    @jsii.member(jsii_name="amplitudeInput")
    def amplitude_input(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude], jsii.get(self, "amplitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="customConnectorInput")
    def custom_connector_input(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector], jsii.get(self, "customConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="datadogInput")
    def datadog_input(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog], jsii.get(self, "datadogInput"))

    @builtins.property
    @jsii.member(jsii_name="dynatraceInput")
    def dynatrace_input(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace], jsii.get(self, "dynatraceInput"))

    @builtins.property
    @jsii.member(jsii_name="googleAnalyticsInput")
    def google_analytics_input(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics], jsii.get(self, "googleAnalyticsInput"))

    @builtins.property
    @jsii.member(jsii_name="inforNexusInput")
    def infor_nexus_input(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus], jsii.get(self, "inforNexusInput"))

    @builtins.property
    @jsii.member(jsii_name="marketoInput")
    def marketo_input(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo], jsii.get(self, "marketoInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="salesforceInput")
    def salesforce_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce"], jsii.get(self, "salesforceInput"))

    @builtins.property
    @jsii.member(jsii_name="sapoDataInput")
    def sapo_data_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData"], jsii.get(self, "sapoDataInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNowInput")
    def service_now_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow"], jsii.get(self, "serviceNowInput"))

    @builtins.property
    @jsii.member(jsii_name="singularInput")
    def singular_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular"], jsii.get(self, "singularInput"))

    @builtins.property
    @jsii.member(jsii_name="slackInput")
    def slack_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack"], jsii.get(self, "slackInput"))

    @builtins.property
    @jsii.member(jsii_name="trendmicroInput")
    def trendmicro_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro"], jsii.get(self, "trendmicroInput"))

    @builtins.property
    @jsii.member(jsii_name="veevaInput")
    def veeva_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva"], jsii.get(self, "veevaInput"))

    @builtins.property
    @jsii.member(jsii_name="zendeskInput")
    def zendesk_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk"], jsii.get(self, "zendeskInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorProperties]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorProperties],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorProperties],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "s3_input_format_config": "s3InputFormatConfig",
    },
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
        s3_input_format_config: typing.Optional[typing.Union["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.
        :param s3_input_format_config: s3_input_format_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_input_format_config AppflowFlow#s3_input_format_config}
        '''
        if isinstance(s3_input_format_config, dict):
            s3_input_format_config = AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig(**s3_input_format_config)
        if __debug__:
            def stub(
                *,
                bucket_name: builtins.str,
                bucket_prefix: typing.Optional[builtins.str] = None,
                s3_input_format_config: typing.Optional[typing.Union[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument s3_input_format_config", value=s3_input_format_config, expected_type=type_hints["s3_input_format_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
        }
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if s3_input_format_config is not None:
            self._values["s3_input_format_config"] = s3_input_format_config

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_name AppflowFlow#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#bucket_prefix AppflowFlow#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_input_format_config(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig"]:
        '''s3_input_format_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_input_format_config AppflowFlow#s3_input_format_config}
        '''
        result = self._values.get("s3_input_format_config")
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3OutputReference",
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

    @jsii.member(jsii_name="putS3InputFormatConfig")
    def put_s3_input_format_config(
        self,
        *,
        s3_input_file_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_input_file_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_input_file_type AppflowFlow#s3_input_file_type}.
        '''
        value = AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig(
            s3_input_file_type=s3_input_file_type
        )

        return typing.cast(None, jsii.invoke(self, "putS3InputFormatConfig", [value]))

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @jsii.member(jsii_name="resetS3InputFormatConfig")
    def reset_s3_input_format_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3InputFormatConfig", []))

    @builtins.property
    @jsii.member(jsii_name="s3InputFormatConfig")
    def s3_input_format_config(
        self,
    ) -> "AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfigOutputReference":
        return typing.cast("AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfigOutputReference", jsii.get(self, "s3InputFormatConfig"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="s3InputFormatConfigInput")
    def s3_input_format_config_input(
        self,
    ) -> typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig"]:
        return typing.cast(typing.Optional["AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig"], jsii.get(self, "s3InputFormatConfigInput"))

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
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig",
    jsii_struct_bases=[],
    name_mapping={"s3_input_file_type": "s3InputFileType"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig:
    def __init__(
        self,
        *,
        s3_input_file_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_input_file_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_input_file_type AppflowFlow#s3_input_file_type}.
        '''
        if __debug__:
            def stub(
                *,
                s3_input_file_type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument s3_input_file_type", value=s3_input_file_type, expected_type=type_hints["s3_input_file_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if s3_input_file_type is not None:
            self._values["s3_input_file_type"] = s3_input_file_type

    @builtins.property
    def s3_input_file_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3_input_file_type AppflowFlow#s3_input_file_type}.'''
        result = self._values.get("s3_input_file_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfigOutputReference",
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

    @jsii.member(jsii_name="resetS3InputFileType")
    def reset_s3_input_file_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3InputFileType", []))

    @builtins.property
    @jsii.member(jsii_name="s3InputFileTypeInput")
    def s3_input_file_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3InputFileTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="s3InputFileType")
    def s3_input_file_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3InputFileType"))

    @s3_input_file_type.setter
    def s3_input_file_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3InputFileType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce",
    jsii_struct_bases=[],
    name_mapping={
        "object": "object",
        "enable_dynamic_field_update": "enableDynamicFieldUpdate",
        "include_deleted_records": "includeDeletedRecords",
    },
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce:
    def __init__(
        self,
        *,
        object: builtins.str,
        enable_dynamic_field_update: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_deleted_records: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param enable_dynamic_field_update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#enable_dynamic_field_update AppflowFlow#enable_dynamic_field_update}.
        :param include_deleted_records: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_deleted_records AppflowFlow#include_deleted_records}.
        '''
        if __debug__:
            def stub(
                *,
                object: builtins.str,
                enable_dynamic_field_update: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                include_deleted_records: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument enable_dynamic_field_update", value=enable_dynamic_field_update, expected_type=type_hints["enable_dynamic_field_update"])
            check_type(argname="argument include_deleted_records", value=include_deleted_records, expected_type=type_hints["include_deleted_records"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }
        if enable_dynamic_field_update is not None:
            self._values["enable_dynamic_field_update"] = enable_dynamic_field_update
        if include_deleted_records is not None:
            self._values["include_deleted_records"] = include_deleted_records

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable_dynamic_field_update(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#enable_dynamic_field_update AppflowFlow#enable_dynamic_field_update}.'''
        result = self._values.get("enable_dynamic_field_update")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include_deleted_records(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_deleted_records AppflowFlow#include_deleted_records}.'''
        result = self._values.get("include_deleted_records")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforceOutputReference",
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

    @jsii.member(jsii_name="resetEnableDynamicFieldUpdate")
    def reset_enable_dynamic_field_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableDynamicFieldUpdate", []))

    @jsii.member(jsii_name="resetIncludeDeletedRecords")
    def reset_include_deleted_records(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeDeletedRecords", []))

    @builtins.property
    @jsii.member(jsii_name="enableDynamicFieldUpdateInput")
    def enable_dynamic_field_update_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableDynamicFieldUpdateInput"))

    @builtins.property
    @jsii.member(jsii_name="includeDeletedRecordsInput")
    def include_deleted_records_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeDeletedRecordsInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="enableDynamicFieldUpdate")
    def enable_dynamic_field_update(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableDynamicFieldUpdate"))

    @enable_dynamic_field_update.setter
    def enable_dynamic_field_update(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDynamicFieldUpdate", value)

    @builtins.property
    @jsii.member(jsii_name="includeDeletedRecords")
    def include_deleted_records(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeDeletedRecords"))

    @include_deleted_records.setter
    def include_deleted_records(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeDeletedRecords", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            def stub(*, object: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoDataOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoDataOutputReference",
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
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            def stub(*, object: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNowOutputReference",
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
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            def stub(*, object: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingularOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingularOutputReference",
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
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            def stub(*, object: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlackOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlackOutputReference",
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
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            def stub(*, object: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicroOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicroOutputReference",
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
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva",
    jsii_struct_bases=[],
    name_mapping={
        "object": "object",
        "document_type": "documentType",
        "include_all_versions": "includeAllVersions",
        "include_renditions": "includeRenditions",
        "include_source_files": "includeSourceFiles",
    },
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva:
    def __init__(
        self,
        *,
        object: builtins.str,
        document_type: typing.Optional[builtins.str] = None,
        include_all_versions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_renditions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_source_files: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        :param document_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#document_type AppflowFlow#document_type}.
        :param include_all_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_all_versions AppflowFlow#include_all_versions}.
        :param include_renditions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_renditions AppflowFlow#include_renditions}.
        :param include_source_files: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_source_files AppflowFlow#include_source_files}.
        '''
        if __debug__:
            def stub(
                *,
                object: builtins.str,
                document_type: typing.Optional[builtins.str] = None,
                include_all_versions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                include_renditions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                include_source_files: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument document_type", value=document_type, expected_type=type_hints["document_type"])
            check_type(argname="argument include_all_versions", value=include_all_versions, expected_type=type_hints["include_all_versions"])
            check_type(argname="argument include_renditions", value=include_renditions, expected_type=type_hints["include_renditions"])
            check_type(argname="argument include_source_files", value=include_source_files, expected_type=type_hints["include_source_files"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }
        if document_type is not None:
            self._values["document_type"] = document_type
        if include_all_versions is not None:
            self._values["include_all_versions"] = include_all_versions
        if include_renditions is not None:
            self._values["include_renditions"] = include_renditions
        if include_source_files is not None:
            self._values["include_source_files"] = include_source_files

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def document_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#document_type AppflowFlow#document_type}.'''
        result = self._values.get("document_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def include_all_versions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_all_versions AppflowFlow#include_all_versions}.'''
        result = self._values.get("include_all_versions")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include_renditions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_renditions AppflowFlow#include_renditions}.'''
        result = self._values.get("include_renditions")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include_source_files(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#include_source_files AppflowFlow#include_source_files}.'''
        result = self._values.get("include_source_files")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeevaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeevaOutputReference",
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

    @jsii.member(jsii_name="resetDocumentType")
    def reset_document_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentType", []))

    @jsii.member(jsii_name="resetIncludeAllVersions")
    def reset_include_all_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeAllVersions", []))

    @jsii.member(jsii_name="resetIncludeRenditions")
    def reset_include_renditions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeRenditions", []))

    @jsii.member(jsii_name="resetIncludeSourceFiles")
    def reset_include_source_files(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeSourceFiles", []))

    @builtins.property
    @jsii.member(jsii_name="documentTypeInput")
    def document_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="includeAllVersionsInput")
    def include_all_versions_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeAllVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeRenditionsInput")
    def include_renditions_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeRenditionsInput"))

    @builtins.property
    @jsii.member(jsii_name="includeSourceFilesInput")
    def include_source_files_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeSourceFilesInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="documentType")
    def document_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "documentType"))

    @document_type.setter
    def document_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentType", value)

    @builtins.property
    @jsii.member(jsii_name="includeAllVersions")
    def include_all_versions(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeAllVersions"))

    @include_all_versions.setter
    def include_all_versions(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeAllVersions", value)

    @builtins.property
    @jsii.member(jsii_name="includeRenditions")
    def include_renditions(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeRenditions"))

    @include_renditions.setter
    def include_renditions(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeRenditions", value)

    @builtins.property
    @jsii.member(jsii_name="includeSourceFiles")
    def include_source_files(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeSourceFiles"))

    @include_source_files.setter
    def include_source_files(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeSourceFiles", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk",
    jsii_struct_bases=[],
    name_mapping={"object": "object"},
)
class AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk:
    def __init__(self, *, object: builtins.str) -> None:
        '''
        :param object: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.
        '''
        if __debug__:
            def stub(*, object: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[str, typing.Any] = {
            "object": object,
        }

    @builtins.property
    def object(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#object AppflowFlow#object}.'''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendeskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendeskOutputReference",
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
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk]:
        return typing.cast(typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowTask",
    jsii_struct_bases=[],
    name_mapping={
        "source_fields": "sourceFields",
        "task_type": "taskType",
        "connector_operator": "connectorOperator",
        "destination_field": "destinationField",
        "task_properties": "taskProperties",
    },
)
class AppflowFlowTask:
    def __init__(
        self,
        *,
        source_fields: typing.Sequence[builtins.str],
        task_type: builtins.str,
        connector_operator: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppflowFlowTaskConnectorOperator", typing.Dict[str, typing.Any]]]]] = None,
        destination_field: typing.Optional[builtins.str] = None,
        task_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param source_fields: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#source_fields AppflowFlow#source_fields}.
        :param task_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#task_type AppflowFlow#task_type}.
        :param connector_operator: connector_operator block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_operator AppflowFlow#connector_operator}
        :param destination_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#destination_field AppflowFlow#destination_field}.
        :param task_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#task_properties AppflowFlow#task_properties}.
        '''
        if __debug__:
            def stub(
                *,
                source_fields: typing.Sequence[builtins.str],
                task_type: builtins.str,
                connector_operator: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppflowFlowTaskConnectorOperator, typing.Dict[str, typing.Any]]]]] = None,
                destination_field: typing.Optional[builtins.str] = None,
                task_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument source_fields", value=source_fields, expected_type=type_hints["source_fields"])
            check_type(argname="argument task_type", value=task_type, expected_type=type_hints["task_type"])
            check_type(argname="argument connector_operator", value=connector_operator, expected_type=type_hints["connector_operator"])
            check_type(argname="argument destination_field", value=destination_field, expected_type=type_hints["destination_field"])
            check_type(argname="argument task_properties", value=task_properties, expected_type=type_hints["task_properties"])
        self._values: typing.Dict[str, typing.Any] = {
            "source_fields": source_fields,
            "task_type": task_type,
        }
        if connector_operator is not None:
            self._values["connector_operator"] = connector_operator
        if destination_field is not None:
            self._values["destination_field"] = destination_field
        if task_properties is not None:
            self._values["task_properties"] = task_properties

    @builtins.property
    def source_fields(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#source_fields AppflowFlow#source_fields}.'''
        result = self._values.get("source_fields")
        assert result is not None, "Required property 'source_fields' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def task_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#task_type AppflowFlow#task_type}.'''
        result = self._values.get("task_type")
        assert result is not None, "Required property 'task_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connector_operator(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppflowFlowTaskConnectorOperator"]]]:
        '''connector_operator block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#connector_operator AppflowFlow#connector_operator}
        '''
        result = self._values.get("connector_operator")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppflowFlowTaskConnectorOperator"]]], result)

    @builtins.property
    def destination_field(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#destination_field AppflowFlow#destination_field}.'''
        result = self._values.get("destination_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def task_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#task_properties AppflowFlow#task_properties}.'''
        result = self._values.get("task_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowTask(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowTaskConnectorOperator",
    jsii_struct_bases=[],
    name_mapping={
        "amplitude": "amplitude",
        "custom_connector": "customConnector",
        "datadog": "datadog",
        "dynatrace": "dynatrace",
        "google_analytics": "googleAnalytics",
        "infor_nexus": "inforNexus",
        "marketo": "marketo",
        "s3": "s3",
        "salesforce": "salesforce",
        "sapo_data": "sapoData",
        "service_now": "serviceNow",
        "singular": "singular",
        "slack": "slack",
        "trendmicro": "trendmicro",
        "veeva": "veeva",
        "zendesk": "zendesk",
    },
)
class AppflowFlowTaskConnectorOperator:
    def __init__(
        self,
        *,
        amplitude: typing.Optional[builtins.str] = None,
        custom_connector: typing.Optional[builtins.str] = None,
        datadog: typing.Optional[builtins.str] = None,
        dynatrace: typing.Optional[builtins.str] = None,
        google_analytics: typing.Optional[builtins.str] = None,
        infor_nexus: typing.Optional[builtins.str] = None,
        marketo: typing.Optional[builtins.str] = None,
        s3: typing.Optional[builtins.str] = None,
        salesforce: typing.Optional[builtins.str] = None,
        sapo_data: typing.Optional[builtins.str] = None,
        service_now: typing.Optional[builtins.str] = None,
        singular: typing.Optional[builtins.str] = None,
        slack: typing.Optional[builtins.str] = None,
        trendmicro: typing.Optional[builtins.str] = None,
        veeva: typing.Optional[builtins.str] = None,
        zendesk: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param amplitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#amplitude AppflowFlow#amplitude}.
        :param custom_connector: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_connector AppflowFlow#custom_connector}.
        :param datadog: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#datadog AppflowFlow#datadog}.
        :param dynatrace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#dynatrace AppflowFlow#dynatrace}.
        :param google_analytics: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#google_analytics AppflowFlow#google_analytics}.
        :param infor_nexus: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#infor_nexus AppflowFlow#infor_nexus}.
        :param marketo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#marketo AppflowFlow#marketo}.
        :param s3: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3 AppflowFlow#s3}.
        :param salesforce: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#salesforce AppflowFlow#salesforce}.
        :param sapo_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#sapo_data AppflowFlow#sapo_data}.
        :param service_now: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#service_now AppflowFlow#service_now}.
        :param singular: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#singular AppflowFlow#singular}.
        :param slack: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#slack AppflowFlow#slack}.
        :param trendmicro: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trendmicro AppflowFlow#trendmicro}.
        :param veeva: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#veeva AppflowFlow#veeva}.
        :param zendesk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#zendesk AppflowFlow#zendesk}.
        '''
        if __debug__:
            def stub(
                *,
                amplitude: typing.Optional[builtins.str] = None,
                custom_connector: typing.Optional[builtins.str] = None,
                datadog: typing.Optional[builtins.str] = None,
                dynatrace: typing.Optional[builtins.str] = None,
                google_analytics: typing.Optional[builtins.str] = None,
                infor_nexus: typing.Optional[builtins.str] = None,
                marketo: typing.Optional[builtins.str] = None,
                s3: typing.Optional[builtins.str] = None,
                salesforce: typing.Optional[builtins.str] = None,
                sapo_data: typing.Optional[builtins.str] = None,
                service_now: typing.Optional[builtins.str] = None,
                singular: typing.Optional[builtins.str] = None,
                slack: typing.Optional[builtins.str] = None,
                trendmicro: typing.Optional[builtins.str] = None,
                veeva: typing.Optional[builtins.str] = None,
                zendesk: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument amplitude", value=amplitude, expected_type=type_hints["amplitude"])
            check_type(argname="argument custom_connector", value=custom_connector, expected_type=type_hints["custom_connector"])
            check_type(argname="argument datadog", value=datadog, expected_type=type_hints["datadog"])
            check_type(argname="argument dynatrace", value=dynatrace, expected_type=type_hints["dynatrace"])
            check_type(argname="argument google_analytics", value=google_analytics, expected_type=type_hints["google_analytics"])
            check_type(argname="argument infor_nexus", value=infor_nexus, expected_type=type_hints["infor_nexus"])
            check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
            check_type(argname="argument sapo_data", value=sapo_data, expected_type=type_hints["sapo_data"])
            check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
            check_type(argname="argument singular", value=singular, expected_type=type_hints["singular"])
            check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
            check_type(argname="argument trendmicro", value=trendmicro, expected_type=type_hints["trendmicro"])
            check_type(argname="argument veeva", value=veeva, expected_type=type_hints["veeva"])
            check_type(argname="argument zendesk", value=zendesk, expected_type=type_hints["zendesk"])
        self._values: typing.Dict[str, typing.Any] = {}
        if amplitude is not None:
            self._values["amplitude"] = amplitude
        if custom_connector is not None:
            self._values["custom_connector"] = custom_connector
        if datadog is not None:
            self._values["datadog"] = datadog
        if dynatrace is not None:
            self._values["dynatrace"] = dynatrace
        if google_analytics is not None:
            self._values["google_analytics"] = google_analytics
        if infor_nexus is not None:
            self._values["infor_nexus"] = infor_nexus
        if marketo is not None:
            self._values["marketo"] = marketo
        if s3 is not None:
            self._values["s3"] = s3
        if salesforce is not None:
            self._values["salesforce"] = salesforce
        if sapo_data is not None:
            self._values["sapo_data"] = sapo_data
        if service_now is not None:
            self._values["service_now"] = service_now
        if singular is not None:
            self._values["singular"] = singular
        if slack is not None:
            self._values["slack"] = slack
        if trendmicro is not None:
            self._values["trendmicro"] = trendmicro
        if veeva is not None:
            self._values["veeva"] = veeva
        if zendesk is not None:
            self._values["zendesk"] = zendesk

    @builtins.property
    def amplitude(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#amplitude AppflowFlow#amplitude}.'''
        result = self._values.get("amplitude")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_connector(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#custom_connector AppflowFlow#custom_connector}.'''
        result = self._values.get("custom_connector")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def datadog(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#datadog AppflowFlow#datadog}.'''
        result = self._values.get("datadog")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynatrace(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#dynatrace AppflowFlow#dynatrace}.'''
        result = self._values.get("dynatrace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def google_analytics(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#google_analytics AppflowFlow#google_analytics}.'''
        result = self._values.get("google_analytics")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def infor_nexus(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#infor_nexus AppflowFlow#infor_nexus}.'''
        result = self._values.get("infor_nexus")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def marketo(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#marketo AppflowFlow#marketo}.'''
        result = self._values.get("marketo")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#s3 AppflowFlow#s3}.'''
        result = self._values.get("s3")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def salesforce(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#salesforce AppflowFlow#salesforce}.'''
        result = self._values.get("salesforce")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sapo_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#sapo_data AppflowFlow#sapo_data}.'''
        result = self._values.get("sapo_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_now(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#service_now AppflowFlow#service_now}.'''
        result = self._values.get("service_now")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def singular(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#singular AppflowFlow#singular}.'''
        result = self._values.get("singular")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slack(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#slack AppflowFlow#slack}.'''
        result = self._values.get("slack")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trendmicro(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trendmicro AppflowFlow#trendmicro}.'''
        result = self._values.get("trendmicro")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def veeva(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#veeva AppflowFlow#veeva}.'''
        result = self._values.get("veeva")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zendesk(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#zendesk AppflowFlow#zendesk}.'''
        result = self._values.get("zendesk")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowTaskConnectorOperator(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowTaskConnectorOperatorList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowTaskConnectorOperatorList",
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
    ) -> "AppflowFlowTaskConnectorOperatorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppflowFlowTaskConnectorOperatorOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppflowFlowTaskConnectorOperator]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppflowFlowTaskConnectorOperator]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppflowFlowTaskConnectorOperator]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppflowFlowTaskConnectorOperator]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowTaskConnectorOperatorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowTaskConnectorOperatorOutputReference",
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

    @jsii.member(jsii_name="resetAmplitude")
    def reset_amplitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAmplitude", []))

    @jsii.member(jsii_name="resetCustomConnector")
    def reset_custom_connector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomConnector", []))

    @jsii.member(jsii_name="resetDatadog")
    def reset_datadog(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatadog", []))

    @jsii.member(jsii_name="resetDynatrace")
    def reset_dynatrace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynatrace", []))

    @jsii.member(jsii_name="resetGoogleAnalytics")
    def reset_google_analytics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleAnalytics", []))

    @jsii.member(jsii_name="resetInforNexus")
    def reset_infor_nexus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInforNexus", []))

    @jsii.member(jsii_name="resetMarketo")
    def reset_marketo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMarketo", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @jsii.member(jsii_name="resetSalesforce")
    def reset_salesforce(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSalesforce", []))

    @jsii.member(jsii_name="resetSapoData")
    def reset_sapo_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSapoData", []))

    @jsii.member(jsii_name="resetServiceNow")
    def reset_service_now(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceNow", []))

    @jsii.member(jsii_name="resetSingular")
    def reset_singular(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingular", []))

    @jsii.member(jsii_name="resetSlack")
    def reset_slack(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlack", []))

    @jsii.member(jsii_name="resetTrendmicro")
    def reset_trendmicro(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrendmicro", []))

    @jsii.member(jsii_name="resetVeeva")
    def reset_veeva(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVeeva", []))

    @jsii.member(jsii_name="resetZendesk")
    def reset_zendesk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZendesk", []))

    @builtins.property
    @jsii.member(jsii_name="amplitudeInput")
    def amplitude_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "amplitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="customConnectorInput")
    def custom_connector_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customConnectorInput"))

    @builtins.property
    @jsii.member(jsii_name="datadogInput")
    def datadog_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datadogInput"))

    @builtins.property
    @jsii.member(jsii_name="dynatraceInput")
    def dynatrace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dynatraceInput"))

    @builtins.property
    @jsii.member(jsii_name="googleAnalyticsInput")
    def google_analytics_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "googleAnalyticsInput"))

    @builtins.property
    @jsii.member(jsii_name="inforNexusInput")
    def infor_nexus_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inforNexusInput"))

    @builtins.property
    @jsii.member(jsii_name="marketoInput")
    def marketo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "marketoInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="salesforceInput")
    def salesforce_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "salesforceInput"))

    @builtins.property
    @jsii.member(jsii_name="sapoDataInput")
    def sapo_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sapoDataInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNowInput")
    def service_now_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNowInput"))

    @builtins.property
    @jsii.member(jsii_name="singularInput")
    def singular_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "singularInput"))

    @builtins.property
    @jsii.member(jsii_name="slackInput")
    def slack_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "slackInput"))

    @builtins.property
    @jsii.member(jsii_name="trendmicroInput")
    def trendmicro_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trendmicroInput"))

    @builtins.property
    @jsii.member(jsii_name="veevaInput")
    def veeva_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "veevaInput"))

    @builtins.property
    @jsii.member(jsii_name="zendeskInput")
    def zendesk_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zendeskInput"))

    @builtins.property
    @jsii.member(jsii_name="amplitude")
    def amplitude(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "amplitude"))

    @amplitude.setter
    def amplitude(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amplitude", value)

    @builtins.property
    @jsii.member(jsii_name="customConnector")
    def custom_connector(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customConnector"))

    @custom_connector.setter
    def custom_connector(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customConnector", value)

    @builtins.property
    @jsii.member(jsii_name="datadog")
    def datadog(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datadog"))

    @datadog.setter
    def datadog(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datadog", value)

    @builtins.property
    @jsii.member(jsii_name="dynatrace")
    def dynatrace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dynatrace"))

    @dynatrace.setter
    def dynatrace(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynatrace", value)

    @builtins.property
    @jsii.member(jsii_name="googleAnalytics")
    def google_analytics(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "googleAnalytics"))

    @google_analytics.setter
    def google_analytics(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "googleAnalytics", value)

    @builtins.property
    @jsii.member(jsii_name="inforNexus")
    def infor_nexus(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inforNexus"))

    @infor_nexus.setter
    def infor_nexus(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inforNexus", value)

    @builtins.property
    @jsii.member(jsii_name="marketo")
    def marketo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "marketo"))

    @marketo.setter
    def marketo(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "marketo", value)

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3"))

    @s3.setter
    def s3(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3", value)

    @builtins.property
    @jsii.member(jsii_name="salesforce")
    def salesforce(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "salesforce"))

    @salesforce.setter
    def salesforce(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "salesforce", value)

    @builtins.property
    @jsii.member(jsii_name="sapoData")
    def sapo_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sapoData"))

    @sapo_data.setter
    def sapo_data(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sapoData", value)

    @builtins.property
    @jsii.member(jsii_name="serviceNow")
    def service_now(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceNow"))

    @service_now.setter
    def service_now(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceNow", value)

    @builtins.property
    @jsii.member(jsii_name="singular")
    def singular(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "singular"))

    @singular.setter
    def singular(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "singular", value)

    @builtins.property
    @jsii.member(jsii_name="slack")
    def slack(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "slack"))

    @slack.setter
    def slack(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slack", value)

    @builtins.property
    @jsii.member(jsii_name="trendmicro")
    def trendmicro(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trendmicro"))

    @trendmicro.setter
    def trendmicro(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trendmicro", value)

    @builtins.property
    @jsii.member(jsii_name="veeva")
    def veeva(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "veeva"))

    @veeva.setter
    def veeva(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "veeva", value)

    @builtins.property
    @jsii.member(jsii_name="zendesk")
    def zendesk(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zendesk"))

    @zendesk.setter
    def zendesk(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zendesk", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppflowFlowTaskConnectorOperator, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppflowFlowTaskConnectorOperator, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppflowFlowTaskConnectorOperator, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[AppflowFlowTaskConnectorOperator, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowTaskList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowTaskList",
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
    def get(self, index: jsii.Number) -> "AppflowFlowTaskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppflowFlowTaskOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppflowFlowTask]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppflowFlowTask]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppflowFlowTask]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppflowFlowTask]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppflowFlowTaskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowTaskOutputReference",
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

    @jsii.member(jsii_name="putConnectorOperator")
    def put_connector_operator(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppflowFlowTaskConnectorOperator, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppflowFlowTaskConnectorOperator, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConnectorOperator", [value]))

    @jsii.member(jsii_name="resetConnectorOperator")
    def reset_connector_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectorOperator", []))

    @jsii.member(jsii_name="resetDestinationField")
    def reset_destination_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationField", []))

    @jsii.member(jsii_name="resetTaskProperties")
    def reset_task_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskProperties", []))

    @builtins.property
    @jsii.member(jsii_name="connectorOperator")
    def connector_operator(self) -> AppflowFlowTaskConnectorOperatorList:
        return typing.cast(AppflowFlowTaskConnectorOperatorList, jsii.get(self, "connectorOperator"))

    @builtins.property
    @jsii.member(jsii_name="connectorOperatorInput")
    def connector_operator_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppflowFlowTaskConnectorOperator]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppflowFlowTaskConnectorOperator]]], jsii.get(self, "connectorOperatorInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationFieldInput")
    def destination_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFieldsInput")
    def source_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="taskPropertiesInput")
    def task_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "taskPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="taskTypeInput")
    def task_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationField")
    def destination_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationField"))

    @destination_field.setter
    def destination_field(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationField", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFields")
    def source_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceFields"))

    @source_fields.setter
    def source_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFields", value)

    @builtins.property
    @jsii.member(jsii_name="taskProperties")
    def task_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "taskProperties"))

    @task_properties.setter
    def task_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskProperties", value)

    @builtins.property
    @jsii.member(jsii_name="taskType")
    def task_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskType"))

    @task_type.setter
    def task_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppflowFlowTask, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppflowFlowTask, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppflowFlowTask, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[AppflowFlowTask, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowTriggerConfig",
    jsii_struct_bases=[],
    name_mapping={
        "trigger_type": "triggerType",
        "trigger_properties": "triggerProperties",
    },
)
class AppflowFlowTriggerConfig:
    def __init__(
        self,
        *,
        trigger_type: builtins.str,
        trigger_properties: typing.Optional[typing.Union["AppflowFlowTriggerConfigTriggerProperties", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trigger_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trigger_type AppflowFlow#trigger_type}.
        :param trigger_properties: trigger_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trigger_properties AppflowFlow#trigger_properties}
        '''
        if isinstance(trigger_properties, dict):
            trigger_properties = AppflowFlowTriggerConfigTriggerProperties(**trigger_properties)
        if __debug__:
            def stub(
                *,
                trigger_type: builtins.str,
                trigger_properties: typing.Optional[typing.Union[AppflowFlowTriggerConfigTriggerProperties, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument trigger_type", value=trigger_type, expected_type=type_hints["trigger_type"])
            check_type(argname="argument trigger_properties", value=trigger_properties, expected_type=type_hints["trigger_properties"])
        self._values: typing.Dict[str, typing.Any] = {
            "trigger_type": trigger_type,
        }
        if trigger_properties is not None:
            self._values["trigger_properties"] = trigger_properties

    @builtins.property
    def trigger_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trigger_type AppflowFlow#trigger_type}.'''
        result = self._values.get("trigger_type")
        assert result is not None, "Required property 'trigger_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def trigger_properties(
        self,
    ) -> typing.Optional["AppflowFlowTriggerConfigTriggerProperties"]:
        '''trigger_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#trigger_properties AppflowFlow#trigger_properties}
        '''
        result = self._values.get("trigger_properties")
        return typing.cast(typing.Optional["AppflowFlowTriggerConfigTriggerProperties"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowTriggerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowTriggerConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowTriggerConfigOutputReference",
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

    @jsii.member(jsii_name="putTriggerProperties")
    def put_trigger_properties(
        self,
        *,
        scheduled: typing.Optional[typing.Union["AppflowFlowTriggerConfigTriggerPropertiesScheduled", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scheduled: scheduled block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#scheduled AppflowFlow#scheduled}
        '''
        value = AppflowFlowTriggerConfigTriggerProperties(scheduled=scheduled)

        return typing.cast(None, jsii.invoke(self, "putTriggerProperties", [value]))

    @jsii.member(jsii_name="resetTriggerProperties")
    def reset_trigger_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggerProperties", []))

    @builtins.property
    @jsii.member(jsii_name="triggerProperties")
    def trigger_properties(
        self,
    ) -> "AppflowFlowTriggerConfigTriggerPropertiesOutputReference":
        return typing.cast("AppflowFlowTriggerConfigTriggerPropertiesOutputReference", jsii.get(self, "triggerProperties"))

    @builtins.property
    @jsii.member(jsii_name="triggerPropertiesInput")
    def trigger_properties_input(
        self,
    ) -> typing.Optional["AppflowFlowTriggerConfigTriggerProperties"]:
        return typing.cast(typing.Optional["AppflowFlowTriggerConfigTriggerProperties"], jsii.get(self, "triggerPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerTypeInput")
    def trigger_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "triggerTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerType")
    def trigger_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "triggerType"))

    @trigger_type.setter
    def trigger_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggerType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppflowFlowTriggerConfig]:
        return typing.cast(typing.Optional[AppflowFlowTriggerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppflowFlowTriggerConfig]) -> None:
        if __debug__:
            def stub(value: typing.Optional[AppflowFlowTriggerConfig]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowTriggerConfigTriggerProperties",
    jsii_struct_bases=[],
    name_mapping={"scheduled": "scheduled"},
)
class AppflowFlowTriggerConfigTriggerProperties:
    def __init__(
        self,
        *,
        scheduled: typing.Optional[typing.Union["AppflowFlowTriggerConfigTriggerPropertiesScheduled", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scheduled: scheduled block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#scheduled AppflowFlow#scheduled}
        '''
        if isinstance(scheduled, dict):
            scheduled = AppflowFlowTriggerConfigTriggerPropertiesScheduled(**scheduled)
        if __debug__:
            def stub(
                *,
                scheduled: typing.Optional[typing.Union[AppflowFlowTriggerConfigTriggerPropertiesScheduled, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scheduled", value=scheduled, expected_type=type_hints["scheduled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if scheduled is not None:
            self._values["scheduled"] = scheduled

    @builtins.property
    def scheduled(
        self,
    ) -> typing.Optional["AppflowFlowTriggerConfigTriggerPropertiesScheduled"]:
        '''scheduled block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#scheduled AppflowFlow#scheduled}
        '''
        result = self._values.get("scheduled")
        return typing.cast(typing.Optional["AppflowFlowTriggerConfigTriggerPropertiesScheduled"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowTriggerConfigTriggerProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowTriggerConfigTriggerPropertiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowTriggerConfigTriggerPropertiesOutputReference",
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

    @jsii.member(jsii_name="putScheduled")
    def put_scheduled(
        self,
        *,
        schedule_expression: builtins.str,
        data_pull_mode: typing.Optional[builtins.str] = None,
        first_execution_from: typing.Optional[builtins.str] = None,
        schedule_end_time: typing.Optional[builtins.str] = None,
        schedule_offset: typing.Optional[jsii.Number] = None,
        schedule_start_time: typing.Optional[builtins.str] = None,
        timezone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param schedule_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_expression AppflowFlow#schedule_expression}.
        :param data_pull_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#data_pull_mode AppflowFlow#data_pull_mode}.
        :param first_execution_from: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#first_execution_from AppflowFlow#first_execution_from}.
        :param schedule_end_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_end_time AppflowFlow#schedule_end_time}.
        :param schedule_offset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_offset AppflowFlow#schedule_offset}.
        :param schedule_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_start_time AppflowFlow#schedule_start_time}.
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#timezone AppflowFlow#timezone}.
        '''
        value = AppflowFlowTriggerConfigTriggerPropertiesScheduled(
            schedule_expression=schedule_expression,
            data_pull_mode=data_pull_mode,
            first_execution_from=first_execution_from,
            schedule_end_time=schedule_end_time,
            schedule_offset=schedule_offset,
            schedule_start_time=schedule_start_time,
            timezone=timezone,
        )

        return typing.cast(None, jsii.invoke(self, "putScheduled", [value]))

    @jsii.member(jsii_name="resetScheduled")
    def reset_scheduled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduled", []))

    @builtins.property
    @jsii.member(jsii_name="scheduled")
    def scheduled(
        self,
    ) -> "AppflowFlowTriggerConfigTriggerPropertiesScheduledOutputReference":
        return typing.cast("AppflowFlowTriggerConfigTriggerPropertiesScheduledOutputReference", jsii.get(self, "scheduled"))

    @builtins.property
    @jsii.member(jsii_name="scheduledInput")
    def scheduled_input(
        self,
    ) -> typing.Optional["AppflowFlowTriggerConfigTriggerPropertiesScheduled"]:
        return typing.cast(typing.Optional["AppflowFlowTriggerConfigTriggerPropertiesScheduled"], jsii.get(self, "scheduledInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowTriggerConfigTriggerProperties]:
        return typing.cast(typing.Optional[AppflowFlowTriggerConfigTriggerProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowTriggerConfigTriggerProperties],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowTriggerConfigTriggerProperties],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowTriggerConfigTriggerPropertiesScheduled",
    jsii_struct_bases=[],
    name_mapping={
        "schedule_expression": "scheduleExpression",
        "data_pull_mode": "dataPullMode",
        "first_execution_from": "firstExecutionFrom",
        "schedule_end_time": "scheduleEndTime",
        "schedule_offset": "scheduleOffset",
        "schedule_start_time": "scheduleStartTime",
        "timezone": "timezone",
    },
)
class AppflowFlowTriggerConfigTriggerPropertiesScheduled:
    def __init__(
        self,
        *,
        schedule_expression: builtins.str,
        data_pull_mode: typing.Optional[builtins.str] = None,
        first_execution_from: typing.Optional[builtins.str] = None,
        schedule_end_time: typing.Optional[builtins.str] = None,
        schedule_offset: typing.Optional[jsii.Number] = None,
        schedule_start_time: typing.Optional[builtins.str] = None,
        timezone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param schedule_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_expression AppflowFlow#schedule_expression}.
        :param data_pull_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#data_pull_mode AppflowFlow#data_pull_mode}.
        :param first_execution_from: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#first_execution_from AppflowFlow#first_execution_from}.
        :param schedule_end_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_end_time AppflowFlow#schedule_end_time}.
        :param schedule_offset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_offset AppflowFlow#schedule_offset}.
        :param schedule_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_start_time AppflowFlow#schedule_start_time}.
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#timezone AppflowFlow#timezone}.
        '''
        if __debug__:
            def stub(
                *,
                schedule_expression: builtins.str,
                data_pull_mode: typing.Optional[builtins.str] = None,
                first_execution_from: typing.Optional[builtins.str] = None,
                schedule_end_time: typing.Optional[builtins.str] = None,
                schedule_offset: typing.Optional[jsii.Number] = None,
                schedule_start_time: typing.Optional[builtins.str] = None,
                timezone: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
            check_type(argname="argument data_pull_mode", value=data_pull_mode, expected_type=type_hints["data_pull_mode"])
            check_type(argname="argument first_execution_from", value=first_execution_from, expected_type=type_hints["first_execution_from"])
            check_type(argname="argument schedule_end_time", value=schedule_end_time, expected_type=type_hints["schedule_end_time"])
            check_type(argname="argument schedule_offset", value=schedule_offset, expected_type=type_hints["schedule_offset"])
            check_type(argname="argument schedule_start_time", value=schedule_start_time, expected_type=type_hints["schedule_start_time"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
        self._values: typing.Dict[str, typing.Any] = {
            "schedule_expression": schedule_expression,
        }
        if data_pull_mode is not None:
            self._values["data_pull_mode"] = data_pull_mode
        if first_execution_from is not None:
            self._values["first_execution_from"] = first_execution_from
        if schedule_end_time is not None:
            self._values["schedule_end_time"] = schedule_end_time
        if schedule_offset is not None:
            self._values["schedule_offset"] = schedule_offset
        if schedule_start_time is not None:
            self._values["schedule_start_time"] = schedule_start_time
        if timezone is not None:
            self._values["timezone"] = timezone

    @builtins.property
    def schedule_expression(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_expression AppflowFlow#schedule_expression}.'''
        result = self._values.get("schedule_expression")
        assert result is not None, "Required property 'schedule_expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_pull_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#data_pull_mode AppflowFlow#data_pull_mode}.'''
        result = self._values.get("data_pull_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def first_execution_from(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#first_execution_from AppflowFlow#first_execution_from}.'''
        result = self._values.get("first_execution_from")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule_end_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_end_time AppflowFlow#schedule_end_time}.'''
        result = self._values.get("schedule_end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule_offset(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_offset AppflowFlow#schedule_offset}.'''
        result = self._values.get("schedule_offset")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def schedule_start_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#schedule_start_time AppflowFlow#schedule_start_time}.'''
        result = self._values.get("schedule_start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appflow_flow#timezone AppflowFlow#timezone}.'''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppflowFlowTriggerConfigTriggerPropertiesScheduled(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppflowFlowTriggerConfigTriggerPropertiesScheduledOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.appflowFlow.AppflowFlowTriggerConfigTriggerPropertiesScheduledOutputReference",
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

    @jsii.member(jsii_name="resetDataPullMode")
    def reset_data_pull_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataPullMode", []))

    @jsii.member(jsii_name="resetFirstExecutionFrom")
    def reset_first_execution_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirstExecutionFrom", []))

    @jsii.member(jsii_name="resetScheduleEndTime")
    def reset_schedule_end_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduleEndTime", []))

    @jsii.member(jsii_name="resetScheduleOffset")
    def reset_schedule_offset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduleOffset", []))

    @jsii.member(jsii_name="resetScheduleStartTime")
    def reset_schedule_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduleStartTime", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

    @builtins.property
    @jsii.member(jsii_name="dataPullModeInput")
    def data_pull_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataPullModeInput"))

    @builtins.property
    @jsii.member(jsii_name="firstExecutionFromInput")
    def first_execution_from_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firstExecutionFromInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleEndTimeInput")
    def schedule_end_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleEndTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleExpressionInput")
    def schedule_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleOffsetInput")
    def schedule_offset_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scheduleOffsetInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleStartTimeInput")
    def schedule_start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleStartTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="dataPullMode")
    def data_pull_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataPullMode"))

    @data_pull_mode.setter
    def data_pull_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataPullMode", value)

    @builtins.property
    @jsii.member(jsii_name="firstExecutionFrom")
    def first_execution_from(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstExecutionFrom"))

    @first_execution_from.setter
    def first_execution_from(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstExecutionFrom", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleEndTime")
    def schedule_end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheduleEndTime"))

    @schedule_end_time.setter
    def schedule_end_time(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleEndTime", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleExpression")
    def schedule_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheduleExpression"))

    @schedule_expression.setter
    def schedule_expression(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleExpression", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleOffset")
    def schedule_offset(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scheduleOffset"))

    @schedule_offset.setter
    def schedule_offset(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleOffset", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleStartTime")
    def schedule_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheduleStartTime"))

    @schedule_start_time.setter
    def schedule_start_time(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timezone"))

    @timezone.setter
    def timezone(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppflowFlowTriggerConfigTriggerPropertiesScheduled]:
        return typing.cast(typing.Optional[AppflowFlowTriggerConfigTriggerPropertiesScheduled], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppflowFlowTriggerConfigTriggerPropertiesScheduled],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[AppflowFlowTriggerConfigTriggerPropertiesScheduled],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppflowFlow",
    "AppflowFlowConfig",
    "AppflowFlowDestinationFlowConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorProperties",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfilesOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetricsOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketo",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesMarketoOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshift",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3OutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoData",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendesk",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfigOutputReference",
    "AppflowFlowDestinationFlowConfigDestinationConnectorPropertiesZendeskOutputReference",
    "AppflowFlowDestinationFlowConfigList",
    "AppflowFlowDestinationFlowConfigOutputReference",
    "AppflowFlowSourceFlowConfig",
    "AppflowFlowSourceFlowConfigIncrementalPullConfig",
    "AppflowFlowSourceFlowConfigIncrementalPullConfigOutputReference",
    "AppflowFlowSourceFlowConfigOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorProperties",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitude",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesAmplitudeOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnector",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesCustomConnectorOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadog",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesDatadogOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatrace",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesDynatraceOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalyticsOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexus",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesInforNexusOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketo",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesMarketoOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3OutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfigOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforce",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSalesforceOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoData",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSapoDataOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNow",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesServiceNowOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingular",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSingularOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlack",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesSlackOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicro",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesTrendmicroOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeeva",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesVeevaOutputReference",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendesk",
    "AppflowFlowSourceFlowConfigSourceConnectorPropertiesZendeskOutputReference",
    "AppflowFlowTask",
    "AppflowFlowTaskConnectorOperator",
    "AppflowFlowTaskConnectorOperatorList",
    "AppflowFlowTaskConnectorOperatorOutputReference",
    "AppflowFlowTaskList",
    "AppflowFlowTaskOutputReference",
    "AppflowFlowTriggerConfig",
    "AppflowFlowTriggerConfigOutputReference",
    "AppflowFlowTriggerConfigTriggerProperties",
    "AppflowFlowTriggerConfigTriggerPropertiesOutputReference",
    "AppflowFlowTriggerConfigTriggerPropertiesScheduled",
    "AppflowFlowTriggerConfigTriggerPropertiesScheduledOutputReference",
]

publication.publish()
