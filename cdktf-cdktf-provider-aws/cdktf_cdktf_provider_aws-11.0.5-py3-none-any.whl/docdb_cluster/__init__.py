'''
# `aws_docdb_cluster`

Refer to the Terraform Registory for docs: [`aws_docdb_cluster`](https://www.terraform.io/docs/providers/aws/r/docdb_cluster).
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


class DocdbCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.docdbCluster.DocdbCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster aws_docdb_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        apply_immediately: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        backup_retention_period: typing.Optional[jsii.Number] = None,
        cluster_identifier: typing.Optional[builtins.str] = None,
        cluster_identifier_prefix: typing.Optional[builtins.str] = None,
        cluster_members: typing.Optional[typing.Sequence[builtins.str]] = None,
        db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enabled_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
        engine: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        final_snapshot_identifier: typing.Optional[builtins.str] = None,
        global_cluster_identifier: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        master_password: typing.Optional[builtins.str] = None,
        master_username: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        skip_final_snapshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        snapshot_identifier: typing.Optional[builtins.str] = None,
        storage_encrypted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DocdbClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster aws_docdb_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param apply_immediately: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#apply_immediately DocdbCluster#apply_immediately}.
        :param availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#availability_zones DocdbCluster#availability_zones}.
        :param backup_retention_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#backup_retention_period DocdbCluster#backup_retention_period}.
        :param cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#cluster_identifier DocdbCluster#cluster_identifier}.
        :param cluster_identifier_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#cluster_identifier_prefix DocdbCluster#cluster_identifier_prefix}.
        :param cluster_members: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#cluster_members DocdbCluster#cluster_members}.
        :param db_cluster_parameter_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#db_cluster_parameter_group_name DocdbCluster#db_cluster_parameter_group_name}.
        :param db_subnet_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#db_subnet_group_name DocdbCluster#db_subnet_group_name}.
        :param deletion_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#deletion_protection DocdbCluster#deletion_protection}.
        :param enabled_cloudwatch_logs_exports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#enabled_cloudwatch_logs_exports DocdbCluster#enabled_cloudwatch_logs_exports}.
        :param engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#engine DocdbCluster#engine}.
        :param engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#engine_version DocdbCluster#engine_version}.
        :param final_snapshot_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#final_snapshot_identifier DocdbCluster#final_snapshot_identifier}.
        :param global_cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#global_cluster_identifier DocdbCluster#global_cluster_identifier}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#id DocdbCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#kms_key_id DocdbCluster#kms_key_id}.
        :param master_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#master_password DocdbCluster#master_password}.
        :param master_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#master_username DocdbCluster#master_username}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#port DocdbCluster#port}.
        :param preferred_backup_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#preferred_backup_window DocdbCluster#preferred_backup_window}.
        :param preferred_maintenance_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#preferred_maintenance_window DocdbCluster#preferred_maintenance_window}.
        :param skip_final_snapshot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#skip_final_snapshot DocdbCluster#skip_final_snapshot}.
        :param snapshot_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#snapshot_identifier DocdbCluster#snapshot_identifier}.
        :param storage_encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#storage_encrypted DocdbCluster#storage_encrypted}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#tags DocdbCluster#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#tags_all DocdbCluster#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#timeouts DocdbCluster#timeouts}
        :param vpc_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#vpc_security_group_ids DocdbCluster#vpc_security_group_ids}.
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
                apply_immediately: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
                backup_retention_period: typing.Optional[jsii.Number] = None,
                cluster_identifier: typing.Optional[builtins.str] = None,
                cluster_identifier_prefix: typing.Optional[builtins.str] = None,
                cluster_members: typing.Optional[typing.Sequence[builtins.str]] = None,
                db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
                db_subnet_group_name: typing.Optional[builtins.str] = None,
                deletion_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                enabled_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
                engine: typing.Optional[builtins.str] = None,
                engine_version: typing.Optional[builtins.str] = None,
                final_snapshot_identifier: typing.Optional[builtins.str] = None,
                global_cluster_identifier: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                kms_key_id: typing.Optional[builtins.str] = None,
                master_password: typing.Optional[builtins.str] = None,
                master_username: typing.Optional[builtins.str] = None,
                port: typing.Optional[jsii.Number] = None,
                preferred_backup_window: typing.Optional[builtins.str] = None,
                preferred_maintenance_window: typing.Optional[builtins.str] = None,
                skip_final_snapshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                snapshot_identifier: typing.Optional[builtins.str] = None,
                storage_encrypted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[DocdbClusterTimeouts, typing.Dict[str, typing.Any]]] = None,
                vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
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
        config = DocdbClusterConfig(
            apply_immediately=apply_immediately,
            availability_zones=availability_zones,
            backup_retention_period=backup_retention_period,
            cluster_identifier=cluster_identifier,
            cluster_identifier_prefix=cluster_identifier_prefix,
            cluster_members=cluster_members,
            db_cluster_parameter_group_name=db_cluster_parameter_group_name,
            db_subnet_group_name=db_subnet_group_name,
            deletion_protection=deletion_protection,
            enabled_cloudwatch_logs_exports=enabled_cloudwatch_logs_exports,
            engine=engine,
            engine_version=engine_version,
            final_snapshot_identifier=final_snapshot_identifier,
            global_cluster_identifier=global_cluster_identifier,
            id=id,
            kms_key_id=kms_key_id,
            master_password=master_password,
            master_username=master_username,
            port=port,
            preferred_backup_window=preferred_backup_window,
            preferred_maintenance_window=preferred_maintenance_window,
            skip_final_snapshot=skip_final_snapshot,
            snapshot_identifier=snapshot_identifier,
            storage_encrypted=storage_encrypted,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            vpc_security_group_ids=vpc_security_group_ids,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#create DocdbCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#delete DocdbCluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#update DocdbCluster#update}.
        '''
        value = DocdbClusterTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetApplyImmediately")
    def reset_apply_immediately(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplyImmediately", []))

    @jsii.member(jsii_name="resetAvailabilityZones")
    def reset_availability_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityZones", []))

    @jsii.member(jsii_name="resetBackupRetentionPeriod")
    def reset_backup_retention_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupRetentionPeriod", []))

    @jsii.member(jsii_name="resetClusterIdentifier")
    def reset_cluster_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterIdentifier", []))

    @jsii.member(jsii_name="resetClusterIdentifierPrefix")
    def reset_cluster_identifier_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterIdentifierPrefix", []))

    @jsii.member(jsii_name="resetClusterMembers")
    def reset_cluster_members(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterMembers", []))

    @jsii.member(jsii_name="resetDbClusterParameterGroupName")
    def reset_db_cluster_parameter_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbClusterParameterGroupName", []))

    @jsii.member(jsii_name="resetDbSubnetGroupName")
    def reset_db_subnet_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbSubnetGroupName", []))

    @jsii.member(jsii_name="resetDeletionProtection")
    def reset_deletion_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeletionProtection", []))

    @jsii.member(jsii_name="resetEnabledCloudwatchLogsExports")
    def reset_enabled_cloudwatch_logs_exports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabledCloudwatchLogsExports", []))

    @jsii.member(jsii_name="resetEngine")
    def reset_engine(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEngine", []))

    @jsii.member(jsii_name="resetEngineVersion")
    def reset_engine_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEngineVersion", []))

    @jsii.member(jsii_name="resetFinalSnapshotIdentifier")
    def reset_final_snapshot_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFinalSnapshotIdentifier", []))

    @jsii.member(jsii_name="resetGlobalClusterIdentifier")
    def reset_global_cluster_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlobalClusterIdentifier", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetMasterPassword")
    def reset_master_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterPassword", []))

    @jsii.member(jsii_name="resetMasterUsername")
    def reset_master_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterUsername", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPreferredBackupWindow")
    def reset_preferred_backup_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredBackupWindow", []))

    @jsii.member(jsii_name="resetPreferredMaintenanceWindow")
    def reset_preferred_maintenance_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredMaintenanceWindow", []))

    @jsii.member(jsii_name="resetSkipFinalSnapshot")
    def reset_skip_final_snapshot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipFinalSnapshot", []))

    @jsii.member(jsii_name="resetSnapshotIdentifier")
    def reset_snapshot_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotIdentifier", []))

    @jsii.member(jsii_name="resetStorageEncrypted")
    def reset_storage_encrypted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageEncrypted", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVpcSecurityGroupIds")
    def reset_vpc_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcSecurityGroupIds", []))

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
    @jsii.member(jsii_name="clusterResourceId")
    def cluster_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterResourceId"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @builtins.property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostedZoneId"))

    @builtins.property
    @jsii.member(jsii_name="readerEndpoint")
    def reader_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "readerEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DocdbClusterTimeoutsOutputReference":
        return typing.cast("DocdbClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="applyImmediatelyInput")
    def apply_immediately_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "applyImmediatelyInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZonesInput")
    def availability_zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "availabilityZonesInput"))

    @builtins.property
    @jsii.member(jsii_name="backupRetentionPeriodInput")
    def backup_retention_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupRetentionPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifierInput")
    def cluster_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifierPrefixInput")
    def cluster_identifier_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdentifierPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterMembersInput")
    def cluster_members_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "clusterMembersInput"))

    @builtins.property
    @jsii.member(jsii_name="dbClusterParameterGroupNameInput")
    def db_cluster_parameter_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbClusterParameterGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dbSubnetGroupNameInput")
    def db_subnet_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbSubnetGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deletionProtectionInput")
    def deletion_protection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deletionProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledCloudwatchLogsExportsInput")
    def enabled_cloudwatch_logs_exports_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "enabledCloudwatchLogsExportsInput"))

    @builtins.property
    @jsii.member(jsii_name="engineInput")
    def engine_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineInput"))

    @builtins.property
    @jsii.member(jsii_name="engineVersionInput")
    def engine_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="finalSnapshotIdentifierInput")
    def final_snapshot_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "finalSnapshotIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="globalClusterIdentifierInput")
    def global_cluster_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "globalClusterIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="masterPasswordInput")
    def master_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="masterUsernameInput")
    def master_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredBackupWindowInput")
    def preferred_backup_window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredBackupWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindowInput")
    def preferred_maintenance_window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="skipFinalSnapshotInput")
    def skip_final_snapshot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipFinalSnapshotInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotIdentifierInput")
    def snapshot_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="storageEncryptedInput")
    def storage_encrypted_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "storageEncryptedInput"))

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
    ) -> typing.Optional[typing.Union["DocdbClusterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DocdbClusterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIdsInput")
    def vpc_security_group_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSecurityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="applyImmediately")
    def apply_immediately(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "applyImmediately"))

    @apply_immediately.setter
    def apply_immediately(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applyImmediately", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "availabilityZones"))

    @availability_zones.setter
    def availability_zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZones", value)

    @builtins.property
    @jsii.member(jsii_name="backupRetentionPeriod")
    def backup_retention_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backupRetentionPeriod"))

    @backup_retention_period.setter
    def backup_retention_period(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterIdentifier"))

    @cluster_identifier.setter
    def cluster_identifier(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifierPrefix")
    def cluster_identifier_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterIdentifierPrefix"))

    @cluster_identifier_prefix.setter
    def cluster_identifier_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterIdentifierPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="clusterMembers")
    def cluster_members(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "clusterMembers"))

    @cluster_members.setter
    def cluster_members(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterMembers", value)

    @builtins.property
    @jsii.member(jsii_name="dbClusterParameterGroupName")
    def db_cluster_parameter_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbClusterParameterGroupName"))

    @db_cluster_parameter_group_name.setter
    def db_cluster_parameter_group_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbClusterParameterGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbSubnetGroupName"))

    @db_subnet_group_name.setter
    def db_subnet_group_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbSubnetGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="deletionProtection")
    def deletion_protection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deletionProtection"))

    @deletion_protection.setter
    def deletion_protection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtection", value)

    @builtins.property
    @jsii.member(jsii_name="enabledCloudwatchLogsExports")
    def enabled_cloudwatch_logs_exports(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "enabledCloudwatchLogsExports"))

    @enabled_cloudwatch_logs_exports.setter
    def enabled_cloudwatch_logs_exports(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledCloudwatchLogsExports", value)

    @builtins.property
    @jsii.member(jsii_name="engine")
    def engine(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engine", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="finalSnapshotIdentifier")
    def final_snapshot_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "finalSnapshotIdentifier"))

    @final_snapshot_identifier.setter
    def final_snapshot_identifier(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "finalSnapshotIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="globalClusterIdentifier")
    def global_cluster_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "globalClusterIdentifier"))

    @global_cluster_identifier.setter
    def global_cluster_identifier(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalClusterIdentifier", value)

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
    @jsii.member(jsii_name="masterPassword")
    def master_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterPassword"))

    @master_password.setter
    def master_password(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterPassword", value)

    @builtins.property
    @jsii.member(jsii_name="masterUsername")
    def master_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterUsername"))

    @master_username.setter
    def master_username(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUsername", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="preferredBackupWindow")
    def preferred_backup_window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferredBackupWindow"))

    @preferred_backup_window.setter
    def preferred_backup_window(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredBackupWindow", value)

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="skipFinalSnapshot")
    def skip_final_snapshot(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "skipFinalSnapshot"))

    @skip_final_snapshot.setter
    def skip_final_snapshot(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipFinalSnapshot", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotIdentifier")
    def snapshot_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotIdentifier"))

    @snapshot_identifier.setter
    def snapshot_identifier(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="storageEncrypted")
    def storage_encrypted(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "storageEncrypted"))

    @storage_encrypted.setter
    def storage_encrypted(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageEncrypted", value)

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
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroupIds", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.docdbCluster.DocdbClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "apply_immediately": "applyImmediately",
        "availability_zones": "availabilityZones",
        "backup_retention_period": "backupRetentionPeriod",
        "cluster_identifier": "clusterIdentifier",
        "cluster_identifier_prefix": "clusterIdentifierPrefix",
        "cluster_members": "clusterMembers",
        "db_cluster_parameter_group_name": "dbClusterParameterGroupName",
        "db_subnet_group_name": "dbSubnetGroupName",
        "deletion_protection": "deletionProtection",
        "enabled_cloudwatch_logs_exports": "enabledCloudwatchLogsExports",
        "engine": "engine",
        "engine_version": "engineVersion",
        "final_snapshot_identifier": "finalSnapshotIdentifier",
        "global_cluster_identifier": "globalClusterIdentifier",
        "id": "id",
        "kms_key_id": "kmsKeyId",
        "master_password": "masterPassword",
        "master_username": "masterUsername",
        "port": "port",
        "preferred_backup_window": "preferredBackupWindow",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "skip_final_snapshot": "skipFinalSnapshot",
        "snapshot_identifier": "snapshotIdentifier",
        "storage_encrypted": "storageEncrypted",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
    },
)
class DocdbClusterConfig(cdktf.TerraformMetaArguments):
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
        apply_immediately: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        backup_retention_period: typing.Optional[jsii.Number] = None,
        cluster_identifier: typing.Optional[builtins.str] = None,
        cluster_identifier_prefix: typing.Optional[builtins.str] = None,
        cluster_members: typing.Optional[typing.Sequence[builtins.str]] = None,
        db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enabled_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
        engine: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        final_snapshot_identifier: typing.Optional[builtins.str] = None,
        global_cluster_identifier: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        master_password: typing.Optional[builtins.str] = None,
        master_username: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        skip_final_snapshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        snapshot_identifier: typing.Optional[builtins.str] = None,
        storage_encrypted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DocdbClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param apply_immediately: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#apply_immediately DocdbCluster#apply_immediately}.
        :param availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#availability_zones DocdbCluster#availability_zones}.
        :param backup_retention_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#backup_retention_period DocdbCluster#backup_retention_period}.
        :param cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#cluster_identifier DocdbCluster#cluster_identifier}.
        :param cluster_identifier_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#cluster_identifier_prefix DocdbCluster#cluster_identifier_prefix}.
        :param cluster_members: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#cluster_members DocdbCluster#cluster_members}.
        :param db_cluster_parameter_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#db_cluster_parameter_group_name DocdbCluster#db_cluster_parameter_group_name}.
        :param db_subnet_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#db_subnet_group_name DocdbCluster#db_subnet_group_name}.
        :param deletion_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#deletion_protection DocdbCluster#deletion_protection}.
        :param enabled_cloudwatch_logs_exports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#enabled_cloudwatch_logs_exports DocdbCluster#enabled_cloudwatch_logs_exports}.
        :param engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#engine DocdbCluster#engine}.
        :param engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#engine_version DocdbCluster#engine_version}.
        :param final_snapshot_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#final_snapshot_identifier DocdbCluster#final_snapshot_identifier}.
        :param global_cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#global_cluster_identifier DocdbCluster#global_cluster_identifier}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#id DocdbCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#kms_key_id DocdbCluster#kms_key_id}.
        :param master_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#master_password DocdbCluster#master_password}.
        :param master_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#master_username DocdbCluster#master_username}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#port DocdbCluster#port}.
        :param preferred_backup_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#preferred_backup_window DocdbCluster#preferred_backup_window}.
        :param preferred_maintenance_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#preferred_maintenance_window DocdbCluster#preferred_maintenance_window}.
        :param skip_final_snapshot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#skip_final_snapshot DocdbCluster#skip_final_snapshot}.
        :param snapshot_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#snapshot_identifier DocdbCluster#snapshot_identifier}.
        :param storage_encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#storage_encrypted DocdbCluster#storage_encrypted}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#tags DocdbCluster#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#tags_all DocdbCluster#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#timeouts DocdbCluster#timeouts}
        :param vpc_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#vpc_security_group_ids DocdbCluster#vpc_security_group_ids}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DocdbClusterTimeouts(**timeouts)
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
                apply_immediately: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
                backup_retention_period: typing.Optional[jsii.Number] = None,
                cluster_identifier: typing.Optional[builtins.str] = None,
                cluster_identifier_prefix: typing.Optional[builtins.str] = None,
                cluster_members: typing.Optional[typing.Sequence[builtins.str]] = None,
                db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
                db_subnet_group_name: typing.Optional[builtins.str] = None,
                deletion_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                enabled_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
                engine: typing.Optional[builtins.str] = None,
                engine_version: typing.Optional[builtins.str] = None,
                final_snapshot_identifier: typing.Optional[builtins.str] = None,
                global_cluster_identifier: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                kms_key_id: typing.Optional[builtins.str] = None,
                master_password: typing.Optional[builtins.str] = None,
                master_username: typing.Optional[builtins.str] = None,
                port: typing.Optional[jsii.Number] = None,
                preferred_backup_window: typing.Optional[builtins.str] = None,
                preferred_maintenance_window: typing.Optional[builtins.str] = None,
                skip_final_snapshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                snapshot_identifier: typing.Optional[builtins.str] = None,
                storage_encrypted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[DocdbClusterTimeouts, typing.Dict[str, typing.Any]]] = None,
                vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
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
            check_type(argname="argument apply_immediately", value=apply_immediately, expected_type=type_hints["apply_immediately"])
            check_type(argname="argument availability_zones", value=availability_zones, expected_type=type_hints["availability_zones"])
            check_type(argname="argument backup_retention_period", value=backup_retention_period, expected_type=type_hints["backup_retention_period"])
            check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
            check_type(argname="argument cluster_identifier_prefix", value=cluster_identifier_prefix, expected_type=type_hints["cluster_identifier_prefix"])
            check_type(argname="argument cluster_members", value=cluster_members, expected_type=type_hints["cluster_members"])
            check_type(argname="argument db_cluster_parameter_group_name", value=db_cluster_parameter_group_name, expected_type=type_hints["db_cluster_parameter_group_name"])
            check_type(argname="argument db_subnet_group_name", value=db_subnet_group_name, expected_type=type_hints["db_subnet_group_name"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument enabled_cloudwatch_logs_exports", value=enabled_cloudwatch_logs_exports, expected_type=type_hints["enabled_cloudwatch_logs_exports"])
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument final_snapshot_identifier", value=final_snapshot_identifier, expected_type=type_hints["final_snapshot_identifier"])
            check_type(argname="argument global_cluster_identifier", value=global_cluster_identifier, expected_type=type_hints["global_cluster_identifier"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument master_password", value=master_password, expected_type=type_hints["master_password"])
            check_type(argname="argument master_username", value=master_username, expected_type=type_hints["master_username"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument preferred_backup_window", value=preferred_backup_window, expected_type=type_hints["preferred_backup_window"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument skip_final_snapshot", value=skip_final_snapshot, expected_type=type_hints["skip_final_snapshot"])
            check_type(argname="argument snapshot_identifier", value=snapshot_identifier, expected_type=type_hints["snapshot_identifier"])
            check_type(argname="argument storage_encrypted", value=storage_encrypted, expected_type=type_hints["storage_encrypted"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vpc_security_group_ids", value=vpc_security_group_ids, expected_type=type_hints["vpc_security_group_ids"])
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
        if apply_immediately is not None:
            self._values["apply_immediately"] = apply_immediately
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if backup_retention_period is not None:
            self._values["backup_retention_period"] = backup_retention_period
        if cluster_identifier is not None:
            self._values["cluster_identifier"] = cluster_identifier
        if cluster_identifier_prefix is not None:
            self._values["cluster_identifier_prefix"] = cluster_identifier_prefix
        if cluster_members is not None:
            self._values["cluster_members"] = cluster_members
        if db_cluster_parameter_group_name is not None:
            self._values["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if db_subnet_group_name is not None:
            self._values["db_subnet_group_name"] = db_subnet_group_name
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if enabled_cloudwatch_logs_exports is not None:
            self._values["enabled_cloudwatch_logs_exports"] = enabled_cloudwatch_logs_exports
        if engine is not None:
            self._values["engine"] = engine
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if final_snapshot_identifier is not None:
            self._values["final_snapshot_identifier"] = final_snapshot_identifier
        if global_cluster_identifier is not None:
            self._values["global_cluster_identifier"] = global_cluster_identifier
        if id is not None:
            self._values["id"] = id
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if master_password is not None:
            self._values["master_password"] = master_password
        if master_username is not None:
            self._values["master_username"] = master_username
        if port is not None:
            self._values["port"] = port
        if preferred_backup_window is not None:
            self._values["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if skip_final_snapshot is not None:
            self._values["skip_final_snapshot"] = skip_final_snapshot
        if snapshot_identifier is not None:
            self._values["snapshot_identifier"] = snapshot_identifier
        if storage_encrypted is not None:
            self._values["storage_encrypted"] = storage_encrypted
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vpc_security_group_ids is not None:
            self._values["vpc_security_group_ids"] = vpc_security_group_ids

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
    def apply_immediately(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#apply_immediately DocdbCluster#apply_immediately}.'''
        result = self._values.get("apply_immediately")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#availability_zones DocdbCluster#availability_zones}.'''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def backup_retention_period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#backup_retention_period DocdbCluster#backup_retention_period}.'''
        result = self._values.get("backup_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#cluster_identifier DocdbCluster#cluster_identifier}.'''
        result = self._values.get("cluster_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_identifier_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#cluster_identifier_prefix DocdbCluster#cluster_identifier_prefix}.'''
        result = self._values.get("cluster_identifier_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_members(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#cluster_members DocdbCluster#cluster_members}.'''
        result = self._values.get("cluster_members")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def db_cluster_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#db_cluster_parameter_group_name DocdbCluster#db_cluster_parameter_group_name}.'''
        result = self._values.get("db_cluster_parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#db_subnet_group_name DocdbCluster#db_subnet_group_name}.'''
        result = self._values.get("db_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#deletion_protection DocdbCluster#deletion_protection}.'''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enabled_cloudwatch_logs_exports(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#enabled_cloudwatch_logs_exports DocdbCluster#enabled_cloudwatch_logs_exports}.'''
        result = self._values.get("enabled_cloudwatch_logs_exports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def engine(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#engine DocdbCluster#engine}.'''
        result = self._values.get("engine")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#engine_version DocdbCluster#engine_version}.'''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def final_snapshot_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#final_snapshot_identifier DocdbCluster#final_snapshot_identifier}.'''
        result = self._values.get("final_snapshot_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#global_cluster_identifier DocdbCluster#global_cluster_identifier}.'''
        result = self._values.get("global_cluster_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#id DocdbCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#kms_key_id DocdbCluster#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#master_password DocdbCluster#master_password}.'''
        result = self._values.get("master_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#master_username DocdbCluster#master_username}.'''
        result = self._values.get("master_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#port DocdbCluster#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#preferred_backup_window DocdbCluster#preferred_backup_window}.'''
        result = self._values.get("preferred_backup_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#preferred_maintenance_window DocdbCluster#preferred_maintenance_window}.'''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_final_snapshot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#skip_final_snapshot DocdbCluster#skip_final_snapshot}.'''
        result = self._values.get("skip_final_snapshot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def snapshot_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#snapshot_identifier DocdbCluster#snapshot_identifier}.'''
        result = self._values.get("snapshot_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#storage_encrypted DocdbCluster#storage_encrypted}.'''
        result = self._values.get("storage_encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#tags DocdbCluster#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#tags_all DocdbCluster#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DocdbClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#timeouts DocdbCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DocdbClusterTimeouts"], result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#vpc_security_group_ids DocdbCluster#vpc_security_group_ids}.'''
        result = self._values.get("vpc_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DocdbClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.docdbCluster.DocdbClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class DocdbClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#create DocdbCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#delete DocdbCluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#update DocdbCluster#update}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#create DocdbCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#delete DocdbCluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/docdb_cluster#update DocdbCluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DocdbClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DocdbClusterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.docdbCluster.DocdbClusterTimeoutsOutputReference",
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
    ) -> typing.Optional[typing.Union[DocdbClusterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DocdbClusterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DocdbClusterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[DocdbClusterTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DocdbCluster",
    "DocdbClusterConfig",
    "DocdbClusterTimeouts",
    "DocdbClusterTimeoutsOutputReference",
]

publication.publish()
