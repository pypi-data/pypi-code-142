'''
# `aws_msk_cluster`

Refer to the Terraform Registory for docs: [`aws_msk_cluster`](https://www.terraform.io/docs/providers/aws/r/msk_cluster).
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


class MskCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster aws_msk_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        broker_node_group_info: typing.Union["MskClusterBrokerNodeGroupInfo", typing.Dict[str, typing.Any]],
        cluster_name: builtins.str,
        kafka_version: builtins.str,
        number_of_broker_nodes: jsii.Number,
        client_authentication: typing.Optional[typing.Union["MskClusterClientAuthentication", typing.Dict[str, typing.Any]]] = None,
        configuration_info: typing.Optional[typing.Union["MskClusterConfigurationInfo", typing.Dict[str, typing.Any]]] = None,
        encryption_info: typing.Optional[typing.Union["MskClusterEncryptionInfo", typing.Dict[str, typing.Any]]] = None,
        enhanced_monitoring: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        logging_info: typing.Optional[typing.Union["MskClusterLoggingInfo", typing.Dict[str, typing.Any]]] = None,
        open_monitoring: typing.Optional[typing.Union["MskClusterOpenMonitoring", typing.Dict[str, typing.Any]]] = None,
        storage_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MskClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster aws_msk_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param broker_node_group_info: broker_node_group_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#broker_node_group_info MskCluster#broker_node_group_info}
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#cluster_name MskCluster#cluster_name}.
        :param kafka_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#kafka_version MskCluster#kafka_version}.
        :param number_of_broker_nodes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#number_of_broker_nodes MskCluster#number_of_broker_nodes}.
        :param client_authentication: client_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#client_authentication MskCluster#client_authentication}
        :param configuration_info: configuration_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#configuration_info MskCluster#configuration_info}
        :param encryption_info: encryption_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#encryption_info MskCluster#encryption_info}
        :param enhanced_monitoring: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enhanced_monitoring MskCluster#enhanced_monitoring}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#id MskCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param logging_info: logging_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#logging_info MskCluster#logging_info}
        :param open_monitoring: open_monitoring block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#open_monitoring MskCluster#open_monitoring}
        :param storage_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#storage_mode MskCluster#storage_mode}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#tags MskCluster#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#tags_all MskCluster#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#timeouts MskCluster#timeouts}
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
                broker_node_group_info: typing.Union[MskClusterBrokerNodeGroupInfo, typing.Dict[str, typing.Any]],
                cluster_name: builtins.str,
                kafka_version: builtins.str,
                number_of_broker_nodes: jsii.Number,
                client_authentication: typing.Optional[typing.Union[MskClusterClientAuthentication, typing.Dict[str, typing.Any]]] = None,
                configuration_info: typing.Optional[typing.Union[MskClusterConfigurationInfo, typing.Dict[str, typing.Any]]] = None,
                encryption_info: typing.Optional[typing.Union[MskClusterEncryptionInfo, typing.Dict[str, typing.Any]]] = None,
                enhanced_monitoring: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                logging_info: typing.Optional[typing.Union[MskClusterLoggingInfo, typing.Dict[str, typing.Any]]] = None,
                open_monitoring: typing.Optional[typing.Union[MskClusterOpenMonitoring, typing.Dict[str, typing.Any]]] = None,
                storage_mode: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[MskClusterTimeouts, typing.Dict[str, typing.Any]]] = None,
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
        config = MskClusterConfig(
            broker_node_group_info=broker_node_group_info,
            cluster_name=cluster_name,
            kafka_version=kafka_version,
            number_of_broker_nodes=number_of_broker_nodes,
            client_authentication=client_authentication,
            configuration_info=configuration_info,
            encryption_info=encryption_info,
            enhanced_monitoring=enhanced_monitoring,
            id=id,
            logging_info=logging_info,
            open_monitoring=open_monitoring,
            storage_mode=storage_mode,
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

    @jsii.member(jsii_name="putBrokerNodeGroupInfo")
    def put_broker_node_group_info(
        self,
        *,
        client_subnets: typing.Sequence[builtins.str],
        instance_type: builtins.str,
        security_groups: typing.Sequence[builtins.str],
        az_distribution: typing.Optional[builtins.str] = None,
        connectivity_info: typing.Optional[typing.Union["MskClusterBrokerNodeGroupInfoConnectivityInfo", typing.Dict[str, typing.Any]]] = None,
        ebs_volume_size: typing.Optional[jsii.Number] = None,
        storage_info: typing.Optional[typing.Union["MskClusterBrokerNodeGroupInfoStorageInfo", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#client_subnets MskCluster#client_subnets}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#instance_type MskCluster#instance_type}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#security_groups MskCluster#security_groups}.
        :param az_distribution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#az_distribution MskCluster#az_distribution}.
        :param connectivity_info: connectivity_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#connectivity_info MskCluster#connectivity_info}
        :param ebs_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#ebs_volume_size MskCluster#ebs_volume_size}.
        :param storage_info: storage_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#storage_info MskCluster#storage_info}
        '''
        value = MskClusterBrokerNodeGroupInfo(
            client_subnets=client_subnets,
            instance_type=instance_type,
            security_groups=security_groups,
            az_distribution=az_distribution,
            connectivity_info=connectivity_info,
            ebs_volume_size=ebs_volume_size,
            storage_info=storage_info,
        )

        return typing.cast(None, jsii.invoke(self, "putBrokerNodeGroupInfo", [value]))

    @jsii.member(jsii_name="putClientAuthentication")
    def put_client_authentication(
        self,
        *,
        sasl: typing.Optional[typing.Union["MskClusterClientAuthenticationSasl", typing.Dict[str, typing.Any]]] = None,
        tls: typing.Optional[typing.Union["MskClusterClientAuthenticationTls", typing.Dict[str, typing.Any]]] = None,
        unauthenticated: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param sasl: sasl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#sasl MskCluster#sasl}
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#tls MskCluster#tls}
        :param unauthenticated: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#unauthenticated MskCluster#unauthenticated}.
        '''
        value = MskClusterClientAuthentication(
            sasl=sasl, tls=tls, unauthenticated=unauthenticated
        )

        return typing.cast(None, jsii.invoke(self, "putClientAuthentication", [value]))

    @jsii.member(jsii_name="putConfigurationInfo")
    def put_configuration_info(
        self,
        *,
        arn: builtins.str,
        revision: jsii.Number,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#arn MskCluster#arn}.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#revision MskCluster#revision}.
        '''
        value = MskClusterConfigurationInfo(arn=arn, revision=revision)

        return typing.cast(None, jsii.invoke(self, "putConfigurationInfo", [value]))

    @jsii.member(jsii_name="putEncryptionInfo")
    def put_encryption_info(
        self,
        *,
        encryption_at_rest_kms_key_arn: typing.Optional[builtins.str] = None,
        encryption_in_transit: typing.Optional[typing.Union["MskClusterEncryptionInfoEncryptionInTransit", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param encryption_at_rest_kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#encryption_at_rest_kms_key_arn MskCluster#encryption_at_rest_kms_key_arn}.
        :param encryption_in_transit: encryption_in_transit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#encryption_in_transit MskCluster#encryption_in_transit}
        '''
        value = MskClusterEncryptionInfo(
            encryption_at_rest_kms_key_arn=encryption_at_rest_kms_key_arn,
            encryption_in_transit=encryption_in_transit,
        )

        return typing.cast(None, jsii.invoke(self, "putEncryptionInfo", [value]))

    @jsii.member(jsii_name="putLoggingInfo")
    def put_logging_info(
        self,
        *,
        broker_logs: typing.Union["MskClusterLoggingInfoBrokerLogs", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param broker_logs: broker_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#broker_logs MskCluster#broker_logs}
        '''
        value = MskClusterLoggingInfo(broker_logs=broker_logs)

        return typing.cast(None, jsii.invoke(self, "putLoggingInfo", [value]))

    @jsii.member(jsii_name="putOpenMonitoring")
    def put_open_monitoring(
        self,
        *,
        prometheus: typing.Union["MskClusterOpenMonitoringPrometheus", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param prometheus: prometheus block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#prometheus MskCluster#prometheus}
        '''
        value = MskClusterOpenMonitoring(prometheus=prometheus)

        return typing.cast(None, jsii.invoke(self, "putOpenMonitoring", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#create MskCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#delete MskCluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#update MskCluster#update}.
        '''
        value = MskClusterTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetClientAuthentication")
    def reset_client_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientAuthentication", []))

    @jsii.member(jsii_name="resetConfigurationInfo")
    def reset_configuration_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurationInfo", []))

    @jsii.member(jsii_name="resetEncryptionInfo")
    def reset_encryption_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionInfo", []))

    @jsii.member(jsii_name="resetEnhancedMonitoring")
    def reset_enhanced_monitoring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnhancedMonitoring", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLoggingInfo")
    def reset_logging_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingInfo", []))

    @jsii.member(jsii_name="resetOpenMonitoring")
    def reset_open_monitoring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpenMonitoring", []))

    @jsii.member(jsii_name="resetStorageMode")
    def reset_storage_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageMode", []))

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
    @jsii.member(jsii_name="bootstrapBrokers")
    def bootstrap_brokers(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootstrapBrokers"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapBrokersPublicSaslIam")
    def bootstrap_brokers_public_sasl_iam(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootstrapBrokersPublicSaslIam"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapBrokersPublicSaslScram")
    def bootstrap_brokers_public_sasl_scram(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootstrapBrokersPublicSaslScram"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapBrokersPublicTls")
    def bootstrap_brokers_public_tls(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootstrapBrokersPublicTls"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapBrokersSaslIam")
    def bootstrap_brokers_sasl_iam(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootstrapBrokersSaslIam"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapBrokersSaslScram")
    def bootstrap_brokers_sasl_scram(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootstrapBrokersSaslScram"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapBrokersTls")
    def bootstrap_brokers_tls(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootstrapBrokersTls"))

    @builtins.property
    @jsii.member(jsii_name="brokerNodeGroupInfo")
    def broker_node_group_info(self) -> "MskClusterBrokerNodeGroupInfoOutputReference":
        return typing.cast("MskClusterBrokerNodeGroupInfoOutputReference", jsii.get(self, "brokerNodeGroupInfo"))

    @builtins.property
    @jsii.member(jsii_name="clientAuthentication")
    def client_authentication(self) -> "MskClusterClientAuthenticationOutputReference":
        return typing.cast("MskClusterClientAuthenticationOutputReference", jsii.get(self, "clientAuthentication"))

    @builtins.property
    @jsii.member(jsii_name="configurationInfo")
    def configuration_info(self) -> "MskClusterConfigurationInfoOutputReference":
        return typing.cast("MskClusterConfigurationInfoOutputReference", jsii.get(self, "configurationInfo"))

    @builtins.property
    @jsii.member(jsii_name="currentVersion")
    def current_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "currentVersion"))

    @builtins.property
    @jsii.member(jsii_name="encryptionInfo")
    def encryption_info(self) -> "MskClusterEncryptionInfoOutputReference":
        return typing.cast("MskClusterEncryptionInfoOutputReference", jsii.get(self, "encryptionInfo"))

    @builtins.property
    @jsii.member(jsii_name="loggingInfo")
    def logging_info(self) -> "MskClusterLoggingInfoOutputReference":
        return typing.cast("MskClusterLoggingInfoOutputReference", jsii.get(self, "loggingInfo"))

    @builtins.property
    @jsii.member(jsii_name="openMonitoring")
    def open_monitoring(self) -> "MskClusterOpenMonitoringOutputReference":
        return typing.cast("MskClusterOpenMonitoringOutputReference", jsii.get(self, "openMonitoring"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MskClusterTimeoutsOutputReference":
        return typing.cast("MskClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="zookeeperConnectString")
    def zookeeper_connect_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zookeeperConnectString"))

    @builtins.property
    @jsii.member(jsii_name="zookeeperConnectStringTls")
    def zookeeper_connect_string_tls(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zookeeperConnectStringTls"))

    @builtins.property
    @jsii.member(jsii_name="brokerNodeGroupInfoInput")
    def broker_node_group_info_input(
        self,
    ) -> typing.Optional["MskClusterBrokerNodeGroupInfo"]:
        return typing.cast(typing.Optional["MskClusterBrokerNodeGroupInfo"], jsii.get(self, "brokerNodeGroupInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="clientAuthenticationInput")
    def client_authentication_input(
        self,
    ) -> typing.Optional["MskClusterClientAuthentication"]:
        return typing.cast(typing.Optional["MskClusterClientAuthentication"], jsii.get(self, "clientAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterNameInput")
    def cluster_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationInfoInput")
    def configuration_info_input(
        self,
    ) -> typing.Optional["MskClusterConfigurationInfo"]:
        return typing.cast(typing.Optional["MskClusterConfigurationInfo"], jsii.get(self, "configurationInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionInfoInput")
    def encryption_info_input(self) -> typing.Optional["MskClusterEncryptionInfo"]:
        return typing.cast(typing.Optional["MskClusterEncryptionInfo"], jsii.get(self, "encryptionInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="enhancedMonitoringInput")
    def enhanced_monitoring_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enhancedMonitoringInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kafkaVersionInput")
    def kafka_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kafkaVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingInfoInput")
    def logging_info_input(self) -> typing.Optional["MskClusterLoggingInfo"]:
        return typing.cast(typing.Optional["MskClusterLoggingInfo"], jsii.get(self, "loggingInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="numberOfBrokerNodesInput")
    def number_of_broker_nodes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberOfBrokerNodesInput"))

    @builtins.property
    @jsii.member(jsii_name="openMonitoringInput")
    def open_monitoring_input(self) -> typing.Optional["MskClusterOpenMonitoring"]:
        return typing.cast(typing.Optional["MskClusterOpenMonitoring"], jsii.get(self, "openMonitoringInput"))

    @builtins.property
    @jsii.member(jsii_name="storageModeInput")
    def storage_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageModeInput"))

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
    ) -> typing.Optional[typing.Union["MskClusterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MskClusterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="enhancedMonitoring")
    def enhanced_monitoring(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enhancedMonitoring"))

    @enhanced_monitoring.setter
    def enhanced_monitoring(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enhancedMonitoring", value)

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
    @jsii.member(jsii_name="kafkaVersion")
    def kafka_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kafkaVersion"))

    @kafka_version.setter
    def kafka_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kafkaVersion", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfBrokerNodes")
    def number_of_broker_nodes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numberOfBrokerNodes"))

    @number_of_broker_nodes.setter
    def number_of_broker_nodes(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfBrokerNodes", value)

    @builtins.property
    @jsii.member(jsii_name="storageMode")
    def storage_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageMode"))

    @storage_mode.setter
    def storage_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageMode", value)

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
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterBrokerNodeGroupInfo",
    jsii_struct_bases=[],
    name_mapping={
        "client_subnets": "clientSubnets",
        "instance_type": "instanceType",
        "security_groups": "securityGroups",
        "az_distribution": "azDistribution",
        "connectivity_info": "connectivityInfo",
        "ebs_volume_size": "ebsVolumeSize",
        "storage_info": "storageInfo",
    },
)
class MskClusterBrokerNodeGroupInfo:
    def __init__(
        self,
        *,
        client_subnets: typing.Sequence[builtins.str],
        instance_type: builtins.str,
        security_groups: typing.Sequence[builtins.str],
        az_distribution: typing.Optional[builtins.str] = None,
        connectivity_info: typing.Optional[typing.Union["MskClusterBrokerNodeGroupInfoConnectivityInfo", typing.Dict[str, typing.Any]]] = None,
        ebs_volume_size: typing.Optional[jsii.Number] = None,
        storage_info: typing.Optional[typing.Union["MskClusterBrokerNodeGroupInfoStorageInfo", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#client_subnets MskCluster#client_subnets}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#instance_type MskCluster#instance_type}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#security_groups MskCluster#security_groups}.
        :param az_distribution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#az_distribution MskCluster#az_distribution}.
        :param connectivity_info: connectivity_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#connectivity_info MskCluster#connectivity_info}
        :param ebs_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#ebs_volume_size MskCluster#ebs_volume_size}.
        :param storage_info: storage_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#storage_info MskCluster#storage_info}
        '''
        if isinstance(connectivity_info, dict):
            connectivity_info = MskClusterBrokerNodeGroupInfoConnectivityInfo(**connectivity_info)
        if isinstance(storage_info, dict):
            storage_info = MskClusterBrokerNodeGroupInfoStorageInfo(**storage_info)
        if __debug__:
            def stub(
                *,
                client_subnets: typing.Sequence[builtins.str],
                instance_type: builtins.str,
                security_groups: typing.Sequence[builtins.str],
                az_distribution: typing.Optional[builtins.str] = None,
                connectivity_info: typing.Optional[typing.Union[MskClusterBrokerNodeGroupInfoConnectivityInfo, typing.Dict[str, typing.Any]]] = None,
                ebs_volume_size: typing.Optional[jsii.Number] = None,
                storage_info: typing.Optional[typing.Union[MskClusterBrokerNodeGroupInfoStorageInfo, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument client_subnets", value=client_subnets, expected_type=type_hints["client_subnets"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument az_distribution", value=az_distribution, expected_type=type_hints["az_distribution"])
            check_type(argname="argument connectivity_info", value=connectivity_info, expected_type=type_hints["connectivity_info"])
            check_type(argname="argument ebs_volume_size", value=ebs_volume_size, expected_type=type_hints["ebs_volume_size"])
            check_type(argname="argument storage_info", value=storage_info, expected_type=type_hints["storage_info"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_subnets": client_subnets,
            "instance_type": instance_type,
            "security_groups": security_groups,
        }
        if az_distribution is not None:
            self._values["az_distribution"] = az_distribution
        if connectivity_info is not None:
            self._values["connectivity_info"] = connectivity_info
        if ebs_volume_size is not None:
            self._values["ebs_volume_size"] = ebs_volume_size
        if storage_info is not None:
            self._values["storage_info"] = storage_info

    @builtins.property
    def client_subnets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#client_subnets MskCluster#client_subnets}.'''
        result = self._values.get("client_subnets")
        assert result is not None, "Required property 'client_subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#instance_type MskCluster#instance_type}.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_groups(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#security_groups MskCluster#security_groups}.'''
        result = self._values.get("security_groups")
        assert result is not None, "Required property 'security_groups' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def az_distribution(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#az_distribution MskCluster#az_distribution}.'''
        result = self._values.get("az_distribution")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connectivity_info(
        self,
    ) -> typing.Optional["MskClusterBrokerNodeGroupInfoConnectivityInfo"]:
        '''connectivity_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#connectivity_info MskCluster#connectivity_info}
        '''
        result = self._values.get("connectivity_info")
        return typing.cast(typing.Optional["MskClusterBrokerNodeGroupInfoConnectivityInfo"], result)

    @builtins.property
    def ebs_volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#ebs_volume_size MskCluster#ebs_volume_size}.'''
        result = self._values.get("ebs_volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_info(
        self,
    ) -> typing.Optional["MskClusterBrokerNodeGroupInfoStorageInfo"]:
        '''storage_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#storage_info MskCluster#storage_info}
        '''
        result = self._values.get("storage_info")
        return typing.cast(typing.Optional["MskClusterBrokerNodeGroupInfoStorageInfo"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterBrokerNodeGroupInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterBrokerNodeGroupInfoConnectivityInfo",
    jsii_struct_bases=[],
    name_mapping={"public_access": "publicAccess"},
)
class MskClusterBrokerNodeGroupInfoConnectivityInfo:
    def __init__(
        self,
        *,
        public_access: typing.Optional[typing.Union["MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param public_access: public_access block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#public_access MskCluster#public_access}
        '''
        if isinstance(public_access, dict):
            public_access = MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess(**public_access)
        if __debug__:
            def stub(
                *,
                public_access: typing.Optional[typing.Union[MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument public_access", value=public_access, expected_type=type_hints["public_access"])
        self._values: typing.Dict[str, typing.Any] = {}
        if public_access is not None:
            self._values["public_access"] = public_access

    @builtins.property
    def public_access(
        self,
    ) -> typing.Optional["MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess"]:
        '''public_access block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#public_access MskCluster#public_access}
        '''
        result = self._values.get("public_access")
        return typing.cast(typing.Optional["MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterBrokerNodeGroupInfoConnectivityInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskClusterBrokerNodeGroupInfoConnectivityInfoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterBrokerNodeGroupInfoConnectivityInfoOutputReference",
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

    @jsii.member(jsii_name="putPublicAccess")
    def put_public_access(self, *, type: typing.Optional[builtins.str] = None) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#type MskCluster#type}.
        '''
        value = MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess(type=type)

        return typing.cast(None, jsii.invoke(self, "putPublicAccess", [value]))

    @jsii.member(jsii_name="resetPublicAccess")
    def reset_public_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicAccess", []))

    @builtins.property
    @jsii.member(jsii_name="publicAccess")
    def public_access(
        self,
    ) -> "MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccessOutputReference":
        return typing.cast("MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccessOutputReference", jsii.get(self, "publicAccess"))

    @builtins.property
    @jsii.member(jsii_name="publicAccessInput")
    def public_access_input(
        self,
    ) -> typing.Optional["MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess"]:
        return typing.cast(typing.Optional["MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess"], jsii.get(self, "publicAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskClusterBrokerNodeGroupInfoConnectivityInfo]:
        return typing.cast(typing.Optional[MskClusterBrokerNodeGroupInfoConnectivityInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskClusterBrokerNodeGroupInfoConnectivityInfo],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskClusterBrokerNodeGroupInfoConnectivityInfo],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess:
    def __init__(self, *, type: typing.Optional[builtins.str] = None) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#type MskCluster#type}.
        '''
        if __debug__:
            def stub(*, type: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#type MskCluster#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccessOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccessOutputReference",
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

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

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
    ) -> typing.Optional[MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess]:
        return typing.cast(typing.Optional[MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MskClusterBrokerNodeGroupInfoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterBrokerNodeGroupInfoOutputReference",
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

    @jsii.member(jsii_name="putConnectivityInfo")
    def put_connectivity_info(
        self,
        *,
        public_access: typing.Optional[typing.Union[MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param public_access: public_access block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#public_access MskCluster#public_access}
        '''
        value = MskClusterBrokerNodeGroupInfoConnectivityInfo(
            public_access=public_access
        )

        return typing.cast(None, jsii.invoke(self, "putConnectivityInfo", [value]))

    @jsii.member(jsii_name="putStorageInfo")
    def put_storage_info(
        self,
        *,
        ebs_storage_info: typing.Optional[typing.Union["MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ebs_storage_info: ebs_storage_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#ebs_storage_info MskCluster#ebs_storage_info}
        '''
        value = MskClusterBrokerNodeGroupInfoStorageInfo(
            ebs_storage_info=ebs_storage_info
        )

        return typing.cast(None, jsii.invoke(self, "putStorageInfo", [value]))

    @jsii.member(jsii_name="resetAzDistribution")
    def reset_az_distribution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzDistribution", []))

    @jsii.member(jsii_name="resetConnectivityInfo")
    def reset_connectivity_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectivityInfo", []))

    @jsii.member(jsii_name="resetEbsVolumeSize")
    def reset_ebs_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsVolumeSize", []))

    @jsii.member(jsii_name="resetStorageInfo")
    def reset_storage_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageInfo", []))

    @builtins.property
    @jsii.member(jsii_name="connectivityInfo")
    def connectivity_info(
        self,
    ) -> MskClusterBrokerNodeGroupInfoConnectivityInfoOutputReference:
        return typing.cast(MskClusterBrokerNodeGroupInfoConnectivityInfoOutputReference, jsii.get(self, "connectivityInfo"))

    @builtins.property
    @jsii.member(jsii_name="storageInfo")
    def storage_info(self) -> "MskClusterBrokerNodeGroupInfoStorageInfoOutputReference":
        return typing.cast("MskClusterBrokerNodeGroupInfoStorageInfoOutputReference", jsii.get(self, "storageInfo"))

    @builtins.property
    @jsii.member(jsii_name="azDistributionInput")
    def az_distribution_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azDistributionInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSubnetsInput")
    def client_subnets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "clientSubnetsInput"))

    @builtins.property
    @jsii.member(jsii_name="connectivityInfoInput")
    def connectivity_info_input(
        self,
    ) -> typing.Optional[MskClusterBrokerNodeGroupInfoConnectivityInfo]:
        return typing.cast(typing.Optional[MskClusterBrokerNodeGroupInfoConnectivityInfo], jsii.get(self, "connectivityInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeSizeInput")
    def ebs_volume_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ebsVolumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="storageInfoInput")
    def storage_info_input(
        self,
    ) -> typing.Optional["MskClusterBrokerNodeGroupInfoStorageInfo"]:
        return typing.cast(typing.Optional["MskClusterBrokerNodeGroupInfoStorageInfo"], jsii.get(self, "storageInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="azDistribution")
    def az_distribution(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azDistribution"))

    @az_distribution.setter
    def az_distribution(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azDistribution", value)

    @builtins.property
    @jsii.member(jsii_name="clientSubnets")
    def client_subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "clientSubnets"))

    @client_subnets.setter
    def client_subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSubnets", value)

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeSize")
    def ebs_volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsVolumeSize"))

    @ebs_volume_size.setter
    def ebs_volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsVolumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskClusterBrokerNodeGroupInfo]:
        return typing.cast(typing.Optional[MskClusterBrokerNodeGroupInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskClusterBrokerNodeGroupInfo],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[MskClusterBrokerNodeGroupInfo]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterBrokerNodeGroupInfoStorageInfo",
    jsii_struct_bases=[],
    name_mapping={"ebs_storage_info": "ebsStorageInfo"},
)
class MskClusterBrokerNodeGroupInfoStorageInfo:
    def __init__(
        self,
        *,
        ebs_storage_info: typing.Optional[typing.Union["MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ebs_storage_info: ebs_storage_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#ebs_storage_info MskCluster#ebs_storage_info}
        '''
        if isinstance(ebs_storage_info, dict):
            ebs_storage_info = MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo(**ebs_storage_info)
        if __debug__:
            def stub(
                *,
                ebs_storage_info: typing.Optional[typing.Union[MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument ebs_storage_info", value=ebs_storage_info, expected_type=type_hints["ebs_storage_info"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ebs_storage_info is not None:
            self._values["ebs_storage_info"] = ebs_storage_info

    @builtins.property
    def ebs_storage_info(
        self,
    ) -> typing.Optional["MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo"]:
        '''ebs_storage_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#ebs_storage_info MskCluster#ebs_storage_info}
        '''
        result = self._values.get("ebs_storage_info")
        return typing.cast(typing.Optional["MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterBrokerNodeGroupInfoStorageInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo",
    jsii_struct_bases=[],
    name_mapping={
        "provisioned_throughput": "provisionedThroughput",
        "volume_size": "volumeSize",
    },
)
class MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo:
    def __init__(
        self,
        *,
        provisioned_throughput: typing.Optional[typing.Union["MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput", typing.Dict[str, typing.Any]]] = None,
        volume_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param provisioned_throughput: provisioned_throughput block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#provisioned_throughput MskCluster#provisioned_throughput}
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#volume_size MskCluster#volume_size}.
        '''
        if isinstance(provisioned_throughput, dict):
            provisioned_throughput = MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput(**provisioned_throughput)
        if __debug__:
            def stub(
                *,
                provisioned_throughput: typing.Optional[typing.Union[MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput, typing.Dict[str, typing.Any]]] = None,
                volume_size: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument provisioned_throughput", value=provisioned_throughput, expected_type=type_hints["provisioned_throughput"])
            check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
        self._values: typing.Dict[str, typing.Any] = {}
        if provisioned_throughput is not None:
            self._values["provisioned_throughput"] = provisioned_throughput
        if volume_size is not None:
            self._values["volume_size"] = volume_size

    @builtins.property
    def provisioned_throughput(
        self,
    ) -> typing.Optional["MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput"]:
        '''provisioned_throughput block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#provisioned_throughput MskCluster#provisioned_throughput}
        '''
        result = self._values.get("provisioned_throughput")
        return typing.cast(typing.Optional["MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput"], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#volume_size MskCluster#volume_size}.'''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoOutputReference",
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

    @jsii.member(jsii_name="putProvisionedThroughput")
    def put_provisioned_throughput(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        volume_throughput: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enabled MskCluster#enabled}.
        :param volume_throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#volume_throughput MskCluster#volume_throughput}.
        '''
        value = MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput(
            enabled=enabled, volume_throughput=volume_throughput
        )

        return typing.cast(None, jsii.invoke(self, "putProvisionedThroughput", [value]))

    @jsii.member(jsii_name="resetProvisionedThroughput")
    def reset_provisioned_throughput(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvisionedThroughput", []))

    @jsii.member(jsii_name="resetVolumeSize")
    def reset_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeSize", []))

    @builtins.property
    @jsii.member(jsii_name="provisionedThroughput")
    def provisioned_throughput(
        self,
    ) -> "MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughputOutputReference":
        return typing.cast("MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughputOutputReference", jsii.get(self, "provisionedThroughput"))

    @builtins.property
    @jsii.member(jsii_name="provisionedThroughputInput")
    def provisioned_throughput_input(
        self,
    ) -> typing.Optional["MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput"]:
        return typing.cast(typing.Optional["MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput"], jsii.get(self, "provisionedThroughputInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeSizeInput")
    def volume_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeSize")
    def volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumeSize"))

    @volume_size.setter
    def volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo]:
        return typing.cast(typing.Optional[MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "volume_throughput": "volumeThroughput"},
)
class MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        volume_throughput: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enabled MskCluster#enabled}.
        :param volume_throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#volume_throughput MskCluster#volume_throughput}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                volume_throughput: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument volume_throughput", value=volume_throughput, expected_type=type_hints["volume_throughput"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if volume_throughput is not None:
            self._values["volume_throughput"] = volume_throughput

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enabled MskCluster#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def volume_throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#volume_throughput MskCluster#volume_throughput}.'''
        result = self._values.get("volume_throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughputOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughputOutputReference",
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

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetVolumeThroughput")
    def reset_volume_throughput(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeThroughput", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeThroughputInput")
    def volume_throughput_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumeThroughputInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="volumeThroughput")
    def volume_throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumeThroughput"))

    @volume_throughput.setter
    def volume_throughput(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeThroughput", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput]:
        return typing.cast(typing.Optional[MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MskClusterBrokerNodeGroupInfoStorageInfoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterBrokerNodeGroupInfoStorageInfoOutputReference",
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

    @jsii.member(jsii_name="putEbsStorageInfo")
    def put_ebs_storage_info(
        self,
        *,
        provisioned_throughput: typing.Optional[typing.Union[MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput, typing.Dict[str, typing.Any]]] = None,
        volume_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param provisioned_throughput: provisioned_throughput block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#provisioned_throughput MskCluster#provisioned_throughput}
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#volume_size MskCluster#volume_size}.
        '''
        value = MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo(
            provisioned_throughput=provisioned_throughput, volume_size=volume_size
        )

        return typing.cast(None, jsii.invoke(self, "putEbsStorageInfo", [value]))

    @jsii.member(jsii_name="resetEbsStorageInfo")
    def reset_ebs_storage_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsStorageInfo", []))

    @builtins.property
    @jsii.member(jsii_name="ebsStorageInfo")
    def ebs_storage_info(
        self,
    ) -> MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoOutputReference:
        return typing.cast(MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoOutputReference, jsii.get(self, "ebsStorageInfo"))

    @builtins.property
    @jsii.member(jsii_name="ebsStorageInfoInput")
    def ebs_storage_info_input(
        self,
    ) -> typing.Optional[MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo]:
        return typing.cast(typing.Optional[MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo], jsii.get(self, "ebsStorageInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskClusterBrokerNodeGroupInfoStorageInfo]:
        return typing.cast(typing.Optional[MskClusterBrokerNodeGroupInfoStorageInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskClusterBrokerNodeGroupInfoStorageInfo],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskClusterBrokerNodeGroupInfoStorageInfo],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterClientAuthentication",
    jsii_struct_bases=[],
    name_mapping={"sasl": "sasl", "tls": "tls", "unauthenticated": "unauthenticated"},
)
class MskClusterClientAuthentication:
    def __init__(
        self,
        *,
        sasl: typing.Optional[typing.Union["MskClusterClientAuthenticationSasl", typing.Dict[str, typing.Any]]] = None,
        tls: typing.Optional[typing.Union["MskClusterClientAuthenticationTls", typing.Dict[str, typing.Any]]] = None,
        unauthenticated: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param sasl: sasl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#sasl MskCluster#sasl}
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#tls MskCluster#tls}
        :param unauthenticated: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#unauthenticated MskCluster#unauthenticated}.
        '''
        if isinstance(sasl, dict):
            sasl = MskClusterClientAuthenticationSasl(**sasl)
        if isinstance(tls, dict):
            tls = MskClusterClientAuthenticationTls(**tls)
        if __debug__:
            def stub(
                *,
                sasl: typing.Optional[typing.Union[MskClusterClientAuthenticationSasl, typing.Dict[str, typing.Any]]] = None,
                tls: typing.Optional[typing.Union[MskClusterClientAuthenticationTls, typing.Dict[str, typing.Any]]] = None,
                unauthenticated: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument sasl", value=sasl, expected_type=type_hints["sasl"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
            check_type(argname="argument unauthenticated", value=unauthenticated, expected_type=type_hints["unauthenticated"])
        self._values: typing.Dict[str, typing.Any] = {}
        if sasl is not None:
            self._values["sasl"] = sasl
        if tls is not None:
            self._values["tls"] = tls
        if unauthenticated is not None:
            self._values["unauthenticated"] = unauthenticated

    @builtins.property
    def sasl(self) -> typing.Optional["MskClusterClientAuthenticationSasl"]:
        '''sasl block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#sasl MskCluster#sasl}
        '''
        result = self._values.get("sasl")
        return typing.cast(typing.Optional["MskClusterClientAuthenticationSasl"], result)

    @builtins.property
    def tls(self) -> typing.Optional["MskClusterClientAuthenticationTls"]:
        '''tls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#tls MskCluster#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["MskClusterClientAuthenticationTls"], result)

    @builtins.property
    def unauthenticated(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#unauthenticated MskCluster#unauthenticated}.'''
        result = self._values.get("unauthenticated")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterClientAuthentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskClusterClientAuthenticationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterClientAuthenticationOutputReference",
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

    @jsii.member(jsii_name="putSasl")
    def put_sasl(
        self,
        *,
        iam: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        scram: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param iam: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#iam MskCluster#iam}.
        :param scram: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#scram MskCluster#scram}.
        '''
        value = MskClusterClientAuthenticationSasl(iam=iam, scram=scram)

        return typing.cast(None, jsii.invoke(self, "putSasl", [value]))

    @jsii.member(jsii_name="putTls")
    def put_tls(
        self,
        *,
        certificate_authority_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param certificate_authority_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#certificate_authority_arns MskCluster#certificate_authority_arns}.
        '''
        value = MskClusterClientAuthenticationTls(
            certificate_authority_arns=certificate_authority_arns
        )

        return typing.cast(None, jsii.invoke(self, "putTls", [value]))

    @jsii.member(jsii_name="resetSasl")
    def reset_sasl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSasl", []))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @jsii.member(jsii_name="resetUnauthenticated")
    def reset_unauthenticated(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnauthenticated", []))

    @builtins.property
    @jsii.member(jsii_name="sasl")
    def sasl(self) -> "MskClusterClientAuthenticationSaslOutputReference":
        return typing.cast("MskClusterClientAuthenticationSaslOutputReference", jsii.get(self, "sasl"))

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> "MskClusterClientAuthenticationTlsOutputReference":
        return typing.cast("MskClusterClientAuthenticationTlsOutputReference", jsii.get(self, "tls"))

    @builtins.property
    @jsii.member(jsii_name="saslInput")
    def sasl_input(self) -> typing.Optional["MskClusterClientAuthenticationSasl"]:
        return typing.cast(typing.Optional["MskClusterClientAuthenticationSasl"], jsii.get(self, "saslInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(self) -> typing.Optional["MskClusterClientAuthenticationTls"]:
        return typing.cast(typing.Optional["MskClusterClientAuthenticationTls"], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="unauthenticatedInput")
    def unauthenticated_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "unauthenticatedInput"))

    @builtins.property
    @jsii.member(jsii_name="unauthenticated")
    def unauthenticated(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "unauthenticated"))

    @unauthenticated.setter
    def unauthenticated(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unauthenticated", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskClusterClientAuthentication]:
        return typing.cast(typing.Optional[MskClusterClientAuthentication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskClusterClientAuthentication],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[MskClusterClientAuthentication]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterClientAuthenticationSasl",
    jsii_struct_bases=[],
    name_mapping={"iam": "iam", "scram": "scram"},
)
class MskClusterClientAuthenticationSasl:
    def __init__(
        self,
        *,
        iam: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        scram: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param iam: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#iam MskCluster#iam}.
        :param scram: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#scram MskCluster#scram}.
        '''
        if __debug__:
            def stub(
                *,
                iam: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                scram: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument iam", value=iam, expected_type=type_hints["iam"])
            check_type(argname="argument scram", value=scram, expected_type=type_hints["scram"])
        self._values: typing.Dict[str, typing.Any] = {}
        if iam is not None:
            self._values["iam"] = iam
        if scram is not None:
            self._values["scram"] = scram

    @builtins.property
    def iam(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#iam MskCluster#iam}.'''
        result = self._values.get("iam")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def scram(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#scram MskCluster#scram}.'''
        result = self._values.get("scram")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterClientAuthenticationSasl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskClusterClientAuthenticationSaslOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterClientAuthenticationSaslOutputReference",
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

    @jsii.member(jsii_name="resetIam")
    def reset_iam(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIam", []))

    @jsii.member(jsii_name="resetScram")
    def reset_scram(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScram", []))

    @builtins.property
    @jsii.member(jsii_name="iamInput")
    def iam_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "iamInput"))

    @builtins.property
    @jsii.member(jsii_name="scramInput")
    def scram_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "scramInput"))

    @builtins.property
    @jsii.member(jsii_name="iam")
    def iam(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "iam"))

    @iam.setter
    def iam(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iam", value)

    @builtins.property
    @jsii.member(jsii_name="scram")
    def scram(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "scram"))

    @scram.setter
    def scram(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scram", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskClusterClientAuthenticationSasl]:
        return typing.cast(typing.Optional[MskClusterClientAuthenticationSasl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskClusterClientAuthenticationSasl],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskClusterClientAuthenticationSasl],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterClientAuthenticationTls",
    jsii_struct_bases=[],
    name_mapping={"certificate_authority_arns": "certificateAuthorityArns"},
)
class MskClusterClientAuthenticationTls:
    def __init__(
        self,
        *,
        certificate_authority_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param certificate_authority_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#certificate_authority_arns MskCluster#certificate_authority_arns}.
        '''
        if __debug__:
            def stub(
                *,
                certificate_authority_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument certificate_authority_arns", value=certificate_authority_arns, expected_type=type_hints["certificate_authority_arns"])
        self._values: typing.Dict[str, typing.Any] = {}
        if certificate_authority_arns is not None:
            self._values["certificate_authority_arns"] = certificate_authority_arns

    @builtins.property
    def certificate_authority_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#certificate_authority_arns MskCluster#certificate_authority_arns}.'''
        result = self._values.get("certificate_authority_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterClientAuthenticationTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskClusterClientAuthenticationTlsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterClientAuthenticationTlsOutputReference",
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

    @jsii.member(jsii_name="resetCertificateAuthorityArns")
    def reset_certificate_authority_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateAuthorityArns", []))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityArnsInput")
    def certificate_authority_arns_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "certificateAuthorityArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityArns")
    def certificate_authority_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "certificateAuthorityArns"))

    @certificate_authority_arns.setter
    def certificate_authority_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAuthorityArns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskClusterClientAuthenticationTls]:
        return typing.cast(typing.Optional[MskClusterClientAuthenticationTls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskClusterClientAuthenticationTls],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[MskClusterClientAuthenticationTls]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "broker_node_group_info": "brokerNodeGroupInfo",
        "cluster_name": "clusterName",
        "kafka_version": "kafkaVersion",
        "number_of_broker_nodes": "numberOfBrokerNodes",
        "client_authentication": "clientAuthentication",
        "configuration_info": "configurationInfo",
        "encryption_info": "encryptionInfo",
        "enhanced_monitoring": "enhancedMonitoring",
        "id": "id",
        "logging_info": "loggingInfo",
        "open_monitoring": "openMonitoring",
        "storage_mode": "storageMode",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class MskClusterConfig(cdktf.TerraformMetaArguments):
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
        broker_node_group_info: typing.Union[MskClusterBrokerNodeGroupInfo, typing.Dict[str, typing.Any]],
        cluster_name: builtins.str,
        kafka_version: builtins.str,
        number_of_broker_nodes: jsii.Number,
        client_authentication: typing.Optional[typing.Union[MskClusterClientAuthentication, typing.Dict[str, typing.Any]]] = None,
        configuration_info: typing.Optional[typing.Union["MskClusterConfigurationInfo", typing.Dict[str, typing.Any]]] = None,
        encryption_info: typing.Optional[typing.Union["MskClusterEncryptionInfo", typing.Dict[str, typing.Any]]] = None,
        enhanced_monitoring: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        logging_info: typing.Optional[typing.Union["MskClusterLoggingInfo", typing.Dict[str, typing.Any]]] = None,
        open_monitoring: typing.Optional[typing.Union["MskClusterOpenMonitoring", typing.Dict[str, typing.Any]]] = None,
        storage_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MskClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param broker_node_group_info: broker_node_group_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#broker_node_group_info MskCluster#broker_node_group_info}
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#cluster_name MskCluster#cluster_name}.
        :param kafka_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#kafka_version MskCluster#kafka_version}.
        :param number_of_broker_nodes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#number_of_broker_nodes MskCluster#number_of_broker_nodes}.
        :param client_authentication: client_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#client_authentication MskCluster#client_authentication}
        :param configuration_info: configuration_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#configuration_info MskCluster#configuration_info}
        :param encryption_info: encryption_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#encryption_info MskCluster#encryption_info}
        :param enhanced_monitoring: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enhanced_monitoring MskCluster#enhanced_monitoring}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#id MskCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param logging_info: logging_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#logging_info MskCluster#logging_info}
        :param open_monitoring: open_monitoring block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#open_monitoring MskCluster#open_monitoring}
        :param storage_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#storage_mode MskCluster#storage_mode}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#tags MskCluster#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#tags_all MskCluster#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#timeouts MskCluster#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(broker_node_group_info, dict):
            broker_node_group_info = MskClusterBrokerNodeGroupInfo(**broker_node_group_info)
        if isinstance(client_authentication, dict):
            client_authentication = MskClusterClientAuthentication(**client_authentication)
        if isinstance(configuration_info, dict):
            configuration_info = MskClusterConfigurationInfo(**configuration_info)
        if isinstance(encryption_info, dict):
            encryption_info = MskClusterEncryptionInfo(**encryption_info)
        if isinstance(logging_info, dict):
            logging_info = MskClusterLoggingInfo(**logging_info)
        if isinstance(open_monitoring, dict):
            open_monitoring = MskClusterOpenMonitoring(**open_monitoring)
        if isinstance(timeouts, dict):
            timeouts = MskClusterTimeouts(**timeouts)
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
                broker_node_group_info: typing.Union[MskClusterBrokerNodeGroupInfo, typing.Dict[str, typing.Any]],
                cluster_name: builtins.str,
                kafka_version: builtins.str,
                number_of_broker_nodes: jsii.Number,
                client_authentication: typing.Optional[typing.Union[MskClusterClientAuthentication, typing.Dict[str, typing.Any]]] = None,
                configuration_info: typing.Optional[typing.Union[MskClusterConfigurationInfo, typing.Dict[str, typing.Any]]] = None,
                encryption_info: typing.Optional[typing.Union[MskClusterEncryptionInfo, typing.Dict[str, typing.Any]]] = None,
                enhanced_monitoring: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                logging_info: typing.Optional[typing.Union[MskClusterLoggingInfo, typing.Dict[str, typing.Any]]] = None,
                open_monitoring: typing.Optional[typing.Union[MskClusterOpenMonitoring, typing.Dict[str, typing.Any]]] = None,
                storage_mode: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                timeouts: typing.Optional[typing.Union[MskClusterTimeouts, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument broker_node_group_info", value=broker_node_group_info, expected_type=type_hints["broker_node_group_info"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument kafka_version", value=kafka_version, expected_type=type_hints["kafka_version"])
            check_type(argname="argument number_of_broker_nodes", value=number_of_broker_nodes, expected_type=type_hints["number_of_broker_nodes"])
            check_type(argname="argument client_authentication", value=client_authentication, expected_type=type_hints["client_authentication"])
            check_type(argname="argument configuration_info", value=configuration_info, expected_type=type_hints["configuration_info"])
            check_type(argname="argument encryption_info", value=encryption_info, expected_type=type_hints["encryption_info"])
            check_type(argname="argument enhanced_monitoring", value=enhanced_monitoring, expected_type=type_hints["enhanced_monitoring"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument logging_info", value=logging_info, expected_type=type_hints["logging_info"])
            check_type(argname="argument open_monitoring", value=open_monitoring, expected_type=type_hints["open_monitoring"])
            check_type(argname="argument storage_mode", value=storage_mode, expected_type=type_hints["storage_mode"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "broker_node_group_info": broker_node_group_info,
            "cluster_name": cluster_name,
            "kafka_version": kafka_version,
            "number_of_broker_nodes": number_of_broker_nodes,
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
        if client_authentication is not None:
            self._values["client_authentication"] = client_authentication
        if configuration_info is not None:
            self._values["configuration_info"] = configuration_info
        if encryption_info is not None:
            self._values["encryption_info"] = encryption_info
        if enhanced_monitoring is not None:
            self._values["enhanced_monitoring"] = enhanced_monitoring
        if id is not None:
            self._values["id"] = id
        if logging_info is not None:
            self._values["logging_info"] = logging_info
        if open_monitoring is not None:
            self._values["open_monitoring"] = open_monitoring
        if storage_mode is not None:
            self._values["storage_mode"] = storage_mode
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
    def broker_node_group_info(self) -> MskClusterBrokerNodeGroupInfo:
        '''broker_node_group_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#broker_node_group_info MskCluster#broker_node_group_info}
        '''
        result = self._values.get("broker_node_group_info")
        assert result is not None, "Required property 'broker_node_group_info' is missing"
        return typing.cast(MskClusterBrokerNodeGroupInfo, result)

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#cluster_name MskCluster#cluster_name}.'''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kafka_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#kafka_version MskCluster#kafka_version}.'''
        result = self._values.get("kafka_version")
        assert result is not None, "Required property 'kafka_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def number_of_broker_nodes(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#number_of_broker_nodes MskCluster#number_of_broker_nodes}.'''
        result = self._values.get("number_of_broker_nodes")
        assert result is not None, "Required property 'number_of_broker_nodes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def client_authentication(self) -> typing.Optional[MskClusterClientAuthentication]:
        '''client_authentication block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#client_authentication MskCluster#client_authentication}
        '''
        result = self._values.get("client_authentication")
        return typing.cast(typing.Optional[MskClusterClientAuthentication], result)

    @builtins.property
    def configuration_info(self) -> typing.Optional["MskClusterConfigurationInfo"]:
        '''configuration_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#configuration_info MskCluster#configuration_info}
        '''
        result = self._values.get("configuration_info")
        return typing.cast(typing.Optional["MskClusterConfigurationInfo"], result)

    @builtins.property
    def encryption_info(self) -> typing.Optional["MskClusterEncryptionInfo"]:
        '''encryption_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#encryption_info MskCluster#encryption_info}
        '''
        result = self._values.get("encryption_info")
        return typing.cast(typing.Optional["MskClusterEncryptionInfo"], result)

    @builtins.property
    def enhanced_monitoring(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enhanced_monitoring MskCluster#enhanced_monitoring}.'''
        result = self._values.get("enhanced_monitoring")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#id MskCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_info(self) -> typing.Optional["MskClusterLoggingInfo"]:
        '''logging_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#logging_info MskCluster#logging_info}
        '''
        result = self._values.get("logging_info")
        return typing.cast(typing.Optional["MskClusterLoggingInfo"], result)

    @builtins.property
    def open_monitoring(self) -> typing.Optional["MskClusterOpenMonitoring"]:
        '''open_monitoring block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#open_monitoring MskCluster#open_monitoring}
        '''
        result = self._values.get("open_monitoring")
        return typing.cast(typing.Optional["MskClusterOpenMonitoring"], result)

    @builtins.property
    def storage_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#storage_mode MskCluster#storage_mode}.'''
        result = self._values.get("storage_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#tags MskCluster#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#tags_all MskCluster#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MskClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#timeouts MskCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MskClusterTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterConfigurationInfo",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "revision": "revision"},
)
class MskClusterConfigurationInfo:
    def __init__(self, *, arn: builtins.str, revision: jsii.Number) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#arn MskCluster#arn}.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#revision MskCluster#revision}.
        '''
        if __debug__:
            def stub(*, arn: builtins.str, revision: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
        self._values: typing.Dict[str, typing.Any] = {
            "arn": arn,
            "revision": revision,
        }

    @builtins.property
    def arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#arn MskCluster#arn}.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def revision(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#revision MskCluster#revision}.'''
        result = self._values.get("revision")
        assert result is not None, "Required property 'revision' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterConfigurationInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskClusterConfigurationInfoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterConfigurationInfoOutputReference",
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
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="revisionInput")
    def revision_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "revisionInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="revision")
    def revision(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "revision"))

    @revision.setter
    def revision(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revision", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskClusterConfigurationInfo]:
        return typing.cast(typing.Optional[MskClusterConfigurationInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskClusterConfigurationInfo],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[MskClusterConfigurationInfo]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterEncryptionInfo",
    jsii_struct_bases=[],
    name_mapping={
        "encryption_at_rest_kms_key_arn": "encryptionAtRestKmsKeyArn",
        "encryption_in_transit": "encryptionInTransit",
    },
)
class MskClusterEncryptionInfo:
    def __init__(
        self,
        *,
        encryption_at_rest_kms_key_arn: typing.Optional[builtins.str] = None,
        encryption_in_transit: typing.Optional[typing.Union["MskClusterEncryptionInfoEncryptionInTransit", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param encryption_at_rest_kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#encryption_at_rest_kms_key_arn MskCluster#encryption_at_rest_kms_key_arn}.
        :param encryption_in_transit: encryption_in_transit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#encryption_in_transit MskCluster#encryption_in_transit}
        '''
        if isinstance(encryption_in_transit, dict):
            encryption_in_transit = MskClusterEncryptionInfoEncryptionInTransit(**encryption_in_transit)
        if __debug__:
            def stub(
                *,
                encryption_at_rest_kms_key_arn: typing.Optional[builtins.str] = None,
                encryption_in_transit: typing.Optional[typing.Union[MskClusterEncryptionInfoEncryptionInTransit, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument encryption_at_rest_kms_key_arn", value=encryption_at_rest_kms_key_arn, expected_type=type_hints["encryption_at_rest_kms_key_arn"])
            check_type(argname="argument encryption_in_transit", value=encryption_in_transit, expected_type=type_hints["encryption_in_transit"])
        self._values: typing.Dict[str, typing.Any] = {}
        if encryption_at_rest_kms_key_arn is not None:
            self._values["encryption_at_rest_kms_key_arn"] = encryption_at_rest_kms_key_arn
        if encryption_in_transit is not None:
            self._values["encryption_in_transit"] = encryption_in_transit

    @builtins.property
    def encryption_at_rest_kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#encryption_at_rest_kms_key_arn MskCluster#encryption_at_rest_kms_key_arn}.'''
        result = self._values.get("encryption_at_rest_kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_in_transit(
        self,
    ) -> typing.Optional["MskClusterEncryptionInfoEncryptionInTransit"]:
        '''encryption_in_transit block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#encryption_in_transit MskCluster#encryption_in_transit}
        '''
        result = self._values.get("encryption_in_transit")
        return typing.cast(typing.Optional["MskClusterEncryptionInfoEncryptionInTransit"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterEncryptionInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterEncryptionInfoEncryptionInTransit",
    jsii_struct_bases=[],
    name_mapping={"client_broker": "clientBroker", "in_cluster": "inCluster"},
)
class MskClusterEncryptionInfoEncryptionInTransit:
    def __init__(
        self,
        *,
        client_broker: typing.Optional[builtins.str] = None,
        in_cluster: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param client_broker: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#client_broker MskCluster#client_broker}.
        :param in_cluster: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#in_cluster MskCluster#in_cluster}.
        '''
        if __debug__:
            def stub(
                *,
                client_broker: typing.Optional[builtins.str] = None,
                in_cluster: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument client_broker", value=client_broker, expected_type=type_hints["client_broker"])
            check_type(argname="argument in_cluster", value=in_cluster, expected_type=type_hints["in_cluster"])
        self._values: typing.Dict[str, typing.Any] = {}
        if client_broker is not None:
            self._values["client_broker"] = client_broker
        if in_cluster is not None:
            self._values["in_cluster"] = in_cluster

    @builtins.property
    def client_broker(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#client_broker MskCluster#client_broker}.'''
        result = self._values.get("client_broker")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def in_cluster(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#in_cluster MskCluster#in_cluster}.'''
        result = self._values.get("in_cluster")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterEncryptionInfoEncryptionInTransit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskClusterEncryptionInfoEncryptionInTransitOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterEncryptionInfoEncryptionInTransitOutputReference",
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

    @jsii.member(jsii_name="resetClientBroker")
    def reset_client_broker(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientBroker", []))

    @jsii.member(jsii_name="resetInCluster")
    def reset_in_cluster(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInCluster", []))

    @builtins.property
    @jsii.member(jsii_name="clientBrokerInput")
    def client_broker_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientBrokerInput"))

    @builtins.property
    @jsii.member(jsii_name="inClusterInput")
    def in_cluster_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "inClusterInput"))

    @builtins.property
    @jsii.member(jsii_name="clientBroker")
    def client_broker(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientBroker"))

    @client_broker.setter
    def client_broker(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientBroker", value)

    @builtins.property
    @jsii.member(jsii_name="inCluster")
    def in_cluster(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "inCluster"))

    @in_cluster.setter
    def in_cluster(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inCluster", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskClusterEncryptionInfoEncryptionInTransit]:
        return typing.cast(typing.Optional[MskClusterEncryptionInfoEncryptionInTransit], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskClusterEncryptionInfoEncryptionInTransit],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskClusterEncryptionInfoEncryptionInTransit],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MskClusterEncryptionInfoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterEncryptionInfoOutputReference",
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

    @jsii.member(jsii_name="putEncryptionInTransit")
    def put_encryption_in_transit(
        self,
        *,
        client_broker: typing.Optional[builtins.str] = None,
        in_cluster: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param client_broker: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#client_broker MskCluster#client_broker}.
        :param in_cluster: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#in_cluster MskCluster#in_cluster}.
        '''
        value = MskClusterEncryptionInfoEncryptionInTransit(
            client_broker=client_broker, in_cluster=in_cluster
        )

        return typing.cast(None, jsii.invoke(self, "putEncryptionInTransit", [value]))

    @jsii.member(jsii_name="resetEncryptionAtRestKmsKeyArn")
    def reset_encryption_at_rest_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionAtRestKmsKeyArn", []))

    @jsii.member(jsii_name="resetEncryptionInTransit")
    def reset_encryption_in_transit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionInTransit", []))

    @builtins.property
    @jsii.member(jsii_name="encryptionInTransit")
    def encryption_in_transit(
        self,
    ) -> MskClusterEncryptionInfoEncryptionInTransitOutputReference:
        return typing.cast(MskClusterEncryptionInfoEncryptionInTransitOutputReference, jsii.get(self, "encryptionInTransit"))

    @builtins.property
    @jsii.member(jsii_name="encryptionAtRestKmsKeyArnInput")
    def encryption_at_rest_kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionAtRestKmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionInTransitInput")
    def encryption_in_transit_input(
        self,
    ) -> typing.Optional[MskClusterEncryptionInfoEncryptionInTransit]:
        return typing.cast(typing.Optional[MskClusterEncryptionInfoEncryptionInTransit], jsii.get(self, "encryptionInTransitInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionAtRestKmsKeyArn")
    def encryption_at_rest_kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionAtRestKmsKeyArn"))

    @encryption_at_rest_kms_key_arn.setter
    def encryption_at_rest_kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionAtRestKmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskClusterEncryptionInfo]:
        return typing.cast(typing.Optional[MskClusterEncryptionInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MskClusterEncryptionInfo]) -> None:
        if __debug__:
            def stub(value: typing.Optional[MskClusterEncryptionInfo]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterLoggingInfo",
    jsii_struct_bases=[],
    name_mapping={"broker_logs": "brokerLogs"},
)
class MskClusterLoggingInfo:
    def __init__(
        self,
        *,
        broker_logs: typing.Union["MskClusterLoggingInfoBrokerLogs", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param broker_logs: broker_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#broker_logs MskCluster#broker_logs}
        '''
        if isinstance(broker_logs, dict):
            broker_logs = MskClusterLoggingInfoBrokerLogs(**broker_logs)
        if __debug__:
            def stub(
                *,
                broker_logs: typing.Union[MskClusterLoggingInfoBrokerLogs, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument broker_logs", value=broker_logs, expected_type=type_hints["broker_logs"])
        self._values: typing.Dict[str, typing.Any] = {
            "broker_logs": broker_logs,
        }

    @builtins.property
    def broker_logs(self) -> "MskClusterLoggingInfoBrokerLogs":
        '''broker_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#broker_logs MskCluster#broker_logs}
        '''
        result = self._values.get("broker_logs")
        assert result is not None, "Required property 'broker_logs' is missing"
        return typing.cast("MskClusterLoggingInfoBrokerLogs", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterLoggingInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterLoggingInfoBrokerLogs",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_logs": "cloudwatchLogs",
        "firehose": "firehose",
        "s3": "s3",
    },
)
class MskClusterLoggingInfoBrokerLogs:
    def __init__(
        self,
        *,
        cloudwatch_logs: typing.Optional[typing.Union["MskClusterLoggingInfoBrokerLogsCloudwatchLogs", typing.Dict[str, typing.Any]]] = None,
        firehose: typing.Optional[typing.Union["MskClusterLoggingInfoBrokerLogsFirehose", typing.Dict[str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["MskClusterLoggingInfoBrokerLogsS3", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_logs: cloudwatch_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#cloudwatch_logs MskCluster#cloudwatch_logs}
        :param firehose: firehose block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#firehose MskCluster#firehose}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#s3 MskCluster#s3}
        '''
        if isinstance(cloudwatch_logs, dict):
            cloudwatch_logs = MskClusterLoggingInfoBrokerLogsCloudwatchLogs(**cloudwatch_logs)
        if isinstance(firehose, dict):
            firehose = MskClusterLoggingInfoBrokerLogsFirehose(**firehose)
        if isinstance(s3, dict):
            s3 = MskClusterLoggingInfoBrokerLogsS3(**s3)
        if __debug__:
            def stub(
                *,
                cloudwatch_logs: typing.Optional[typing.Union[MskClusterLoggingInfoBrokerLogsCloudwatchLogs, typing.Dict[str, typing.Any]]] = None,
                firehose: typing.Optional[typing.Union[MskClusterLoggingInfoBrokerLogsFirehose, typing.Dict[str, typing.Any]]] = None,
                s3: typing.Optional[typing.Union[MskClusterLoggingInfoBrokerLogsS3, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cloudwatch_logs", value=cloudwatch_logs, expected_type=type_hints["cloudwatch_logs"])
            check_type(argname="argument firehose", value=firehose, expected_type=type_hints["firehose"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cloudwatch_logs is not None:
            self._values["cloudwatch_logs"] = cloudwatch_logs
        if firehose is not None:
            self._values["firehose"] = firehose
        if s3 is not None:
            self._values["s3"] = s3

    @builtins.property
    def cloudwatch_logs(
        self,
    ) -> typing.Optional["MskClusterLoggingInfoBrokerLogsCloudwatchLogs"]:
        '''cloudwatch_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#cloudwatch_logs MskCluster#cloudwatch_logs}
        '''
        result = self._values.get("cloudwatch_logs")
        return typing.cast(typing.Optional["MskClusterLoggingInfoBrokerLogsCloudwatchLogs"], result)

    @builtins.property
    def firehose(self) -> typing.Optional["MskClusterLoggingInfoBrokerLogsFirehose"]:
        '''firehose block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#firehose MskCluster#firehose}
        '''
        result = self._values.get("firehose")
        return typing.cast(typing.Optional["MskClusterLoggingInfoBrokerLogsFirehose"], result)

    @builtins.property
    def s3(self) -> typing.Optional["MskClusterLoggingInfoBrokerLogsS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#s3 MskCluster#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["MskClusterLoggingInfoBrokerLogsS3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterLoggingInfoBrokerLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterLoggingInfoBrokerLogsCloudwatchLogs",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "log_group": "logGroup"},
)
class MskClusterLoggingInfoBrokerLogsCloudwatchLogs:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        log_group: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enabled MskCluster#enabled}.
        :param log_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#log_group MskCluster#log_group}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Union[builtins.bool, cdktf.IResolvable],
                log_group: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if log_group is not None:
            self._values["log_group"] = log_group

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enabled MskCluster#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def log_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#log_group MskCluster#log_group}.'''
        result = self._values.get("log_group")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterLoggingInfoBrokerLogsCloudwatchLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskClusterLoggingInfoBrokerLogsCloudwatchLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterLoggingInfoBrokerLogsCloudwatchLogsOutputReference",
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

    @jsii.member(jsii_name="resetLogGroup")
    def reset_log_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroup", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupInput")
    def log_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="logGroup")
    def log_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroup"))

    @log_group.setter
    def log_group(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroup", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskClusterLoggingInfoBrokerLogsCloudwatchLogs]:
        return typing.cast(typing.Optional[MskClusterLoggingInfoBrokerLogsCloudwatchLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskClusterLoggingInfoBrokerLogsCloudwatchLogs],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskClusterLoggingInfoBrokerLogsCloudwatchLogs],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterLoggingInfoBrokerLogsFirehose",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "delivery_stream": "deliveryStream"},
)
class MskClusterLoggingInfoBrokerLogsFirehose:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        delivery_stream: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enabled MskCluster#enabled}.
        :param delivery_stream: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#delivery_stream MskCluster#delivery_stream}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Union[builtins.bool, cdktf.IResolvable],
                delivery_stream: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument delivery_stream", value=delivery_stream, expected_type=type_hints["delivery_stream"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if delivery_stream is not None:
            self._values["delivery_stream"] = delivery_stream

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enabled MskCluster#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def delivery_stream(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#delivery_stream MskCluster#delivery_stream}.'''
        result = self._values.get("delivery_stream")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterLoggingInfoBrokerLogsFirehose(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskClusterLoggingInfoBrokerLogsFirehoseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterLoggingInfoBrokerLogsFirehoseOutputReference",
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

    @jsii.member(jsii_name="resetDeliveryStream")
    def reset_delivery_stream(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeliveryStream", []))

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamInput")
    def delivery_stream_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryStreamInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryStream")
    def delivery_stream(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deliveryStream"))

    @delivery_stream.setter
    def delivery_stream(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryStream", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskClusterLoggingInfoBrokerLogsFirehose]:
        return typing.cast(typing.Optional[MskClusterLoggingInfoBrokerLogsFirehose], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskClusterLoggingInfoBrokerLogsFirehose],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskClusterLoggingInfoBrokerLogsFirehose],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MskClusterLoggingInfoBrokerLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterLoggingInfoBrokerLogsOutputReference",
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

    @jsii.member(jsii_name="putCloudwatchLogs")
    def put_cloudwatch_logs(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        log_group: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enabled MskCluster#enabled}.
        :param log_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#log_group MskCluster#log_group}.
        '''
        value = MskClusterLoggingInfoBrokerLogsCloudwatchLogs(
            enabled=enabled, log_group=log_group
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLogs", [value]))

    @jsii.member(jsii_name="putFirehose")
    def put_firehose(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        delivery_stream: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enabled MskCluster#enabled}.
        :param delivery_stream: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#delivery_stream MskCluster#delivery_stream}.
        '''
        value = MskClusterLoggingInfoBrokerLogsFirehose(
            enabled=enabled, delivery_stream=delivery_stream
        )

        return typing.cast(None, jsii.invoke(self, "putFirehose", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        bucket: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enabled MskCluster#enabled}.
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#bucket MskCluster#bucket}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#prefix MskCluster#prefix}.
        '''
        value = MskClusterLoggingInfoBrokerLogsS3(
            enabled=enabled, bucket=bucket, prefix=prefix
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="resetCloudwatchLogs")
    def reset_cloudwatch_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLogs", []))

    @jsii.member(jsii_name="resetFirehose")
    def reset_firehose(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirehose", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogs")
    def cloudwatch_logs(
        self,
    ) -> MskClusterLoggingInfoBrokerLogsCloudwatchLogsOutputReference:
        return typing.cast(MskClusterLoggingInfoBrokerLogsCloudwatchLogsOutputReference, jsii.get(self, "cloudwatchLogs"))

    @builtins.property
    @jsii.member(jsii_name="firehose")
    def firehose(self) -> MskClusterLoggingInfoBrokerLogsFirehoseOutputReference:
        return typing.cast(MskClusterLoggingInfoBrokerLogsFirehoseOutputReference, jsii.get(self, "firehose"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "MskClusterLoggingInfoBrokerLogsS3OutputReference":
        return typing.cast("MskClusterLoggingInfoBrokerLogsS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogsInput")
    def cloudwatch_logs_input(
        self,
    ) -> typing.Optional[MskClusterLoggingInfoBrokerLogsCloudwatchLogs]:
        return typing.cast(typing.Optional[MskClusterLoggingInfoBrokerLogsCloudwatchLogs], jsii.get(self, "cloudwatchLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="firehoseInput")
    def firehose_input(
        self,
    ) -> typing.Optional[MskClusterLoggingInfoBrokerLogsFirehose]:
        return typing.cast(typing.Optional[MskClusterLoggingInfoBrokerLogsFirehose], jsii.get(self, "firehoseInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(self) -> typing.Optional["MskClusterLoggingInfoBrokerLogsS3"]:
        return typing.cast(typing.Optional["MskClusterLoggingInfoBrokerLogsS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskClusterLoggingInfoBrokerLogs]:
        return typing.cast(typing.Optional[MskClusterLoggingInfoBrokerLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskClusterLoggingInfoBrokerLogs],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[MskClusterLoggingInfoBrokerLogs]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterLoggingInfoBrokerLogsS3",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "bucket": "bucket", "prefix": "prefix"},
)
class MskClusterLoggingInfoBrokerLogsS3:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        bucket: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enabled MskCluster#enabled}.
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#bucket MskCluster#bucket}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#prefix MskCluster#prefix}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Union[builtins.bool, cdktf.IResolvable],
                bucket: typing.Optional[builtins.str] = None,
                prefix: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if bucket is not None:
            self._values["bucket"] = bucket
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enabled MskCluster#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#bucket MskCluster#bucket}.'''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#prefix MskCluster#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterLoggingInfoBrokerLogsS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskClusterLoggingInfoBrokerLogsS3OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterLoggingInfoBrokerLogsS3OutputReference",
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

    @jsii.member(jsii_name="resetBucket")
    def reset_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucket", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskClusterLoggingInfoBrokerLogsS3]:
        return typing.cast(typing.Optional[MskClusterLoggingInfoBrokerLogsS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskClusterLoggingInfoBrokerLogsS3],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[MskClusterLoggingInfoBrokerLogsS3]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MskClusterLoggingInfoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterLoggingInfoOutputReference",
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

    @jsii.member(jsii_name="putBrokerLogs")
    def put_broker_logs(
        self,
        *,
        cloudwatch_logs: typing.Optional[typing.Union[MskClusterLoggingInfoBrokerLogsCloudwatchLogs, typing.Dict[str, typing.Any]]] = None,
        firehose: typing.Optional[typing.Union[MskClusterLoggingInfoBrokerLogsFirehose, typing.Dict[str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union[MskClusterLoggingInfoBrokerLogsS3, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_logs: cloudwatch_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#cloudwatch_logs MskCluster#cloudwatch_logs}
        :param firehose: firehose block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#firehose MskCluster#firehose}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#s3 MskCluster#s3}
        '''
        value = MskClusterLoggingInfoBrokerLogs(
            cloudwatch_logs=cloudwatch_logs, firehose=firehose, s3=s3
        )

        return typing.cast(None, jsii.invoke(self, "putBrokerLogs", [value]))

    @builtins.property
    @jsii.member(jsii_name="brokerLogs")
    def broker_logs(self) -> MskClusterLoggingInfoBrokerLogsOutputReference:
        return typing.cast(MskClusterLoggingInfoBrokerLogsOutputReference, jsii.get(self, "brokerLogs"))

    @builtins.property
    @jsii.member(jsii_name="brokerLogsInput")
    def broker_logs_input(self) -> typing.Optional[MskClusterLoggingInfoBrokerLogs]:
        return typing.cast(typing.Optional[MskClusterLoggingInfoBrokerLogs], jsii.get(self, "brokerLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskClusterLoggingInfo]:
        return typing.cast(typing.Optional[MskClusterLoggingInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MskClusterLoggingInfo]) -> None:
        if __debug__:
            def stub(value: typing.Optional[MskClusterLoggingInfo]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterOpenMonitoring",
    jsii_struct_bases=[],
    name_mapping={"prometheus": "prometheus"},
)
class MskClusterOpenMonitoring:
    def __init__(
        self,
        *,
        prometheus: typing.Union["MskClusterOpenMonitoringPrometheus", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param prometheus: prometheus block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#prometheus MskCluster#prometheus}
        '''
        if isinstance(prometheus, dict):
            prometheus = MskClusterOpenMonitoringPrometheus(**prometheus)
        if __debug__:
            def stub(
                *,
                prometheus: typing.Union[MskClusterOpenMonitoringPrometheus, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument prometheus", value=prometheus, expected_type=type_hints["prometheus"])
        self._values: typing.Dict[str, typing.Any] = {
            "prometheus": prometheus,
        }

    @builtins.property
    def prometheus(self) -> "MskClusterOpenMonitoringPrometheus":
        '''prometheus block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#prometheus MskCluster#prometheus}
        '''
        result = self._values.get("prometheus")
        assert result is not None, "Required property 'prometheus' is missing"
        return typing.cast("MskClusterOpenMonitoringPrometheus", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterOpenMonitoring(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskClusterOpenMonitoringOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterOpenMonitoringOutputReference",
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

    @jsii.member(jsii_name="putPrometheus")
    def put_prometheus(
        self,
        *,
        jmx_exporter: typing.Optional[typing.Union["MskClusterOpenMonitoringPrometheusJmxExporter", typing.Dict[str, typing.Any]]] = None,
        node_exporter: typing.Optional[typing.Union["MskClusterOpenMonitoringPrometheusNodeExporter", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param jmx_exporter: jmx_exporter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#jmx_exporter MskCluster#jmx_exporter}
        :param node_exporter: node_exporter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#node_exporter MskCluster#node_exporter}
        '''
        value = MskClusterOpenMonitoringPrometheus(
            jmx_exporter=jmx_exporter, node_exporter=node_exporter
        )

        return typing.cast(None, jsii.invoke(self, "putPrometheus", [value]))

    @builtins.property
    @jsii.member(jsii_name="prometheus")
    def prometheus(self) -> "MskClusterOpenMonitoringPrometheusOutputReference":
        return typing.cast("MskClusterOpenMonitoringPrometheusOutputReference", jsii.get(self, "prometheus"))

    @builtins.property
    @jsii.member(jsii_name="prometheusInput")
    def prometheus_input(self) -> typing.Optional["MskClusterOpenMonitoringPrometheus"]:
        return typing.cast(typing.Optional["MskClusterOpenMonitoringPrometheus"], jsii.get(self, "prometheusInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskClusterOpenMonitoring]:
        return typing.cast(typing.Optional[MskClusterOpenMonitoring], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MskClusterOpenMonitoring]) -> None:
        if __debug__:
            def stub(value: typing.Optional[MskClusterOpenMonitoring]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterOpenMonitoringPrometheus",
    jsii_struct_bases=[],
    name_mapping={"jmx_exporter": "jmxExporter", "node_exporter": "nodeExporter"},
)
class MskClusterOpenMonitoringPrometheus:
    def __init__(
        self,
        *,
        jmx_exporter: typing.Optional[typing.Union["MskClusterOpenMonitoringPrometheusJmxExporter", typing.Dict[str, typing.Any]]] = None,
        node_exporter: typing.Optional[typing.Union["MskClusterOpenMonitoringPrometheusNodeExporter", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param jmx_exporter: jmx_exporter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#jmx_exporter MskCluster#jmx_exporter}
        :param node_exporter: node_exporter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#node_exporter MskCluster#node_exporter}
        '''
        if isinstance(jmx_exporter, dict):
            jmx_exporter = MskClusterOpenMonitoringPrometheusJmxExporter(**jmx_exporter)
        if isinstance(node_exporter, dict):
            node_exporter = MskClusterOpenMonitoringPrometheusNodeExporter(**node_exporter)
        if __debug__:
            def stub(
                *,
                jmx_exporter: typing.Optional[typing.Union[MskClusterOpenMonitoringPrometheusJmxExporter, typing.Dict[str, typing.Any]]] = None,
                node_exporter: typing.Optional[typing.Union[MskClusterOpenMonitoringPrometheusNodeExporter, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument jmx_exporter", value=jmx_exporter, expected_type=type_hints["jmx_exporter"])
            check_type(argname="argument node_exporter", value=node_exporter, expected_type=type_hints["node_exporter"])
        self._values: typing.Dict[str, typing.Any] = {}
        if jmx_exporter is not None:
            self._values["jmx_exporter"] = jmx_exporter
        if node_exporter is not None:
            self._values["node_exporter"] = node_exporter

    @builtins.property
    def jmx_exporter(
        self,
    ) -> typing.Optional["MskClusterOpenMonitoringPrometheusJmxExporter"]:
        '''jmx_exporter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#jmx_exporter MskCluster#jmx_exporter}
        '''
        result = self._values.get("jmx_exporter")
        return typing.cast(typing.Optional["MskClusterOpenMonitoringPrometheusJmxExporter"], result)

    @builtins.property
    def node_exporter(
        self,
    ) -> typing.Optional["MskClusterOpenMonitoringPrometheusNodeExporter"]:
        '''node_exporter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#node_exporter MskCluster#node_exporter}
        '''
        result = self._values.get("node_exporter")
        return typing.cast(typing.Optional["MskClusterOpenMonitoringPrometheusNodeExporter"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterOpenMonitoringPrometheus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterOpenMonitoringPrometheusJmxExporter",
    jsii_struct_bases=[],
    name_mapping={"enabled_in_broker": "enabledInBroker"},
)
class MskClusterOpenMonitoringPrometheusJmxExporter:
    def __init__(
        self,
        *,
        enabled_in_broker: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled_in_broker: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enabled_in_broker MskCluster#enabled_in_broker}.
        '''
        if __debug__:
            def stub(
                *,
                enabled_in_broker: typing.Union[builtins.bool, cdktf.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled_in_broker", value=enabled_in_broker, expected_type=type_hints["enabled_in_broker"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled_in_broker": enabled_in_broker,
        }

    @builtins.property
    def enabled_in_broker(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enabled_in_broker MskCluster#enabled_in_broker}.'''
        result = self._values.get("enabled_in_broker")
        assert result is not None, "Required property 'enabled_in_broker' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterOpenMonitoringPrometheusJmxExporter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskClusterOpenMonitoringPrometheusJmxExporterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterOpenMonitoringPrometheusJmxExporterOutputReference",
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
    @jsii.member(jsii_name="enabledInBrokerInput")
    def enabled_in_broker_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInBrokerInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInBroker")
    def enabled_in_broker(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabledInBroker"))

    @enabled_in_broker.setter
    def enabled_in_broker(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledInBroker", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskClusterOpenMonitoringPrometheusJmxExporter]:
        return typing.cast(typing.Optional[MskClusterOpenMonitoringPrometheusJmxExporter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskClusterOpenMonitoringPrometheusJmxExporter],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskClusterOpenMonitoringPrometheusJmxExporter],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterOpenMonitoringPrometheusNodeExporter",
    jsii_struct_bases=[],
    name_mapping={"enabled_in_broker": "enabledInBroker"},
)
class MskClusterOpenMonitoringPrometheusNodeExporter:
    def __init__(
        self,
        *,
        enabled_in_broker: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled_in_broker: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enabled_in_broker MskCluster#enabled_in_broker}.
        '''
        if __debug__:
            def stub(
                *,
                enabled_in_broker: typing.Union[builtins.bool, cdktf.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled_in_broker", value=enabled_in_broker, expected_type=type_hints["enabled_in_broker"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled_in_broker": enabled_in_broker,
        }

    @builtins.property
    def enabled_in_broker(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enabled_in_broker MskCluster#enabled_in_broker}.'''
        result = self._values.get("enabled_in_broker")
        assert result is not None, "Required property 'enabled_in_broker' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterOpenMonitoringPrometheusNodeExporter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskClusterOpenMonitoringPrometheusNodeExporterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterOpenMonitoringPrometheusNodeExporterOutputReference",
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
    @jsii.member(jsii_name="enabledInBrokerInput")
    def enabled_in_broker_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInBrokerInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInBroker")
    def enabled_in_broker(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabledInBroker"))

    @enabled_in_broker.setter
    def enabled_in_broker(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledInBroker", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskClusterOpenMonitoringPrometheusNodeExporter]:
        return typing.cast(typing.Optional[MskClusterOpenMonitoringPrometheusNodeExporter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskClusterOpenMonitoringPrometheusNodeExporter],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskClusterOpenMonitoringPrometheusNodeExporter],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MskClusterOpenMonitoringPrometheusOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterOpenMonitoringPrometheusOutputReference",
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

    @jsii.member(jsii_name="putJmxExporter")
    def put_jmx_exporter(
        self,
        *,
        enabled_in_broker: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled_in_broker: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enabled_in_broker MskCluster#enabled_in_broker}.
        '''
        value = MskClusterOpenMonitoringPrometheusJmxExporter(
            enabled_in_broker=enabled_in_broker
        )

        return typing.cast(None, jsii.invoke(self, "putJmxExporter", [value]))

    @jsii.member(jsii_name="putNodeExporter")
    def put_node_exporter(
        self,
        *,
        enabled_in_broker: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled_in_broker: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#enabled_in_broker MskCluster#enabled_in_broker}.
        '''
        value = MskClusterOpenMonitoringPrometheusNodeExporter(
            enabled_in_broker=enabled_in_broker
        )

        return typing.cast(None, jsii.invoke(self, "putNodeExporter", [value]))

    @jsii.member(jsii_name="resetJmxExporter")
    def reset_jmx_exporter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJmxExporter", []))

    @jsii.member(jsii_name="resetNodeExporter")
    def reset_node_exporter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeExporter", []))

    @builtins.property
    @jsii.member(jsii_name="jmxExporter")
    def jmx_exporter(
        self,
    ) -> MskClusterOpenMonitoringPrometheusJmxExporterOutputReference:
        return typing.cast(MskClusterOpenMonitoringPrometheusJmxExporterOutputReference, jsii.get(self, "jmxExporter"))

    @builtins.property
    @jsii.member(jsii_name="nodeExporter")
    def node_exporter(
        self,
    ) -> MskClusterOpenMonitoringPrometheusNodeExporterOutputReference:
        return typing.cast(MskClusterOpenMonitoringPrometheusNodeExporterOutputReference, jsii.get(self, "nodeExporter"))

    @builtins.property
    @jsii.member(jsii_name="jmxExporterInput")
    def jmx_exporter_input(
        self,
    ) -> typing.Optional[MskClusterOpenMonitoringPrometheusJmxExporter]:
        return typing.cast(typing.Optional[MskClusterOpenMonitoringPrometheusJmxExporter], jsii.get(self, "jmxExporterInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeExporterInput")
    def node_exporter_input(
        self,
    ) -> typing.Optional[MskClusterOpenMonitoringPrometheusNodeExporter]:
        return typing.cast(typing.Optional[MskClusterOpenMonitoringPrometheusNodeExporter], jsii.get(self, "nodeExporterInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskClusterOpenMonitoringPrometheus]:
        return typing.cast(typing.Optional[MskClusterOpenMonitoringPrometheus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskClusterOpenMonitoringPrometheus],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskClusterOpenMonitoringPrometheus],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class MskClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#create MskCluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#delete MskCluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#update MskCluster#update}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#create MskCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#delete MskCluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/msk_cluster#update MskCluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskClusterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskCluster.MskClusterTimeoutsOutputReference",
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
    ) -> typing.Optional[typing.Union[MskClusterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MskClusterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MskClusterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[MskClusterTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MskCluster",
    "MskClusterBrokerNodeGroupInfo",
    "MskClusterBrokerNodeGroupInfoConnectivityInfo",
    "MskClusterBrokerNodeGroupInfoConnectivityInfoOutputReference",
    "MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccess",
    "MskClusterBrokerNodeGroupInfoConnectivityInfoPublicAccessOutputReference",
    "MskClusterBrokerNodeGroupInfoOutputReference",
    "MskClusterBrokerNodeGroupInfoStorageInfo",
    "MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfo",
    "MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoOutputReference",
    "MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughput",
    "MskClusterBrokerNodeGroupInfoStorageInfoEbsStorageInfoProvisionedThroughputOutputReference",
    "MskClusterBrokerNodeGroupInfoStorageInfoOutputReference",
    "MskClusterClientAuthentication",
    "MskClusterClientAuthenticationOutputReference",
    "MskClusterClientAuthenticationSasl",
    "MskClusterClientAuthenticationSaslOutputReference",
    "MskClusterClientAuthenticationTls",
    "MskClusterClientAuthenticationTlsOutputReference",
    "MskClusterConfig",
    "MskClusterConfigurationInfo",
    "MskClusterConfigurationInfoOutputReference",
    "MskClusterEncryptionInfo",
    "MskClusterEncryptionInfoEncryptionInTransit",
    "MskClusterEncryptionInfoEncryptionInTransitOutputReference",
    "MskClusterEncryptionInfoOutputReference",
    "MskClusterLoggingInfo",
    "MskClusterLoggingInfoBrokerLogs",
    "MskClusterLoggingInfoBrokerLogsCloudwatchLogs",
    "MskClusterLoggingInfoBrokerLogsCloudwatchLogsOutputReference",
    "MskClusterLoggingInfoBrokerLogsFirehose",
    "MskClusterLoggingInfoBrokerLogsFirehoseOutputReference",
    "MskClusterLoggingInfoBrokerLogsOutputReference",
    "MskClusterLoggingInfoBrokerLogsS3",
    "MskClusterLoggingInfoBrokerLogsS3OutputReference",
    "MskClusterLoggingInfoOutputReference",
    "MskClusterOpenMonitoring",
    "MskClusterOpenMonitoringOutputReference",
    "MskClusterOpenMonitoringPrometheus",
    "MskClusterOpenMonitoringPrometheusJmxExporter",
    "MskClusterOpenMonitoringPrometheusJmxExporterOutputReference",
    "MskClusterOpenMonitoringPrometheusNodeExporter",
    "MskClusterOpenMonitoringPrometheusNodeExporterOutputReference",
    "MskClusterOpenMonitoringPrometheusOutputReference",
    "MskClusterTimeouts",
    "MskClusterTimeoutsOutputReference",
]

publication.publish()
