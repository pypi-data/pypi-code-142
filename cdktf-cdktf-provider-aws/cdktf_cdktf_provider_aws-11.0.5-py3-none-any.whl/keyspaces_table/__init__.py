'''
# `aws_keyspaces_table`

Refer to the Terraform Registory for docs: [`aws_keyspaces_table`](https://www.terraform.io/docs/providers/aws/r/keyspaces_table).
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


class KeyspacesTable(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTable",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table aws_keyspaces_table}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        keyspace_name: builtins.str,
        schema_definition: typing.Union["KeyspacesTableSchemaDefinition", typing.Dict[str, typing.Any]],
        table_name: builtins.str,
        capacity_specification: typing.Optional[typing.Union["KeyspacesTableCapacitySpecification", typing.Dict[str, typing.Any]]] = None,
        comment: typing.Optional[typing.Union["KeyspacesTableComment", typing.Dict[str, typing.Any]]] = None,
        default_time_to_live: typing.Optional[jsii.Number] = None,
        encryption_specification: typing.Optional[typing.Union["KeyspacesTableEncryptionSpecification", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        point_in_time_recovery: typing.Optional[typing.Union["KeyspacesTablePointInTimeRecovery", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KeyspacesTableTimeouts", typing.Dict[str, typing.Any]]] = None,
        ttl: typing.Optional[typing.Union["KeyspacesTableTtl", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table aws_keyspaces_table} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param keyspace_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#keyspace_name KeyspacesTable#keyspace_name}.
        :param schema_definition: schema_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#schema_definition KeyspacesTable#schema_definition}
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#table_name KeyspacesTable#table_name}.
        :param capacity_specification: capacity_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#capacity_specification KeyspacesTable#capacity_specification}
        :param comment: comment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#comment KeyspacesTable#comment}
        :param default_time_to_live: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#default_time_to_live KeyspacesTable#default_time_to_live}.
        :param encryption_specification: encryption_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#encryption_specification KeyspacesTable#encryption_specification}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#id KeyspacesTable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param point_in_time_recovery: point_in_time_recovery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#point_in_time_recovery KeyspacesTable#point_in_time_recovery}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#tags KeyspacesTable#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#tags_all KeyspacesTable#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#timeouts KeyspacesTable#timeouts}
        :param ttl: ttl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#ttl KeyspacesTable#ttl}
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
                keyspace_name: builtins.str,
                schema_definition: typing.Union[KeyspacesTableSchemaDefinition, typing.Dict[str, typing.Any]],
                table_name: builtins.str,
                capacity_specification: typing.Optional[typing.Union[KeyspacesTableCapacitySpecification, typing.Dict[str, typing.Any]]] = None,
                comment: typing.Optional[typing.Union[KeyspacesTableComment, typing.Dict[str, typing.Any]]] = None,
                default_time_to_live: typing.Optional[jsii.Number] = None,
                encryption_specification: typing.Optional[typing.Union[KeyspacesTableEncryptionSpecification, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                point_in_time_recovery: typing.Optional[typing.Union[KeyspacesTablePointInTimeRecovery, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[KeyspacesTableTimeouts, typing.Dict[str, typing.Any]]] = None,
                ttl: typing.Optional[typing.Union[KeyspacesTableTtl, typing.Dict[str, typing.Any]]] = None,
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
        config = KeyspacesTableConfig(
            keyspace_name=keyspace_name,
            schema_definition=schema_definition,
            table_name=table_name,
            capacity_specification=capacity_specification,
            comment=comment,
            default_time_to_live=default_time_to_live,
            encryption_specification=encryption_specification,
            id=id,
            point_in_time_recovery=point_in_time_recovery,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            ttl=ttl,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCapacitySpecification")
    def put_capacity_specification(
        self,
        *,
        read_capacity_units: typing.Optional[jsii.Number] = None,
        throughput_mode: typing.Optional[builtins.str] = None,
        write_capacity_units: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param read_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#read_capacity_units KeyspacesTable#read_capacity_units}.
        :param throughput_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#throughput_mode KeyspacesTable#throughput_mode}.
        :param write_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#write_capacity_units KeyspacesTable#write_capacity_units}.
        '''
        value = KeyspacesTableCapacitySpecification(
            read_capacity_units=read_capacity_units,
            throughput_mode=throughput_mode,
            write_capacity_units=write_capacity_units,
        )

        return typing.cast(None, jsii.invoke(self, "putCapacitySpecification", [value]))

    @jsii.member(jsii_name="putComment")
    def put_comment(self, *, message: typing.Optional[builtins.str] = None) -> None:
        '''
        :param message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#message KeyspacesTable#message}.
        '''
        value = KeyspacesTableComment(message=message)

        return typing.cast(None, jsii.invoke(self, "putComment", [value]))

    @jsii.member(jsii_name="putEncryptionSpecification")
    def put_encryption_specification(
        self,
        *,
        kms_key_identifier: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kms_key_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#kms_key_identifier KeyspacesTable#kms_key_identifier}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#type KeyspacesTable#type}.
        '''
        value = KeyspacesTableEncryptionSpecification(
            kms_key_identifier=kms_key_identifier, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putEncryptionSpecification", [value]))

    @jsii.member(jsii_name="putPointInTimeRecovery")
    def put_point_in_time_recovery(
        self,
        *,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#status KeyspacesTable#status}.
        '''
        value = KeyspacesTablePointInTimeRecovery(status=status)

        return typing.cast(None, jsii.invoke(self, "putPointInTimeRecovery", [value]))

    @jsii.member(jsii_name="putSchemaDefinition")
    def put_schema_definition(
        self,
        *,
        column: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionColumn", typing.Dict[str, typing.Any]]]],
        partition_key: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionPartitionKey", typing.Dict[str, typing.Any]]]],
        clustering_key: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionClusteringKey", typing.Dict[str, typing.Any]]]]] = None,
        static_column: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionStaticColumn", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param column: column block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#column KeyspacesTable#column}
        :param partition_key: partition_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#partition_key KeyspacesTable#partition_key}
        :param clustering_key: clustering_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#clustering_key KeyspacesTable#clustering_key}
        :param static_column: static_column block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#static_column KeyspacesTable#static_column}
        '''
        value = KeyspacesTableSchemaDefinition(
            column=column,
            partition_key=partition_key,
            clustering_key=clustering_key,
            static_column=static_column,
        )

        return typing.cast(None, jsii.invoke(self, "putSchemaDefinition", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#create KeyspacesTable#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#delete KeyspacesTable#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#update KeyspacesTable#update}.
        '''
        value = KeyspacesTableTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTtl")
    def put_ttl(self, *, status: builtins.str) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#status KeyspacesTable#status}.
        '''
        value = KeyspacesTableTtl(status=status)

        return typing.cast(None, jsii.invoke(self, "putTtl", [value]))

    @jsii.member(jsii_name="resetCapacitySpecification")
    def reset_capacity_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacitySpecification", []))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetDefaultTimeToLive")
    def reset_default_time_to_live(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultTimeToLive", []))

    @jsii.member(jsii_name="resetEncryptionSpecification")
    def reset_encryption_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionSpecification", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPointInTimeRecovery")
    def reset_point_in_time_recovery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPointInTimeRecovery", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

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
    @jsii.member(jsii_name="capacitySpecification")
    def capacity_specification(
        self,
    ) -> "KeyspacesTableCapacitySpecificationOutputReference":
        return typing.cast("KeyspacesTableCapacitySpecificationOutputReference", jsii.get(self, "capacitySpecification"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> "KeyspacesTableCommentOutputReference":
        return typing.cast("KeyspacesTableCommentOutputReference", jsii.get(self, "comment"))

    @builtins.property
    @jsii.member(jsii_name="encryptionSpecification")
    def encryption_specification(
        self,
    ) -> "KeyspacesTableEncryptionSpecificationOutputReference":
        return typing.cast("KeyspacesTableEncryptionSpecificationOutputReference", jsii.get(self, "encryptionSpecification"))

    @builtins.property
    @jsii.member(jsii_name="pointInTimeRecovery")
    def point_in_time_recovery(
        self,
    ) -> "KeyspacesTablePointInTimeRecoveryOutputReference":
        return typing.cast("KeyspacesTablePointInTimeRecoveryOutputReference", jsii.get(self, "pointInTimeRecovery"))

    @builtins.property
    @jsii.member(jsii_name="schemaDefinition")
    def schema_definition(self) -> "KeyspacesTableSchemaDefinitionOutputReference":
        return typing.cast("KeyspacesTableSchemaDefinitionOutputReference", jsii.get(self, "schemaDefinition"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "KeyspacesTableTimeoutsOutputReference":
        return typing.cast("KeyspacesTableTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> "KeyspacesTableTtlOutputReference":
        return typing.cast("KeyspacesTableTtlOutputReference", jsii.get(self, "ttl"))

    @builtins.property
    @jsii.member(jsii_name="capacitySpecificationInput")
    def capacity_specification_input(
        self,
    ) -> typing.Optional["KeyspacesTableCapacitySpecification"]:
        return typing.cast(typing.Optional["KeyspacesTableCapacitySpecification"], jsii.get(self, "capacitySpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional["KeyspacesTableComment"]:
        return typing.cast(typing.Optional["KeyspacesTableComment"], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTimeToLiveInput")
    def default_time_to_live_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultTimeToLiveInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionSpecificationInput")
    def encryption_specification_input(
        self,
    ) -> typing.Optional["KeyspacesTableEncryptionSpecification"]:
        return typing.cast(typing.Optional["KeyspacesTableEncryptionSpecification"], jsii.get(self, "encryptionSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="keyspaceNameInput")
    def keyspace_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyspaceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="pointInTimeRecoveryInput")
    def point_in_time_recovery_input(
        self,
    ) -> typing.Optional["KeyspacesTablePointInTimeRecovery"]:
        return typing.cast(typing.Optional["KeyspacesTablePointInTimeRecovery"], jsii.get(self, "pointInTimeRecoveryInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaDefinitionInput")
    def schema_definition_input(
        self,
    ) -> typing.Optional["KeyspacesTableSchemaDefinition"]:
        return typing.cast(typing.Optional["KeyspacesTableSchemaDefinition"], jsii.get(self, "schemaDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

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
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["KeyspacesTableTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["KeyspacesTableTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional["KeyspacesTableTtl"]:
        return typing.cast(typing.Optional["KeyspacesTableTtl"], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTimeToLive")
    def default_time_to_live(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultTimeToLive"))

    @default_time_to_live.setter
    def default_time_to_live(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTimeToLive", value)

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
    @jsii.member(jsii_name="keyspaceName")
    def keyspace_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyspaceName"))

    @keyspace_name.setter
    def keyspace_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyspaceName", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

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
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableCapacitySpecification",
    jsii_struct_bases=[],
    name_mapping={
        "read_capacity_units": "readCapacityUnits",
        "throughput_mode": "throughputMode",
        "write_capacity_units": "writeCapacityUnits",
    },
)
class KeyspacesTableCapacitySpecification:
    def __init__(
        self,
        *,
        read_capacity_units: typing.Optional[jsii.Number] = None,
        throughput_mode: typing.Optional[builtins.str] = None,
        write_capacity_units: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param read_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#read_capacity_units KeyspacesTable#read_capacity_units}.
        :param throughput_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#throughput_mode KeyspacesTable#throughput_mode}.
        :param write_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#write_capacity_units KeyspacesTable#write_capacity_units}.
        '''
        if __debug__:
            def stub(
                *,
                read_capacity_units: typing.Optional[jsii.Number] = None,
                throughput_mode: typing.Optional[builtins.str] = None,
                write_capacity_units: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument read_capacity_units", value=read_capacity_units, expected_type=type_hints["read_capacity_units"])
            check_type(argname="argument throughput_mode", value=throughput_mode, expected_type=type_hints["throughput_mode"])
            check_type(argname="argument write_capacity_units", value=write_capacity_units, expected_type=type_hints["write_capacity_units"])
        self._values: typing.Dict[str, typing.Any] = {}
        if read_capacity_units is not None:
            self._values["read_capacity_units"] = read_capacity_units
        if throughput_mode is not None:
            self._values["throughput_mode"] = throughput_mode
        if write_capacity_units is not None:
            self._values["write_capacity_units"] = write_capacity_units

    @builtins.property
    def read_capacity_units(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#read_capacity_units KeyspacesTable#read_capacity_units}.'''
        result = self._values.get("read_capacity_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def throughput_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#throughput_mode KeyspacesTable#throughput_mode}.'''
        result = self._values.get("throughput_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def write_capacity_units(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#write_capacity_units KeyspacesTable#write_capacity_units}.'''
        result = self._values.get("write_capacity_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableCapacitySpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTableCapacitySpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableCapacitySpecificationOutputReference",
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

    @jsii.member(jsii_name="resetReadCapacityUnits")
    def reset_read_capacity_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadCapacityUnits", []))

    @jsii.member(jsii_name="resetThroughputMode")
    def reset_throughput_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThroughputMode", []))

    @jsii.member(jsii_name="resetWriteCapacityUnits")
    def reset_write_capacity_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteCapacityUnits", []))

    @builtins.property
    @jsii.member(jsii_name="readCapacityUnitsInput")
    def read_capacity_units_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "readCapacityUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="throughputModeInput")
    def throughput_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "throughputModeInput"))

    @builtins.property
    @jsii.member(jsii_name="writeCapacityUnitsInput")
    def write_capacity_units_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "writeCapacityUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="readCapacityUnits")
    def read_capacity_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "readCapacityUnits"))

    @read_capacity_units.setter
    def read_capacity_units(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readCapacityUnits", value)

    @builtins.property
    @jsii.member(jsii_name="throughputMode")
    def throughput_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "throughputMode"))

    @throughput_mode.setter
    def throughput_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughputMode", value)

    @builtins.property
    @jsii.member(jsii_name="writeCapacityUnits")
    def write_capacity_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "writeCapacityUnits"))

    @write_capacity_units.setter
    def write_capacity_units(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeCapacityUnits", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KeyspacesTableCapacitySpecification]:
        return typing.cast(typing.Optional[KeyspacesTableCapacitySpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KeyspacesTableCapacitySpecification],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KeyspacesTableCapacitySpecification],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableComment",
    jsii_struct_bases=[],
    name_mapping={"message": "message"},
)
class KeyspacesTableComment:
    def __init__(self, *, message: typing.Optional[builtins.str] = None) -> None:
        '''
        :param message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#message KeyspacesTable#message}.
        '''
        if __debug__:
            def stub(*, message: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
        self._values: typing.Dict[str, typing.Any] = {}
        if message is not None:
            self._values["message"] = message

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#message KeyspacesTable#message}.'''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableComment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTableCommentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableCommentOutputReference",
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

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KeyspacesTableComment]:
        return typing.cast(typing.Optional[KeyspacesTableComment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[KeyspacesTableComment]) -> None:
        if __debug__:
            def stub(value: typing.Optional[KeyspacesTableComment]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "keyspace_name": "keyspaceName",
        "schema_definition": "schemaDefinition",
        "table_name": "tableName",
        "capacity_specification": "capacitySpecification",
        "comment": "comment",
        "default_time_to_live": "defaultTimeToLive",
        "encryption_specification": "encryptionSpecification",
        "id": "id",
        "point_in_time_recovery": "pointInTimeRecovery",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "ttl": "ttl",
    },
)
class KeyspacesTableConfig(cdktf.TerraformMetaArguments):
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
        keyspace_name: builtins.str,
        schema_definition: typing.Union["KeyspacesTableSchemaDefinition", typing.Dict[str, typing.Any]],
        table_name: builtins.str,
        capacity_specification: typing.Optional[typing.Union[KeyspacesTableCapacitySpecification, typing.Dict[str, typing.Any]]] = None,
        comment: typing.Optional[typing.Union[KeyspacesTableComment, typing.Dict[str, typing.Any]]] = None,
        default_time_to_live: typing.Optional[jsii.Number] = None,
        encryption_specification: typing.Optional[typing.Union["KeyspacesTableEncryptionSpecification", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        point_in_time_recovery: typing.Optional[typing.Union["KeyspacesTablePointInTimeRecovery", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KeyspacesTableTimeouts", typing.Dict[str, typing.Any]]] = None,
        ttl: typing.Optional[typing.Union["KeyspacesTableTtl", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param keyspace_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#keyspace_name KeyspacesTable#keyspace_name}.
        :param schema_definition: schema_definition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#schema_definition KeyspacesTable#schema_definition}
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#table_name KeyspacesTable#table_name}.
        :param capacity_specification: capacity_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#capacity_specification KeyspacesTable#capacity_specification}
        :param comment: comment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#comment KeyspacesTable#comment}
        :param default_time_to_live: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#default_time_to_live KeyspacesTable#default_time_to_live}.
        :param encryption_specification: encryption_specification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#encryption_specification KeyspacesTable#encryption_specification}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#id KeyspacesTable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param point_in_time_recovery: point_in_time_recovery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#point_in_time_recovery KeyspacesTable#point_in_time_recovery}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#tags KeyspacesTable#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#tags_all KeyspacesTable#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#timeouts KeyspacesTable#timeouts}
        :param ttl: ttl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#ttl KeyspacesTable#ttl}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(schema_definition, dict):
            schema_definition = KeyspacesTableSchemaDefinition(**schema_definition)
        if isinstance(capacity_specification, dict):
            capacity_specification = KeyspacesTableCapacitySpecification(**capacity_specification)
        if isinstance(comment, dict):
            comment = KeyspacesTableComment(**comment)
        if isinstance(encryption_specification, dict):
            encryption_specification = KeyspacesTableEncryptionSpecification(**encryption_specification)
        if isinstance(point_in_time_recovery, dict):
            point_in_time_recovery = KeyspacesTablePointInTimeRecovery(**point_in_time_recovery)
        if isinstance(timeouts, dict):
            timeouts = KeyspacesTableTimeouts(**timeouts)
        if isinstance(ttl, dict):
            ttl = KeyspacesTableTtl(**ttl)
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
                keyspace_name: builtins.str,
                schema_definition: typing.Union[KeyspacesTableSchemaDefinition, typing.Dict[str, typing.Any]],
                table_name: builtins.str,
                capacity_specification: typing.Optional[typing.Union[KeyspacesTableCapacitySpecification, typing.Dict[str, typing.Any]]] = None,
                comment: typing.Optional[typing.Union[KeyspacesTableComment, typing.Dict[str, typing.Any]]] = None,
                default_time_to_live: typing.Optional[jsii.Number] = None,
                encryption_specification: typing.Optional[typing.Union[KeyspacesTableEncryptionSpecification, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                point_in_time_recovery: typing.Optional[typing.Union[KeyspacesTablePointInTimeRecovery, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[KeyspacesTableTimeouts, typing.Dict[str, typing.Any]]] = None,
                ttl: typing.Optional[typing.Union[KeyspacesTableTtl, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument keyspace_name", value=keyspace_name, expected_type=type_hints["keyspace_name"])
            check_type(argname="argument schema_definition", value=schema_definition, expected_type=type_hints["schema_definition"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument capacity_specification", value=capacity_specification, expected_type=type_hints["capacity_specification"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument default_time_to_live", value=default_time_to_live, expected_type=type_hints["default_time_to_live"])
            check_type(argname="argument encryption_specification", value=encryption_specification, expected_type=type_hints["encryption_specification"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument point_in_time_recovery", value=point_in_time_recovery, expected_type=type_hints["point_in_time_recovery"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[str, typing.Any] = {
            "keyspace_name": keyspace_name,
            "schema_definition": schema_definition,
            "table_name": table_name,
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
        if capacity_specification is not None:
            self._values["capacity_specification"] = capacity_specification
        if comment is not None:
            self._values["comment"] = comment
        if default_time_to_live is not None:
            self._values["default_time_to_live"] = default_time_to_live
        if encryption_specification is not None:
            self._values["encryption_specification"] = encryption_specification
        if id is not None:
            self._values["id"] = id
        if point_in_time_recovery is not None:
            self._values["point_in_time_recovery"] = point_in_time_recovery
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if ttl is not None:
            self._values["ttl"] = ttl

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
    def keyspace_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#keyspace_name KeyspacesTable#keyspace_name}.'''
        result = self._values.get("keyspace_name")
        assert result is not None, "Required property 'keyspace_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema_definition(self) -> "KeyspacesTableSchemaDefinition":
        '''schema_definition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#schema_definition KeyspacesTable#schema_definition}
        '''
        result = self._values.get("schema_definition")
        assert result is not None, "Required property 'schema_definition' is missing"
        return typing.cast("KeyspacesTableSchemaDefinition", result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#table_name KeyspacesTable#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity_specification(
        self,
    ) -> typing.Optional[KeyspacesTableCapacitySpecification]:
        '''capacity_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#capacity_specification KeyspacesTable#capacity_specification}
        '''
        result = self._values.get("capacity_specification")
        return typing.cast(typing.Optional[KeyspacesTableCapacitySpecification], result)

    @builtins.property
    def comment(self) -> typing.Optional[KeyspacesTableComment]:
        '''comment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#comment KeyspacesTable#comment}
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[KeyspacesTableComment], result)

    @builtins.property
    def default_time_to_live(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#default_time_to_live KeyspacesTable#default_time_to_live}.'''
        result = self._values.get("default_time_to_live")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def encryption_specification(
        self,
    ) -> typing.Optional["KeyspacesTableEncryptionSpecification"]:
        '''encryption_specification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#encryption_specification KeyspacesTable#encryption_specification}
        '''
        result = self._values.get("encryption_specification")
        return typing.cast(typing.Optional["KeyspacesTableEncryptionSpecification"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#id KeyspacesTable#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def point_in_time_recovery(
        self,
    ) -> typing.Optional["KeyspacesTablePointInTimeRecovery"]:
        '''point_in_time_recovery block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#point_in_time_recovery KeyspacesTable#point_in_time_recovery}
        '''
        result = self._values.get("point_in_time_recovery")
        return typing.cast(typing.Optional["KeyspacesTablePointInTimeRecovery"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#tags KeyspacesTable#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#tags_all KeyspacesTable#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["KeyspacesTableTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#timeouts KeyspacesTable#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["KeyspacesTableTimeouts"], result)

    @builtins.property
    def ttl(self) -> typing.Optional["KeyspacesTableTtl"]:
        '''ttl block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#ttl KeyspacesTable#ttl}
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional["KeyspacesTableTtl"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableEncryptionSpecification",
    jsii_struct_bases=[],
    name_mapping={"kms_key_identifier": "kmsKeyIdentifier", "type": "type"},
)
class KeyspacesTableEncryptionSpecification:
    def __init__(
        self,
        *,
        kms_key_identifier: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kms_key_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#kms_key_identifier KeyspacesTable#kms_key_identifier}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#type KeyspacesTable#type}.
        '''
        if __debug__:
            def stub(
                *,
                kms_key_identifier: typing.Optional[builtins.str] = None,
                type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument kms_key_identifier", value=kms_key_identifier, expected_type=type_hints["kms_key_identifier"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if kms_key_identifier is not None:
            self._values["kms_key_identifier"] = kms_key_identifier
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def kms_key_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#kms_key_identifier KeyspacesTable#kms_key_identifier}.'''
        result = self._values.get("kms_key_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#type KeyspacesTable#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableEncryptionSpecification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTableEncryptionSpecificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableEncryptionSpecificationOutputReference",
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

    @jsii.member(jsii_name="resetKmsKeyIdentifier")
    def reset_kms_key_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyIdentifier", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdentifierInput")
    def kms_key_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyIdentifier"))

    @kms_key_identifier.setter
    def kms_key_identifier(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyIdentifier", value)

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
    def internal_value(self) -> typing.Optional[KeyspacesTableEncryptionSpecification]:
        return typing.cast(typing.Optional[KeyspacesTableEncryptionSpecification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KeyspacesTableEncryptionSpecification],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KeyspacesTableEncryptionSpecification],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTablePointInTimeRecovery",
    jsii_struct_bases=[],
    name_mapping={"status": "status"},
)
class KeyspacesTablePointInTimeRecovery:
    def __init__(self, *, status: typing.Optional[builtins.str] = None) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#status KeyspacesTable#status}.
        '''
        if __debug__:
            def stub(*, status: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[str, typing.Any] = {}
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#status KeyspacesTable#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTablePointInTimeRecovery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTablePointInTimeRecoveryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTablePointInTimeRecoveryOutputReference",
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

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KeyspacesTablePointInTimeRecovery]:
        return typing.cast(typing.Optional[KeyspacesTablePointInTimeRecovery], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KeyspacesTablePointInTimeRecovery],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[KeyspacesTablePointInTimeRecovery]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableSchemaDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "partition_key": "partitionKey",
        "clustering_key": "clusteringKey",
        "static_column": "staticColumn",
    },
)
class KeyspacesTableSchemaDefinition:
    def __init__(
        self,
        *,
        column: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionColumn", typing.Dict[str, typing.Any]]]],
        partition_key: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionPartitionKey", typing.Dict[str, typing.Any]]]],
        clustering_key: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionClusteringKey", typing.Dict[str, typing.Any]]]]] = None,
        static_column: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionStaticColumn", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param column: column block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#column KeyspacesTable#column}
        :param partition_key: partition_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#partition_key KeyspacesTable#partition_key}
        :param clustering_key: clustering_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#clustering_key KeyspacesTable#clustering_key}
        :param static_column: static_column block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#static_column KeyspacesTable#static_column}
        '''
        if __debug__:
            def stub(
                *,
                column: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionColumn, typing.Dict[str, typing.Any]]]],
                partition_key: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionPartitionKey, typing.Dict[str, typing.Any]]]],
                clustering_key: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionClusteringKey, typing.Dict[str, typing.Any]]]]] = None,
                static_column: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionStaticColumn, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument partition_key", value=partition_key, expected_type=type_hints["partition_key"])
            check_type(argname="argument clustering_key", value=clustering_key, expected_type=type_hints["clustering_key"])
            check_type(argname="argument static_column", value=static_column, expected_type=type_hints["static_column"])
        self._values: typing.Dict[str, typing.Any] = {
            "column": column,
            "partition_key": partition_key,
        }
        if clustering_key is not None:
            self._values["clustering_key"] = clustering_key
        if static_column is not None:
            self._values["static_column"] = static_column

    @builtins.property
    def column(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["KeyspacesTableSchemaDefinitionColumn"]]:
        '''column block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#column KeyspacesTable#column}
        '''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["KeyspacesTableSchemaDefinitionColumn"]], result)

    @builtins.property
    def partition_key(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["KeyspacesTableSchemaDefinitionPartitionKey"]]:
        '''partition_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#partition_key KeyspacesTable#partition_key}
        '''
        result = self._values.get("partition_key")
        assert result is not None, "Required property 'partition_key' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["KeyspacesTableSchemaDefinitionPartitionKey"]], result)

    @builtins.property
    def clustering_key(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KeyspacesTableSchemaDefinitionClusteringKey"]]]:
        '''clustering_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#clustering_key KeyspacesTable#clustering_key}
        '''
        result = self._values.get("clustering_key")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KeyspacesTableSchemaDefinitionClusteringKey"]]], result)

    @builtins.property
    def static_column(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KeyspacesTableSchemaDefinitionStaticColumn"]]]:
        '''static_column block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#static_column KeyspacesTable#static_column}
        '''
        result = self._values.get("static_column")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KeyspacesTableSchemaDefinitionStaticColumn"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableSchemaDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableSchemaDefinitionClusteringKey",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "order_by": "orderBy"},
)
class KeyspacesTableSchemaDefinitionClusteringKey:
    def __init__(self, *, name: builtins.str, order_by: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#name KeyspacesTable#name}.
        :param order_by: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#order_by KeyspacesTable#order_by}.
        '''
        if __debug__:
            def stub(*, name: builtins.str, order_by: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument order_by", value=order_by, expected_type=type_hints["order_by"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "order_by": order_by,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#name KeyspacesTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def order_by(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#order_by KeyspacesTable#order_by}.'''
        result = self._values.get("order_by")
        assert result is not None, "Required property 'order_by' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableSchemaDefinitionClusteringKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTableSchemaDefinitionClusteringKeyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableSchemaDefinitionClusteringKeyList",
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
    ) -> "KeyspacesTableSchemaDefinitionClusteringKeyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KeyspacesTableSchemaDefinitionClusteringKeyOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionClusteringKey]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionClusteringKey]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionClusteringKey]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionClusteringKey]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KeyspacesTableSchemaDefinitionClusteringKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableSchemaDefinitionClusteringKeyOutputReference",
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
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="orderByInput")
    def order_by_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "orderByInput"))

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
    @jsii.member(jsii_name="orderBy")
    def order_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "orderBy"))

    @order_by.setter
    def order_by(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "orderBy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionClusteringKey, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionClusteringKey, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionClusteringKey, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionClusteringKey, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableSchemaDefinitionColumn",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class KeyspacesTableSchemaDefinitionColumn:
    def __init__(self, *, name: builtins.str, type: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#name KeyspacesTable#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#type KeyspacesTable#type}.
        '''
        if __debug__:
            def stub(*, name: builtins.str, type: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#name KeyspacesTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#type KeyspacesTable#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableSchemaDefinitionColumn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTableSchemaDefinitionColumnList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableSchemaDefinitionColumnList",
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
    ) -> "KeyspacesTableSchemaDefinitionColumnOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KeyspacesTableSchemaDefinitionColumnOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionColumn]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionColumn]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionColumn]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionColumn]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KeyspacesTableSchemaDefinitionColumnOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableSchemaDefinitionColumnOutputReference",
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
    ) -> typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionColumn, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionColumn, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionColumn, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionColumn, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KeyspacesTableSchemaDefinitionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableSchemaDefinitionOutputReference",
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

    @jsii.member(jsii_name="putClusteringKey")
    def put_clustering_key(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionClusteringKey, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionClusteringKey, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putClusteringKey", [value]))

    @jsii.member(jsii_name="putColumn")
    def put_column(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionColumn, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionColumn, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putColumn", [value]))

    @jsii.member(jsii_name="putPartitionKey")
    def put_partition_key(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionPartitionKey", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionPartitionKey, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPartitionKey", [value]))

    @jsii.member(jsii_name="putStaticColumn")
    def put_static_column(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KeyspacesTableSchemaDefinitionStaticColumn", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KeyspacesTableSchemaDefinitionStaticColumn, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStaticColumn", [value]))

    @jsii.member(jsii_name="resetClusteringKey")
    def reset_clustering_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusteringKey", []))

    @jsii.member(jsii_name="resetStaticColumn")
    def reset_static_column(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStaticColumn", []))

    @builtins.property
    @jsii.member(jsii_name="clusteringKey")
    def clustering_key(self) -> KeyspacesTableSchemaDefinitionClusteringKeyList:
        return typing.cast(KeyspacesTableSchemaDefinitionClusteringKeyList, jsii.get(self, "clusteringKey"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> KeyspacesTableSchemaDefinitionColumnList:
        return typing.cast(KeyspacesTableSchemaDefinitionColumnList, jsii.get(self, "column"))

    @builtins.property
    @jsii.member(jsii_name="partitionKey")
    def partition_key(self) -> "KeyspacesTableSchemaDefinitionPartitionKeyList":
        return typing.cast("KeyspacesTableSchemaDefinitionPartitionKeyList", jsii.get(self, "partitionKey"))

    @builtins.property
    @jsii.member(jsii_name="staticColumn")
    def static_column(self) -> "KeyspacesTableSchemaDefinitionStaticColumnList":
        return typing.cast("KeyspacesTableSchemaDefinitionStaticColumnList", jsii.get(self, "staticColumn"))

    @builtins.property
    @jsii.member(jsii_name="clusteringKeyInput")
    def clustering_key_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionClusteringKey]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionClusteringKey]]], jsii.get(self, "clusteringKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionColumn]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionColumn]]], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionKeyInput")
    def partition_key_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KeyspacesTableSchemaDefinitionPartitionKey"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KeyspacesTableSchemaDefinitionPartitionKey"]]], jsii.get(self, "partitionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="staticColumnInput")
    def static_column_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KeyspacesTableSchemaDefinitionStaticColumn"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KeyspacesTableSchemaDefinitionStaticColumn"]]], jsii.get(self, "staticColumnInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KeyspacesTableSchemaDefinition]:
        return typing.cast(typing.Optional[KeyspacesTableSchemaDefinition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KeyspacesTableSchemaDefinition],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[KeyspacesTableSchemaDefinition]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableSchemaDefinitionPartitionKey",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class KeyspacesTableSchemaDefinitionPartitionKey:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#name KeyspacesTable#name}.
        '''
        if __debug__:
            def stub(*, name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#name KeyspacesTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableSchemaDefinitionPartitionKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTableSchemaDefinitionPartitionKeyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableSchemaDefinitionPartitionKeyList",
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
    ) -> "KeyspacesTableSchemaDefinitionPartitionKeyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KeyspacesTableSchemaDefinitionPartitionKeyOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionPartitionKey]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionPartitionKey]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionPartitionKey]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionPartitionKey]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KeyspacesTableSchemaDefinitionPartitionKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableSchemaDefinitionPartitionKeyOutputReference",
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
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionPartitionKey, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionPartitionKey, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionPartitionKey, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionPartitionKey, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableSchemaDefinitionStaticColumn",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class KeyspacesTableSchemaDefinitionStaticColumn:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#name KeyspacesTable#name}.
        '''
        if __debug__:
            def stub(*, name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#name KeyspacesTable#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableSchemaDefinitionStaticColumn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTableSchemaDefinitionStaticColumnList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableSchemaDefinitionStaticColumnList",
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
    ) -> "KeyspacesTableSchemaDefinitionStaticColumnOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KeyspacesTableSchemaDefinitionStaticColumnOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionStaticColumn]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionStaticColumn]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionStaticColumn]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KeyspacesTableSchemaDefinitionStaticColumn]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KeyspacesTableSchemaDefinitionStaticColumnOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableSchemaDefinitionStaticColumnOutputReference",
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
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionStaticColumn, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionStaticColumn, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionStaticColumn, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KeyspacesTableSchemaDefinitionStaticColumn, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class KeyspacesTableTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#create KeyspacesTable#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#delete KeyspacesTable#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#update KeyspacesTable#update}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#create KeyspacesTable#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#delete KeyspacesTable#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#update KeyspacesTable#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTableTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableTimeoutsOutputReference",
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
    ) -> typing.Optional[typing.Union[KeyspacesTableTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KeyspacesTableTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KeyspacesTableTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KeyspacesTableTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableTtl",
    jsii_struct_bases=[],
    name_mapping={"status": "status"},
)
class KeyspacesTableTtl:
    def __init__(self, *, status: builtins.str) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#status KeyspacesTable#status}.
        '''
        if __debug__:
            def stub(*, status: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[str, typing.Any] = {
            "status": status,
        }

    @builtins.property
    def status(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/keyspaces_table#status KeyspacesTable#status}.'''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspacesTableTtl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyspacesTableTtlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.keyspacesTable.KeyspacesTableTtlOutputReference",
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
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KeyspacesTableTtl]:
        return typing.cast(typing.Optional[KeyspacesTableTtl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[KeyspacesTableTtl]) -> None:
        if __debug__:
            def stub(value: typing.Optional[KeyspacesTableTtl]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KeyspacesTable",
    "KeyspacesTableCapacitySpecification",
    "KeyspacesTableCapacitySpecificationOutputReference",
    "KeyspacesTableComment",
    "KeyspacesTableCommentOutputReference",
    "KeyspacesTableConfig",
    "KeyspacesTableEncryptionSpecification",
    "KeyspacesTableEncryptionSpecificationOutputReference",
    "KeyspacesTablePointInTimeRecovery",
    "KeyspacesTablePointInTimeRecoveryOutputReference",
    "KeyspacesTableSchemaDefinition",
    "KeyspacesTableSchemaDefinitionClusteringKey",
    "KeyspacesTableSchemaDefinitionClusteringKeyList",
    "KeyspacesTableSchemaDefinitionClusteringKeyOutputReference",
    "KeyspacesTableSchemaDefinitionColumn",
    "KeyspacesTableSchemaDefinitionColumnList",
    "KeyspacesTableSchemaDefinitionColumnOutputReference",
    "KeyspacesTableSchemaDefinitionOutputReference",
    "KeyspacesTableSchemaDefinitionPartitionKey",
    "KeyspacesTableSchemaDefinitionPartitionKeyList",
    "KeyspacesTableSchemaDefinitionPartitionKeyOutputReference",
    "KeyspacesTableSchemaDefinitionStaticColumn",
    "KeyspacesTableSchemaDefinitionStaticColumnList",
    "KeyspacesTableSchemaDefinitionStaticColumnOutputReference",
    "KeyspacesTableTimeouts",
    "KeyspacesTableTimeoutsOutputReference",
    "KeyspacesTableTtl",
    "KeyspacesTableTtlOutputReference",
]

publication.publish()
