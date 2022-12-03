'''
# `aws_cloudformation_stack_set`

Refer to the Terraform Registory for docs: [`aws_cloudformation_stack_set`](https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set).
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


class CloudformationStackSet(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudformationStackSet.CloudformationStackSet",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set aws_cloudformation_stack_set}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        administration_role_arn: typing.Optional[builtins.str] = None,
        auto_deployment: typing.Optional[typing.Union["CloudformationStackSetAutoDeployment", typing.Dict[str, typing.Any]]] = None,
        call_as: typing.Optional[builtins.str] = None,
        capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        execution_role_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        operation_preferences: typing.Optional[typing.Union["CloudformationStackSetOperationPreferences", typing.Dict[str, typing.Any]]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        permission_model: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        template_body: typing.Optional[builtins.str] = None,
        template_url: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CloudformationStackSetTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set aws_cloudformation_stack_set} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#name CloudformationStackSet#name}.
        :param administration_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#administration_role_arn CloudformationStackSet#administration_role_arn}.
        :param auto_deployment: auto_deployment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#auto_deployment CloudformationStackSet#auto_deployment}
        :param call_as: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#call_as CloudformationStackSet#call_as}.
        :param capabilities: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#capabilities CloudformationStackSet#capabilities}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#description CloudformationStackSet#description}.
        :param execution_role_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#execution_role_name CloudformationStackSet#execution_role_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#id CloudformationStackSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param operation_preferences: operation_preferences block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#operation_preferences CloudformationStackSet#operation_preferences}
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#parameters CloudformationStackSet#parameters}.
        :param permission_model: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#permission_model CloudformationStackSet#permission_model}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#tags CloudformationStackSet#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#tags_all CloudformationStackSet#tags_all}.
        :param template_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#template_body CloudformationStackSet#template_body}.
        :param template_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#template_url CloudformationStackSet#template_url}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#timeouts CloudformationStackSet#timeouts}
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
                administration_role_arn: typing.Optional[builtins.str] = None,
                auto_deployment: typing.Optional[typing.Union[CloudformationStackSetAutoDeployment, typing.Dict[str, typing.Any]]] = None,
                call_as: typing.Optional[builtins.str] = None,
                capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
                description: typing.Optional[builtins.str] = None,
                execution_role_name: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                operation_preferences: typing.Optional[typing.Union[CloudformationStackSetOperationPreferences, typing.Dict[str, typing.Any]]] = None,
                parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                permission_model: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                template_body: typing.Optional[builtins.str] = None,
                template_url: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[CloudformationStackSetTimeouts, typing.Dict[str, typing.Any]]] = None,
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
        config = CloudformationStackSetConfig(
            name=name,
            administration_role_arn=administration_role_arn,
            auto_deployment=auto_deployment,
            call_as=call_as,
            capabilities=capabilities,
            description=description,
            execution_role_name=execution_role_name,
            id=id,
            operation_preferences=operation_preferences,
            parameters=parameters,
            permission_model=permission_model,
            tags=tags,
            tags_all=tags_all,
            template_body=template_body,
            template_url=template_url,
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

    @jsii.member(jsii_name="putAutoDeployment")
    def put_auto_deployment(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        retain_stacks_on_account_removal: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#enabled CloudformationStackSet#enabled}.
        :param retain_stacks_on_account_removal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#retain_stacks_on_account_removal CloudformationStackSet#retain_stacks_on_account_removal}.
        '''
        value = CloudformationStackSetAutoDeployment(
            enabled=enabled,
            retain_stacks_on_account_removal=retain_stacks_on_account_removal,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoDeployment", [value]))

    @jsii.member(jsii_name="putOperationPreferences")
    def put_operation_preferences(
        self,
        *,
        failure_tolerance_count: typing.Optional[jsii.Number] = None,
        failure_tolerance_percentage: typing.Optional[jsii.Number] = None,
        max_concurrent_count: typing.Optional[jsii.Number] = None,
        max_concurrent_percentage: typing.Optional[jsii.Number] = None,
        region_concurrency_type: typing.Optional[builtins.str] = None,
        region_order: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param failure_tolerance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#failure_tolerance_count CloudformationStackSet#failure_tolerance_count}.
        :param failure_tolerance_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#failure_tolerance_percentage CloudformationStackSet#failure_tolerance_percentage}.
        :param max_concurrent_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#max_concurrent_count CloudformationStackSet#max_concurrent_count}.
        :param max_concurrent_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#max_concurrent_percentage CloudformationStackSet#max_concurrent_percentage}.
        :param region_concurrency_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#region_concurrency_type CloudformationStackSet#region_concurrency_type}.
        :param region_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#region_order CloudformationStackSet#region_order}.
        '''
        value = CloudformationStackSetOperationPreferences(
            failure_tolerance_count=failure_tolerance_count,
            failure_tolerance_percentage=failure_tolerance_percentage,
            max_concurrent_count=max_concurrent_count,
            max_concurrent_percentage=max_concurrent_percentage,
            region_concurrency_type=region_concurrency_type,
            region_order=region_order,
        )

        return typing.cast(None, jsii.invoke(self, "putOperationPreferences", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, update: typing.Optional[builtins.str] = None) -> None:
        '''
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#update CloudformationStackSet#update}.
        '''
        value = CloudformationStackSetTimeouts(update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAdministrationRoleArn")
    def reset_administration_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdministrationRoleArn", []))

    @jsii.member(jsii_name="resetAutoDeployment")
    def reset_auto_deployment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoDeployment", []))

    @jsii.member(jsii_name="resetCallAs")
    def reset_call_as(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCallAs", []))

    @jsii.member(jsii_name="resetCapabilities")
    def reset_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapabilities", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExecutionRoleName")
    def reset_execution_role_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutionRoleName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOperationPreferences")
    def reset_operation_preferences(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperationPreferences", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetPermissionModel")
    def reset_permission_model(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermissionModel", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTemplateBody")
    def reset_template_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplateBody", []))

    @jsii.member(jsii_name="resetTemplateUrl")
    def reset_template_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplateUrl", []))

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
    @jsii.member(jsii_name="autoDeployment")
    def auto_deployment(self) -> "CloudformationStackSetAutoDeploymentOutputReference":
        return typing.cast("CloudformationStackSetAutoDeploymentOutputReference", jsii.get(self, "autoDeployment"))

    @builtins.property
    @jsii.member(jsii_name="operationPreferences")
    def operation_preferences(
        self,
    ) -> "CloudformationStackSetOperationPreferencesOutputReference":
        return typing.cast("CloudformationStackSetOperationPreferencesOutputReference", jsii.get(self, "operationPreferences"))

    @builtins.property
    @jsii.member(jsii_name="stackSetId")
    def stack_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stackSetId"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "CloudformationStackSetTimeoutsOutputReference":
        return typing.cast("CloudformationStackSetTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="administrationRoleArnInput")
    def administration_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "administrationRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="autoDeploymentInput")
    def auto_deployment_input(
        self,
    ) -> typing.Optional["CloudformationStackSetAutoDeployment"]:
        return typing.cast(typing.Optional["CloudformationStackSetAutoDeployment"], jsii.get(self, "autoDeploymentInput"))

    @builtins.property
    @jsii.member(jsii_name="callAsInput")
    def call_as_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "callAsInput"))

    @builtins.property
    @jsii.member(jsii_name="capabilitiesInput")
    def capabilities_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "capabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleNameInput")
    def execution_role_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="operationPreferencesInput")
    def operation_preferences_input(
        self,
    ) -> typing.Optional["CloudformationStackSetOperationPreferences"]:
        return typing.cast(typing.Optional["CloudformationStackSetOperationPreferences"], jsii.get(self, "operationPreferencesInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionModelInput")
    def permission_model_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionModelInput"))

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
    @jsii.member(jsii_name="templateBodyInput")
    def template_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="templateUrlInput")
    def template_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["CloudformationStackSetTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["CloudformationStackSetTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="administrationRoleArn")
    def administration_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "administrationRoleArn"))

    @administration_role_arn.setter
    def administration_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "administrationRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="callAs")
    def call_as(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "callAs"))

    @call_as.setter
    def call_as(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "callAs", value)

    @builtins.property
    @jsii.member(jsii_name="capabilities")
    def capabilities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "capabilities"))

    @capabilities.setter
    def capabilities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capabilities", value)

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
    @jsii.member(jsii_name="executionRoleName")
    def execution_role_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionRoleName"))

    @execution_role_name.setter
    def execution_role_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleName", value)

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
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="permissionModel")
    def permission_model(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permissionModel"))

    @permission_model.setter
    def permission_model(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionModel", value)

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
    @jsii.member(jsii_name="templateBody")
    def template_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "templateBody"))

    @template_body.setter
    def template_body(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateBody", value)

    @builtins.property
    @jsii.member(jsii_name="templateUrl")
    def template_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "templateUrl"))

    @template_url.setter
    def template_url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateUrl", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudformationStackSet.CloudformationStackSetAutoDeployment",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "retain_stacks_on_account_removal": "retainStacksOnAccountRemoval",
    },
)
class CloudformationStackSetAutoDeployment:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        retain_stacks_on_account_removal: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#enabled CloudformationStackSet#enabled}.
        :param retain_stacks_on_account_removal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#retain_stacks_on_account_removal CloudformationStackSet#retain_stacks_on_account_removal}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                retain_stacks_on_account_removal: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument retain_stacks_on_account_removal", value=retain_stacks_on_account_removal, expected_type=type_hints["retain_stacks_on_account_removal"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if retain_stacks_on_account_removal is not None:
            self._values["retain_stacks_on_account_removal"] = retain_stacks_on_account_removal

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#enabled CloudformationStackSet#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def retain_stacks_on_account_removal(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#retain_stacks_on_account_removal CloudformationStackSet#retain_stacks_on_account_removal}.'''
        result = self._values.get("retain_stacks_on_account_removal")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudformationStackSetAutoDeployment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudformationStackSetAutoDeploymentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudformationStackSet.CloudformationStackSetAutoDeploymentOutputReference",
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

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetRetainStacksOnAccountRemoval")
    def reset_retain_stacks_on_account_removal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetainStacksOnAccountRemoval", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="retainStacksOnAccountRemovalInput")
    def retain_stacks_on_account_removal_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "retainStacksOnAccountRemovalInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="retainStacksOnAccountRemoval")
    def retain_stacks_on_account_removal(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "retainStacksOnAccountRemoval"))

    @retain_stacks_on_account_removal.setter
    def retain_stacks_on_account_removal(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retainStacksOnAccountRemoval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudformationStackSetAutoDeployment]:
        return typing.cast(typing.Optional[CloudformationStackSetAutoDeployment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudformationStackSetAutoDeployment],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudformationStackSetAutoDeployment],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudformationStackSet.CloudformationStackSetConfig",
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
        "administration_role_arn": "administrationRoleArn",
        "auto_deployment": "autoDeployment",
        "call_as": "callAs",
        "capabilities": "capabilities",
        "description": "description",
        "execution_role_name": "executionRoleName",
        "id": "id",
        "operation_preferences": "operationPreferences",
        "parameters": "parameters",
        "permission_model": "permissionModel",
        "tags": "tags",
        "tags_all": "tagsAll",
        "template_body": "templateBody",
        "template_url": "templateUrl",
        "timeouts": "timeouts",
    },
)
class CloudformationStackSetConfig(cdktf.TerraformMetaArguments):
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
        administration_role_arn: typing.Optional[builtins.str] = None,
        auto_deployment: typing.Optional[typing.Union[CloudformationStackSetAutoDeployment, typing.Dict[str, typing.Any]]] = None,
        call_as: typing.Optional[builtins.str] = None,
        capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        execution_role_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        operation_preferences: typing.Optional[typing.Union["CloudformationStackSetOperationPreferences", typing.Dict[str, typing.Any]]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        permission_model: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        template_body: typing.Optional[builtins.str] = None,
        template_url: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CloudformationStackSetTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#name CloudformationStackSet#name}.
        :param administration_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#administration_role_arn CloudformationStackSet#administration_role_arn}.
        :param auto_deployment: auto_deployment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#auto_deployment CloudformationStackSet#auto_deployment}
        :param call_as: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#call_as CloudformationStackSet#call_as}.
        :param capabilities: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#capabilities CloudformationStackSet#capabilities}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#description CloudformationStackSet#description}.
        :param execution_role_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#execution_role_name CloudformationStackSet#execution_role_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#id CloudformationStackSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param operation_preferences: operation_preferences block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#operation_preferences CloudformationStackSet#operation_preferences}
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#parameters CloudformationStackSet#parameters}.
        :param permission_model: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#permission_model CloudformationStackSet#permission_model}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#tags CloudformationStackSet#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#tags_all CloudformationStackSet#tags_all}.
        :param template_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#template_body CloudformationStackSet#template_body}.
        :param template_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#template_url CloudformationStackSet#template_url}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#timeouts CloudformationStackSet#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(auto_deployment, dict):
            auto_deployment = CloudformationStackSetAutoDeployment(**auto_deployment)
        if isinstance(operation_preferences, dict):
            operation_preferences = CloudformationStackSetOperationPreferences(**operation_preferences)
        if isinstance(timeouts, dict):
            timeouts = CloudformationStackSetTimeouts(**timeouts)
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
                administration_role_arn: typing.Optional[builtins.str] = None,
                auto_deployment: typing.Optional[typing.Union[CloudformationStackSetAutoDeployment, typing.Dict[str, typing.Any]]] = None,
                call_as: typing.Optional[builtins.str] = None,
                capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
                description: typing.Optional[builtins.str] = None,
                execution_role_name: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                operation_preferences: typing.Optional[typing.Union[CloudformationStackSetOperationPreferences, typing.Dict[str, typing.Any]]] = None,
                parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                permission_model: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                template_body: typing.Optional[builtins.str] = None,
                template_url: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[CloudformationStackSetTimeouts, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument administration_role_arn", value=administration_role_arn, expected_type=type_hints["administration_role_arn"])
            check_type(argname="argument auto_deployment", value=auto_deployment, expected_type=type_hints["auto_deployment"])
            check_type(argname="argument call_as", value=call_as, expected_type=type_hints["call_as"])
            check_type(argname="argument capabilities", value=capabilities, expected_type=type_hints["capabilities"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument execution_role_name", value=execution_role_name, expected_type=type_hints["execution_role_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument operation_preferences", value=operation_preferences, expected_type=type_hints["operation_preferences"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument permission_model", value=permission_model, expected_type=type_hints["permission_model"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument template_body", value=template_body, expected_type=type_hints["template_body"])
            check_type(argname="argument template_url", value=template_url, expected_type=type_hints["template_url"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
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
        if administration_role_arn is not None:
            self._values["administration_role_arn"] = administration_role_arn
        if auto_deployment is not None:
            self._values["auto_deployment"] = auto_deployment
        if call_as is not None:
            self._values["call_as"] = call_as
        if capabilities is not None:
            self._values["capabilities"] = capabilities
        if description is not None:
            self._values["description"] = description
        if execution_role_name is not None:
            self._values["execution_role_name"] = execution_role_name
        if id is not None:
            self._values["id"] = id
        if operation_preferences is not None:
            self._values["operation_preferences"] = operation_preferences
        if parameters is not None:
            self._values["parameters"] = parameters
        if permission_model is not None:
            self._values["permission_model"] = permission_model
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if template_body is not None:
            self._values["template_body"] = template_body
        if template_url is not None:
            self._values["template_url"] = template_url
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#name CloudformationStackSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def administration_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#administration_role_arn CloudformationStackSet#administration_role_arn}.'''
        result = self._values.get("administration_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_deployment(self) -> typing.Optional[CloudformationStackSetAutoDeployment]:
        '''auto_deployment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#auto_deployment CloudformationStackSet#auto_deployment}
        '''
        result = self._values.get("auto_deployment")
        return typing.cast(typing.Optional[CloudformationStackSetAutoDeployment], result)

    @builtins.property
    def call_as(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#call_as CloudformationStackSet#call_as}.'''
        result = self._values.get("call_as")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#capabilities CloudformationStackSet#capabilities}.'''
        result = self._values.get("capabilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#description CloudformationStackSet#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_role_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#execution_role_name CloudformationStackSet#execution_role_name}.'''
        result = self._values.get("execution_role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#id CloudformationStackSet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operation_preferences(
        self,
    ) -> typing.Optional["CloudformationStackSetOperationPreferences"]:
        '''operation_preferences block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#operation_preferences CloudformationStackSet#operation_preferences}
        '''
        result = self._values.get("operation_preferences")
        return typing.cast(typing.Optional["CloudformationStackSetOperationPreferences"], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#parameters CloudformationStackSet#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def permission_model(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#permission_model CloudformationStackSet#permission_model}.'''
        result = self._values.get("permission_model")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#tags CloudformationStackSet#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#tags_all CloudformationStackSet#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def template_body(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#template_body CloudformationStackSet#template_body}.'''
        result = self._values.get("template_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#template_url CloudformationStackSet#template_url}.'''
        result = self._values.get("template_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CloudformationStackSetTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#timeouts CloudformationStackSet#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CloudformationStackSetTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudformationStackSetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudformationStackSet.CloudformationStackSetOperationPreferences",
    jsii_struct_bases=[],
    name_mapping={
        "failure_tolerance_count": "failureToleranceCount",
        "failure_tolerance_percentage": "failureTolerancePercentage",
        "max_concurrent_count": "maxConcurrentCount",
        "max_concurrent_percentage": "maxConcurrentPercentage",
        "region_concurrency_type": "regionConcurrencyType",
        "region_order": "regionOrder",
    },
)
class CloudformationStackSetOperationPreferences:
    def __init__(
        self,
        *,
        failure_tolerance_count: typing.Optional[jsii.Number] = None,
        failure_tolerance_percentage: typing.Optional[jsii.Number] = None,
        max_concurrent_count: typing.Optional[jsii.Number] = None,
        max_concurrent_percentage: typing.Optional[jsii.Number] = None,
        region_concurrency_type: typing.Optional[builtins.str] = None,
        region_order: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param failure_tolerance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#failure_tolerance_count CloudformationStackSet#failure_tolerance_count}.
        :param failure_tolerance_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#failure_tolerance_percentage CloudformationStackSet#failure_tolerance_percentage}.
        :param max_concurrent_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#max_concurrent_count CloudformationStackSet#max_concurrent_count}.
        :param max_concurrent_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#max_concurrent_percentage CloudformationStackSet#max_concurrent_percentage}.
        :param region_concurrency_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#region_concurrency_type CloudformationStackSet#region_concurrency_type}.
        :param region_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#region_order CloudformationStackSet#region_order}.
        '''
        if __debug__:
            def stub(
                *,
                failure_tolerance_count: typing.Optional[jsii.Number] = None,
                failure_tolerance_percentage: typing.Optional[jsii.Number] = None,
                max_concurrent_count: typing.Optional[jsii.Number] = None,
                max_concurrent_percentage: typing.Optional[jsii.Number] = None,
                region_concurrency_type: typing.Optional[builtins.str] = None,
                region_order: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument failure_tolerance_count", value=failure_tolerance_count, expected_type=type_hints["failure_tolerance_count"])
            check_type(argname="argument failure_tolerance_percentage", value=failure_tolerance_percentage, expected_type=type_hints["failure_tolerance_percentage"])
            check_type(argname="argument max_concurrent_count", value=max_concurrent_count, expected_type=type_hints["max_concurrent_count"])
            check_type(argname="argument max_concurrent_percentage", value=max_concurrent_percentage, expected_type=type_hints["max_concurrent_percentage"])
            check_type(argname="argument region_concurrency_type", value=region_concurrency_type, expected_type=type_hints["region_concurrency_type"])
            check_type(argname="argument region_order", value=region_order, expected_type=type_hints["region_order"])
        self._values: typing.Dict[str, typing.Any] = {}
        if failure_tolerance_count is not None:
            self._values["failure_tolerance_count"] = failure_tolerance_count
        if failure_tolerance_percentage is not None:
            self._values["failure_tolerance_percentage"] = failure_tolerance_percentage
        if max_concurrent_count is not None:
            self._values["max_concurrent_count"] = max_concurrent_count
        if max_concurrent_percentage is not None:
            self._values["max_concurrent_percentage"] = max_concurrent_percentage
        if region_concurrency_type is not None:
            self._values["region_concurrency_type"] = region_concurrency_type
        if region_order is not None:
            self._values["region_order"] = region_order

    @builtins.property
    def failure_tolerance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#failure_tolerance_count CloudformationStackSet#failure_tolerance_count}.'''
        result = self._values.get("failure_tolerance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def failure_tolerance_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#failure_tolerance_percentage CloudformationStackSet#failure_tolerance_percentage}.'''
        result = self._values.get("failure_tolerance_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_concurrent_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#max_concurrent_count CloudformationStackSet#max_concurrent_count}.'''
        result = self._values.get("max_concurrent_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_concurrent_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#max_concurrent_percentage CloudformationStackSet#max_concurrent_percentage}.'''
        result = self._values.get("max_concurrent_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def region_concurrency_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#region_concurrency_type CloudformationStackSet#region_concurrency_type}.'''
        result = self._values.get("region_concurrency_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region_order(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#region_order CloudformationStackSet#region_order}.'''
        result = self._values.get("region_order")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudformationStackSetOperationPreferences(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudformationStackSetOperationPreferencesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudformationStackSet.CloudformationStackSetOperationPreferencesOutputReference",
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

    @jsii.member(jsii_name="resetFailureToleranceCount")
    def reset_failure_tolerance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailureToleranceCount", []))

    @jsii.member(jsii_name="resetFailureTolerancePercentage")
    def reset_failure_tolerance_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailureTolerancePercentage", []))

    @jsii.member(jsii_name="resetMaxConcurrentCount")
    def reset_max_concurrent_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrentCount", []))

    @jsii.member(jsii_name="resetMaxConcurrentPercentage")
    def reset_max_concurrent_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrentPercentage", []))

    @jsii.member(jsii_name="resetRegionConcurrencyType")
    def reset_region_concurrency_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegionConcurrencyType", []))

    @jsii.member(jsii_name="resetRegionOrder")
    def reset_region_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegionOrder", []))

    @builtins.property
    @jsii.member(jsii_name="failureToleranceCountInput")
    def failure_tolerance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "failureToleranceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="failureTolerancePercentageInput")
    def failure_tolerance_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "failureTolerancePercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentCountInput")
    def max_concurrent_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrentCountInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentPercentageInput")
    def max_concurrent_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrentPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="regionConcurrencyTypeInput")
    def region_concurrency_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionConcurrencyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="regionOrderInput")
    def region_order_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "regionOrderInput"))

    @builtins.property
    @jsii.member(jsii_name="failureToleranceCount")
    def failure_tolerance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "failureToleranceCount"))

    @failure_tolerance_count.setter
    def failure_tolerance_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failureToleranceCount", value)

    @builtins.property
    @jsii.member(jsii_name="failureTolerancePercentage")
    def failure_tolerance_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "failureTolerancePercentage"))

    @failure_tolerance_percentage.setter
    def failure_tolerance_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failureTolerancePercentage", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentCount")
    def max_concurrent_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrentCount"))

    @max_concurrent_count.setter
    def max_concurrent_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentCount", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentPercentage")
    def max_concurrent_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrentPercentage"))

    @max_concurrent_percentage.setter
    def max_concurrent_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="regionConcurrencyType")
    def region_concurrency_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regionConcurrencyType"))

    @region_concurrency_type.setter
    def region_concurrency_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionConcurrencyType", value)

    @builtins.property
    @jsii.member(jsii_name="regionOrder")
    def region_order(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "regionOrder"))

    @region_order.setter
    def region_order(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionOrder", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudformationStackSetOperationPreferences]:
        return typing.cast(typing.Optional[CloudformationStackSetOperationPreferences], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudformationStackSetOperationPreferences],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CloudformationStackSetOperationPreferences],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.cloudformationStackSet.CloudformationStackSetTimeouts",
    jsii_struct_bases=[],
    name_mapping={"update": "update"},
)
class CloudformationStackSetTimeouts:
    def __init__(self, *, update: typing.Optional[builtins.str] = None) -> None:
        '''
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#update CloudformationStackSet#update}.
        '''
        if __debug__:
            def stub(*, update: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set#update CloudformationStackSet#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudformationStackSetTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudformationStackSetTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.cloudformationStackSet.CloudformationStackSetTimeoutsOutputReference",
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

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

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
    ) -> typing.Optional[typing.Union[CloudformationStackSetTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudformationStackSetTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudformationStackSetTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CloudformationStackSetTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudformationStackSet",
    "CloudformationStackSetAutoDeployment",
    "CloudformationStackSetAutoDeploymentOutputReference",
    "CloudformationStackSetConfig",
    "CloudformationStackSetOperationPreferences",
    "CloudformationStackSetOperationPreferencesOutputReference",
    "CloudformationStackSetTimeouts",
    "CloudformationStackSetTimeoutsOutputReference",
]

publication.publish()
