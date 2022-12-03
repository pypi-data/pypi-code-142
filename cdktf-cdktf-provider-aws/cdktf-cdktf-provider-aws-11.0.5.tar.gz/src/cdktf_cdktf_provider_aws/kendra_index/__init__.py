'''
# `aws_kendra_index`

Refer to the Terraform Registory for docs: [`aws_kendra_index`](https://www.terraform.io/docs/providers/aws/r/kendra_index).
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


class KendraIndex(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndex",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/kendra_index aws_kendra_index}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        role_arn: builtins.str,
        capacity_units: typing.Optional[typing.Union["KendraIndexCapacityUnits", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        document_metadata_configuration_updates: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KendraIndexDocumentMetadataConfigurationUpdates", typing.Dict[str, typing.Any]]]]] = None,
        edition: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union["KendraIndexServerSideEncryptionConfiguration", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KendraIndexTimeouts", typing.Dict[str, typing.Any]]] = None,
        user_context_policy: typing.Optional[builtins.str] = None,
        user_group_resolution_configuration: typing.Optional[typing.Union["KendraIndexUserGroupResolutionConfiguration", typing.Dict[str, typing.Any]]] = None,
        user_token_configurations: typing.Optional[typing.Union["KendraIndexUserTokenConfigurations", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/kendra_index aws_kendra_index} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#name KendraIndex#name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#role_arn KendraIndex#role_arn}.
        :param capacity_units: capacity_units block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#capacity_units KendraIndex#capacity_units}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#description KendraIndex#description}.
        :param document_metadata_configuration_updates: document_metadata_configuration_updates block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#document_metadata_configuration_updates KendraIndex#document_metadata_configuration_updates}
        :param edition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#edition KendraIndex#edition}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#id KendraIndex#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param server_side_encryption_configuration: server_side_encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#server_side_encryption_configuration KendraIndex#server_side_encryption_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#tags KendraIndex#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#tags_all KendraIndex#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#timeouts KendraIndex#timeouts}
        :param user_context_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_context_policy KendraIndex#user_context_policy}.
        :param user_group_resolution_configuration: user_group_resolution_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_group_resolution_configuration KendraIndex#user_group_resolution_configuration}
        :param user_token_configurations: user_token_configurations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_token_configurations KendraIndex#user_token_configurations}
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
                role_arn: builtins.str,
                capacity_units: typing.Optional[typing.Union[KendraIndexCapacityUnits, typing.Dict[str, typing.Any]]] = None,
                description: typing.Optional[builtins.str] = None,
                document_metadata_configuration_updates: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KendraIndexDocumentMetadataConfigurationUpdates, typing.Dict[str, typing.Any]]]]] = None,
                edition: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                server_side_encryption_configuration: typing.Optional[typing.Union[KendraIndexServerSideEncryptionConfiguration, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[KendraIndexTimeouts, typing.Dict[str, typing.Any]]] = None,
                user_context_policy: typing.Optional[builtins.str] = None,
                user_group_resolution_configuration: typing.Optional[typing.Union[KendraIndexUserGroupResolutionConfiguration, typing.Dict[str, typing.Any]]] = None,
                user_token_configurations: typing.Optional[typing.Union[KendraIndexUserTokenConfigurations, typing.Dict[str, typing.Any]]] = None,
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
        config = KendraIndexConfig(
            name=name,
            role_arn=role_arn,
            capacity_units=capacity_units,
            description=description,
            document_metadata_configuration_updates=document_metadata_configuration_updates,
            edition=edition,
            id=id,
            server_side_encryption_configuration=server_side_encryption_configuration,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            user_context_policy=user_context_policy,
            user_group_resolution_configuration=user_group_resolution_configuration,
            user_token_configurations=user_token_configurations,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCapacityUnits")
    def put_capacity_units(
        self,
        *,
        query_capacity_units: typing.Optional[jsii.Number] = None,
        storage_capacity_units: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#query_capacity_units KendraIndex#query_capacity_units}.
        :param storage_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#storage_capacity_units KendraIndex#storage_capacity_units}.
        '''
        value = KendraIndexCapacityUnits(
            query_capacity_units=query_capacity_units,
            storage_capacity_units=storage_capacity_units,
        )

        return typing.cast(None, jsii.invoke(self, "putCapacityUnits", [value]))

    @jsii.member(jsii_name="putDocumentMetadataConfigurationUpdates")
    def put_document_metadata_configuration_updates(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KendraIndexDocumentMetadataConfigurationUpdates", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KendraIndexDocumentMetadataConfigurationUpdates, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDocumentMetadataConfigurationUpdates", [value]))

    @jsii.member(jsii_name="putServerSideEncryptionConfiguration")
    def put_server_side_encryption_configuration(
        self,
        *,
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#kms_key_id KendraIndex#kms_key_id}.
        '''
        value = KendraIndexServerSideEncryptionConfiguration(kms_key_id=kms_key_id)

        return typing.cast(None, jsii.invoke(self, "putServerSideEncryptionConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#create KendraIndex#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#delete KendraIndex#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#update KendraIndex#update}.
        '''
        value = KendraIndexTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putUserGroupResolutionConfiguration")
    def put_user_group_resolution_configuration(
        self,
        *,
        user_group_resolution_mode: builtins.str,
    ) -> None:
        '''
        :param user_group_resolution_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_group_resolution_mode KendraIndex#user_group_resolution_mode}.
        '''
        value = KendraIndexUserGroupResolutionConfiguration(
            user_group_resolution_mode=user_group_resolution_mode
        )

        return typing.cast(None, jsii.invoke(self, "putUserGroupResolutionConfiguration", [value]))

    @jsii.member(jsii_name="putUserTokenConfigurations")
    def put_user_token_configurations(
        self,
        *,
        json_token_type_configuration: typing.Optional[typing.Union["KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration", typing.Dict[str, typing.Any]]] = None,
        jwt_token_type_configuration: typing.Optional[typing.Union["KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param json_token_type_configuration: json_token_type_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#json_token_type_configuration KendraIndex#json_token_type_configuration}
        :param jwt_token_type_configuration: jwt_token_type_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#jwt_token_type_configuration KendraIndex#jwt_token_type_configuration}
        '''
        value = KendraIndexUserTokenConfigurations(
            json_token_type_configuration=json_token_type_configuration,
            jwt_token_type_configuration=jwt_token_type_configuration,
        )

        return typing.cast(None, jsii.invoke(self, "putUserTokenConfigurations", [value]))

    @jsii.member(jsii_name="resetCapacityUnits")
    def reset_capacity_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityUnits", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDocumentMetadataConfigurationUpdates")
    def reset_document_metadata_configuration_updates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDocumentMetadataConfigurationUpdates", []))

    @jsii.member(jsii_name="resetEdition")
    def reset_edition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEdition", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetServerSideEncryptionConfiguration")
    def reset_server_side_encryption_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerSideEncryptionConfiguration", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUserContextPolicy")
    def reset_user_context_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserContextPolicy", []))

    @jsii.member(jsii_name="resetUserGroupResolutionConfiguration")
    def reset_user_group_resolution_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserGroupResolutionConfiguration", []))

    @jsii.member(jsii_name="resetUserTokenConfigurations")
    def reset_user_token_configurations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserTokenConfigurations", []))

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
    @jsii.member(jsii_name="capacityUnits")
    def capacity_units(self) -> "KendraIndexCapacityUnitsOutputReference":
        return typing.cast("KendraIndexCapacityUnitsOutputReference", jsii.get(self, "capacityUnits"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="documentMetadataConfigurationUpdates")
    def document_metadata_configuration_updates(
        self,
    ) -> "KendraIndexDocumentMetadataConfigurationUpdatesList":
        return typing.cast("KendraIndexDocumentMetadataConfigurationUpdatesList", jsii.get(self, "documentMetadataConfigurationUpdates"))

    @builtins.property
    @jsii.member(jsii_name="errorMessage")
    def error_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorMessage"))

    @builtins.property
    @jsii.member(jsii_name="indexStatistics")
    def index_statistics(self) -> "KendraIndexIndexStatisticsList":
        return typing.cast("KendraIndexIndexStatisticsList", jsii.get(self, "indexStatistics"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionConfiguration")
    def server_side_encryption_configuration(
        self,
    ) -> "KendraIndexServerSideEncryptionConfigurationOutputReference":
        return typing.cast("KendraIndexServerSideEncryptionConfigurationOutputReference", jsii.get(self, "serverSideEncryptionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "KendraIndexTimeoutsOutputReference":
        return typing.cast("KendraIndexTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updatedAt")
    def updated_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedAt"))

    @builtins.property
    @jsii.member(jsii_name="userGroupResolutionConfiguration")
    def user_group_resolution_configuration(
        self,
    ) -> "KendraIndexUserGroupResolutionConfigurationOutputReference":
        return typing.cast("KendraIndexUserGroupResolutionConfigurationOutputReference", jsii.get(self, "userGroupResolutionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="userTokenConfigurations")
    def user_token_configurations(
        self,
    ) -> "KendraIndexUserTokenConfigurationsOutputReference":
        return typing.cast("KendraIndexUserTokenConfigurationsOutputReference", jsii.get(self, "userTokenConfigurations"))

    @builtins.property
    @jsii.member(jsii_name="capacityUnitsInput")
    def capacity_units_input(self) -> typing.Optional["KendraIndexCapacityUnits"]:
        return typing.cast(typing.Optional["KendraIndexCapacityUnits"], jsii.get(self, "capacityUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="documentMetadataConfigurationUpdatesInput")
    def document_metadata_configuration_updates_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KendraIndexDocumentMetadataConfigurationUpdates"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KendraIndexDocumentMetadataConfigurationUpdates"]]], jsii.get(self, "documentMetadataConfigurationUpdatesInput"))

    @builtins.property
    @jsii.member(jsii_name="editionInput")
    def edition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "editionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionConfigurationInput")
    def server_side_encryption_configuration_input(
        self,
    ) -> typing.Optional["KendraIndexServerSideEncryptionConfiguration"]:
        return typing.cast(typing.Optional["KendraIndexServerSideEncryptionConfiguration"], jsii.get(self, "serverSideEncryptionConfigurationInput"))

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
    ) -> typing.Optional[typing.Union["KendraIndexTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["KendraIndexTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="userContextPolicyInput")
    def user_context_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userContextPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="userGroupResolutionConfigurationInput")
    def user_group_resolution_configuration_input(
        self,
    ) -> typing.Optional["KendraIndexUserGroupResolutionConfiguration"]:
        return typing.cast(typing.Optional["KendraIndexUserGroupResolutionConfiguration"], jsii.get(self, "userGroupResolutionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="userTokenConfigurationsInput")
    def user_token_configurations_input(
        self,
    ) -> typing.Optional["KendraIndexUserTokenConfigurations"]:
        return typing.cast(typing.Optional["KendraIndexUserTokenConfigurations"], jsii.get(self, "userTokenConfigurationsInput"))

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
    @jsii.member(jsii_name="edition")
    def edition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "edition"))

    @edition.setter
    def edition(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edition", value)

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

    @builtins.property
    @jsii.member(jsii_name="userContextPolicy")
    def user_context_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userContextPolicy"))

    @user_context_policy.setter
    def user_context_policy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userContextPolicy", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexCapacityUnits",
    jsii_struct_bases=[],
    name_mapping={
        "query_capacity_units": "queryCapacityUnits",
        "storage_capacity_units": "storageCapacityUnits",
    },
)
class KendraIndexCapacityUnits:
    def __init__(
        self,
        *,
        query_capacity_units: typing.Optional[jsii.Number] = None,
        storage_capacity_units: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#query_capacity_units KendraIndex#query_capacity_units}.
        :param storage_capacity_units: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#storage_capacity_units KendraIndex#storage_capacity_units}.
        '''
        if __debug__:
            def stub(
                *,
                query_capacity_units: typing.Optional[jsii.Number] = None,
                storage_capacity_units: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument query_capacity_units", value=query_capacity_units, expected_type=type_hints["query_capacity_units"])
            check_type(argname="argument storage_capacity_units", value=storage_capacity_units, expected_type=type_hints["storage_capacity_units"])
        self._values: typing.Dict[str, typing.Any] = {}
        if query_capacity_units is not None:
            self._values["query_capacity_units"] = query_capacity_units
        if storage_capacity_units is not None:
            self._values["storage_capacity_units"] = storage_capacity_units

    @builtins.property
    def query_capacity_units(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#query_capacity_units KendraIndex#query_capacity_units}.'''
        result = self._values.get("query_capacity_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_capacity_units(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#storage_capacity_units KendraIndex#storage_capacity_units}.'''
        result = self._values.get("storage_capacity_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexCapacityUnits(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexCapacityUnitsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexCapacityUnitsOutputReference",
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

    @jsii.member(jsii_name="resetQueryCapacityUnits")
    def reset_query_capacity_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryCapacityUnits", []))

    @jsii.member(jsii_name="resetStorageCapacityUnits")
    def reset_storage_capacity_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageCapacityUnits", []))

    @builtins.property
    @jsii.member(jsii_name="queryCapacityUnitsInput")
    def query_capacity_units_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "queryCapacityUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="storageCapacityUnitsInput")
    def storage_capacity_units_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageCapacityUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="queryCapacityUnits")
    def query_capacity_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "queryCapacityUnits"))

    @query_capacity_units.setter
    def query_capacity_units(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryCapacityUnits", value)

    @builtins.property
    @jsii.member(jsii_name="storageCapacityUnits")
    def storage_capacity_units(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storageCapacityUnits"))

    @storage_capacity_units.setter
    def storage_capacity_units(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageCapacityUnits", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KendraIndexCapacityUnits]:
        return typing.cast(typing.Optional[KendraIndexCapacityUnits], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[KendraIndexCapacityUnits]) -> None:
        if __debug__:
            def stub(value: typing.Optional[KendraIndexCapacityUnits]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexConfig",
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
        "role_arn": "roleArn",
        "capacity_units": "capacityUnits",
        "description": "description",
        "document_metadata_configuration_updates": "documentMetadataConfigurationUpdates",
        "edition": "edition",
        "id": "id",
        "server_side_encryption_configuration": "serverSideEncryptionConfiguration",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "user_context_policy": "userContextPolicy",
        "user_group_resolution_configuration": "userGroupResolutionConfiguration",
        "user_token_configurations": "userTokenConfigurations",
    },
)
class KendraIndexConfig(cdktf.TerraformMetaArguments):
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
        role_arn: builtins.str,
        capacity_units: typing.Optional[typing.Union[KendraIndexCapacityUnits, typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        document_metadata_configuration_updates: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KendraIndexDocumentMetadataConfigurationUpdates", typing.Dict[str, typing.Any]]]]] = None,
        edition: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union["KendraIndexServerSideEncryptionConfiguration", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KendraIndexTimeouts", typing.Dict[str, typing.Any]]] = None,
        user_context_policy: typing.Optional[builtins.str] = None,
        user_group_resolution_configuration: typing.Optional[typing.Union["KendraIndexUserGroupResolutionConfiguration", typing.Dict[str, typing.Any]]] = None,
        user_token_configurations: typing.Optional[typing.Union["KendraIndexUserTokenConfigurations", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#name KendraIndex#name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#role_arn KendraIndex#role_arn}.
        :param capacity_units: capacity_units block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#capacity_units KendraIndex#capacity_units}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#description KendraIndex#description}.
        :param document_metadata_configuration_updates: document_metadata_configuration_updates block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#document_metadata_configuration_updates KendraIndex#document_metadata_configuration_updates}
        :param edition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#edition KendraIndex#edition}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#id KendraIndex#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param server_side_encryption_configuration: server_side_encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#server_side_encryption_configuration KendraIndex#server_side_encryption_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#tags KendraIndex#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#tags_all KendraIndex#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#timeouts KendraIndex#timeouts}
        :param user_context_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_context_policy KendraIndex#user_context_policy}.
        :param user_group_resolution_configuration: user_group_resolution_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_group_resolution_configuration KendraIndex#user_group_resolution_configuration}
        :param user_token_configurations: user_token_configurations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_token_configurations KendraIndex#user_token_configurations}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(capacity_units, dict):
            capacity_units = KendraIndexCapacityUnits(**capacity_units)
        if isinstance(server_side_encryption_configuration, dict):
            server_side_encryption_configuration = KendraIndexServerSideEncryptionConfiguration(**server_side_encryption_configuration)
        if isinstance(timeouts, dict):
            timeouts = KendraIndexTimeouts(**timeouts)
        if isinstance(user_group_resolution_configuration, dict):
            user_group_resolution_configuration = KendraIndexUserGroupResolutionConfiguration(**user_group_resolution_configuration)
        if isinstance(user_token_configurations, dict):
            user_token_configurations = KendraIndexUserTokenConfigurations(**user_token_configurations)
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
                role_arn: builtins.str,
                capacity_units: typing.Optional[typing.Union[KendraIndexCapacityUnits, typing.Dict[str, typing.Any]]] = None,
                description: typing.Optional[builtins.str] = None,
                document_metadata_configuration_updates: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KendraIndexDocumentMetadataConfigurationUpdates, typing.Dict[str, typing.Any]]]]] = None,
                edition: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                server_side_encryption_configuration: typing.Optional[typing.Union[KendraIndexServerSideEncryptionConfiguration, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[KendraIndexTimeouts, typing.Dict[str, typing.Any]]] = None,
                user_context_policy: typing.Optional[builtins.str] = None,
                user_group_resolution_configuration: typing.Optional[typing.Union[KendraIndexUserGroupResolutionConfiguration, typing.Dict[str, typing.Any]]] = None,
                user_token_configurations: typing.Optional[typing.Union[KendraIndexUserTokenConfigurations, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument capacity_units", value=capacity_units, expected_type=type_hints["capacity_units"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument document_metadata_configuration_updates", value=document_metadata_configuration_updates, expected_type=type_hints["document_metadata_configuration_updates"])
            check_type(argname="argument edition", value=edition, expected_type=type_hints["edition"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument server_side_encryption_configuration", value=server_side_encryption_configuration, expected_type=type_hints["server_side_encryption_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument user_context_policy", value=user_context_policy, expected_type=type_hints["user_context_policy"])
            check_type(argname="argument user_group_resolution_configuration", value=user_group_resolution_configuration, expected_type=type_hints["user_group_resolution_configuration"])
            check_type(argname="argument user_token_configurations", value=user_token_configurations, expected_type=type_hints["user_token_configurations"])
        self._values: typing.Dict[str, typing.Any] = {
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
        if capacity_units is not None:
            self._values["capacity_units"] = capacity_units
        if description is not None:
            self._values["description"] = description
        if document_metadata_configuration_updates is not None:
            self._values["document_metadata_configuration_updates"] = document_metadata_configuration_updates
        if edition is not None:
            self._values["edition"] = edition
        if id is not None:
            self._values["id"] = id
        if server_side_encryption_configuration is not None:
            self._values["server_side_encryption_configuration"] = server_side_encryption_configuration
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if user_context_policy is not None:
            self._values["user_context_policy"] = user_context_policy
        if user_group_resolution_configuration is not None:
            self._values["user_group_resolution_configuration"] = user_group_resolution_configuration
        if user_token_configurations is not None:
            self._values["user_token_configurations"] = user_token_configurations

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#name KendraIndex#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#role_arn KendraIndex#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity_units(self) -> typing.Optional[KendraIndexCapacityUnits]:
        '''capacity_units block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#capacity_units KendraIndex#capacity_units}
        '''
        result = self._values.get("capacity_units")
        return typing.cast(typing.Optional[KendraIndexCapacityUnits], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#description KendraIndex#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_metadata_configuration_updates(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KendraIndexDocumentMetadataConfigurationUpdates"]]]:
        '''document_metadata_configuration_updates block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#document_metadata_configuration_updates KendraIndex#document_metadata_configuration_updates}
        '''
        result = self._values.get("document_metadata_configuration_updates")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KendraIndexDocumentMetadataConfigurationUpdates"]]], result)

    @builtins.property
    def edition(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#edition KendraIndex#edition}.'''
        result = self._values.get("edition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#id KendraIndex#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional["KendraIndexServerSideEncryptionConfiguration"]:
        '''server_side_encryption_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#server_side_encryption_configuration KendraIndex#server_side_encryption_configuration}
        '''
        result = self._values.get("server_side_encryption_configuration")
        return typing.cast(typing.Optional["KendraIndexServerSideEncryptionConfiguration"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#tags KendraIndex#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#tags_all KendraIndex#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["KendraIndexTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#timeouts KendraIndex#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["KendraIndexTimeouts"], result)

    @builtins.property
    def user_context_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_context_policy KendraIndex#user_context_policy}.'''
        result = self._values.get("user_context_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_group_resolution_configuration(
        self,
    ) -> typing.Optional["KendraIndexUserGroupResolutionConfiguration"]:
        '''user_group_resolution_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_group_resolution_configuration KendraIndex#user_group_resolution_configuration}
        '''
        result = self._values.get("user_group_resolution_configuration")
        return typing.cast(typing.Optional["KendraIndexUserGroupResolutionConfiguration"], result)

    @builtins.property
    def user_token_configurations(
        self,
    ) -> typing.Optional["KendraIndexUserTokenConfigurations"]:
        '''user_token_configurations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_token_configurations KendraIndex#user_token_configurations}
        '''
        result = self._values.get("user_token_configurations")
        return typing.cast(typing.Optional["KendraIndexUserTokenConfigurations"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexDocumentMetadataConfigurationUpdates",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "relevance": "relevance",
        "search": "search",
    },
)
class KendraIndexDocumentMetadataConfigurationUpdates:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        relevance: typing.Optional[typing.Union["KendraIndexDocumentMetadataConfigurationUpdatesRelevance", typing.Dict[str, typing.Any]]] = None,
        search: typing.Optional[typing.Union["KendraIndexDocumentMetadataConfigurationUpdatesSearch", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#name KendraIndex#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#type KendraIndex#type}.
        :param relevance: relevance block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#relevance KendraIndex#relevance}
        :param search: search block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#search KendraIndex#search}
        '''
        if isinstance(relevance, dict):
            relevance = KendraIndexDocumentMetadataConfigurationUpdatesRelevance(**relevance)
        if isinstance(search, dict):
            search = KendraIndexDocumentMetadataConfigurationUpdatesSearch(**search)
        if __debug__:
            def stub(
                *,
                name: builtins.str,
                type: builtins.str,
                relevance: typing.Optional[typing.Union[KendraIndexDocumentMetadataConfigurationUpdatesRelevance, typing.Dict[str, typing.Any]]] = None,
                search: typing.Optional[typing.Union[KendraIndexDocumentMetadataConfigurationUpdatesSearch, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument relevance", value=relevance, expected_type=type_hints["relevance"])
            check_type(argname="argument search", value=search, expected_type=type_hints["search"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if relevance is not None:
            self._values["relevance"] = relevance
        if search is not None:
            self._values["search"] = search

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#name KendraIndex#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#type KendraIndex#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relevance(
        self,
    ) -> typing.Optional["KendraIndexDocumentMetadataConfigurationUpdatesRelevance"]:
        '''relevance block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#relevance KendraIndex#relevance}
        '''
        result = self._values.get("relevance")
        return typing.cast(typing.Optional["KendraIndexDocumentMetadataConfigurationUpdatesRelevance"], result)

    @builtins.property
    def search(
        self,
    ) -> typing.Optional["KendraIndexDocumentMetadataConfigurationUpdatesSearch"]:
        '''search block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#search KendraIndex#search}
        '''
        result = self._values.get("search")
        return typing.cast(typing.Optional["KendraIndexDocumentMetadataConfigurationUpdatesSearch"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexDocumentMetadataConfigurationUpdates(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexDocumentMetadataConfigurationUpdatesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexDocumentMetadataConfigurationUpdatesList",
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
    ) -> "KendraIndexDocumentMetadataConfigurationUpdatesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KendraIndexDocumentMetadataConfigurationUpdatesOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KendraIndexDocumentMetadataConfigurationUpdates]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KendraIndexDocumentMetadataConfigurationUpdates]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KendraIndexDocumentMetadataConfigurationUpdates]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KendraIndexDocumentMetadataConfigurationUpdates]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraIndexDocumentMetadataConfigurationUpdatesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexDocumentMetadataConfigurationUpdatesOutputReference",
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

    @jsii.member(jsii_name="putRelevance")
    def put_relevance(
        self,
        *,
        duration: typing.Optional[builtins.str] = None,
        freshness: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        importance: typing.Optional[jsii.Number] = None,
        rank_order: typing.Optional[builtins.str] = None,
        values_importance_map: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
    ) -> None:
        '''
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#duration KendraIndex#duration}.
        :param freshness: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#freshness KendraIndex#freshness}.
        :param importance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#importance KendraIndex#importance}.
        :param rank_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#rank_order KendraIndex#rank_order}.
        :param values_importance_map: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#values_importance_map KendraIndex#values_importance_map}.
        '''
        value = KendraIndexDocumentMetadataConfigurationUpdatesRelevance(
            duration=duration,
            freshness=freshness,
            importance=importance,
            rank_order=rank_order,
            values_importance_map=values_importance_map,
        )

        return typing.cast(None, jsii.invoke(self, "putRelevance", [value]))

    @jsii.member(jsii_name="putSearch")
    def put_search(
        self,
        *,
        displayable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        facetable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        searchable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sortable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param displayable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#displayable KendraIndex#displayable}.
        :param facetable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#facetable KendraIndex#facetable}.
        :param searchable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#searchable KendraIndex#searchable}.
        :param sortable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#sortable KendraIndex#sortable}.
        '''
        value = KendraIndexDocumentMetadataConfigurationUpdatesSearch(
            displayable=displayable,
            facetable=facetable,
            searchable=searchable,
            sortable=sortable,
        )

        return typing.cast(None, jsii.invoke(self, "putSearch", [value]))

    @jsii.member(jsii_name="resetRelevance")
    def reset_relevance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRelevance", []))

    @jsii.member(jsii_name="resetSearch")
    def reset_search(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearch", []))

    @builtins.property
    @jsii.member(jsii_name="relevance")
    def relevance(
        self,
    ) -> "KendraIndexDocumentMetadataConfigurationUpdatesRelevanceOutputReference":
        return typing.cast("KendraIndexDocumentMetadataConfigurationUpdatesRelevanceOutputReference", jsii.get(self, "relevance"))

    @builtins.property
    @jsii.member(jsii_name="search")
    def search(
        self,
    ) -> "KendraIndexDocumentMetadataConfigurationUpdatesSearchOutputReference":
        return typing.cast("KendraIndexDocumentMetadataConfigurationUpdatesSearchOutputReference", jsii.get(self, "search"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="relevanceInput")
    def relevance_input(
        self,
    ) -> typing.Optional["KendraIndexDocumentMetadataConfigurationUpdatesRelevance"]:
        return typing.cast(typing.Optional["KendraIndexDocumentMetadataConfigurationUpdatesRelevance"], jsii.get(self, "relevanceInput"))

    @builtins.property
    @jsii.member(jsii_name="searchInput")
    def search_input(
        self,
    ) -> typing.Optional["KendraIndexDocumentMetadataConfigurationUpdatesSearch"]:
        return typing.cast(typing.Optional["KendraIndexDocumentMetadataConfigurationUpdatesSearch"], jsii.get(self, "searchInput"))

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
    ) -> typing.Optional[typing.Union[KendraIndexDocumentMetadataConfigurationUpdates, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KendraIndexDocumentMetadataConfigurationUpdates, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KendraIndexDocumentMetadataConfigurationUpdates, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KendraIndexDocumentMetadataConfigurationUpdates, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexDocumentMetadataConfigurationUpdatesRelevance",
    jsii_struct_bases=[],
    name_mapping={
        "duration": "duration",
        "freshness": "freshness",
        "importance": "importance",
        "rank_order": "rankOrder",
        "values_importance_map": "valuesImportanceMap",
    },
)
class KendraIndexDocumentMetadataConfigurationUpdatesRelevance:
    def __init__(
        self,
        *,
        duration: typing.Optional[builtins.str] = None,
        freshness: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        importance: typing.Optional[jsii.Number] = None,
        rank_order: typing.Optional[builtins.str] = None,
        values_importance_map: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
    ) -> None:
        '''
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#duration KendraIndex#duration}.
        :param freshness: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#freshness KendraIndex#freshness}.
        :param importance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#importance KendraIndex#importance}.
        :param rank_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#rank_order KendraIndex#rank_order}.
        :param values_importance_map: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#values_importance_map KendraIndex#values_importance_map}.
        '''
        if __debug__:
            def stub(
                *,
                duration: typing.Optional[builtins.str] = None,
                freshness: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                importance: typing.Optional[jsii.Number] = None,
                rank_order: typing.Optional[builtins.str] = None,
                values_importance_map: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument freshness", value=freshness, expected_type=type_hints["freshness"])
            check_type(argname="argument importance", value=importance, expected_type=type_hints["importance"])
            check_type(argname="argument rank_order", value=rank_order, expected_type=type_hints["rank_order"])
            check_type(argname="argument values_importance_map", value=values_importance_map, expected_type=type_hints["values_importance_map"])
        self._values: typing.Dict[str, typing.Any] = {}
        if duration is not None:
            self._values["duration"] = duration
        if freshness is not None:
            self._values["freshness"] = freshness
        if importance is not None:
            self._values["importance"] = importance
        if rank_order is not None:
            self._values["rank_order"] = rank_order
        if values_importance_map is not None:
            self._values["values_importance_map"] = values_importance_map

    @builtins.property
    def duration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#duration KendraIndex#duration}.'''
        result = self._values.get("duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def freshness(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#freshness KendraIndex#freshness}.'''
        result = self._values.get("freshness")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def importance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#importance KendraIndex#importance}.'''
        result = self._values.get("importance")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rank_order(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#rank_order KendraIndex#rank_order}.'''
        result = self._values.get("rank_order")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values_importance_map(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#values_importance_map KendraIndex#values_importance_map}.'''
        result = self._values.get("values_importance_map")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexDocumentMetadataConfigurationUpdatesRelevance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexDocumentMetadataConfigurationUpdatesRelevanceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexDocumentMetadataConfigurationUpdatesRelevanceOutputReference",
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

    @jsii.member(jsii_name="resetDuration")
    def reset_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDuration", []))

    @jsii.member(jsii_name="resetFreshness")
    def reset_freshness(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFreshness", []))

    @jsii.member(jsii_name="resetImportance")
    def reset_importance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImportance", []))

    @jsii.member(jsii_name="resetRankOrder")
    def reset_rank_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRankOrder", []))

    @jsii.member(jsii_name="resetValuesImportanceMap")
    def reset_values_importance_map(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValuesImportanceMap", []))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="freshnessInput")
    def freshness_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "freshnessInput"))

    @builtins.property
    @jsii.member(jsii_name="importanceInput")
    def importance_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "importanceInput"))

    @builtins.property
    @jsii.member(jsii_name="rankOrderInput")
    def rank_order_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rankOrderInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesImportanceMapInput")
    def values_importance_map_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], jsii.get(self, "valuesImportanceMapInput"))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="freshness")
    def freshness(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "freshness"))

    @freshness.setter
    def freshness(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "freshness", value)

    @builtins.property
    @jsii.member(jsii_name="importance")
    def importance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "importance"))

    @importance.setter
    def importance(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "importance", value)

    @builtins.property
    @jsii.member(jsii_name="rankOrder")
    def rank_order(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rankOrder"))

    @rank_order.setter
    def rank_order(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rankOrder", value)

    @builtins.property
    @jsii.member(jsii_name="valuesImportanceMap")
    def values_importance_map(self) -> typing.Mapping[builtins.str, jsii.Number]:
        return typing.cast(typing.Mapping[builtins.str, jsii.Number], jsii.get(self, "valuesImportanceMap"))

    @values_importance_map.setter
    def values_importance_map(
        self,
        value: typing.Mapping[builtins.str, jsii.Number],
    ) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, jsii.Number]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valuesImportanceMap", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraIndexDocumentMetadataConfigurationUpdatesRelevance]:
        return typing.cast(typing.Optional[KendraIndexDocumentMetadataConfigurationUpdatesRelevance], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexDocumentMetadataConfigurationUpdatesRelevance],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraIndexDocumentMetadataConfigurationUpdatesRelevance],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexDocumentMetadataConfigurationUpdatesSearch",
    jsii_struct_bases=[],
    name_mapping={
        "displayable": "displayable",
        "facetable": "facetable",
        "searchable": "searchable",
        "sortable": "sortable",
    },
)
class KendraIndexDocumentMetadataConfigurationUpdatesSearch:
    def __init__(
        self,
        *,
        displayable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        facetable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        searchable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sortable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param displayable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#displayable KendraIndex#displayable}.
        :param facetable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#facetable KendraIndex#facetable}.
        :param searchable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#searchable KendraIndex#searchable}.
        :param sortable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#sortable KendraIndex#sortable}.
        '''
        if __debug__:
            def stub(
                *,
                displayable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                facetable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                searchable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                sortable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument displayable", value=displayable, expected_type=type_hints["displayable"])
            check_type(argname="argument facetable", value=facetable, expected_type=type_hints["facetable"])
            check_type(argname="argument searchable", value=searchable, expected_type=type_hints["searchable"])
            check_type(argname="argument sortable", value=sortable, expected_type=type_hints["sortable"])
        self._values: typing.Dict[str, typing.Any] = {}
        if displayable is not None:
            self._values["displayable"] = displayable
        if facetable is not None:
            self._values["facetable"] = facetable
        if searchable is not None:
            self._values["searchable"] = searchable
        if sortable is not None:
            self._values["sortable"] = sortable

    @builtins.property
    def displayable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#displayable KendraIndex#displayable}.'''
        result = self._values.get("displayable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def facetable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#facetable KendraIndex#facetable}.'''
        result = self._values.get("facetable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def searchable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#searchable KendraIndex#searchable}.'''
        result = self._values.get("searchable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def sortable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#sortable KendraIndex#sortable}.'''
        result = self._values.get("sortable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexDocumentMetadataConfigurationUpdatesSearch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexDocumentMetadataConfigurationUpdatesSearchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexDocumentMetadataConfigurationUpdatesSearchOutputReference",
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

    @jsii.member(jsii_name="resetDisplayable")
    def reset_displayable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayable", []))

    @jsii.member(jsii_name="resetFacetable")
    def reset_facetable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFacetable", []))

    @jsii.member(jsii_name="resetSearchable")
    def reset_searchable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearchable", []))

    @jsii.member(jsii_name="resetSortable")
    def reset_sortable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSortable", []))

    @builtins.property
    @jsii.member(jsii_name="displayableInput")
    def displayable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "displayableInput"))

    @builtins.property
    @jsii.member(jsii_name="facetableInput")
    def facetable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "facetableInput"))

    @builtins.property
    @jsii.member(jsii_name="searchableInput")
    def searchable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "searchableInput"))

    @builtins.property
    @jsii.member(jsii_name="sortableInput")
    def sortable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sortableInput"))

    @builtins.property
    @jsii.member(jsii_name="displayable")
    def displayable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "displayable"))

    @displayable.setter
    def displayable(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayable", value)

    @builtins.property
    @jsii.member(jsii_name="facetable")
    def facetable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "facetable"))

    @facetable.setter
    def facetable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "facetable", value)

    @builtins.property
    @jsii.member(jsii_name="searchable")
    def searchable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "searchable"))

    @searchable.setter
    def searchable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "searchable", value)

    @builtins.property
    @jsii.member(jsii_name="sortable")
    def sortable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sortable"))

    @sortable.setter
    def sortable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sortable", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraIndexDocumentMetadataConfigurationUpdatesSearch]:
        return typing.cast(typing.Optional[KendraIndexDocumentMetadataConfigurationUpdatesSearch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexDocumentMetadataConfigurationUpdatesSearch],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraIndexDocumentMetadataConfigurationUpdatesSearch],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexIndexStatistics",
    jsii_struct_bases=[],
    name_mapping={},
)
class KendraIndexIndexStatistics:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexIndexStatistics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexIndexStatisticsFaqStatistics",
    jsii_struct_bases=[],
    name_mapping={},
)
class KendraIndexIndexStatisticsFaqStatistics:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexIndexStatisticsFaqStatistics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexIndexStatisticsFaqStatisticsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexIndexStatisticsFaqStatisticsList",
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
    ) -> "KendraIndexIndexStatisticsFaqStatisticsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KendraIndexIndexStatisticsFaqStatisticsOutputReference", jsii.invoke(self, "get", [index]))

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


class KendraIndexIndexStatisticsFaqStatisticsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexIndexStatisticsFaqStatisticsOutputReference",
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
    @jsii.member(jsii_name="indexedQuestionAnswersCount")
    def indexed_question_answers_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "indexedQuestionAnswersCount"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraIndexIndexStatisticsFaqStatistics]:
        return typing.cast(typing.Optional[KendraIndexIndexStatisticsFaqStatistics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexIndexStatisticsFaqStatistics],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraIndexIndexStatisticsFaqStatistics],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraIndexIndexStatisticsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexIndexStatisticsList",
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
    def get(self, index: jsii.Number) -> "KendraIndexIndexStatisticsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KendraIndexIndexStatisticsOutputReference", jsii.invoke(self, "get", [index]))

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


class KendraIndexIndexStatisticsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexIndexStatisticsOutputReference",
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
    @jsii.member(jsii_name="faqStatistics")
    def faq_statistics(self) -> KendraIndexIndexStatisticsFaqStatisticsList:
        return typing.cast(KendraIndexIndexStatisticsFaqStatisticsList, jsii.get(self, "faqStatistics"))

    @builtins.property
    @jsii.member(jsii_name="textDocumentStatistics")
    def text_document_statistics(
        self,
    ) -> "KendraIndexIndexStatisticsTextDocumentStatisticsList":
        return typing.cast("KendraIndexIndexStatisticsTextDocumentStatisticsList", jsii.get(self, "textDocumentStatistics"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KendraIndexIndexStatistics]:
        return typing.cast(typing.Optional[KendraIndexIndexStatistics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexIndexStatistics],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[KendraIndexIndexStatistics]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexIndexStatisticsTextDocumentStatistics",
    jsii_struct_bases=[],
    name_mapping={},
)
class KendraIndexIndexStatisticsTextDocumentStatistics:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexIndexStatisticsTextDocumentStatistics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexIndexStatisticsTextDocumentStatisticsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexIndexStatisticsTextDocumentStatisticsList",
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
    ) -> "KendraIndexIndexStatisticsTextDocumentStatisticsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KendraIndexIndexStatisticsTextDocumentStatisticsOutputReference", jsii.invoke(self, "get", [index]))

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


class KendraIndexIndexStatisticsTextDocumentStatisticsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexIndexStatisticsTextDocumentStatisticsOutputReference",
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
    @jsii.member(jsii_name="indexedTextBytes")
    def indexed_text_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "indexedTextBytes"))

    @builtins.property
    @jsii.member(jsii_name="indexedTextDocumentsCount")
    def indexed_text_documents_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "indexedTextDocumentsCount"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraIndexIndexStatisticsTextDocumentStatistics]:
        return typing.cast(typing.Optional[KendraIndexIndexStatisticsTextDocumentStatistics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexIndexStatisticsTextDocumentStatistics],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraIndexIndexStatisticsTextDocumentStatistics],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexServerSideEncryptionConfiguration",
    jsii_struct_bases=[],
    name_mapping={"kms_key_id": "kmsKeyId"},
)
class KendraIndexServerSideEncryptionConfiguration:
    def __init__(self, *, kms_key_id: typing.Optional[builtins.str] = None) -> None:
        '''
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#kms_key_id KendraIndex#kms_key_id}.
        '''
        if __debug__:
            def stub(*, kms_key_id: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#kms_key_id KendraIndex#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexServerSideEncryptionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexServerSideEncryptionConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexServerSideEncryptionConfigurationOutputReference",
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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraIndexServerSideEncryptionConfiguration]:
        return typing.cast(typing.Optional[KendraIndexServerSideEncryptionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexServerSideEncryptionConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraIndexServerSideEncryptionConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class KendraIndexTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#create KendraIndex#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#delete KendraIndex#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#update KendraIndex#update}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#create KendraIndex#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#delete KendraIndex#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#update KendraIndex#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexTimeoutsOutputReference",
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
    ) -> typing.Optional[typing.Union[KendraIndexTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KendraIndexTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KendraIndexTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KendraIndexTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexUserGroupResolutionConfiguration",
    jsii_struct_bases=[],
    name_mapping={"user_group_resolution_mode": "userGroupResolutionMode"},
)
class KendraIndexUserGroupResolutionConfiguration:
    def __init__(self, *, user_group_resolution_mode: builtins.str) -> None:
        '''
        :param user_group_resolution_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_group_resolution_mode KendraIndex#user_group_resolution_mode}.
        '''
        if __debug__:
            def stub(*, user_group_resolution_mode: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument user_group_resolution_mode", value=user_group_resolution_mode, expected_type=type_hints["user_group_resolution_mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "user_group_resolution_mode": user_group_resolution_mode,
        }

    @builtins.property
    def user_group_resolution_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_group_resolution_mode KendraIndex#user_group_resolution_mode}.'''
        result = self._values.get("user_group_resolution_mode")
        assert result is not None, "Required property 'user_group_resolution_mode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexUserGroupResolutionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexUserGroupResolutionConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexUserGroupResolutionConfigurationOutputReference",
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
    @jsii.member(jsii_name="userGroupResolutionModeInput")
    def user_group_resolution_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userGroupResolutionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="userGroupResolutionMode")
    def user_group_resolution_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userGroupResolutionMode"))

    @user_group_resolution_mode.setter
    def user_group_resolution_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userGroupResolutionMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraIndexUserGroupResolutionConfiguration]:
        return typing.cast(typing.Optional[KendraIndexUserGroupResolutionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexUserGroupResolutionConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraIndexUserGroupResolutionConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexUserTokenConfigurations",
    jsii_struct_bases=[],
    name_mapping={
        "json_token_type_configuration": "jsonTokenTypeConfiguration",
        "jwt_token_type_configuration": "jwtTokenTypeConfiguration",
    },
)
class KendraIndexUserTokenConfigurations:
    def __init__(
        self,
        *,
        json_token_type_configuration: typing.Optional[typing.Union["KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration", typing.Dict[str, typing.Any]]] = None,
        jwt_token_type_configuration: typing.Optional[typing.Union["KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param json_token_type_configuration: json_token_type_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#json_token_type_configuration KendraIndex#json_token_type_configuration}
        :param jwt_token_type_configuration: jwt_token_type_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#jwt_token_type_configuration KendraIndex#jwt_token_type_configuration}
        '''
        if isinstance(json_token_type_configuration, dict):
            json_token_type_configuration = KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration(**json_token_type_configuration)
        if isinstance(jwt_token_type_configuration, dict):
            jwt_token_type_configuration = KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration(**jwt_token_type_configuration)
        if __debug__:
            def stub(
                *,
                json_token_type_configuration: typing.Optional[typing.Union[KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration, typing.Dict[str, typing.Any]]] = None,
                jwt_token_type_configuration: typing.Optional[typing.Union[KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument json_token_type_configuration", value=json_token_type_configuration, expected_type=type_hints["json_token_type_configuration"])
            check_type(argname="argument jwt_token_type_configuration", value=jwt_token_type_configuration, expected_type=type_hints["jwt_token_type_configuration"])
        self._values: typing.Dict[str, typing.Any] = {}
        if json_token_type_configuration is not None:
            self._values["json_token_type_configuration"] = json_token_type_configuration
        if jwt_token_type_configuration is not None:
            self._values["jwt_token_type_configuration"] = jwt_token_type_configuration

    @builtins.property
    def json_token_type_configuration(
        self,
    ) -> typing.Optional["KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration"]:
        '''json_token_type_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#json_token_type_configuration KendraIndex#json_token_type_configuration}
        '''
        result = self._values.get("json_token_type_configuration")
        return typing.cast(typing.Optional["KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration"], result)

    @builtins.property
    def jwt_token_type_configuration(
        self,
    ) -> typing.Optional["KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration"]:
        '''jwt_token_type_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#jwt_token_type_configuration KendraIndex#jwt_token_type_configuration}
        '''
        result = self._values.get("jwt_token_type_configuration")
        return typing.cast(typing.Optional["KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexUserTokenConfigurations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "group_attribute_field": "groupAttributeField",
        "user_name_attribute_field": "userNameAttributeField",
    },
)
class KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration:
    def __init__(
        self,
        *,
        group_attribute_field: builtins.str,
        user_name_attribute_field: builtins.str,
    ) -> None:
        '''
        :param group_attribute_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#group_attribute_field KendraIndex#group_attribute_field}.
        :param user_name_attribute_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_name_attribute_field KendraIndex#user_name_attribute_field}.
        '''
        if __debug__:
            def stub(
                *,
                group_attribute_field: builtins.str,
                user_name_attribute_field: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument group_attribute_field", value=group_attribute_field, expected_type=type_hints["group_attribute_field"])
            check_type(argname="argument user_name_attribute_field", value=user_name_attribute_field, expected_type=type_hints["user_name_attribute_field"])
        self._values: typing.Dict[str, typing.Any] = {
            "group_attribute_field": group_attribute_field,
            "user_name_attribute_field": user_name_attribute_field,
        }

    @builtins.property
    def group_attribute_field(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#group_attribute_field KendraIndex#group_attribute_field}.'''
        result = self._values.get("group_attribute_field")
        assert result is not None, "Required property 'group_attribute_field' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name_attribute_field(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_name_attribute_field KendraIndex#user_name_attribute_field}.'''
        result = self._values.get("user_name_attribute_field")
        assert result is not None, "Required property 'user_name_attribute_field' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexUserTokenConfigurationsJsonTokenTypeConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexUserTokenConfigurationsJsonTokenTypeConfigurationOutputReference",
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
    @jsii.member(jsii_name="groupAttributeFieldInput")
    def group_attribute_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupAttributeFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="userNameAttributeFieldInput")
    def user_name_attribute_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userNameAttributeFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="groupAttributeField")
    def group_attribute_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupAttributeField"))

    @group_attribute_field.setter
    def group_attribute_field(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupAttributeField", value)

    @builtins.property
    @jsii.member(jsii_name="userNameAttributeField")
    def user_name_attribute_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userNameAttributeField"))

    @user_name_attribute_field.setter
    def user_name_attribute_field(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userNameAttributeField", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration]:
        return typing.cast(typing.Optional[KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "key_location": "keyLocation",
        "claim_regex": "claimRegex",
        "group_attribute_field": "groupAttributeField",
        "issuer": "issuer",
        "secrets_manager_arn": "secretsManagerArn",
        "url": "url",
        "user_name_attribute_field": "userNameAttributeField",
    },
)
class KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration:
    def __init__(
        self,
        *,
        key_location: builtins.str,
        claim_regex: typing.Optional[builtins.str] = None,
        group_attribute_field: typing.Optional[builtins.str] = None,
        issuer: typing.Optional[builtins.str] = None,
        secrets_manager_arn: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
        user_name_attribute_field: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#key_location KendraIndex#key_location}.
        :param claim_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#claim_regex KendraIndex#claim_regex}.
        :param group_attribute_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#group_attribute_field KendraIndex#group_attribute_field}.
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#issuer KendraIndex#issuer}.
        :param secrets_manager_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#secrets_manager_arn KendraIndex#secrets_manager_arn}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#url KendraIndex#url}.
        :param user_name_attribute_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_name_attribute_field KendraIndex#user_name_attribute_field}.
        '''
        if __debug__:
            def stub(
                *,
                key_location: builtins.str,
                claim_regex: typing.Optional[builtins.str] = None,
                group_attribute_field: typing.Optional[builtins.str] = None,
                issuer: typing.Optional[builtins.str] = None,
                secrets_manager_arn: typing.Optional[builtins.str] = None,
                url: typing.Optional[builtins.str] = None,
                user_name_attribute_field: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key_location", value=key_location, expected_type=type_hints["key_location"])
            check_type(argname="argument claim_regex", value=claim_regex, expected_type=type_hints["claim_regex"])
            check_type(argname="argument group_attribute_field", value=group_attribute_field, expected_type=type_hints["group_attribute_field"])
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            check_type(argname="argument secrets_manager_arn", value=secrets_manager_arn, expected_type=type_hints["secrets_manager_arn"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument user_name_attribute_field", value=user_name_attribute_field, expected_type=type_hints["user_name_attribute_field"])
        self._values: typing.Dict[str, typing.Any] = {
            "key_location": key_location,
        }
        if claim_regex is not None:
            self._values["claim_regex"] = claim_regex
        if group_attribute_field is not None:
            self._values["group_attribute_field"] = group_attribute_field
        if issuer is not None:
            self._values["issuer"] = issuer
        if secrets_manager_arn is not None:
            self._values["secrets_manager_arn"] = secrets_manager_arn
        if url is not None:
            self._values["url"] = url
        if user_name_attribute_field is not None:
            self._values["user_name_attribute_field"] = user_name_attribute_field

    @builtins.property
    def key_location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#key_location KendraIndex#key_location}.'''
        result = self._values.get("key_location")
        assert result is not None, "Required property 'key_location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def claim_regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#claim_regex KendraIndex#claim_regex}.'''
        result = self._values.get("claim_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_attribute_field(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#group_attribute_field KendraIndex#group_attribute_field}.'''
        result = self._values.get("group_attribute_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def issuer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#issuer KendraIndex#issuer}.'''
        result = self._values.get("issuer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secrets_manager_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#secrets_manager_arn KendraIndex#secrets_manager_arn}.'''
        result = self._values.get("secrets_manager_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#url KendraIndex#url}.'''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_name_attribute_field(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_name_attribute_field KendraIndex#user_name_attribute_field}.'''
        result = self._values.get("user_name_attribute_field")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KendraIndexUserTokenConfigurationsJwtTokenTypeConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexUserTokenConfigurationsJwtTokenTypeConfigurationOutputReference",
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

    @jsii.member(jsii_name="resetClaimRegex")
    def reset_claim_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClaimRegex", []))

    @jsii.member(jsii_name="resetGroupAttributeField")
    def reset_group_attribute_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupAttributeField", []))

    @jsii.member(jsii_name="resetIssuer")
    def reset_issuer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuer", []))

    @jsii.member(jsii_name="resetSecretsManagerArn")
    def reset_secrets_manager_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretsManagerArn", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @jsii.member(jsii_name="resetUserNameAttributeField")
    def reset_user_name_attribute_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserNameAttributeField", []))

    @builtins.property
    @jsii.member(jsii_name="claimRegexInput")
    def claim_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "claimRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="groupAttributeFieldInput")
    def group_attribute_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupAttributeFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="keyLocationInput")
    def key_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="secretsManagerArnInput")
    def secrets_manager_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretsManagerArnInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="userNameAttributeFieldInput")
    def user_name_attribute_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userNameAttributeFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="claimRegex")
    def claim_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "claimRegex"))

    @claim_regex.setter
    def claim_regex(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "claimRegex", value)

    @builtins.property
    @jsii.member(jsii_name="groupAttributeField")
    def group_attribute_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupAttributeField"))

    @group_attribute_field.setter
    def group_attribute_field(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupAttributeField", value)

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
    @jsii.member(jsii_name="keyLocation")
    def key_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyLocation"))

    @key_location.setter
    def key_location(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyLocation", value)

    @builtins.property
    @jsii.member(jsii_name="secretsManagerArn")
    def secrets_manager_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretsManagerArn"))

    @secrets_manager_arn.setter
    def secrets_manager_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretsManagerArn", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="userNameAttributeField")
    def user_name_attribute_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userNameAttributeField"))

    @user_name_attribute_field.setter
    def user_name_attribute_field(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userNameAttributeField", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration]:
        return typing.cast(typing.Optional[KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KendraIndexUserTokenConfigurationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kendraIndex.KendraIndexUserTokenConfigurationsOutputReference",
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

    @jsii.member(jsii_name="putJsonTokenTypeConfiguration")
    def put_json_token_type_configuration(
        self,
        *,
        group_attribute_field: builtins.str,
        user_name_attribute_field: builtins.str,
    ) -> None:
        '''
        :param group_attribute_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#group_attribute_field KendraIndex#group_attribute_field}.
        :param user_name_attribute_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_name_attribute_field KendraIndex#user_name_attribute_field}.
        '''
        value = KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration(
            group_attribute_field=group_attribute_field,
            user_name_attribute_field=user_name_attribute_field,
        )

        return typing.cast(None, jsii.invoke(self, "putJsonTokenTypeConfiguration", [value]))

    @jsii.member(jsii_name="putJwtTokenTypeConfiguration")
    def put_jwt_token_type_configuration(
        self,
        *,
        key_location: builtins.str,
        claim_regex: typing.Optional[builtins.str] = None,
        group_attribute_field: typing.Optional[builtins.str] = None,
        issuer: typing.Optional[builtins.str] = None,
        secrets_manager_arn: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
        user_name_attribute_field: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#key_location KendraIndex#key_location}.
        :param claim_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#claim_regex KendraIndex#claim_regex}.
        :param group_attribute_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#group_attribute_field KendraIndex#group_attribute_field}.
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#issuer KendraIndex#issuer}.
        :param secrets_manager_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#secrets_manager_arn KendraIndex#secrets_manager_arn}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#url KendraIndex#url}.
        :param user_name_attribute_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kendra_index#user_name_attribute_field KendraIndex#user_name_attribute_field}.
        '''
        value = KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration(
            key_location=key_location,
            claim_regex=claim_regex,
            group_attribute_field=group_attribute_field,
            issuer=issuer,
            secrets_manager_arn=secrets_manager_arn,
            url=url,
            user_name_attribute_field=user_name_attribute_field,
        )

        return typing.cast(None, jsii.invoke(self, "putJwtTokenTypeConfiguration", [value]))

    @jsii.member(jsii_name="resetJsonTokenTypeConfiguration")
    def reset_json_token_type_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonTokenTypeConfiguration", []))

    @jsii.member(jsii_name="resetJwtTokenTypeConfiguration")
    def reset_jwt_token_type_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJwtTokenTypeConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="jsonTokenTypeConfiguration")
    def json_token_type_configuration(
        self,
    ) -> KendraIndexUserTokenConfigurationsJsonTokenTypeConfigurationOutputReference:
        return typing.cast(KendraIndexUserTokenConfigurationsJsonTokenTypeConfigurationOutputReference, jsii.get(self, "jsonTokenTypeConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="jwtTokenTypeConfiguration")
    def jwt_token_type_configuration(
        self,
    ) -> KendraIndexUserTokenConfigurationsJwtTokenTypeConfigurationOutputReference:
        return typing.cast(KendraIndexUserTokenConfigurationsJwtTokenTypeConfigurationOutputReference, jsii.get(self, "jwtTokenTypeConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="jsonTokenTypeConfigurationInput")
    def json_token_type_configuration_input(
        self,
    ) -> typing.Optional[KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration]:
        return typing.cast(typing.Optional[KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration], jsii.get(self, "jsonTokenTypeConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="jwtTokenTypeConfigurationInput")
    def jwt_token_type_configuration_input(
        self,
    ) -> typing.Optional[KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration]:
        return typing.cast(typing.Optional[KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration], jsii.get(self, "jwtTokenTypeConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KendraIndexUserTokenConfigurations]:
        return typing.cast(typing.Optional[KendraIndexUserTokenConfigurations], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KendraIndexUserTokenConfigurations],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KendraIndexUserTokenConfigurations],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KendraIndex",
    "KendraIndexCapacityUnits",
    "KendraIndexCapacityUnitsOutputReference",
    "KendraIndexConfig",
    "KendraIndexDocumentMetadataConfigurationUpdates",
    "KendraIndexDocumentMetadataConfigurationUpdatesList",
    "KendraIndexDocumentMetadataConfigurationUpdatesOutputReference",
    "KendraIndexDocumentMetadataConfigurationUpdatesRelevance",
    "KendraIndexDocumentMetadataConfigurationUpdatesRelevanceOutputReference",
    "KendraIndexDocumentMetadataConfigurationUpdatesSearch",
    "KendraIndexDocumentMetadataConfigurationUpdatesSearchOutputReference",
    "KendraIndexIndexStatistics",
    "KendraIndexIndexStatisticsFaqStatistics",
    "KendraIndexIndexStatisticsFaqStatisticsList",
    "KendraIndexIndexStatisticsFaqStatisticsOutputReference",
    "KendraIndexIndexStatisticsList",
    "KendraIndexIndexStatisticsOutputReference",
    "KendraIndexIndexStatisticsTextDocumentStatistics",
    "KendraIndexIndexStatisticsTextDocumentStatisticsList",
    "KendraIndexIndexStatisticsTextDocumentStatisticsOutputReference",
    "KendraIndexServerSideEncryptionConfiguration",
    "KendraIndexServerSideEncryptionConfigurationOutputReference",
    "KendraIndexTimeouts",
    "KendraIndexTimeoutsOutputReference",
    "KendraIndexUserGroupResolutionConfiguration",
    "KendraIndexUserGroupResolutionConfigurationOutputReference",
    "KendraIndexUserTokenConfigurations",
    "KendraIndexUserTokenConfigurationsJsonTokenTypeConfiguration",
    "KendraIndexUserTokenConfigurationsJsonTokenTypeConfigurationOutputReference",
    "KendraIndexUserTokenConfigurationsJwtTokenTypeConfiguration",
    "KendraIndexUserTokenConfigurationsJwtTokenTypeConfigurationOutputReference",
    "KendraIndexUserTokenConfigurationsOutputReference",
]

publication.publish()
