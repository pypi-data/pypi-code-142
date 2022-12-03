'''
# `aws_sagemaker_flow_definition`

Refer to the Terraform Registory for docs: [`aws_sagemaker_flow_definition`](https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition).
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


class SagemakerFlowDefinition(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerFlowDefinition.SagemakerFlowDefinition",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition aws_sagemaker_flow_definition}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        flow_definition_name: builtins.str,
        human_loop_config: typing.Union["SagemakerFlowDefinitionHumanLoopConfig", typing.Dict[str, typing.Any]],
        output_config: typing.Union["SagemakerFlowDefinitionOutputConfig", typing.Dict[str, typing.Any]],
        role_arn: builtins.str,
        human_loop_activation_config: typing.Optional[typing.Union["SagemakerFlowDefinitionHumanLoopActivationConfig", typing.Dict[str, typing.Any]]] = None,
        human_loop_request_source: typing.Optional[typing.Union["SagemakerFlowDefinitionHumanLoopRequestSource", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition aws_sagemaker_flow_definition} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param flow_definition_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#flow_definition_name SagemakerFlowDefinition#flow_definition_name}.
        :param human_loop_config: human_loop_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#human_loop_config SagemakerFlowDefinition#human_loop_config}
        :param output_config: output_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#output_config SagemakerFlowDefinition#output_config}
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#role_arn SagemakerFlowDefinition#role_arn}.
        :param human_loop_activation_config: human_loop_activation_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#human_loop_activation_config SagemakerFlowDefinition#human_loop_activation_config}
        :param human_loop_request_source: human_loop_request_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#human_loop_request_source SagemakerFlowDefinition#human_loop_request_source}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#id SagemakerFlowDefinition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#tags SagemakerFlowDefinition#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#tags_all SagemakerFlowDefinition#tags_all}.
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
                flow_definition_name: builtins.str,
                human_loop_config: typing.Union[SagemakerFlowDefinitionHumanLoopConfig, typing.Dict[str, typing.Any]],
                output_config: typing.Union[SagemakerFlowDefinitionOutputConfig, typing.Dict[str, typing.Any]],
                role_arn: builtins.str,
                human_loop_activation_config: typing.Optional[typing.Union[SagemakerFlowDefinitionHumanLoopActivationConfig, typing.Dict[str, typing.Any]]] = None,
                human_loop_request_source: typing.Optional[typing.Union[SagemakerFlowDefinitionHumanLoopRequestSource, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
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
        config = SagemakerFlowDefinitionConfig(
            flow_definition_name=flow_definition_name,
            human_loop_config=human_loop_config,
            output_config=output_config,
            role_arn=role_arn,
            human_loop_activation_config=human_loop_activation_config,
            human_loop_request_source=human_loop_request_source,
            id=id,
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

    @jsii.member(jsii_name="putHumanLoopActivationConfig")
    def put_human_loop_activation_config(
        self,
        *,
        human_loop_activation_conditions_config: typing.Optional[typing.Union["SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param human_loop_activation_conditions_config: human_loop_activation_conditions_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#human_loop_activation_conditions_config SagemakerFlowDefinition#human_loop_activation_conditions_config}
        '''
        value = SagemakerFlowDefinitionHumanLoopActivationConfig(
            human_loop_activation_conditions_config=human_loop_activation_conditions_config,
        )

        return typing.cast(None, jsii.invoke(self, "putHumanLoopActivationConfig", [value]))

    @jsii.member(jsii_name="putHumanLoopConfig")
    def put_human_loop_config(
        self,
        *,
        human_task_ui_arn: builtins.str,
        task_count: jsii.Number,
        task_description: builtins.str,
        task_title: builtins.str,
        workteam_arn: builtins.str,
        public_workforce_task_price: typing.Optional[typing.Union["SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice", typing.Dict[str, typing.Any]]] = None,
        task_availability_lifetime_in_seconds: typing.Optional[jsii.Number] = None,
        task_keywords: typing.Optional[typing.Sequence[builtins.str]] = None,
        task_time_limit_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param human_task_ui_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#human_task_ui_arn SagemakerFlowDefinition#human_task_ui_arn}.
        :param task_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#task_count SagemakerFlowDefinition#task_count}.
        :param task_description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#task_description SagemakerFlowDefinition#task_description}.
        :param task_title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#task_title SagemakerFlowDefinition#task_title}.
        :param workteam_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#workteam_arn SagemakerFlowDefinition#workteam_arn}.
        :param public_workforce_task_price: public_workforce_task_price block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#public_workforce_task_price SagemakerFlowDefinition#public_workforce_task_price}
        :param task_availability_lifetime_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#task_availability_lifetime_in_seconds SagemakerFlowDefinition#task_availability_lifetime_in_seconds}.
        :param task_keywords: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#task_keywords SagemakerFlowDefinition#task_keywords}.
        :param task_time_limit_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#task_time_limit_in_seconds SagemakerFlowDefinition#task_time_limit_in_seconds}.
        '''
        value = SagemakerFlowDefinitionHumanLoopConfig(
            human_task_ui_arn=human_task_ui_arn,
            task_count=task_count,
            task_description=task_description,
            task_title=task_title,
            workteam_arn=workteam_arn,
            public_workforce_task_price=public_workforce_task_price,
            task_availability_lifetime_in_seconds=task_availability_lifetime_in_seconds,
            task_keywords=task_keywords,
            task_time_limit_in_seconds=task_time_limit_in_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putHumanLoopConfig", [value]))

    @jsii.member(jsii_name="putHumanLoopRequestSource")
    def put_human_loop_request_source(
        self,
        *,
        aws_managed_human_loop_request_source: builtins.str,
    ) -> None:
        '''
        :param aws_managed_human_loop_request_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#aws_managed_human_loop_request_source SagemakerFlowDefinition#aws_managed_human_loop_request_source}.
        '''
        value = SagemakerFlowDefinitionHumanLoopRequestSource(
            aws_managed_human_loop_request_source=aws_managed_human_loop_request_source
        )

        return typing.cast(None, jsii.invoke(self, "putHumanLoopRequestSource", [value]))

    @jsii.member(jsii_name="putOutputConfig")
    def put_output_config(
        self,
        *,
        s3_output_path: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_output_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#s3_output_path SagemakerFlowDefinition#s3_output_path}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#kms_key_id SagemakerFlowDefinition#kms_key_id}.
        '''
        value = SagemakerFlowDefinitionOutputConfig(
            s3_output_path=s3_output_path, kms_key_id=kms_key_id
        )

        return typing.cast(None, jsii.invoke(self, "putOutputConfig", [value]))

    @jsii.member(jsii_name="resetHumanLoopActivationConfig")
    def reset_human_loop_activation_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHumanLoopActivationConfig", []))

    @jsii.member(jsii_name="resetHumanLoopRequestSource")
    def reset_human_loop_request_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHumanLoopRequestSource", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="humanLoopActivationConfig")
    def human_loop_activation_config(
        self,
    ) -> "SagemakerFlowDefinitionHumanLoopActivationConfigOutputReference":
        return typing.cast("SagemakerFlowDefinitionHumanLoopActivationConfigOutputReference", jsii.get(self, "humanLoopActivationConfig"))

    @builtins.property
    @jsii.member(jsii_name="humanLoopConfig")
    def human_loop_config(
        self,
    ) -> "SagemakerFlowDefinitionHumanLoopConfigOutputReference":
        return typing.cast("SagemakerFlowDefinitionHumanLoopConfigOutputReference", jsii.get(self, "humanLoopConfig"))

    @builtins.property
    @jsii.member(jsii_name="humanLoopRequestSource")
    def human_loop_request_source(
        self,
    ) -> "SagemakerFlowDefinitionHumanLoopRequestSourceOutputReference":
        return typing.cast("SagemakerFlowDefinitionHumanLoopRequestSourceOutputReference", jsii.get(self, "humanLoopRequestSource"))

    @builtins.property
    @jsii.member(jsii_name="outputConfig")
    def output_config(self) -> "SagemakerFlowDefinitionOutputConfigOutputReference":
        return typing.cast("SagemakerFlowDefinitionOutputConfigOutputReference", jsii.get(self, "outputConfig"))

    @builtins.property
    @jsii.member(jsii_name="flowDefinitionNameInput")
    def flow_definition_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flowDefinitionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="humanLoopActivationConfigInput")
    def human_loop_activation_config_input(
        self,
    ) -> typing.Optional["SagemakerFlowDefinitionHumanLoopActivationConfig"]:
        return typing.cast(typing.Optional["SagemakerFlowDefinitionHumanLoopActivationConfig"], jsii.get(self, "humanLoopActivationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="humanLoopConfigInput")
    def human_loop_config_input(
        self,
    ) -> typing.Optional["SagemakerFlowDefinitionHumanLoopConfig"]:
        return typing.cast(typing.Optional["SagemakerFlowDefinitionHumanLoopConfig"], jsii.get(self, "humanLoopConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="humanLoopRequestSourceInput")
    def human_loop_request_source_input(
        self,
    ) -> typing.Optional["SagemakerFlowDefinitionHumanLoopRequestSource"]:
        return typing.cast(typing.Optional["SagemakerFlowDefinitionHumanLoopRequestSource"], jsii.get(self, "humanLoopRequestSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="outputConfigInput")
    def output_config_input(
        self,
    ) -> typing.Optional["SagemakerFlowDefinitionOutputConfig"]:
        return typing.cast(typing.Optional["SagemakerFlowDefinitionOutputConfig"], jsii.get(self, "outputConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

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
    @jsii.member(jsii_name="flowDefinitionName")
    def flow_definition_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "flowDefinitionName"))

    @flow_definition_name.setter
    def flow_definition_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowDefinitionName", value)

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
    jsii_type="@cdktf/provider-aws.sagemakerFlowDefinition.SagemakerFlowDefinitionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "flow_definition_name": "flowDefinitionName",
        "human_loop_config": "humanLoopConfig",
        "output_config": "outputConfig",
        "role_arn": "roleArn",
        "human_loop_activation_config": "humanLoopActivationConfig",
        "human_loop_request_source": "humanLoopRequestSource",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class SagemakerFlowDefinitionConfig(cdktf.TerraformMetaArguments):
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
        flow_definition_name: builtins.str,
        human_loop_config: typing.Union["SagemakerFlowDefinitionHumanLoopConfig", typing.Dict[str, typing.Any]],
        output_config: typing.Union["SagemakerFlowDefinitionOutputConfig", typing.Dict[str, typing.Any]],
        role_arn: builtins.str,
        human_loop_activation_config: typing.Optional[typing.Union["SagemakerFlowDefinitionHumanLoopActivationConfig", typing.Dict[str, typing.Any]]] = None,
        human_loop_request_source: typing.Optional[typing.Union["SagemakerFlowDefinitionHumanLoopRequestSource", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
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
        :param flow_definition_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#flow_definition_name SagemakerFlowDefinition#flow_definition_name}.
        :param human_loop_config: human_loop_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#human_loop_config SagemakerFlowDefinition#human_loop_config}
        :param output_config: output_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#output_config SagemakerFlowDefinition#output_config}
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#role_arn SagemakerFlowDefinition#role_arn}.
        :param human_loop_activation_config: human_loop_activation_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#human_loop_activation_config SagemakerFlowDefinition#human_loop_activation_config}
        :param human_loop_request_source: human_loop_request_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#human_loop_request_source SagemakerFlowDefinition#human_loop_request_source}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#id SagemakerFlowDefinition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#tags SagemakerFlowDefinition#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#tags_all SagemakerFlowDefinition#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(human_loop_config, dict):
            human_loop_config = SagemakerFlowDefinitionHumanLoopConfig(**human_loop_config)
        if isinstance(output_config, dict):
            output_config = SagemakerFlowDefinitionOutputConfig(**output_config)
        if isinstance(human_loop_activation_config, dict):
            human_loop_activation_config = SagemakerFlowDefinitionHumanLoopActivationConfig(**human_loop_activation_config)
        if isinstance(human_loop_request_source, dict):
            human_loop_request_source = SagemakerFlowDefinitionHumanLoopRequestSource(**human_loop_request_source)
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
                flow_definition_name: builtins.str,
                human_loop_config: typing.Union[SagemakerFlowDefinitionHumanLoopConfig, typing.Dict[str, typing.Any]],
                output_config: typing.Union[SagemakerFlowDefinitionOutputConfig, typing.Dict[str, typing.Any]],
                role_arn: builtins.str,
                human_loop_activation_config: typing.Optional[typing.Union[SagemakerFlowDefinitionHumanLoopActivationConfig, typing.Dict[str, typing.Any]]] = None,
                human_loop_request_source: typing.Optional[typing.Union[SagemakerFlowDefinitionHumanLoopRequestSource, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument flow_definition_name", value=flow_definition_name, expected_type=type_hints["flow_definition_name"])
            check_type(argname="argument human_loop_config", value=human_loop_config, expected_type=type_hints["human_loop_config"])
            check_type(argname="argument output_config", value=output_config, expected_type=type_hints["output_config"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument human_loop_activation_config", value=human_loop_activation_config, expected_type=type_hints["human_loop_activation_config"])
            check_type(argname="argument human_loop_request_source", value=human_loop_request_source, expected_type=type_hints["human_loop_request_source"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "flow_definition_name": flow_definition_name,
            "human_loop_config": human_loop_config,
            "output_config": output_config,
            "role_arn": role_arn,
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
        if human_loop_activation_config is not None:
            self._values["human_loop_activation_config"] = human_loop_activation_config
        if human_loop_request_source is not None:
            self._values["human_loop_request_source"] = human_loop_request_source
        if id is not None:
            self._values["id"] = id
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
    def flow_definition_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#flow_definition_name SagemakerFlowDefinition#flow_definition_name}.'''
        result = self._values.get("flow_definition_name")
        assert result is not None, "Required property 'flow_definition_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def human_loop_config(self) -> "SagemakerFlowDefinitionHumanLoopConfig":
        '''human_loop_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#human_loop_config SagemakerFlowDefinition#human_loop_config}
        '''
        result = self._values.get("human_loop_config")
        assert result is not None, "Required property 'human_loop_config' is missing"
        return typing.cast("SagemakerFlowDefinitionHumanLoopConfig", result)

    @builtins.property
    def output_config(self) -> "SagemakerFlowDefinitionOutputConfig":
        '''output_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#output_config SagemakerFlowDefinition#output_config}
        '''
        result = self._values.get("output_config")
        assert result is not None, "Required property 'output_config' is missing"
        return typing.cast("SagemakerFlowDefinitionOutputConfig", result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#role_arn SagemakerFlowDefinition#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def human_loop_activation_config(
        self,
    ) -> typing.Optional["SagemakerFlowDefinitionHumanLoopActivationConfig"]:
        '''human_loop_activation_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#human_loop_activation_config SagemakerFlowDefinition#human_loop_activation_config}
        '''
        result = self._values.get("human_loop_activation_config")
        return typing.cast(typing.Optional["SagemakerFlowDefinitionHumanLoopActivationConfig"], result)

    @builtins.property
    def human_loop_request_source(
        self,
    ) -> typing.Optional["SagemakerFlowDefinitionHumanLoopRequestSource"]:
        '''human_loop_request_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#human_loop_request_source SagemakerFlowDefinition#human_loop_request_source}
        '''
        result = self._values.get("human_loop_request_source")
        return typing.cast(typing.Optional["SagemakerFlowDefinitionHumanLoopRequestSource"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#id SagemakerFlowDefinition#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#tags SagemakerFlowDefinition#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#tags_all SagemakerFlowDefinition#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerFlowDefinitionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerFlowDefinition.SagemakerFlowDefinitionHumanLoopActivationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "human_loop_activation_conditions_config": "humanLoopActivationConditionsConfig",
    },
)
class SagemakerFlowDefinitionHumanLoopActivationConfig:
    def __init__(
        self,
        *,
        human_loop_activation_conditions_config: typing.Optional[typing.Union["SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param human_loop_activation_conditions_config: human_loop_activation_conditions_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#human_loop_activation_conditions_config SagemakerFlowDefinition#human_loop_activation_conditions_config}
        '''
        if isinstance(human_loop_activation_conditions_config, dict):
            human_loop_activation_conditions_config = SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig(**human_loop_activation_conditions_config)
        if __debug__:
            def stub(
                *,
                human_loop_activation_conditions_config: typing.Optional[typing.Union[SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument human_loop_activation_conditions_config", value=human_loop_activation_conditions_config, expected_type=type_hints["human_loop_activation_conditions_config"])
        self._values: typing.Dict[str, typing.Any] = {}
        if human_loop_activation_conditions_config is not None:
            self._values["human_loop_activation_conditions_config"] = human_loop_activation_conditions_config

    @builtins.property
    def human_loop_activation_conditions_config(
        self,
    ) -> typing.Optional["SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig"]:
        '''human_loop_activation_conditions_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#human_loop_activation_conditions_config SagemakerFlowDefinition#human_loop_activation_conditions_config}
        '''
        result = self._values.get("human_loop_activation_conditions_config")
        return typing.cast(typing.Optional["SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerFlowDefinitionHumanLoopActivationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerFlowDefinition.SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig",
    jsii_struct_bases=[],
    name_mapping={"human_loop_activation_conditions": "humanLoopActivationConditions"},
)
class SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig:
    def __init__(self, *, human_loop_activation_conditions: builtins.str) -> None:
        '''
        :param human_loop_activation_conditions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#human_loop_activation_conditions SagemakerFlowDefinition#human_loop_activation_conditions}.
        '''
        if __debug__:
            def stub(*, human_loop_activation_conditions: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument human_loop_activation_conditions", value=human_loop_activation_conditions, expected_type=type_hints["human_loop_activation_conditions"])
        self._values: typing.Dict[str, typing.Any] = {
            "human_loop_activation_conditions": human_loop_activation_conditions,
        }

    @builtins.property
    def human_loop_activation_conditions(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#human_loop_activation_conditions SagemakerFlowDefinition#human_loop_activation_conditions}.'''
        result = self._values.get("human_loop_activation_conditions")
        assert result is not None, "Required property 'human_loop_activation_conditions' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerFlowDefinition.SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfigOutputReference",
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
    @jsii.member(jsii_name="humanLoopActivationConditionsInput")
    def human_loop_activation_conditions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "humanLoopActivationConditionsInput"))

    @builtins.property
    @jsii.member(jsii_name="humanLoopActivationConditions")
    def human_loop_activation_conditions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "humanLoopActivationConditions"))

    @human_loop_activation_conditions.setter
    def human_loop_activation_conditions(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "humanLoopActivationConditions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig]:
        return typing.cast(typing.Optional[SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerFlowDefinitionHumanLoopActivationConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerFlowDefinition.SagemakerFlowDefinitionHumanLoopActivationConfigOutputReference",
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

    @jsii.member(jsii_name="putHumanLoopActivationConditionsConfig")
    def put_human_loop_activation_conditions_config(
        self,
        *,
        human_loop_activation_conditions: builtins.str,
    ) -> None:
        '''
        :param human_loop_activation_conditions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#human_loop_activation_conditions SagemakerFlowDefinition#human_loop_activation_conditions}.
        '''
        value = SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig(
            human_loop_activation_conditions=human_loop_activation_conditions
        )

        return typing.cast(None, jsii.invoke(self, "putHumanLoopActivationConditionsConfig", [value]))

    @jsii.member(jsii_name="resetHumanLoopActivationConditionsConfig")
    def reset_human_loop_activation_conditions_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHumanLoopActivationConditionsConfig", []))

    @builtins.property
    @jsii.member(jsii_name="humanLoopActivationConditionsConfig")
    def human_loop_activation_conditions_config(
        self,
    ) -> SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfigOutputReference:
        return typing.cast(SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfigOutputReference, jsii.get(self, "humanLoopActivationConditionsConfig"))

    @builtins.property
    @jsii.member(jsii_name="humanLoopActivationConditionsConfigInput")
    def human_loop_activation_conditions_config_input(
        self,
    ) -> typing.Optional[SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig]:
        return typing.cast(typing.Optional[SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig], jsii.get(self, "humanLoopActivationConditionsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerFlowDefinitionHumanLoopActivationConfig]:
        return typing.cast(typing.Optional[SagemakerFlowDefinitionHumanLoopActivationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerFlowDefinitionHumanLoopActivationConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[SagemakerFlowDefinitionHumanLoopActivationConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerFlowDefinition.SagemakerFlowDefinitionHumanLoopConfig",
    jsii_struct_bases=[],
    name_mapping={
        "human_task_ui_arn": "humanTaskUiArn",
        "task_count": "taskCount",
        "task_description": "taskDescription",
        "task_title": "taskTitle",
        "workteam_arn": "workteamArn",
        "public_workforce_task_price": "publicWorkforceTaskPrice",
        "task_availability_lifetime_in_seconds": "taskAvailabilityLifetimeInSeconds",
        "task_keywords": "taskKeywords",
        "task_time_limit_in_seconds": "taskTimeLimitInSeconds",
    },
)
class SagemakerFlowDefinitionHumanLoopConfig:
    def __init__(
        self,
        *,
        human_task_ui_arn: builtins.str,
        task_count: jsii.Number,
        task_description: builtins.str,
        task_title: builtins.str,
        workteam_arn: builtins.str,
        public_workforce_task_price: typing.Optional[typing.Union["SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice", typing.Dict[str, typing.Any]]] = None,
        task_availability_lifetime_in_seconds: typing.Optional[jsii.Number] = None,
        task_keywords: typing.Optional[typing.Sequence[builtins.str]] = None,
        task_time_limit_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param human_task_ui_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#human_task_ui_arn SagemakerFlowDefinition#human_task_ui_arn}.
        :param task_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#task_count SagemakerFlowDefinition#task_count}.
        :param task_description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#task_description SagemakerFlowDefinition#task_description}.
        :param task_title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#task_title SagemakerFlowDefinition#task_title}.
        :param workteam_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#workteam_arn SagemakerFlowDefinition#workteam_arn}.
        :param public_workforce_task_price: public_workforce_task_price block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#public_workforce_task_price SagemakerFlowDefinition#public_workforce_task_price}
        :param task_availability_lifetime_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#task_availability_lifetime_in_seconds SagemakerFlowDefinition#task_availability_lifetime_in_seconds}.
        :param task_keywords: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#task_keywords SagemakerFlowDefinition#task_keywords}.
        :param task_time_limit_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#task_time_limit_in_seconds SagemakerFlowDefinition#task_time_limit_in_seconds}.
        '''
        if isinstance(public_workforce_task_price, dict):
            public_workforce_task_price = SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice(**public_workforce_task_price)
        if __debug__:
            def stub(
                *,
                human_task_ui_arn: builtins.str,
                task_count: jsii.Number,
                task_description: builtins.str,
                task_title: builtins.str,
                workteam_arn: builtins.str,
                public_workforce_task_price: typing.Optional[typing.Union[SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice, typing.Dict[str, typing.Any]]] = None,
                task_availability_lifetime_in_seconds: typing.Optional[jsii.Number] = None,
                task_keywords: typing.Optional[typing.Sequence[builtins.str]] = None,
                task_time_limit_in_seconds: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument human_task_ui_arn", value=human_task_ui_arn, expected_type=type_hints["human_task_ui_arn"])
            check_type(argname="argument task_count", value=task_count, expected_type=type_hints["task_count"])
            check_type(argname="argument task_description", value=task_description, expected_type=type_hints["task_description"])
            check_type(argname="argument task_title", value=task_title, expected_type=type_hints["task_title"])
            check_type(argname="argument workteam_arn", value=workteam_arn, expected_type=type_hints["workteam_arn"])
            check_type(argname="argument public_workforce_task_price", value=public_workforce_task_price, expected_type=type_hints["public_workforce_task_price"])
            check_type(argname="argument task_availability_lifetime_in_seconds", value=task_availability_lifetime_in_seconds, expected_type=type_hints["task_availability_lifetime_in_seconds"])
            check_type(argname="argument task_keywords", value=task_keywords, expected_type=type_hints["task_keywords"])
            check_type(argname="argument task_time_limit_in_seconds", value=task_time_limit_in_seconds, expected_type=type_hints["task_time_limit_in_seconds"])
        self._values: typing.Dict[str, typing.Any] = {
            "human_task_ui_arn": human_task_ui_arn,
            "task_count": task_count,
            "task_description": task_description,
            "task_title": task_title,
            "workteam_arn": workteam_arn,
        }
        if public_workforce_task_price is not None:
            self._values["public_workforce_task_price"] = public_workforce_task_price
        if task_availability_lifetime_in_seconds is not None:
            self._values["task_availability_lifetime_in_seconds"] = task_availability_lifetime_in_seconds
        if task_keywords is not None:
            self._values["task_keywords"] = task_keywords
        if task_time_limit_in_seconds is not None:
            self._values["task_time_limit_in_seconds"] = task_time_limit_in_seconds

    @builtins.property
    def human_task_ui_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#human_task_ui_arn SagemakerFlowDefinition#human_task_ui_arn}.'''
        result = self._values.get("human_task_ui_arn")
        assert result is not None, "Required property 'human_task_ui_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def task_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#task_count SagemakerFlowDefinition#task_count}.'''
        result = self._values.get("task_count")
        assert result is not None, "Required property 'task_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def task_description(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#task_description SagemakerFlowDefinition#task_description}.'''
        result = self._values.get("task_description")
        assert result is not None, "Required property 'task_description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def task_title(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#task_title SagemakerFlowDefinition#task_title}.'''
        result = self._values.get("task_title")
        assert result is not None, "Required property 'task_title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workteam_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#workteam_arn SagemakerFlowDefinition#workteam_arn}.'''
        result = self._values.get("workteam_arn")
        assert result is not None, "Required property 'workteam_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def public_workforce_task_price(
        self,
    ) -> typing.Optional["SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice"]:
        '''public_workforce_task_price block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#public_workforce_task_price SagemakerFlowDefinition#public_workforce_task_price}
        '''
        result = self._values.get("public_workforce_task_price")
        return typing.cast(typing.Optional["SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice"], result)

    @builtins.property
    def task_availability_lifetime_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#task_availability_lifetime_in_seconds SagemakerFlowDefinition#task_availability_lifetime_in_seconds}.'''
        result = self._values.get("task_availability_lifetime_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def task_keywords(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#task_keywords SagemakerFlowDefinition#task_keywords}.'''
        result = self._values.get("task_keywords")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def task_time_limit_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#task_time_limit_in_seconds SagemakerFlowDefinition#task_time_limit_in_seconds}.'''
        result = self._values.get("task_time_limit_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerFlowDefinitionHumanLoopConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerFlowDefinitionHumanLoopConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerFlowDefinition.SagemakerFlowDefinitionHumanLoopConfigOutputReference",
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

    @jsii.member(jsii_name="putPublicWorkforceTaskPrice")
    def put_public_workforce_task_price(
        self,
        *,
        amount_in_usd: typing.Optional[typing.Union["SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param amount_in_usd: amount_in_usd block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#amount_in_usd SagemakerFlowDefinition#amount_in_usd}
        '''
        value = SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice(
            amount_in_usd=amount_in_usd
        )

        return typing.cast(None, jsii.invoke(self, "putPublicWorkforceTaskPrice", [value]))

    @jsii.member(jsii_name="resetPublicWorkforceTaskPrice")
    def reset_public_workforce_task_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicWorkforceTaskPrice", []))

    @jsii.member(jsii_name="resetTaskAvailabilityLifetimeInSeconds")
    def reset_task_availability_lifetime_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskAvailabilityLifetimeInSeconds", []))

    @jsii.member(jsii_name="resetTaskKeywords")
    def reset_task_keywords(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskKeywords", []))

    @jsii.member(jsii_name="resetTaskTimeLimitInSeconds")
    def reset_task_time_limit_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskTimeLimitInSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="publicWorkforceTaskPrice")
    def public_workforce_task_price(
        self,
    ) -> "SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceOutputReference":
        return typing.cast("SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceOutputReference", jsii.get(self, "publicWorkforceTaskPrice"))

    @builtins.property
    @jsii.member(jsii_name="humanTaskUiArnInput")
    def human_task_ui_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "humanTaskUiArnInput"))

    @builtins.property
    @jsii.member(jsii_name="publicWorkforceTaskPriceInput")
    def public_workforce_task_price_input(
        self,
    ) -> typing.Optional["SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice"]:
        return typing.cast(typing.Optional["SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice"], jsii.get(self, "publicWorkforceTaskPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="taskAvailabilityLifetimeInSecondsInput")
    def task_availability_lifetime_in_seconds_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "taskAvailabilityLifetimeInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="taskCountInput")
    def task_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "taskCountInput"))

    @builtins.property
    @jsii.member(jsii_name="taskDescriptionInput")
    def task_description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskDescriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="taskKeywordsInput")
    def task_keywords_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "taskKeywordsInput"))

    @builtins.property
    @jsii.member(jsii_name="taskTimeLimitInSecondsInput")
    def task_time_limit_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "taskTimeLimitInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="taskTitleInput")
    def task_title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskTitleInput"))

    @builtins.property
    @jsii.member(jsii_name="workteamArnInput")
    def workteam_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workteamArnInput"))

    @builtins.property
    @jsii.member(jsii_name="humanTaskUiArn")
    def human_task_ui_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "humanTaskUiArn"))

    @human_task_ui_arn.setter
    def human_task_ui_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "humanTaskUiArn", value)

    @builtins.property
    @jsii.member(jsii_name="taskAvailabilityLifetimeInSeconds")
    def task_availability_lifetime_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "taskAvailabilityLifetimeInSeconds"))

    @task_availability_lifetime_in_seconds.setter
    def task_availability_lifetime_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskAvailabilityLifetimeInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="taskCount")
    def task_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "taskCount"))

    @task_count.setter
    def task_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskCount", value)

    @builtins.property
    @jsii.member(jsii_name="taskDescription")
    def task_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskDescription"))

    @task_description.setter
    def task_description(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskDescription", value)

    @builtins.property
    @jsii.member(jsii_name="taskKeywords")
    def task_keywords(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "taskKeywords"))

    @task_keywords.setter
    def task_keywords(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskKeywords", value)

    @builtins.property
    @jsii.member(jsii_name="taskTimeLimitInSeconds")
    def task_time_limit_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "taskTimeLimitInSeconds"))

    @task_time_limit_in_seconds.setter
    def task_time_limit_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskTimeLimitInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="taskTitle")
    def task_title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskTitle"))

    @task_title.setter
    def task_title(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskTitle", value)

    @builtins.property
    @jsii.member(jsii_name="workteamArn")
    def workteam_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workteamArn"))

    @workteam_arn.setter
    def workteam_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workteamArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SagemakerFlowDefinitionHumanLoopConfig]:
        return typing.cast(typing.Optional[SagemakerFlowDefinitionHumanLoopConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerFlowDefinitionHumanLoopConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[SagemakerFlowDefinitionHumanLoopConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerFlowDefinition.SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice",
    jsii_struct_bases=[],
    name_mapping={"amount_in_usd": "amountInUsd"},
)
class SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice:
    def __init__(
        self,
        *,
        amount_in_usd: typing.Optional[typing.Union["SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param amount_in_usd: amount_in_usd block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#amount_in_usd SagemakerFlowDefinition#amount_in_usd}
        '''
        if isinstance(amount_in_usd, dict):
            amount_in_usd = SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd(**amount_in_usd)
        if __debug__:
            def stub(
                *,
                amount_in_usd: typing.Optional[typing.Union[SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument amount_in_usd", value=amount_in_usd, expected_type=type_hints["amount_in_usd"])
        self._values: typing.Dict[str, typing.Any] = {}
        if amount_in_usd is not None:
            self._values["amount_in_usd"] = amount_in_usd

    @builtins.property
    def amount_in_usd(
        self,
    ) -> typing.Optional["SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd"]:
        '''amount_in_usd block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#amount_in_usd SagemakerFlowDefinition#amount_in_usd}
        '''
        result = self._values.get("amount_in_usd")
        return typing.cast(typing.Optional["SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerFlowDefinition.SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd",
    jsii_struct_bases=[],
    name_mapping={
        "cents": "cents",
        "dollars": "dollars",
        "tenth_fractions_of_a_cent": "tenthFractionsOfACent",
    },
)
class SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd:
    def __init__(
        self,
        *,
        cents: typing.Optional[jsii.Number] = None,
        dollars: typing.Optional[jsii.Number] = None,
        tenth_fractions_of_a_cent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cents: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#cents SagemakerFlowDefinition#cents}.
        :param dollars: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#dollars SagemakerFlowDefinition#dollars}.
        :param tenth_fractions_of_a_cent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#tenth_fractions_of_a_cent SagemakerFlowDefinition#tenth_fractions_of_a_cent}.
        '''
        if __debug__:
            def stub(
                *,
                cents: typing.Optional[jsii.Number] = None,
                dollars: typing.Optional[jsii.Number] = None,
                tenth_fractions_of_a_cent: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cents", value=cents, expected_type=type_hints["cents"])
            check_type(argname="argument dollars", value=dollars, expected_type=type_hints["dollars"])
            check_type(argname="argument tenth_fractions_of_a_cent", value=tenth_fractions_of_a_cent, expected_type=type_hints["tenth_fractions_of_a_cent"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cents is not None:
            self._values["cents"] = cents
        if dollars is not None:
            self._values["dollars"] = dollars
        if tenth_fractions_of_a_cent is not None:
            self._values["tenth_fractions_of_a_cent"] = tenth_fractions_of_a_cent

    @builtins.property
    def cents(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#cents SagemakerFlowDefinition#cents}.'''
        result = self._values.get("cents")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dollars(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#dollars SagemakerFlowDefinition#dollars}.'''
        result = self._values.get("dollars")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tenth_fractions_of_a_cent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#tenth_fractions_of_a_cent SagemakerFlowDefinition#tenth_fractions_of_a_cent}.'''
        result = self._values.get("tenth_fractions_of_a_cent")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerFlowDefinition.SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdOutputReference",
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

    @jsii.member(jsii_name="resetCents")
    def reset_cents(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCents", []))

    @jsii.member(jsii_name="resetDollars")
    def reset_dollars(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDollars", []))

    @jsii.member(jsii_name="resetTenthFractionsOfACent")
    def reset_tenth_fractions_of_a_cent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenthFractionsOfACent", []))

    @builtins.property
    @jsii.member(jsii_name="centsInput")
    def cents_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "centsInput"))

    @builtins.property
    @jsii.member(jsii_name="dollarsInput")
    def dollars_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dollarsInput"))

    @builtins.property
    @jsii.member(jsii_name="tenthFractionsOfACentInput")
    def tenth_fractions_of_a_cent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tenthFractionsOfACentInput"))

    @builtins.property
    @jsii.member(jsii_name="cents")
    def cents(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cents"))

    @cents.setter
    def cents(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cents", value)

    @builtins.property
    @jsii.member(jsii_name="dollars")
    def dollars(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dollars"))

    @dollars.setter
    def dollars(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dollars", value)

    @builtins.property
    @jsii.member(jsii_name="tenthFractionsOfACent")
    def tenth_fractions_of_a_cent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tenthFractionsOfACent"))

    @tenth_fractions_of_a_cent.setter
    def tenth_fractions_of_a_cent(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenthFractionsOfACent", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd]:
        return typing.cast(typing.Optional[SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerFlowDefinition.SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceOutputReference",
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

    @jsii.member(jsii_name="putAmountInUsd")
    def put_amount_in_usd(
        self,
        *,
        cents: typing.Optional[jsii.Number] = None,
        dollars: typing.Optional[jsii.Number] = None,
        tenth_fractions_of_a_cent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cents: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#cents SagemakerFlowDefinition#cents}.
        :param dollars: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#dollars SagemakerFlowDefinition#dollars}.
        :param tenth_fractions_of_a_cent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#tenth_fractions_of_a_cent SagemakerFlowDefinition#tenth_fractions_of_a_cent}.
        '''
        value = SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd(
            cents=cents,
            dollars=dollars,
            tenth_fractions_of_a_cent=tenth_fractions_of_a_cent,
        )

        return typing.cast(None, jsii.invoke(self, "putAmountInUsd", [value]))

    @jsii.member(jsii_name="resetAmountInUsd")
    def reset_amount_in_usd(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAmountInUsd", []))

    @builtins.property
    @jsii.member(jsii_name="amountInUsd")
    def amount_in_usd(
        self,
    ) -> SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdOutputReference:
        return typing.cast(SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdOutputReference, jsii.get(self, "amountInUsd"))

    @builtins.property
    @jsii.member(jsii_name="amountInUsdInput")
    def amount_in_usd_input(
        self,
    ) -> typing.Optional[SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd]:
        return typing.cast(typing.Optional[SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd], jsii.get(self, "amountInUsdInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice]:
        return typing.cast(typing.Optional[SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerFlowDefinition.SagemakerFlowDefinitionHumanLoopRequestSource",
    jsii_struct_bases=[],
    name_mapping={
        "aws_managed_human_loop_request_source": "awsManagedHumanLoopRequestSource",
    },
)
class SagemakerFlowDefinitionHumanLoopRequestSource:
    def __init__(self, *, aws_managed_human_loop_request_source: builtins.str) -> None:
        '''
        :param aws_managed_human_loop_request_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#aws_managed_human_loop_request_source SagemakerFlowDefinition#aws_managed_human_loop_request_source}.
        '''
        if __debug__:
            def stub(*, aws_managed_human_loop_request_source: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument aws_managed_human_loop_request_source", value=aws_managed_human_loop_request_source, expected_type=type_hints["aws_managed_human_loop_request_source"])
        self._values: typing.Dict[str, typing.Any] = {
            "aws_managed_human_loop_request_source": aws_managed_human_loop_request_source,
        }

    @builtins.property
    def aws_managed_human_loop_request_source(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#aws_managed_human_loop_request_source SagemakerFlowDefinition#aws_managed_human_loop_request_source}.'''
        result = self._values.get("aws_managed_human_loop_request_source")
        assert result is not None, "Required property 'aws_managed_human_loop_request_source' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerFlowDefinitionHumanLoopRequestSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerFlowDefinitionHumanLoopRequestSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerFlowDefinition.SagemakerFlowDefinitionHumanLoopRequestSourceOutputReference",
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
    @jsii.member(jsii_name="awsManagedHumanLoopRequestSourceInput")
    def aws_managed_human_loop_request_source_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsManagedHumanLoopRequestSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="awsManagedHumanLoopRequestSource")
    def aws_managed_human_loop_request_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsManagedHumanLoopRequestSource"))

    @aws_managed_human_loop_request_source.setter
    def aws_managed_human_loop_request_source(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsManagedHumanLoopRequestSource", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerFlowDefinitionHumanLoopRequestSource]:
        return typing.cast(typing.Optional[SagemakerFlowDefinitionHumanLoopRequestSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerFlowDefinitionHumanLoopRequestSource],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[SagemakerFlowDefinitionHumanLoopRequestSource],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.sagemakerFlowDefinition.SagemakerFlowDefinitionOutputConfig",
    jsii_struct_bases=[],
    name_mapping={"s3_output_path": "s3OutputPath", "kms_key_id": "kmsKeyId"},
)
class SagemakerFlowDefinitionOutputConfig:
    def __init__(
        self,
        *,
        s3_output_path: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_output_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#s3_output_path SagemakerFlowDefinition#s3_output_path}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#kms_key_id SagemakerFlowDefinition#kms_key_id}.
        '''
        if __debug__:
            def stub(
                *,
                s3_output_path: builtins.str,
                kms_key_id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument s3_output_path", value=s3_output_path, expected_type=type_hints["s3_output_path"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "s3_output_path": s3_output_path,
        }
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id

    @builtins.property
    def s3_output_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#s3_output_path SagemakerFlowDefinition#s3_output_path}.'''
        result = self._values.get("s3_output_path")
        assert result is not None, "Required property 's3_output_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_flow_definition#kms_key_id SagemakerFlowDefinition#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerFlowDefinitionOutputConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerFlowDefinitionOutputConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.sagemakerFlowDefinition.SagemakerFlowDefinitionOutputConfigOutputReference",
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

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="s3OutputPathInput")
    def s3_output_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3OutputPathInput"))

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
    @jsii.member(jsii_name="s3OutputPath")
    def s3_output_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3OutputPath"))

    @s3_output_path.setter
    def s3_output_path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3OutputPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SagemakerFlowDefinitionOutputConfig]:
        return typing.cast(typing.Optional[SagemakerFlowDefinitionOutputConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerFlowDefinitionOutputConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[SagemakerFlowDefinitionOutputConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SagemakerFlowDefinition",
    "SagemakerFlowDefinitionConfig",
    "SagemakerFlowDefinitionHumanLoopActivationConfig",
    "SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfig",
    "SagemakerFlowDefinitionHumanLoopActivationConfigHumanLoopActivationConditionsConfigOutputReference",
    "SagemakerFlowDefinitionHumanLoopActivationConfigOutputReference",
    "SagemakerFlowDefinitionHumanLoopConfig",
    "SagemakerFlowDefinitionHumanLoopConfigOutputReference",
    "SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPrice",
    "SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsd",
    "SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceAmountInUsdOutputReference",
    "SagemakerFlowDefinitionHumanLoopConfigPublicWorkforceTaskPriceOutputReference",
    "SagemakerFlowDefinitionHumanLoopRequestSource",
    "SagemakerFlowDefinitionHumanLoopRequestSourceOutputReference",
    "SagemakerFlowDefinitionOutputConfig",
    "SagemakerFlowDefinitionOutputConfigOutputReference",
]

publication.publish()
