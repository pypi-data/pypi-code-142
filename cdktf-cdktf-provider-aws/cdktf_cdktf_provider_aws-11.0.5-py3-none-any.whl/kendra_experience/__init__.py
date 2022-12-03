'''
# `aws_kendra_experience`

Refer to the Terraform Registory for docs: [`aws_kendra_experience`](https://www.terraform.io/docs/providers/aws/r/kendra_experience).
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


class KendraExperience(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraExperience.KendraExperience",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience aws_kendra_experience}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        index_id: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        configuration: typing.Optional[typing.Union["KendraExperienceConfiguration", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["KendraExperienceTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience aws_kendra_experience} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param index_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#index_id KendraExperience#index_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#name KendraExperience#name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#role_arn KendraExperience#role_arn}.
        :param configuration: configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#configuration KendraExperience#configuration}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#description KendraExperience#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#id KendraExperience#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#timeouts KendraExperience#timeouts}
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
                role_arn: builtins.str,
                configuration: typing.Optional[typing.Union[KendraExperienceConfiguration, typing.Dict[str, typing.Any]]] = None,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[KendraExperienceTimeouts, typing.Dict[str, typing.Any]]] = None,
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
        config = KendraExperienceConfig(
            index_id=index_id,
            name=name,
            role_arn=role_arn,
            configuration=configuration,
            description=description,
            id=id,
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
        content_source_configuration: typing.Optional[typing.Union["KendraExperienceConfigurationContentSourceConfiguration", typing.Dict[str, typing.Any]]] = None,
        user_identity_configuration: typing.Optional[typing.Union["KendraExperienceConfigurationUserIdentityConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param content_source_configuration: content_source_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#content_source_configuration KendraExperience#content_source_configuration}
        :param user_identity_configuration: user_identity_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#user_identity_configuration KendraExperience#user_identity_configuration}
        '''
        value = KendraExperienceConfiguration(
            content_source_configuration=content_source_configuration,
            user_identity_configuration=user_identity_configuration,
        )

        return typing.cast(None, jsii.invoke(self, "putConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#create KendraExperience#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#delete KendraExperience#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#update KendraExperience#update}.
        '''
        value = KendraExperienceTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetConfiguration")
    def reset_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfiguration", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    def configuration(self) -> "KendraExperienceConfigurationOutputReference":
        return typing.cast("KendraExperienceConfigurationOutputReference", jsii.get(self, "configuration"))

    @builtins.property
    @jsii.member(jsii_name="endpoints")
    def endpoints(self) -> "KendraExperienceEndpointsList":
        return typing.cast("KendraExperienceEndpointsList", jsii.get(self, "endpoints"))

    @builtins.property
    @jsii.member(jsii_name="experienceId")
    def experience_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "experienceId"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "KendraExperienceTimeoutsOutputReference":
        return typing.cast("KendraExperienceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="configurationInput")
    def configuration_input(self) -> typing.Optional["KendraExperienceConfiguration"]:
        return typing.cast(typing.Optional["KendraExperienceConfiguration"], jsii.get(self, "configurationInput"))

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
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["KendraExperienceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["KendraExperienceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

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


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraExperience.KendraExperienceConfig",
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
        "role_arn": "roleArn",
        "configuration": "configuration",
        "description": "description",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class KendraExperienceConfig(cdktf.TerraformMetaArguments):
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
        role_arn: builtins.str,
        configuration: typing.Optional[typing.Union["KendraExperienceConfiguration", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["KendraExperienceTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param index_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#index_id KendraExperience#index_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#name KendraExperience#name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#role_arn KendraExperience#role_arn}.
        :param configuration: configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#configuration KendraExperience#configuration}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#description KendraExperience#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#id KendraExperience#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#timeouts KendraExperience#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(configuration, dict):
            configuration = KendraExperienceConfiguration(**configuration)
        if isinstance(timeouts, dict):
            timeouts = KendraExperienceTimeouts(**timeouts)
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
                role_arn: builtins.str,
                configuration: typing.Optional[typing.Union[KendraExperienceConfiguration, typing.Dict[str, typing.Any]]] = None,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[KendraExperienceTimeouts, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "index_id": index_id,
            "name": name,
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
        if configuration is not None:
            self._values["configuration"] = configuration
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#index_id KendraExperience#index_id}.'''
        result = self._values.get("index_id")
        assert result is not None, "Required property 'index_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#name KendraExperience#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#role_arn KendraExperience#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration(self) -> typing.Optional["KendraExperienceConfiguration"]:
        '''configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#configuration KendraExperience#configuration}
        '''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional["KendraExperienceConfiguration"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#description KendraExperience#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#id KendraExperience#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["KendraExperienceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#timeouts KendraExperience#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["KendraExperienceTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraExperienceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraExperience.KendraExperienceConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "content_source_configuration": "contentSourceConfiguration",
        "user_identity_configuration": "userIdentityConfiguration",
    },
)
class KendraExperienceConfiguration:
    def __init__(
        self,
        *,
        content_source_configuration: typing.Optional[typing.Union["KendraExperienceConfigurationContentSourceConfiguration", typing.Dict[str, typing.Any]]] = None,
        user_identity_configuration: typing.Optional[typing.Union["KendraExperienceConfigurationUserIdentityConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param content_source_configuration: content_source_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#content_source_configuration KendraExperience#content_source_configuration}
        :param user_identity_configuration: user_identity_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#user_identity_configuration KendraExperience#user_identity_configuration}
        '''
        if isinstance(content_source_configuration, dict):
            content_source_configuration = KendraExperienceConfigurationContentSourceConfiguration(**content_source_configuration)
        if isinstance(user_identity_configuration, dict):
            user_identity_configuration = KendraExperienceConfigurationUserIdentityConfiguration(**user_identity_configuration)
        if __debug__:
            def stub(
                *,
                content_source_configuration: typing.Optional[typing.Union[KendraExperienceConfigurationContentSourceConfiguration, typing.Dict[str, typing.Any]]] = None,
                user_identity_configuration: typing.Optional[typing.Union[KendraExperienceConfigurationUserIdentityConfiguration, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument content_source_configuration", value=content_source_configuration, expected_type=type_hints["content_source_configuration"])
            check_type(argname="argument user_identity_configuration", value=user_identity_configuration, expected_type=type_hints["user_identity_configuration"])
        self._values: typing.Dict[str, typing.Any] = {}
        if content_source_configuration is not None:
            self._values["content_source_configuration"] = content_source_configuration
        if user_identity_configuration is not None:
            self._values["user_identity_configuration"] = user_identity_configuration

    @builtins.property
    def content_source_configuration(
        self,
    ) -> typing.Optional["KendraExperienceConfigurationContentSourceConfiguration"]:
        '''content_source_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#content_source_configuration KendraExperience#content_source_configuration}
        '''
        result = self._values.get("content_source_configuration")
        return typing.cast(typing.Optional["KendraExperienceConfigurationContentSourceConfiguration"], result)

    @builtins.property
    def user_identity_configuration(
        self,
    ) -> typing.Optional["KendraExperienceConfigurationUserIdentityConfiguration"]:
        '''user_identity_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#user_identity_configuration KendraExperience#user_identity_configuration}
        '''
        result = self._values.get("user_identity_configuration")
        return typing.cast(typing.Optional["KendraExperienceConfigurationUserIdentityConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraExperienceConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraExperience.KendraExperienceConfigurationContentSourceConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "data_source_ids": "dataSourceIds",
        "direct_put_content": "directPutContent",
        "faq_ids": "faqIds",
    },
)
class KendraExperienceConfigurationContentSourceConfiguration:
    def __init__(
        self,
        *,
        data_source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        direct_put_content: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        faq_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param data_source_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#data_source_ids KendraExperience#data_source_ids}.
        :param direct_put_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#direct_put_content KendraExperience#direct_put_content}.
        :param faq_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#faq_ids KendraExperience#faq_ids}.
        '''
        if __debug__:
            def stub(
                *,
                data_source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
                direct_put_content: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                faq_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument data_source_ids", value=data_source_ids, expected_type=type_hints["data_source_ids"])
            check_type(argname="argument direct_put_content", value=direct_put_content, expected_type=type_hints["direct_put_content"])
            check_type(argname="argument faq_ids", value=faq_ids, expected_type=type_hints["faq_ids"])
        self._values: typing.Dict[str, typing.Any] = {}
        if data_source_ids is not None:
            self._values["data_source_ids"] = data_source_ids
        if direct_put_content is not None:
            self._values["direct_put_content"] = direct_put_content
        if faq_ids is not None:
            self._values["faq_ids"] = faq_ids

    @builtins.property
    def data_source_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#data_source_ids KendraExperience#data_source_ids}.'''
        result = self._values.get("data_source_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def direct_put_content(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#direct_put_content KendraExperience#direct_put_content}.'''
        result = self._values.get("direct_put_content")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def faq_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#faq_ids KendraExperience#faq_ids}.'''
        result = self._values.get("faq_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraExperienceConfigurationContentSourceConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraExperienceConfigurationContentSourceConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraExperience.KendraExperienceConfigurationContentSourceConfigurationOutputReference",
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

    @jsii.member(jsii_name="resetDataSourceIds")
    def reset_data_source_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataSourceIds", []))

    @jsii.member(jsii_name="resetDirectPutContent")
    def reset_direct_put_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectPutContent", []))

    @jsii.member(jsii_name="resetFaqIds")
    def reset_faq_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFaqIds", []))

    @builtins.property
    @jsii.member(jsii_name="dataSourceIdsInput")
    def data_source_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dataSourceIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="directPutContentInput")
    def direct_put_content_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "directPutContentInput"))

    @builtins.property
    @jsii.member(jsii_name="faqIdsInput")
    def faq_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "faqIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceIds")
    def data_source_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dataSourceIds"))

    @data_source_ids.setter
    def data_source_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSourceIds", value)

    @builtins.property
    @jsii.member(jsii_name="directPutContent")
    def direct_put_content(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "directPutContent"))

    @direct_put_content.setter
    def direct_put_content(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directPutContent", value)

    @builtins.property
    @jsii.member(jsii_name="faqIds")
    def faq_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "faqIds"))

    @faq_ids.setter
    def faq_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "faqIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraExperienceConfigurationContentSourceConfiguration]:
        return typing.cast(typing.Optional[KendraExperienceConfigurationContentSourceConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraExperienceConfigurationContentSourceConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraExperienceConfigurationContentSourceConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraExperienceConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraExperience.KendraExperienceConfigurationOutputReference",
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

    @jsii.member(jsii_name="putContentSourceConfiguration")
    def put_content_source_configuration(
        self,
        *,
        data_source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        direct_put_content: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        faq_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param data_source_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#data_source_ids KendraExperience#data_source_ids}.
        :param direct_put_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#direct_put_content KendraExperience#direct_put_content}.
        :param faq_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#faq_ids KendraExperience#faq_ids}.
        '''
        value = KendraExperienceConfigurationContentSourceConfiguration(
            data_source_ids=data_source_ids,
            direct_put_content=direct_put_content,
            faq_ids=faq_ids,
        )

        return typing.cast(None, jsii.invoke(self, "putContentSourceConfiguration", [value]))

    @jsii.member(jsii_name="putUserIdentityConfiguration")
    def put_user_identity_configuration(
        self,
        *,
        identity_attribute_name: builtins.str,
    ) -> None:
        '''
        :param identity_attribute_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#identity_attribute_name KendraExperience#identity_attribute_name}.
        '''
        value = KendraExperienceConfigurationUserIdentityConfiguration(
            identity_attribute_name=identity_attribute_name
        )

        return typing.cast(None, jsii.invoke(self, "putUserIdentityConfiguration", [value]))

    @jsii.member(jsii_name="resetContentSourceConfiguration")
    def reset_content_source_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentSourceConfiguration", []))

    @jsii.member(jsii_name="resetUserIdentityConfiguration")
    def reset_user_identity_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserIdentityConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="contentSourceConfiguration")
    def content_source_configuration(
        self,
    ) -> KendraExperienceConfigurationContentSourceConfigurationOutputReference:
        return typing.cast(KendraExperienceConfigurationContentSourceConfigurationOutputReference, jsii.get(self, "contentSourceConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="userIdentityConfiguration")
    def user_identity_configuration(
        self,
    ) -> "KendraExperienceConfigurationUserIdentityConfigurationOutputReference":
        return typing.cast("KendraExperienceConfigurationUserIdentityConfigurationOutputReference", jsii.get(self, "userIdentityConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="contentSourceConfigurationInput")
    def content_source_configuration_input(
        self,
    ) -> typing.Optional[KendraExperienceConfigurationContentSourceConfiguration]:
        return typing.cast(typing.Optional[KendraExperienceConfigurationContentSourceConfiguration], jsii.get(self, "contentSourceConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="userIdentityConfigurationInput")
    def user_identity_configuration_input(
        self,
    ) -> typing.Optional["KendraExperienceConfigurationUserIdentityConfiguration"]:
        return typing.cast(typing.Optional["KendraExperienceConfigurationUserIdentityConfiguration"], jsii.get(self, "userIdentityConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KendraExperienceConfiguration]:
        return typing.cast(typing.Optional[KendraExperienceConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraExperienceConfiguration],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[KendraExperienceConfiguration]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraExperience.KendraExperienceConfigurationUserIdentityConfiguration",
    jsii_struct_bases=[],
    name_mapping={"identity_attribute_name": "identityAttributeName"},
)
class KendraExperienceConfigurationUserIdentityConfiguration:
    def __init__(self, *, identity_attribute_name: builtins.str) -> None:
        '''
        :param identity_attribute_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#identity_attribute_name KendraExperience#identity_attribute_name}.
        '''
        if __debug__:
            def stub(*, identity_attribute_name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument identity_attribute_name", value=identity_attribute_name, expected_type=type_hints["identity_attribute_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "identity_attribute_name": identity_attribute_name,
        }

    @builtins.property
    def identity_attribute_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#identity_attribute_name KendraExperience#identity_attribute_name}.'''
        result = self._values.get("identity_attribute_name")
        assert result is not None, "Required property 'identity_attribute_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraExperienceConfigurationUserIdentityConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraExperienceConfigurationUserIdentityConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraExperience.KendraExperienceConfigurationUserIdentityConfigurationOutputReference",
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
    @jsii.member(jsii_name="identityAttributeNameInput")
    def identity_attribute_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityAttributeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="identityAttributeName")
    def identity_attribute_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityAttributeName"))

    @identity_attribute_name.setter
    def identity_attribute_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityAttributeName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraExperienceConfigurationUserIdentityConfiguration]:
        return typing.cast(typing.Optional[KendraExperienceConfigurationUserIdentityConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraExperienceConfigurationUserIdentityConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraExperienceConfigurationUserIdentityConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraExperience.KendraExperienceEndpoints",
    jsii_struct_bases=[],
    name_mapping={},
)
class KendraExperienceEndpoints:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraExperienceEndpoints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraExperienceEndpointsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraExperience.KendraExperienceEndpointsList",
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
    def get(self, index: jsii.Number) -> "KendraExperienceEndpointsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KendraExperienceEndpointsOutputReference", jsii.invoke(self, "get", [index]))

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


class KendraExperienceEndpointsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraExperience.KendraExperienceEndpointsOutputReference",
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
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @builtins.property
    @jsii.member(jsii_name="endpointType")
    def endpoint_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointType"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KendraExperienceEndpoints]:
        return typing.cast(typing.Optional[KendraExperienceEndpoints], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[KendraExperienceEndpoints]) -> None:
        if __debug__:
            def stub(value: typing.Optional[KendraExperienceEndpoints]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraExperience.KendraExperienceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class KendraExperienceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#create KendraExperience#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#delete KendraExperience#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#update KendraExperience#update}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#create KendraExperience#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#delete KendraExperience#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_experience#update KendraExperience#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraExperienceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraExperienceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraExperience.KendraExperienceTimeoutsOutputReference",
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
    ) -> typing.Optional[typing.Union[KendraExperienceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KendraExperienceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KendraExperienceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KendraExperienceTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KendraExperience",
    "KendraExperienceConfig",
    "KendraExperienceConfiguration",
    "KendraExperienceConfigurationContentSourceConfiguration",
    "KendraExperienceConfigurationContentSourceConfigurationOutputReference",
    "KendraExperienceConfigurationOutputReference",
    "KendraExperienceConfigurationUserIdentityConfiguration",
    "KendraExperienceConfigurationUserIdentityConfigurationOutputReference",
    "KendraExperienceEndpoints",
    "KendraExperienceEndpointsList",
    "KendraExperienceEndpointsOutputReference",
    "KendraExperienceTimeouts",
    "KendraExperienceTimeoutsOutputReference",
]

publication.publish()
