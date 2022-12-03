'''
# `aws_glue_catalog_database`

Refer to the Terraform Registory for docs: [`aws_glue_catalog_database`](https://www.terraform.io/docs/providers/aws/r/glue_catalog_database).
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


class GlueCatalogDatabase(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCatalogDatabase.GlueCatalogDatabase",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database aws_glue_catalog_database}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        create_table_default_permission: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCatalogDatabaseCreateTableDefaultPermission", typing.Dict[str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        location_uri: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target_database: typing.Optional[typing.Union["GlueCatalogDatabaseTargetDatabase", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database aws_glue_catalog_database} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#name GlueCatalogDatabase#name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#catalog_id GlueCatalogDatabase#catalog_id}.
        :param create_table_default_permission: create_table_default_permission block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#create_table_default_permission GlueCatalogDatabase#create_table_default_permission}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#description GlueCatalogDatabase#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#id GlueCatalogDatabase#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#location_uri GlueCatalogDatabase#location_uri}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#parameters GlueCatalogDatabase#parameters}.
        :param target_database: target_database block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#target_database GlueCatalogDatabase#target_database}
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
                catalog_id: typing.Optional[builtins.str] = None,
                create_table_default_permission: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCatalogDatabaseCreateTableDefaultPermission, typing.Dict[str, typing.Any]]]]] = None,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                location_uri: typing.Optional[builtins.str] = None,
                parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                target_database: typing.Optional[typing.Union[GlueCatalogDatabaseTargetDatabase, typing.Dict[str, typing.Any]]] = None,
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
        config = GlueCatalogDatabaseConfig(
            name=name,
            catalog_id=catalog_id,
            create_table_default_permission=create_table_default_permission,
            description=description,
            id=id,
            location_uri=location_uri,
            parameters=parameters,
            target_database=target_database,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCreateTableDefaultPermission")
    def put_create_table_default_permission(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCatalogDatabaseCreateTableDefaultPermission", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCatalogDatabaseCreateTableDefaultPermission, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCreateTableDefaultPermission", [value]))

    @jsii.member(jsii_name="putTargetDatabase")
    def put_target_database(
        self,
        *,
        catalog_id: builtins.str,
        database_name: builtins.str,
    ) -> None:
        '''
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#catalog_id GlueCatalogDatabase#catalog_id}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#database_name GlueCatalogDatabase#database_name}.
        '''
        value = GlueCatalogDatabaseTargetDatabase(
            catalog_id=catalog_id, database_name=database_name
        )

        return typing.cast(None, jsii.invoke(self, "putTargetDatabase", [value]))

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @jsii.member(jsii_name="resetCreateTableDefaultPermission")
    def reset_create_table_default_permission(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateTableDefaultPermission", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocationUri")
    def reset_location_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocationUri", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetTargetDatabase")
    def reset_target_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetDatabase", []))

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
    @jsii.member(jsii_name="createTableDefaultPermission")
    def create_table_default_permission(
        self,
    ) -> "GlueCatalogDatabaseCreateTableDefaultPermissionList":
        return typing.cast("GlueCatalogDatabaseCreateTableDefaultPermissionList", jsii.get(self, "createTableDefaultPermission"))

    @builtins.property
    @jsii.member(jsii_name="targetDatabase")
    def target_database(self) -> "GlueCatalogDatabaseTargetDatabaseOutputReference":
        return typing.cast("GlueCatalogDatabaseTargetDatabaseOutputReference", jsii.get(self, "targetDatabase"))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="createTableDefaultPermissionInput")
    def create_table_default_permission_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCatalogDatabaseCreateTableDefaultPermission"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCatalogDatabaseCreateTableDefaultPermission"]]], jsii.get(self, "createTableDefaultPermissionInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationUriInput")
    def location_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationUriInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="targetDatabaseInput")
    def target_database_input(
        self,
    ) -> typing.Optional["GlueCatalogDatabaseTargetDatabase"]:
        return typing.cast(typing.Optional["GlueCatalogDatabaseTargetDatabase"], jsii.get(self, "targetDatabaseInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

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
    @jsii.member(jsii_name="locationUri")
    def location_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locationUri"))

    @location_uri.setter
    def location_uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationUri", value)

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


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueCatalogDatabase.GlueCatalogDatabaseConfig",
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
        "catalog_id": "catalogId",
        "create_table_default_permission": "createTableDefaultPermission",
        "description": "description",
        "id": "id",
        "location_uri": "locationUri",
        "parameters": "parameters",
        "target_database": "targetDatabase",
    },
)
class GlueCatalogDatabaseConfig(cdktf.TerraformMetaArguments):
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
        catalog_id: typing.Optional[builtins.str] = None,
        create_table_default_permission: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GlueCatalogDatabaseCreateTableDefaultPermission", typing.Dict[str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        location_uri: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target_database: typing.Optional[typing.Union["GlueCatalogDatabaseTargetDatabase", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#name GlueCatalogDatabase#name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#catalog_id GlueCatalogDatabase#catalog_id}.
        :param create_table_default_permission: create_table_default_permission block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#create_table_default_permission GlueCatalogDatabase#create_table_default_permission}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#description GlueCatalogDatabase#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#id GlueCatalogDatabase#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#location_uri GlueCatalogDatabase#location_uri}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#parameters GlueCatalogDatabase#parameters}.
        :param target_database: target_database block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#target_database GlueCatalogDatabase#target_database}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(target_database, dict):
            target_database = GlueCatalogDatabaseTargetDatabase(**target_database)
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
                catalog_id: typing.Optional[builtins.str] = None,
                create_table_default_permission: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GlueCatalogDatabaseCreateTableDefaultPermission, typing.Dict[str, typing.Any]]]]] = None,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                location_uri: typing.Optional[builtins.str] = None,
                parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                target_database: typing.Optional[typing.Union[GlueCatalogDatabaseTargetDatabase, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument create_table_default_permission", value=create_table_default_permission, expected_type=type_hints["create_table_default_permission"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument location_uri", value=location_uri, expected_type=type_hints["location_uri"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument target_database", value=target_database, expected_type=type_hints["target_database"])
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
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id
        if create_table_default_permission is not None:
            self._values["create_table_default_permission"] = create_table_default_permission
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if location_uri is not None:
            self._values["location_uri"] = location_uri
        if parameters is not None:
            self._values["parameters"] = parameters
        if target_database is not None:
            self._values["target_database"] = target_database

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#name GlueCatalogDatabase#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#catalog_id GlueCatalogDatabase#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def create_table_default_permission(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCatalogDatabaseCreateTableDefaultPermission"]]]:
        '''create_table_default_permission block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#create_table_default_permission GlueCatalogDatabase#create_table_default_permission}
        '''
        result = self._values.get("create_table_default_permission")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GlueCatalogDatabaseCreateTableDefaultPermission"]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#description GlueCatalogDatabase#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#id GlueCatalogDatabase#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#location_uri GlueCatalogDatabase#location_uri}.'''
        result = self._values.get("location_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#parameters GlueCatalogDatabase#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def target_database(self) -> typing.Optional["GlueCatalogDatabaseTargetDatabase"]:
        '''target_database block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#target_database GlueCatalogDatabase#target_database}
        '''
        result = self._values.get("target_database")
        return typing.cast(typing.Optional["GlueCatalogDatabaseTargetDatabase"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCatalogDatabaseConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueCatalogDatabase.GlueCatalogDatabaseCreateTableDefaultPermission",
    jsii_struct_bases=[],
    name_mapping={"permissions": "permissions", "principal": "principal"},
)
class GlueCatalogDatabaseCreateTableDefaultPermission:
    def __init__(
        self,
        *,
        permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        principal: typing.Optional[typing.Union["GlueCatalogDatabaseCreateTableDefaultPermissionPrincipal", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param permissions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#permissions GlueCatalogDatabase#permissions}.
        :param principal: principal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#principal GlueCatalogDatabase#principal}
        '''
        if isinstance(principal, dict):
            principal = GlueCatalogDatabaseCreateTableDefaultPermissionPrincipal(**principal)
        if __debug__:
            def stub(
                *,
                permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
                principal: typing.Optional[typing.Union[GlueCatalogDatabaseCreateTableDefaultPermissionPrincipal, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
        self._values: typing.Dict[str, typing.Any] = {}
        if permissions is not None:
            self._values["permissions"] = permissions
        if principal is not None:
            self._values["principal"] = principal

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#permissions GlueCatalogDatabase#permissions}.'''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def principal(
        self,
    ) -> typing.Optional["GlueCatalogDatabaseCreateTableDefaultPermissionPrincipal"]:
        '''principal block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#principal GlueCatalogDatabase#principal}
        '''
        result = self._values.get("principal")
        return typing.cast(typing.Optional["GlueCatalogDatabaseCreateTableDefaultPermissionPrincipal"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCatalogDatabaseCreateTableDefaultPermission(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCatalogDatabaseCreateTableDefaultPermissionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCatalogDatabase.GlueCatalogDatabaseCreateTableDefaultPermissionList",
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
    ) -> "GlueCatalogDatabaseCreateTableDefaultPermissionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GlueCatalogDatabaseCreateTableDefaultPermissionOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCatalogDatabaseCreateTableDefaultPermission]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCatalogDatabaseCreateTableDefaultPermission]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCatalogDatabaseCreateTableDefaultPermission]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GlueCatalogDatabaseCreateTableDefaultPermission]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GlueCatalogDatabaseCreateTableDefaultPermissionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCatalogDatabase.GlueCatalogDatabaseCreateTableDefaultPermissionOutputReference",
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

    @jsii.member(jsii_name="putPrincipal")
    def put_principal(
        self,
        *,
        data_lake_principal_identifier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param data_lake_principal_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#data_lake_principal_identifier GlueCatalogDatabase#data_lake_principal_identifier}.
        '''
        value = GlueCatalogDatabaseCreateTableDefaultPermissionPrincipal(
            data_lake_principal_identifier=data_lake_principal_identifier
        )

        return typing.cast(None, jsii.invoke(self, "putPrincipal", [value]))

    @jsii.member(jsii_name="resetPermissions")
    def reset_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermissions", []))

    @jsii.member(jsii_name="resetPrincipal")
    def reset_principal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrincipal", []))

    @builtins.property
    @jsii.member(jsii_name="principal")
    def principal(
        self,
    ) -> "GlueCatalogDatabaseCreateTableDefaultPermissionPrincipalOutputReference":
        return typing.cast("GlueCatalogDatabaseCreateTableDefaultPermissionPrincipalOutputReference", jsii.get(self, "principal"))

    @builtins.property
    @jsii.member(jsii_name="permissionsInput")
    def permissions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="principalInput")
    def principal_input(
        self,
    ) -> typing.Optional["GlueCatalogDatabaseCreateTableDefaultPermissionPrincipal"]:
        return typing.cast(typing.Optional["GlueCatalogDatabaseCreateTableDefaultPermissionPrincipal"], jsii.get(self, "principalInput"))

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GlueCatalogDatabaseCreateTableDefaultPermission, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GlueCatalogDatabaseCreateTableDefaultPermission, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GlueCatalogDatabaseCreateTableDefaultPermission, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[GlueCatalogDatabaseCreateTableDefaultPermission, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueCatalogDatabase.GlueCatalogDatabaseCreateTableDefaultPermissionPrincipal",
    jsii_struct_bases=[],
    name_mapping={"data_lake_principal_identifier": "dataLakePrincipalIdentifier"},
)
class GlueCatalogDatabaseCreateTableDefaultPermissionPrincipal:
    def __init__(
        self,
        *,
        data_lake_principal_identifier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param data_lake_principal_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#data_lake_principal_identifier GlueCatalogDatabase#data_lake_principal_identifier}.
        '''
        if __debug__:
            def stub(
                *,
                data_lake_principal_identifier: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument data_lake_principal_identifier", value=data_lake_principal_identifier, expected_type=type_hints["data_lake_principal_identifier"])
        self._values: typing.Dict[str, typing.Any] = {}
        if data_lake_principal_identifier is not None:
            self._values["data_lake_principal_identifier"] = data_lake_principal_identifier

    @builtins.property
    def data_lake_principal_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#data_lake_principal_identifier GlueCatalogDatabase#data_lake_principal_identifier}.'''
        result = self._values.get("data_lake_principal_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCatalogDatabaseCreateTableDefaultPermissionPrincipal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCatalogDatabaseCreateTableDefaultPermissionPrincipalOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCatalogDatabase.GlueCatalogDatabaseCreateTableDefaultPermissionPrincipalOutputReference",
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

    @jsii.member(jsii_name="resetDataLakePrincipalIdentifier")
    def reset_data_lake_principal_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataLakePrincipalIdentifier", []))

    @builtins.property
    @jsii.member(jsii_name="dataLakePrincipalIdentifierInput")
    def data_lake_principal_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataLakePrincipalIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="dataLakePrincipalIdentifier")
    def data_lake_principal_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataLakePrincipalIdentifier"))

    @data_lake_principal_identifier.setter
    def data_lake_principal_identifier(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataLakePrincipalIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GlueCatalogDatabaseCreateTableDefaultPermissionPrincipal]:
        return typing.cast(typing.Optional[GlueCatalogDatabaseCreateTableDefaultPermissionPrincipal], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueCatalogDatabaseCreateTableDefaultPermissionPrincipal],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[GlueCatalogDatabaseCreateTableDefaultPermissionPrincipal],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.glueCatalogDatabase.GlueCatalogDatabaseTargetDatabase",
    jsii_struct_bases=[],
    name_mapping={"catalog_id": "catalogId", "database_name": "databaseName"},
)
class GlueCatalogDatabaseTargetDatabase:
    def __init__(
        self,
        *,
        catalog_id: builtins.str,
        database_name: builtins.str,
    ) -> None:
        '''
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#catalog_id GlueCatalogDatabase#catalog_id}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#database_name GlueCatalogDatabase#database_name}.
        '''
        if __debug__:
            def stub(*, catalog_id: builtins.str, database_name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "catalog_id": catalog_id,
            "database_name": database_name,
        }

    @builtins.property
    def catalog_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#catalog_id GlueCatalogDatabase#catalog_id}.'''
        result = self._values.get("catalog_id")
        assert result is not None, "Required property 'catalog_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/glue_catalog_database#database_name GlueCatalogDatabase#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlueCatalogDatabaseTargetDatabase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GlueCatalogDatabaseTargetDatabaseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.glueCatalogDatabase.GlueCatalogDatabaseTargetDatabaseOutputReference",
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
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogId")
    def catalog_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogId"))

    @catalog_id.setter
    def catalog_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogId", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GlueCatalogDatabaseTargetDatabase]:
        return typing.cast(typing.Optional[GlueCatalogDatabaseTargetDatabase], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GlueCatalogDatabaseTargetDatabase],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[GlueCatalogDatabaseTargetDatabase]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GlueCatalogDatabase",
    "GlueCatalogDatabaseConfig",
    "GlueCatalogDatabaseCreateTableDefaultPermission",
    "GlueCatalogDatabaseCreateTableDefaultPermissionList",
    "GlueCatalogDatabaseCreateTableDefaultPermissionOutputReference",
    "GlueCatalogDatabaseCreateTableDefaultPermissionPrincipal",
    "GlueCatalogDatabaseCreateTableDefaultPermissionPrincipalOutputReference",
    "GlueCatalogDatabaseTargetDatabase",
    "GlueCatalogDatabaseTargetDatabaseOutputReference",
]

publication.publish()
