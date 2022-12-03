'''
# `aws_rds_cluster`

Refer to the Terraform Registory for docs: [`aws_rds_cluster`](https://www.terraform.io/docs/providers/aws/r/rds_cluster).
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


class RdsCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.rdsCluster.RdsCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster aws_rds_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        allocated_storage: typing.Optional[jsii.Number] = None,
        allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        apply_immediately: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        backtrack_window: typing.Optional[jsii.Number] = None,
        backup_retention_period: typing.Optional[jsii.Number] = None,
        cluster_identifier: typing.Optional[builtins.str] = None,
        cluster_identifier_prefix: typing.Optional[builtins.str] = None,
        cluster_members: typing.Optional[typing.Sequence[builtins.str]] = None,
        copy_tags_to_snapshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        database_name: typing.Optional[builtins.str] = None,
        db_cluster_instance_class: typing.Optional[builtins.str] = None,
        db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        db_instance_parameter_group_name: typing.Optional[builtins.str] = None,
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enabled_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_global_write_forwarding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_http_endpoint: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        engine: typing.Optional[builtins.str] = None,
        engine_mode: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        final_snapshot_identifier: typing.Optional[builtins.str] = None,
        global_cluster_identifier: typing.Optional[builtins.str] = None,
        iam_database_authentication_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        master_password: typing.Optional[builtins.str] = None,
        master_username: typing.Optional[builtins.str] = None,
        network_type: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        replication_source_identifier: typing.Optional[builtins.str] = None,
        restore_to_point_in_time: typing.Optional[typing.Union["RdsClusterRestoreToPointInTime", typing.Dict[str, typing.Any]]] = None,
        s3_import: typing.Optional[typing.Union["RdsClusterS3Import", typing.Dict[str, typing.Any]]] = None,
        scaling_configuration: typing.Optional[typing.Union["RdsClusterScalingConfiguration", typing.Dict[str, typing.Any]]] = None,
        serverlessv2_scaling_configuration: typing.Optional[typing.Union["RdsClusterServerlessv2ScalingConfiguration", typing.Dict[str, typing.Any]]] = None,
        skip_final_snapshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        snapshot_identifier: typing.Optional[builtins.str] = None,
        source_region: typing.Optional[builtins.str] = None,
        storage_encrypted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        storage_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["RdsClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster aws_rds_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param allocated_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#allocated_storage RdsCluster#allocated_storage}.
        :param allow_major_version_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#allow_major_version_upgrade RdsCluster#allow_major_version_upgrade}.
        :param apply_immediately: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#apply_immediately RdsCluster#apply_immediately}.
        :param availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#availability_zones RdsCluster#availability_zones}.
        :param backtrack_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#backtrack_window RdsCluster#backtrack_window}.
        :param backup_retention_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#backup_retention_period RdsCluster#backup_retention_period}.
        :param cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#cluster_identifier RdsCluster#cluster_identifier}.
        :param cluster_identifier_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#cluster_identifier_prefix RdsCluster#cluster_identifier_prefix}.
        :param cluster_members: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#cluster_members RdsCluster#cluster_members}.
        :param copy_tags_to_snapshot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#copy_tags_to_snapshot RdsCluster#copy_tags_to_snapshot}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#database_name RdsCluster#database_name}.
        :param db_cluster_instance_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#db_cluster_instance_class RdsCluster#db_cluster_instance_class}.
        :param db_cluster_parameter_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#db_cluster_parameter_group_name RdsCluster#db_cluster_parameter_group_name}.
        :param db_instance_parameter_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#db_instance_parameter_group_name RdsCluster#db_instance_parameter_group_name}.
        :param db_subnet_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#db_subnet_group_name RdsCluster#db_subnet_group_name}.
        :param deletion_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#deletion_protection RdsCluster#deletion_protection}.
        :param enabled_cloudwatch_logs_exports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#enabled_cloudwatch_logs_exports RdsCluster#enabled_cloudwatch_logs_exports}.
        :param enable_global_write_forwarding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#enable_global_write_forwarding RdsCluster#enable_global_write_forwarding}.
        :param enable_http_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#enable_http_endpoint RdsCluster#enable_http_endpoint}.
        :param engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#engine RdsCluster#engine}.
        :param engine_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#engine_mode RdsCluster#engine_mode}.
        :param engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#engine_version RdsCluster#engine_version}.
        :param final_snapshot_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#final_snapshot_identifier RdsCluster#final_snapshot_identifier}.
        :param global_cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#global_cluster_identifier RdsCluster#global_cluster_identifier}.
        :param iam_database_authentication_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#iam_database_authentication_enabled RdsCluster#iam_database_authentication_enabled}.
        :param iam_roles: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#iam_roles RdsCluster#iam_roles}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#id RdsCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#iops RdsCluster#iops}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#kms_key_id RdsCluster#kms_key_id}.
        :param master_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#master_password RdsCluster#master_password}.
        :param master_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#master_username RdsCluster#master_username}.
        :param network_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#network_type RdsCluster#network_type}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#port RdsCluster#port}.
        :param preferred_backup_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#preferred_backup_window RdsCluster#preferred_backup_window}.
        :param preferred_maintenance_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#preferred_maintenance_window RdsCluster#preferred_maintenance_window}.
        :param replication_source_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#replication_source_identifier RdsCluster#replication_source_identifier}.
        :param restore_to_point_in_time: restore_to_point_in_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#restore_to_point_in_time RdsCluster#restore_to_point_in_time}
        :param s3_import: s3_import block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#s3_import RdsCluster#s3_import}
        :param scaling_configuration: scaling_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#scaling_configuration RdsCluster#scaling_configuration}
        :param serverlessv2_scaling_configuration: serverlessv2_scaling_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#serverlessv2_scaling_configuration RdsCluster#serverlessv2_scaling_configuration}
        :param skip_final_snapshot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#skip_final_snapshot RdsCluster#skip_final_snapshot}.
        :param snapshot_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#snapshot_identifier RdsCluster#snapshot_identifier}.
        :param source_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#source_region RdsCluster#source_region}.
        :param storage_encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#storage_encrypted RdsCluster#storage_encrypted}.
        :param storage_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#storage_type RdsCluster#storage_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#tags RdsCluster#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#tags_all RdsCluster#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#timeouts RdsCluster#timeouts}
        :param vpc_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#vpc_security_group_ids RdsCluster#vpc_security_group_ids}.
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
                allocated_storage: typing.Optional[jsii.Number] = None,
                allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                apply_immediately: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
                backtrack_window: typing.Optional[jsii.Number] = None,
                backup_retention_period: typing.Optional[jsii.Number] = None,
                cluster_identifier: typing.Optional[builtins.str] = None,
                cluster_identifier_prefix: typing.Optional[builtins.str] = None,
                cluster_members: typing.Optional[typing.Sequence[builtins.str]] = None,
                copy_tags_to_snapshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                database_name: typing.Optional[builtins.str] = None,
                db_cluster_instance_class: typing.Optional[builtins.str] = None,
                db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
                db_instance_parameter_group_name: typing.Optional[builtins.str] = None,
                db_subnet_group_name: typing.Optional[builtins.str] = None,
                deletion_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                enabled_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
                enable_global_write_forwarding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                enable_http_endpoint: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                engine: typing.Optional[builtins.str] = None,
                engine_mode: typing.Optional[builtins.str] = None,
                engine_version: typing.Optional[builtins.str] = None,
                final_snapshot_identifier: typing.Optional[builtins.str] = None,
                global_cluster_identifier: typing.Optional[builtins.str] = None,
                iam_database_authentication_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
                id: typing.Optional[builtins.str] = None,
                iops: typing.Optional[jsii.Number] = None,
                kms_key_id: typing.Optional[builtins.str] = None,
                master_password: typing.Optional[builtins.str] = None,
                master_username: typing.Optional[builtins.str] = None,
                network_type: typing.Optional[builtins.str] = None,
                port: typing.Optional[jsii.Number] = None,
                preferred_backup_window: typing.Optional[builtins.str] = None,
                preferred_maintenance_window: typing.Optional[builtins.str] = None,
                replication_source_identifier: typing.Optional[builtins.str] = None,
                restore_to_point_in_time: typing.Optional[typing.Union[RdsClusterRestoreToPointInTime, typing.Dict[str, typing.Any]]] = None,
                s3_import: typing.Optional[typing.Union[RdsClusterS3Import, typing.Dict[str, typing.Any]]] = None,
                scaling_configuration: typing.Optional[typing.Union[RdsClusterScalingConfiguration, typing.Dict[str, typing.Any]]] = None,
                serverlessv2_scaling_configuration: typing.Optional[typing.Union[RdsClusterServerlessv2ScalingConfiguration, typing.Dict[str, typing.Any]]] = None,
                skip_final_snapshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                snapshot_identifier: typing.Optional[builtins.str] = None,
                source_region: typing.Optional[builtins.str] = None,
                storage_encrypted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                storage_type: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[RdsClusterTimeouts, typing.Dict[str, typing.Any]]] = None,
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
        config = RdsClusterConfig(
            allocated_storage=allocated_storage,
            allow_major_version_upgrade=allow_major_version_upgrade,
            apply_immediately=apply_immediately,
            availability_zones=availability_zones,
            backtrack_window=backtrack_window,
            backup_retention_period=backup_retention_period,
            cluster_identifier=cluster_identifier,
            cluster_identifier_prefix=cluster_identifier_prefix,
            cluster_members=cluster_members,
            copy_tags_to_snapshot=copy_tags_to_snapshot,
            database_name=database_name,
            db_cluster_instance_class=db_cluster_instance_class,
            db_cluster_parameter_group_name=db_cluster_parameter_group_name,
            db_instance_parameter_group_name=db_instance_parameter_group_name,
            db_subnet_group_name=db_subnet_group_name,
            deletion_protection=deletion_protection,
            enabled_cloudwatch_logs_exports=enabled_cloudwatch_logs_exports,
            enable_global_write_forwarding=enable_global_write_forwarding,
            enable_http_endpoint=enable_http_endpoint,
            engine=engine,
            engine_mode=engine_mode,
            engine_version=engine_version,
            final_snapshot_identifier=final_snapshot_identifier,
            global_cluster_identifier=global_cluster_identifier,
            iam_database_authentication_enabled=iam_database_authentication_enabled,
            iam_roles=iam_roles,
            id=id,
            iops=iops,
            kms_key_id=kms_key_id,
            master_password=master_password,
            master_username=master_username,
            network_type=network_type,
            port=port,
            preferred_backup_window=preferred_backup_window,
            preferred_maintenance_window=preferred_maintenance_window,
            replication_source_identifier=replication_source_identifier,
            restore_to_point_in_time=restore_to_point_in_time,
            s3_import=s3_import,
            scaling_configuration=scaling_configuration,
            serverlessv2_scaling_configuration=serverlessv2_scaling_configuration,
            skip_final_snapshot=skip_final_snapshot,
            snapshot_identifier=snapshot_identifier,
            source_region=source_region,
            storage_encrypted=storage_encrypted,
            storage_type=storage_type,
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

    @jsii.member(jsii_name="putRestoreToPointInTime")
    def put_restore_to_point_in_time(
        self,
        *,
        source_cluster_identifier: builtins.str,
        restore_to_time: typing.Optional[builtins.str] = None,
        restore_type: typing.Optional[builtins.str] = None,
        use_latest_restorable_time: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param source_cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#source_cluster_identifier RdsCluster#source_cluster_identifier}.
        :param restore_to_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#restore_to_time RdsCluster#restore_to_time}.
        :param restore_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#restore_type RdsCluster#restore_type}.
        :param use_latest_restorable_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#use_latest_restorable_time RdsCluster#use_latest_restorable_time}.
        '''
        value = RdsClusterRestoreToPointInTime(
            source_cluster_identifier=source_cluster_identifier,
            restore_to_time=restore_to_time,
            restore_type=restore_type,
            use_latest_restorable_time=use_latest_restorable_time,
        )

        return typing.cast(None, jsii.invoke(self, "putRestoreToPointInTime", [value]))

    @jsii.member(jsii_name="putS3Import")
    def put_s3_import(
        self,
        *,
        bucket_name: builtins.str,
        ingestion_role: builtins.str,
        source_engine: builtins.str,
        source_engine_version: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#bucket_name RdsCluster#bucket_name}.
        :param ingestion_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#ingestion_role RdsCluster#ingestion_role}.
        :param source_engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#source_engine RdsCluster#source_engine}.
        :param source_engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#source_engine_version RdsCluster#source_engine_version}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#bucket_prefix RdsCluster#bucket_prefix}.
        '''
        value = RdsClusterS3Import(
            bucket_name=bucket_name,
            ingestion_role=ingestion_role,
            source_engine=source_engine,
            source_engine_version=source_engine_version,
            bucket_prefix=bucket_prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putS3Import", [value]))

    @jsii.member(jsii_name="putScalingConfiguration")
    def put_scaling_configuration(
        self,
        *,
        auto_pause: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        seconds_until_auto_pause: typing.Optional[jsii.Number] = None,
        timeout_action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_pause: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#auto_pause RdsCluster#auto_pause}.
        :param max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#max_capacity RdsCluster#max_capacity}.
        :param min_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#min_capacity RdsCluster#min_capacity}.
        :param seconds_until_auto_pause: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#seconds_until_auto_pause RdsCluster#seconds_until_auto_pause}.
        :param timeout_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#timeout_action RdsCluster#timeout_action}.
        '''
        value = RdsClusterScalingConfiguration(
            auto_pause=auto_pause,
            max_capacity=max_capacity,
            min_capacity=min_capacity,
            seconds_until_auto_pause=seconds_until_auto_pause,
            timeout_action=timeout_action,
        )

        return typing.cast(None, jsii.invoke(self, "putScalingConfiguration", [value]))

    @jsii.member(jsii_name="putServerlessv2ScalingConfiguration")
    def put_serverlessv2_scaling_configuration(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
    ) -> None:
        '''
        :param max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#max_capacity RdsCluster#max_capacity}.
        :param min_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#min_capacity RdsCluster#min_capacity}.
        '''
        value = RdsClusterServerlessv2ScalingConfiguration(
            max_capacity=max_capacity, min_capacity=min_capacity
        )

        return typing.cast(None, jsii.invoke(self, "putServerlessv2ScalingConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#create RdsCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#delete RdsCluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#update RdsCluster#update}.
        '''
        value = RdsClusterTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAllocatedStorage")
    def reset_allocated_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllocatedStorage", []))

    @jsii.member(jsii_name="resetAllowMajorVersionUpgrade")
    def reset_allow_major_version_upgrade(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowMajorVersionUpgrade", []))

    @jsii.member(jsii_name="resetApplyImmediately")
    def reset_apply_immediately(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplyImmediately", []))

    @jsii.member(jsii_name="resetAvailabilityZones")
    def reset_availability_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityZones", []))

    @jsii.member(jsii_name="resetBacktrackWindow")
    def reset_backtrack_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBacktrackWindow", []))

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

    @jsii.member(jsii_name="resetCopyTagsToSnapshot")
    def reset_copy_tags_to_snapshot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyTagsToSnapshot", []))

    @jsii.member(jsii_name="resetDatabaseName")
    def reset_database_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseName", []))

    @jsii.member(jsii_name="resetDbClusterInstanceClass")
    def reset_db_cluster_instance_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbClusterInstanceClass", []))

    @jsii.member(jsii_name="resetDbClusterParameterGroupName")
    def reset_db_cluster_parameter_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbClusterParameterGroupName", []))

    @jsii.member(jsii_name="resetDbInstanceParameterGroupName")
    def reset_db_instance_parameter_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbInstanceParameterGroupName", []))

    @jsii.member(jsii_name="resetDbSubnetGroupName")
    def reset_db_subnet_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbSubnetGroupName", []))

    @jsii.member(jsii_name="resetDeletionProtection")
    def reset_deletion_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeletionProtection", []))

    @jsii.member(jsii_name="resetEnabledCloudwatchLogsExports")
    def reset_enabled_cloudwatch_logs_exports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabledCloudwatchLogsExports", []))

    @jsii.member(jsii_name="resetEnableGlobalWriteForwarding")
    def reset_enable_global_write_forwarding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableGlobalWriteForwarding", []))

    @jsii.member(jsii_name="resetEnableHttpEndpoint")
    def reset_enable_http_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableHttpEndpoint", []))

    @jsii.member(jsii_name="resetEngine")
    def reset_engine(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEngine", []))

    @jsii.member(jsii_name="resetEngineMode")
    def reset_engine_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEngineMode", []))

    @jsii.member(jsii_name="resetEngineVersion")
    def reset_engine_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEngineVersion", []))

    @jsii.member(jsii_name="resetFinalSnapshotIdentifier")
    def reset_final_snapshot_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFinalSnapshotIdentifier", []))

    @jsii.member(jsii_name="resetGlobalClusterIdentifier")
    def reset_global_cluster_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlobalClusterIdentifier", []))

    @jsii.member(jsii_name="resetIamDatabaseAuthenticationEnabled")
    def reset_iam_database_authentication_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamDatabaseAuthenticationEnabled", []))

    @jsii.member(jsii_name="resetIamRoles")
    def reset_iam_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamRoles", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetMasterPassword")
    def reset_master_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterPassword", []))

    @jsii.member(jsii_name="resetMasterUsername")
    def reset_master_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterUsername", []))

    @jsii.member(jsii_name="resetNetworkType")
    def reset_network_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkType", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPreferredBackupWindow")
    def reset_preferred_backup_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredBackupWindow", []))

    @jsii.member(jsii_name="resetPreferredMaintenanceWindow")
    def reset_preferred_maintenance_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredMaintenanceWindow", []))

    @jsii.member(jsii_name="resetReplicationSourceIdentifier")
    def reset_replication_source_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicationSourceIdentifier", []))

    @jsii.member(jsii_name="resetRestoreToPointInTime")
    def reset_restore_to_point_in_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestoreToPointInTime", []))

    @jsii.member(jsii_name="resetS3Import")
    def reset_s3_import(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Import", []))

    @jsii.member(jsii_name="resetScalingConfiguration")
    def reset_scaling_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScalingConfiguration", []))

    @jsii.member(jsii_name="resetServerlessv2ScalingConfiguration")
    def reset_serverlessv2_scaling_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerlessv2ScalingConfiguration", []))

    @jsii.member(jsii_name="resetSkipFinalSnapshot")
    def reset_skip_final_snapshot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipFinalSnapshot", []))

    @jsii.member(jsii_name="resetSnapshotIdentifier")
    def reset_snapshot_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotIdentifier", []))

    @jsii.member(jsii_name="resetSourceRegion")
    def reset_source_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceRegion", []))

    @jsii.member(jsii_name="resetStorageEncrypted")
    def reset_storage_encrypted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageEncrypted", []))

    @jsii.member(jsii_name="resetStorageType")
    def reset_storage_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageType", []))

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
    @jsii.member(jsii_name="engineVersionActual")
    def engine_version_actual(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineVersionActual"))

    @builtins.property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostedZoneId"))

    @builtins.property
    @jsii.member(jsii_name="readerEndpoint")
    def reader_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "readerEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="restoreToPointInTime")
    def restore_to_point_in_time(
        self,
    ) -> "RdsClusterRestoreToPointInTimeOutputReference":
        return typing.cast("RdsClusterRestoreToPointInTimeOutputReference", jsii.get(self, "restoreToPointInTime"))

    @builtins.property
    @jsii.member(jsii_name="s3Import")
    def s3_import(self) -> "RdsClusterS3ImportOutputReference":
        return typing.cast("RdsClusterS3ImportOutputReference", jsii.get(self, "s3Import"))

    @builtins.property
    @jsii.member(jsii_name="scalingConfiguration")
    def scaling_configuration(self) -> "RdsClusterScalingConfigurationOutputReference":
        return typing.cast("RdsClusterScalingConfigurationOutputReference", jsii.get(self, "scalingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="serverlessv2ScalingConfiguration")
    def serverlessv2_scaling_configuration(
        self,
    ) -> "RdsClusterServerlessv2ScalingConfigurationOutputReference":
        return typing.cast("RdsClusterServerlessv2ScalingConfigurationOutputReference", jsii.get(self, "serverlessv2ScalingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "RdsClusterTimeoutsOutputReference":
        return typing.cast("RdsClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="allocatedStorageInput")
    def allocated_storage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "allocatedStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="allowMajorVersionUpgradeInput")
    def allow_major_version_upgrade_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowMajorVersionUpgradeInput"))

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
    @jsii.member(jsii_name="backtrackWindowInput")
    def backtrack_window_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backtrackWindowInput"))

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
    @jsii.member(jsii_name="copyTagsToSnapshotInput")
    def copy_tags_to_snapshot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "copyTagsToSnapshotInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dbClusterInstanceClassInput")
    def db_cluster_instance_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbClusterInstanceClassInput"))

    @builtins.property
    @jsii.member(jsii_name="dbClusterParameterGroupNameInput")
    def db_cluster_parameter_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbClusterParameterGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dbInstanceParameterGroupNameInput")
    def db_instance_parameter_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbInstanceParameterGroupNameInput"))

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
    @jsii.member(jsii_name="enableGlobalWriteForwardingInput")
    def enable_global_write_forwarding_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableGlobalWriteForwardingInput"))

    @builtins.property
    @jsii.member(jsii_name="enableHttpEndpointInput")
    def enable_http_endpoint_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableHttpEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="engineInput")
    def engine_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineInput"))

    @builtins.property
    @jsii.member(jsii_name="engineModeInput")
    def engine_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineModeInput"))

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
    @jsii.member(jsii_name="iamDatabaseAuthenticationEnabledInput")
    def iam_database_authentication_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "iamDatabaseAuthenticationEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="iamRolesInput")
    def iam_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "iamRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

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
    @jsii.member(jsii_name="networkTypeInput")
    def network_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkTypeInput"))

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
    @jsii.member(jsii_name="replicationSourceIdentifierInput")
    def replication_source_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationSourceIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="restoreToPointInTimeInput")
    def restore_to_point_in_time_input(
        self,
    ) -> typing.Optional["RdsClusterRestoreToPointInTime"]:
        return typing.cast(typing.Optional["RdsClusterRestoreToPointInTime"], jsii.get(self, "restoreToPointInTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="s3ImportInput")
    def s3_import_input(self) -> typing.Optional["RdsClusterS3Import"]:
        return typing.cast(typing.Optional["RdsClusterS3Import"], jsii.get(self, "s3ImportInput"))

    @builtins.property
    @jsii.member(jsii_name="scalingConfigurationInput")
    def scaling_configuration_input(
        self,
    ) -> typing.Optional["RdsClusterScalingConfiguration"]:
        return typing.cast(typing.Optional["RdsClusterScalingConfiguration"], jsii.get(self, "scalingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="serverlessv2ScalingConfigurationInput")
    def serverlessv2_scaling_configuration_input(
        self,
    ) -> typing.Optional["RdsClusterServerlessv2ScalingConfiguration"]:
        return typing.cast(typing.Optional["RdsClusterServerlessv2ScalingConfiguration"], jsii.get(self, "serverlessv2ScalingConfigurationInput"))

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
    @jsii.member(jsii_name="sourceRegionInput")
    def source_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="storageEncryptedInput")
    def storage_encrypted_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "storageEncryptedInput"))

    @builtins.property
    @jsii.member(jsii_name="storageTypeInput")
    def storage_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageTypeInput"))

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
    ) -> typing.Optional[typing.Union["RdsClusterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["RdsClusterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIdsInput")
    def vpc_security_group_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSecurityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="allocatedStorage")
    def allocated_storage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "allocatedStorage"))

    @allocated_storage.setter
    def allocated_storage(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocatedStorage", value)

    @builtins.property
    @jsii.member(jsii_name="allowMajorVersionUpgrade")
    def allow_major_version_upgrade(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowMajorVersionUpgrade"))

    @allow_major_version_upgrade.setter
    def allow_major_version_upgrade(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowMajorVersionUpgrade", value)

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
    @jsii.member(jsii_name="backtrackWindow")
    def backtrack_window(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backtrackWindow"))

    @backtrack_window.setter
    def backtrack_window(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backtrackWindow", value)

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
    @jsii.member(jsii_name="copyTagsToSnapshot")
    def copy_tags_to_snapshot(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "copyTagsToSnapshot"))

    @copy_tags_to_snapshot.setter
    def copy_tags_to_snapshot(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyTagsToSnapshot", value)

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
    @jsii.member(jsii_name="dbClusterInstanceClass")
    def db_cluster_instance_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbClusterInstanceClass"))

    @db_cluster_instance_class.setter
    def db_cluster_instance_class(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbClusterInstanceClass", value)

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
    @jsii.member(jsii_name="dbInstanceParameterGroupName")
    def db_instance_parameter_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbInstanceParameterGroupName"))

    @db_instance_parameter_group_name.setter
    def db_instance_parameter_group_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbInstanceParameterGroupName", value)

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
    @jsii.member(jsii_name="enableGlobalWriteForwarding")
    def enable_global_write_forwarding(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableGlobalWriteForwarding"))

    @enable_global_write_forwarding.setter
    def enable_global_write_forwarding(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableGlobalWriteForwarding", value)

    @builtins.property
    @jsii.member(jsii_name="enableHttpEndpoint")
    def enable_http_endpoint(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableHttpEndpoint"))

    @enable_http_endpoint.setter
    def enable_http_endpoint(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableHttpEndpoint", value)

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
    @jsii.member(jsii_name="engineMode")
    def engine_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineMode"))

    @engine_mode.setter
    def engine_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineMode", value)

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
    @jsii.member(jsii_name="iamDatabaseAuthenticationEnabled")
    def iam_database_authentication_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "iamDatabaseAuthenticationEnabled"))

    @iam_database_authentication_enabled.setter
    def iam_database_authentication_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamDatabaseAuthenticationEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="iamRoles")
    def iam_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "iamRoles"))

    @iam_roles.setter
    def iam_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoles", value)

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
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

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
    @jsii.member(jsii_name="networkType")
    def network_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkType"))

    @network_type.setter
    def network_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkType", value)

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
    @jsii.member(jsii_name="replicationSourceIdentifier")
    def replication_source_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replicationSourceIdentifier"))

    @replication_source_identifier.setter
    def replication_source_identifier(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationSourceIdentifier", value)

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
    @jsii.member(jsii_name="sourceRegion")
    def source_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceRegion"))

    @source_region.setter
    def source_region(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceRegion", value)

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
    @jsii.member(jsii_name="storageType")
    def storage_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageType"))

    @storage_type.setter
    def storage_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageType", value)

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
    jsii_type="@cdktf/provider-aws.rdsCluster.RdsClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "allocated_storage": "allocatedStorage",
        "allow_major_version_upgrade": "allowMajorVersionUpgrade",
        "apply_immediately": "applyImmediately",
        "availability_zones": "availabilityZones",
        "backtrack_window": "backtrackWindow",
        "backup_retention_period": "backupRetentionPeriod",
        "cluster_identifier": "clusterIdentifier",
        "cluster_identifier_prefix": "clusterIdentifierPrefix",
        "cluster_members": "clusterMembers",
        "copy_tags_to_snapshot": "copyTagsToSnapshot",
        "database_name": "databaseName",
        "db_cluster_instance_class": "dbClusterInstanceClass",
        "db_cluster_parameter_group_name": "dbClusterParameterGroupName",
        "db_instance_parameter_group_name": "dbInstanceParameterGroupName",
        "db_subnet_group_name": "dbSubnetGroupName",
        "deletion_protection": "deletionProtection",
        "enabled_cloudwatch_logs_exports": "enabledCloudwatchLogsExports",
        "enable_global_write_forwarding": "enableGlobalWriteForwarding",
        "enable_http_endpoint": "enableHttpEndpoint",
        "engine": "engine",
        "engine_mode": "engineMode",
        "engine_version": "engineVersion",
        "final_snapshot_identifier": "finalSnapshotIdentifier",
        "global_cluster_identifier": "globalClusterIdentifier",
        "iam_database_authentication_enabled": "iamDatabaseAuthenticationEnabled",
        "iam_roles": "iamRoles",
        "id": "id",
        "iops": "iops",
        "kms_key_id": "kmsKeyId",
        "master_password": "masterPassword",
        "master_username": "masterUsername",
        "network_type": "networkType",
        "port": "port",
        "preferred_backup_window": "preferredBackupWindow",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "replication_source_identifier": "replicationSourceIdentifier",
        "restore_to_point_in_time": "restoreToPointInTime",
        "s3_import": "s3Import",
        "scaling_configuration": "scalingConfiguration",
        "serverlessv2_scaling_configuration": "serverlessv2ScalingConfiguration",
        "skip_final_snapshot": "skipFinalSnapshot",
        "snapshot_identifier": "snapshotIdentifier",
        "source_region": "sourceRegion",
        "storage_encrypted": "storageEncrypted",
        "storage_type": "storageType",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
    },
)
class RdsClusterConfig(cdktf.TerraformMetaArguments):
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
        allocated_storage: typing.Optional[jsii.Number] = None,
        allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        apply_immediately: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        backtrack_window: typing.Optional[jsii.Number] = None,
        backup_retention_period: typing.Optional[jsii.Number] = None,
        cluster_identifier: typing.Optional[builtins.str] = None,
        cluster_identifier_prefix: typing.Optional[builtins.str] = None,
        cluster_members: typing.Optional[typing.Sequence[builtins.str]] = None,
        copy_tags_to_snapshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        database_name: typing.Optional[builtins.str] = None,
        db_cluster_instance_class: typing.Optional[builtins.str] = None,
        db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        db_instance_parameter_group_name: typing.Optional[builtins.str] = None,
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enabled_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_global_write_forwarding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_http_endpoint: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        engine: typing.Optional[builtins.str] = None,
        engine_mode: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        final_snapshot_identifier: typing.Optional[builtins.str] = None,
        global_cluster_identifier: typing.Optional[builtins.str] = None,
        iam_database_authentication_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        master_password: typing.Optional[builtins.str] = None,
        master_username: typing.Optional[builtins.str] = None,
        network_type: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        replication_source_identifier: typing.Optional[builtins.str] = None,
        restore_to_point_in_time: typing.Optional[typing.Union["RdsClusterRestoreToPointInTime", typing.Dict[str, typing.Any]]] = None,
        s3_import: typing.Optional[typing.Union["RdsClusterS3Import", typing.Dict[str, typing.Any]]] = None,
        scaling_configuration: typing.Optional[typing.Union["RdsClusterScalingConfiguration", typing.Dict[str, typing.Any]]] = None,
        serverlessv2_scaling_configuration: typing.Optional[typing.Union["RdsClusterServerlessv2ScalingConfiguration", typing.Dict[str, typing.Any]]] = None,
        skip_final_snapshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        snapshot_identifier: typing.Optional[builtins.str] = None,
        source_region: typing.Optional[builtins.str] = None,
        storage_encrypted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        storage_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["RdsClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
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
        :param allocated_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#allocated_storage RdsCluster#allocated_storage}.
        :param allow_major_version_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#allow_major_version_upgrade RdsCluster#allow_major_version_upgrade}.
        :param apply_immediately: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#apply_immediately RdsCluster#apply_immediately}.
        :param availability_zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#availability_zones RdsCluster#availability_zones}.
        :param backtrack_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#backtrack_window RdsCluster#backtrack_window}.
        :param backup_retention_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#backup_retention_period RdsCluster#backup_retention_period}.
        :param cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#cluster_identifier RdsCluster#cluster_identifier}.
        :param cluster_identifier_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#cluster_identifier_prefix RdsCluster#cluster_identifier_prefix}.
        :param cluster_members: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#cluster_members RdsCluster#cluster_members}.
        :param copy_tags_to_snapshot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#copy_tags_to_snapshot RdsCluster#copy_tags_to_snapshot}.
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#database_name RdsCluster#database_name}.
        :param db_cluster_instance_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#db_cluster_instance_class RdsCluster#db_cluster_instance_class}.
        :param db_cluster_parameter_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#db_cluster_parameter_group_name RdsCluster#db_cluster_parameter_group_name}.
        :param db_instance_parameter_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#db_instance_parameter_group_name RdsCluster#db_instance_parameter_group_name}.
        :param db_subnet_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#db_subnet_group_name RdsCluster#db_subnet_group_name}.
        :param deletion_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#deletion_protection RdsCluster#deletion_protection}.
        :param enabled_cloudwatch_logs_exports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#enabled_cloudwatch_logs_exports RdsCluster#enabled_cloudwatch_logs_exports}.
        :param enable_global_write_forwarding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#enable_global_write_forwarding RdsCluster#enable_global_write_forwarding}.
        :param enable_http_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#enable_http_endpoint RdsCluster#enable_http_endpoint}.
        :param engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#engine RdsCluster#engine}.
        :param engine_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#engine_mode RdsCluster#engine_mode}.
        :param engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#engine_version RdsCluster#engine_version}.
        :param final_snapshot_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#final_snapshot_identifier RdsCluster#final_snapshot_identifier}.
        :param global_cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#global_cluster_identifier RdsCluster#global_cluster_identifier}.
        :param iam_database_authentication_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#iam_database_authentication_enabled RdsCluster#iam_database_authentication_enabled}.
        :param iam_roles: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#iam_roles RdsCluster#iam_roles}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#id RdsCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#iops RdsCluster#iops}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#kms_key_id RdsCluster#kms_key_id}.
        :param master_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#master_password RdsCluster#master_password}.
        :param master_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#master_username RdsCluster#master_username}.
        :param network_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#network_type RdsCluster#network_type}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#port RdsCluster#port}.
        :param preferred_backup_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#preferred_backup_window RdsCluster#preferred_backup_window}.
        :param preferred_maintenance_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#preferred_maintenance_window RdsCluster#preferred_maintenance_window}.
        :param replication_source_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#replication_source_identifier RdsCluster#replication_source_identifier}.
        :param restore_to_point_in_time: restore_to_point_in_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#restore_to_point_in_time RdsCluster#restore_to_point_in_time}
        :param s3_import: s3_import block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#s3_import RdsCluster#s3_import}
        :param scaling_configuration: scaling_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#scaling_configuration RdsCluster#scaling_configuration}
        :param serverlessv2_scaling_configuration: serverlessv2_scaling_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#serverlessv2_scaling_configuration RdsCluster#serverlessv2_scaling_configuration}
        :param skip_final_snapshot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#skip_final_snapshot RdsCluster#skip_final_snapshot}.
        :param snapshot_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#snapshot_identifier RdsCluster#snapshot_identifier}.
        :param source_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#source_region RdsCluster#source_region}.
        :param storage_encrypted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#storage_encrypted RdsCluster#storage_encrypted}.
        :param storage_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#storage_type RdsCluster#storage_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#tags RdsCluster#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#tags_all RdsCluster#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#timeouts RdsCluster#timeouts}
        :param vpc_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#vpc_security_group_ids RdsCluster#vpc_security_group_ids}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(restore_to_point_in_time, dict):
            restore_to_point_in_time = RdsClusterRestoreToPointInTime(**restore_to_point_in_time)
        if isinstance(s3_import, dict):
            s3_import = RdsClusterS3Import(**s3_import)
        if isinstance(scaling_configuration, dict):
            scaling_configuration = RdsClusterScalingConfiguration(**scaling_configuration)
        if isinstance(serverlessv2_scaling_configuration, dict):
            serverlessv2_scaling_configuration = RdsClusterServerlessv2ScalingConfiguration(**serverlessv2_scaling_configuration)
        if isinstance(timeouts, dict):
            timeouts = RdsClusterTimeouts(**timeouts)
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
                allocated_storage: typing.Optional[jsii.Number] = None,
                allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                apply_immediately: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
                backtrack_window: typing.Optional[jsii.Number] = None,
                backup_retention_period: typing.Optional[jsii.Number] = None,
                cluster_identifier: typing.Optional[builtins.str] = None,
                cluster_identifier_prefix: typing.Optional[builtins.str] = None,
                cluster_members: typing.Optional[typing.Sequence[builtins.str]] = None,
                copy_tags_to_snapshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                database_name: typing.Optional[builtins.str] = None,
                db_cluster_instance_class: typing.Optional[builtins.str] = None,
                db_cluster_parameter_group_name: typing.Optional[builtins.str] = None,
                db_instance_parameter_group_name: typing.Optional[builtins.str] = None,
                db_subnet_group_name: typing.Optional[builtins.str] = None,
                deletion_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                enabled_cloudwatch_logs_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
                enable_global_write_forwarding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                enable_http_endpoint: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                engine: typing.Optional[builtins.str] = None,
                engine_mode: typing.Optional[builtins.str] = None,
                engine_version: typing.Optional[builtins.str] = None,
                final_snapshot_identifier: typing.Optional[builtins.str] = None,
                global_cluster_identifier: typing.Optional[builtins.str] = None,
                iam_database_authentication_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
                id: typing.Optional[builtins.str] = None,
                iops: typing.Optional[jsii.Number] = None,
                kms_key_id: typing.Optional[builtins.str] = None,
                master_password: typing.Optional[builtins.str] = None,
                master_username: typing.Optional[builtins.str] = None,
                network_type: typing.Optional[builtins.str] = None,
                port: typing.Optional[jsii.Number] = None,
                preferred_backup_window: typing.Optional[builtins.str] = None,
                preferred_maintenance_window: typing.Optional[builtins.str] = None,
                replication_source_identifier: typing.Optional[builtins.str] = None,
                restore_to_point_in_time: typing.Optional[typing.Union[RdsClusterRestoreToPointInTime, typing.Dict[str, typing.Any]]] = None,
                s3_import: typing.Optional[typing.Union[RdsClusterS3Import, typing.Dict[str, typing.Any]]] = None,
                scaling_configuration: typing.Optional[typing.Union[RdsClusterScalingConfiguration, typing.Dict[str, typing.Any]]] = None,
                serverlessv2_scaling_configuration: typing.Optional[typing.Union[RdsClusterServerlessv2ScalingConfiguration, typing.Dict[str, typing.Any]]] = None,
                skip_final_snapshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                snapshot_identifier: typing.Optional[builtins.str] = None,
                source_region: typing.Optional[builtins.str] = None,
                storage_encrypted: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                storage_type: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[RdsClusterTimeouts, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument allocated_storage", value=allocated_storage, expected_type=type_hints["allocated_storage"])
            check_type(argname="argument allow_major_version_upgrade", value=allow_major_version_upgrade, expected_type=type_hints["allow_major_version_upgrade"])
            check_type(argname="argument apply_immediately", value=apply_immediately, expected_type=type_hints["apply_immediately"])
            check_type(argname="argument availability_zones", value=availability_zones, expected_type=type_hints["availability_zones"])
            check_type(argname="argument backtrack_window", value=backtrack_window, expected_type=type_hints["backtrack_window"])
            check_type(argname="argument backup_retention_period", value=backup_retention_period, expected_type=type_hints["backup_retention_period"])
            check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
            check_type(argname="argument cluster_identifier_prefix", value=cluster_identifier_prefix, expected_type=type_hints["cluster_identifier_prefix"])
            check_type(argname="argument cluster_members", value=cluster_members, expected_type=type_hints["cluster_members"])
            check_type(argname="argument copy_tags_to_snapshot", value=copy_tags_to_snapshot, expected_type=type_hints["copy_tags_to_snapshot"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument db_cluster_instance_class", value=db_cluster_instance_class, expected_type=type_hints["db_cluster_instance_class"])
            check_type(argname="argument db_cluster_parameter_group_name", value=db_cluster_parameter_group_name, expected_type=type_hints["db_cluster_parameter_group_name"])
            check_type(argname="argument db_instance_parameter_group_name", value=db_instance_parameter_group_name, expected_type=type_hints["db_instance_parameter_group_name"])
            check_type(argname="argument db_subnet_group_name", value=db_subnet_group_name, expected_type=type_hints["db_subnet_group_name"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument enabled_cloudwatch_logs_exports", value=enabled_cloudwatch_logs_exports, expected_type=type_hints["enabled_cloudwatch_logs_exports"])
            check_type(argname="argument enable_global_write_forwarding", value=enable_global_write_forwarding, expected_type=type_hints["enable_global_write_forwarding"])
            check_type(argname="argument enable_http_endpoint", value=enable_http_endpoint, expected_type=type_hints["enable_http_endpoint"])
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            check_type(argname="argument engine_mode", value=engine_mode, expected_type=type_hints["engine_mode"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument final_snapshot_identifier", value=final_snapshot_identifier, expected_type=type_hints["final_snapshot_identifier"])
            check_type(argname="argument global_cluster_identifier", value=global_cluster_identifier, expected_type=type_hints["global_cluster_identifier"])
            check_type(argname="argument iam_database_authentication_enabled", value=iam_database_authentication_enabled, expected_type=type_hints["iam_database_authentication_enabled"])
            check_type(argname="argument iam_roles", value=iam_roles, expected_type=type_hints["iam_roles"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument master_password", value=master_password, expected_type=type_hints["master_password"])
            check_type(argname="argument master_username", value=master_username, expected_type=type_hints["master_username"])
            check_type(argname="argument network_type", value=network_type, expected_type=type_hints["network_type"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument preferred_backup_window", value=preferred_backup_window, expected_type=type_hints["preferred_backup_window"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument replication_source_identifier", value=replication_source_identifier, expected_type=type_hints["replication_source_identifier"])
            check_type(argname="argument restore_to_point_in_time", value=restore_to_point_in_time, expected_type=type_hints["restore_to_point_in_time"])
            check_type(argname="argument s3_import", value=s3_import, expected_type=type_hints["s3_import"])
            check_type(argname="argument scaling_configuration", value=scaling_configuration, expected_type=type_hints["scaling_configuration"])
            check_type(argname="argument serverlessv2_scaling_configuration", value=serverlessv2_scaling_configuration, expected_type=type_hints["serverlessv2_scaling_configuration"])
            check_type(argname="argument skip_final_snapshot", value=skip_final_snapshot, expected_type=type_hints["skip_final_snapshot"])
            check_type(argname="argument snapshot_identifier", value=snapshot_identifier, expected_type=type_hints["snapshot_identifier"])
            check_type(argname="argument source_region", value=source_region, expected_type=type_hints["source_region"])
            check_type(argname="argument storage_encrypted", value=storage_encrypted, expected_type=type_hints["storage_encrypted"])
            check_type(argname="argument storage_type", value=storage_type, expected_type=type_hints["storage_type"])
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
        if allocated_storage is not None:
            self._values["allocated_storage"] = allocated_storage
        if allow_major_version_upgrade is not None:
            self._values["allow_major_version_upgrade"] = allow_major_version_upgrade
        if apply_immediately is not None:
            self._values["apply_immediately"] = apply_immediately
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if backtrack_window is not None:
            self._values["backtrack_window"] = backtrack_window
        if backup_retention_period is not None:
            self._values["backup_retention_period"] = backup_retention_period
        if cluster_identifier is not None:
            self._values["cluster_identifier"] = cluster_identifier
        if cluster_identifier_prefix is not None:
            self._values["cluster_identifier_prefix"] = cluster_identifier_prefix
        if cluster_members is not None:
            self._values["cluster_members"] = cluster_members
        if copy_tags_to_snapshot is not None:
            self._values["copy_tags_to_snapshot"] = copy_tags_to_snapshot
        if database_name is not None:
            self._values["database_name"] = database_name
        if db_cluster_instance_class is not None:
            self._values["db_cluster_instance_class"] = db_cluster_instance_class
        if db_cluster_parameter_group_name is not None:
            self._values["db_cluster_parameter_group_name"] = db_cluster_parameter_group_name
        if db_instance_parameter_group_name is not None:
            self._values["db_instance_parameter_group_name"] = db_instance_parameter_group_name
        if db_subnet_group_name is not None:
            self._values["db_subnet_group_name"] = db_subnet_group_name
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if enabled_cloudwatch_logs_exports is not None:
            self._values["enabled_cloudwatch_logs_exports"] = enabled_cloudwatch_logs_exports
        if enable_global_write_forwarding is not None:
            self._values["enable_global_write_forwarding"] = enable_global_write_forwarding
        if enable_http_endpoint is not None:
            self._values["enable_http_endpoint"] = enable_http_endpoint
        if engine is not None:
            self._values["engine"] = engine
        if engine_mode is not None:
            self._values["engine_mode"] = engine_mode
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if final_snapshot_identifier is not None:
            self._values["final_snapshot_identifier"] = final_snapshot_identifier
        if global_cluster_identifier is not None:
            self._values["global_cluster_identifier"] = global_cluster_identifier
        if iam_database_authentication_enabled is not None:
            self._values["iam_database_authentication_enabled"] = iam_database_authentication_enabled
        if iam_roles is not None:
            self._values["iam_roles"] = iam_roles
        if id is not None:
            self._values["id"] = id
        if iops is not None:
            self._values["iops"] = iops
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if master_password is not None:
            self._values["master_password"] = master_password
        if master_username is not None:
            self._values["master_username"] = master_username
        if network_type is not None:
            self._values["network_type"] = network_type
        if port is not None:
            self._values["port"] = port
        if preferred_backup_window is not None:
            self._values["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if replication_source_identifier is not None:
            self._values["replication_source_identifier"] = replication_source_identifier
        if restore_to_point_in_time is not None:
            self._values["restore_to_point_in_time"] = restore_to_point_in_time
        if s3_import is not None:
            self._values["s3_import"] = s3_import
        if scaling_configuration is not None:
            self._values["scaling_configuration"] = scaling_configuration
        if serverlessv2_scaling_configuration is not None:
            self._values["serverlessv2_scaling_configuration"] = serverlessv2_scaling_configuration
        if skip_final_snapshot is not None:
            self._values["skip_final_snapshot"] = skip_final_snapshot
        if snapshot_identifier is not None:
            self._values["snapshot_identifier"] = snapshot_identifier
        if source_region is not None:
            self._values["source_region"] = source_region
        if storage_encrypted is not None:
            self._values["storage_encrypted"] = storage_encrypted
        if storage_type is not None:
            self._values["storage_type"] = storage_type
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
    def allocated_storage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#allocated_storage RdsCluster#allocated_storage}.'''
        result = self._values.get("allocated_storage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def allow_major_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#allow_major_version_upgrade RdsCluster#allow_major_version_upgrade}.'''
        result = self._values.get("allow_major_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def apply_immediately(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#apply_immediately RdsCluster#apply_immediately}.'''
        result = self._values.get("apply_immediately")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#availability_zones RdsCluster#availability_zones}.'''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def backtrack_window(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#backtrack_window RdsCluster#backtrack_window}.'''
        result = self._values.get("backtrack_window")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def backup_retention_period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#backup_retention_period RdsCluster#backup_retention_period}.'''
        result = self._values.get("backup_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#cluster_identifier RdsCluster#cluster_identifier}.'''
        result = self._values.get("cluster_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_identifier_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#cluster_identifier_prefix RdsCluster#cluster_identifier_prefix}.'''
        result = self._values.get("cluster_identifier_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_members(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#cluster_members RdsCluster#cluster_members}.'''
        result = self._values.get("cluster_members")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def copy_tags_to_snapshot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#copy_tags_to_snapshot RdsCluster#copy_tags_to_snapshot}.'''
        result = self._values.get("copy_tags_to_snapshot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#database_name RdsCluster#database_name}.'''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_cluster_instance_class(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#db_cluster_instance_class RdsCluster#db_cluster_instance_class}.'''
        result = self._values.get("db_cluster_instance_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_cluster_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#db_cluster_parameter_group_name RdsCluster#db_cluster_parameter_group_name}.'''
        result = self._values.get("db_cluster_parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_instance_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#db_instance_parameter_group_name RdsCluster#db_instance_parameter_group_name}.'''
        result = self._values.get("db_instance_parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#db_subnet_group_name RdsCluster#db_subnet_group_name}.'''
        result = self._values.get("db_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#deletion_protection RdsCluster#deletion_protection}.'''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enabled_cloudwatch_logs_exports(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#enabled_cloudwatch_logs_exports RdsCluster#enabled_cloudwatch_logs_exports}.'''
        result = self._values.get("enabled_cloudwatch_logs_exports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enable_global_write_forwarding(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#enable_global_write_forwarding RdsCluster#enable_global_write_forwarding}.'''
        result = self._values.get("enable_global_write_forwarding")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_http_endpoint(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#enable_http_endpoint RdsCluster#enable_http_endpoint}.'''
        result = self._values.get("enable_http_endpoint")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def engine(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#engine RdsCluster#engine}.'''
        result = self._values.get("engine")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#engine_mode RdsCluster#engine_mode}.'''
        result = self._values.get("engine_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#engine_version RdsCluster#engine_version}.'''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def final_snapshot_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#final_snapshot_identifier RdsCluster#final_snapshot_identifier}.'''
        result = self._values.get("final_snapshot_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#global_cluster_identifier RdsCluster#global_cluster_identifier}.'''
        result = self._values.get("global_cluster_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_database_authentication_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#iam_database_authentication_enabled RdsCluster#iam_database_authentication_enabled}.'''
        result = self._values.get("iam_database_authentication_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def iam_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#iam_roles RdsCluster#iam_roles}.'''
        result = self._values.get("iam_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#id RdsCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#iops RdsCluster#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#kms_key_id RdsCluster#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#master_password RdsCluster#master_password}.'''
        result = self._values.get("master_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#master_username RdsCluster#master_username}.'''
        result = self._values.get("master_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#network_type RdsCluster#network_type}.'''
        result = self._values.get("network_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#port RdsCluster#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#preferred_backup_window RdsCluster#preferred_backup_window}.'''
        result = self._values.get("preferred_backup_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#preferred_maintenance_window RdsCluster#preferred_maintenance_window}.'''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_source_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#replication_source_identifier RdsCluster#replication_source_identifier}.'''
        result = self._values.get("replication_source_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restore_to_point_in_time(
        self,
    ) -> typing.Optional["RdsClusterRestoreToPointInTime"]:
        '''restore_to_point_in_time block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#restore_to_point_in_time RdsCluster#restore_to_point_in_time}
        '''
        result = self._values.get("restore_to_point_in_time")
        return typing.cast(typing.Optional["RdsClusterRestoreToPointInTime"], result)

    @builtins.property
    def s3_import(self) -> typing.Optional["RdsClusterS3Import"]:
        '''s3_import block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#s3_import RdsCluster#s3_import}
        '''
        result = self._values.get("s3_import")
        return typing.cast(typing.Optional["RdsClusterS3Import"], result)

    @builtins.property
    def scaling_configuration(
        self,
    ) -> typing.Optional["RdsClusterScalingConfiguration"]:
        '''scaling_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#scaling_configuration RdsCluster#scaling_configuration}
        '''
        result = self._values.get("scaling_configuration")
        return typing.cast(typing.Optional["RdsClusterScalingConfiguration"], result)

    @builtins.property
    def serverlessv2_scaling_configuration(
        self,
    ) -> typing.Optional["RdsClusterServerlessv2ScalingConfiguration"]:
        '''serverlessv2_scaling_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#serverlessv2_scaling_configuration RdsCluster#serverlessv2_scaling_configuration}
        '''
        result = self._values.get("serverlessv2_scaling_configuration")
        return typing.cast(typing.Optional["RdsClusterServerlessv2ScalingConfiguration"], result)

    @builtins.property
    def skip_final_snapshot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#skip_final_snapshot RdsCluster#skip_final_snapshot}.'''
        result = self._values.get("skip_final_snapshot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def snapshot_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#snapshot_identifier RdsCluster#snapshot_identifier}.'''
        result = self._values.get("snapshot_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#source_region RdsCluster#source_region}.'''
        result = self._values.get("source_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#storage_encrypted RdsCluster#storage_encrypted}.'''
        result = self._values.get("storage_encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def storage_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#storage_type RdsCluster#storage_type}.'''
        result = self._values.get("storage_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#tags RdsCluster#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#tags_all RdsCluster#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["RdsClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#timeouts RdsCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["RdsClusterTimeouts"], result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#vpc_security_group_ids RdsCluster#vpc_security_group_ids}.'''
        result = self._values.get("vpc_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RdsClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.rdsCluster.RdsClusterRestoreToPointInTime",
    jsii_struct_bases=[],
    name_mapping={
        "source_cluster_identifier": "sourceClusterIdentifier",
        "restore_to_time": "restoreToTime",
        "restore_type": "restoreType",
        "use_latest_restorable_time": "useLatestRestorableTime",
    },
)
class RdsClusterRestoreToPointInTime:
    def __init__(
        self,
        *,
        source_cluster_identifier: builtins.str,
        restore_to_time: typing.Optional[builtins.str] = None,
        restore_type: typing.Optional[builtins.str] = None,
        use_latest_restorable_time: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param source_cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#source_cluster_identifier RdsCluster#source_cluster_identifier}.
        :param restore_to_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#restore_to_time RdsCluster#restore_to_time}.
        :param restore_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#restore_type RdsCluster#restore_type}.
        :param use_latest_restorable_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#use_latest_restorable_time RdsCluster#use_latest_restorable_time}.
        '''
        if __debug__:
            def stub(
                *,
                source_cluster_identifier: builtins.str,
                restore_to_time: typing.Optional[builtins.str] = None,
                restore_type: typing.Optional[builtins.str] = None,
                use_latest_restorable_time: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument source_cluster_identifier", value=source_cluster_identifier, expected_type=type_hints["source_cluster_identifier"])
            check_type(argname="argument restore_to_time", value=restore_to_time, expected_type=type_hints["restore_to_time"])
            check_type(argname="argument restore_type", value=restore_type, expected_type=type_hints["restore_type"])
            check_type(argname="argument use_latest_restorable_time", value=use_latest_restorable_time, expected_type=type_hints["use_latest_restorable_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "source_cluster_identifier": source_cluster_identifier,
        }
        if restore_to_time is not None:
            self._values["restore_to_time"] = restore_to_time
        if restore_type is not None:
            self._values["restore_type"] = restore_type
        if use_latest_restorable_time is not None:
            self._values["use_latest_restorable_time"] = use_latest_restorable_time

    @builtins.property
    def source_cluster_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#source_cluster_identifier RdsCluster#source_cluster_identifier}.'''
        result = self._values.get("source_cluster_identifier")
        assert result is not None, "Required property 'source_cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def restore_to_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#restore_to_time RdsCluster#restore_to_time}.'''
        result = self._values.get("restore_to_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restore_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#restore_type RdsCluster#restore_type}.'''
        result = self._values.get("restore_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_latest_restorable_time(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#use_latest_restorable_time RdsCluster#use_latest_restorable_time}.'''
        result = self._values.get("use_latest_restorable_time")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RdsClusterRestoreToPointInTime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RdsClusterRestoreToPointInTimeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.rdsCluster.RdsClusterRestoreToPointInTimeOutputReference",
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

    @jsii.member(jsii_name="resetRestoreToTime")
    def reset_restore_to_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestoreToTime", []))

    @jsii.member(jsii_name="resetRestoreType")
    def reset_restore_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestoreType", []))

    @jsii.member(jsii_name="resetUseLatestRestorableTime")
    def reset_use_latest_restorable_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseLatestRestorableTime", []))

    @builtins.property
    @jsii.member(jsii_name="restoreToTimeInput")
    def restore_to_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restoreToTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="restoreTypeInput")
    def restore_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restoreTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceClusterIdentifierInput")
    def source_cluster_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceClusterIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="useLatestRestorableTimeInput")
    def use_latest_restorable_time_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useLatestRestorableTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="restoreToTime")
    def restore_to_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restoreToTime"))

    @restore_to_time.setter
    def restore_to_time(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreToTime", value)

    @builtins.property
    @jsii.member(jsii_name="restoreType")
    def restore_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restoreType"))

    @restore_type.setter
    def restore_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restoreType", value)

    @builtins.property
    @jsii.member(jsii_name="sourceClusterIdentifier")
    def source_cluster_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceClusterIdentifier"))

    @source_cluster_identifier.setter
    def source_cluster_identifier(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceClusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="useLatestRestorableTime")
    def use_latest_restorable_time(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useLatestRestorableTime"))

    @use_latest_restorable_time.setter
    def use_latest_restorable_time(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useLatestRestorableTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RdsClusterRestoreToPointInTime]:
        return typing.cast(typing.Optional[RdsClusterRestoreToPointInTime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RdsClusterRestoreToPointInTime],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[RdsClusterRestoreToPointInTime]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.rdsCluster.RdsClusterS3Import",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "ingestion_role": "ingestionRole",
        "source_engine": "sourceEngine",
        "source_engine_version": "sourceEngineVersion",
        "bucket_prefix": "bucketPrefix",
    },
)
class RdsClusterS3Import:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        ingestion_role: builtins.str,
        source_engine: builtins.str,
        source_engine_version: builtins.str,
        bucket_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#bucket_name RdsCluster#bucket_name}.
        :param ingestion_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#ingestion_role RdsCluster#ingestion_role}.
        :param source_engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#source_engine RdsCluster#source_engine}.
        :param source_engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#source_engine_version RdsCluster#source_engine_version}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#bucket_prefix RdsCluster#bucket_prefix}.
        '''
        if __debug__:
            def stub(
                *,
                bucket_name: builtins.str,
                ingestion_role: builtins.str,
                source_engine: builtins.str,
                source_engine_version: builtins.str,
                bucket_prefix: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument ingestion_role", value=ingestion_role, expected_type=type_hints["ingestion_role"])
            check_type(argname="argument source_engine", value=source_engine, expected_type=type_hints["source_engine"])
            check_type(argname="argument source_engine_version", value=source_engine_version, expected_type=type_hints["source_engine_version"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
            "ingestion_role": ingestion_role,
            "source_engine": source_engine,
            "source_engine_version": source_engine_version,
        }
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#bucket_name RdsCluster#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ingestion_role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#ingestion_role RdsCluster#ingestion_role}.'''
        result = self._values.get("ingestion_role")
        assert result is not None, "Required property 'ingestion_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_engine(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#source_engine RdsCluster#source_engine}.'''
        result = self._values.get("source_engine")
        assert result is not None, "Required property 'source_engine' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_engine_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#source_engine_version RdsCluster#source_engine_version}.'''
        result = self._values.get("source_engine_version")
        assert result is not None, "Required property 'source_engine_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#bucket_prefix RdsCluster#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RdsClusterS3Import(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RdsClusterS3ImportOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.rdsCluster.RdsClusterS3ImportOutputReference",
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

    @jsii.member(jsii_name="resetBucketPrefix")
    def reset_bucket_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucketPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="ingestionRoleInput")
    def ingestion_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ingestionRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceEngineInput")
    def source_engine_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceEngineInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceEngineVersionInput")
    def source_engine_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceEngineVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="ingestionRole")
    def ingestion_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ingestionRole"))

    @ingestion_role.setter
    def ingestion_role(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingestionRole", value)

    @builtins.property
    @jsii.member(jsii_name="sourceEngine")
    def source_engine(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceEngine"))

    @source_engine.setter
    def source_engine(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceEngine", value)

    @builtins.property
    @jsii.member(jsii_name="sourceEngineVersion")
    def source_engine_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceEngineVersion"))

    @source_engine_version.setter
    def source_engine_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceEngineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RdsClusterS3Import]:
        return typing.cast(typing.Optional[RdsClusterS3Import], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RdsClusterS3Import]) -> None:
        if __debug__:
            def stub(value: typing.Optional[RdsClusterS3Import]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.rdsCluster.RdsClusterScalingConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "auto_pause": "autoPause",
        "max_capacity": "maxCapacity",
        "min_capacity": "minCapacity",
        "seconds_until_auto_pause": "secondsUntilAutoPause",
        "timeout_action": "timeoutAction",
    },
)
class RdsClusterScalingConfiguration:
    def __init__(
        self,
        *,
        auto_pause: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        seconds_until_auto_pause: typing.Optional[jsii.Number] = None,
        timeout_action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_pause: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#auto_pause RdsCluster#auto_pause}.
        :param max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#max_capacity RdsCluster#max_capacity}.
        :param min_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#min_capacity RdsCluster#min_capacity}.
        :param seconds_until_auto_pause: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#seconds_until_auto_pause RdsCluster#seconds_until_auto_pause}.
        :param timeout_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#timeout_action RdsCluster#timeout_action}.
        '''
        if __debug__:
            def stub(
                *,
                auto_pause: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                max_capacity: typing.Optional[jsii.Number] = None,
                min_capacity: typing.Optional[jsii.Number] = None,
                seconds_until_auto_pause: typing.Optional[jsii.Number] = None,
                timeout_action: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument auto_pause", value=auto_pause, expected_type=type_hints["auto_pause"])
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
            check_type(argname="argument seconds_until_auto_pause", value=seconds_until_auto_pause, expected_type=type_hints["seconds_until_auto_pause"])
            check_type(argname="argument timeout_action", value=timeout_action, expected_type=type_hints["timeout_action"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_pause is not None:
            self._values["auto_pause"] = auto_pause
        if max_capacity is not None:
            self._values["max_capacity"] = max_capacity
        if min_capacity is not None:
            self._values["min_capacity"] = min_capacity
        if seconds_until_auto_pause is not None:
            self._values["seconds_until_auto_pause"] = seconds_until_auto_pause
        if timeout_action is not None:
            self._values["timeout_action"] = timeout_action

    @builtins.property
    def auto_pause(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#auto_pause RdsCluster#auto_pause}.'''
        result = self._values.get("auto_pause")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#max_capacity RdsCluster#max_capacity}.'''
        result = self._values.get("max_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#min_capacity RdsCluster#min_capacity}.'''
        result = self._values.get("min_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def seconds_until_auto_pause(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#seconds_until_auto_pause RdsCluster#seconds_until_auto_pause}.'''
        result = self._values.get("seconds_until_auto_pause")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#timeout_action RdsCluster#timeout_action}.'''
        result = self._values.get("timeout_action")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RdsClusterScalingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RdsClusterScalingConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.rdsCluster.RdsClusterScalingConfigurationOutputReference",
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

    @jsii.member(jsii_name="resetAutoPause")
    def reset_auto_pause(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoPause", []))

    @jsii.member(jsii_name="resetMaxCapacity")
    def reset_max_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxCapacity", []))

    @jsii.member(jsii_name="resetMinCapacity")
    def reset_min_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCapacity", []))

    @jsii.member(jsii_name="resetSecondsUntilAutoPause")
    def reset_seconds_until_auto_pause(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondsUntilAutoPause", []))

    @jsii.member(jsii_name="resetTimeoutAction")
    def reset_timeout_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutAction", []))

    @builtins.property
    @jsii.member(jsii_name="autoPauseInput")
    def auto_pause_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoPauseInput"))

    @builtins.property
    @jsii.member(jsii_name="maxCapacityInput")
    def max_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="minCapacityInput")
    def min_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsUntilAutoPauseInput")
    def seconds_until_auto_pause_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "secondsUntilAutoPauseInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutActionInput")
    def timeout_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeoutActionInput"))

    @builtins.property
    @jsii.member(jsii_name="autoPause")
    def auto_pause(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoPause"))

    @auto_pause.setter
    def auto_pause(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoPause", value)

    @builtins.property
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxCapacity"))

    @max_capacity.setter
    def max_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="minCapacity")
    def min_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minCapacity"))

    @min_capacity.setter
    def min_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="secondsUntilAutoPause")
    def seconds_until_auto_pause(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "secondsUntilAutoPause"))

    @seconds_until_auto_pause.setter
    def seconds_until_auto_pause(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secondsUntilAutoPause", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutAction")
    def timeout_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeoutAction"))

    @timeout_action.setter
    def timeout_action(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutAction", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RdsClusterScalingConfiguration]:
        return typing.cast(typing.Optional[RdsClusterScalingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RdsClusterScalingConfiguration],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[RdsClusterScalingConfiguration]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.rdsCluster.RdsClusterServerlessv2ScalingConfiguration",
    jsii_struct_bases=[],
    name_mapping={"max_capacity": "maxCapacity", "min_capacity": "minCapacity"},
)
class RdsClusterServerlessv2ScalingConfiguration:
    def __init__(self, *, max_capacity: jsii.Number, min_capacity: jsii.Number) -> None:
        '''
        :param max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#max_capacity RdsCluster#max_capacity}.
        :param min_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#min_capacity RdsCluster#min_capacity}.
        '''
        if __debug__:
            def stub(*, max_capacity: jsii.Number, min_capacity: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_capacity": max_capacity,
            "min_capacity": min_capacity,
        }

    @builtins.property
    def max_capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#max_capacity RdsCluster#max_capacity}.'''
        result = self._values.get("max_capacity")
        assert result is not None, "Required property 'max_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#min_capacity RdsCluster#min_capacity}.'''
        result = self._values.get("min_capacity")
        assert result is not None, "Required property 'min_capacity' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RdsClusterServerlessv2ScalingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RdsClusterServerlessv2ScalingConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.rdsCluster.RdsClusterServerlessv2ScalingConfigurationOutputReference",
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
    @jsii.member(jsii_name="maxCapacityInput")
    def max_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="minCapacityInput")
    def min_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxCapacity"))

    @max_capacity.setter
    def max_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="minCapacity")
    def min_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minCapacity"))

    @min_capacity.setter
    def min_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[RdsClusterServerlessv2ScalingConfiguration]:
        return typing.cast(typing.Optional[RdsClusterServerlessv2ScalingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RdsClusterServerlessv2ScalingConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[RdsClusterServerlessv2ScalingConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.rdsCluster.RdsClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class RdsClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#create RdsCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#delete RdsCluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#update RdsCluster#update}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#create RdsCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#delete RdsCluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster#update RdsCluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RdsClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RdsClusterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.rdsCluster.RdsClusterTimeoutsOutputReference",
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
    ) -> typing.Optional[typing.Union[RdsClusterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RdsClusterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RdsClusterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[RdsClusterTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "RdsCluster",
    "RdsClusterConfig",
    "RdsClusterRestoreToPointInTime",
    "RdsClusterRestoreToPointInTimeOutputReference",
    "RdsClusterS3Import",
    "RdsClusterS3ImportOutputReference",
    "RdsClusterScalingConfiguration",
    "RdsClusterScalingConfigurationOutputReference",
    "RdsClusterServerlessv2ScalingConfiguration",
    "RdsClusterServerlessv2ScalingConfigurationOutputReference",
    "RdsClusterTimeouts",
    "RdsClusterTimeoutsOutputReference",
]

publication.publish()
