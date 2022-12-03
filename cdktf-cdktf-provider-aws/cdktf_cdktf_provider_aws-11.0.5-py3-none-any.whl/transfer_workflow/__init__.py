'''
# `aws_transfer_workflow`

Refer to the Terraform Registory for docs: [`aws_transfer_workflow`](https://www.terraform.io/docs/providers/aws/r/transfer_workflow).
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


class TransferWorkflow(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflow",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow aws_transfer_workflow}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        steps: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TransferWorkflowSteps", typing.Dict[str, typing.Any]]]],
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        on_exception_steps: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TransferWorkflowOnExceptionSteps", typing.Dict[str, typing.Any]]]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow aws_transfer_workflow} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param steps: steps block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#steps TransferWorkflow#steps}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#description TransferWorkflow#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#id TransferWorkflow#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param on_exception_steps: on_exception_steps block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#on_exception_steps TransferWorkflow#on_exception_steps}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags TransferWorkflow#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags_all TransferWorkflow#tags_all}.
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
                steps: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[TransferWorkflowSteps, typing.Dict[str, typing.Any]]]],
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                on_exception_steps: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[TransferWorkflowOnExceptionSteps, typing.Dict[str, typing.Any]]]]] = None,
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
        config = TransferWorkflowConfig(
            steps=steps,
            description=description,
            id=id,
            on_exception_steps=on_exception_steps,
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

    @jsii.member(jsii_name="putOnExceptionSteps")
    def put_on_exception_steps(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TransferWorkflowOnExceptionSteps", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[TransferWorkflowOnExceptionSteps, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOnExceptionSteps", [value]))

    @jsii.member(jsii_name="putSteps")
    def put_steps(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TransferWorkflowSteps", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[TransferWorkflowSteps, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSteps", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOnExceptionSteps")
    def reset_on_exception_steps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnExceptionSteps", []))

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
    @jsii.member(jsii_name="onExceptionSteps")
    def on_exception_steps(self) -> "TransferWorkflowOnExceptionStepsList":
        return typing.cast("TransferWorkflowOnExceptionStepsList", jsii.get(self, "onExceptionSteps"))

    @builtins.property
    @jsii.member(jsii_name="steps")
    def steps(self) -> "TransferWorkflowStepsList":
        return typing.cast("TransferWorkflowStepsList", jsii.get(self, "steps"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="onExceptionStepsInput")
    def on_exception_steps_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TransferWorkflowOnExceptionSteps"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TransferWorkflowOnExceptionSteps"]]], jsii.get(self, "onExceptionStepsInput"))

    @builtins.property
    @jsii.member(jsii_name="stepsInput")
    def steps_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TransferWorkflowSteps"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TransferWorkflowSteps"]]], jsii.get(self, "stepsInput"))

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
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "steps": "steps",
        "description": "description",
        "id": "id",
        "on_exception_steps": "onExceptionSteps",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class TransferWorkflowConfig(cdktf.TerraformMetaArguments):
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
        steps: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TransferWorkflowSteps", typing.Dict[str, typing.Any]]]],
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        on_exception_steps: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TransferWorkflowOnExceptionSteps", typing.Dict[str, typing.Any]]]]] = None,
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
        :param steps: steps block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#steps TransferWorkflow#steps}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#description TransferWorkflow#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#id TransferWorkflow#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param on_exception_steps: on_exception_steps block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#on_exception_steps TransferWorkflow#on_exception_steps}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags TransferWorkflow#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags_all TransferWorkflow#tags_all}.
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
                steps: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[TransferWorkflowSteps, typing.Dict[str, typing.Any]]]],
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                on_exception_steps: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[TransferWorkflowOnExceptionSteps, typing.Dict[str, typing.Any]]]]] = None,
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
            check_type(argname="argument steps", value=steps, expected_type=type_hints["steps"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument on_exception_steps", value=on_exception_steps, expected_type=type_hints["on_exception_steps"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[str, typing.Any] = {
            "steps": steps,
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
        if on_exception_steps is not None:
            self._values["on_exception_steps"] = on_exception_steps
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
    def steps(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["TransferWorkflowSteps"]]:
        '''steps block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#steps TransferWorkflow#steps}
        '''
        result = self._values.get("steps")
        assert result is not None, "Required property 'steps' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["TransferWorkflowSteps"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#description TransferWorkflow#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#id TransferWorkflow#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_exception_steps(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TransferWorkflowOnExceptionSteps"]]]:
        '''on_exception_steps block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#on_exception_steps TransferWorkflow#on_exception_steps}
        '''
        result = self._values.get("on_exception_steps")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TransferWorkflowOnExceptionSteps"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags TransferWorkflow#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags_all TransferWorkflow#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionSteps",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "copy_step_details": "copyStepDetails",
        "custom_step_details": "customStepDetails",
        "delete_step_details": "deleteStepDetails",
        "tag_step_details": "tagStepDetails",
    },
)
class TransferWorkflowOnExceptionSteps:
    def __init__(
        self,
        *,
        type: builtins.str,
        copy_step_details: typing.Optional[typing.Union["TransferWorkflowOnExceptionStepsCopyStepDetails", typing.Dict[str, typing.Any]]] = None,
        custom_step_details: typing.Optional[typing.Union["TransferWorkflowOnExceptionStepsCustomStepDetails", typing.Dict[str, typing.Any]]] = None,
        delete_step_details: typing.Optional[typing.Union["TransferWorkflowOnExceptionStepsDeleteStepDetails", typing.Dict[str, typing.Any]]] = None,
        tag_step_details: typing.Optional[typing.Union["TransferWorkflowOnExceptionStepsTagStepDetails", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#type TransferWorkflow#type}.
        :param copy_step_details: copy_step_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#copy_step_details TransferWorkflow#copy_step_details}
        :param custom_step_details: custom_step_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#custom_step_details TransferWorkflow#custom_step_details}
        :param delete_step_details: delete_step_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#delete_step_details TransferWorkflow#delete_step_details}
        :param tag_step_details: tag_step_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tag_step_details TransferWorkflow#tag_step_details}
        '''
        if isinstance(copy_step_details, dict):
            copy_step_details = TransferWorkflowOnExceptionStepsCopyStepDetails(**copy_step_details)
        if isinstance(custom_step_details, dict):
            custom_step_details = TransferWorkflowOnExceptionStepsCustomStepDetails(**custom_step_details)
        if isinstance(delete_step_details, dict):
            delete_step_details = TransferWorkflowOnExceptionStepsDeleteStepDetails(**delete_step_details)
        if isinstance(tag_step_details, dict):
            tag_step_details = TransferWorkflowOnExceptionStepsTagStepDetails(**tag_step_details)
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                copy_step_details: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsCopyStepDetails, typing.Dict[str, typing.Any]]] = None,
                custom_step_details: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsCustomStepDetails, typing.Dict[str, typing.Any]]] = None,
                delete_step_details: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsDeleteStepDetails, typing.Dict[str, typing.Any]]] = None,
                tag_step_details: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsTagStepDetails, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument copy_step_details", value=copy_step_details, expected_type=type_hints["copy_step_details"])
            check_type(argname="argument custom_step_details", value=custom_step_details, expected_type=type_hints["custom_step_details"])
            check_type(argname="argument delete_step_details", value=delete_step_details, expected_type=type_hints["delete_step_details"])
            check_type(argname="argument tag_step_details", value=tag_step_details, expected_type=type_hints["tag_step_details"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if copy_step_details is not None:
            self._values["copy_step_details"] = copy_step_details
        if custom_step_details is not None:
            self._values["custom_step_details"] = custom_step_details
        if delete_step_details is not None:
            self._values["delete_step_details"] = delete_step_details
        if tag_step_details is not None:
            self._values["tag_step_details"] = tag_step_details

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#type TransferWorkflow#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def copy_step_details(
        self,
    ) -> typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetails"]:
        '''copy_step_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#copy_step_details TransferWorkflow#copy_step_details}
        '''
        result = self._values.get("copy_step_details")
        return typing.cast(typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetails"], result)

    @builtins.property
    def custom_step_details(
        self,
    ) -> typing.Optional["TransferWorkflowOnExceptionStepsCustomStepDetails"]:
        '''custom_step_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#custom_step_details TransferWorkflow#custom_step_details}
        '''
        result = self._values.get("custom_step_details")
        return typing.cast(typing.Optional["TransferWorkflowOnExceptionStepsCustomStepDetails"], result)

    @builtins.property
    def delete_step_details(
        self,
    ) -> typing.Optional["TransferWorkflowOnExceptionStepsDeleteStepDetails"]:
        '''delete_step_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#delete_step_details TransferWorkflow#delete_step_details}
        '''
        result = self._values.get("delete_step_details")
        return typing.cast(typing.Optional["TransferWorkflowOnExceptionStepsDeleteStepDetails"], result)

    @builtins.property
    def tag_step_details(
        self,
    ) -> typing.Optional["TransferWorkflowOnExceptionStepsTagStepDetails"]:
        '''tag_step_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tag_step_details TransferWorkflow#tag_step_details}
        '''
        result = self._values.get("tag_step_details")
        return typing.cast(typing.Optional["TransferWorkflowOnExceptionStepsTagStepDetails"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowOnExceptionSteps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsCopyStepDetails",
    jsii_struct_bases=[],
    name_mapping={
        "destination_file_location": "destinationFileLocation",
        "name": "name",
        "overwrite_existing": "overwriteExisting",
        "source_file_location": "sourceFileLocation",
    },
)
class TransferWorkflowOnExceptionStepsCopyStepDetails:
    def __init__(
        self,
        *,
        destination_file_location: typing.Optional[typing.Union["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation", typing.Dict[str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        overwrite_existing: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination_file_location: destination_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#destination_file_location TransferWorkflow#destination_file_location}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param overwrite_existing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#overwrite_existing TransferWorkflow#overwrite_existing}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        '''
        if isinstance(destination_file_location, dict):
            destination_file_location = TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation(**destination_file_location)
        if __debug__:
            def stub(
                *,
                destination_file_location: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation, typing.Dict[str, typing.Any]]] = None,
                name: typing.Optional[builtins.str] = None,
                overwrite_existing: typing.Optional[builtins.str] = None,
                source_file_location: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument destination_file_location", value=destination_file_location, expected_type=type_hints["destination_file_location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument overwrite_existing", value=overwrite_existing, expected_type=type_hints["overwrite_existing"])
            check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
        self._values: typing.Dict[str, typing.Any] = {}
        if destination_file_location is not None:
            self._values["destination_file_location"] = destination_file_location
        if name is not None:
            self._values["name"] = name
        if overwrite_existing is not None:
            self._values["overwrite_existing"] = overwrite_existing
        if source_file_location is not None:
            self._values["source_file_location"] = source_file_location

    @builtins.property
    def destination_file_location(
        self,
    ) -> typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation"]:
        '''destination_file_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#destination_file_location TransferWorkflow#destination_file_location}
        '''
        result = self._values.get("destination_file_location")
        return typing.cast(typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def overwrite_existing(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#overwrite_existing TransferWorkflow#overwrite_existing}.'''
        result = self._values.get("overwrite_existing")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_file_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.'''
        result = self._values.get("source_file_location")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowOnExceptionStepsCopyStepDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation",
    jsii_struct_bases=[],
    name_mapping={
        "efs_file_location": "efsFileLocation",
        "s3_file_location": "s3FileLocation",
    },
)
class TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation:
    def __init__(
        self,
        *,
        efs_file_location: typing.Optional[typing.Union["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation", typing.Dict[str, typing.Any]]] = None,
        s3_file_location: typing.Optional[typing.Union["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param efs_file_location: efs_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#efs_file_location TransferWorkflow#efs_file_location}
        :param s3_file_location: s3_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#s3_file_location TransferWorkflow#s3_file_location}
        '''
        if isinstance(efs_file_location, dict):
            efs_file_location = TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation(**efs_file_location)
        if isinstance(s3_file_location, dict):
            s3_file_location = TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation(**s3_file_location)
        if __debug__:
            def stub(
                *,
                efs_file_location: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation, typing.Dict[str, typing.Any]]] = None,
                s3_file_location: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument efs_file_location", value=efs_file_location, expected_type=type_hints["efs_file_location"])
            check_type(argname="argument s3_file_location", value=s3_file_location, expected_type=type_hints["s3_file_location"])
        self._values: typing.Dict[str, typing.Any] = {}
        if efs_file_location is not None:
            self._values["efs_file_location"] = efs_file_location
        if s3_file_location is not None:
            self._values["s3_file_location"] = s3_file_location

    @builtins.property
    def efs_file_location(
        self,
    ) -> typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation"]:
        '''efs_file_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#efs_file_location TransferWorkflow#efs_file_location}
        '''
        result = self._values.get("efs_file_location")
        return typing.cast(typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation"], result)

    @builtins.property
    def s3_file_location(
        self,
    ) -> typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation"]:
        '''s3_file_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#s3_file_location TransferWorkflow#s3_file_location}
        '''
        result = self._values.get("s3_file_location")
        return typing.cast(typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation",
    jsii_struct_bases=[],
    name_mapping={"file_system_id": "fileSystemId", "path": "path"},
)
class TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation:
    def __init__(
        self,
        *,
        file_system_id: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#file_system_id TransferWorkflow#file_system_id}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#path TransferWorkflow#path}.
        '''
        if __debug__:
            def stub(
                *,
                file_system_id: typing.Optional[builtins.str] = None,
                path: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if file_system_id is not None:
            self._values["file_system_id"] = file_system_id
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def file_system_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#file_system_id TransferWorkflow#file_system_id}.'''
        result = self._values.get("file_system_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#path TransferWorkflow#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference",
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

    @jsii.member(jsii_name="resetFileSystemId")
    def reset_file_system_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileSystemId", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="fileSystemIdInput")
    def file_system_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemIdInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @file_system_id.setter
    def file_system_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemId", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationOutputReference",
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

    @jsii.member(jsii_name="putEfsFileLocation")
    def put_efs_file_location(
        self,
        *,
        file_system_id: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#file_system_id TransferWorkflow#file_system_id}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#path TransferWorkflow#path}.
        '''
        value = TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation(
            file_system_id=file_system_id, path=path
        )

        return typing.cast(None, jsii.invoke(self, "putEfsFileLocation", [value]))

    @jsii.member(jsii_name="putS3FileLocation")
    def put_s3_file_location(
        self,
        *,
        bucket: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#bucket TransferWorkflow#bucket}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.
        '''
        value = TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation(
            bucket=bucket, key=key
        )

        return typing.cast(None, jsii.invoke(self, "putS3FileLocation", [value]))

    @jsii.member(jsii_name="resetEfsFileLocation")
    def reset_efs_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEfsFileLocation", []))

    @jsii.member(jsii_name="resetS3FileLocation")
    def reset_s3_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3FileLocation", []))

    @builtins.property
    @jsii.member(jsii_name="efsFileLocation")
    def efs_file_location(
        self,
    ) -> TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference:
        return typing.cast(TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference, jsii.get(self, "efsFileLocation"))

    @builtins.property
    @jsii.member(jsii_name="s3FileLocation")
    def s3_file_location(
        self,
    ) -> "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference":
        return typing.cast("TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference", jsii.get(self, "s3FileLocation"))

    @builtins.property
    @jsii.member(jsii_name="efsFileLocationInput")
    def efs_file_location_input(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation], jsii.get(self, "efsFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="s3FileLocationInput")
    def s3_file_location_input(
        self,
    ) -> typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation"]:
        return typing.cast(typing.Optional["TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation"], jsii.get(self, "s3FileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "key": "key"},
)
class TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation:
    def __init__(
        self,
        *,
        bucket: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#bucket TransferWorkflow#bucket}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.
        '''
        if __debug__:
            def stub(
                *,
                bucket: typing.Optional[builtins.str] = None,
                key: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket is not None:
            self._values["bucket"] = bucket
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#bucket TransferWorkflow#bucket}.'''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference",
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

    @jsii.member(jsii_name="resetBucket")
    def reset_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucket", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowOnExceptionStepsCopyStepDetailsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsCopyStepDetailsOutputReference",
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

    @jsii.member(jsii_name="putDestinationFileLocation")
    def put_destination_file_location(
        self,
        *,
        efs_file_location: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation, typing.Dict[str, typing.Any]]] = None,
        s3_file_location: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param efs_file_location: efs_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#efs_file_location TransferWorkflow#efs_file_location}
        :param s3_file_location: s3_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#s3_file_location TransferWorkflow#s3_file_location}
        '''
        value = TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation(
            efs_file_location=efs_file_location, s3_file_location=s3_file_location
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationFileLocation", [value]))

    @jsii.member(jsii_name="resetDestinationFileLocation")
    def reset_destination_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationFileLocation", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetOverwriteExisting")
    def reset_overwrite_existing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverwriteExisting", []))

    @jsii.member(jsii_name="resetSourceFileLocation")
    def reset_source_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFileLocation", []))

    @builtins.property
    @jsii.member(jsii_name="destinationFileLocation")
    def destination_file_location(
        self,
    ) -> TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationOutputReference:
        return typing.cast(TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationOutputReference, jsii.get(self, "destinationFileLocation"))

    @builtins.property
    @jsii.member(jsii_name="destinationFileLocationInput")
    def destination_file_location_input(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation], jsii.get(self, "destinationFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="overwriteExistingInput")
    def overwrite_existing_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "overwriteExistingInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocationInput")
    def source_file_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFileLocationInput"))

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
    @jsii.member(jsii_name="overwriteExisting")
    def overwrite_existing(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "overwriteExisting"))

    @overwrite_existing.setter
    def overwrite_existing(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overwriteExisting", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocation")
    def source_file_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFileLocation"))

    @source_file_location.setter
    def source_file_location(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFileLocation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetails],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetails],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsCustomStepDetails",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "source_file_location": "sourceFileLocation",
        "target": "target",
        "timeout_seconds": "timeoutSeconds",
    },
)
class TransferWorkflowOnExceptionStepsCustomStepDetails:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#target TransferWorkflow#target}.
        :param timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#timeout_seconds TransferWorkflow#timeout_seconds}.
        '''
        if __debug__:
            def stub(
                *,
                name: typing.Optional[builtins.str] = None,
                source_file_location: typing.Optional[builtins.str] = None,
                target: typing.Optional[builtins.str] = None,
                timeout_seconds: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if source_file_location is not None:
            self._values["source_file_location"] = source_file_location
        if target is not None:
            self._values["target"] = target
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_file_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.'''
        result = self._values.get("source_file_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#target TransferWorkflow#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#timeout_seconds TransferWorkflow#timeout_seconds}.'''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowOnExceptionStepsCustomStepDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowOnExceptionStepsCustomStepDetailsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsCustomStepDetailsOutputReference",
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

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSourceFileLocation")
    def reset_source_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFileLocation", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetTimeoutSeconds")
    def reset_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocationInput")
    def source_file_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutSecondsInput")
    def timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutSecondsInput"))

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
    @jsii.member(jsii_name="sourceFileLocation")
    def source_file_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFileLocation"))

    @source_file_location.setter
    def source_file_location(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFileLocation", value)

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
    @jsii.member(jsii_name="timeoutSeconds")
    def timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutSeconds"))

    @timeout_seconds.setter
    def timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsCustomStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsCustomStepDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowOnExceptionStepsCustomStepDetails],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TransferWorkflowOnExceptionStepsCustomStepDetails],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsDeleteStepDetails",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "source_file_location": "sourceFileLocation"},
)
class TransferWorkflowOnExceptionStepsDeleteStepDetails:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        '''
        if __debug__:
            def stub(
                *,
                name: typing.Optional[builtins.str] = None,
                source_file_location: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if source_file_location is not None:
            self._values["source_file_location"] = source_file_location

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_file_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.'''
        result = self._values.get("source_file_location")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowOnExceptionStepsDeleteStepDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowOnExceptionStepsDeleteStepDetailsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsDeleteStepDetailsOutputReference",
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

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSourceFileLocation")
    def reset_source_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFileLocation", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocationInput")
    def source_file_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFileLocationInput"))

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
    @jsii.member(jsii_name="sourceFileLocation")
    def source_file_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFileLocation"))

    @source_file_location.setter
    def source_file_location(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFileLocation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsDeleteStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsDeleteStepDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowOnExceptionStepsDeleteStepDetails],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TransferWorkflowOnExceptionStepsDeleteStepDetails],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowOnExceptionStepsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsList",
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
    ) -> "TransferWorkflowOnExceptionStepsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("TransferWorkflowOnExceptionStepsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TransferWorkflowOnExceptionSteps]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TransferWorkflowOnExceptionSteps]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TransferWorkflowOnExceptionSteps]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TransferWorkflowOnExceptionSteps]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowOnExceptionStepsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsOutputReference",
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

    @jsii.member(jsii_name="putCopyStepDetails")
    def put_copy_step_details(
        self,
        *,
        destination_file_location: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation, typing.Dict[str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        overwrite_existing: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination_file_location: destination_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#destination_file_location TransferWorkflow#destination_file_location}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param overwrite_existing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#overwrite_existing TransferWorkflow#overwrite_existing}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        '''
        value = TransferWorkflowOnExceptionStepsCopyStepDetails(
            destination_file_location=destination_file_location,
            name=name,
            overwrite_existing=overwrite_existing,
            source_file_location=source_file_location,
        )

        return typing.cast(None, jsii.invoke(self, "putCopyStepDetails", [value]))

    @jsii.member(jsii_name="putCustomStepDetails")
    def put_custom_step_details(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#target TransferWorkflow#target}.
        :param timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#timeout_seconds TransferWorkflow#timeout_seconds}.
        '''
        value = TransferWorkflowOnExceptionStepsCustomStepDetails(
            name=name,
            source_file_location=source_file_location,
            target=target,
            timeout_seconds=timeout_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomStepDetails", [value]))

    @jsii.member(jsii_name="putDeleteStepDetails")
    def put_delete_step_details(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        '''
        value = TransferWorkflowOnExceptionStepsDeleteStepDetails(
            name=name, source_file_location=source_file_location
        )

        return typing.cast(None, jsii.invoke(self, "putDeleteStepDetails", [value]))

    @jsii.member(jsii_name="putTagStepDetails")
    def put_tag_step_details(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TransferWorkflowOnExceptionStepsTagStepDetailsTags", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags TransferWorkflow#tags}
        '''
        value = TransferWorkflowOnExceptionStepsTagStepDetails(
            name=name, source_file_location=source_file_location, tags=tags
        )

        return typing.cast(None, jsii.invoke(self, "putTagStepDetails", [value]))

    @jsii.member(jsii_name="resetCopyStepDetails")
    def reset_copy_step_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyStepDetails", []))

    @jsii.member(jsii_name="resetCustomStepDetails")
    def reset_custom_step_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomStepDetails", []))

    @jsii.member(jsii_name="resetDeleteStepDetails")
    def reset_delete_step_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteStepDetails", []))

    @jsii.member(jsii_name="resetTagStepDetails")
    def reset_tag_step_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagStepDetails", []))

    @builtins.property
    @jsii.member(jsii_name="copyStepDetails")
    def copy_step_details(
        self,
    ) -> TransferWorkflowOnExceptionStepsCopyStepDetailsOutputReference:
        return typing.cast(TransferWorkflowOnExceptionStepsCopyStepDetailsOutputReference, jsii.get(self, "copyStepDetails"))

    @builtins.property
    @jsii.member(jsii_name="customStepDetails")
    def custom_step_details(
        self,
    ) -> TransferWorkflowOnExceptionStepsCustomStepDetailsOutputReference:
        return typing.cast(TransferWorkflowOnExceptionStepsCustomStepDetailsOutputReference, jsii.get(self, "customStepDetails"))

    @builtins.property
    @jsii.member(jsii_name="deleteStepDetails")
    def delete_step_details(
        self,
    ) -> TransferWorkflowOnExceptionStepsDeleteStepDetailsOutputReference:
        return typing.cast(TransferWorkflowOnExceptionStepsDeleteStepDetailsOutputReference, jsii.get(self, "deleteStepDetails"))

    @builtins.property
    @jsii.member(jsii_name="tagStepDetails")
    def tag_step_details(
        self,
    ) -> "TransferWorkflowOnExceptionStepsTagStepDetailsOutputReference":
        return typing.cast("TransferWorkflowOnExceptionStepsTagStepDetailsOutputReference", jsii.get(self, "tagStepDetails"))

    @builtins.property
    @jsii.member(jsii_name="copyStepDetailsInput")
    def copy_step_details_input(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsCopyStepDetails], jsii.get(self, "copyStepDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="customStepDetailsInput")
    def custom_step_details_input(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsCustomStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsCustomStepDetails], jsii.get(self, "customStepDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteStepDetailsInput")
    def delete_step_details_input(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsDeleteStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsDeleteStepDetails], jsii.get(self, "deleteStepDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagStepDetailsInput")
    def tag_step_details_input(
        self,
    ) -> typing.Optional["TransferWorkflowOnExceptionStepsTagStepDetails"]:
        return typing.cast(typing.Optional["TransferWorkflowOnExceptionStepsTagStepDetails"], jsii.get(self, "tagStepDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

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
    ) -> typing.Optional[typing.Union[TransferWorkflowOnExceptionSteps, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[TransferWorkflowOnExceptionSteps, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[TransferWorkflowOnExceptionSteps, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[TransferWorkflowOnExceptionSteps, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsTagStepDetails",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "source_file_location": "sourceFileLocation",
        "tags": "tags",
    },
)
class TransferWorkflowOnExceptionStepsTagStepDetails:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TransferWorkflowOnExceptionStepsTagStepDetailsTags", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags TransferWorkflow#tags}
        '''
        if __debug__:
            def stub(
                *,
                name: typing.Optional[builtins.str] = None,
                source_file_location: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[TransferWorkflowOnExceptionStepsTagStepDetailsTags, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if source_file_location is not None:
            self._values["source_file_location"] = source_file_location
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_file_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.'''
        result = self._values.get("source_file_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TransferWorkflowOnExceptionStepsTagStepDetailsTags"]]]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags TransferWorkflow#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TransferWorkflowOnExceptionStepsTagStepDetailsTags"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowOnExceptionStepsTagStepDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowOnExceptionStepsTagStepDetailsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsTagStepDetailsOutputReference",
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

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TransferWorkflowOnExceptionStepsTagStepDetailsTags", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[TransferWorkflowOnExceptionStepsTagStepDetailsTags, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSourceFileLocation")
    def reset_source_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFileLocation", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "TransferWorkflowOnExceptionStepsTagStepDetailsTagsList":
        return typing.cast("TransferWorkflowOnExceptionStepsTagStepDetailsTagsList", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocationInput")
    def source_file_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TransferWorkflowOnExceptionStepsTagStepDetailsTags"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TransferWorkflowOnExceptionStepsTagStepDetailsTags"]]], jsii.get(self, "tagsInput"))

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
    @jsii.member(jsii_name="sourceFileLocation")
    def source_file_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFileLocation"))

    @source_file_location.setter
    def source_file_location(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFileLocation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowOnExceptionStepsTagStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowOnExceptionStepsTagStepDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowOnExceptionStepsTagStepDetails],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TransferWorkflowOnExceptionStepsTagStepDetails],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsTagStepDetailsTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class TransferWorkflowOnExceptionStepsTagStepDetailsTags:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#value TransferWorkflow#value}.
        '''
        if __debug__:
            def stub(*, key: builtins.str, value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#value TransferWorkflow#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowOnExceptionStepsTagStepDetailsTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowOnExceptionStepsTagStepDetailsTagsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsTagStepDetailsTagsList",
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
    ) -> "TransferWorkflowOnExceptionStepsTagStepDetailsTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("TransferWorkflowOnExceptionStepsTagStepDetailsTagsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TransferWorkflowOnExceptionStepsTagStepDetailsTags]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TransferWorkflowOnExceptionStepsTagStepDetailsTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TransferWorkflowOnExceptionStepsTagStepDetailsTags]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TransferWorkflowOnExceptionStepsTagStepDetailsTags]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowOnExceptionStepsTagStepDetailsTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowOnExceptionStepsTagStepDetailsTagsOutputReference",
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
    ) -> typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsTagStepDetailsTags, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsTagStepDetailsTags, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsTagStepDetailsTags, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[TransferWorkflowOnExceptionStepsTagStepDetailsTags, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowSteps",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "copy_step_details": "copyStepDetails",
        "custom_step_details": "customStepDetails",
        "delete_step_details": "deleteStepDetails",
        "tag_step_details": "tagStepDetails",
    },
)
class TransferWorkflowSteps:
    def __init__(
        self,
        *,
        type: builtins.str,
        copy_step_details: typing.Optional[typing.Union["TransferWorkflowStepsCopyStepDetails", typing.Dict[str, typing.Any]]] = None,
        custom_step_details: typing.Optional[typing.Union["TransferWorkflowStepsCustomStepDetails", typing.Dict[str, typing.Any]]] = None,
        delete_step_details: typing.Optional[typing.Union["TransferWorkflowStepsDeleteStepDetails", typing.Dict[str, typing.Any]]] = None,
        tag_step_details: typing.Optional[typing.Union["TransferWorkflowStepsTagStepDetails", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#type TransferWorkflow#type}.
        :param copy_step_details: copy_step_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#copy_step_details TransferWorkflow#copy_step_details}
        :param custom_step_details: custom_step_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#custom_step_details TransferWorkflow#custom_step_details}
        :param delete_step_details: delete_step_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#delete_step_details TransferWorkflow#delete_step_details}
        :param tag_step_details: tag_step_details block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tag_step_details TransferWorkflow#tag_step_details}
        '''
        if isinstance(copy_step_details, dict):
            copy_step_details = TransferWorkflowStepsCopyStepDetails(**copy_step_details)
        if isinstance(custom_step_details, dict):
            custom_step_details = TransferWorkflowStepsCustomStepDetails(**custom_step_details)
        if isinstance(delete_step_details, dict):
            delete_step_details = TransferWorkflowStepsDeleteStepDetails(**delete_step_details)
        if isinstance(tag_step_details, dict):
            tag_step_details = TransferWorkflowStepsTagStepDetails(**tag_step_details)
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                copy_step_details: typing.Optional[typing.Union[TransferWorkflowStepsCopyStepDetails, typing.Dict[str, typing.Any]]] = None,
                custom_step_details: typing.Optional[typing.Union[TransferWorkflowStepsCustomStepDetails, typing.Dict[str, typing.Any]]] = None,
                delete_step_details: typing.Optional[typing.Union[TransferWorkflowStepsDeleteStepDetails, typing.Dict[str, typing.Any]]] = None,
                tag_step_details: typing.Optional[typing.Union[TransferWorkflowStepsTagStepDetails, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument copy_step_details", value=copy_step_details, expected_type=type_hints["copy_step_details"])
            check_type(argname="argument custom_step_details", value=custom_step_details, expected_type=type_hints["custom_step_details"])
            check_type(argname="argument delete_step_details", value=delete_step_details, expected_type=type_hints["delete_step_details"])
            check_type(argname="argument tag_step_details", value=tag_step_details, expected_type=type_hints["tag_step_details"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if copy_step_details is not None:
            self._values["copy_step_details"] = copy_step_details
        if custom_step_details is not None:
            self._values["custom_step_details"] = custom_step_details
        if delete_step_details is not None:
            self._values["delete_step_details"] = delete_step_details
        if tag_step_details is not None:
            self._values["tag_step_details"] = tag_step_details

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#type TransferWorkflow#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def copy_step_details(
        self,
    ) -> typing.Optional["TransferWorkflowStepsCopyStepDetails"]:
        '''copy_step_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#copy_step_details TransferWorkflow#copy_step_details}
        '''
        result = self._values.get("copy_step_details")
        return typing.cast(typing.Optional["TransferWorkflowStepsCopyStepDetails"], result)

    @builtins.property
    def custom_step_details(
        self,
    ) -> typing.Optional["TransferWorkflowStepsCustomStepDetails"]:
        '''custom_step_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#custom_step_details TransferWorkflow#custom_step_details}
        '''
        result = self._values.get("custom_step_details")
        return typing.cast(typing.Optional["TransferWorkflowStepsCustomStepDetails"], result)

    @builtins.property
    def delete_step_details(
        self,
    ) -> typing.Optional["TransferWorkflowStepsDeleteStepDetails"]:
        '''delete_step_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#delete_step_details TransferWorkflow#delete_step_details}
        '''
        result = self._values.get("delete_step_details")
        return typing.cast(typing.Optional["TransferWorkflowStepsDeleteStepDetails"], result)

    @builtins.property
    def tag_step_details(
        self,
    ) -> typing.Optional["TransferWorkflowStepsTagStepDetails"]:
        '''tag_step_details block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tag_step_details TransferWorkflow#tag_step_details}
        '''
        result = self._values.get("tag_step_details")
        return typing.cast(typing.Optional["TransferWorkflowStepsTagStepDetails"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowSteps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsCopyStepDetails",
    jsii_struct_bases=[],
    name_mapping={
        "destination_file_location": "destinationFileLocation",
        "name": "name",
        "overwrite_existing": "overwriteExisting",
        "source_file_location": "sourceFileLocation",
    },
)
class TransferWorkflowStepsCopyStepDetails:
    def __init__(
        self,
        *,
        destination_file_location: typing.Optional[typing.Union["TransferWorkflowStepsCopyStepDetailsDestinationFileLocation", typing.Dict[str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        overwrite_existing: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination_file_location: destination_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#destination_file_location TransferWorkflow#destination_file_location}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param overwrite_existing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#overwrite_existing TransferWorkflow#overwrite_existing}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        '''
        if isinstance(destination_file_location, dict):
            destination_file_location = TransferWorkflowStepsCopyStepDetailsDestinationFileLocation(**destination_file_location)
        if __debug__:
            def stub(
                *,
                destination_file_location: typing.Optional[typing.Union[TransferWorkflowStepsCopyStepDetailsDestinationFileLocation, typing.Dict[str, typing.Any]]] = None,
                name: typing.Optional[builtins.str] = None,
                overwrite_existing: typing.Optional[builtins.str] = None,
                source_file_location: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument destination_file_location", value=destination_file_location, expected_type=type_hints["destination_file_location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument overwrite_existing", value=overwrite_existing, expected_type=type_hints["overwrite_existing"])
            check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
        self._values: typing.Dict[str, typing.Any] = {}
        if destination_file_location is not None:
            self._values["destination_file_location"] = destination_file_location
        if name is not None:
            self._values["name"] = name
        if overwrite_existing is not None:
            self._values["overwrite_existing"] = overwrite_existing
        if source_file_location is not None:
            self._values["source_file_location"] = source_file_location

    @builtins.property
    def destination_file_location(
        self,
    ) -> typing.Optional["TransferWorkflowStepsCopyStepDetailsDestinationFileLocation"]:
        '''destination_file_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#destination_file_location TransferWorkflow#destination_file_location}
        '''
        result = self._values.get("destination_file_location")
        return typing.cast(typing.Optional["TransferWorkflowStepsCopyStepDetailsDestinationFileLocation"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def overwrite_existing(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#overwrite_existing TransferWorkflow#overwrite_existing}.'''
        result = self._values.get("overwrite_existing")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_file_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.'''
        result = self._values.get("source_file_location")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowStepsCopyStepDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsCopyStepDetailsDestinationFileLocation",
    jsii_struct_bases=[],
    name_mapping={
        "efs_file_location": "efsFileLocation",
        "s3_file_location": "s3FileLocation",
    },
)
class TransferWorkflowStepsCopyStepDetailsDestinationFileLocation:
    def __init__(
        self,
        *,
        efs_file_location: typing.Optional[typing.Union["TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation", typing.Dict[str, typing.Any]]] = None,
        s3_file_location: typing.Optional[typing.Union["TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param efs_file_location: efs_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#efs_file_location TransferWorkflow#efs_file_location}
        :param s3_file_location: s3_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#s3_file_location TransferWorkflow#s3_file_location}
        '''
        if isinstance(efs_file_location, dict):
            efs_file_location = TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation(**efs_file_location)
        if isinstance(s3_file_location, dict):
            s3_file_location = TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation(**s3_file_location)
        if __debug__:
            def stub(
                *,
                efs_file_location: typing.Optional[typing.Union[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation, typing.Dict[str, typing.Any]]] = None,
                s3_file_location: typing.Optional[typing.Union[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument efs_file_location", value=efs_file_location, expected_type=type_hints["efs_file_location"])
            check_type(argname="argument s3_file_location", value=s3_file_location, expected_type=type_hints["s3_file_location"])
        self._values: typing.Dict[str, typing.Any] = {}
        if efs_file_location is not None:
            self._values["efs_file_location"] = efs_file_location
        if s3_file_location is not None:
            self._values["s3_file_location"] = s3_file_location

    @builtins.property
    def efs_file_location(
        self,
    ) -> typing.Optional["TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation"]:
        '''efs_file_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#efs_file_location TransferWorkflow#efs_file_location}
        '''
        result = self._values.get("efs_file_location")
        return typing.cast(typing.Optional["TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation"], result)

    @builtins.property
    def s3_file_location(
        self,
    ) -> typing.Optional["TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation"]:
        '''s3_file_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#s3_file_location TransferWorkflow#s3_file_location}
        '''
        result = self._values.get("s3_file_location")
        return typing.cast(typing.Optional["TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowStepsCopyStepDetailsDestinationFileLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation",
    jsii_struct_bases=[],
    name_mapping={"file_system_id": "fileSystemId", "path": "path"},
)
class TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation:
    def __init__(
        self,
        *,
        file_system_id: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#file_system_id TransferWorkflow#file_system_id}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#path TransferWorkflow#path}.
        '''
        if __debug__:
            def stub(
                *,
                file_system_id: typing.Optional[builtins.str] = None,
                path: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if file_system_id is not None:
            self._values["file_system_id"] = file_system_id
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def file_system_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#file_system_id TransferWorkflow#file_system_id}.'''
        result = self._values.get("file_system_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#path TransferWorkflow#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference",
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

    @jsii.member(jsii_name="resetFileSystemId")
    def reset_file_system_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileSystemId", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="fileSystemIdInput")
    def file_system_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemIdInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @file_system_id.setter
    def file_system_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemId", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowStepsCopyStepDetailsDestinationFileLocationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsCopyStepDetailsDestinationFileLocationOutputReference",
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

    @jsii.member(jsii_name="putEfsFileLocation")
    def put_efs_file_location(
        self,
        *,
        file_system_id: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file_system_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#file_system_id TransferWorkflow#file_system_id}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#path TransferWorkflow#path}.
        '''
        value = TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation(
            file_system_id=file_system_id, path=path
        )

        return typing.cast(None, jsii.invoke(self, "putEfsFileLocation", [value]))

    @jsii.member(jsii_name="putS3FileLocation")
    def put_s3_file_location(
        self,
        *,
        bucket: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#bucket TransferWorkflow#bucket}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.
        '''
        value = TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation(
            bucket=bucket, key=key
        )

        return typing.cast(None, jsii.invoke(self, "putS3FileLocation", [value]))

    @jsii.member(jsii_name="resetEfsFileLocation")
    def reset_efs_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEfsFileLocation", []))

    @jsii.member(jsii_name="resetS3FileLocation")
    def reset_s3_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3FileLocation", []))

    @builtins.property
    @jsii.member(jsii_name="efsFileLocation")
    def efs_file_location(
        self,
    ) -> TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference:
        return typing.cast(TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference, jsii.get(self, "efsFileLocation"))

    @builtins.property
    @jsii.member(jsii_name="s3FileLocation")
    def s3_file_location(
        self,
    ) -> "TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference":
        return typing.cast("TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference", jsii.get(self, "s3FileLocation"))

    @builtins.property
    @jsii.member(jsii_name="efsFileLocationInput")
    def efs_file_location_input(
        self,
    ) -> typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation], jsii.get(self, "efsFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="s3FileLocationInput")
    def s3_file_location_input(
        self,
    ) -> typing.Optional["TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation"]:
        return typing.cast(typing.Optional["TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation"], jsii.get(self, "s3FileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocation],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocation],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "key": "key"},
)
class TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation:
    def __init__(
        self,
        *,
        bucket: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#bucket TransferWorkflow#bucket}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.
        '''
        if __debug__:
            def stub(
                *,
                bucket: typing.Optional[builtins.str] = None,
                key: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket is not None:
            self._values["bucket"] = bucket
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#bucket TransferWorkflow#bucket}.'''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference",
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

    @jsii.member(jsii_name="resetBucket")
    def reset_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucket", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowStepsCopyStepDetailsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsCopyStepDetailsOutputReference",
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

    @jsii.member(jsii_name="putDestinationFileLocation")
    def put_destination_file_location(
        self,
        *,
        efs_file_location: typing.Optional[typing.Union[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation, typing.Dict[str, typing.Any]]] = None,
        s3_file_location: typing.Optional[typing.Union[TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param efs_file_location: efs_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#efs_file_location TransferWorkflow#efs_file_location}
        :param s3_file_location: s3_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#s3_file_location TransferWorkflow#s3_file_location}
        '''
        value = TransferWorkflowStepsCopyStepDetailsDestinationFileLocation(
            efs_file_location=efs_file_location, s3_file_location=s3_file_location
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationFileLocation", [value]))

    @jsii.member(jsii_name="resetDestinationFileLocation")
    def reset_destination_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationFileLocation", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetOverwriteExisting")
    def reset_overwrite_existing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverwriteExisting", []))

    @jsii.member(jsii_name="resetSourceFileLocation")
    def reset_source_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFileLocation", []))

    @builtins.property
    @jsii.member(jsii_name="destinationFileLocation")
    def destination_file_location(
        self,
    ) -> TransferWorkflowStepsCopyStepDetailsDestinationFileLocationOutputReference:
        return typing.cast(TransferWorkflowStepsCopyStepDetailsDestinationFileLocationOutputReference, jsii.get(self, "destinationFileLocation"))

    @builtins.property
    @jsii.member(jsii_name="destinationFileLocationInput")
    def destination_file_location_input(
        self,
    ) -> typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocation]:
        return typing.cast(typing.Optional[TransferWorkflowStepsCopyStepDetailsDestinationFileLocation], jsii.get(self, "destinationFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="overwriteExistingInput")
    def overwrite_existing_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "overwriteExistingInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocationInput")
    def source_file_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFileLocationInput"))

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
    @jsii.member(jsii_name="overwriteExisting")
    def overwrite_existing(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "overwriteExisting"))

    @overwrite_existing.setter
    def overwrite_existing(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overwriteExisting", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocation")
    def source_file_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFileLocation"))

    @source_file_location.setter
    def source_file_location(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFileLocation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TransferWorkflowStepsCopyStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowStepsCopyStepDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowStepsCopyStepDetails],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TransferWorkflowStepsCopyStepDetails],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsCustomStepDetails",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "source_file_location": "sourceFileLocation",
        "target": "target",
        "timeout_seconds": "timeoutSeconds",
    },
)
class TransferWorkflowStepsCustomStepDetails:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#target TransferWorkflow#target}.
        :param timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#timeout_seconds TransferWorkflow#timeout_seconds}.
        '''
        if __debug__:
            def stub(
                *,
                name: typing.Optional[builtins.str] = None,
                source_file_location: typing.Optional[builtins.str] = None,
                target: typing.Optional[builtins.str] = None,
                timeout_seconds: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if source_file_location is not None:
            self._values["source_file_location"] = source_file_location
        if target is not None:
            self._values["target"] = target
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_file_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.'''
        result = self._values.get("source_file_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#target TransferWorkflow#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#timeout_seconds TransferWorkflow#timeout_seconds}.'''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowStepsCustomStepDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowStepsCustomStepDetailsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsCustomStepDetailsOutputReference",
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

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSourceFileLocation")
    def reset_source_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFileLocation", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetTimeoutSeconds")
    def reset_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocationInput")
    def source_file_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutSecondsInput")
    def timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutSecondsInput"))

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
    @jsii.member(jsii_name="sourceFileLocation")
    def source_file_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFileLocation"))

    @source_file_location.setter
    def source_file_location(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFileLocation", value)

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
    @jsii.member(jsii_name="timeoutSeconds")
    def timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutSeconds"))

    @timeout_seconds.setter
    def timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TransferWorkflowStepsCustomStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowStepsCustomStepDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowStepsCustomStepDetails],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TransferWorkflowStepsCustomStepDetails],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsDeleteStepDetails",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "source_file_location": "sourceFileLocation"},
)
class TransferWorkflowStepsDeleteStepDetails:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        '''
        if __debug__:
            def stub(
                *,
                name: typing.Optional[builtins.str] = None,
                source_file_location: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if source_file_location is not None:
            self._values["source_file_location"] = source_file_location

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_file_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.'''
        result = self._values.get("source_file_location")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowStepsDeleteStepDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowStepsDeleteStepDetailsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsDeleteStepDetailsOutputReference",
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

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSourceFileLocation")
    def reset_source_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFileLocation", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocationInput")
    def source_file_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFileLocationInput"))

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
    @jsii.member(jsii_name="sourceFileLocation")
    def source_file_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFileLocation"))

    @source_file_location.setter
    def source_file_location(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFileLocation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TransferWorkflowStepsDeleteStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowStepsDeleteStepDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowStepsDeleteStepDetails],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TransferWorkflowStepsDeleteStepDetails],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowStepsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsList",
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
    def get(self, index: jsii.Number) -> "TransferWorkflowStepsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("TransferWorkflowStepsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TransferWorkflowSteps]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TransferWorkflowSteps]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TransferWorkflowSteps]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TransferWorkflowSteps]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowStepsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsOutputReference",
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

    @jsii.member(jsii_name="putCopyStepDetails")
    def put_copy_step_details(
        self,
        *,
        destination_file_location: typing.Optional[typing.Union[TransferWorkflowStepsCopyStepDetailsDestinationFileLocation, typing.Dict[str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        overwrite_existing: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination_file_location: destination_file_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#destination_file_location TransferWorkflow#destination_file_location}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param overwrite_existing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#overwrite_existing TransferWorkflow#overwrite_existing}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        '''
        value = TransferWorkflowStepsCopyStepDetails(
            destination_file_location=destination_file_location,
            name=name,
            overwrite_existing=overwrite_existing,
            source_file_location=source_file_location,
        )

        return typing.cast(None, jsii.invoke(self, "putCopyStepDetails", [value]))

    @jsii.member(jsii_name="putCustomStepDetails")
    def put_custom_step_details(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#target TransferWorkflow#target}.
        :param timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#timeout_seconds TransferWorkflow#timeout_seconds}.
        '''
        value = TransferWorkflowStepsCustomStepDetails(
            name=name,
            source_file_location=source_file_location,
            target=target,
            timeout_seconds=timeout_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomStepDetails", [value]))

    @jsii.member(jsii_name="putDeleteStepDetails")
    def put_delete_step_details(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        '''
        value = TransferWorkflowStepsDeleteStepDetails(
            name=name, source_file_location=source_file_location
        )

        return typing.cast(None, jsii.invoke(self, "putDeleteStepDetails", [value]))

    @jsii.member(jsii_name="putTagStepDetails")
    def put_tag_step_details(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TransferWorkflowStepsTagStepDetailsTags", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags TransferWorkflow#tags}
        '''
        value = TransferWorkflowStepsTagStepDetails(
            name=name, source_file_location=source_file_location, tags=tags
        )

        return typing.cast(None, jsii.invoke(self, "putTagStepDetails", [value]))

    @jsii.member(jsii_name="resetCopyStepDetails")
    def reset_copy_step_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyStepDetails", []))

    @jsii.member(jsii_name="resetCustomStepDetails")
    def reset_custom_step_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomStepDetails", []))

    @jsii.member(jsii_name="resetDeleteStepDetails")
    def reset_delete_step_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteStepDetails", []))

    @jsii.member(jsii_name="resetTagStepDetails")
    def reset_tag_step_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagStepDetails", []))

    @builtins.property
    @jsii.member(jsii_name="copyStepDetails")
    def copy_step_details(self) -> TransferWorkflowStepsCopyStepDetailsOutputReference:
        return typing.cast(TransferWorkflowStepsCopyStepDetailsOutputReference, jsii.get(self, "copyStepDetails"))

    @builtins.property
    @jsii.member(jsii_name="customStepDetails")
    def custom_step_details(
        self,
    ) -> TransferWorkflowStepsCustomStepDetailsOutputReference:
        return typing.cast(TransferWorkflowStepsCustomStepDetailsOutputReference, jsii.get(self, "customStepDetails"))

    @builtins.property
    @jsii.member(jsii_name="deleteStepDetails")
    def delete_step_details(
        self,
    ) -> TransferWorkflowStepsDeleteStepDetailsOutputReference:
        return typing.cast(TransferWorkflowStepsDeleteStepDetailsOutputReference, jsii.get(self, "deleteStepDetails"))

    @builtins.property
    @jsii.member(jsii_name="tagStepDetails")
    def tag_step_details(self) -> "TransferWorkflowStepsTagStepDetailsOutputReference":
        return typing.cast("TransferWorkflowStepsTagStepDetailsOutputReference", jsii.get(self, "tagStepDetails"))

    @builtins.property
    @jsii.member(jsii_name="copyStepDetailsInput")
    def copy_step_details_input(
        self,
    ) -> typing.Optional[TransferWorkflowStepsCopyStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowStepsCopyStepDetails], jsii.get(self, "copyStepDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="customStepDetailsInput")
    def custom_step_details_input(
        self,
    ) -> typing.Optional[TransferWorkflowStepsCustomStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowStepsCustomStepDetails], jsii.get(self, "customStepDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteStepDetailsInput")
    def delete_step_details_input(
        self,
    ) -> typing.Optional[TransferWorkflowStepsDeleteStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowStepsDeleteStepDetails], jsii.get(self, "deleteStepDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagStepDetailsInput")
    def tag_step_details_input(
        self,
    ) -> typing.Optional["TransferWorkflowStepsTagStepDetails"]:
        return typing.cast(typing.Optional["TransferWorkflowStepsTagStepDetails"], jsii.get(self, "tagStepDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

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
    ) -> typing.Optional[typing.Union[TransferWorkflowSteps, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[TransferWorkflowSteps, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[TransferWorkflowSteps, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[TransferWorkflowSteps, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsTagStepDetails",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "source_file_location": "sourceFileLocation",
        "tags": "tags",
    },
)
class TransferWorkflowStepsTagStepDetails:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        source_file_location: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TransferWorkflowStepsTagStepDetailsTags", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.
        :param source_file_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags TransferWorkflow#tags}
        '''
        if __debug__:
            def stub(
                *,
                name: typing.Optional[builtins.str] = None,
                source_file_location: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[TransferWorkflowStepsTagStepDetailsTags, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if source_file_location is not None:
            self._values["source_file_location"] = source_file_location
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#name TransferWorkflow#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_file_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#source_file_location TransferWorkflow#source_file_location}.'''
        result = self._values.get("source_file_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TransferWorkflowStepsTagStepDetailsTags"]]]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#tags TransferWorkflow#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TransferWorkflowStepsTagStepDetailsTags"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowStepsTagStepDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowStepsTagStepDetailsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsTagStepDetailsOutputReference",
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

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TransferWorkflowStepsTagStepDetailsTags", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[TransferWorkflowStepsTagStepDetailsTags, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSourceFileLocation")
    def reset_source_file_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFileLocation", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "TransferWorkflowStepsTagStepDetailsTagsList":
        return typing.cast("TransferWorkflowStepsTagStepDetailsTagsList", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFileLocationInput")
    def source_file_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFileLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TransferWorkflowStepsTagStepDetailsTags"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TransferWorkflowStepsTagStepDetailsTags"]]], jsii.get(self, "tagsInput"))

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
    @jsii.member(jsii_name="sourceFileLocation")
    def source_file_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFileLocation"))

    @source_file_location.setter
    def source_file_location(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFileLocation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TransferWorkflowStepsTagStepDetails]:
        return typing.cast(typing.Optional[TransferWorkflowStepsTagStepDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferWorkflowStepsTagStepDetails],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[TransferWorkflowStepsTagStepDetails],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsTagStepDetailsTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class TransferWorkflowStepsTagStepDetailsTags:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#value TransferWorkflow#value}.
        '''
        if __debug__:
            def stub(*, key: builtins.str, value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#key TransferWorkflow#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_workflow#value TransferWorkflow#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferWorkflowStepsTagStepDetailsTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferWorkflowStepsTagStepDetailsTagsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsTagStepDetailsTagsList",
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
    ) -> "TransferWorkflowStepsTagStepDetailsTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("TransferWorkflowStepsTagStepDetailsTagsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TransferWorkflowStepsTagStepDetailsTags]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TransferWorkflowStepsTagStepDetailsTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TransferWorkflowStepsTagStepDetailsTags]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TransferWorkflowStepsTagStepDetailsTags]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferWorkflowStepsTagStepDetailsTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.transferWorkflow.TransferWorkflowStepsTagStepDetailsTagsOutputReference",
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
    ) -> typing.Optional[typing.Union[TransferWorkflowStepsTagStepDetailsTags, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[TransferWorkflowStepsTagStepDetailsTags, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[TransferWorkflowStepsTagStepDetailsTags, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[TransferWorkflowStepsTagStepDetailsTags, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "TransferWorkflow",
    "TransferWorkflowConfig",
    "TransferWorkflowOnExceptionSteps",
    "TransferWorkflowOnExceptionStepsCopyStepDetails",
    "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocation",
    "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocation",
    "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference",
    "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationOutputReference",
    "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocation",
    "TransferWorkflowOnExceptionStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference",
    "TransferWorkflowOnExceptionStepsCopyStepDetailsOutputReference",
    "TransferWorkflowOnExceptionStepsCustomStepDetails",
    "TransferWorkflowOnExceptionStepsCustomStepDetailsOutputReference",
    "TransferWorkflowOnExceptionStepsDeleteStepDetails",
    "TransferWorkflowOnExceptionStepsDeleteStepDetailsOutputReference",
    "TransferWorkflowOnExceptionStepsList",
    "TransferWorkflowOnExceptionStepsOutputReference",
    "TransferWorkflowOnExceptionStepsTagStepDetails",
    "TransferWorkflowOnExceptionStepsTagStepDetailsOutputReference",
    "TransferWorkflowOnExceptionStepsTagStepDetailsTags",
    "TransferWorkflowOnExceptionStepsTagStepDetailsTagsList",
    "TransferWorkflowOnExceptionStepsTagStepDetailsTagsOutputReference",
    "TransferWorkflowSteps",
    "TransferWorkflowStepsCopyStepDetails",
    "TransferWorkflowStepsCopyStepDetailsDestinationFileLocation",
    "TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocation",
    "TransferWorkflowStepsCopyStepDetailsDestinationFileLocationEfsFileLocationOutputReference",
    "TransferWorkflowStepsCopyStepDetailsDestinationFileLocationOutputReference",
    "TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocation",
    "TransferWorkflowStepsCopyStepDetailsDestinationFileLocationS3FileLocationOutputReference",
    "TransferWorkflowStepsCopyStepDetailsOutputReference",
    "TransferWorkflowStepsCustomStepDetails",
    "TransferWorkflowStepsCustomStepDetailsOutputReference",
    "TransferWorkflowStepsDeleteStepDetails",
    "TransferWorkflowStepsDeleteStepDetailsOutputReference",
    "TransferWorkflowStepsList",
    "TransferWorkflowStepsOutputReference",
    "TransferWorkflowStepsTagStepDetails",
    "TransferWorkflowStepsTagStepDetailsOutputReference",
    "TransferWorkflowStepsTagStepDetailsTags",
    "TransferWorkflowStepsTagStepDetailsTagsList",
    "TransferWorkflowStepsTagStepDetailsTagsOutputReference",
]

publication.publish()
