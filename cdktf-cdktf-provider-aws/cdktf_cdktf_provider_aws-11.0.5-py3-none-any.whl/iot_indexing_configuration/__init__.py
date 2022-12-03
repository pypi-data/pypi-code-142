'''
# `aws_iot_indexing_configuration`

Refer to the Terraform Registory for docs: [`aws_iot_indexing_configuration`](https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration).
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


class IotIndexingConfiguration(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.iotIndexingConfiguration.IotIndexingConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration aws_iot_indexing_configuration}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        id: typing.Optional[builtins.str] = None,
        thing_group_indexing_configuration: typing.Optional[typing.Union["IotIndexingConfigurationThingGroupIndexingConfiguration", typing.Dict[str, typing.Any]]] = None,
        thing_indexing_configuration: typing.Optional[typing.Union["IotIndexingConfigurationThingIndexingConfiguration", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration aws_iot_indexing_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#id IotIndexingConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param thing_group_indexing_configuration: thing_group_indexing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_group_indexing_configuration IotIndexingConfiguration#thing_group_indexing_configuration}
        :param thing_indexing_configuration: thing_indexing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_indexing_configuration IotIndexingConfiguration#thing_indexing_configuration}
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
                id: typing.Optional[builtins.str] = None,
                thing_group_indexing_configuration: typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfiguration, typing.Dict[str, typing.Any]]] = None,
                thing_indexing_configuration: typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfiguration, typing.Dict[str, typing.Any]]] = None,
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
        config = IotIndexingConfigurationConfig(
            id=id,
            thing_group_indexing_configuration=thing_group_indexing_configuration,
            thing_indexing_configuration=thing_indexing_configuration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putThingGroupIndexingConfiguration")
    def put_thing_group_indexing_configuration(
        self,
        *,
        thing_group_indexing_mode: builtins.str,
        custom_field: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IotIndexingConfigurationThingGroupIndexingConfigurationCustomField", typing.Dict[str, typing.Any]]]]] = None,
        managed_field: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IotIndexingConfigurationThingGroupIndexingConfigurationManagedField", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param thing_group_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_group_indexing_mode IotIndexingConfiguration#thing_group_indexing_mode}.
        :param custom_field: custom_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#custom_field IotIndexingConfiguration#custom_field}
        :param managed_field: managed_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#managed_field IotIndexingConfiguration#managed_field}
        '''
        value = IotIndexingConfigurationThingGroupIndexingConfiguration(
            thing_group_indexing_mode=thing_group_indexing_mode,
            custom_field=custom_field,
            managed_field=managed_field,
        )

        return typing.cast(None, jsii.invoke(self, "putThingGroupIndexingConfiguration", [value]))

    @jsii.member(jsii_name="putThingIndexingConfiguration")
    def put_thing_indexing_configuration(
        self,
        *,
        thing_indexing_mode: builtins.str,
        custom_field: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IotIndexingConfigurationThingIndexingConfigurationCustomField", typing.Dict[str, typing.Any]]]]] = None,
        device_defender_indexing_mode: typing.Optional[builtins.str] = None,
        managed_field: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IotIndexingConfigurationThingIndexingConfigurationManagedField", typing.Dict[str, typing.Any]]]]] = None,
        named_shadow_indexing_mode: typing.Optional[builtins.str] = None,
        thing_connectivity_indexing_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param thing_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_indexing_mode IotIndexingConfiguration#thing_indexing_mode}.
        :param custom_field: custom_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#custom_field IotIndexingConfiguration#custom_field}
        :param device_defender_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#device_defender_indexing_mode IotIndexingConfiguration#device_defender_indexing_mode}.
        :param managed_field: managed_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#managed_field IotIndexingConfiguration#managed_field}
        :param named_shadow_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#named_shadow_indexing_mode IotIndexingConfiguration#named_shadow_indexing_mode}.
        :param thing_connectivity_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_connectivity_indexing_mode IotIndexingConfiguration#thing_connectivity_indexing_mode}.
        '''
        value = IotIndexingConfigurationThingIndexingConfiguration(
            thing_indexing_mode=thing_indexing_mode,
            custom_field=custom_field,
            device_defender_indexing_mode=device_defender_indexing_mode,
            managed_field=managed_field,
            named_shadow_indexing_mode=named_shadow_indexing_mode,
            thing_connectivity_indexing_mode=thing_connectivity_indexing_mode,
        )

        return typing.cast(None, jsii.invoke(self, "putThingIndexingConfiguration", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetThingGroupIndexingConfiguration")
    def reset_thing_group_indexing_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThingGroupIndexingConfiguration", []))

    @jsii.member(jsii_name="resetThingIndexingConfiguration")
    def reset_thing_indexing_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThingIndexingConfiguration", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="thingGroupIndexingConfiguration")
    def thing_group_indexing_configuration(
        self,
    ) -> "IotIndexingConfigurationThingGroupIndexingConfigurationOutputReference":
        return typing.cast("IotIndexingConfigurationThingGroupIndexingConfigurationOutputReference", jsii.get(self, "thingGroupIndexingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="thingIndexingConfiguration")
    def thing_indexing_configuration(
        self,
    ) -> "IotIndexingConfigurationThingIndexingConfigurationOutputReference":
        return typing.cast("IotIndexingConfigurationThingIndexingConfigurationOutputReference", jsii.get(self, "thingIndexingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="thingGroupIndexingConfigurationInput")
    def thing_group_indexing_configuration_input(
        self,
    ) -> typing.Optional["IotIndexingConfigurationThingGroupIndexingConfiguration"]:
        return typing.cast(typing.Optional["IotIndexingConfigurationThingGroupIndexingConfiguration"], jsii.get(self, "thingGroupIndexingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="thingIndexingConfigurationInput")
    def thing_indexing_configuration_input(
        self,
    ) -> typing.Optional["IotIndexingConfigurationThingIndexingConfiguration"]:
        return typing.cast(typing.Optional["IotIndexingConfigurationThingIndexingConfiguration"], jsii.get(self, "thingIndexingConfigurationInput"))

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


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.iotIndexingConfiguration.IotIndexingConfigurationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "id": "id",
        "thing_group_indexing_configuration": "thingGroupIndexingConfiguration",
        "thing_indexing_configuration": "thingIndexingConfiguration",
    },
)
class IotIndexingConfigurationConfig(cdktf.TerraformMetaArguments):
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
        id: typing.Optional[builtins.str] = None,
        thing_group_indexing_configuration: typing.Optional[typing.Union["IotIndexingConfigurationThingGroupIndexingConfiguration", typing.Dict[str, typing.Any]]] = None,
        thing_indexing_configuration: typing.Optional[typing.Union["IotIndexingConfigurationThingIndexingConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#id IotIndexingConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param thing_group_indexing_configuration: thing_group_indexing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_group_indexing_configuration IotIndexingConfiguration#thing_group_indexing_configuration}
        :param thing_indexing_configuration: thing_indexing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_indexing_configuration IotIndexingConfiguration#thing_indexing_configuration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(thing_group_indexing_configuration, dict):
            thing_group_indexing_configuration = IotIndexingConfigurationThingGroupIndexingConfiguration(**thing_group_indexing_configuration)
        if isinstance(thing_indexing_configuration, dict):
            thing_indexing_configuration = IotIndexingConfigurationThingIndexingConfiguration(**thing_indexing_configuration)
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
                id: typing.Optional[builtins.str] = None,
                thing_group_indexing_configuration: typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfiguration, typing.Dict[str, typing.Any]]] = None,
                thing_indexing_configuration: typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfiguration, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument thing_group_indexing_configuration", value=thing_group_indexing_configuration, expected_type=type_hints["thing_group_indexing_configuration"])
            check_type(argname="argument thing_indexing_configuration", value=thing_indexing_configuration, expected_type=type_hints["thing_indexing_configuration"])
        self._values: typing.Dict[str, typing.Any] = {}
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
        if id is not None:
            self._values["id"] = id
        if thing_group_indexing_configuration is not None:
            self._values["thing_group_indexing_configuration"] = thing_group_indexing_configuration
        if thing_indexing_configuration is not None:
            self._values["thing_indexing_configuration"] = thing_indexing_configuration

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
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#id IotIndexingConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def thing_group_indexing_configuration(
        self,
    ) -> typing.Optional["IotIndexingConfigurationThingGroupIndexingConfiguration"]:
        '''thing_group_indexing_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_group_indexing_configuration IotIndexingConfiguration#thing_group_indexing_configuration}
        '''
        result = self._values.get("thing_group_indexing_configuration")
        return typing.cast(typing.Optional["IotIndexingConfigurationThingGroupIndexingConfiguration"], result)

    @builtins.property
    def thing_indexing_configuration(
        self,
    ) -> typing.Optional["IotIndexingConfigurationThingIndexingConfiguration"]:
        '''thing_indexing_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_indexing_configuration IotIndexingConfiguration#thing_indexing_configuration}
        '''
        result = self._values.get("thing_indexing_configuration")
        return typing.cast(typing.Optional["IotIndexingConfigurationThingIndexingConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotIndexingConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.iotIndexingConfiguration.IotIndexingConfigurationThingGroupIndexingConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "thing_group_indexing_mode": "thingGroupIndexingMode",
        "custom_field": "customField",
        "managed_field": "managedField",
    },
)
class IotIndexingConfigurationThingGroupIndexingConfiguration:
    def __init__(
        self,
        *,
        thing_group_indexing_mode: builtins.str,
        custom_field: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IotIndexingConfigurationThingGroupIndexingConfigurationCustomField", typing.Dict[str, typing.Any]]]]] = None,
        managed_field: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IotIndexingConfigurationThingGroupIndexingConfigurationManagedField", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param thing_group_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_group_indexing_mode IotIndexingConfiguration#thing_group_indexing_mode}.
        :param custom_field: custom_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#custom_field IotIndexingConfiguration#custom_field}
        :param managed_field: managed_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#managed_field IotIndexingConfiguration#managed_field}
        '''
        if __debug__:
            def stub(
                *,
                thing_group_indexing_mode: builtins.str,
                custom_field: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField, typing.Dict[str, typing.Any]]]]] = None,
                managed_field: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument thing_group_indexing_mode", value=thing_group_indexing_mode, expected_type=type_hints["thing_group_indexing_mode"])
            check_type(argname="argument custom_field", value=custom_field, expected_type=type_hints["custom_field"])
            check_type(argname="argument managed_field", value=managed_field, expected_type=type_hints["managed_field"])
        self._values: typing.Dict[str, typing.Any] = {
            "thing_group_indexing_mode": thing_group_indexing_mode,
        }
        if custom_field is not None:
            self._values["custom_field"] = custom_field
        if managed_field is not None:
            self._values["managed_field"] = managed_field

    @builtins.property
    def thing_group_indexing_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_group_indexing_mode IotIndexingConfiguration#thing_group_indexing_mode}.'''
        result = self._values.get("thing_group_indexing_mode")
        assert result is not None, "Required property 'thing_group_indexing_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_field(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IotIndexingConfigurationThingGroupIndexingConfigurationCustomField"]]]:
        '''custom_field block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#custom_field IotIndexingConfiguration#custom_field}
        '''
        result = self._values.get("custom_field")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IotIndexingConfigurationThingGroupIndexingConfigurationCustomField"]]], result)

    @builtins.property
    def managed_field(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IotIndexingConfigurationThingGroupIndexingConfigurationManagedField"]]]:
        '''managed_field block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#managed_field IotIndexingConfiguration#managed_field}
        '''
        result = self._values.get("managed_field")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IotIndexingConfigurationThingGroupIndexingConfigurationManagedField"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotIndexingConfigurationThingGroupIndexingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.iotIndexingConfiguration.IotIndexingConfigurationThingGroupIndexingConfigurationCustomField",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class IotIndexingConfigurationThingGroupIndexingConfigurationCustomField:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#name IotIndexingConfiguration#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#type IotIndexingConfiguration#type}.
        '''
        if __debug__:
            def stub(
                *,
                name: typing.Optional[builtins.str] = None,
                type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#name IotIndexingConfiguration#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#type IotIndexingConfiguration#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotIndexingConfigurationThingGroupIndexingConfigurationCustomField(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.iotIndexingConfiguration.IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldList",
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
    ) -> "IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.iotIndexingConfiguration.IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldOutputReference",
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

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

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
    ) -> typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.iotIndexingConfiguration.IotIndexingConfigurationThingGroupIndexingConfigurationManagedField",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class IotIndexingConfigurationThingGroupIndexingConfigurationManagedField:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#name IotIndexingConfiguration#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#type IotIndexingConfiguration#type}.
        '''
        if __debug__:
            def stub(
                *,
                name: typing.Optional[builtins.str] = None,
                type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#name IotIndexingConfiguration#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#type IotIndexingConfiguration#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotIndexingConfigurationThingGroupIndexingConfigurationManagedField(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.iotIndexingConfiguration.IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldList",
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
    ) -> "IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.iotIndexingConfiguration.IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldOutputReference",
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

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

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
    ) -> typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotIndexingConfigurationThingGroupIndexingConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.iotIndexingConfiguration.IotIndexingConfigurationThingGroupIndexingConfigurationOutputReference",
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

    @jsii.member(jsii_name="putCustomField")
    def put_custom_field(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomField", [value]))

    @jsii.member(jsii_name="putManagedField")
    def put_managed_field(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putManagedField", [value]))

    @jsii.member(jsii_name="resetCustomField")
    def reset_custom_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomField", []))

    @jsii.member(jsii_name="resetManagedField")
    def reset_managed_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedField", []))

    @builtins.property
    @jsii.member(jsii_name="customField")
    def custom_field(
        self,
    ) -> IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldList:
        return typing.cast(IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldList, jsii.get(self, "customField"))

    @builtins.property
    @jsii.member(jsii_name="managedField")
    def managed_field(
        self,
    ) -> IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldList:
        return typing.cast(IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldList, jsii.get(self, "managedField"))

    @builtins.property
    @jsii.member(jsii_name="customFieldInput")
    def custom_field_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationCustomField]]], jsii.get(self, "customFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="managedFieldInput")
    def managed_field_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingGroupIndexingConfigurationManagedField]]], jsii.get(self, "managedFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="thingGroupIndexingModeInput")
    def thing_group_indexing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thingGroupIndexingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="thingGroupIndexingMode")
    def thing_group_indexing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thingGroupIndexingMode"))

    @thing_group_indexing_mode.setter
    def thing_group_indexing_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thingGroupIndexingMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IotIndexingConfigurationThingGroupIndexingConfiguration]:
        return typing.cast(typing.Optional[IotIndexingConfigurationThingGroupIndexingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotIndexingConfigurationThingGroupIndexingConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[IotIndexingConfigurationThingGroupIndexingConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.iotIndexingConfiguration.IotIndexingConfigurationThingIndexingConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "thing_indexing_mode": "thingIndexingMode",
        "custom_field": "customField",
        "device_defender_indexing_mode": "deviceDefenderIndexingMode",
        "managed_field": "managedField",
        "named_shadow_indexing_mode": "namedShadowIndexingMode",
        "thing_connectivity_indexing_mode": "thingConnectivityIndexingMode",
    },
)
class IotIndexingConfigurationThingIndexingConfiguration:
    def __init__(
        self,
        *,
        thing_indexing_mode: builtins.str,
        custom_field: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IotIndexingConfigurationThingIndexingConfigurationCustomField", typing.Dict[str, typing.Any]]]]] = None,
        device_defender_indexing_mode: typing.Optional[builtins.str] = None,
        managed_field: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["IotIndexingConfigurationThingIndexingConfigurationManagedField", typing.Dict[str, typing.Any]]]]] = None,
        named_shadow_indexing_mode: typing.Optional[builtins.str] = None,
        thing_connectivity_indexing_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param thing_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_indexing_mode IotIndexingConfiguration#thing_indexing_mode}.
        :param custom_field: custom_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#custom_field IotIndexingConfiguration#custom_field}
        :param device_defender_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#device_defender_indexing_mode IotIndexingConfiguration#device_defender_indexing_mode}.
        :param managed_field: managed_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#managed_field IotIndexingConfiguration#managed_field}
        :param named_shadow_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#named_shadow_indexing_mode IotIndexingConfiguration#named_shadow_indexing_mode}.
        :param thing_connectivity_indexing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_connectivity_indexing_mode IotIndexingConfiguration#thing_connectivity_indexing_mode}.
        '''
        if __debug__:
            def stub(
                *,
                thing_indexing_mode: builtins.str,
                custom_field: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingIndexingConfigurationCustomField, typing.Dict[str, typing.Any]]]]] = None,
                device_defender_indexing_mode: typing.Optional[builtins.str] = None,
                managed_field: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingIndexingConfigurationManagedField, typing.Dict[str, typing.Any]]]]] = None,
                named_shadow_indexing_mode: typing.Optional[builtins.str] = None,
                thing_connectivity_indexing_mode: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument thing_indexing_mode", value=thing_indexing_mode, expected_type=type_hints["thing_indexing_mode"])
            check_type(argname="argument custom_field", value=custom_field, expected_type=type_hints["custom_field"])
            check_type(argname="argument device_defender_indexing_mode", value=device_defender_indexing_mode, expected_type=type_hints["device_defender_indexing_mode"])
            check_type(argname="argument managed_field", value=managed_field, expected_type=type_hints["managed_field"])
            check_type(argname="argument named_shadow_indexing_mode", value=named_shadow_indexing_mode, expected_type=type_hints["named_shadow_indexing_mode"])
            check_type(argname="argument thing_connectivity_indexing_mode", value=thing_connectivity_indexing_mode, expected_type=type_hints["thing_connectivity_indexing_mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "thing_indexing_mode": thing_indexing_mode,
        }
        if custom_field is not None:
            self._values["custom_field"] = custom_field
        if device_defender_indexing_mode is not None:
            self._values["device_defender_indexing_mode"] = device_defender_indexing_mode
        if managed_field is not None:
            self._values["managed_field"] = managed_field
        if named_shadow_indexing_mode is not None:
            self._values["named_shadow_indexing_mode"] = named_shadow_indexing_mode
        if thing_connectivity_indexing_mode is not None:
            self._values["thing_connectivity_indexing_mode"] = thing_connectivity_indexing_mode

    @builtins.property
    def thing_indexing_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_indexing_mode IotIndexingConfiguration#thing_indexing_mode}.'''
        result = self._values.get("thing_indexing_mode")
        assert result is not None, "Required property 'thing_indexing_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_field(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IotIndexingConfigurationThingIndexingConfigurationCustomField"]]]:
        '''custom_field block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#custom_field IotIndexingConfiguration#custom_field}
        '''
        result = self._values.get("custom_field")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IotIndexingConfigurationThingIndexingConfigurationCustomField"]]], result)

    @builtins.property
    def device_defender_indexing_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#device_defender_indexing_mode IotIndexingConfiguration#device_defender_indexing_mode}.'''
        result = self._values.get("device_defender_indexing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_field(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IotIndexingConfigurationThingIndexingConfigurationManagedField"]]]:
        '''managed_field block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#managed_field IotIndexingConfiguration#managed_field}
        '''
        result = self._values.get("managed_field")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["IotIndexingConfigurationThingIndexingConfigurationManagedField"]]], result)

    @builtins.property
    def named_shadow_indexing_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#named_shadow_indexing_mode IotIndexingConfiguration#named_shadow_indexing_mode}.'''
        result = self._values.get("named_shadow_indexing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def thing_connectivity_indexing_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#thing_connectivity_indexing_mode IotIndexingConfiguration#thing_connectivity_indexing_mode}.'''
        result = self._values.get("thing_connectivity_indexing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotIndexingConfigurationThingIndexingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.iotIndexingConfiguration.IotIndexingConfigurationThingIndexingConfigurationCustomField",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class IotIndexingConfigurationThingIndexingConfigurationCustomField:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#name IotIndexingConfiguration#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#type IotIndexingConfiguration#type}.
        '''
        if __debug__:
            def stub(
                *,
                name: typing.Optional[builtins.str] = None,
                type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#name IotIndexingConfiguration#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#type IotIndexingConfiguration#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotIndexingConfigurationThingIndexingConfigurationCustomField(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotIndexingConfigurationThingIndexingConfigurationCustomFieldList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.iotIndexingConfiguration.IotIndexingConfigurationThingIndexingConfigurationCustomFieldList",
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
    ) -> "IotIndexingConfigurationThingIndexingConfigurationCustomFieldOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotIndexingConfigurationThingIndexingConfigurationCustomFieldOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationCustomField]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationCustomField]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationCustomField]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationCustomField]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotIndexingConfigurationThingIndexingConfigurationCustomFieldOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.iotIndexingConfiguration.IotIndexingConfigurationThingIndexingConfigurationCustomFieldOutputReference",
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

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

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
    ) -> typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfigurationCustomField, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfigurationCustomField, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfigurationCustomField, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfigurationCustomField, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.iotIndexingConfiguration.IotIndexingConfigurationThingIndexingConfigurationManagedField",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class IotIndexingConfigurationThingIndexingConfigurationManagedField:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#name IotIndexingConfiguration#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#type IotIndexingConfiguration#type}.
        '''
        if __debug__:
            def stub(
                *,
                name: typing.Optional[builtins.str] = None,
                type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#name IotIndexingConfiguration#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_indexing_configuration#type IotIndexingConfiguration#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotIndexingConfigurationThingIndexingConfigurationManagedField(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotIndexingConfigurationThingIndexingConfigurationManagedFieldList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.iotIndexingConfiguration.IotIndexingConfigurationThingIndexingConfigurationManagedFieldList",
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
    ) -> "IotIndexingConfigurationThingIndexingConfigurationManagedFieldOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotIndexingConfigurationThingIndexingConfigurationManagedFieldOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationManagedField]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationManagedField]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationManagedField]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationManagedField]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotIndexingConfigurationThingIndexingConfigurationManagedFieldOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.iotIndexingConfiguration.IotIndexingConfigurationThingIndexingConfigurationManagedFieldOutputReference",
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

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

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
    ) -> typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfigurationManagedField, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfigurationManagedField, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfigurationManagedField, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[IotIndexingConfigurationThingIndexingConfigurationManagedField, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotIndexingConfigurationThingIndexingConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.iotIndexingConfiguration.IotIndexingConfigurationThingIndexingConfigurationOutputReference",
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

    @jsii.member(jsii_name="putCustomField")
    def put_custom_field(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingIndexingConfigurationCustomField, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingIndexingConfigurationCustomField, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomField", [value]))

    @jsii.member(jsii_name="putManagedField")
    def put_managed_field(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingIndexingConfigurationManagedField, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[IotIndexingConfigurationThingIndexingConfigurationManagedField, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putManagedField", [value]))

    @jsii.member(jsii_name="resetCustomField")
    def reset_custom_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomField", []))

    @jsii.member(jsii_name="resetDeviceDefenderIndexingMode")
    def reset_device_defender_indexing_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceDefenderIndexingMode", []))

    @jsii.member(jsii_name="resetManagedField")
    def reset_managed_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedField", []))

    @jsii.member(jsii_name="resetNamedShadowIndexingMode")
    def reset_named_shadow_indexing_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamedShadowIndexingMode", []))

    @jsii.member(jsii_name="resetThingConnectivityIndexingMode")
    def reset_thing_connectivity_indexing_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThingConnectivityIndexingMode", []))

    @builtins.property
    @jsii.member(jsii_name="customField")
    def custom_field(
        self,
    ) -> IotIndexingConfigurationThingIndexingConfigurationCustomFieldList:
        return typing.cast(IotIndexingConfigurationThingIndexingConfigurationCustomFieldList, jsii.get(self, "customField"))

    @builtins.property
    @jsii.member(jsii_name="managedField")
    def managed_field(
        self,
    ) -> IotIndexingConfigurationThingIndexingConfigurationManagedFieldList:
        return typing.cast(IotIndexingConfigurationThingIndexingConfigurationManagedFieldList, jsii.get(self, "managedField"))

    @builtins.property
    @jsii.member(jsii_name="customFieldInput")
    def custom_field_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationCustomField]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationCustomField]]], jsii.get(self, "customFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceDefenderIndexingModeInput")
    def device_defender_indexing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceDefenderIndexingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="managedFieldInput")
    def managed_field_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationManagedField]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[IotIndexingConfigurationThingIndexingConfigurationManagedField]]], jsii.get(self, "managedFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="namedShadowIndexingModeInput")
    def named_shadow_indexing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namedShadowIndexingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="thingConnectivityIndexingModeInput")
    def thing_connectivity_indexing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thingConnectivityIndexingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="thingIndexingModeInput")
    def thing_indexing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thingIndexingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceDefenderIndexingMode")
    def device_defender_indexing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceDefenderIndexingMode"))

    @device_defender_indexing_mode.setter
    def device_defender_indexing_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceDefenderIndexingMode", value)

    @builtins.property
    @jsii.member(jsii_name="namedShadowIndexingMode")
    def named_shadow_indexing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namedShadowIndexingMode"))

    @named_shadow_indexing_mode.setter
    def named_shadow_indexing_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namedShadowIndexingMode", value)

    @builtins.property
    @jsii.member(jsii_name="thingConnectivityIndexingMode")
    def thing_connectivity_indexing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thingConnectivityIndexingMode"))

    @thing_connectivity_indexing_mode.setter
    def thing_connectivity_indexing_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thingConnectivityIndexingMode", value)

    @builtins.property
    @jsii.member(jsii_name="thingIndexingMode")
    def thing_indexing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thingIndexingMode"))

    @thing_indexing_mode.setter
    def thing_indexing_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thingIndexingMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IotIndexingConfigurationThingIndexingConfiguration]:
        return typing.cast(typing.Optional[IotIndexingConfigurationThingIndexingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotIndexingConfigurationThingIndexingConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[IotIndexingConfigurationThingIndexingConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "IotIndexingConfiguration",
    "IotIndexingConfigurationConfig",
    "IotIndexingConfigurationThingGroupIndexingConfiguration",
    "IotIndexingConfigurationThingGroupIndexingConfigurationCustomField",
    "IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldList",
    "IotIndexingConfigurationThingGroupIndexingConfigurationCustomFieldOutputReference",
    "IotIndexingConfigurationThingGroupIndexingConfigurationManagedField",
    "IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldList",
    "IotIndexingConfigurationThingGroupIndexingConfigurationManagedFieldOutputReference",
    "IotIndexingConfigurationThingGroupIndexingConfigurationOutputReference",
    "IotIndexingConfigurationThingIndexingConfiguration",
    "IotIndexingConfigurationThingIndexingConfigurationCustomField",
    "IotIndexingConfigurationThingIndexingConfigurationCustomFieldList",
    "IotIndexingConfigurationThingIndexingConfigurationCustomFieldOutputReference",
    "IotIndexingConfigurationThingIndexingConfigurationManagedField",
    "IotIndexingConfigurationThingIndexingConfigurationManagedFieldList",
    "IotIndexingConfigurationThingIndexingConfigurationManagedFieldOutputReference",
    "IotIndexingConfigurationThingIndexingConfigurationOutputReference",
]

publication.publish()
