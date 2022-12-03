'''
# `aws_mskconnect_connector`

Refer to the Terraform Registory for docs: [`aws_mskconnect_connector`](https://www.terraform.io/docs/providers/aws/r/mskconnect_connector).
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


class MskconnectConnector(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnector",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector aws_mskconnect_connector}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        capacity: typing.Union["MskconnectConnectorCapacity", typing.Dict[str, typing.Any]],
        connector_configuration: typing.Mapping[builtins.str, builtins.str],
        kafka_cluster: typing.Union["MskconnectConnectorKafkaCluster", typing.Dict[str, typing.Any]],
        kafka_cluster_client_authentication: typing.Union["MskconnectConnectorKafkaClusterClientAuthentication", typing.Dict[str, typing.Any]],
        kafka_cluster_encryption_in_transit: typing.Union["MskconnectConnectorKafkaClusterEncryptionInTransit", typing.Dict[str, typing.Any]],
        kafkaconnect_version: builtins.str,
        name: builtins.str,
        plugin: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MskconnectConnectorPlugin", typing.Dict[str, typing.Any]]]],
        service_execution_role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        log_delivery: typing.Optional[typing.Union["MskconnectConnectorLogDelivery", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["MskconnectConnectorTimeouts", typing.Dict[str, typing.Any]]] = None,
        worker_configuration: typing.Optional[typing.Union["MskconnectConnectorWorkerConfiguration", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector aws_mskconnect_connector} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param capacity: capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#capacity MskconnectConnector#capacity}
        :param connector_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#connector_configuration MskconnectConnector#connector_configuration}.
        :param kafka_cluster: kafka_cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafka_cluster MskconnectConnector#kafka_cluster}
        :param kafka_cluster_client_authentication: kafka_cluster_client_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafka_cluster_client_authentication MskconnectConnector#kafka_cluster_client_authentication}
        :param kafka_cluster_encryption_in_transit: kafka_cluster_encryption_in_transit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafka_cluster_encryption_in_transit MskconnectConnector#kafka_cluster_encryption_in_transit}
        :param kafkaconnect_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafkaconnect_version MskconnectConnector#kafkaconnect_version}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#name MskconnectConnector#name}.
        :param plugin: plugin block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#plugin MskconnectConnector#plugin}
        :param service_execution_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#service_execution_role_arn MskconnectConnector#service_execution_role_arn}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#description MskconnectConnector#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#id MskconnectConnector#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_delivery: log_delivery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#log_delivery MskconnectConnector#log_delivery}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#timeouts MskconnectConnector#timeouts}
        :param worker_configuration: worker_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#worker_configuration MskconnectConnector#worker_configuration}
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
                capacity: typing.Union[MskconnectConnectorCapacity, typing.Dict[str, typing.Any]],
                connector_configuration: typing.Mapping[builtins.str, builtins.str],
                kafka_cluster: typing.Union[MskconnectConnectorKafkaCluster, typing.Dict[str, typing.Any]],
                kafka_cluster_client_authentication: typing.Union[MskconnectConnectorKafkaClusterClientAuthentication, typing.Dict[str, typing.Any]],
                kafka_cluster_encryption_in_transit: typing.Union[MskconnectConnectorKafkaClusterEncryptionInTransit, typing.Dict[str, typing.Any]],
                kafkaconnect_version: builtins.str,
                name: builtins.str,
                plugin: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MskconnectConnectorPlugin, typing.Dict[str, typing.Any]]]],
                service_execution_role_arn: builtins.str,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                log_delivery: typing.Optional[typing.Union[MskconnectConnectorLogDelivery, typing.Dict[str, typing.Any]]] = None,
                timeouts: typing.Optional[typing.Union[MskconnectConnectorTimeouts, typing.Dict[str, typing.Any]]] = None,
                worker_configuration: typing.Optional[typing.Union[MskconnectConnectorWorkerConfiguration, typing.Dict[str, typing.Any]]] = None,
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
        config = MskconnectConnectorConfig(
            capacity=capacity,
            connector_configuration=connector_configuration,
            kafka_cluster=kafka_cluster,
            kafka_cluster_client_authentication=kafka_cluster_client_authentication,
            kafka_cluster_encryption_in_transit=kafka_cluster_encryption_in_transit,
            kafkaconnect_version=kafkaconnect_version,
            name=name,
            plugin=plugin,
            service_execution_role_arn=service_execution_role_arn,
            description=description,
            id=id,
            log_delivery=log_delivery,
            timeouts=timeouts,
            worker_configuration=worker_configuration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCapacity")
    def put_capacity(
        self,
        *,
        autoscaling: typing.Optional[typing.Union["MskconnectConnectorCapacityAutoscaling", typing.Dict[str, typing.Any]]] = None,
        provisioned_capacity: typing.Optional[typing.Union["MskconnectConnectorCapacityProvisionedCapacity", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param autoscaling: autoscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#autoscaling MskconnectConnector#autoscaling}
        :param provisioned_capacity: provisioned_capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#provisioned_capacity MskconnectConnector#provisioned_capacity}
        '''
        value = MskconnectConnectorCapacity(
            autoscaling=autoscaling, provisioned_capacity=provisioned_capacity
        )

        return typing.cast(None, jsii.invoke(self, "putCapacity", [value]))

    @jsii.member(jsii_name="putKafkaCluster")
    def put_kafka_cluster(
        self,
        *,
        apache_kafka_cluster: typing.Union["MskconnectConnectorKafkaClusterApacheKafkaCluster", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param apache_kafka_cluster: apache_kafka_cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#apache_kafka_cluster MskconnectConnector#apache_kafka_cluster}
        '''
        value = MskconnectConnectorKafkaCluster(
            apache_kafka_cluster=apache_kafka_cluster
        )

        return typing.cast(None, jsii.invoke(self, "putKafkaCluster", [value]))

    @jsii.member(jsii_name="putKafkaClusterClientAuthentication")
    def put_kafka_cluster_client_authentication(
        self,
        *,
        authentication_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#authentication_type MskconnectConnector#authentication_type}.
        '''
        value = MskconnectConnectorKafkaClusterClientAuthentication(
            authentication_type=authentication_type
        )

        return typing.cast(None, jsii.invoke(self, "putKafkaClusterClientAuthentication", [value]))

    @jsii.member(jsii_name="putKafkaClusterEncryptionInTransit")
    def put_kafka_cluster_encryption_in_transit(
        self,
        *,
        encryption_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#encryption_type MskconnectConnector#encryption_type}.
        '''
        value = MskconnectConnectorKafkaClusterEncryptionInTransit(
            encryption_type=encryption_type
        )

        return typing.cast(None, jsii.invoke(self, "putKafkaClusterEncryptionInTransit", [value]))

    @jsii.member(jsii_name="putLogDelivery")
    def put_log_delivery(
        self,
        *,
        worker_log_delivery: typing.Union["MskconnectConnectorLogDeliveryWorkerLogDelivery", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param worker_log_delivery: worker_log_delivery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#worker_log_delivery MskconnectConnector#worker_log_delivery}
        '''
        value = MskconnectConnectorLogDelivery(worker_log_delivery=worker_log_delivery)

        return typing.cast(None, jsii.invoke(self, "putLogDelivery", [value]))

    @jsii.member(jsii_name="putPlugin")
    def put_plugin(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MskconnectConnectorPlugin", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MskconnectConnectorPlugin, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPlugin", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#create MskconnectConnector#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#delete MskconnectConnector#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#update MskconnectConnector#update}.
        '''
        value = MskconnectConnectorTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWorkerConfiguration")
    def put_worker_configuration(
        self,
        *,
        arn: builtins.str,
        revision: jsii.Number,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#arn MskconnectConnector#arn}.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#revision MskconnectConnector#revision}.
        '''
        value = MskconnectConnectorWorkerConfiguration(arn=arn, revision=revision)

        return typing.cast(None, jsii.invoke(self, "putWorkerConfiguration", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogDelivery")
    def reset_log_delivery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogDelivery", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWorkerConfiguration")
    def reset_worker_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkerConfiguration", []))

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
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> "MskconnectConnectorCapacityOutputReference":
        return typing.cast("MskconnectConnectorCapacityOutputReference", jsii.get(self, "capacity"))

    @builtins.property
    @jsii.member(jsii_name="kafkaCluster")
    def kafka_cluster(self) -> "MskconnectConnectorKafkaClusterOutputReference":
        return typing.cast("MskconnectConnectorKafkaClusterOutputReference", jsii.get(self, "kafkaCluster"))

    @builtins.property
    @jsii.member(jsii_name="kafkaClusterClientAuthentication")
    def kafka_cluster_client_authentication(
        self,
    ) -> "MskconnectConnectorKafkaClusterClientAuthenticationOutputReference":
        return typing.cast("MskconnectConnectorKafkaClusterClientAuthenticationOutputReference", jsii.get(self, "kafkaClusterClientAuthentication"))

    @builtins.property
    @jsii.member(jsii_name="kafkaClusterEncryptionInTransit")
    def kafka_cluster_encryption_in_transit(
        self,
    ) -> "MskconnectConnectorKafkaClusterEncryptionInTransitOutputReference":
        return typing.cast("MskconnectConnectorKafkaClusterEncryptionInTransitOutputReference", jsii.get(self, "kafkaClusterEncryptionInTransit"))

    @builtins.property
    @jsii.member(jsii_name="logDelivery")
    def log_delivery(self) -> "MskconnectConnectorLogDeliveryOutputReference":
        return typing.cast("MskconnectConnectorLogDeliveryOutputReference", jsii.get(self, "logDelivery"))

    @builtins.property
    @jsii.member(jsii_name="plugin")
    def plugin(self) -> "MskconnectConnectorPluginList":
        return typing.cast("MskconnectConnectorPluginList", jsii.get(self, "plugin"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MskconnectConnectorTimeoutsOutputReference":
        return typing.cast("MskconnectConnectorTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="workerConfiguration")
    def worker_configuration(
        self,
    ) -> "MskconnectConnectorWorkerConfigurationOutputReference":
        return typing.cast("MskconnectConnectorWorkerConfigurationOutputReference", jsii.get(self, "workerConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(self) -> typing.Optional["MskconnectConnectorCapacity"]:
        return typing.cast(typing.Optional["MskconnectConnectorCapacity"], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorConfigurationInput")
    def connector_configuration_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "connectorConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kafkaClusterClientAuthenticationInput")
    def kafka_cluster_client_authentication_input(
        self,
    ) -> typing.Optional["MskconnectConnectorKafkaClusterClientAuthentication"]:
        return typing.cast(typing.Optional["MskconnectConnectorKafkaClusterClientAuthentication"], jsii.get(self, "kafkaClusterClientAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="kafkaClusterEncryptionInTransitInput")
    def kafka_cluster_encryption_in_transit_input(
        self,
    ) -> typing.Optional["MskconnectConnectorKafkaClusterEncryptionInTransit"]:
        return typing.cast(typing.Optional["MskconnectConnectorKafkaClusterEncryptionInTransit"], jsii.get(self, "kafkaClusterEncryptionInTransitInput"))

    @builtins.property
    @jsii.member(jsii_name="kafkaClusterInput")
    def kafka_cluster_input(self) -> typing.Optional["MskconnectConnectorKafkaCluster"]:
        return typing.cast(typing.Optional["MskconnectConnectorKafkaCluster"], jsii.get(self, "kafkaClusterInput"))

    @builtins.property
    @jsii.member(jsii_name="kafkaconnectVersionInput")
    def kafkaconnect_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kafkaconnectVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="logDeliveryInput")
    def log_delivery_input(self) -> typing.Optional["MskconnectConnectorLogDelivery"]:
        return typing.cast(typing.Optional["MskconnectConnectorLogDelivery"], jsii.get(self, "logDeliveryInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginInput")
    def plugin_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MskconnectConnectorPlugin"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MskconnectConnectorPlugin"]]], jsii.get(self, "pluginInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceExecutionRoleArnInput")
    def service_execution_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceExecutionRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MskconnectConnectorTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MskconnectConnectorTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="workerConfigurationInput")
    def worker_configuration_input(
        self,
    ) -> typing.Optional["MskconnectConnectorWorkerConfiguration"]:
        return typing.cast(typing.Optional["MskconnectConnectorWorkerConfiguration"], jsii.get(self, "workerConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="connectorConfiguration")
    def connector_configuration(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "connectorConfiguration"))

    @connector_configuration.setter
    def connector_configuration(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorConfiguration", value)

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
    @jsii.member(jsii_name="kafkaconnectVersion")
    def kafkaconnect_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kafkaconnectVersion"))

    @kafkaconnect_version.setter
    def kafkaconnect_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kafkaconnectVersion", value)

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
    @jsii.member(jsii_name="serviceExecutionRoleArn")
    def service_execution_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceExecutionRoleArn"))

    @service_execution_role_arn.setter
    def service_execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceExecutionRoleArn", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorCapacity",
    jsii_struct_bases=[],
    name_mapping={
        "autoscaling": "autoscaling",
        "provisioned_capacity": "provisionedCapacity",
    },
)
class MskconnectConnectorCapacity:
    def __init__(
        self,
        *,
        autoscaling: typing.Optional[typing.Union["MskconnectConnectorCapacityAutoscaling", typing.Dict[str, typing.Any]]] = None,
        provisioned_capacity: typing.Optional[typing.Union["MskconnectConnectorCapacityProvisionedCapacity", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param autoscaling: autoscaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#autoscaling MskconnectConnector#autoscaling}
        :param provisioned_capacity: provisioned_capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#provisioned_capacity MskconnectConnector#provisioned_capacity}
        '''
        if isinstance(autoscaling, dict):
            autoscaling = MskconnectConnectorCapacityAutoscaling(**autoscaling)
        if isinstance(provisioned_capacity, dict):
            provisioned_capacity = MskconnectConnectorCapacityProvisionedCapacity(**provisioned_capacity)
        if __debug__:
            def stub(
                *,
                autoscaling: typing.Optional[typing.Union[MskconnectConnectorCapacityAutoscaling, typing.Dict[str, typing.Any]]] = None,
                provisioned_capacity: typing.Optional[typing.Union[MskconnectConnectorCapacityProvisionedCapacity, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument autoscaling", value=autoscaling, expected_type=type_hints["autoscaling"])
            check_type(argname="argument provisioned_capacity", value=provisioned_capacity, expected_type=type_hints["provisioned_capacity"])
        self._values: typing.Dict[str, typing.Any] = {}
        if autoscaling is not None:
            self._values["autoscaling"] = autoscaling
        if provisioned_capacity is not None:
            self._values["provisioned_capacity"] = provisioned_capacity

    @builtins.property
    def autoscaling(self) -> typing.Optional["MskconnectConnectorCapacityAutoscaling"]:
        '''autoscaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#autoscaling MskconnectConnector#autoscaling}
        '''
        result = self._values.get("autoscaling")
        return typing.cast(typing.Optional["MskconnectConnectorCapacityAutoscaling"], result)

    @builtins.property
    def provisioned_capacity(
        self,
    ) -> typing.Optional["MskconnectConnectorCapacityProvisionedCapacity"]:
        '''provisioned_capacity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#provisioned_capacity MskconnectConnector#provisioned_capacity}
        '''
        result = self._values.get("provisioned_capacity")
        return typing.cast(typing.Optional["MskconnectConnectorCapacityProvisionedCapacity"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorCapacity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorCapacityAutoscaling",
    jsii_struct_bases=[],
    name_mapping={
        "max_worker_count": "maxWorkerCount",
        "min_worker_count": "minWorkerCount",
        "mcu_count": "mcuCount",
        "scale_in_policy": "scaleInPolicy",
        "scale_out_policy": "scaleOutPolicy",
    },
)
class MskconnectConnectorCapacityAutoscaling:
    def __init__(
        self,
        *,
        max_worker_count: jsii.Number,
        min_worker_count: jsii.Number,
        mcu_count: typing.Optional[jsii.Number] = None,
        scale_in_policy: typing.Optional[typing.Union["MskconnectConnectorCapacityAutoscalingScaleInPolicy", typing.Dict[str, typing.Any]]] = None,
        scale_out_policy: typing.Optional[typing.Union["MskconnectConnectorCapacityAutoscalingScaleOutPolicy", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param max_worker_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#max_worker_count MskconnectConnector#max_worker_count}.
        :param min_worker_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#min_worker_count MskconnectConnector#min_worker_count}.
        :param mcu_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#mcu_count MskconnectConnector#mcu_count}.
        :param scale_in_policy: scale_in_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#scale_in_policy MskconnectConnector#scale_in_policy}
        :param scale_out_policy: scale_out_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#scale_out_policy MskconnectConnector#scale_out_policy}
        '''
        if isinstance(scale_in_policy, dict):
            scale_in_policy = MskconnectConnectorCapacityAutoscalingScaleInPolicy(**scale_in_policy)
        if isinstance(scale_out_policy, dict):
            scale_out_policy = MskconnectConnectorCapacityAutoscalingScaleOutPolicy(**scale_out_policy)
        if __debug__:
            def stub(
                *,
                max_worker_count: jsii.Number,
                min_worker_count: jsii.Number,
                mcu_count: typing.Optional[jsii.Number] = None,
                scale_in_policy: typing.Optional[typing.Union[MskconnectConnectorCapacityAutoscalingScaleInPolicy, typing.Dict[str, typing.Any]]] = None,
                scale_out_policy: typing.Optional[typing.Union[MskconnectConnectorCapacityAutoscalingScaleOutPolicy, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max_worker_count", value=max_worker_count, expected_type=type_hints["max_worker_count"])
            check_type(argname="argument min_worker_count", value=min_worker_count, expected_type=type_hints["min_worker_count"])
            check_type(argname="argument mcu_count", value=mcu_count, expected_type=type_hints["mcu_count"])
            check_type(argname="argument scale_in_policy", value=scale_in_policy, expected_type=type_hints["scale_in_policy"])
            check_type(argname="argument scale_out_policy", value=scale_out_policy, expected_type=type_hints["scale_out_policy"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_worker_count": max_worker_count,
            "min_worker_count": min_worker_count,
        }
        if mcu_count is not None:
            self._values["mcu_count"] = mcu_count
        if scale_in_policy is not None:
            self._values["scale_in_policy"] = scale_in_policy
        if scale_out_policy is not None:
            self._values["scale_out_policy"] = scale_out_policy

    @builtins.property
    def max_worker_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#max_worker_count MskconnectConnector#max_worker_count}.'''
        result = self._values.get("max_worker_count")
        assert result is not None, "Required property 'max_worker_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_worker_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#min_worker_count MskconnectConnector#min_worker_count}.'''
        result = self._values.get("min_worker_count")
        assert result is not None, "Required property 'min_worker_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def mcu_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#mcu_count MskconnectConnector#mcu_count}.'''
        result = self._values.get("mcu_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scale_in_policy(
        self,
    ) -> typing.Optional["MskconnectConnectorCapacityAutoscalingScaleInPolicy"]:
        '''scale_in_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#scale_in_policy MskconnectConnector#scale_in_policy}
        '''
        result = self._values.get("scale_in_policy")
        return typing.cast(typing.Optional["MskconnectConnectorCapacityAutoscalingScaleInPolicy"], result)

    @builtins.property
    def scale_out_policy(
        self,
    ) -> typing.Optional["MskconnectConnectorCapacityAutoscalingScaleOutPolicy"]:
        '''scale_out_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#scale_out_policy MskconnectConnector#scale_out_policy}
        '''
        result = self._values.get("scale_out_policy")
        return typing.cast(typing.Optional["MskconnectConnectorCapacityAutoscalingScaleOutPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorCapacityAutoscaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorCapacityAutoscalingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorCapacityAutoscalingOutputReference",
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

    @jsii.member(jsii_name="putScaleInPolicy")
    def put_scale_in_policy(
        self,
        *,
        cpu_utilization_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu_utilization_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#cpu_utilization_percentage MskconnectConnector#cpu_utilization_percentage}.
        '''
        value = MskconnectConnectorCapacityAutoscalingScaleInPolicy(
            cpu_utilization_percentage=cpu_utilization_percentage
        )

        return typing.cast(None, jsii.invoke(self, "putScaleInPolicy", [value]))

    @jsii.member(jsii_name="putScaleOutPolicy")
    def put_scale_out_policy(
        self,
        *,
        cpu_utilization_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu_utilization_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#cpu_utilization_percentage MskconnectConnector#cpu_utilization_percentage}.
        '''
        value = MskconnectConnectorCapacityAutoscalingScaleOutPolicy(
            cpu_utilization_percentage=cpu_utilization_percentage
        )

        return typing.cast(None, jsii.invoke(self, "putScaleOutPolicy", [value]))

    @jsii.member(jsii_name="resetMcuCount")
    def reset_mcu_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMcuCount", []))

    @jsii.member(jsii_name="resetScaleInPolicy")
    def reset_scale_in_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleInPolicy", []))

    @jsii.member(jsii_name="resetScaleOutPolicy")
    def reset_scale_out_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleOutPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="scaleInPolicy")
    def scale_in_policy(
        self,
    ) -> "MskconnectConnectorCapacityAutoscalingScaleInPolicyOutputReference":
        return typing.cast("MskconnectConnectorCapacityAutoscalingScaleInPolicyOutputReference", jsii.get(self, "scaleInPolicy"))

    @builtins.property
    @jsii.member(jsii_name="scaleOutPolicy")
    def scale_out_policy(
        self,
    ) -> "MskconnectConnectorCapacityAutoscalingScaleOutPolicyOutputReference":
        return typing.cast("MskconnectConnectorCapacityAutoscalingScaleOutPolicyOutputReference", jsii.get(self, "scaleOutPolicy"))

    @builtins.property
    @jsii.member(jsii_name="maxWorkerCountInput")
    def max_worker_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxWorkerCountInput"))

    @builtins.property
    @jsii.member(jsii_name="mcuCountInput")
    def mcu_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mcuCountInput"))

    @builtins.property
    @jsii.member(jsii_name="minWorkerCountInput")
    def min_worker_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minWorkerCountInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleInPolicyInput")
    def scale_in_policy_input(
        self,
    ) -> typing.Optional["MskconnectConnectorCapacityAutoscalingScaleInPolicy"]:
        return typing.cast(typing.Optional["MskconnectConnectorCapacityAutoscalingScaleInPolicy"], jsii.get(self, "scaleInPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleOutPolicyInput")
    def scale_out_policy_input(
        self,
    ) -> typing.Optional["MskconnectConnectorCapacityAutoscalingScaleOutPolicy"]:
        return typing.cast(typing.Optional["MskconnectConnectorCapacityAutoscalingScaleOutPolicy"], jsii.get(self, "scaleOutPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="maxWorkerCount")
    def max_worker_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxWorkerCount"))

    @max_worker_count.setter
    def max_worker_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWorkerCount", value)

    @builtins.property
    @jsii.member(jsii_name="mcuCount")
    def mcu_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mcuCount"))

    @mcu_count.setter
    def mcu_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mcuCount", value)

    @builtins.property
    @jsii.member(jsii_name="minWorkerCount")
    def min_worker_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minWorkerCount"))

    @min_worker_count.setter
    def min_worker_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minWorkerCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskconnectConnectorCapacityAutoscaling]:
        return typing.cast(typing.Optional[MskconnectConnectorCapacityAutoscaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorCapacityAutoscaling],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskconnectConnectorCapacityAutoscaling],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorCapacityAutoscalingScaleInPolicy",
    jsii_struct_bases=[],
    name_mapping={"cpu_utilization_percentage": "cpuUtilizationPercentage"},
)
class MskconnectConnectorCapacityAutoscalingScaleInPolicy:
    def __init__(
        self,
        *,
        cpu_utilization_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu_utilization_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#cpu_utilization_percentage MskconnectConnector#cpu_utilization_percentage}.
        '''
        if __debug__:
            def stub(
                *,
                cpu_utilization_percentage: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cpu_utilization_percentage", value=cpu_utilization_percentage, expected_type=type_hints["cpu_utilization_percentage"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cpu_utilization_percentage is not None:
            self._values["cpu_utilization_percentage"] = cpu_utilization_percentage

    @builtins.property
    def cpu_utilization_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#cpu_utilization_percentage MskconnectConnector#cpu_utilization_percentage}.'''
        result = self._values.get("cpu_utilization_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorCapacityAutoscalingScaleInPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorCapacityAutoscalingScaleInPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorCapacityAutoscalingScaleInPolicyOutputReference",
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

    @jsii.member(jsii_name="resetCpuUtilizationPercentage")
    def reset_cpu_utilization_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuUtilizationPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="cpuUtilizationPercentageInput")
    def cpu_utilization_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuUtilizationPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuUtilizationPercentage")
    def cpu_utilization_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuUtilizationPercentage"))

    @cpu_utilization_percentage.setter
    def cpu_utilization_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuUtilizationPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorCapacityAutoscalingScaleInPolicy]:
        return typing.cast(typing.Optional[MskconnectConnectorCapacityAutoscalingScaleInPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorCapacityAutoscalingScaleInPolicy],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskconnectConnectorCapacityAutoscalingScaleInPolicy],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorCapacityAutoscalingScaleOutPolicy",
    jsii_struct_bases=[],
    name_mapping={"cpu_utilization_percentage": "cpuUtilizationPercentage"},
)
class MskconnectConnectorCapacityAutoscalingScaleOutPolicy:
    def __init__(
        self,
        *,
        cpu_utilization_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cpu_utilization_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#cpu_utilization_percentage MskconnectConnector#cpu_utilization_percentage}.
        '''
        if __debug__:
            def stub(
                *,
                cpu_utilization_percentage: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cpu_utilization_percentage", value=cpu_utilization_percentage, expected_type=type_hints["cpu_utilization_percentage"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cpu_utilization_percentage is not None:
            self._values["cpu_utilization_percentage"] = cpu_utilization_percentage

    @builtins.property
    def cpu_utilization_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#cpu_utilization_percentage MskconnectConnector#cpu_utilization_percentage}.'''
        result = self._values.get("cpu_utilization_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorCapacityAutoscalingScaleOutPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorCapacityAutoscalingScaleOutPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorCapacityAutoscalingScaleOutPolicyOutputReference",
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

    @jsii.member(jsii_name="resetCpuUtilizationPercentage")
    def reset_cpu_utilization_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuUtilizationPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="cpuUtilizationPercentageInput")
    def cpu_utilization_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuUtilizationPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuUtilizationPercentage")
    def cpu_utilization_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuUtilizationPercentage"))

    @cpu_utilization_percentage.setter
    def cpu_utilization_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuUtilizationPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorCapacityAutoscalingScaleOutPolicy]:
        return typing.cast(typing.Optional[MskconnectConnectorCapacityAutoscalingScaleOutPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorCapacityAutoscalingScaleOutPolicy],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskconnectConnectorCapacityAutoscalingScaleOutPolicy],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MskconnectConnectorCapacityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorCapacityOutputReference",
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

    @jsii.member(jsii_name="putAutoscaling")
    def put_autoscaling(
        self,
        *,
        max_worker_count: jsii.Number,
        min_worker_count: jsii.Number,
        mcu_count: typing.Optional[jsii.Number] = None,
        scale_in_policy: typing.Optional[typing.Union[MskconnectConnectorCapacityAutoscalingScaleInPolicy, typing.Dict[str, typing.Any]]] = None,
        scale_out_policy: typing.Optional[typing.Union[MskconnectConnectorCapacityAutoscalingScaleOutPolicy, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param max_worker_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#max_worker_count MskconnectConnector#max_worker_count}.
        :param min_worker_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#min_worker_count MskconnectConnector#min_worker_count}.
        :param mcu_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#mcu_count MskconnectConnector#mcu_count}.
        :param scale_in_policy: scale_in_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#scale_in_policy MskconnectConnector#scale_in_policy}
        :param scale_out_policy: scale_out_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#scale_out_policy MskconnectConnector#scale_out_policy}
        '''
        value = MskconnectConnectorCapacityAutoscaling(
            max_worker_count=max_worker_count,
            min_worker_count=min_worker_count,
            mcu_count=mcu_count,
            scale_in_policy=scale_in_policy,
            scale_out_policy=scale_out_policy,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscaling", [value]))

    @jsii.member(jsii_name="putProvisionedCapacity")
    def put_provisioned_capacity(
        self,
        *,
        worker_count: jsii.Number,
        mcu_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param worker_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#worker_count MskconnectConnector#worker_count}.
        :param mcu_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#mcu_count MskconnectConnector#mcu_count}.
        '''
        value = MskconnectConnectorCapacityProvisionedCapacity(
            worker_count=worker_count, mcu_count=mcu_count
        )

        return typing.cast(None, jsii.invoke(self, "putProvisionedCapacity", [value]))

    @jsii.member(jsii_name="resetAutoscaling")
    def reset_autoscaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscaling", []))

    @jsii.member(jsii_name="resetProvisionedCapacity")
    def reset_provisioned_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvisionedCapacity", []))

    @builtins.property
    @jsii.member(jsii_name="autoscaling")
    def autoscaling(self) -> MskconnectConnectorCapacityAutoscalingOutputReference:
        return typing.cast(MskconnectConnectorCapacityAutoscalingOutputReference, jsii.get(self, "autoscaling"))

    @builtins.property
    @jsii.member(jsii_name="provisionedCapacity")
    def provisioned_capacity(
        self,
    ) -> "MskconnectConnectorCapacityProvisionedCapacityOutputReference":
        return typing.cast("MskconnectConnectorCapacityProvisionedCapacityOutputReference", jsii.get(self, "provisionedCapacity"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingInput")
    def autoscaling_input(
        self,
    ) -> typing.Optional[MskconnectConnectorCapacityAutoscaling]:
        return typing.cast(typing.Optional[MskconnectConnectorCapacityAutoscaling], jsii.get(self, "autoscalingInput"))

    @builtins.property
    @jsii.member(jsii_name="provisionedCapacityInput")
    def provisioned_capacity_input(
        self,
    ) -> typing.Optional["MskconnectConnectorCapacityProvisionedCapacity"]:
        return typing.cast(typing.Optional["MskconnectConnectorCapacityProvisionedCapacity"], jsii.get(self, "provisionedCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskconnectConnectorCapacity]:
        return typing.cast(typing.Optional[MskconnectConnectorCapacity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorCapacity],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[MskconnectConnectorCapacity]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorCapacityProvisionedCapacity",
    jsii_struct_bases=[],
    name_mapping={"worker_count": "workerCount", "mcu_count": "mcuCount"},
)
class MskconnectConnectorCapacityProvisionedCapacity:
    def __init__(
        self,
        *,
        worker_count: jsii.Number,
        mcu_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param worker_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#worker_count MskconnectConnector#worker_count}.
        :param mcu_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#mcu_count MskconnectConnector#mcu_count}.
        '''
        if __debug__:
            def stub(
                *,
                worker_count: jsii.Number,
                mcu_count: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument worker_count", value=worker_count, expected_type=type_hints["worker_count"])
            check_type(argname="argument mcu_count", value=mcu_count, expected_type=type_hints["mcu_count"])
        self._values: typing.Dict[str, typing.Any] = {
            "worker_count": worker_count,
        }
        if mcu_count is not None:
            self._values["mcu_count"] = mcu_count

    @builtins.property
    def worker_count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#worker_count MskconnectConnector#worker_count}.'''
        result = self._values.get("worker_count")
        assert result is not None, "Required property 'worker_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def mcu_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#mcu_count MskconnectConnector#mcu_count}.'''
        result = self._values.get("mcu_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorCapacityProvisionedCapacity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorCapacityProvisionedCapacityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorCapacityProvisionedCapacityOutputReference",
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

    @jsii.member(jsii_name="resetMcuCount")
    def reset_mcu_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMcuCount", []))

    @builtins.property
    @jsii.member(jsii_name="mcuCountInput")
    def mcu_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mcuCountInput"))

    @builtins.property
    @jsii.member(jsii_name="workerCountInput")
    def worker_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "workerCountInput"))

    @builtins.property
    @jsii.member(jsii_name="mcuCount")
    def mcu_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mcuCount"))

    @mcu_count.setter
    def mcu_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mcuCount", value)

    @builtins.property
    @jsii.member(jsii_name="workerCount")
    def worker_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "workerCount"))

    @worker_count.setter
    def worker_count(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workerCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorCapacityProvisionedCapacity]:
        return typing.cast(typing.Optional[MskconnectConnectorCapacityProvisionedCapacity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorCapacityProvisionedCapacity],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskconnectConnectorCapacityProvisionedCapacity],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "capacity": "capacity",
        "connector_configuration": "connectorConfiguration",
        "kafka_cluster": "kafkaCluster",
        "kafka_cluster_client_authentication": "kafkaClusterClientAuthentication",
        "kafka_cluster_encryption_in_transit": "kafkaClusterEncryptionInTransit",
        "kafkaconnect_version": "kafkaconnectVersion",
        "name": "name",
        "plugin": "plugin",
        "service_execution_role_arn": "serviceExecutionRoleArn",
        "description": "description",
        "id": "id",
        "log_delivery": "logDelivery",
        "timeouts": "timeouts",
        "worker_configuration": "workerConfiguration",
    },
)
class MskconnectConnectorConfig(cdktf.TerraformMetaArguments):
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
        capacity: typing.Union[MskconnectConnectorCapacity, typing.Dict[str, typing.Any]],
        connector_configuration: typing.Mapping[builtins.str, builtins.str],
        kafka_cluster: typing.Union["MskconnectConnectorKafkaCluster", typing.Dict[str, typing.Any]],
        kafka_cluster_client_authentication: typing.Union["MskconnectConnectorKafkaClusterClientAuthentication", typing.Dict[str, typing.Any]],
        kafka_cluster_encryption_in_transit: typing.Union["MskconnectConnectorKafkaClusterEncryptionInTransit", typing.Dict[str, typing.Any]],
        kafkaconnect_version: builtins.str,
        name: builtins.str,
        plugin: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MskconnectConnectorPlugin", typing.Dict[str, typing.Any]]]],
        service_execution_role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        log_delivery: typing.Optional[typing.Union["MskconnectConnectorLogDelivery", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["MskconnectConnectorTimeouts", typing.Dict[str, typing.Any]]] = None,
        worker_configuration: typing.Optional[typing.Union["MskconnectConnectorWorkerConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param capacity: capacity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#capacity MskconnectConnector#capacity}
        :param connector_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#connector_configuration MskconnectConnector#connector_configuration}.
        :param kafka_cluster: kafka_cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafka_cluster MskconnectConnector#kafka_cluster}
        :param kafka_cluster_client_authentication: kafka_cluster_client_authentication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafka_cluster_client_authentication MskconnectConnector#kafka_cluster_client_authentication}
        :param kafka_cluster_encryption_in_transit: kafka_cluster_encryption_in_transit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafka_cluster_encryption_in_transit MskconnectConnector#kafka_cluster_encryption_in_transit}
        :param kafkaconnect_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafkaconnect_version MskconnectConnector#kafkaconnect_version}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#name MskconnectConnector#name}.
        :param plugin: plugin block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#plugin MskconnectConnector#plugin}
        :param service_execution_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#service_execution_role_arn MskconnectConnector#service_execution_role_arn}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#description MskconnectConnector#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#id MskconnectConnector#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_delivery: log_delivery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#log_delivery MskconnectConnector#log_delivery}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#timeouts MskconnectConnector#timeouts}
        :param worker_configuration: worker_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#worker_configuration MskconnectConnector#worker_configuration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(capacity, dict):
            capacity = MskconnectConnectorCapacity(**capacity)
        if isinstance(kafka_cluster, dict):
            kafka_cluster = MskconnectConnectorKafkaCluster(**kafka_cluster)
        if isinstance(kafka_cluster_client_authentication, dict):
            kafka_cluster_client_authentication = MskconnectConnectorKafkaClusterClientAuthentication(**kafka_cluster_client_authentication)
        if isinstance(kafka_cluster_encryption_in_transit, dict):
            kafka_cluster_encryption_in_transit = MskconnectConnectorKafkaClusterEncryptionInTransit(**kafka_cluster_encryption_in_transit)
        if isinstance(log_delivery, dict):
            log_delivery = MskconnectConnectorLogDelivery(**log_delivery)
        if isinstance(timeouts, dict):
            timeouts = MskconnectConnectorTimeouts(**timeouts)
        if isinstance(worker_configuration, dict):
            worker_configuration = MskconnectConnectorWorkerConfiguration(**worker_configuration)
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
                capacity: typing.Union[MskconnectConnectorCapacity, typing.Dict[str, typing.Any]],
                connector_configuration: typing.Mapping[builtins.str, builtins.str],
                kafka_cluster: typing.Union[MskconnectConnectorKafkaCluster, typing.Dict[str, typing.Any]],
                kafka_cluster_client_authentication: typing.Union[MskconnectConnectorKafkaClusterClientAuthentication, typing.Dict[str, typing.Any]],
                kafka_cluster_encryption_in_transit: typing.Union[MskconnectConnectorKafkaClusterEncryptionInTransit, typing.Dict[str, typing.Any]],
                kafkaconnect_version: builtins.str,
                name: builtins.str,
                plugin: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MskconnectConnectorPlugin, typing.Dict[str, typing.Any]]]],
                service_execution_role_arn: builtins.str,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                log_delivery: typing.Optional[typing.Union[MskconnectConnectorLogDelivery, typing.Dict[str, typing.Any]]] = None,
                timeouts: typing.Optional[typing.Union[MskconnectConnectorTimeouts, typing.Dict[str, typing.Any]]] = None,
                worker_configuration: typing.Optional[typing.Union[MskconnectConnectorWorkerConfiguration, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument connector_configuration", value=connector_configuration, expected_type=type_hints["connector_configuration"])
            check_type(argname="argument kafka_cluster", value=kafka_cluster, expected_type=type_hints["kafka_cluster"])
            check_type(argname="argument kafka_cluster_client_authentication", value=kafka_cluster_client_authentication, expected_type=type_hints["kafka_cluster_client_authentication"])
            check_type(argname="argument kafka_cluster_encryption_in_transit", value=kafka_cluster_encryption_in_transit, expected_type=type_hints["kafka_cluster_encryption_in_transit"])
            check_type(argname="argument kafkaconnect_version", value=kafkaconnect_version, expected_type=type_hints["kafkaconnect_version"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument plugin", value=plugin, expected_type=type_hints["plugin"])
            check_type(argname="argument service_execution_role_arn", value=service_execution_role_arn, expected_type=type_hints["service_execution_role_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log_delivery", value=log_delivery, expected_type=type_hints["log_delivery"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument worker_configuration", value=worker_configuration, expected_type=type_hints["worker_configuration"])
        self._values: typing.Dict[str, typing.Any] = {
            "capacity": capacity,
            "connector_configuration": connector_configuration,
            "kafka_cluster": kafka_cluster,
            "kafka_cluster_client_authentication": kafka_cluster_client_authentication,
            "kafka_cluster_encryption_in_transit": kafka_cluster_encryption_in_transit,
            "kafkaconnect_version": kafkaconnect_version,
            "name": name,
            "plugin": plugin,
            "service_execution_role_arn": service_execution_role_arn,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if log_delivery is not None:
            self._values["log_delivery"] = log_delivery
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if worker_configuration is not None:
            self._values["worker_configuration"] = worker_configuration

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
    def capacity(self) -> MskconnectConnectorCapacity:
        '''capacity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#capacity MskconnectConnector#capacity}
        '''
        result = self._values.get("capacity")
        assert result is not None, "Required property 'capacity' is missing"
        return typing.cast(MskconnectConnectorCapacity, result)

    @builtins.property
    def connector_configuration(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#connector_configuration MskconnectConnector#connector_configuration}.'''
        result = self._values.get("connector_configuration")
        assert result is not None, "Required property 'connector_configuration' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def kafka_cluster(self) -> "MskconnectConnectorKafkaCluster":
        '''kafka_cluster block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafka_cluster MskconnectConnector#kafka_cluster}
        '''
        result = self._values.get("kafka_cluster")
        assert result is not None, "Required property 'kafka_cluster' is missing"
        return typing.cast("MskconnectConnectorKafkaCluster", result)

    @builtins.property
    def kafka_cluster_client_authentication(
        self,
    ) -> "MskconnectConnectorKafkaClusterClientAuthentication":
        '''kafka_cluster_client_authentication block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafka_cluster_client_authentication MskconnectConnector#kafka_cluster_client_authentication}
        '''
        result = self._values.get("kafka_cluster_client_authentication")
        assert result is not None, "Required property 'kafka_cluster_client_authentication' is missing"
        return typing.cast("MskconnectConnectorKafkaClusterClientAuthentication", result)

    @builtins.property
    def kafka_cluster_encryption_in_transit(
        self,
    ) -> "MskconnectConnectorKafkaClusterEncryptionInTransit":
        '''kafka_cluster_encryption_in_transit block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafka_cluster_encryption_in_transit MskconnectConnector#kafka_cluster_encryption_in_transit}
        '''
        result = self._values.get("kafka_cluster_encryption_in_transit")
        assert result is not None, "Required property 'kafka_cluster_encryption_in_transit' is missing"
        return typing.cast("MskconnectConnectorKafkaClusterEncryptionInTransit", result)

    @builtins.property
    def kafkaconnect_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#kafkaconnect_version MskconnectConnector#kafkaconnect_version}.'''
        result = self._values.get("kafkaconnect_version")
        assert result is not None, "Required property 'kafkaconnect_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#name MskconnectConnector#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def plugin(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["MskconnectConnectorPlugin"]]:
        '''plugin block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#plugin MskconnectConnector#plugin}
        '''
        result = self._values.get("plugin")
        assert result is not None, "Required property 'plugin' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["MskconnectConnectorPlugin"]], result)

    @builtins.property
    def service_execution_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#service_execution_role_arn MskconnectConnector#service_execution_role_arn}.'''
        result = self._values.get("service_execution_role_arn")
        assert result is not None, "Required property 'service_execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#description MskconnectConnector#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#id MskconnectConnector#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_delivery(self) -> typing.Optional["MskconnectConnectorLogDelivery"]:
        '''log_delivery block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#log_delivery MskconnectConnector#log_delivery}
        '''
        result = self._values.get("log_delivery")
        return typing.cast(typing.Optional["MskconnectConnectorLogDelivery"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MskconnectConnectorTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#timeouts MskconnectConnector#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MskconnectConnectorTimeouts"], result)

    @builtins.property
    def worker_configuration(
        self,
    ) -> typing.Optional["MskconnectConnectorWorkerConfiguration"]:
        '''worker_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#worker_configuration MskconnectConnector#worker_configuration}
        '''
        result = self._values.get("worker_configuration")
        return typing.cast(typing.Optional["MskconnectConnectorWorkerConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorKafkaCluster",
    jsii_struct_bases=[],
    name_mapping={"apache_kafka_cluster": "apacheKafkaCluster"},
)
class MskconnectConnectorKafkaCluster:
    def __init__(
        self,
        *,
        apache_kafka_cluster: typing.Union["MskconnectConnectorKafkaClusterApacheKafkaCluster", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param apache_kafka_cluster: apache_kafka_cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#apache_kafka_cluster MskconnectConnector#apache_kafka_cluster}
        '''
        if isinstance(apache_kafka_cluster, dict):
            apache_kafka_cluster = MskconnectConnectorKafkaClusterApacheKafkaCluster(**apache_kafka_cluster)
        if __debug__:
            def stub(
                *,
                apache_kafka_cluster: typing.Union[MskconnectConnectorKafkaClusterApacheKafkaCluster, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument apache_kafka_cluster", value=apache_kafka_cluster, expected_type=type_hints["apache_kafka_cluster"])
        self._values: typing.Dict[str, typing.Any] = {
            "apache_kafka_cluster": apache_kafka_cluster,
        }

    @builtins.property
    def apache_kafka_cluster(
        self,
    ) -> "MskconnectConnectorKafkaClusterApacheKafkaCluster":
        '''apache_kafka_cluster block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#apache_kafka_cluster MskconnectConnector#apache_kafka_cluster}
        '''
        result = self._values.get("apache_kafka_cluster")
        assert result is not None, "Required property 'apache_kafka_cluster' is missing"
        return typing.cast("MskconnectConnectorKafkaClusterApacheKafkaCluster", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorKafkaCluster(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorKafkaClusterApacheKafkaCluster",
    jsii_struct_bases=[],
    name_mapping={"bootstrap_servers": "bootstrapServers", "vpc": "vpc"},
)
class MskconnectConnectorKafkaClusterApacheKafkaCluster:
    def __init__(
        self,
        *,
        bootstrap_servers: builtins.str,
        vpc: typing.Union["MskconnectConnectorKafkaClusterApacheKafkaClusterVpc", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param bootstrap_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#bootstrap_servers MskconnectConnector#bootstrap_servers}.
        :param vpc: vpc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#vpc MskconnectConnector#vpc}
        '''
        if isinstance(vpc, dict):
            vpc = MskconnectConnectorKafkaClusterApacheKafkaClusterVpc(**vpc)
        if __debug__:
            def stub(
                *,
                bootstrap_servers: builtins.str,
                vpc: typing.Union[MskconnectConnectorKafkaClusterApacheKafkaClusterVpc, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bootstrap_servers", value=bootstrap_servers, expected_type=type_hints["bootstrap_servers"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[str, typing.Any] = {
            "bootstrap_servers": bootstrap_servers,
            "vpc": vpc,
        }

    @builtins.property
    def bootstrap_servers(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#bootstrap_servers MskconnectConnector#bootstrap_servers}.'''
        result = self._values.get("bootstrap_servers")
        assert result is not None, "Required property 'bootstrap_servers' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc(self) -> "MskconnectConnectorKafkaClusterApacheKafkaClusterVpc":
        '''vpc block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#vpc MskconnectConnector#vpc}
        '''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast("MskconnectConnectorKafkaClusterApacheKafkaClusterVpc", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorKafkaClusterApacheKafkaCluster(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorKafkaClusterApacheKafkaClusterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorKafkaClusterApacheKafkaClusterOutputReference",
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

    @jsii.member(jsii_name="putVpc")
    def put_vpc(
        self,
        *,
        security_groups: typing.Sequence[builtins.str],
        subnets: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#security_groups MskconnectConnector#security_groups}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#subnets MskconnectConnector#subnets}.
        '''
        value = MskconnectConnectorKafkaClusterApacheKafkaClusterVpc(
            security_groups=security_groups, subnets=subnets
        )

        return typing.cast(None, jsii.invoke(self, "putVpc", [value]))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(
        self,
    ) -> "MskconnectConnectorKafkaClusterApacheKafkaClusterVpcOutputReference":
        return typing.cast("MskconnectConnectorKafkaClusterApacheKafkaClusterVpcOutputReference", jsii.get(self, "vpc"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapServersInput")
    def bootstrap_servers_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bootstrapServersInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcInput")
    def vpc_input(
        self,
    ) -> typing.Optional["MskconnectConnectorKafkaClusterApacheKafkaClusterVpc"]:
        return typing.cast(typing.Optional["MskconnectConnectorKafkaClusterApacheKafkaClusterVpc"], jsii.get(self, "vpcInput"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapServers")
    def bootstrap_servers(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bootstrapServers"))

    @bootstrap_servers.setter
    def bootstrap_servers(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootstrapServers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaCluster]:
        return typing.cast(typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaCluster], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaCluster],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaCluster],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorKafkaClusterApacheKafkaClusterVpc",
    jsii_struct_bases=[],
    name_mapping={"security_groups": "securityGroups", "subnets": "subnets"},
)
class MskconnectConnectorKafkaClusterApacheKafkaClusterVpc:
    def __init__(
        self,
        *,
        security_groups: typing.Sequence[builtins.str],
        subnets: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#security_groups MskconnectConnector#security_groups}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#subnets MskconnectConnector#subnets}.
        '''
        if __debug__:
            def stub(
                *,
                security_groups: typing.Sequence[builtins.str],
                subnets: typing.Sequence[builtins.str],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
        self._values: typing.Dict[str, typing.Any] = {
            "security_groups": security_groups,
            "subnets": subnets,
        }

    @builtins.property
    def security_groups(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#security_groups MskconnectConnector#security_groups}.'''
        result = self._values.get("security_groups")
        assert result is not None, "Required property 'security_groups' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#subnets MskconnectConnector#subnets}.'''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorKafkaClusterApacheKafkaClusterVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorKafkaClusterApacheKafkaClusterVpcOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorKafkaClusterApacheKafkaClusterVpcOutputReference",
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
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetsInput")
    def subnets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetsInput"))

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
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaClusterVpc]:
        return typing.cast(typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaClusterVpc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaClusterVpc],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaClusterVpc],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorKafkaClusterClientAuthentication",
    jsii_struct_bases=[],
    name_mapping={"authentication_type": "authenticationType"},
)
class MskconnectConnectorKafkaClusterClientAuthentication:
    def __init__(
        self,
        *,
        authentication_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#authentication_type MskconnectConnector#authentication_type}.
        '''
        if __debug__:
            def stub(
                *,
                authentication_type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if authentication_type is not None:
            self._values["authentication_type"] = authentication_type

    @builtins.property
    def authentication_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#authentication_type MskconnectConnector#authentication_type}.'''
        result = self._values.get("authentication_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorKafkaClusterClientAuthentication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorKafkaClusterClientAuthenticationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorKafkaClusterClientAuthenticationOutputReference",
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

    @jsii.member(jsii_name="resetAuthenticationType")
    def reset_authentication_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationType", []))

    @builtins.property
    @jsii.member(jsii_name="authenticationTypeInput")
    def authentication_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationType"))

    @authentication_type.setter
    def authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorKafkaClusterClientAuthentication]:
        return typing.cast(typing.Optional[MskconnectConnectorKafkaClusterClientAuthentication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorKafkaClusterClientAuthentication],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskconnectConnectorKafkaClusterClientAuthentication],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorKafkaClusterEncryptionInTransit",
    jsii_struct_bases=[],
    name_mapping={"encryption_type": "encryptionType"},
)
class MskconnectConnectorKafkaClusterEncryptionInTransit:
    def __init__(
        self,
        *,
        encryption_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#encryption_type MskconnectConnector#encryption_type}.
        '''
        if __debug__:
            def stub(*, encryption_type: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if encryption_type is not None:
            self._values["encryption_type"] = encryption_type

    @builtins.property
    def encryption_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#encryption_type MskconnectConnector#encryption_type}.'''
        result = self._values.get("encryption_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorKafkaClusterEncryptionInTransit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorKafkaClusterEncryptionInTransitOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorKafkaClusterEncryptionInTransitOutputReference",
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

    @jsii.member(jsii_name="resetEncryptionType")
    def reset_encryption_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionType", []))

    @builtins.property
    @jsii.member(jsii_name="encryptionTypeInput")
    def encryption_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionType")
    def encryption_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionType"))

    @encryption_type.setter
    def encryption_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorKafkaClusterEncryptionInTransit]:
        return typing.cast(typing.Optional[MskconnectConnectorKafkaClusterEncryptionInTransit], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorKafkaClusterEncryptionInTransit],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskconnectConnectorKafkaClusterEncryptionInTransit],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MskconnectConnectorKafkaClusterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorKafkaClusterOutputReference",
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

    @jsii.member(jsii_name="putApacheKafkaCluster")
    def put_apache_kafka_cluster(
        self,
        *,
        bootstrap_servers: builtins.str,
        vpc: typing.Union[MskconnectConnectorKafkaClusterApacheKafkaClusterVpc, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param bootstrap_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#bootstrap_servers MskconnectConnector#bootstrap_servers}.
        :param vpc: vpc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#vpc MskconnectConnector#vpc}
        '''
        value = MskconnectConnectorKafkaClusterApacheKafkaCluster(
            bootstrap_servers=bootstrap_servers, vpc=vpc
        )

        return typing.cast(None, jsii.invoke(self, "putApacheKafkaCluster", [value]))

    @builtins.property
    @jsii.member(jsii_name="apacheKafkaCluster")
    def apache_kafka_cluster(
        self,
    ) -> MskconnectConnectorKafkaClusterApacheKafkaClusterOutputReference:
        return typing.cast(MskconnectConnectorKafkaClusterApacheKafkaClusterOutputReference, jsii.get(self, "apacheKafkaCluster"))

    @builtins.property
    @jsii.member(jsii_name="apacheKafkaClusterInput")
    def apache_kafka_cluster_input(
        self,
    ) -> typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaCluster]:
        return typing.cast(typing.Optional[MskconnectConnectorKafkaClusterApacheKafkaCluster], jsii.get(self, "apacheKafkaClusterInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskconnectConnectorKafkaCluster]:
        return typing.cast(typing.Optional[MskconnectConnectorKafkaCluster], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorKafkaCluster],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[MskconnectConnectorKafkaCluster]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorLogDelivery",
    jsii_struct_bases=[],
    name_mapping={"worker_log_delivery": "workerLogDelivery"},
)
class MskconnectConnectorLogDelivery:
    def __init__(
        self,
        *,
        worker_log_delivery: typing.Union["MskconnectConnectorLogDeliveryWorkerLogDelivery", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param worker_log_delivery: worker_log_delivery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#worker_log_delivery MskconnectConnector#worker_log_delivery}
        '''
        if isinstance(worker_log_delivery, dict):
            worker_log_delivery = MskconnectConnectorLogDeliveryWorkerLogDelivery(**worker_log_delivery)
        if __debug__:
            def stub(
                *,
                worker_log_delivery: typing.Union[MskconnectConnectorLogDeliveryWorkerLogDelivery, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument worker_log_delivery", value=worker_log_delivery, expected_type=type_hints["worker_log_delivery"])
        self._values: typing.Dict[str, typing.Any] = {
            "worker_log_delivery": worker_log_delivery,
        }

    @builtins.property
    def worker_log_delivery(self) -> "MskconnectConnectorLogDeliveryWorkerLogDelivery":
        '''worker_log_delivery block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#worker_log_delivery MskconnectConnector#worker_log_delivery}
        '''
        result = self._values.get("worker_log_delivery")
        assert result is not None, "Required property 'worker_log_delivery' is missing"
        return typing.cast("MskconnectConnectorLogDeliveryWorkerLogDelivery", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorLogDelivery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorLogDeliveryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorLogDeliveryOutputReference",
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

    @jsii.member(jsii_name="putWorkerLogDelivery")
    def put_worker_log_delivery(
        self,
        *,
        cloudwatch_logs: typing.Optional[typing.Union["MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs", typing.Dict[str, typing.Any]]] = None,
        firehose: typing.Optional[typing.Union["MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose", typing.Dict[str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["MskconnectConnectorLogDeliveryWorkerLogDeliveryS3", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_logs: cloudwatch_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#cloudwatch_logs MskconnectConnector#cloudwatch_logs}
        :param firehose: firehose block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#firehose MskconnectConnector#firehose}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#s3 MskconnectConnector#s3}
        '''
        value = MskconnectConnectorLogDeliveryWorkerLogDelivery(
            cloudwatch_logs=cloudwatch_logs, firehose=firehose, s3=s3
        )

        return typing.cast(None, jsii.invoke(self, "putWorkerLogDelivery", [value]))

    @builtins.property
    @jsii.member(jsii_name="workerLogDelivery")
    def worker_log_delivery(
        self,
    ) -> "MskconnectConnectorLogDeliveryWorkerLogDeliveryOutputReference":
        return typing.cast("MskconnectConnectorLogDeliveryWorkerLogDeliveryOutputReference", jsii.get(self, "workerLogDelivery"))

    @builtins.property
    @jsii.member(jsii_name="workerLogDeliveryInput")
    def worker_log_delivery_input(
        self,
    ) -> typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDelivery"]:
        return typing.cast(typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDelivery"], jsii.get(self, "workerLogDeliveryInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MskconnectConnectorLogDelivery]:
        return typing.cast(typing.Optional[MskconnectConnectorLogDelivery], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorLogDelivery],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[MskconnectConnectorLogDelivery]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorLogDeliveryWorkerLogDelivery",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_logs": "cloudwatchLogs",
        "firehose": "firehose",
        "s3": "s3",
    },
)
class MskconnectConnectorLogDeliveryWorkerLogDelivery:
    def __init__(
        self,
        *,
        cloudwatch_logs: typing.Optional[typing.Union["MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs", typing.Dict[str, typing.Any]]] = None,
        firehose: typing.Optional[typing.Union["MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose", typing.Dict[str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["MskconnectConnectorLogDeliveryWorkerLogDeliveryS3", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_logs: cloudwatch_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#cloudwatch_logs MskconnectConnector#cloudwatch_logs}
        :param firehose: firehose block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#firehose MskconnectConnector#firehose}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#s3 MskconnectConnector#s3}
        '''
        if isinstance(cloudwatch_logs, dict):
            cloudwatch_logs = MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs(**cloudwatch_logs)
        if isinstance(firehose, dict):
            firehose = MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose(**firehose)
        if isinstance(s3, dict):
            s3 = MskconnectConnectorLogDeliveryWorkerLogDeliveryS3(**s3)
        if __debug__:
            def stub(
                *,
                cloudwatch_logs: typing.Optional[typing.Union[MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs, typing.Dict[str, typing.Any]]] = None,
                firehose: typing.Optional[typing.Union[MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose, typing.Dict[str, typing.Any]]] = None,
                s3: typing.Optional[typing.Union[MskconnectConnectorLogDeliveryWorkerLogDeliveryS3, typing.Dict[str, typing.Any]]] = None,
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
    ) -> typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs"]:
        '''cloudwatch_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#cloudwatch_logs MskconnectConnector#cloudwatch_logs}
        '''
        result = self._values.get("cloudwatch_logs")
        return typing.cast(typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs"], result)

    @builtins.property
    def firehose(
        self,
    ) -> typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose"]:
        '''firehose block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#firehose MskconnectConnector#firehose}
        '''
        result = self._values.get("firehose")
        return typing.cast(typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose"], result)

    @builtins.property
    def s3(
        self,
    ) -> typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDeliveryS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#s3 MskconnectConnector#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDeliveryS3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorLogDeliveryWorkerLogDelivery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "log_group": "logGroup"},
)
class MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        log_group: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#enabled MskconnectConnector#enabled}.
        :param log_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#log_group MskconnectConnector#log_group}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#enabled MskconnectConnector#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def log_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#log_group MskconnectConnector#log_group}.'''
        result = self._values.get("log_group")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogsOutputReference",
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
    ) -> typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs]:
        return typing.cast(typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "delivery_stream": "deliveryStream"},
)
class MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        delivery_stream: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#enabled MskconnectConnector#enabled}.
        :param delivery_stream: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#delivery_stream MskconnectConnector#delivery_stream}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#enabled MskconnectConnector#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def delivery_stream(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#delivery_stream MskconnectConnector#delivery_stream}.'''
        result = self._values.get("delivery_stream")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehoseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehoseOutputReference",
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
    ) -> typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose]:
        return typing.cast(typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MskconnectConnectorLogDeliveryWorkerLogDeliveryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorLogDeliveryWorkerLogDeliveryOutputReference",
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
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#enabled MskconnectConnector#enabled}.
        :param log_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#log_group MskconnectConnector#log_group}.
        '''
        value = MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs(
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
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#enabled MskconnectConnector#enabled}.
        :param delivery_stream: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#delivery_stream MskconnectConnector#delivery_stream}.
        '''
        value = MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose(
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
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#enabled MskconnectConnector#enabled}.
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#bucket MskconnectConnector#bucket}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#prefix MskconnectConnector#prefix}.
        '''
        value = MskconnectConnectorLogDeliveryWorkerLogDeliveryS3(
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
    ) -> MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogsOutputReference:
        return typing.cast(MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogsOutputReference, jsii.get(self, "cloudwatchLogs"))

    @builtins.property
    @jsii.member(jsii_name="firehose")
    def firehose(
        self,
    ) -> MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehoseOutputReference:
        return typing.cast(MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehoseOutputReference, jsii.get(self, "firehose"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "MskconnectConnectorLogDeliveryWorkerLogDeliveryS3OutputReference":
        return typing.cast("MskconnectConnectorLogDeliveryWorkerLogDeliveryS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogsInput")
    def cloudwatch_logs_input(
        self,
    ) -> typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs]:
        return typing.cast(typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs], jsii.get(self, "cloudwatchLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="firehoseInput")
    def firehose_input(
        self,
    ) -> typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose]:
        return typing.cast(typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose], jsii.get(self, "firehoseInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(
        self,
    ) -> typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDeliveryS3"]:
        return typing.cast(typing.Optional["MskconnectConnectorLogDeliveryWorkerLogDeliveryS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDelivery]:
        return typing.cast(typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDelivery], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDelivery],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDelivery],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorLogDeliveryWorkerLogDeliveryS3",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "bucket": "bucket", "prefix": "prefix"},
)
class MskconnectConnectorLogDeliveryWorkerLogDeliveryS3:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        bucket: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#enabled MskconnectConnector#enabled}.
        :param bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#bucket MskconnectConnector#bucket}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#prefix MskconnectConnector#prefix}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#enabled MskconnectConnector#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#bucket MskconnectConnector#bucket}.'''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#prefix MskconnectConnector#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorLogDeliveryWorkerLogDeliveryS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorLogDeliveryWorkerLogDeliveryS3OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorLogDeliveryWorkerLogDeliveryS3OutputReference",
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
    def internal_value(
        self,
    ) -> typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryS3]:
        return typing.cast(typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryS3],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskconnectConnectorLogDeliveryWorkerLogDeliveryS3],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorPlugin",
    jsii_struct_bases=[],
    name_mapping={"custom_plugin": "customPlugin"},
)
class MskconnectConnectorPlugin:
    def __init__(
        self,
        *,
        custom_plugin: typing.Union["MskconnectConnectorPluginCustomPlugin", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param custom_plugin: custom_plugin block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#custom_plugin MskconnectConnector#custom_plugin}
        '''
        if isinstance(custom_plugin, dict):
            custom_plugin = MskconnectConnectorPluginCustomPlugin(**custom_plugin)
        if __debug__:
            def stub(
                *,
                custom_plugin: typing.Union[MskconnectConnectorPluginCustomPlugin, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument custom_plugin", value=custom_plugin, expected_type=type_hints["custom_plugin"])
        self._values: typing.Dict[str, typing.Any] = {
            "custom_plugin": custom_plugin,
        }

    @builtins.property
    def custom_plugin(self) -> "MskconnectConnectorPluginCustomPlugin":
        '''custom_plugin block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#custom_plugin MskconnectConnector#custom_plugin}
        '''
        result = self._values.get("custom_plugin")
        assert result is not None, "Required property 'custom_plugin' is missing"
        return typing.cast("MskconnectConnectorPluginCustomPlugin", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorPlugin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorPluginCustomPlugin",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "revision": "revision"},
)
class MskconnectConnectorPluginCustomPlugin:
    def __init__(self, *, arn: builtins.str, revision: jsii.Number) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#arn MskconnectConnector#arn}.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#revision MskconnectConnector#revision}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#arn MskconnectConnector#arn}.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def revision(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#revision MskconnectConnector#revision}.'''
        result = self._values.get("revision")
        assert result is not None, "Required property 'revision' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorPluginCustomPlugin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorPluginCustomPluginOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorPluginCustomPluginOutputReference",
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
    def internal_value(self) -> typing.Optional[MskconnectConnectorPluginCustomPlugin]:
        return typing.cast(typing.Optional[MskconnectConnectorPluginCustomPlugin], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorPluginCustomPlugin],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskconnectConnectorPluginCustomPlugin],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MskconnectConnectorPluginList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorPluginList",
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
    def get(self, index: jsii.Number) -> "MskconnectConnectorPluginOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MskconnectConnectorPluginOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MskconnectConnectorPlugin]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MskconnectConnectorPlugin]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MskconnectConnectorPlugin]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MskconnectConnectorPlugin]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MskconnectConnectorPluginOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorPluginOutputReference",
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

    @jsii.member(jsii_name="putCustomPlugin")
    def put_custom_plugin(self, *, arn: builtins.str, revision: jsii.Number) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#arn MskconnectConnector#arn}.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#revision MskconnectConnector#revision}.
        '''
        value = MskconnectConnectorPluginCustomPlugin(arn=arn, revision=revision)

        return typing.cast(None, jsii.invoke(self, "putCustomPlugin", [value]))

    @builtins.property
    @jsii.member(jsii_name="customPlugin")
    def custom_plugin(self) -> MskconnectConnectorPluginCustomPluginOutputReference:
        return typing.cast(MskconnectConnectorPluginCustomPluginOutputReference, jsii.get(self, "customPlugin"))

    @builtins.property
    @jsii.member(jsii_name="customPluginInput")
    def custom_plugin_input(
        self,
    ) -> typing.Optional[MskconnectConnectorPluginCustomPlugin]:
        return typing.cast(typing.Optional[MskconnectConnectorPluginCustomPlugin], jsii.get(self, "customPluginInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MskconnectConnectorPlugin, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MskconnectConnectorPlugin, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MskconnectConnectorPlugin, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[MskconnectConnectorPlugin, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class MskconnectConnectorTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#create MskconnectConnector#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#delete MskconnectConnector#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#update MskconnectConnector#update}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#create MskconnectConnector#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#delete MskconnectConnector#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#update MskconnectConnector#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorTimeoutsOutputReference",
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
    ) -> typing.Optional[typing.Union[MskconnectConnectorTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MskconnectConnectorTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MskconnectConnectorTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[MskconnectConnectorTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorWorkerConfiguration",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "revision": "revision"},
)
class MskconnectConnectorWorkerConfiguration:
    def __init__(self, *, arn: builtins.str, revision: jsii.Number) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#arn MskconnectConnector#arn}.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#revision MskconnectConnector#revision}.
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#arn MskconnectConnector#arn}.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def revision(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mskconnect_connector#revision MskconnectConnector#revision}.'''
        result = self._values.get("revision")
        assert result is not None, "Required property 'revision' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MskconnectConnectorWorkerConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MskconnectConnectorWorkerConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.mskconnectConnector.MskconnectConnectorWorkerConfigurationOutputReference",
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
    def internal_value(self) -> typing.Optional[MskconnectConnectorWorkerConfiguration]:
        return typing.cast(typing.Optional[MskconnectConnectorWorkerConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MskconnectConnectorWorkerConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[MskconnectConnectorWorkerConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MskconnectConnector",
    "MskconnectConnectorCapacity",
    "MskconnectConnectorCapacityAutoscaling",
    "MskconnectConnectorCapacityAutoscalingOutputReference",
    "MskconnectConnectorCapacityAutoscalingScaleInPolicy",
    "MskconnectConnectorCapacityAutoscalingScaleInPolicyOutputReference",
    "MskconnectConnectorCapacityAutoscalingScaleOutPolicy",
    "MskconnectConnectorCapacityAutoscalingScaleOutPolicyOutputReference",
    "MskconnectConnectorCapacityOutputReference",
    "MskconnectConnectorCapacityProvisionedCapacity",
    "MskconnectConnectorCapacityProvisionedCapacityOutputReference",
    "MskconnectConnectorConfig",
    "MskconnectConnectorKafkaCluster",
    "MskconnectConnectorKafkaClusterApacheKafkaCluster",
    "MskconnectConnectorKafkaClusterApacheKafkaClusterOutputReference",
    "MskconnectConnectorKafkaClusterApacheKafkaClusterVpc",
    "MskconnectConnectorKafkaClusterApacheKafkaClusterVpcOutputReference",
    "MskconnectConnectorKafkaClusterClientAuthentication",
    "MskconnectConnectorKafkaClusterClientAuthenticationOutputReference",
    "MskconnectConnectorKafkaClusterEncryptionInTransit",
    "MskconnectConnectorKafkaClusterEncryptionInTransitOutputReference",
    "MskconnectConnectorKafkaClusterOutputReference",
    "MskconnectConnectorLogDelivery",
    "MskconnectConnectorLogDeliveryOutputReference",
    "MskconnectConnectorLogDeliveryWorkerLogDelivery",
    "MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogs",
    "MskconnectConnectorLogDeliveryWorkerLogDeliveryCloudwatchLogsOutputReference",
    "MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehose",
    "MskconnectConnectorLogDeliveryWorkerLogDeliveryFirehoseOutputReference",
    "MskconnectConnectorLogDeliveryWorkerLogDeliveryOutputReference",
    "MskconnectConnectorLogDeliveryWorkerLogDeliveryS3",
    "MskconnectConnectorLogDeliveryWorkerLogDeliveryS3OutputReference",
    "MskconnectConnectorPlugin",
    "MskconnectConnectorPluginCustomPlugin",
    "MskconnectConnectorPluginCustomPluginOutputReference",
    "MskconnectConnectorPluginList",
    "MskconnectConnectorPluginOutputReference",
    "MskconnectConnectorTimeouts",
    "MskconnectConnectorTimeoutsOutputReference",
    "MskconnectConnectorWorkerConfiguration",
    "MskconnectConnectorWorkerConfigurationOutputReference",
]

publication.publish()
