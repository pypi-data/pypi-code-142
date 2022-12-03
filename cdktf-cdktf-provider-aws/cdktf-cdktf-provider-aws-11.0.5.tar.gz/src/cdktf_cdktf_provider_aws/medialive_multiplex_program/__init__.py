'''
# `aws_medialive_multiplex_program`

Refer to the Terraform Registory for docs: [`aws_medialive_multiplex_program`](https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program).
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


class MedialiveMultiplexProgram(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.medialiveMultiplexProgram.MedialiveMultiplexProgram",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program aws_medialive_multiplex_program}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        multiplex_id: builtins.str,
        multiplex_program_settings: typing.Union["MedialiveMultiplexProgramMultiplexProgramSettings", typing.Dict[str, typing.Any]],
        program_name: builtins.str,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program aws_medialive_multiplex_program} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param multiplex_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#multiplex_id MedialiveMultiplexProgram#multiplex_id}.
        :param multiplex_program_settings: multiplex_program_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#multiplex_program_settings MedialiveMultiplexProgram#multiplex_program_settings}
        :param program_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#program_name MedialiveMultiplexProgram#program_name}.
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
                id: builtins.str,
                *,
                multiplex_id: builtins.str,
                multiplex_program_settings: typing.Union[MedialiveMultiplexProgramMultiplexProgramSettings, typing.Dict[str, typing.Any]],
                program_name: builtins.str,
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
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = MedialiveMultiplexProgramConfig(
            multiplex_id=multiplex_id,
            multiplex_program_settings=multiplex_program_settings,
            program_name=program_name,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putMultiplexProgramSettings")
    def put_multiplex_program_settings(
        self,
        *,
        preferred_channel_pipeline: builtins.str,
        program_number: jsii.Number,
        service_descriptor: typing.Optional[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor", typing.Dict[str, typing.Any]]] = None,
        video_settings: typing.Optional[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param preferred_channel_pipeline: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#preferred_channel_pipeline MedialiveMultiplexProgram#preferred_channel_pipeline}.
        :param program_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#program_number MedialiveMultiplexProgram#program_number}.
        :param service_descriptor: service_descriptor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#service_descriptor MedialiveMultiplexProgram#service_descriptor}
        :param video_settings: video_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#video_settings MedialiveMultiplexProgram#video_settings}
        '''
        value = MedialiveMultiplexProgramMultiplexProgramSettings(
            preferred_channel_pipeline=preferred_channel_pipeline,
            program_number=program_number,
            service_descriptor=service_descriptor,
            video_settings=video_settings,
        )

        return typing.cast(None, jsii.invoke(self, "putMultiplexProgramSettings", [value]))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="multiplexProgramSettings")
    def multiplex_program_settings(
        self,
    ) -> "MedialiveMultiplexProgramMultiplexProgramSettingsOutputReference":
        return typing.cast("MedialiveMultiplexProgramMultiplexProgramSettingsOutputReference", jsii.get(self, "multiplexProgramSettings"))

    @builtins.property
    @jsii.member(jsii_name="multiplexIdInput")
    def multiplex_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "multiplexIdInput"))

    @builtins.property
    @jsii.member(jsii_name="multiplexProgramSettingsInput")
    def multiplex_program_settings_input(
        self,
    ) -> typing.Optional["MedialiveMultiplexProgramMultiplexProgramSettings"]:
        return typing.cast(typing.Optional["MedialiveMultiplexProgramMultiplexProgramSettings"], jsii.get(self, "multiplexProgramSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="programNameInput")
    def program_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "programNameInput"))

    @builtins.property
    @jsii.member(jsii_name="multiplexId")
    def multiplex_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "multiplexId"))

    @multiplex_id.setter
    def multiplex_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multiplexId", value)

    @builtins.property
    @jsii.member(jsii_name="programName")
    def program_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "programName"))

    @program_name.setter
    def program_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "programName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.medialiveMultiplexProgram.MedialiveMultiplexProgramConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "multiplex_id": "multiplexId",
        "multiplex_program_settings": "multiplexProgramSettings",
        "program_name": "programName",
    },
)
class MedialiveMultiplexProgramConfig(cdktf.TerraformMetaArguments):
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
        multiplex_id: builtins.str,
        multiplex_program_settings: typing.Union["MedialiveMultiplexProgramMultiplexProgramSettings", typing.Dict[str, typing.Any]],
        program_name: builtins.str,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param multiplex_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#multiplex_id MedialiveMultiplexProgram#multiplex_id}.
        :param multiplex_program_settings: multiplex_program_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#multiplex_program_settings MedialiveMultiplexProgram#multiplex_program_settings}
        :param program_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#program_name MedialiveMultiplexProgram#program_name}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(multiplex_program_settings, dict):
            multiplex_program_settings = MedialiveMultiplexProgramMultiplexProgramSettings(**multiplex_program_settings)
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
                multiplex_id: builtins.str,
                multiplex_program_settings: typing.Union[MedialiveMultiplexProgramMultiplexProgramSettings, typing.Dict[str, typing.Any]],
                program_name: builtins.str,
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
            check_type(argname="argument multiplex_id", value=multiplex_id, expected_type=type_hints["multiplex_id"])
            check_type(argname="argument multiplex_program_settings", value=multiplex_program_settings, expected_type=type_hints["multiplex_program_settings"])
            check_type(argname="argument program_name", value=program_name, expected_type=type_hints["program_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "multiplex_id": multiplex_id,
            "multiplex_program_settings": multiplex_program_settings,
            "program_name": program_name,
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
    def multiplex_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#multiplex_id MedialiveMultiplexProgram#multiplex_id}.'''
        result = self._values.get("multiplex_id")
        assert result is not None, "Required property 'multiplex_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def multiplex_program_settings(
        self,
    ) -> "MedialiveMultiplexProgramMultiplexProgramSettings":
        '''multiplex_program_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#multiplex_program_settings MedialiveMultiplexProgram#multiplex_program_settings}
        '''
        result = self._values.get("multiplex_program_settings")
        assert result is not None, "Required property 'multiplex_program_settings' is missing"
        return typing.cast("MedialiveMultiplexProgramMultiplexProgramSettings", result)

    @builtins.property
    def program_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#program_name MedialiveMultiplexProgram#program_name}.'''
        result = self._values.get("program_name")
        assert result is not None, "Required property 'program_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MedialiveMultiplexProgramConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettings",
    jsii_struct_bases=[],
    name_mapping={
        "preferred_channel_pipeline": "preferredChannelPipeline",
        "program_number": "programNumber",
        "service_descriptor": "serviceDescriptor",
        "video_settings": "videoSettings",
    },
)
class MedialiveMultiplexProgramMultiplexProgramSettings:
    def __init__(
        self,
        *,
        preferred_channel_pipeline: builtins.str,
        program_number: jsii.Number,
        service_descriptor: typing.Optional[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor", typing.Dict[str, typing.Any]]] = None,
        video_settings: typing.Optional[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param preferred_channel_pipeline: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#preferred_channel_pipeline MedialiveMultiplexProgram#preferred_channel_pipeline}.
        :param program_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#program_number MedialiveMultiplexProgram#program_number}.
        :param service_descriptor: service_descriptor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#service_descriptor MedialiveMultiplexProgram#service_descriptor}
        :param video_settings: video_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#video_settings MedialiveMultiplexProgram#video_settings}
        '''
        if isinstance(service_descriptor, dict):
            service_descriptor = MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor(**service_descriptor)
        if isinstance(video_settings, dict):
            video_settings = MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings(**video_settings)
        if __debug__:
            def stub(
                *,
                preferred_channel_pipeline: builtins.str,
                program_number: jsii.Number,
                service_descriptor: typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor, typing.Dict[str, typing.Any]]] = None,
                video_settings: typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument preferred_channel_pipeline", value=preferred_channel_pipeline, expected_type=type_hints["preferred_channel_pipeline"])
            check_type(argname="argument program_number", value=program_number, expected_type=type_hints["program_number"])
            check_type(argname="argument service_descriptor", value=service_descriptor, expected_type=type_hints["service_descriptor"])
            check_type(argname="argument video_settings", value=video_settings, expected_type=type_hints["video_settings"])
        self._values: typing.Dict[str, typing.Any] = {
            "preferred_channel_pipeline": preferred_channel_pipeline,
            "program_number": program_number,
        }
        if service_descriptor is not None:
            self._values["service_descriptor"] = service_descriptor
        if video_settings is not None:
            self._values["video_settings"] = video_settings

    @builtins.property
    def preferred_channel_pipeline(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#preferred_channel_pipeline MedialiveMultiplexProgram#preferred_channel_pipeline}.'''
        result = self._values.get("preferred_channel_pipeline")
        assert result is not None, "Required property 'preferred_channel_pipeline' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def program_number(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#program_number MedialiveMultiplexProgram#program_number}.'''
        result = self._values.get("program_number")
        assert result is not None, "Required property 'program_number' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def service_descriptor(
        self,
    ) -> typing.Optional["MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor"]:
        '''service_descriptor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#service_descriptor MedialiveMultiplexProgram#service_descriptor}
        '''
        result = self._values.get("service_descriptor")
        return typing.cast(typing.Optional["MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor"], result)

    @builtins.property
    def video_settings(
        self,
    ) -> typing.Optional["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings"]:
        '''video_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#video_settings MedialiveMultiplexProgram#video_settings}
        '''
        result = self._values.get("video_settings")
        return typing.cast(typing.Optional["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MedialiveMultiplexProgramMultiplexProgramSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MedialiveMultiplexProgramMultiplexProgramSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsOutputReference",
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

    @jsii.member(jsii_name="putServiceDescriptor")
    def put_service_descriptor(
        self,
        *,
        provider_name: builtins.str,
        service_name: builtins.str,
    ) -> None:
        '''
        :param provider_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#provider_name MedialiveMultiplexProgram#provider_name}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#service_name MedialiveMultiplexProgram#service_name}.
        '''
        value = MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor(
            provider_name=provider_name, service_name=service_name
        )

        return typing.cast(None, jsii.invoke(self, "putServiceDescriptor", [value]))

    @jsii.member(jsii_name="putVideoSettings")
    def put_video_settings(
        self,
        *,
        constant_bitrate: typing.Optional[jsii.Number] = None,
        statemux_settings: typing.Optional[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings", typing.Dict[str, typing.Any]]] = None,
        statmux_settings: typing.Optional[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param constant_bitrate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#constant_bitrate MedialiveMultiplexProgram#constant_bitrate}.
        :param statemux_settings: statemux_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#statemux_settings MedialiveMultiplexProgram#statemux_settings}
        :param statmux_settings: statmux_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#statmux_settings MedialiveMultiplexProgram#statmux_settings}
        '''
        value = MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings(
            constant_bitrate=constant_bitrate,
            statemux_settings=statemux_settings,
            statmux_settings=statmux_settings,
        )

        return typing.cast(None, jsii.invoke(self, "putVideoSettings", [value]))

    @jsii.member(jsii_name="resetServiceDescriptor")
    def reset_service_descriptor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceDescriptor", []))

    @jsii.member(jsii_name="resetVideoSettings")
    def reset_video_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVideoSettings", []))

    @builtins.property
    @jsii.member(jsii_name="serviceDescriptor")
    def service_descriptor(
        self,
    ) -> "MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptorOutputReference":
        return typing.cast("MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptorOutputReference", jsii.get(self, "serviceDescriptor"))

    @builtins.property
    @jsii.member(jsii_name="videoSettings")
    def video_settings(
        self,
    ) -> "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsOutputReference":
        return typing.cast("MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsOutputReference", jsii.get(self, "videoSettings"))

    @builtins.property
    @jsii.member(jsii_name="preferredChannelPipelineInput")
    def preferred_channel_pipeline_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredChannelPipelineInput"))

    @builtins.property
    @jsii.member(jsii_name="programNumberInput")
    def program_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "programNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceDescriptorInput")
    def service_descriptor_input(
        self,
    ) -> typing.Optional["MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor"]:
        return typing.cast(typing.Optional["MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor"], jsii.get(self, "serviceDescriptorInput"))

    @builtins.property
    @jsii.member(jsii_name="videoSettingsInput")
    def video_settings_input(
        self,
    ) -> typing.Optional["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings"]:
        return typing.cast(typing.Optional["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings"], jsii.get(self, "videoSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredChannelPipeline")
    def preferred_channel_pipeline(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferredChannelPipeline"))

    @preferred_channel_pipeline.setter
    def preferred_channel_pipeline(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredChannelPipeline", value)

    @builtins.property
    @jsii.member(jsii_name="programNumber")
    def program_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "programNumber"))

    @program_number.setter
    def program_number(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "programNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettings]:
        return typing.cast(typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettings],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettings],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor",
    jsii_struct_bases=[],
    name_mapping={"provider_name": "providerName", "service_name": "serviceName"},
)
class MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor:
    def __init__(
        self,
        *,
        provider_name: builtins.str,
        service_name: builtins.str,
    ) -> None:
        '''
        :param provider_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#provider_name MedialiveMultiplexProgram#provider_name}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#service_name MedialiveMultiplexProgram#service_name}.
        '''
        if __debug__:
            def stub(
                *,
                provider_name: builtins.str,
                service_name: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument provider_name", value=provider_name, expected_type=type_hints["provider_name"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "provider_name": provider_name,
            "service_name": service_name,
        }

    @builtins.property
    def provider_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#provider_name MedialiveMultiplexProgram#provider_name}.'''
        result = self._values.get("provider_name")
        assert result is not None, "Required property 'provider_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#service_name MedialiveMultiplexProgram#service_name}.'''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptorOutputReference",
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
    @jsii.member(jsii_name="providerNameInput")
    def provider_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "providerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

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
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor]:
        return typing.cast(typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings",
    jsii_struct_bases=[],
    name_mapping={
        "constant_bitrate": "constantBitrate",
        "statemux_settings": "statemuxSettings",
        "statmux_settings": "statmuxSettings",
    },
)
class MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings:
    def __init__(
        self,
        *,
        constant_bitrate: typing.Optional[jsii.Number] = None,
        statemux_settings: typing.Optional[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings", typing.Dict[str, typing.Any]]] = None,
        statmux_settings: typing.Optional[typing.Union["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param constant_bitrate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#constant_bitrate MedialiveMultiplexProgram#constant_bitrate}.
        :param statemux_settings: statemux_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#statemux_settings MedialiveMultiplexProgram#statemux_settings}
        :param statmux_settings: statmux_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#statmux_settings MedialiveMultiplexProgram#statmux_settings}
        '''
        if isinstance(statemux_settings, dict):
            statemux_settings = MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings(**statemux_settings)
        if isinstance(statmux_settings, dict):
            statmux_settings = MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings(**statmux_settings)
        if __debug__:
            def stub(
                *,
                constant_bitrate: typing.Optional[jsii.Number] = None,
                statemux_settings: typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings, typing.Dict[str, typing.Any]]] = None,
                statmux_settings: typing.Optional[typing.Union[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument constant_bitrate", value=constant_bitrate, expected_type=type_hints["constant_bitrate"])
            check_type(argname="argument statemux_settings", value=statemux_settings, expected_type=type_hints["statemux_settings"])
            check_type(argname="argument statmux_settings", value=statmux_settings, expected_type=type_hints["statmux_settings"])
        self._values: typing.Dict[str, typing.Any] = {}
        if constant_bitrate is not None:
            self._values["constant_bitrate"] = constant_bitrate
        if statemux_settings is not None:
            self._values["statemux_settings"] = statemux_settings
        if statmux_settings is not None:
            self._values["statmux_settings"] = statmux_settings

    @builtins.property
    def constant_bitrate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#constant_bitrate MedialiveMultiplexProgram#constant_bitrate}.'''
        result = self._values.get("constant_bitrate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def statemux_settings(
        self,
    ) -> typing.Optional["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings"]:
        '''statemux_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#statemux_settings MedialiveMultiplexProgram#statemux_settings}
        '''
        result = self._values.get("statemux_settings")
        return typing.cast(typing.Optional["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings"], result)

    @builtins.property
    def statmux_settings(
        self,
    ) -> typing.Optional["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings"]:
        '''statmux_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#statmux_settings MedialiveMultiplexProgram#statmux_settings}
        '''
        result = self._values.get("statmux_settings")
        return typing.cast(typing.Optional["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsOutputReference",
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

    @jsii.member(jsii_name="putStatemuxSettings")
    def put_statemux_settings(
        self,
        *,
        maximum_bitrate: typing.Optional[jsii.Number] = None,
        minimum_bitrate: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param maximum_bitrate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#maximum_bitrate MedialiveMultiplexProgram#maximum_bitrate}.
        :param minimum_bitrate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#minimum_bitrate MedialiveMultiplexProgram#minimum_bitrate}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#priority MedialiveMultiplexProgram#priority}.
        '''
        value = MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings(
            maximum_bitrate=maximum_bitrate,
            minimum_bitrate=minimum_bitrate,
            priority=priority,
        )

        return typing.cast(None, jsii.invoke(self, "putStatemuxSettings", [value]))

    @jsii.member(jsii_name="putStatmuxSettings")
    def put_statmux_settings(
        self,
        *,
        maximum_bitrate: typing.Optional[jsii.Number] = None,
        minimum_bitrate: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param maximum_bitrate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#maximum_bitrate MedialiveMultiplexProgram#maximum_bitrate}.
        :param minimum_bitrate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#minimum_bitrate MedialiveMultiplexProgram#minimum_bitrate}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#priority MedialiveMultiplexProgram#priority}.
        '''
        value = MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings(
            maximum_bitrate=maximum_bitrate,
            minimum_bitrate=minimum_bitrate,
            priority=priority,
        )

        return typing.cast(None, jsii.invoke(self, "putStatmuxSettings", [value]))

    @jsii.member(jsii_name="resetConstantBitrate")
    def reset_constant_bitrate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConstantBitrate", []))

    @jsii.member(jsii_name="resetStatemuxSettings")
    def reset_statemux_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatemuxSettings", []))

    @jsii.member(jsii_name="resetStatmuxSettings")
    def reset_statmux_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatmuxSettings", []))

    @builtins.property
    @jsii.member(jsii_name="statemuxSettings")
    def statemux_settings(
        self,
    ) -> "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettingsOutputReference":
        return typing.cast("MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettingsOutputReference", jsii.get(self, "statemuxSettings"))

    @builtins.property
    @jsii.member(jsii_name="statmuxSettings")
    def statmux_settings(
        self,
    ) -> "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsOutputReference":
        return typing.cast("MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsOutputReference", jsii.get(self, "statmuxSettings"))

    @builtins.property
    @jsii.member(jsii_name="constantBitrateInput")
    def constant_bitrate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "constantBitrateInput"))

    @builtins.property
    @jsii.member(jsii_name="statemuxSettingsInput")
    def statemux_settings_input(
        self,
    ) -> typing.Optional["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings"]:
        return typing.cast(typing.Optional["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings"], jsii.get(self, "statemuxSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="statmuxSettingsInput")
    def statmux_settings_input(
        self,
    ) -> typing.Optional["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings"]:
        return typing.cast(typing.Optional["MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings"], jsii.get(self, "statmuxSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="constantBitrate")
    def constant_bitrate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "constantBitrate"))

    @constant_bitrate.setter
    def constant_bitrate(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "constantBitrate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings]:
        return typing.cast(typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings",
    jsii_struct_bases=[],
    name_mapping={
        "maximum_bitrate": "maximumBitrate",
        "minimum_bitrate": "minimumBitrate",
        "priority": "priority",
    },
)
class MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings:
    def __init__(
        self,
        *,
        maximum_bitrate: typing.Optional[jsii.Number] = None,
        minimum_bitrate: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param maximum_bitrate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#maximum_bitrate MedialiveMultiplexProgram#maximum_bitrate}.
        :param minimum_bitrate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#minimum_bitrate MedialiveMultiplexProgram#minimum_bitrate}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#priority MedialiveMultiplexProgram#priority}.
        '''
        if __debug__:
            def stub(
                *,
                maximum_bitrate: typing.Optional[jsii.Number] = None,
                minimum_bitrate: typing.Optional[jsii.Number] = None,
                priority: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument maximum_bitrate", value=maximum_bitrate, expected_type=type_hints["maximum_bitrate"])
            check_type(argname="argument minimum_bitrate", value=minimum_bitrate, expected_type=type_hints["minimum_bitrate"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
        self._values: typing.Dict[str, typing.Any] = {}
        if maximum_bitrate is not None:
            self._values["maximum_bitrate"] = maximum_bitrate
        if minimum_bitrate is not None:
            self._values["minimum_bitrate"] = minimum_bitrate
        if priority is not None:
            self._values["priority"] = priority

    @builtins.property
    def maximum_bitrate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#maximum_bitrate MedialiveMultiplexProgram#maximum_bitrate}.'''
        result = self._values.get("maximum_bitrate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minimum_bitrate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#minimum_bitrate MedialiveMultiplexProgram#minimum_bitrate}.'''
        result = self._values.get("minimum_bitrate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#priority MedialiveMultiplexProgram#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettingsOutputReference",
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

    @jsii.member(jsii_name="resetMaximumBitrate")
    def reset_maximum_bitrate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumBitrate", []))

    @jsii.member(jsii_name="resetMinimumBitrate")
    def reset_minimum_bitrate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumBitrate", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @builtins.property
    @jsii.member(jsii_name="maximumBitrateInput")
    def maximum_bitrate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumBitrateInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumBitrateInput")
    def minimum_bitrate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumBitrateInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumBitrate")
    def maximum_bitrate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumBitrate"))

    @maximum_bitrate.setter
    def maximum_bitrate(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumBitrate", value)

    @builtins.property
    @jsii.member(jsii_name="minimumBitrate")
    def minimum_bitrate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumBitrate"))

    @minimum_bitrate.setter
    def minimum_bitrate(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumBitrate", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings]:
        return typing.cast(typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings",
    jsii_struct_bases=[],
    name_mapping={
        "maximum_bitrate": "maximumBitrate",
        "minimum_bitrate": "minimumBitrate",
        "priority": "priority",
    },
)
class MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings:
    def __init__(
        self,
        *,
        maximum_bitrate: typing.Optional[jsii.Number] = None,
        minimum_bitrate: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param maximum_bitrate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#maximum_bitrate MedialiveMultiplexProgram#maximum_bitrate}.
        :param minimum_bitrate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#minimum_bitrate MedialiveMultiplexProgram#minimum_bitrate}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#priority MedialiveMultiplexProgram#priority}.
        '''
        if __debug__:
            def stub(
                *,
                maximum_bitrate: typing.Optional[jsii.Number] = None,
                minimum_bitrate: typing.Optional[jsii.Number] = None,
                priority: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument maximum_bitrate", value=maximum_bitrate, expected_type=type_hints["maximum_bitrate"])
            check_type(argname="argument minimum_bitrate", value=minimum_bitrate, expected_type=type_hints["minimum_bitrate"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
        self._values: typing.Dict[str, typing.Any] = {}
        if maximum_bitrate is not None:
            self._values["maximum_bitrate"] = maximum_bitrate
        if minimum_bitrate is not None:
            self._values["minimum_bitrate"] = minimum_bitrate
        if priority is not None:
            self._values["priority"] = priority

    @builtins.property
    def maximum_bitrate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#maximum_bitrate MedialiveMultiplexProgram#maximum_bitrate}.'''
        result = self._values.get("maximum_bitrate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minimum_bitrate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#minimum_bitrate MedialiveMultiplexProgram#minimum_bitrate}.'''
        result = self._values.get("minimum_bitrate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/medialive_multiplex_program#priority MedialiveMultiplexProgram#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.medialiveMultiplexProgram.MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsOutputReference",
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

    @jsii.member(jsii_name="resetMaximumBitrate")
    def reset_maximum_bitrate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumBitrate", []))

    @jsii.member(jsii_name="resetMinimumBitrate")
    def reset_minimum_bitrate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumBitrate", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @builtins.property
    @jsii.member(jsii_name="maximumBitrateInput")
    def maximum_bitrate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumBitrateInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumBitrateInput")
    def minimum_bitrate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumBitrateInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumBitrate")
    def maximum_bitrate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumBitrate"))

    @maximum_bitrate.setter
    def maximum_bitrate(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumBitrate", value)

    @builtins.property
    @jsii.member(jsii_name="minimumBitrate")
    def minimum_bitrate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumBitrate"))

    @minimum_bitrate.setter
    def minimum_bitrate(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumBitrate", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings]:
        return typing.cast(typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MedialiveMultiplexProgram",
    "MedialiveMultiplexProgramConfig",
    "MedialiveMultiplexProgramMultiplexProgramSettings",
    "MedialiveMultiplexProgramMultiplexProgramSettingsOutputReference",
    "MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptor",
    "MedialiveMultiplexProgramMultiplexProgramSettingsServiceDescriptorOutputReference",
    "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettings",
    "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsOutputReference",
    "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettings",
    "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatemuxSettingsOutputReference",
    "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettings",
    "MedialiveMultiplexProgramMultiplexProgramSettingsVideoSettingsStatmuxSettingsOutputReference",
]

publication.publish()
