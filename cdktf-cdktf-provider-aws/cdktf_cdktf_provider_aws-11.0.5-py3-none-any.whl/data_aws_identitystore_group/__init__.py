'''
# `data_aws_identitystore_group`

Refer to the Terraform Registory for docs: [`data_aws_identitystore_group`](https://www.terraform.io/docs/providers/aws/d/identitystore_group).
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


class DataAwsIdentitystoreGroup(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsIdentitystoreGroup.DataAwsIdentitystoreGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group aws_identitystore_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        identity_store_id: builtins.str,
        alternate_identifier: typing.Optional[typing.Union["DataAwsIdentitystoreGroupAlternateIdentifier", typing.Dict[str, typing.Any]]] = None,
        filter: typing.Optional[typing.Union["DataAwsIdentitystoreGroupFilter", typing.Dict[str, typing.Any]]] = None,
        group_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group aws_identitystore_group} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param identity_store_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#identity_store_id DataAwsIdentitystoreGroup#identity_store_id}.
        :param alternate_identifier: alternate_identifier block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#alternate_identifier DataAwsIdentitystoreGroup#alternate_identifier}
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#filter DataAwsIdentitystoreGroup#filter}
        :param group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#group_id DataAwsIdentitystoreGroup#group_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#id DataAwsIdentitystoreGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
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
                identity_store_id: builtins.str,
                alternate_identifier: typing.Optional[typing.Union[DataAwsIdentitystoreGroupAlternateIdentifier, typing.Dict[str, typing.Any]]] = None,
                filter: typing.Optional[typing.Union[DataAwsIdentitystoreGroupFilter, typing.Dict[str, typing.Any]]] = None,
                group_id: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
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
        config = DataAwsIdentitystoreGroupConfig(
            identity_store_id=identity_store_id,
            alternate_identifier=alternate_identifier,
            filter=filter,
            group_id=group_id,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAlternateIdentifier")
    def put_alternate_identifier(
        self,
        *,
        external_id: typing.Optional[typing.Union["DataAwsIdentitystoreGroupAlternateIdentifierExternalId", typing.Dict[str, typing.Any]]] = None,
        unique_attribute: typing.Optional[typing.Union["DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttribute", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param external_id: external_id block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#external_id DataAwsIdentitystoreGroup#external_id}
        :param unique_attribute: unique_attribute block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#unique_attribute DataAwsIdentitystoreGroup#unique_attribute}
        '''
        value = DataAwsIdentitystoreGroupAlternateIdentifier(
            external_id=external_id, unique_attribute=unique_attribute
        )

        return typing.cast(None, jsii.invoke(self, "putAlternateIdentifier", [value]))

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        *,
        attribute_path: builtins.str,
        attribute_value: builtins.str,
    ) -> None:
        '''
        :param attribute_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#attribute_path DataAwsIdentitystoreGroup#attribute_path}.
        :param attribute_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#attribute_value DataAwsIdentitystoreGroup#attribute_value}.
        '''
        value = DataAwsIdentitystoreGroupFilter(
            attribute_path=attribute_path, attribute_value=attribute_value
        )

        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="resetAlternateIdentifier")
    def reset_alternate_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlternateIdentifier", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetGroupId")
    def reset_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="alternateIdentifier")
    def alternate_identifier(
        self,
    ) -> "DataAwsIdentitystoreGroupAlternateIdentifierOutputReference":
        return typing.cast("DataAwsIdentitystoreGroupAlternateIdentifierOutputReference", jsii.get(self, "alternateIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @builtins.property
    @jsii.member(jsii_name="externalIds")
    def external_ids(self) -> "DataAwsIdentitystoreGroupExternalIdsList":
        return typing.cast("DataAwsIdentitystoreGroupExternalIdsList", jsii.get(self, "externalIds"))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> "DataAwsIdentitystoreGroupFilterOutputReference":
        return typing.cast("DataAwsIdentitystoreGroupFilterOutputReference", jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="alternateIdentifierInput")
    def alternate_identifier_input(
        self,
    ) -> typing.Optional["DataAwsIdentitystoreGroupAlternateIdentifier"]:
        return typing.cast(typing.Optional["DataAwsIdentitystoreGroupAlternateIdentifier"], jsii.get(self, "alternateIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional["DataAwsIdentitystoreGroupFilter"]:
        return typing.cast(typing.Optional["DataAwsIdentitystoreGroupFilter"], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="identityStoreIdInput")
    def identity_store_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityStoreIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

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
    @jsii.member(jsii_name="identityStoreId")
    def identity_store_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityStoreId"))

    @identity_store_id.setter
    def identity_store_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityStoreId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsIdentitystoreGroup.DataAwsIdentitystoreGroupAlternateIdentifier",
    jsii_struct_bases=[],
    name_mapping={"external_id": "externalId", "unique_attribute": "uniqueAttribute"},
)
class DataAwsIdentitystoreGroupAlternateIdentifier:
    def __init__(
        self,
        *,
        external_id: typing.Optional[typing.Union["DataAwsIdentitystoreGroupAlternateIdentifierExternalId", typing.Dict[str, typing.Any]]] = None,
        unique_attribute: typing.Optional[typing.Union["DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttribute", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param external_id: external_id block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#external_id DataAwsIdentitystoreGroup#external_id}
        :param unique_attribute: unique_attribute block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#unique_attribute DataAwsIdentitystoreGroup#unique_attribute}
        '''
        if isinstance(external_id, dict):
            external_id = DataAwsIdentitystoreGroupAlternateIdentifierExternalId(**external_id)
        if isinstance(unique_attribute, dict):
            unique_attribute = DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttribute(**unique_attribute)
        if __debug__:
            def stub(
                *,
                external_id: typing.Optional[typing.Union[DataAwsIdentitystoreGroupAlternateIdentifierExternalId, typing.Dict[str, typing.Any]]] = None,
                unique_attribute: typing.Optional[typing.Union[DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttribute, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            check_type(argname="argument unique_attribute", value=unique_attribute, expected_type=type_hints["unique_attribute"])
        self._values: typing.Dict[str, typing.Any] = {}
        if external_id is not None:
            self._values["external_id"] = external_id
        if unique_attribute is not None:
            self._values["unique_attribute"] = unique_attribute

    @builtins.property
    def external_id(
        self,
    ) -> typing.Optional["DataAwsIdentitystoreGroupAlternateIdentifierExternalId"]:
        '''external_id block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#external_id DataAwsIdentitystoreGroup#external_id}
        '''
        result = self._values.get("external_id")
        return typing.cast(typing.Optional["DataAwsIdentitystoreGroupAlternateIdentifierExternalId"], result)

    @builtins.property
    def unique_attribute(
        self,
    ) -> typing.Optional["DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttribute"]:
        '''unique_attribute block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#unique_attribute DataAwsIdentitystoreGroup#unique_attribute}
        '''
        result = self._values.get("unique_attribute")
        return typing.cast(typing.Optional["DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttribute"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsIdentitystoreGroupAlternateIdentifier(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsIdentitystoreGroup.DataAwsIdentitystoreGroupAlternateIdentifierExternalId",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "issuer": "issuer"},
)
class DataAwsIdentitystoreGroupAlternateIdentifierExternalId:
    def __init__(self, *, id: builtins.str, issuer: builtins.str) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#id DataAwsIdentitystoreGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#issuer DataAwsIdentitystoreGroup#issuer}.
        '''
        if __debug__:
            def stub(*, id: builtins.str, issuer: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
            "issuer": issuer,
        }

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#id DataAwsIdentitystoreGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def issuer(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#issuer DataAwsIdentitystoreGroup#issuer}.'''
        result = self._values.get("issuer")
        assert result is not None, "Required property 'issuer' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsIdentitystoreGroupAlternateIdentifierExternalId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsIdentitystoreGroupAlternateIdentifierExternalIdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsIdentitystoreGroup.DataAwsIdentitystoreGroupAlternateIdentifierExternalIdOutputReference",
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
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

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
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsIdentitystoreGroupAlternateIdentifierExternalId]:
        return typing.cast(typing.Optional[DataAwsIdentitystoreGroupAlternateIdentifierExternalId], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsIdentitystoreGroupAlternateIdentifierExternalId],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[DataAwsIdentitystoreGroupAlternateIdentifierExternalId],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataAwsIdentitystoreGroupAlternateIdentifierOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsIdentitystoreGroup.DataAwsIdentitystoreGroupAlternateIdentifierOutputReference",
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

    @jsii.member(jsii_name="putExternalId")
    def put_external_id(self, *, id: builtins.str, issuer: builtins.str) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#id DataAwsIdentitystoreGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#issuer DataAwsIdentitystoreGroup#issuer}.
        '''
        value = DataAwsIdentitystoreGroupAlternateIdentifierExternalId(
            id=id, issuer=issuer
        )

        return typing.cast(None, jsii.invoke(self, "putExternalId", [value]))

    @jsii.member(jsii_name="putUniqueAttribute")
    def put_unique_attribute(
        self,
        *,
        attribute_path: builtins.str,
        attribute_value: builtins.str,
    ) -> None:
        '''
        :param attribute_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#attribute_path DataAwsIdentitystoreGroup#attribute_path}.
        :param attribute_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#attribute_value DataAwsIdentitystoreGroup#attribute_value}.
        '''
        value = DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttribute(
            attribute_path=attribute_path, attribute_value=attribute_value
        )

        return typing.cast(None, jsii.invoke(self, "putUniqueAttribute", [value]))

    @jsii.member(jsii_name="resetExternalId")
    def reset_external_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalId", []))

    @jsii.member(jsii_name="resetUniqueAttribute")
    def reset_unique_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUniqueAttribute", []))

    @builtins.property
    @jsii.member(jsii_name="externalId")
    def external_id(
        self,
    ) -> DataAwsIdentitystoreGroupAlternateIdentifierExternalIdOutputReference:
        return typing.cast(DataAwsIdentitystoreGroupAlternateIdentifierExternalIdOutputReference, jsii.get(self, "externalId"))

    @builtins.property
    @jsii.member(jsii_name="uniqueAttribute")
    def unique_attribute(
        self,
    ) -> "DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttributeOutputReference":
        return typing.cast("DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttributeOutputReference", jsii.get(self, "uniqueAttribute"))

    @builtins.property
    @jsii.member(jsii_name="externalIdInput")
    def external_id_input(
        self,
    ) -> typing.Optional[DataAwsIdentitystoreGroupAlternateIdentifierExternalId]:
        return typing.cast(typing.Optional[DataAwsIdentitystoreGroupAlternateIdentifierExternalId], jsii.get(self, "externalIdInput"))

    @builtins.property
    @jsii.member(jsii_name="uniqueAttributeInput")
    def unique_attribute_input(
        self,
    ) -> typing.Optional["DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttribute"]:
        return typing.cast(typing.Optional["DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttribute"], jsii.get(self, "uniqueAttributeInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsIdentitystoreGroupAlternateIdentifier]:
        return typing.cast(typing.Optional[DataAwsIdentitystoreGroupAlternateIdentifier], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsIdentitystoreGroupAlternateIdentifier],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[DataAwsIdentitystoreGroupAlternateIdentifier],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsIdentitystoreGroup.DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttribute",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_path": "attributePath",
        "attribute_value": "attributeValue",
    },
)
class DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttribute:
    def __init__(
        self,
        *,
        attribute_path: builtins.str,
        attribute_value: builtins.str,
    ) -> None:
        '''
        :param attribute_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#attribute_path DataAwsIdentitystoreGroup#attribute_path}.
        :param attribute_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#attribute_value DataAwsIdentitystoreGroup#attribute_value}.
        '''
        if __debug__:
            def stub(
                *,
                attribute_path: builtins.str,
                attribute_value: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument attribute_path", value=attribute_path, expected_type=type_hints["attribute_path"])
            check_type(argname="argument attribute_value", value=attribute_value, expected_type=type_hints["attribute_value"])
        self._values: typing.Dict[str, typing.Any] = {
            "attribute_path": attribute_path,
            "attribute_value": attribute_value,
        }

    @builtins.property
    def attribute_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#attribute_path DataAwsIdentitystoreGroup#attribute_path}.'''
        result = self._values.get("attribute_path")
        assert result is not None, "Required property 'attribute_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attribute_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#attribute_value DataAwsIdentitystoreGroup#attribute_value}.'''
        result = self._values.get("attribute_value")
        assert result is not None, "Required property 'attribute_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttribute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttributeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsIdentitystoreGroup.DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttributeOutputReference",
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
    @jsii.member(jsii_name="attributePathInput")
    def attribute_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributePathInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeValueInput")
    def attribute_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeValueInput"))

    @builtins.property
    @jsii.member(jsii_name="attributePath")
    def attribute_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributePath"))

    @attribute_path.setter
    def attribute_path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributePath", value)

    @builtins.property
    @jsii.member(jsii_name="attributeValue")
    def attribute_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeValue"))

    @attribute_value.setter
    def attribute_value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttribute]:
        return typing.cast(typing.Optional[DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttribute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttribute],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttribute],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsIdentitystoreGroup.DataAwsIdentitystoreGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "identity_store_id": "identityStoreId",
        "alternate_identifier": "alternateIdentifier",
        "filter": "filter",
        "group_id": "groupId",
        "id": "id",
    },
)
class DataAwsIdentitystoreGroupConfig(cdktf.TerraformMetaArguments):
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
        identity_store_id: builtins.str,
        alternate_identifier: typing.Optional[typing.Union[DataAwsIdentitystoreGroupAlternateIdentifier, typing.Dict[str, typing.Any]]] = None,
        filter: typing.Optional[typing.Union["DataAwsIdentitystoreGroupFilter", typing.Dict[str, typing.Any]]] = None,
        group_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param identity_store_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#identity_store_id DataAwsIdentitystoreGroup#identity_store_id}.
        :param alternate_identifier: alternate_identifier block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#alternate_identifier DataAwsIdentitystoreGroup#alternate_identifier}
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#filter DataAwsIdentitystoreGroup#filter}
        :param group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#group_id DataAwsIdentitystoreGroup#group_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#id DataAwsIdentitystoreGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(alternate_identifier, dict):
            alternate_identifier = DataAwsIdentitystoreGroupAlternateIdentifier(**alternate_identifier)
        if isinstance(filter, dict):
            filter = DataAwsIdentitystoreGroupFilter(**filter)
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
                identity_store_id: builtins.str,
                alternate_identifier: typing.Optional[typing.Union[DataAwsIdentitystoreGroupAlternateIdentifier, typing.Dict[str, typing.Any]]] = None,
                filter: typing.Optional[typing.Union[DataAwsIdentitystoreGroupFilter, typing.Dict[str, typing.Any]]] = None,
                group_id: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument identity_store_id", value=identity_store_id, expected_type=type_hints["identity_store_id"])
            check_type(argname="argument alternate_identifier", value=alternate_identifier, expected_type=type_hints["alternate_identifier"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "identity_store_id": identity_store_id,
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
        if alternate_identifier is not None:
            self._values["alternate_identifier"] = alternate_identifier
        if filter is not None:
            self._values["filter"] = filter
        if group_id is not None:
            self._values["group_id"] = group_id
        if id is not None:
            self._values["id"] = id

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
    def identity_store_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#identity_store_id DataAwsIdentitystoreGroup#identity_store_id}.'''
        result = self._values.get("identity_store_id")
        assert result is not None, "Required property 'identity_store_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alternate_identifier(
        self,
    ) -> typing.Optional[DataAwsIdentitystoreGroupAlternateIdentifier]:
        '''alternate_identifier block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#alternate_identifier DataAwsIdentitystoreGroup#alternate_identifier}
        '''
        result = self._values.get("alternate_identifier")
        return typing.cast(typing.Optional[DataAwsIdentitystoreGroupAlternateIdentifier], result)

    @builtins.property
    def filter(self) -> typing.Optional["DataAwsIdentitystoreGroupFilter"]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#filter DataAwsIdentitystoreGroup#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional["DataAwsIdentitystoreGroupFilter"], result)

    @builtins.property
    def group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#group_id DataAwsIdentitystoreGroup#group_id}.'''
        result = self._values.get("group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#id DataAwsIdentitystoreGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsIdentitystoreGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsIdentitystoreGroup.DataAwsIdentitystoreGroupExternalIds",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsIdentitystoreGroupExternalIds:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsIdentitystoreGroupExternalIds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsIdentitystoreGroupExternalIdsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsIdentitystoreGroup.DataAwsIdentitystoreGroupExternalIdsList",
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
    ) -> "DataAwsIdentitystoreGroupExternalIdsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsIdentitystoreGroupExternalIdsOutputReference", jsii.invoke(self, "get", [index]))

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


class DataAwsIdentitystoreGroupExternalIdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsIdentitystoreGroup.DataAwsIdentitystoreGroupExternalIdsOutputReference",
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
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsIdentitystoreGroupExternalIds]:
        return typing.cast(typing.Optional[DataAwsIdentitystoreGroupExternalIds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsIdentitystoreGroupExternalIds],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[DataAwsIdentitystoreGroupExternalIds],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.dataAwsIdentitystoreGroup.DataAwsIdentitystoreGroupFilter",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_path": "attributePath",
        "attribute_value": "attributeValue",
    },
)
class DataAwsIdentitystoreGroupFilter:
    def __init__(
        self,
        *,
        attribute_path: builtins.str,
        attribute_value: builtins.str,
    ) -> None:
        '''
        :param attribute_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#attribute_path DataAwsIdentitystoreGroup#attribute_path}.
        :param attribute_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#attribute_value DataAwsIdentitystoreGroup#attribute_value}.
        '''
        if __debug__:
            def stub(
                *,
                attribute_path: builtins.str,
                attribute_value: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument attribute_path", value=attribute_path, expected_type=type_hints["attribute_path"])
            check_type(argname="argument attribute_value", value=attribute_value, expected_type=type_hints["attribute_value"])
        self._values: typing.Dict[str, typing.Any] = {
            "attribute_path": attribute_path,
            "attribute_value": attribute_value,
        }

    @builtins.property
    def attribute_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#attribute_path DataAwsIdentitystoreGroup#attribute_path}.'''
        result = self._values.get("attribute_path")
        assert result is not None, "Required property 'attribute_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attribute_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/d/identitystore_group#attribute_value DataAwsIdentitystoreGroup#attribute_value}.'''
        result = self._values.get("attribute_value")
        assert result is not None, "Required property 'attribute_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsIdentitystoreGroupFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsIdentitystoreGroupFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.dataAwsIdentitystoreGroup.DataAwsIdentitystoreGroupFilterOutputReference",
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
    @jsii.member(jsii_name="attributePathInput")
    def attribute_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributePathInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeValueInput")
    def attribute_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeValueInput"))

    @builtins.property
    @jsii.member(jsii_name="attributePath")
    def attribute_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributePath"))

    @attribute_path.setter
    def attribute_path(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributePath", value)

    @builtins.property
    @jsii.member(jsii_name="attributeValue")
    def attribute_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeValue"))

    @attribute_value.setter
    def attribute_value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsIdentitystoreGroupFilter]:
        return typing.cast(typing.Optional[DataAwsIdentitystoreGroupFilter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsIdentitystoreGroupFilter],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[DataAwsIdentitystoreGroupFilter]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAwsIdentitystoreGroup",
    "DataAwsIdentitystoreGroupAlternateIdentifier",
    "DataAwsIdentitystoreGroupAlternateIdentifierExternalId",
    "DataAwsIdentitystoreGroupAlternateIdentifierExternalIdOutputReference",
    "DataAwsIdentitystoreGroupAlternateIdentifierOutputReference",
    "DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttribute",
    "DataAwsIdentitystoreGroupAlternateIdentifierUniqueAttributeOutputReference",
    "DataAwsIdentitystoreGroupConfig",
    "DataAwsIdentitystoreGroupExternalIds",
    "DataAwsIdentitystoreGroupExternalIdsList",
    "DataAwsIdentitystoreGroupExternalIdsOutputReference",
    "DataAwsIdentitystoreGroupFilter",
    "DataAwsIdentitystoreGroupFilterOutputReference",
]

publication.publish()
