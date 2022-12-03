'''
# `aws_rds_cluster_instance`

Refer to the Terraform Registory for docs: [`aws_rds_cluster_instance`](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance).
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


class RdsClusterInstance(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.rdsClusterInstance.RdsClusterInstance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance aws_rds_cluster_instance}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cluster_identifier: builtins.str,
        instance_class: builtins.str,
        apply_immediately: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        ca_cert_identifier: typing.Optional[builtins.str] = None,
        copy_tags_to_snapshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        db_parameter_group_name: typing.Optional[builtins.str] = None,
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        engine: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identifier: typing.Optional[builtins.str] = None,
        identifier_prefix: typing.Optional[builtins.str] = None,
        monitoring_interval: typing.Optional[jsii.Number] = None,
        monitoring_role_arn: typing.Optional[builtins.str] = None,
        performance_insights_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        performance_insights_kms_key_id: typing.Optional[builtins.str] = None,
        performance_insights_retention_period: typing.Optional[jsii.Number] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        promotion_tier: typing.Optional[jsii.Number] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["RdsClusterInstanceTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance aws_rds_cluster_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#cluster_identifier RdsClusterInstance#cluster_identifier}.
        :param instance_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#instance_class RdsClusterInstance#instance_class}.
        :param apply_immediately: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#apply_immediately RdsClusterInstance#apply_immediately}.
        :param auto_minor_version_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#auto_minor_version_upgrade RdsClusterInstance#auto_minor_version_upgrade}.
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#availability_zone RdsClusterInstance#availability_zone}.
        :param ca_cert_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#ca_cert_identifier RdsClusterInstance#ca_cert_identifier}.
        :param copy_tags_to_snapshot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#copy_tags_to_snapshot RdsClusterInstance#copy_tags_to_snapshot}.
        :param db_parameter_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#db_parameter_group_name RdsClusterInstance#db_parameter_group_name}.
        :param db_subnet_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#db_subnet_group_name RdsClusterInstance#db_subnet_group_name}.
        :param engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#engine RdsClusterInstance#engine}.
        :param engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#engine_version RdsClusterInstance#engine_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#id RdsClusterInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#identifier RdsClusterInstance#identifier}.
        :param identifier_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#identifier_prefix RdsClusterInstance#identifier_prefix}.
        :param monitoring_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#monitoring_interval RdsClusterInstance#monitoring_interval}.
        :param monitoring_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#monitoring_role_arn RdsClusterInstance#monitoring_role_arn}.
        :param performance_insights_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#performance_insights_enabled RdsClusterInstance#performance_insights_enabled}.
        :param performance_insights_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#performance_insights_kms_key_id RdsClusterInstance#performance_insights_kms_key_id}.
        :param performance_insights_retention_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#performance_insights_retention_period RdsClusterInstance#performance_insights_retention_period}.
        :param preferred_backup_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#preferred_backup_window RdsClusterInstance#preferred_backup_window}.
        :param preferred_maintenance_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#preferred_maintenance_window RdsClusterInstance#preferred_maintenance_window}.
        :param promotion_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#promotion_tier RdsClusterInstance#promotion_tier}.
        :param publicly_accessible: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#publicly_accessible RdsClusterInstance#publicly_accessible}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#tags RdsClusterInstance#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#tags_all RdsClusterInstance#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#timeouts RdsClusterInstance#timeouts}
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
                cluster_identifier: builtins.str,
                instance_class: builtins.str,
                apply_immediately: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                availability_zone: typing.Optional[builtins.str] = None,
                ca_cert_identifier: typing.Optional[builtins.str] = None,
                copy_tags_to_snapshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                db_parameter_group_name: typing.Optional[builtins.str] = None,
                db_subnet_group_name: typing.Optional[builtins.str] = None,
                engine: typing.Optional[builtins.str] = None,
                engine_version: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                identifier: typing.Optional[builtins.str] = None,
                identifier_prefix: typing.Optional[builtins.str] = None,
                monitoring_interval: typing.Optional[jsii.Number] = None,
                monitoring_role_arn: typing.Optional[builtins.str] = None,
                performance_insights_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                performance_insights_kms_key_id: typing.Optional[builtins.str] = None,
                performance_insights_retention_period: typing.Optional[jsii.Number] = None,
                preferred_backup_window: typing.Optional[builtins.str] = None,
                preferred_maintenance_window: typing.Optional[builtins.str] = None,
                promotion_tier: typing.Optional[jsii.Number] = None,
                publicly_accessible: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[RdsClusterInstanceTimeouts, typing.Dict[str, typing.Any]]] = None,
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
        config = RdsClusterInstanceConfig(
            cluster_identifier=cluster_identifier,
            instance_class=instance_class,
            apply_immediately=apply_immediately,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            availability_zone=availability_zone,
            ca_cert_identifier=ca_cert_identifier,
            copy_tags_to_snapshot=copy_tags_to_snapshot,
            db_parameter_group_name=db_parameter_group_name,
            db_subnet_group_name=db_subnet_group_name,
            engine=engine,
            engine_version=engine_version,
            id=id,
            identifier=identifier,
            identifier_prefix=identifier_prefix,
            monitoring_interval=monitoring_interval,
            monitoring_role_arn=monitoring_role_arn,
            performance_insights_enabled=performance_insights_enabled,
            performance_insights_kms_key_id=performance_insights_kms_key_id,
            performance_insights_retention_period=performance_insights_retention_period,
            preferred_backup_window=preferred_backup_window,
            preferred_maintenance_window=preferred_maintenance_window,
            promotion_tier=promotion_tier,
            publicly_accessible=publicly_accessible,
            tags=tags,
            tags_all=tags_all,
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

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#create RdsClusterInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#delete RdsClusterInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#update RdsClusterInstance#update}.
        '''
        value = RdsClusterInstanceTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetApplyImmediately")
    def reset_apply_immediately(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplyImmediately", []))

    @jsii.member(jsii_name="resetAutoMinorVersionUpgrade")
    def reset_auto_minor_version_upgrade(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoMinorVersionUpgrade", []))

    @jsii.member(jsii_name="resetAvailabilityZone")
    def reset_availability_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityZone", []))

    @jsii.member(jsii_name="resetCaCertIdentifier")
    def reset_ca_cert_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaCertIdentifier", []))

    @jsii.member(jsii_name="resetCopyTagsToSnapshot")
    def reset_copy_tags_to_snapshot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyTagsToSnapshot", []))

    @jsii.member(jsii_name="resetDbParameterGroupName")
    def reset_db_parameter_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbParameterGroupName", []))

    @jsii.member(jsii_name="resetDbSubnetGroupName")
    def reset_db_subnet_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbSubnetGroupName", []))

    @jsii.member(jsii_name="resetEngine")
    def reset_engine(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEngine", []))

    @jsii.member(jsii_name="resetEngineVersion")
    def reset_engine_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEngineVersion", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentifier")
    def reset_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentifier", []))

    @jsii.member(jsii_name="resetIdentifierPrefix")
    def reset_identifier_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentifierPrefix", []))

    @jsii.member(jsii_name="resetMonitoringInterval")
    def reset_monitoring_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitoringInterval", []))

    @jsii.member(jsii_name="resetMonitoringRoleArn")
    def reset_monitoring_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitoringRoleArn", []))

    @jsii.member(jsii_name="resetPerformanceInsightsEnabled")
    def reset_performance_insights_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerformanceInsightsEnabled", []))

    @jsii.member(jsii_name="resetPerformanceInsightsKmsKeyId")
    def reset_performance_insights_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerformanceInsightsKmsKeyId", []))

    @jsii.member(jsii_name="resetPerformanceInsightsRetentionPeriod")
    def reset_performance_insights_retention_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerformanceInsightsRetentionPeriod", []))

    @jsii.member(jsii_name="resetPreferredBackupWindow")
    def reset_preferred_backup_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredBackupWindow", []))

    @jsii.member(jsii_name="resetPreferredMaintenanceWindow")
    def reset_preferred_maintenance_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferredMaintenanceWindow", []))

    @jsii.member(jsii_name="resetPromotionTier")
    def reset_promotion_tier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPromotionTier", []))

    @jsii.member(jsii_name="resetPubliclyAccessible")
    def reset_publicly_accessible(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPubliclyAccessible", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

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
    @jsii.member(jsii_name="dbiResourceId")
    def dbi_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbiResourceId"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @builtins.property
    @jsii.member(jsii_name="engineVersionActual")
    def engine_version_actual(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineVersionActual"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @builtins.property
    @jsii.member(jsii_name="networkType")
    def network_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkType"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="storageEncrypted")
    def storage_encrypted(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "storageEncrypted"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "RdsClusterInstanceTimeoutsOutputReference":
        return typing.cast("RdsClusterInstanceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="writer")
    def writer(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "writer"))

    @builtins.property
    @jsii.member(jsii_name="applyImmediatelyInput")
    def apply_immediately_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "applyImmediatelyInput"))

    @builtins.property
    @jsii.member(jsii_name="autoMinorVersionUpgradeInput")
    def auto_minor_version_upgrade_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoMinorVersionUpgradeInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneInput")
    def availability_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="caCertIdentifierInput")
    def ca_cert_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifierInput")
    def cluster_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="copyTagsToSnapshotInput")
    def copy_tags_to_snapshot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "copyTagsToSnapshotInput"))

    @builtins.property
    @jsii.member(jsii_name="dbParameterGroupNameInput")
    def db_parameter_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbParameterGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dbSubnetGroupNameInput")
    def db_subnet_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbSubnetGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="engineInput")
    def engine_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineInput"))

    @builtins.property
    @jsii.member(jsii_name="engineVersionInput")
    def engine_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="identifierInput")
    def identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identifierInput"))

    @builtins.property
    @jsii.member(jsii_name="identifierPrefixInput")
    def identifier_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identifierPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceClassInput")
    def instance_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceClassInput"))

    @builtins.property
    @jsii.member(jsii_name="monitoringIntervalInput")
    def monitoring_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "monitoringIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="monitoringRoleArnInput")
    def monitoring_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "monitoringRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="performanceInsightsEnabledInput")
    def performance_insights_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "performanceInsightsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="performanceInsightsKmsKeyIdInput")
    def performance_insights_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "performanceInsightsKmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="performanceInsightsRetentionPeriodInput")
    def performance_insights_retention_period_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "performanceInsightsRetentionPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredBackupWindowInput")
    def preferred_backup_window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredBackupWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindowInput")
    def preferred_maintenance_window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="promotionTierInput")
    def promotion_tier_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "promotionTierInput"))

    @builtins.property
    @jsii.member(jsii_name="publiclyAccessibleInput")
    def publicly_accessible_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publiclyAccessibleInput"))

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
    ) -> typing.Optional[typing.Union["RdsClusterInstanceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["RdsClusterInstanceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

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
    @jsii.member(jsii_name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoMinorVersionUpgrade"))

    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoMinorVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="caCertIdentifier")
    def ca_cert_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caCertIdentifier"))

    @ca_cert_identifier.setter
    def ca_cert_identifier(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCertIdentifier", value)

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
    @jsii.member(jsii_name="dbParameterGroupName")
    def db_parameter_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbParameterGroupName"))

    @db_parameter_group_name.setter
    def db_parameter_group_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbParameterGroupName", value)

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
    @jsii.member(jsii_name="identifier")
    def identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identifier"))

    @identifier.setter
    def identifier(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identifier", value)

    @builtins.property
    @jsii.member(jsii_name="identifierPrefix")
    def identifier_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identifierPrefix"))

    @identifier_prefix.setter
    def identifier_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identifierPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="instanceClass")
    def instance_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceClass"))

    @instance_class.setter
    def instance_class(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceClass", value)

    @builtins.property
    @jsii.member(jsii_name="monitoringInterval")
    def monitoring_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "monitoringInterval"))

    @monitoring_interval.setter
    def monitoring_interval(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitoringInterval", value)

    @builtins.property
    @jsii.member(jsii_name="monitoringRoleArn")
    def monitoring_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "monitoringRoleArn"))

    @monitoring_role_arn.setter
    def monitoring_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitoringRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="performanceInsightsEnabled")
    def performance_insights_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "performanceInsightsEnabled"))

    @performance_insights_enabled.setter
    def performance_insights_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "performanceInsightsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="performanceInsightsKmsKeyId")
    def performance_insights_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "performanceInsightsKmsKeyId"))

    @performance_insights_kms_key_id.setter
    def performance_insights_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "performanceInsightsKmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="performanceInsightsRetentionPeriod")
    def performance_insights_retention_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "performanceInsightsRetentionPeriod"))

    @performance_insights_retention_period.setter
    def performance_insights_retention_period(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "performanceInsightsRetentionPeriod", value)

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
    @jsii.member(jsii_name="promotionTier")
    def promotion_tier(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "promotionTier"))

    @promotion_tier.setter
    def promotion_tier(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "promotionTier", value)

    @builtins.property
    @jsii.member(jsii_name="publiclyAccessible")
    def publicly_accessible(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publiclyAccessible"))

    @publicly_accessible.setter
    def publicly_accessible(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publiclyAccessible", value)

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
    jsii_type="@cdktf/provider-aws.rdsClusterInstance.RdsClusterInstanceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster_identifier": "clusterIdentifier",
        "instance_class": "instanceClass",
        "apply_immediately": "applyImmediately",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "availability_zone": "availabilityZone",
        "ca_cert_identifier": "caCertIdentifier",
        "copy_tags_to_snapshot": "copyTagsToSnapshot",
        "db_parameter_group_name": "dbParameterGroupName",
        "db_subnet_group_name": "dbSubnetGroupName",
        "engine": "engine",
        "engine_version": "engineVersion",
        "id": "id",
        "identifier": "identifier",
        "identifier_prefix": "identifierPrefix",
        "monitoring_interval": "monitoringInterval",
        "monitoring_role_arn": "monitoringRoleArn",
        "performance_insights_enabled": "performanceInsightsEnabled",
        "performance_insights_kms_key_id": "performanceInsightsKmsKeyId",
        "performance_insights_retention_period": "performanceInsightsRetentionPeriod",
        "preferred_backup_window": "preferredBackupWindow",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "promotion_tier": "promotionTier",
        "publicly_accessible": "publiclyAccessible",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class RdsClusterInstanceConfig(cdktf.TerraformMetaArguments):
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
        cluster_identifier: builtins.str,
        instance_class: builtins.str,
        apply_immediately: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        ca_cert_identifier: typing.Optional[builtins.str] = None,
        copy_tags_to_snapshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        db_parameter_group_name: typing.Optional[builtins.str] = None,
        db_subnet_group_name: typing.Optional[builtins.str] = None,
        engine: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identifier: typing.Optional[builtins.str] = None,
        identifier_prefix: typing.Optional[builtins.str] = None,
        monitoring_interval: typing.Optional[jsii.Number] = None,
        monitoring_role_arn: typing.Optional[builtins.str] = None,
        performance_insights_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        performance_insights_kms_key_id: typing.Optional[builtins.str] = None,
        performance_insights_retention_period: typing.Optional[jsii.Number] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        promotion_tier: typing.Optional[jsii.Number] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["RdsClusterInstanceTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cluster_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#cluster_identifier RdsClusterInstance#cluster_identifier}.
        :param instance_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#instance_class RdsClusterInstance#instance_class}.
        :param apply_immediately: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#apply_immediately RdsClusterInstance#apply_immediately}.
        :param auto_minor_version_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#auto_minor_version_upgrade RdsClusterInstance#auto_minor_version_upgrade}.
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#availability_zone RdsClusterInstance#availability_zone}.
        :param ca_cert_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#ca_cert_identifier RdsClusterInstance#ca_cert_identifier}.
        :param copy_tags_to_snapshot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#copy_tags_to_snapshot RdsClusterInstance#copy_tags_to_snapshot}.
        :param db_parameter_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#db_parameter_group_name RdsClusterInstance#db_parameter_group_name}.
        :param db_subnet_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#db_subnet_group_name RdsClusterInstance#db_subnet_group_name}.
        :param engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#engine RdsClusterInstance#engine}.
        :param engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#engine_version RdsClusterInstance#engine_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#id RdsClusterInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#identifier RdsClusterInstance#identifier}.
        :param identifier_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#identifier_prefix RdsClusterInstance#identifier_prefix}.
        :param monitoring_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#monitoring_interval RdsClusterInstance#monitoring_interval}.
        :param monitoring_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#monitoring_role_arn RdsClusterInstance#monitoring_role_arn}.
        :param performance_insights_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#performance_insights_enabled RdsClusterInstance#performance_insights_enabled}.
        :param performance_insights_kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#performance_insights_kms_key_id RdsClusterInstance#performance_insights_kms_key_id}.
        :param performance_insights_retention_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#performance_insights_retention_period RdsClusterInstance#performance_insights_retention_period}.
        :param preferred_backup_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#preferred_backup_window RdsClusterInstance#preferred_backup_window}.
        :param preferred_maintenance_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#preferred_maintenance_window RdsClusterInstance#preferred_maintenance_window}.
        :param promotion_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#promotion_tier RdsClusterInstance#promotion_tier}.
        :param publicly_accessible: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#publicly_accessible RdsClusterInstance#publicly_accessible}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#tags RdsClusterInstance#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#tags_all RdsClusterInstance#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#timeouts RdsClusterInstance#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = RdsClusterInstanceTimeouts(**timeouts)
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
                cluster_identifier: builtins.str,
                instance_class: builtins.str,
                apply_immediately: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                availability_zone: typing.Optional[builtins.str] = None,
                ca_cert_identifier: typing.Optional[builtins.str] = None,
                copy_tags_to_snapshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                db_parameter_group_name: typing.Optional[builtins.str] = None,
                db_subnet_group_name: typing.Optional[builtins.str] = None,
                engine: typing.Optional[builtins.str] = None,
                engine_version: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                identifier: typing.Optional[builtins.str] = None,
                identifier_prefix: typing.Optional[builtins.str] = None,
                monitoring_interval: typing.Optional[jsii.Number] = None,
                monitoring_role_arn: typing.Optional[builtins.str] = None,
                performance_insights_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                performance_insights_kms_key_id: typing.Optional[builtins.str] = None,
                performance_insights_retention_period: typing.Optional[jsii.Number] = None,
                preferred_backup_window: typing.Optional[builtins.str] = None,
                preferred_maintenance_window: typing.Optional[builtins.str] = None,
                promotion_tier: typing.Optional[jsii.Number] = None,
                publicly_accessible: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[RdsClusterInstanceTimeouts, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
            check_type(argname="argument instance_class", value=instance_class, expected_type=type_hints["instance_class"])
            check_type(argname="argument apply_immediately", value=apply_immediately, expected_type=type_hints["apply_immediately"])
            check_type(argname="argument auto_minor_version_upgrade", value=auto_minor_version_upgrade, expected_type=type_hints["auto_minor_version_upgrade"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument ca_cert_identifier", value=ca_cert_identifier, expected_type=type_hints["ca_cert_identifier"])
            check_type(argname="argument copy_tags_to_snapshot", value=copy_tags_to_snapshot, expected_type=type_hints["copy_tags_to_snapshot"])
            check_type(argname="argument db_parameter_group_name", value=db_parameter_group_name, expected_type=type_hints["db_parameter_group_name"])
            check_type(argname="argument db_subnet_group_name", value=db_subnet_group_name, expected_type=type_hints["db_subnet_group_name"])
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
            check_type(argname="argument identifier_prefix", value=identifier_prefix, expected_type=type_hints["identifier_prefix"])
            check_type(argname="argument monitoring_interval", value=monitoring_interval, expected_type=type_hints["monitoring_interval"])
            check_type(argname="argument monitoring_role_arn", value=monitoring_role_arn, expected_type=type_hints["monitoring_role_arn"])
            check_type(argname="argument performance_insights_enabled", value=performance_insights_enabled, expected_type=type_hints["performance_insights_enabled"])
            check_type(argname="argument performance_insights_kms_key_id", value=performance_insights_kms_key_id, expected_type=type_hints["performance_insights_kms_key_id"])
            check_type(argname="argument performance_insights_retention_period", value=performance_insights_retention_period, expected_type=type_hints["performance_insights_retention_period"])
            check_type(argname="argument preferred_backup_window", value=preferred_backup_window, expected_type=type_hints["preferred_backup_window"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument promotion_tier", value=promotion_tier, expected_type=type_hints["promotion_tier"])
            check_type(argname="argument publicly_accessible", value=publicly_accessible, expected_type=type_hints["publicly_accessible"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_identifier": cluster_identifier,
            "instance_class": instance_class,
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
        if apply_immediately is not None:
            self._values["apply_immediately"] = apply_immediately
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if ca_cert_identifier is not None:
            self._values["ca_cert_identifier"] = ca_cert_identifier
        if copy_tags_to_snapshot is not None:
            self._values["copy_tags_to_snapshot"] = copy_tags_to_snapshot
        if db_parameter_group_name is not None:
            self._values["db_parameter_group_name"] = db_parameter_group_name
        if db_subnet_group_name is not None:
            self._values["db_subnet_group_name"] = db_subnet_group_name
        if engine is not None:
            self._values["engine"] = engine
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if id is not None:
            self._values["id"] = id
        if identifier is not None:
            self._values["identifier"] = identifier
        if identifier_prefix is not None:
            self._values["identifier_prefix"] = identifier_prefix
        if monitoring_interval is not None:
            self._values["monitoring_interval"] = monitoring_interval
        if monitoring_role_arn is not None:
            self._values["monitoring_role_arn"] = monitoring_role_arn
        if performance_insights_enabled is not None:
            self._values["performance_insights_enabled"] = performance_insights_enabled
        if performance_insights_kms_key_id is not None:
            self._values["performance_insights_kms_key_id"] = performance_insights_kms_key_id
        if performance_insights_retention_period is not None:
            self._values["performance_insights_retention_period"] = performance_insights_retention_period
        if preferred_backup_window is not None:
            self._values["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if promotion_tier is not None:
            self._values["promotion_tier"] = promotion_tier
        if publicly_accessible is not None:
            self._values["publicly_accessible"] = publicly_accessible
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
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
    def cluster_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#cluster_identifier RdsClusterInstance#cluster_identifier}.'''
        result = self._values.get("cluster_identifier")
        assert result is not None, "Required property 'cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_class(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#instance_class RdsClusterInstance#instance_class}.'''
        result = self._values.get("instance_class")
        assert result is not None, "Required property 'instance_class' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def apply_immediately(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#apply_immediately RdsClusterInstance#apply_immediately}.'''
        result = self._values.get("apply_immediately")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#auto_minor_version_upgrade RdsClusterInstance#auto_minor_version_upgrade}.'''
        result = self._values.get("auto_minor_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#availability_zone RdsClusterInstance#availability_zone}.'''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ca_cert_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#ca_cert_identifier RdsClusterInstance#ca_cert_identifier}.'''
        result = self._values.get("ca_cert_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def copy_tags_to_snapshot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#copy_tags_to_snapshot RdsClusterInstance#copy_tags_to_snapshot}.'''
        result = self._values.get("copy_tags_to_snapshot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def db_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#db_parameter_group_name RdsClusterInstance#db_parameter_group_name}.'''
        result = self._values.get("db_parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#db_subnet_group_name RdsClusterInstance#db_subnet_group_name}.'''
        result = self._values.get("db_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#engine RdsClusterInstance#engine}.'''
        result = self._values.get("engine")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#engine_version RdsClusterInstance#engine_version}.'''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#id RdsClusterInstance#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#identifier RdsClusterInstance#identifier}.'''
        result = self._values.get("identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identifier_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#identifier_prefix RdsClusterInstance#identifier_prefix}.'''
        result = self._values.get("identifier_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monitoring_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#monitoring_interval RdsClusterInstance#monitoring_interval}.'''
        result = self._values.get("monitoring_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def monitoring_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#monitoring_role_arn RdsClusterInstance#monitoring_role_arn}.'''
        result = self._values.get("monitoring_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def performance_insights_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#performance_insights_enabled RdsClusterInstance#performance_insights_enabled}.'''
        result = self._values.get("performance_insights_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def performance_insights_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#performance_insights_kms_key_id RdsClusterInstance#performance_insights_kms_key_id}.'''
        result = self._values.get("performance_insights_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def performance_insights_retention_period(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#performance_insights_retention_period RdsClusterInstance#performance_insights_retention_period}.'''
        result = self._values.get("performance_insights_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#preferred_backup_window RdsClusterInstance#preferred_backup_window}.'''
        result = self._values.get("preferred_backup_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#preferred_maintenance_window RdsClusterInstance#preferred_maintenance_window}.'''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def promotion_tier(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#promotion_tier RdsClusterInstance#promotion_tier}.'''
        result = self._values.get("promotion_tier")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#publicly_accessible RdsClusterInstance#publicly_accessible}.'''
        result = self._values.get("publicly_accessible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#tags RdsClusterInstance#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#tags_all RdsClusterInstance#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["RdsClusterInstanceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#timeouts RdsClusterInstance#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["RdsClusterInstanceTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RdsClusterInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.rdsClusterInstance.RdsClusterInstanceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class RdsClusterInstanceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#create RdsClusterInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#delete RdsClusterInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#update RdsClusterInstance#update}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#create RdsClusterInstance#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#delete RdsClusterInstance#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance#update RdsClusterInstance#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RdsClusterInstanceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RdsClusterInstanceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.rdsClusterInstance.RdsClusterInstanceTimeoutsOutputReference",
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
    ) -> typing.Optional[typing.Union[RdsClusterInstanceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RdsClusterInstanceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RdsClusterInstanceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[RdsClusterInstanceTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "RdsClusterInstance",
    "RdsClusterInstanceConfig",
    "RdsClusterInstanceTimeouts",
    "RdsClusterInstanceTimeoutsOutputReference",
]

publication.publish()
