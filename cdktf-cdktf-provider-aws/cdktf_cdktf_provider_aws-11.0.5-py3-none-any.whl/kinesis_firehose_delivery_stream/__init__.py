'''
# `aws_kinesis_firehose_delivery_stream`

Refer to the Terraform Registory for docs: [`aws_kinesis_firehose_delivery_stream`](https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream).
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


class KinesisFirehoseDeliveryStream(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStream",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream aws_kinesis_firehose_delivery_stream}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        destination: builtins.str,
        name: builtins.str,
        arn: typing.Optional[builtins.str] = None,
        destination_id: typing.Optional[builtins.str] = None,
        elasticsearch_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfiguration", typing.Dict[str, typing.Any]]] = None,
        extended_s3_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3Configuration", typing.Dict[str, typing.Any]]] = None,
        http_endpoint_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfiguration", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        kinesis_source_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamKinesisSourceConfiguration", typing.Dict[str, typing.Any]]] = None,
        redshift_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfiguration", typing.Dict[str, typing.Any]]] = None,
        s3_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamS3Configuration", typing.Dict[str, typing.Any]]] = None,
        server_side_encryption: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamServerSideEncryption", typing.Dict[str, typing.Any]]] = None,
        splunk_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfiguration", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        version_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream aws_kinesis_firehose_delivery_stream} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#destination KinesisFirehoseDeliveryStream#destination}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#name KinesisFirehoseDeliveryStream#name}.
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#arn KinesisFirehoseDeliveryStream#arn}.
        :param destination_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#destination_id KinesisFirehoseDeliveryStream#destination_id}.
        :param elasticsearch_configuration: elasticsearch_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#elasticsearch_configuration KinesisFirehoseDeliveryStream#elasticsearch_configuration}
        :param extended_s3_configuration: extended_s3_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#extended_s3_configuration KinesisFirehoseDeliveryStream#extended_s3_configuration}
        :param http_endpoint_configuration: http_endpoint_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#http_endpoint_configuration KinesisFirehoseDeliveryStream#http_endpoint_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#id KinesisFirehoseDeliveryStream#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kinesis_source_configuration: kinesis_source_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kinesis_source_configuration KinesisFirehoseDeliveryStream#kinesis_source_configuration}
        :param redshift_configuration: redshift_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#redshift_configuration KinesisFirehoseDeliveryStream#redshift_configuration}
        :param s3_configuration: s3_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_configuration KinesisFirehoseDeliveryStream#s3_configuration}
        :param server_side_encryption: server_side_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#server_side_encryption KinesisFirehoseDeliveryStream#server_side_encryption}
        :param splunk_configuration: splunk_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#splunk_configuration KinesisFirehoseDeliveryStream#splunk_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#tags KinesisFirehoseDeliveryStream#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#tags_all KinesisFirehoseDeliveryStream#tags_all}.
        :param version_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#version_id KinesisFirehoseDeliveryStream#version_id}.
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
                destination: builtins.str,
                name: builtins.str,
                arn: typing.Optional[builtins.str] = None,
                destination_id: typing.Optional[builtins.str] = None,
                elasticsearch_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfiguration, typing.Dict[str, typing.Any]]] = None,
                extended_s3_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3Configuration, typing.Dict[str, typing.Any]]] = None,
                http_endpoint_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfiguration, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                kinesis_source_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamKinesisSourceConfiguration, typing.Dict[str, typing.Any]]] = None,
                redshift_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfiguration, typing.Dict[str, typing.Any]]] = None,
                s3_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamS3Configuration, typing.Dict[str, typing.Any]]] = None,
                server_side_encryption: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamServerSideEncryption, typing.Dict[str, typing.Any]]] = None,
                splunk_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfiguration, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                version_id: typing.Optional[builtins.str] = None,
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
        config = KinesisFirehoseDeliveryStreamConfig(
            destination=destination,
            name=name,
            arn=arn,
            destination_id=destination_id,
            elasticsearch_configuration=elasticsearch_configuration,
            extended_s3_configuration=extended_s3_configuration,
            http_endpoint_configuration=http_endpoint_configuration,
            id=id,
            kinesis_source_configuration=kinesis_source_configuration,
            redshift_configuration=redshift_configuration,
            s3_configuration=s3_configuration,
            server_side_encryption=server_side_encryption,
            splunk_configuration=splunk_configuration,
            tags=tags,
            tags_all=tags_all,
            version_id=version_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putElasticsearchConfiguration")
    def put_elasticsearch_configuration(
        self,
        *,
        index_name: builtins.str,
        role_arn: builtins.str,
        buffering_interval: typing.Optional[jsii.Number] = None,
        buffering_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions", typing.Dict[str, typing.Any]]] = None,
        cluster_endpoint: typing.Optional[builtins.str] = None,
        domain_arn: typing.Optional[builtins.str] = None,
        index_rotation_period: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration", typing.Dict[str, typing.Any]]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
        vpc_config: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param index_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#index_name KinesisFirehoseDeliveryStream#index_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffering_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_interval KinesisFirehoseDeliveryStream#buffering_interval}.
        :param buffering_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_size KinesisFirehoseDeliveryStream#buffering_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param cluster_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cluster_endpoint KinesisFirehoseDeliveryStream#cluster_endpoint}.
        :param domain_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#domain_arn KinesisFirehoseDeliveryStream#domain_arn}.
        :param index_rotation_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#index_rotation_period KinesisFirehoseDeliveryStream#index_rotation_period}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        :param type_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type_name KinesisFirehoseDeliveryStream#type_name}.
        :param vpc_config: vpc_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#vpc_config KinesisFirehoseDeliveryStream#vpc_config}
        '''
        value = KinesisFirehoseDeliveryStreamElasticsearchConfiguration(
            index_name=index_name,
            role_arn=role_arn,
            buffering_interval=buffering_interval,
            buffering_size=buffering_size,
            cloudwatch_logging_options=cloudwatch_logging_options,
            cluster_endpoint=cluster_endpoint,
            domain_arn=domain_arn,
            index_rotation_period=index_rotation_period,
            processing_configuration=processing_configuration,
            retry_duration=retry_duration,
            s3_backup_mode=s3_backup_mode,
            type_name=type_name,
            vpc_config=vpc_config,
        )

        return typing.cast(None, jsii.invoke(self, "putElasticsearchConfiguration", [value]))

    @jsii.member(jsii_name="putExtendedS3Configuration")
    def put_extended_s3_configuration(
        self,
        *,
        bucket_arn: builtins.str,
        role_arn: builtins.str,
        buffer_interval: typing.Optional[jsii.Number] = None,
        buffer_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions", typing.Dict[str, typing.Any]]] = None,
        compression_format: typing.Optional[builtins.str] = None,
        data_format_conversion_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration", typing.Dict[str, typing.Any]]] = None,
        dynamic_partitioning_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration", typing.Dict[str, typing.Any]]] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration", typing.Dict[str, typing.Any]]] = None,
        s3_backup_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration", typing.Dict[str, typing.Any]]] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffer_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.
        :param buffer_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param compression_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.
        :param data_format_conversion_configuration: data_format_conversion_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#data_format_conversion_configuration KinesisFirehoseDeliveryStream#data_format_conversion_configuration}
        :param dynamic_partitioning_configuration: dynamic_partitioning_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#dynamic_partitioning_configuration KinesisFirehoseDeliveryStream#dynamic_partitioning_configuration}
        :param error_output_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param s3_backup_configuration: s3_backup_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_configuration KinesisFirehoseDeliveryStream#s3_backup_configuration}
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3Configuration(
            bucket_arn=bucket_arn,
            role_arn=role_arn,
            buffer_interval=buffer_interval,
            buffer_size=buffer_size,
            cloudwatch_logging_options=cloudwatch_logging_options,
            compression_format=compression_format,
            data_format_conversion_configuration=data_format_conversion_configuration,
            dynamic_partitioning_configuration=dynamic_partitioning_configuration,
            error_output_prefix=error_output_prefix,
            kms_key_arn=kms_key_arn,
            prefix=prefix,
            processing_configuration=processing_configuration,
            s3_backup_configuration=s3_backup_configuration,
            s3_backup_mode=s3_backup_mode,
        )

        return typing.cast(None, jsii.invoke(self, "putExtendedS3Configuration", [value]))

    @jsii.member(jsii_name="putHttpEndpointConfiguration")
    def put_http_endpoint_configuration(
        self,
        *,
        url: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        buffering_interval: typing.Optional[jsii.Number] = None,
        buffering_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions", typing.Dict[str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration", typing.Dict[str, typing.Any]]] = None,
        request_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration", typing.Dict[str, typing.Any]]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
        role_arn: typing.Optional[builtins.str] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#url KinesisFirehoseDeliveryStream#url}.
        :param access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#access_key KinesisFirehoseDeliveryStream#access_key}.
        :param buffering_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_interval KinesisFirehoseDeliveryStream#buffering_interval}.
        :param buffering_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_size KinesisFirehoseDeliveryStream#buffering_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#name KinesisFirehoseDeliveryStream#name}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param request_configuration: request_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#request_configuration KinesisFirehoseDeliveryStream#request_configuration}
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        '''
        value = KinesisFirehoseDeliveryStreamHttpEndpointConfiguration(
            url=url,
            access_key=access_key,
            buffering_interval=buffering_interval,
            buffering_size=buffering_size,
            cloudwatch_logging_options=cloudwatch_logging_options,
            name=name,
            processing_configuration=processing_configuration,
            request_configuration=request_configuration,
            retry_duration=retry_duration,
            role_arn=role_arn,
            s3_backup_mode=s3_backup_mode,
        )

        return typing.cast(None, jsii.invoke(self, "putHttpEndpointConfiguration", [value]))

    @jsii.member(jsii_name="putKinesisSourceConfiguration")
    def put_kinesis_source_configuration(
        self,
        *,
        kinesis_stream_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param kinesis_stream_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kinesis_stream_arn KinesisFirehoseDeliveryStream#kinesis_stream_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        '''
        value = KinesisFirehoseDeliveryStreamKinesisSourceConfiguration(
            kinesis_stream_arn=kinesis_stream_arn, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisSourceConfiguration", [value]))

    @jsii.member(jsii_name="putRedshiftConfiguration")
    def put_redshift_configuration(
        self,
        *,
        cluster_jdbcurl: builtins.str,
        data_table_name: builtins.str,
        password: builtins.str,
        role_arn: builtins.str,
        username: builtins.str,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions", typing.Dict[str, typing.Any]]] = None,
        copy_options: typing.Optional[builtins.str] = None,
        data_table_columns: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration", typing.Dict[str, typing.Any]]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
        s3_backup_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration", typing.Dict[str, typing.Any]]] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cluster_jdbcurl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cluster_jdbcurl KinesisFirehoseDeliveryStream#cluster_jdbcurl}.
        :param data_table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#data_table_name KinesisFirehoseDeliveryStream#data_table_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#password KinesisFirehoseDeliveryStream#password}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#username KinesisFirehoseDeliveryStream#username}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param copy_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#copy_options KinesisFirehoseDeliveryStream#copy_options}.
        :param data_table_columns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#data_table_columns KinesisFirehoseDeliveryStream#data_table_columns}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        :param s3_backup_configuration: s3_backup_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_configuration KinesisFirehoseDeliveryStream#s3_backup_configuration}
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        '''
        value = KinesisFirehoseDeliveryStreamRedshiftConfiguration(
            cluster_jdbcurl=cluster_jdbcurl,
            data_table_name=data_table_name,
            password=password,
            role_arn=role_arn,
            username=username,
            cloudwatch_logging_options=cloudwatch_logging_options,
            copy_options=copy_options,
            data_table_columns=data_table_columns,
            processing_configuration=processing_configuration,
            retry_duration=retry_duration,
            s3_backup_configuration=s3_backup_configuration,
            s3_backup_mode=s3_backup_mode,
        )

        return typing.cast(None, jsii.invoke(self, "putRedshiftConfiguration", [value]))

    @jsii.member(jsii_name="putS3Configuration")
    def put_s3_configuration(
        self,
        *,
        bucket_arn: builtins.str,
        role_arn: builtins.str,
        buffer_interval: typing.Optional[jsii.Number] = None,
        buffer_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions", typing.Dict[str, typing.Any]]] = None,
        compression_format: typing.Optional[builtins.str] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffer_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.
        :param buffer_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param compression_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.
        :param error_output_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.
        '''
        value = KinesisFirehoseDeliveryStreamS3Configuration(
            bucket_arn=bucket_arn,
            role_arn=role_arn,
            buffer_interval=buffer_interval,
            buffer_size=buffer_size,
            cloudwatch_logging_options=cloudwatch_logging_options,
            compression_format=compression_format,
            error_output_prefix=error_output_prefix,
            kms_key_arn=kms_key_arn,
            prefix=prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putS3Configuration", [value]))

    @jsii.member(jsii_name="putServerSideEncryption")
    def put_server_side_encryption(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key_arn: typing.Optional[builtins.str] = None,
        key_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#key_arn KinesisFirehoseDeliveryStream#key_arn}.
        :param key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#key_type KinesisFirehoseDeliveryStream#key_type}.
        '''
        value = KinesisFirehoseDeliveryStreamServerSideEncryption(
            enabled=enabled, key_arn=key_arn, key_type=key_type
        )

        return typing.cast(None, jsii.invoke(self, "putServerSideEncryption", [value]))

    @jsii.member(jsii_name="putSplunkConfiguration")
    def put_splunk_configuration(
        self,
        *,
        hec_endpoint: builtins.str,
        hec_token: builtins.str,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions", typing.Dict[str, typing.Any]]] = None,
        hec_acknowledgment_timeout: typing.Optional[jsii.Number] = None,
        hec_endpoint_type: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration", typing.Dict[str, typing.Any]]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hec_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_endpoint KinesisFirehoseDeliveryStream#hec_endpoint}.
        :param hec_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_token KinesisFirehoseDeliveryStream#hec_token}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param hec_acknowledgment_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_acknowledgment_timeout KinesisFirehoseDeliveryStream#hec_acknowledgment_timeout}.
        :param hec_endpoint_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_endpoint_type KinesisFirehoseDeliveryStream#hec_endpoint_type}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        '''
        value = KinesisFirehoseDeliveryStreamSplunkConfiguration(
            hec_endpoint=hec_endpoint,
            hec_token=hec_token,
            cloudwatch_logging_options=cloudwatch_logging_options,
            hec_acknowledgment_timeout=hec_acknowledgment_timeout,
            hec_endpoint_type=hec_endpoint_type,
            processing_configuration=processing_configuration,
            retry_duration=retry_duration,
            s3_backup_mode=s3_backup_mode,
        )

        return typing.cast(None, jsii.invoke(self, "putSplunkConfiguration", [value]))

    @jsii.member(jsii_name="resetArn")
    def reset_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArn", []))

    @jsii.member(jsii_name="resetDestinationId")
    def reset_destination_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationId", []))

    @jsii.member(jsii_name="resetElasticsearchConfiguration")
    def reset_elasticsearch_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticsearchConfiguration", []))

    @jsii.member(jsii_name="resetExtendedS3Configuration")
    def reset_extended_s3_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtendedS3Configuration", []))

    @jsii.member(jsii_name="resetHttpEndpointConfiguration")
    def reset_http_endpoint_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpEndpointConfiguration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKinesisSourceConfiguration")
    def reset_kinesis_source_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisSourceConfiguration", []))

    @jsii.member(jsii_name="resetRedshiftConfiguration")
    def reset_redshift_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedshiftConfiguration", []))

    @jsii.member(jsii_name="resetS3Configuration")
    def reset_s3_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Configuration", []))

    @jsii.member(jsii_name="resetServerSideEncryption")
    def reset_server_side_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerSideEncryption", []))

    @jsii.member(jsii_name="resetSplunkConfiguration")
    def reset_splunk_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSplunkConfiguration", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetVersionId")
    def reset_version_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersionId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchConfiguration")
    def elasticsearch_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamElasticsearchConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamElasticsearchConfigurationOutputReference", jsii.get(self, "elasticsearchConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="extendedS3Configuration")
    def extended_s3_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationOutputReference", jsii.get(self, "extendedS3Configuration"))

    @builtins.property
    @jsii.member(jsii_name="httpEndpointConfiguration")
    def http_endpoint_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamHttpEndpointConfigurationOutputReference", jsii.get(self, "httpEndpointConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="kinesisSourceConfiguration")
    def kinesis_source_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamKinesisSourceConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamKinesisSourceConfigurationOutputReference", jsii.get(self, "kinesisSourceConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="redshiftConfiguration")
    def redshift_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamRedshiftConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamRedshiftConfigurationOutputReference", jsii.get(self, "redshiftConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="s3Configuration")
    def s3_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamS3ConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamS3ConfigurationOutputReference", jsii.get(self, "s3Configuration"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryption")
    def server_side_encryption(
        self,
    ) -> "KinesisFirehoseDeliveryStreamServerSideEncryptionOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamServerSideEncryptionOutputReference", jsii.get(self, "serverSideEncryption"))

    @builtins.property
    @jsii.member(jsii_name="splunkConfiguration")
    def splunk_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamSplunkConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamSplunkConfigurationOutputReference", jsii.get(self, "splunkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationIdInput")
    def destination_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchConfigurationInput")
    def elasticsearch_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfiguration"], jsii.get(self, "elasticsearchConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="extendedS3ConfigurationInput")
    def extended_s3_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3Configuration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3Configuration"], jsii.get(self, "extendedS3ConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="httpEndpointConfigurationInput")
    def http_endpoint_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfiguration"], jsii.get(self, "httpEndpointConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisSourceConfigurationInput")
    def kinesis_source_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamKinesisSourceConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamKinesisSourceConfiguration"], jsii.get(self, "kinesisSourceConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftConfigurationInput")
    def redshift_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfiguration"], jsii.get(self, "redshiftConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="s3ConfigurationInput")
    def s3_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamS3Configuration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamS3Configuration"], jsii.get(self, "s3ConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionInput")
    def server_side_encryption_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamServerSideEncryption"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamServerSideEncryption"], jsii.get(self, "serverSideEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="splunkConfigurationInput")
    def splunk_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfiguration"], jsii.get(self, "splunkConfigurationInput"))

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
    @jsii.member(jsii_name="versionIdInput")
    def version_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionIdInput"))

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
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="destinationId")
    def destination_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationId"))

    @destination_id.setter
    def destination_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationId", value)

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
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionId"))

    @version_id.setter
    def version_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "destination": "destination",
        "name": "name",
        "arn": "arn",
        "destination_id": "destinationId",
        "elasticsearch_configuration": "elasticsearchConfiguration",
        "extended_s3_configuration": "extendedS3Configuration",
        "http_endpoint_configuration": "httpEndpointConfiguration",
        "id": "id",
        "kinesis_source_configuration": "kinesisSourceConfiguration",
        "redshift_configuration": "redshiftConfiguration",
        "s3_configuration": "s3Configuration",
        "server_side_encryption": "serverSideEncryption",
        "splunk_configuration": "splunkConfiguration",
        "tags": "tags",
        "tags_all": "tagsAll",
        "version_id": "versionId",
    },
)
class KinesisFirehoseDeliveryStreamConfig(cdktf.TerraformMetaArguments):
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
        destination: builtins.str,
        name: builtins.str,
        arn: typing.Optional[builtins.str] = None,
        destination_id: typing.Optional[builtins.str] = None,
        elasticsearch_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfiguration", typing.Dict[str, typing.Any]]] = None,
        extended_s3_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3Configuration", typing.Dict[str, typing.Any]]] = None,
        http_endpoint_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfiguration", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        kinesis_source_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamKinesisSourceConfiguration", typing.Dict[str, typing.Any]]] = None,
        redshift_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfiguration", typing.Dict[str, typing.Any]]] = None,
        s3_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamS3Configuration", typing.Dict[str, typing.Any]]] = None,
        server_side_encryption: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamServerSideEncryption", typing.Dict[str, typing.Any]]] = None,
        splunk_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfiguration", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#destination KinesisFirehoseDeliveryStream#destination}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#name KinesisFirehoseDeliveryStream#name}.
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#arn KinesisFirehoseDeliveryStream#arn}.
        :param destination_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#destination_id KinesisFirehoseDeliveryStream#destination_id}.
        :param elasticsearch_configuration: elasticsearch_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#elasticsearch_configuration KinesisFirehoseDeliveryStream#elasticsearch_configuration}
        :param extended_s3_configuration: extended_s3_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#extended_s3_configuration KinesisFirehoseDeliveryStream#extended_s3_configuration}
        :param http_endpoint_configuration: http_endpoint_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#http_endpoint_configuration KinesisFirehoseDeliveryStream#http_endpoint_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#id KinesisFirehoseDeliveryStream#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kinesis_source_configuration: kinesis_source_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kinesis_source_configuration KinesisFirehoseDeliveryStream#kinesis_source_configuration}
        :param redshift_configuration: redshift_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#redshift_configuration KinesisFirehoseDeliveryStream#redshift_configuration}
        :param s3_configuration: s3_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_configuration KinesisFirehoseDeliveryStream#s3_configuration}
        :param server_side_encryption: server_side_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#server_side_encryption KinesisFirehoseDeliveryStream#server_side_encryption}
        :param splunk_configuration: splunk_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#splunk_configuration KinesisFirehoseDeliveryStream#splunk_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#tags KinesisFirehoseDeliveryStream#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#tags_all KinesisFirehoseDeliveryStream#tags_all}.
        :param version_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#version_id KinesisFirehoseDeliveryStream#version_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(elasticsearch_configuration, dict):
            elasticsearch_configuration = KinesisFirehoseDeliveryStreamElasticsearchConfiguration(**elasticsearch_configuration)
        if isinstance(extended_s3_configuration, dict):
            extended_s3_configuration = KinesisFirehoseDeliveryStreamExtendedS3Configuration(**extended_s3_configuration)
        if isinstance(http_endpoint_configuration, dict):
            http_endpoint_configuration = KinesisFirehoseDeliveryStreamHttpEndpointConfiguration(**http_endpoint_configuration)
        if isinstance(kinesis_source_configuration, dict):
            kinesis_source_configuration = KinesisFirehoseDeliveryStreamKinesisSourceConfiguration(**kinesis_source_configuration)
        if isinstance(redshift_configuration, dict):
            redshift_configuration = KinesisFirehoseDeliveryStreamRedshiftConfiguration(**redshift_configuration)
        if isinstance(s3_configuration, dict):
            s3_configuration = KinesisFirehoseDeliveryStreamS3Configuration(**s3_configuration)
        if isinstance(server_side_encryption, dict):
            server_side_encryption = KinesisFirehoseDeliveryStreamServerSideEncryption(**server_side_encryption)
        if isinstance(splunk_configuration, dict):
            splunk_configuration = KinesisFirehoseDeliveryStreamSplunkConfiguration(**splunk_configuration)
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
                destination: builtins.str,
                name: builtins.str,
                arn: typing.Optional[builtins.str] = None,
                destination_id: typing.Optional[builtins.str] = None,
                elasticsearch_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfiguration, typing.Dict[str, typing.Any]]] = None,
                extended_s3_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3Configuration, typing.Dict[str, typing.Any]]] = None,
                http_endpoint_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfiguration, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                kinesis_source_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamKinesisSourceConfiguration, typing.Dict[str, typing.Any]]] = None,
                redshift_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfiguration, typing.Dict[str, typing.Any]]] = None,
                s3_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamS3Configuration, typing.Dict[str, typing.Any]]] = None,
                server_side_encryption: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamServerSideEncryption, typing.Dict[str, typing.Any]]] = None,
                splunk_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfiguration, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                version_id: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument destination_id", value=destination_id, expected_type=type_hints["destination_id"])
            check_type(argname="argument elasticsearch_configuration", value=elasticsearch_configuration, expected_type=type_hints["elasticsearch_configuration"])
            check_type(argname="argument extended_s3_configuration", value=extended_s3_configuration, expected_type=type_hints["extended_s3_configuration"])
            check_type(argname="argument http_endpoint_configuration", value=http_endpoint_configuration, expected_type=type_hints["http_endpoint_configuration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kinesis_source_configuration", value=kinesis_source_configuration, expected_type=type_hints["kinesis_source_configuration"])
            check_type(argname="argument redshift_configuration", value=redshift_configuration, expected_type=type_hints["redshift_configuration"])
            check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
            check_type(argname="argument server_side_encryption", value=server_side_encryption, expected_type=type_hints["server_side_encryption"])
            check_type(argname="argument splunk_configuration", value=splunk_configuration, expected_type=type_hints["splunk_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument version_id", value=version_id, expected_type=type_hints["version_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
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
        if arn is not None:
            self._values["arn"] = arn
        if destination_id is not None:
            self._values["destination_id"] = destination_id
        if elasticsearch_configuration is not None:
            self._values["elasticsearch_configuration"] = elasticsearch_configuration
        if extended_s3_configuration is not None:
            self._values["extended_s3_configuration"] = extended_s3_configuration
        if http_endpoint_configuration is not None:
            self._values["http_endpoint_configuration"] = http_endpoint_configuration
        if id is not None:
            self._values["id"] = id
        if kinesis_source_configuration is not None:
            self._values["kinesis_source_configuration"] = kinesis_source_configuration
        if redshift_configuration is not None:
            self._values["redshift_configuration"] = redshift_configuration
        if s3_configuration is not None:
            self._values["s3_configuration"] = s3_configuration
        if server_side_encryption is not None:
            self._values["server_side_encryption"] = server_side_encryption
        if splunk_configuration is not None:
            self._values["splunk_configuration"] = splunk_configuration
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if version_id is not None:
            self._values["version_id"] = version_id

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
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#destination KinesisFirehoseDeliveryStream#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#name KinesisFirehoseDeliveryStream#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#arn KinesisFirehoseDeliveryStream#arn}.'''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#destination_id KinesisFirehoseDeliveryStream#destination_id}.'''
        result = self._values.get("destination_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elasticsearch_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfiguration"]:
        '''elasticsearch_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#elasticsearch_configuration KinesisFirehoseDeliveryStream#elasticsearch_configuration}
        '''
        result = self._values.get("elasticsearch_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfiguration"], result)

    @builtins.property
    def extended_s3_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3Configuration"]:
        '''extended_s3_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#extended_s3_configuration KinesisFirehoseDeliveryStream#extended_s3_configuration}
        '''
        result = self._values.get("extended_s3_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3Configuration"], result)

    @builtins.property
    def http_endpoint_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfiguration"]:
        '''http_endpoint_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#http_endpoint_configuration KinesisFirehoseDeliveryStream#http_endpoint_configuration}
        '''
        result = self._values.get("http_endpoint_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfiguration"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#id KinesisFirehoseDeliveryStream#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kinesis_source_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamKinesisSourceConfiguration"]:
        '''kinesis_source_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kinesis_source_configuration KinesisFirehoseDeliveryStream#kinesis_source_configuration}
        '''
        result = self._values.get("kinesis_source_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamKinesisSourceConfiguration"], result)

    @builtins.property
    def redshift_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfiguration"]:
        '''redshift_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#redshift_configuration KinesisFirehoseDeliveryStream#redshift_configuration}
        '''
        result = self._values.get("redshift_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfiguration"], result)

    @builtins.property
    def s3_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamS3Configuration"]:
        '''s3_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_configuration KinesisFirehoseDeliveryStream#s3_configuration}
        '''
        result = self._values.get("s3_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamS3Configuration"], result)

    @builtins.property
    def server_side_encryption(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamServerSideEncryption"]:
        '''server_side_encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#server_side_encryption KinesisFirehoseDeliveryStream#server_side_encryption}
        '''
        result = self._values.get("server_side_encryption")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamServerSideEncryption"], result)

    @builtins.property
    def splunk_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfiguration"]:
        '''splunk_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#splunk_configuration KinesisFirehoseDeliveryStream#splunk_configuration}
        '''
        result = self._values.get("splunk_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfiguration"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#tags KinesisFirehoseDeliveryStream#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#tags_all KinesisFirehoseDeliveryStream#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def version_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#version_id KinesisFirehoseDeliveryStream#version_id}.'''
        result = self._values.get("version_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "index_name": "indexName",
        "role_arn": "roleArn",
        "buffering_interval": "bufferingInterval",
        "buffering_size": "bufferingSize",
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "cluster_endpoint": "clusterEndpoint",
        "domain_arn": "domainArn",
        "index_rotation_period": "indexRotationPeriod",
        "processing_configuration": "processingConfiguration",
        "retry_duration": "retryDuration",
        "s3_backup_mode": "s3BackupMode",
        "type_name": "typeName",
        "vpc_config": "vpcConfig",
    },
)
class KinesisFirehoseDeliveryStreamElasticsearchConfiguration:
    def __init__(
        self,
        *,
        index_name: builtins.str,
        role_arn: builtins.str,
        buffering_interval: typing.Optional[jsii.Number] = None,
        buffering_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions", typing.Dict[str, typing.Any]]] = None,
        cluster_endpoint: typing.Optional[builtins.str] = None,
        domain_arn: typing.Optional[builtins.str] = None,
        index_rotation_period: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration", typing.Dict[str, typing.Any]]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
        vpc_config: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param index_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#index_name KinesisFirehoseDeliveryStream#index_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffering_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_interval KinesisFirehoseDeliveryStream#buffering_interval}.
        :param buffering_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_size KinesisFirehoseDeliveryStream#buffering_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param cluster_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cluster_endpoint KinesisFirehoseDeliveryStream#cluster_endpoint}.
        :param domain_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#domain_arn KinesisFirehoseDeliveryStream#domain_arn}.
        :param index_rotation_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#index_rotation_period KinesisFirehoseDeliveryStream#index_rotation_period}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        :param type_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type_name KinesisFirehoseDeliveryStream#type_name}.
        :param vpc_config: vpc_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#vpc_config KinesisFirehoseDeliveryStream#vpc_config}
        '''
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if isinstance(processing_configuration, dict):
            processing_configuration = KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration(**processing_configuration)
        if isinstance(vpc_config, dict):
            vpc_config = KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig(**vpc_config)
        if __debug__:
            def stub(
                *,
                index_name: builtins.str,
                role_arn: builtins.str,
                buffering_interval: typing.Optional[jsii.Number] = None,
                buffering_size: typing.Optional[jsii.Number] = None,
                cloudwatch_logging_options: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions, typing.Dict[str, typing.Any]]] = None,
                cluster_endpoint: typing.Optional[builtins.str] = None,
                domain_arn: typing.Optional[builtins.str] = None,
                index_rotation_period: typing.Optional[builtins.str] = None,
                processing_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration, typing.Dict[str, typing.Any]]] = None,
                retry_duration: typing.Optional[jsii.Number] = None,
                s3_backup_mode: typing.Optional[builtins.str] = None,
                type_name: typing.Optional[builtins.str] = None,
                vpc_config: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument buffering_interval", value=buffering_interval, expected_type=type_hints["buffering_interval"])
            check_type(argname="argument buffering_size", value=buffering_size, expected_type=type_hints["buffering_size"])
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument cluster_endpoint", value=cluster_endpoint, expected_type=type_hints["cluster_endpoint"])
            check_type(argname="argument domain_arn", value=domain_arn, expected_type=type_hints["domain_arn"])
            check_type(argname="argument index_rotation_period", value=index_rotation_period, expected_type=type_hints["index_rotation_period"])
            check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
            check_type(argname="argument retry_duration", value=retry_duration, expected_type=type_hints["retry_duration"])
            check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "index_name": index_name,
            "role_arn": role_arn,
        }
        if buffering_interval is not None:
            self._values["buffering_interval"] = buffering_interval
        if buffering_size is not None:
            self._values["buffering_size"] = buffering_size
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if cluster_endpoint is not None:
            self._values["cluster_endpoint"] = cluster_endpoint
        if domain_arn is not None:
            self._values["domain_arn"] = domain_arn
        if index_rotation_period is not None:
            self._values["index_rotation_period"] = index_rotation_period
        if processing_configuration is not None:
            self._values["processing_configuration"] = processing_configuration
        if retry_duration is not None:
            self._values["retry_duration"] = retry_duration
        if s3_backup_mode is not None:
            self._values["s3_backup_mode"] = s3_backup_mode
        if type_name is not None:
            self._values["type_name"] = type_name
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

    @builtins.property
    def index_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#index_name KinesisFirehoseDeliveryStream#index_name}.'''
        result = self._values.get("index_name")
        assert result is not None, "Required property 'index_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def buffering_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_interval KinesisFirehoseDeliveryStream#buffering_interval}.'''
        result = self._values.get("buffering_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def buffering_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_size KinesisFirehoseDeliveryStream#buffering_size}.'''
        result = self._values.get("buffering_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions"]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions"], result)

    @builtins.property
    def cluster_endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cluster_endpoint KinesisFirehoseDeliveryStream#cluster_endpoint}.'''
        result = self._values.get("cluster_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#domain_arn KinesisFirehoseDeliveryStream#domain_arn}.'''
        result = self._values.get("domain_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def index_rotation_period(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#index_rotation_period KinesisFirehoseDeliveryStream#index_rotation_period}.'''
        result = self._values.get("index_rotation_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def processing_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration"]:
        '''processing_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        '''
        result = self._values.get("processing_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration"], result)

    @builtins.property
    def retry_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.'''
        result = self._values.get("retry_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def s3_backup_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.'''
        result = self._values.get("s3_backup_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type_name KinesisFirehoseDeliveryStream#type_name}.'''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_config(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig"]:
        '''vpc_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#vpc_config KinesisFirehoseDeliveryStream#vpc_config}
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamElasticsearchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                log_group_name: typing.Optional[builtins.str] = None,
                log_stream_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.'''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.'''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsOutputReference",
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

    @jsii.member(jsii_name="resetLogGroupName")
    def reset_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupName", []))

    @jsii.member(jsii_name="resetLogStreamName")
    def reset_log_stream_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreamName", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamNameInput")
    def log_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamNameInput"))

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
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))

    @log_stream_name.setter
    def log_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamElasticsearchConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationOutputReference",
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

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        value = KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions(
            enabled=enabled,
            log_group_name=log_group_name,
            log_stream_name=log_stream_name,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="putProcessingConfiguration")
    def put_processing_configuration(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        processors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        value = KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration(
            enabled=enabled, processors=processors
        )

        return typing.cast(None, jsii.invoke(self, "putProcessingConfiguration", [value]))

    @jsii.member(jsii_name="putVpcConfig")
    def put_vpc_config(
        self,
        *,
        role_arn: builtins.str,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#security_group_ids KinesisFirehoseDeliveryStream#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#subnet_ids KinesisFirehoseDeliveryStream#subnet_ids}.
        '''
        value = KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig(
            role_arn=role_arn,
            security_group_ids=security_group_ids,
            subnet_ids=subnet_ids,
        )

        return typing.cast(None, jsii.invoke(self, "putVpcConfig", [value]))

    @jsii.member(jsii_name="resetBufferingInterval")
    def reset_buffering_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferingInterval", []))

    @jsii.member(jsii_name="resetBufferingSize")
    def reset_buffering_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferingSize", []))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetClusterEndpoint")
    def reset_cluster_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterEndpoint", []))

    @jsii.member(jsii_name="resetDomainArn")
    def reset_domain_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomainArn", []))

    @jsii.member(jsii_name="resetIndexRotationPeriod")
    def reset_index_rotation_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIndexRotationPeriod", []))

    @jsii.member(jsii_name="resetProcessingConfiguration")
    def reset_processing_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessingConfiguration", []))

    @jsii.member(jsii_name="resetRetryDuration")
    def reset_retry_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryDuration", []))

    @jsii.member(jsii_name="resetS3BackupMode")
    def reset_s3_backup_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BackupMode", []))

    @jsii.member(jsii_name="resetTypeName")
    def reset_type_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypeName", []))

    @jsii.member(jsii_name="resetVpcConfig")
    def reset_vpc_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcConfig", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsOutputReference, jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationOutputReference", jsii.get(self, "processingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(
        self,
    ) -> "KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfigOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfigOutputReference", jsii.get(self, "vpcConfig"))

    @builtins.property
    @jsii.member(jsii_name="bufferingIntervalInput")
    def buffering_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferingSizeInput")
    def buffering_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferingSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterEndpointInput")
    def cluster_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="domainArnInput")
    def domain_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainArnInput"))

    @builtins.property
    @jsii.member(jsii_name="indexNameInput")
    def index_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "indexNameInput"))

    @builtins.property
    @jsii.member(jsii_name="indexRotationPeriodInput")
    def index_rotation_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "indexRotationPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="processingConfigurationInput")
    def processing_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration"], jsii.get(self, "processingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="retryDurationInput")
    def retry_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BackupModeInput")
    def s3_backup_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BackupModeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeNameInput")
    def type_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcConfigInput")
    def vpc_config_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig"], jsii.get(self, "vpcConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferingInterval")
    def buffering_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferingInterval"))

    @buffering_interval.setter
    def buffering_interval(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="bufferingSize")
    def buffering_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferingSize"))

    @buffering_size.setter
    def buffering_size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferingSize", value)

    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterEndpoint"))

    @cluster_endpoint.setter
    def cluster_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="domainArn")
    def domain_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainArn"))

    @domain_arn.setter
    def domain_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainArn", value)

    @builtins.property
    @jsii.member(jsii_name="indexName")
    def index_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "indexName"))

    @index_name.setter
    def index_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexName", value)

    @builtins.property
    @jsii.member(jsii_name="indexRotationPeriod")
    def index_rotation_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "indexRotationPeriod"))

    @index_rotation_period.setter
    def index_rotation_period(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexRotationPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="retryDuration")
    def retry_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retryDuration"))

    @retry_duration.setter
    def retry_duration(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryDuration", value)

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
    @jsii.member(jsii_name="s3BackupMode")
    def s3_backup_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3BackupMode"))

    @s3_backup_mode.setter
    def s3_backup_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BackupMode", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "processors": "processors"},
)
class KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        processors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                processors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument processors", value=processors, expected_type=type_hints["processors"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if processors is not None:
            self._values["processors"] = processors

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def processors(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors"]]]:
        '''processors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        result = self._values.get("processors")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationOutputReference",
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

    @jsii.member(jsii_name="putProcessors")
    def put_processors(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProcessors", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetProcessors")
    def reset_processors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessors", []))

    @builtins.property
    @jsii.member(jsii_name="processors")
    def processors(
        self,
    ) -> "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsList":
        return typing.cast("KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsList", jsii.get(self, "processors"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="processorsInput")
    def processors_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors"]]], jsii.get(self, "processorsInput"))

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
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "parameters": "parameters"},
)
class KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors:
    def __init__(
        self,
        *,
        type: builtins.str,
        parameters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                parameters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters"]]]:
        '''parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsList",
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
    ) -> "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsOutputReference",
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

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersList":
        return typing.cast("KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersList", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters"]]], jsii.get(self, "parametersInput"))

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
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "parameter_name": "parameterName",
        "parameter_value": "parameterValue",
    },
)
class KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters:
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        parameter_value: builtins.str,
    ) -> None:
        '''
        :param parameter_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.
        :param parameter_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.
        '''
        if __debug__:
            def stub(
                *,
                parameter_name: builtins.str,
                parameter_value: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
        self._values: typing.Dict[str, typing.Any] = {
            "parameter_name": parameter_name,
            "parameter_value": parameter_value,
        }

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.'''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.'''
        result = self._values.get("parameter_value")
        assert result is not None, "Required property 'parameter_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersList",
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
    ) -> "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersOutputReference",
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
    @jsii.member(jsii_name="parameterNameInput")
    def parameter_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterValueInput")
    def parameter_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterValueInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @parameter_name.setter
    def parameter_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterName", value)

    @builtins.property
    @jsii.member(jsii_name="parameterValue")
    def parameter_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterValue"))

    @parameter_value.setter
    def parameter_value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig",
    jsii_struct_bases=[],
    name_mapping={
        "role_arn": "roleArn",
        "security_group_ids": "securityGroupIds",
        "subnet_ids": "subnetIds",
    },
)
class KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#security_group_ids KinesisFirehoseDeliveryStream#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#subnet_ids KinesisFirehoseDeliveryStream#subnet_ids}.
        '''
        if __debug__:
            def stub(
                *,
                role_arn: builtins.str,
                security_group_ids: typing.Sequence[builtins.str],
                subnet_ids: typing.Sequence[builtins.str],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "role_arn": role_arn,
            "security_group_ids": security_group_ids,
            "subnet_ids": subnet_ids,
        }

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#security_group_ids KinesisFirehoseDeliveryStream#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#subnet_ids KinesisFirehoseDeliveryStream#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfigOutputReference",
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
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

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
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3Configuration",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_arn": "bucketArn",
        "role_arn": "roleArn",
        "buffer_interval": "bufferInterval",
        "buffer_size": "bufferSize",
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "compression_format": "compressionFormat",
        "data_format_conversion_configuration": "dataFormatConversionConfiguration",
        "dynamic_partitioning_configuration": "dynamicPartitioningConfiguration",
        "error_output_prefix": "errorOutputPrefix",
        "kms_key_arn": "kmsKeyArn",
        "prefix": "prefix",
        "processing_configuration": "processingConfiguration",
        "s3_backup_configuration": "s3BackupConfiguration",
        "s3_backup_mode": "s3BackupMode",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3Configuration:
    def __init__(
        self,
        *,
        bucket_arn: builtins.str,
        role_arn: builtins.str,
        buffer_interval: typing.Optional[jsii.Number] = None,
        buffer_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions", typing.Dict[str, typing.Any]]] = None,
        compression_format: typing.Optional[builtins.str] = None,
        data_format_conversion_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration", typing.Dict[str, typing.Any]]] = None,
        dynamic_partitioning_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration", typing.Dict[str, typing.Any]]] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration", typing.Dict[str, typing.Any]]] = None,
        s3_backup_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration", typing.Dict[str, typing.Any]]] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffer_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.
        :param buffer_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param compression_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.
        :param data_format_conversion_configuration: data_format_conversion_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#data_format_conversion_configuration KinesisFirehoseDeliveryStream#data_format_conversion_configuration}
        :param dynamic_partitioning_configuration: dynamic_partitioning_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#dynamic_partitioning_configuration KinesisFirehoseDeliveryStream#dynamic_partitioning_configuration}
        :param error_output_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param s3_backup_configuration: s3_backup_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_configuration KinesisFirehoseDeliveryStream#s3_backup_configuration}
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        '''
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if isinstance(data_format_conversion_configuration, dict):
            data_format_conversion_configuration = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration(**data_format_conversion_configuration)
        if isinstance(dynamic_partitioning_configuration, dict):
            dynamic_partitioning_configuration = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration(**dynamic_partitioning_configuration)
        if isinstance(processing_configuration, dict):
            processing_configuration = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration(**processing_configuration)
        if isinstance(s3_backup_configuration, dict):
            s3_backup_configuration = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration(**s3_backup_configuration)
        if __debug__:
            def stub(
                *,
                bucket_arn: builtins.str,
                role_arn: builtins.str,
                buffer_interval: typing.Optional[jsii.Number] = None,
                buffer_size: typing.Optional[jsii.Number] = None,
                cloudwatch_logging_options: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions, typing.Dict[str, typing.Any]]] = None,
                compression_format: typing.Optional[builtins.str] = None,
                data_format_conversion_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration, typing.Dict[str, typing.Any]]] = None,
                dynamic_partitioning_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration, typing.Dict[str, typing.Any]]] = None,
                error_output_prefix: typing.Optional[builtins.str] = None,
                kms_key_arn: typing.Optional[builtins.str] = None,
                prefix: typing.Optional[builtins.str] = None,
                processing_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration, typing.Dict[str, typing.Any]]] = None,
                s3_backup_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration, typing.Dict[str, typing.Any]]] = None,
                s3_backup_mode: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument buffer_interval", value=buffer_interval, expected_type=type_hints["buffer_interval"])
            check_type(argname="argument buffer_size", value=buffer_size, expected_type=type_hints["buffer_size"])
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument compression_format", value=compression_format, expected_type=type_hints["compression_format"])
            check_type(argname="argument data_format_conversion_configuration", value=data_format_conversion_configuration, expected_type=type_hints["data_format_conversion_configuration"])
            check_type(argname="argument dynamic_partitioning_configuration", value=dynamic_partitioning_configuration, expected_type=type_hints["dynamic_partitioning_configuration"])
            check_type(argname="argument error_output_prefix", value=error_output_prefix, expected_type=type_hints["error_output_prefix"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
            check_type(argname="argument s3_backup_configuration", value=s3_backup_configuration, expected_type=type_hints["s3_backup_configuration"])
            check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_arn": bucket_arn,
            "role_arn": role_arn,
        }
        if buffer_interval is not None:
            self._values["buffer_interval"] = buffer_interval
        if buffer_size is not None:
            self._values["buffer_size"] = buffer_size
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if compression_format is not None:
            self._values["compression_format"] = compression_format
        if data_format_conversion_configuration is not None:
            self._values["data_format_conversion_configuration"] = data_format_conversion_configuration
        if dynamic_partitioning_configuration is not None:
            self._values["dynamic_partitioning_configuration"] = dynamic_partitioning_configuration
        if error_output_prefix is not None:
            self._values["error_output_prefix"] = error_output_prefix
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if prefix is not None:
            self._values["prefix"] = prefix
        if processing_configuration is not None:
            self._values["processing_configuration"] = processing_configuration
        if s3_backup_configuration is not None:
            self._values["s3_backup_configuration"] = s3_backup_configuration
        if s3_backup_mode is not None:
            self._values["s3_backup_mode"] = s3_backup_mode

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def buffer_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.'''
        result = self._values.get("buffer_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def buffer_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.'''
        result = self._values.get("buffer_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions"]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions"], result)

    @builtins.property
    def compression_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.'''
        result = self._values.get("compression_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_format_conversion_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration"]:
        '''data_format_conversion_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#data_format_conversion_configuration KinesisFirehoseDeliveryStream#data_format_conversion_configuration}
        '''
        result = self._values.get("data_format_conversion_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration"], result)

    @builtins.property
    def dynamic_partitioning_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration"]:
        '''dynamic_partitioning_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#dynamic_partitioning_configuration KinesisFirehoseDeliveryStream#dynamic_partitioning_configuration}
        '''
        result = self._values.get("dynamic_partitioning_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration"], result)

    @builtins.property
    def error_output_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.'''
        result = self._values.get("error_output_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def processing_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration"]:
        '''processing_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        '''
        result = self._values.get("processing_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration"], result)

    @builtins.property
    def s3_backup_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration"]:
        '''s3_backup_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_configuration KinesisFirehoseDeliveryStream#s3_backup_configuration}
        '''
        result = self._values.get("s3_backup_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration"], result)

    @builtins.property
    def s3_backup_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.'''
        result = self._values.get("s3_backup_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3Configuration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                log_group_name: typing.Optional[builtins.str] = None,
                log_stream_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.'''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.'''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsOutputReference",
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

    @jsii.member(jsii_name="resetLogGroupName")
    def reset_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupName", []))

    @jsii.member(jsii_name="resetLogStreamName")
    def reset_log_stream_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreamName", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamNameInput")
    def log_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamNameInput"))

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
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))

    @log_stream_name.setter
    def log_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "input_format_configuration": "inputFormatConfiguration",
        "output_format_configuration": "outputFormatConfiguration",
        "schema_configuration": "schemaConfiguration",
        "enabled": "enabled",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration:
    def __init__(
        self,
        *,
        input_format_configuration: typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration", typing.Dict[str, typing.Any]],
        output_format_configuration: typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration", typing.Dict[str, typing.Any]],
        schema_configuration: typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration", typing.Dict[str, typing.Any]],
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param input_format_configuration: input_format_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#input_format_configuration KinesisFirehoseDeliveryStream#input_format_configuration}
        :param output_format_configuration: output_format_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#output_format_configuration KinesisFirehoseDeliveryStream#output_format_configuration}
        :param schema_configuration: schema_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#schema_configuration KinesisFirehoseDeliveryStream#schema_configuration}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        '''
        if isinstance(input_format_configuration, dict):
            input_format_configuration = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration(**input_format_configuration)
        if isinstance(output_format_configuration, dict):
            output_format_configuration = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration(**output_format_configuration)
        if isinstance(schema_configuration, dict):
            schema_configuration = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration(**schema_configuration)
        if __debug__:
            def stub(
                *,
                input_format_configuration: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration, typing.Dict[str, typing.Any]],
                output_format_configuration: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration, typing.Dict[str, typing.Any]],
                schema_configuration: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration, typing.Dict[str, typing.Any]],
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument input_format_configuration", value=input_format_configuration, expected_type=type_hints["input_format_configuration"])
            check_type(argname="argument output_format_configuration", value=output_format_configuration, expected_type=type_hints["output_format_configuration"])
            check_type(argname="argument schema_configuration", value=schema_configuration, expected_type=type_hints["schema_configuration"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "input_format_configuration": input_format_configuration,
            "output_format_configuration": output_format_configuration,
            "schema_configuration": schema_configuration,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def input_format_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration":
        '''input_format_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#input_format_configuration KinesisFirehoseDeliveryStream#input_format_configuration}
        '''
        result = self._values.get("input_format_configuration")
        assert result is not None, "Required property 'input_format_configuration' is missing"
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration", result)

    @builtins.property
    def output_format_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration":
        '''output_format_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#output_format_configuration KinesisFirehoseDeliveryStream#output_format_configuration}
        '''
        result = self._values.get("output_format_configuration")
        assert result is not None, "Required property 'output_format_configuration' is missing"
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration", result)

    @builtins.property
    def schema_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration":
        '''schema_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#schema_configuration KinesisFirehoseDeliveryStream#schema_configuration}
        '''
        result = self._values.get("schema_configuration")
        assert result is not None, "Required property 'schema_configuration' is missing"
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration", result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration",
    jsii_struct_bases=[],
    name_mapping={"deserializer": "deserializer"},
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration:
    def __init__(
        self,
        *,
        deserializer: typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param deserializer: deserializer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#deserializer KinesisFirehoseDeliveryStream#deserializer}
        '''
        if isinstance(deserializer, dict):
            deserializer = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer(**deserializer)
        if __debug__:
            def stub(
                *,
                deserializer: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument deserializer", value=deserializer, expected_type=type_hints["deserializer"])
        self._values: typing.Dict[str, typing.Any] = {
            "deserializer": deserializer,
        }

    @builtins.property
    def deserializer(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer":
        '''deserializer block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#deserializer KinesisFirehoseDeliveryStream#deserializer}
        '''
        result = self._values.get("deserializer")
        assert result is not None, "Required property 'deserializer' is missing"
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer",
    jsii_struct_bases=[],
    name_mapping={
        "hive_json_ser_de": "hiveJsonSerDe",
        "open_x_json_ser_de": "openXJsonSerDe",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer:
    def __init__(
        self,
        *,
        hive_json_ser_de: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe", typing.Dict[str, typing.Any]]] = None,
        open_x_json_ser_de: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param hive_json_ser_de: hive_json_ser_de block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hive_json_ser_de KinesisFirehoseDeliveryStream#hive_json_ser_de}
        :param open_x_json_ser_de: open_x_json_ser_de block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#open_x_json_ser_de KinesisFirehoseDeliveryStream#open_x_json_ser_de}
        '''
        if isinstance(hive_json_ser_de, dict):
            hive_json_ser_de = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe(**hive_json_ser_de)
        if isinstance(open_x_json_ser_de, dict):
            open_x_json_ser_de = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe(**open_x_json_ser_de)
        if __debug__:
            def stub(
                *,
                hive_json_ser_de: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe, typing.Dict[str, typing.Any]]] = None,
                open_x_json_ser_de: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument hive_json_ser_de", value=hive_json_ser_de, expected_type=type_hints["hive_json_ser_de"])
            check_type(argname="argument open_x_json_ser_de", value=open_x_json_ser_de, expected_type=type_hints["open_x_json_ser_de"])
        self._values: typing.Dict[str, typing.Any] = {}
        if hive_json_ser_de is not None:
            self._values["hive_json_ser_de"] = hive_json_ser_de
        if open_x_json_ser_de is not None:
            self._values["open_x_json_ser_de"] = open_x_json_ser_de

    @builtins.property
    def hive_json_ser_de(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe"]:
        '''hive_json_ser_de block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hive_json_ser_de KinesisFirehoseDeliveryStream#hive_json_ser_de}
        '''
        result = self._values.get("hive_json_ser_de")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe"], result)

    @builtins.property
    def open_x_json_ser_de(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe"]:
        '''open_x_json_ser_de block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#open_x_json_ser_de KinesisFirehoseDeliveryStream#open_x_json_ser_de}
        '''
        result = self._values.get("open_x_json_ser_de")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe",
    jsii_struct_bases=[],
    name_mapping={"timestamp_formats": "timestampFormats"},
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe:
    def __init__(
        self,
        *,
        timestamp_formats: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param timestamp_formats: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#timestamp_formats KinesisFirehoseDeliveryStream#timestamp_formats}.
        '''
        if __debug__:
            def stub(
                *,
                timestamp_formats: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument timestamp_formats", value=timestamp_formats, expected_type=type_hints["timestamp_formats"])
        self._values: typing.Dict[str, typing.Any] = {}
        if timestamp_formats is not None:
            self._values["timestamp_formats"] = timestamp_formats

    @builtins.property
    def timestamp_formats(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#timestamp_formats KinesisFirehoseDeliveryStream#timestamp_formats}.'''
        result = self._values.get("timestamp_formats")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeOutputReference",
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

    @jsii.member(jsii_name="resetTimestampFormats")
    def reset_timestamp_formats(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimestampFormats", []))

    @builtins.property
    @jsii.member(jsii_name="timestampFormatsInput")
    def timestamp_formats_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "timestampFormatsInput"))

    @builtins.property
    @jsii.member(jsii_name="timestampFormats")
    def timestamp_formats(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "timestampFormats"))

    @timestamp_formats.setter
    def timestamp_formats(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timestampFormats", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe",
    jsii_struct_bases=[],
    name_mapping={
        "case_insensitive": "caseInsensitive",
        "column_to_json_key_mappings": "columnToJsonKeyMappings",
        "convert_dots_in_json_keys_to_underscores": "convertDotsInJsonKeysToUnderscores",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe:
    def __init__(
        self,
        *,
        case_insensitive: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        column_to_json_key_mappings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        convert_dots_in_json_keys_to_underscores: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param case_insensitive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#case_insensitive KinesisFirehoseDeliveryStream#case_insensitive}.
        :param column_to_json_key_mappings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#column_to_json_key_mappings KinesisFirehoseDeliveryStream#column_to_json_key_mappings}.
        :param convert_dots_in_json_keys_to_underscores: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#convert_dots_in_json_keys_to_underscores KinesisFirehoseDeliveryStream#convert_dots_in_json_keys_to_underscores}.
        '''
        if __debug__:
            def stub(
                *,
                case_insensitive: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                column_to_json_key_mappings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                convert_dots_in_json_keys_to_underscores: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument case_insensitive", value=case_insensitive, expected_type=type_hints["case_insensitive"])
            check_type(argname="argument column_to_json_key_mappings", value=column_to_json_key_mappings, expected_type=type_hints["column_to_json_key_mappings"])
            check_type(argname="argument convert_dots_in_json_keys_to_underscores", value=convert_dots_in_json_keys_to_underscores, expected_type=type_hints["convert_dots_in_json_keys_to_underscores"])
        self._values: typing.Dict[str, typing.Any] = {}
        if case_insensitive is not None:
            self._values["case_insensitive"] = case_insensitive
        if column_to_json_key_mappings is not None:
            self._values["column_to_json_key_mappings"] = column_to_json_key_mappings
        if convert_dots_in_json_keys_to_underscores is not None:
            self._values["convert_dots_in_json_keys_to_underscores"] = convert_dots_in_json_keys_to_underscores

    @builtins.property
    def case_insensitive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#case_insensitive KinesisFirehoseDeliveryStream#case_insensitive}.'''
        result = self._values.get("case_insensitive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def column_to_json_key_mappings(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#column_to_json_key_mappings KinesisFirehoseDeliveryStream#column_to_json_key_mappings}.'''
        result = self._values.get("column_to_json_key_mappings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def convert_dots_in_json_keys_to_underscores(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#convert_dots_in_json_keys_to_underscores KinesisFirehoseDeliveryStream#convert_dots_in_json_keys_to_underscores}.'''
        result = self._values.get("convert_dots_in_json_keys_to_underscores")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeOutputReference",
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

    @jsii.member(jsii_name="resetCaseInsensitive")
    def reset_case_insensitive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaseInsensitive", []))

    @jsii.member(jsii_name="resetColumnToJsonKeyMappings")
    def reset_column_to_json_key_mappings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColumnToJsonKeyMappings", []))

    @jsii.member(jsii_name="resetConvertDotsInJsonKeysToUnderscores")
    def reset_convert_dots_in_json_keys_to_underscores(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConvertDotsInJsonKeysToUnderscores", []))

    @builtins.property
    @jsii.member(jsii_name="caseInsensitiveInput")
    def case_insensitive_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "caseInsensitiveInput"))

    @builtins.property
    @jsii.member(jsii_name="columnToJsonKeyMappingsInput")
    def column_to_json_key_mappings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "columnToJsonKeyMappingsInput"))

    @builtins.property
    @jsii.member(jsii_name="convertDotsInJsonKeysToUnderscoresInput")
    def convert_dots_in_json_keys_to_underscores_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "convertDotsInJsonKeysToUnderscoresInput"))

    @builtins.property
    @jsii.member(jsii_name="caseInsensitive")
    def case_insensitive(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "caseInsensitive"))

    @case_insensitive.setter
    def case_insensitive(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caseInsensitive", value)

    @builtins.property
    @jsii.member(jsii_name="columnToJsonKeyMappings")
    def column_to_json_key_mappings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "columnToJsonKeyMappings"))

    @column_to_json_key_mappings.setter
    def column_to_json_key_mappings(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "columnToJsonKeyMappings", value)

    @builtins.property
    @jsii.member(jsii_name="convertDotsInJsonKeysToUnderscores")
    def convert_dots_in_json_keys_to_underscores(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "convertDotsInJsonKeysToUnderscores"))

    @convert_dots_in_json_keys_to_underscores.setter
    def convert_dots_in_json_keys_to_underscores(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "convertDotsInJsonKeysToUnderscores", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOutputReference",
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

    @jsii.member(jsii_name="putHiveJsonSerDe")
    def put_hive_json_ser_de(
        self,
        *,
        timestamp_formats: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param timestamp_formats: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#timestamp_formats KinesisFirehoseDeliveryStream#timestamp_formats}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe(
            timestamp_formats=timestamp_formats
        )

        return typing.cast(None, jsii.invoke(self, "putHiveJsonSerDe", [value]))

    @jsii.member(jsii_name="putOpenXJsonSerDe")
    def put_open_x_json_ser_de(
        self,
        *,
        case_insensitive: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        column_to_json_key_mappings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        convert_dots_in_json_keys_to_underscores: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param case_insensitive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#case_insensitive KinesisFirehoseDeliveryStream#case_insensitive}.
        :param column_to_json_key_mappings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#column_to_json_key_mappings KinesisFirehoseDeliveryStream#column_to_json_key_mappings}.
        :param convert_dots_in_json_keys_to_underscores: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#convert_dots_in_json_keys_to_underscores KinesisFirehoseDeliveryStream#convert_dots_in_json_keys_to_underscores}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe(
            case_insensitive=case_insensitive,
            column_to_json_key_mappings=column_to_json_key_mappings,
            convert_dots_in_json_keys_to_underscores=convert_dots_in_json_keys_to_underscores,
        )

        return typing.cast(None, jsii.invoke(self, "putOpenXJsonSerDe", [value]))

    @jsii.member(jsii_name="resetHiveJsonSerDe")
    def reset_hive_json_ser_de(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHiveJsonSerDe", []))

    @jsii.member(jsii_name="resetOpenXJsonSerDe")
    def reset_open_x_json_ser_de(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpenXJsonSerDe", []))

    @builtins.property
    @jsii.member(jsii_name="hiveJsonSerDe")
    def hive_json_ser_de(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeOutputReference, jsii.get(self, "hiveJsonSerDe"))

    @builtins.property
    @jsii.member(jsii_name="openXJsonSerDe")
    def open_x_json_ser_de(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeOutputReference, jsii.get(self, "openXJsonSerDe"))

    @builtins.property
    @jsii.member(jsii_name="hiveJsonSerDeInput")
    def hive_json_ser_de_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe], jsii.get(self, "hiveJsonSerDeInput"))

    @builtins.property
    @jsii.member(jsii_name="openXJsonSerDeInput")
    def open_x_json_ser_de_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe], jsii.get(self, "openXJsonSerDeInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationOutputReference",
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

    @jsii.member(jsii_name="putDeserializer")
    def put_deserializer(
        self,
        *,
        hive_json_ser_de: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe, typing.Dict[str, typing.Any]]] = None,
        open_x_json_ser_de: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param hive_json_ser_de: hive_json_ser_de block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hive_json_ser_de KinesisFirehoseDeliveryStream#hive_json_ser_de}
        :param open_x_json_ser_de: open_x_json_ser_de block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#open_x_json_ser_de KinesisFirehoseDeliveryStream#open_x_json_ser_de}
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer(
            hive_json_ser_de=hive_json_ser_de, open_x_json_ser_de=open_x_json_ser_de
        )

        return typing.cast(None, jsii.invoke(self, "putDeserializer", [value]))

    @builtins.property
    @jsii.member(jsii_name="deserializer")
    def deserializer(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOutputReference, jsii.get(self, "deserializer"))

    @builtins.property
    @jsii.member(jsii_name="deserializerInput")
    def deserializer_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer], jsii.get(self, "deserializerInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration",
    jsii_struct_bases=[],
    name_mapping={"serializer": "serializer"},
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration:
    def __init__(
        self,
        *,
        serializer: typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param serializer: serializer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#serializer KinesisFirehoseDeliveryStream#serializer}
        '''
        if isinstance(serializer, dict):
            serializer = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer(**serializer)
        if __debug__:
            def stub(
                *,
                serializer: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument serializer", value=serializer, expected_type=type_hints["serializer"])
        self._values: typing.Dict[str, typing.Any] = {
            "serializer": serializer,
        }

    @builtins.property
    def serializer(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer":
        '''serializer block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#serializer KinesisFirehoseDeliveryStream#serializer}
        '''
        result = self._values.get("serializer")
        assert result is not None, "Required property 'serializer' is missing"
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationOutputReference",
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

    @jsii.member(jsii_name="putSerializer")
    def put_serializer(
        self,
        *,
        orc_ser_de: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe", typing.Dict[str, typing.Any]]] = None,
        parquet_ser_de: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param orc_ser_de: orc_ser_de block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#orc_ser_de KinesisFirehoseDeliveryStream#orc_ser_de}
        :param parquet_ser_de: parquet_ser_de block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parquet_ser_de KinesisFirehoseDeliveryStream#parquet_ser_de}
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer(
            orc_ser_de=orc_ser_de, parquet_ser_de=parquet_ser_de
        )

        return typing.cast(None, jsii.invoke(self, "putSerializer", [value]))

    @builtins.property
    @jsii.member(jsii_name="serializer")
    def serializer(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOutputReference", jsii.get(self, "serializer"))

    @builtins.property
    @jsii.member(jsii_name="serializerInput")
    def serializer_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer"], jsii.get(self, "serializerInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer",
    jsii_struct_bases=[],
    name_mapping={"orc_ser_de": "orcSerDe", "parquet_ser_de": "parquetSerDe"},
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer:
    def __init__(
        self,
        *,
        orc_ser_de: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe", typing.Dict[str, typing.Any]]] = None,
        parquet_ser_de: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param orc_ser_de: orc_ser_de block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#orc_ser_de KinesisFirehoseDeliveryStream#orc_ser_de}
        :param parquet_ser_de: parquet_ser_de block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parquet_ser_de KinesisFirehoseDeliveryStream#parquet_ser_de}
        '''
        if isinstance(orc_ser_de, dict):
            orc_ser_de = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe(**orc_ser_de)
        if isinstance(parquet_ser_de, dict):
            parquet_ser_de = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe(**parquet_ser_de)
        if __debug__:
            def stub(
                *,
                orc_ser_de: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe, typing.Dict[str, typing.Any]]] = None,
                parquet_ser_de: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument orc_ser_de", value=orc_ser_de, expected_type=type_hints["orc_ser_de"])
            check_type(argname="argument parquet_ser_de", value=parquet_ser_de, expected_type=type_hints["parquet_ser_de"])
        self._values: typing.Dict[str, typing.Any] = {}
        if orc_ser_de is not None:
            self._values["orc_ser_de"] = orc_ser_de
        if parquet_ser_de is not None:
            self._values["parquet_ser_de"] = parquet_ser_de

    @builtins.property
    def orc_ser_de(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe"]:
        '''orc_ser_de block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#orc_ser_de KinesisFirehoseDeliveryStream#orc_ser_de}
        '''
        result = self._values.get("orc_ser_de")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe"], result)

    @builtins.property
    def parquet_ser_de(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe"]:
        '''parquet_ser_de block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parquet_ser_de KinesisFirehoseDeliveryStream#parquet_ser_de}
        '''
        result = self._values.get("parquet_ser_de")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe",
    jsii_struct_bases=[],
    name_mapping={
        "block_size_bytes": "blockSizeBytes",
        "bloom_filter_columns": "bloomFilterColumns",
        "bloom_filter_false_positive_probability": "bloomFilterFalsePositiveProbability",
        "compression": "compression",
        "dictionary_key_threshold": "dictionaryKeyThreshold",
        "enable_padding": "enablePadding",
        "format_version": "formatVersion",
        "padding_tolerance": "paddingTolerance",
        "row_index_stride": "rowIndexStride",
        "stripe_size_bytes": "stripeSizeBytes",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe:
    def __init__(
        self,
        *,
        block_size_bytes: typing.Optional[jsii.Number] = None,
        bloom_filter_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
        bloom_filter_false_positive_probability: typing.Optional[jsii.Number] = None,
        compression: typing.Optional[builtins.str] = None,
        dictionary_key_threshold: typing.Optional[jsii.Number] = None,
        enable_padding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        format_version: typing.Optional[builtins.str] = None,
        padding_tolerance: typing.Optional[jsii.Number] = None,
        row_index_stride: typing.Optional[jsii.Number] = None,
        stripe_size_bytes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param block_size_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#block_size_bytes KinesisFirehoseDeliveryStream#block_size_bytes}.
        :param bloom_filter_columns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bloom_filter_columns KinesisFirehoseDeliveryStream#bloom_filter_columns}.
        :param bloom_filter_false_positive_probability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bloom_filter_false_positive_probability KinesisFirehoseDeliveryStream#bloom_filter_false_positive_probability}.
        :param compression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression KinesisFirehoseDeliveryStream#compression}.
        :param dictionary_key_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#dictionary_key_threshold KinesisFirehoseDeliveryStream#dictionary_key_threshold}.
        :param enable_padding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enable_padding KinesisFirehoseDeliveryStream#enable_padding}.
        :param format_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#format_version KinesisFirehoseDeliveryStream#format_version}.
        :param padding_tolerance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#padding_tolerance KinesisFirehoseDeliveryStream#padding_tolerance}.
        :param row_index_stride: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#row_index_stride KinesisFirehoseDeliveryStream#row_index_stride}.
        :param stripe_size_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#stripe_size_bytes KinesisFirehoseDeliveryStream#stripe_size_bytes}.
        '''
        if __debug__:
            def stub(
                *,
                block_size_bytes: typing.Optional[jsii.Number] = None,
                bloom_filter_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
                bloom_filter_false_positive_probability: typing.Optional[jsii.Number] = None,
                compression: typing.Optional[builtins.str] = None,
                dictionary_key_threshold: typing.Optional[jsii.Number] = None,
                enable_padding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                format_version: typing.Optional[builtins.str] = None,
                padding_tolerance: typing.Optional[jsii.Number] = None,
                row_index_stride: typing.Optional[jsii.Number] = None,
                stripe_size_bytes: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument block_size_bytes", value=block_size_bytes, expected_type=type_hints["block_size_bytes"])
            check_type(argname="argument bloom_filter_columns", value=bloom_filter_columns, expected_type=type_hints["bloom_filter_columns"])
            check_type(argname="argument bloom_filter_false_positive_probability", value=bloom_filter_false_positive_probability, expected_type=type_hints["bloom_filter_false_positive_probability"])
            check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
            check_type(argname="argument dictionary_key_threshold", value=dictionary_key_threshold, expected_type=type_hints["dictionary_key_threshold"])
            check_type(argname="argument enable_padding", value=enable_padding, expected_type=type_hints["enable_padding"])
            check_type(argname="argument format_version", value=format_version, expected_type=type_hints["format_version"])
            check_type(argname="argument padding_tolerance", value=padding_tolerance, expected_type=type_hints["padding_tolerance"])
            check_type(argname="argument row_index_stride", value=row_index_stride, expected_type=type_hints["row_index_stride"])
            check_type(argname="argument stripe_size_bytes", value=stripe_size_bytes, expected_type=type_hints["stripe_size_bytes"])
        self._values: typing.Dict[str, typing.Any] = {}
        if block_size_bytes is not None:
            self._values["block_size_bytes"] = block_size_bytes
        if bloom_filter_columns is not None:
            self._values["bloom_filter_columns"] = bloom_filter_columns
        if bloom_filter_false_positive_probability is not None:
            self._values["bloom_filter_false_positive_probability"] = bloom_filter_false_positive_probability
        if compression is not None:
            self._values["compression"] = compression
        if dictionary_key_threshold is not None:
            self._values["dictionary_key_threshold"] = dictionary_key_threshold
        if enable_padding is not None:
            self._values["enable_padding"] = enable_padding
        if format_version is not None:
            self._values["format_version"] = format_version
        if padding_tolerance is not None:
            self._values["padding_tolerance"] = padding_tolerance
        if row_index_stride is not None:
            self._values["row_index_stride"] = row_index_stride
        if stripe_size_bytes is not None:
            self._values["stripe_size_bytes"] = stripe_size_bytes

    @builtins.property
    def block_size_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#block_size_bytes KinesisFirehoseDeliveryStream#block_size_bytes}.'''
        result = self._values.get("block_size_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def bloom_filter_columns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bloom_filter_columns KinesisFirehoseDeliveryStream#bloom_filter_columns}.'''
        result = self._values.get("bloom_filter_columns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def bloom_filter_false_positive_probability(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bloom_filter_false_positive_probability KinesisFirehoseDeliveryStream#bloom_filter_false_positive_probability}.'''
        result = self._values.get("bloom_filter_false_positive_probability")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def compression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression KinesisFirehoseDeliveryStream#compression}.'''
        result = self._values.get("compression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dictionary_key_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#dictionary_key_threshold KinesisFirehoseDeliveryStream#dictionary_key_threshold}.'''
        result = self._values.get("dictionary_key_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enable_padding(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enable_padding KinesisFirehoseDeliveryStream#enable_padding}.'''
        result = self._values.get("enable_padding")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def format_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#format_version KinesisFirehoseDeliveryStream#format_version}.'''
        result = self._values.get("format_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def padding_tolerance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#padding_tolerance KinesisFirehoseDeliveryStream#padding_tolerance}.'''
        result = self._values.get("padding_tolerance")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def row_index_stride(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#row_index_stride KinesisFirehoseDeliveryStream#row_index_stride}.'''
        result = self._values.get("row_index_stride")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stripe_size_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#stripe_size_bytes KinesisFirehoseDeliveryStream#stripe_size_bytes}.'''
        result = self._values.get("stripe_size_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeOutputReference",
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

    @jsii.member(jsii_name="resetBlockSizeBytes")
    def reset_block_size_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockSizeBytes", []))

    @jsii.member(jsii_name="resetBloomFilterColumns")
    def reset_bloom_filter_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBloomFilterColumns", []))

    @jsii.member(jsii_name="resetBloomFilterFalsePositiveProbability")
    def reset_bloom_filter_false_positive_probability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBloomFilterFalsePositiveProbability", []))

    @jsii.member(jsii_name="resetCompression")
    def reset_compression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompression", []))

    @jsii.member(jsii_name="resetDictionaryKeyThreshold")
    def reset_dictionary_key_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDictionaryKeyThreshold", []))

    @jsii.member(jsii_name="resetEnablePadding")
    def reset_enable_padding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablePadding", []))

    @jsii.member(jsii_name="resetFormatVersion")
    def reset_format_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFormatVersion", []))

    @jsii.member(jsii_name="resetPaddingTolerance")
    def reset_padding_tolerance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPaddingTolerance", []))

    @jsii.member(jsii_name="resetRowIndexStride")
    def reset_row_index_stride(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRowIndexStride", []))

    @jsii.member(jsii_name="resetStripeSizeBytes")
    def reset_stripe_size_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStripeSizeBytes", []))

    @builtins.property
    @jsii.member(jsii_name="blockSizeBytesInput")
    def block_size_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "blockSizeBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="bloomFilterColumnsInput")
    def bloom_filter_columns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "bloomFilterColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="bloomFilterFalsePositiveProbabilityInput")
    def bloom_filter_false_positive_probability_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bloomFilterFalsePositiveProbabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionInput")
    def compression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionInput"))

    @builtins.property
    @jsii.member(jsii_name="dictionaryKeyThresholdInput")
    def dictionary_key_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dictionaryKeyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="enablePaddingInput")
    def enable_padding_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enablePaddingInput"))

    @builtins.property
    @jsii.member(jsii_name="formatVersionInput")
    def format_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="paddingToleranceInput")
    def padding_tolerance_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "paddingToleranceInput"))

    @builtins.property
    @jsii.member(jsii_name="rowIndexStrideInput")
    def row_index_stride_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowIndexStrideInput"))

    @builtins.property
    @jsii.member(jsii_name="stripeSizeBytesInput")
    def stripe_size_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "stripeSizeBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="blockSizeBytes")
    def block_size_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "blockSizeBytes"))

    @block_size_bytes.setter
    def block_size_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockSizeBytes", value)

    @builtins.property
    @jsii.member(jsii_name="bloomFilterColumns")
    def bloom_filter_columns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "bloomFilterColumns"))

    @bloom_filter_columns.setter
    def bloom_filter_columns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bloomFilterColumns", value)

    @builtins.property
    @jsii.member(jsii_name="bloomFilterFalsePositiveProbability")
    def bloom_filter_false_positive_probability(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bloomFilterFalsePositiveProbability"))

    @bloom_filter_false_positive_probability.setter
    def bloom_filter_false_positive_probability(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bloomFilterFalsePositiveProbability", value)

    @builtins.property
    @jsii.member(jsii_name="compression")
    def compression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compression"))

    @compression.setter
    def compression(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compression", value)

    @builtins.property
    @jsii.member(jsii_name="dictionaryKeyThreshold")
    def dictionary_key_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dictionaryKeyThreshold"))

    @dictionary_key_threshold.setter
    def dictionary_key_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dictionaryKeyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="enablePadding")
    def enable_padding(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enablePadding"))

    @enable_padding.setter
    def enable_padding(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePadding", value)

    @builtins.property
    @jsii.member(jsii_name="formatVersion")
    def format_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "formatVersion"))

    @format_version.setter
    def format_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "formatVersion", value)

    @builtins.property
    @jsii.member(jsii_name="paddingTolerance")
    def padding_tolerance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "paddingTolerance"))

    @padding_tolerance.setter
    def padding_tolerance(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "paddingTolerance", value)

    @builtins.property
    @jsii.member(jsii_name="rowIndexStride")
    def row_index_stride(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rowIndexStride"))

    @row_index_stride.setter
    def row_index_stride(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rowIndexStride", value)

    @builtins.property
    @jsii.member(jsii_name="stripeSizeBytes")
    def stripe_size_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "stripeSizeBytes"))

    @stripe_size_bytes.setter
    def stripe_size_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stripeSizeBytes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOutputReference",
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

    @jsii.member(jsii_name="putOrcSerDe")
    def put_orc_ser_de(
        self,
        *,
        block_size_bytes: typing.Optional[jsii.Number] = None,
        bloom_filter_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
        bloom_filter_false_positive_probability: typing.Optional[jsii.Number] = None,
        compression: typing.Optional[builtins.str] = None,
        dictionary_key_threshold: typing.Optional[jsii.Number] = None,
        enable_padding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        format_version: typing.Optional[builtins.str] = None,
        padding_tolerance: typing.Optional[jsii.Number] = None,
        row_index_stride: typing.Optional[jsii.Number] = None,
        stripe_size_bytes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param block_size_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#block_size_bytes KinesisFirehoseDeliveryStream#block_size_bytes}.
        :param bloom_filter_columns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bloom_filter_columns KinesisFirehoseDeliveryStream#bloom_filter_columns}.
        :param bloom_filter_false_positive_probability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bloom_filter_false_positive_probability KinesisFirehoseDeliveryStream#bloom_filter_false_positive_probability}.
        :param compression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression KinesisFirehoseDeliveryStream#compression}.
        :param dictionary_key_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#dictionary_key_threshold KinesisFirehoseDeliveryStream#dictionary_key_threshold}.
        :param enable_padding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enable_padding KinesisFirehoseDeliveryStream#enable_padding}.
        :param format_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#format_version KinesisFirehoseDeliveryStream#format_version}.
        :param padding_tolerance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#padding_tolerance KinesisFirehoseDeliveryStream#padding_tolerance}.
        :param row_index_stride: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#row_index_stride KinesisFirehoseDeliveryStream#row_index_stride}.
        :param stripe_size_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#stripe_size_bytes KinesisFirehoseDeliveryStream#stripe_size_bytes}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe(
            block_size_bytes=block_size_bytes,
            bloom_filter_columns=bloom_filter_columns,
            bloom_filter_false_positive_probability=bloom_filter_false_positive_probability,
            compression=compression,
            dictionary_key_threshold=dictionary_key_threshold,
            enable_padding=enable_padding,
            format_version=format_version,
            padding_tolerance=padding_tolerance,
            row_index_stride=row_index_stride,
            stripe_size_bytes=stripe_size_bytes,
        )

        return typing.cast(None, jsii.invoke(self, "putOrcSerDe", [value]))

    @jsii.member(jsii_name="putParquetSerDe")
    def put_parquet_ser_de(
        self,
        *,
        block_size_bytes: typing.Optional[jsii.Number] = None,
        compression: typing.Optional[builtins.str] = None,
        enable_dictionary_compression: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_padding_bytes: typing.Optional[jsii.Number] = None,
        page_size_bytes: typing.Optional[jsii.Number] = None,
        writer_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param block_size_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#block_size_bytes KinesisFirehoseDeliveryStream#block_size_bytes}.
        :param compression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression KinesisFirehoseDeliveryStream#compression}.
        :param enable_dictionary_compression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enable_dictionary_compression KinesisFirehoseDeliveryStream#enable_dictionary_compression}.
        :param max_padding_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#max_padding_bytes KinesisFirehoseDeliveryStream#max_padding_bytes}.
        :param page_size_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#page_size_bytes KinesisFirehoseDeliveryStream#page_size_bytes}.
        :param writer_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#writer_version KinesisFirehoseDeliveryStream#writer_version}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe(
            block_size_bytes=block_size_bytes,
            compression=compression,
            enable_dictionary_compression=enable_dictionary_compression,
            max_padding_bytes=max_padding_bytes,
            page_size_bytes=page_size_bytes,
            writer_version=writer_version,
        )

        return typing.cast(None, jsii.invoke(self, "putParquetSerDe", [value]))

    @jsii.member(jsii_name="resetOrcSerDe")
    def reset_orc_ser_de(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrcSerDe", []))

    @jsii.member(jsii_name="resetParquetSerDe")
    def reset_parquet_ser_de(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParquetSerDe", []))

    @builtins.property
    @jsii.member(jsii_name="orcSerDe")
    def orc_ser_de(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeOutputReference, jsii.get(self, "orcSerDe"))

    @builtins.property
    @jsii.member(jsii_name="parquetSerDe")
    def parquet_ser_de(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeOutputReference", jsii.get(self, "parquetSerDe"))

    @builtins.property
    @jsii.member(jsii_name="orcSerDeInput")
    def orc_ser_de_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe], jsii.get(self, "orcSerDeInput"))

    @builtins.property
    @jsii.member(jsii_name="parquetSerDeInput")
    def parquet_ser_de_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe"], jsii.get(self, "parquetSerDeInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe",
    jsii_struct_bases=[],
    name_mapping={
        "block_size_bytes": "blockSizeBytes",
        "compression": "compression",
        "enable_dictionary_compression": "enableDictionaryCompression",
        "max_padding_bytes": "maxPaddingBytes",
        "page_size_bytes": "pageSizeBytes",
        "writer_version": "writerVersion",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe:
    def __init__(
        self,
        *,
        block_size_bytes: typing.Optional[jsii.Number] = None,
        compression: typing.Optional[builtins.str] = None,
        enable_dictionary_compression: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_padding_bytes: typing.Optional[jsii.Number] = None,
        page_size_bytes: typing.Optional[jsii.Number] = None,
        writer_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param block_size_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#block_size_bytes KinesisFirehoseDeliveryStream#block_size_bytes}.
        :param compression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression KinesisFirehoseDeliveryStream#compression}.
        :param enable_dictionary_compression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enable_dictionary_compression KinesisFirehoseDeliveryStream#enable_dictionary_compression}.
        :param max_padding_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#max_padding_bytes KinesisFirehoseDeliveryStream#max_padding_bytes}.
        :param page_size_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#page_size_bytes KinesisFirehoseDeliveryStream#page_size_bytes}.
        :param writer_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#writer_version KinesisFirehoseDeliveryStream#writer_version}.
        '''
        if __debug__:
            def stub(
                *,
                block_size_bytes: typing.Optional[jsii.Number] = None,
                compression: typing.Optional[builtins.str] = None,
                enable_dictionary_compression: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                max_padding_bytes: typing.Optional[jsii.Number] = None,
                page_size_bytes: typing.Optional[jsii.Number] = None,
                writer_version: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument block_size_bytes", value=block_size_bytes, expected_type=type_hints["block_size_bytes"])
            check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
            check_type(argname="argument enable_dictionary_compression", value=enable_dictionary_compression, expected_type=type_hints["enable_dictionary_compression"])
            check_type(argname="argument max_padding_bytes", value=max_padding_bytes, expected_type=type_hints["max_padding_bytes"])
            check_type(argname="argument page_size_bytes", value=page_size_bytes, expected_type=type_hints["page_size_bytes"])
            check_type(argname="argument writer_version", value=writer_version, expected_type=type_hints["writer_version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if block_size_bytes is not None:
            self._values["block_size_bytes"] = block_size_bytes
        if compression is not None:
            self._values["compression"] = compression
        if enable_dictionary_compression is not None:
            self._values["enable_dictionary_compression"] = enable_dictionary_compression
        if max_padding_bytes is not None:
            self._values["max_padding_bytes"] = max_padding_bytes
        if page_size_bytes is not None:
            self._values["page_size_bytes"] = page_size_bytes
        if writer_version is not None:
            self._values["writer_version"] = writer_version

    @builtins.property
    def block_size_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#block_size_bytes KinesisFirehoseDeliveryStream#block_size_bytes}.'''
        result = self._values.get("block_size_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def compression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression KinesisFirehoseDeliveryStream#compression}.'''
        result = self._values.get("compression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_dictionary_compression(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enable_dictionary_compression KinesisFirehoseDeliveryStream#enable_dictionary_compression}.'''
        result = self._values.get("enable_dictionary_compression")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_padding_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#max_padding_bytes KinesisFirehoseDeliveryStream#max_padding_bytes}.'''
        result = self._values.get("max_padding_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def page_size_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#page_size_bytes KinesisFirehoseDeliveryStream#page_size_bytes}.'''
        result = self._values.get("page_size_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def writer_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#writer_version KinesisFirehoseDeliveryStream#writer_version}.'''
        result = self._values.get("writer_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeOutputReference",
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

    @jsii.member(jsii_name="resetBlockSizeBytes")
    def reset_block_size_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockSizeBytes", []))

    @jsii.member(jsii_name="resetCompression")
    def reset_compression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompression", []))

    @jsii.member(jsii_name="resetEnableDictionaryCompression")
    def reset_enable_dictionary_compression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableDictionaryCompression", []))

    @jsii.member(jsii_name="resetMaxPaddingBytes")
    def reset_max_padding_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxPaddingBytes", []))

    @jsii.member(jsii_name="resetPageSizeBytes")
    def reset_page_size_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPageSizeBytes", []))

    @jsii.member(jsii_name="resetWriterVersion")
    def reset_writer_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriterVersion", []))

    @builtins.property
    @jsii.member(jsii_name="blockSizeBytesInput")
    def block_size_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "blockSizeBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionInput")
    def compression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionInput"))

    @builtins.property
    @jsii.member(jsii_name="enableDictionaryCompressionInput")
    def enable_dictionary_compression_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableDictionaryCompressionInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPaddingBytesInput")
    def max_padding_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxPaddingBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="pageSizeBytesInput")
    def page_size_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "pageSizeBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="writerVersionInput")
    def writer_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "writerVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="blockSizeBytes")
    def block_size_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "blockSizeBytes"))

    @block_size_bytes.setter
    def block_size_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockSizeBytes", value)

    @builtins.property
    @jsii.member(jsii_name="compression")
    def compression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compression"))

    @compression.setter
    def compression(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compression", value)

    @builtins.property
    @jsii.member(jsii_name="enableDictionaryCompression")
    def enable_dictionary_compression(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableDictionaryCompression"))

    @enable_dictionary_compression.setter
    def enable_dictionary_compression(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDictionaryCompression", value)

    @builtins.property
    @jsii.member(jsii_name="maxPaddingBytes")
    def max_padding_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPaddingBytes"))

    @max_padding_bytes.setter
    def max_padding_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPaddingBytes", value)

    @builtins.property
    @jsii.member(jsii_name="pageSizeBytes")
    def page_size_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "pageSizeBytes"))

    @page_size_bytes.setter
    def page_size_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pageSizeBytes", value)

    @builtins.property
    @jsii.member(jsii_name="writerVersion")
    def writer_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "writerVersion"))

    @writer_version.setter
    def writer_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writerVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputReference",
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

    @jsii.member(jsii_name="putInputFormatConfiguration")
    def put_input_format_configuration(
        self,
        *,
        deserializer: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param deserializer: deserializer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#deserializer KinesisFirehoseDeliveryStream#deserializer}
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration(
            deserializer=deserializer
        )

        return typing.cast(None, jsii.invoke(self, "putInputFormatConfiguration", [value]))

    @jsii.member(jsii_name="putOutputFormatConfiguration")
    def put_output_format_configuration(
        self,
        *,
        serializer: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param serializer: serializer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#serializer KinesisFirehoseDeliveryStream#serializer}
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration(
            serializer=serializer
        )

        return typing.cast(None, jsii.invoke(self, "putOutputFormatConfiguration", [value]))

    @jsii.member(jsii_name="putSchemaConfiguration")
    def put_schema_configuration(
        self,
        *,
        database_name: builtins.str,
        role_arn: builtins.str,
        table_name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#database_name KinesisFirehoseDeliveryStream#database_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#table_name KinesisFirehoseDeliveryStream#table_name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#catalog_id KinesisFirehoseDeliveryStream#catalog_id}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#region KinesisFirehoseDeliveryStream#region}.
        :param version_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#version_id KinesisFirehoseDeliveryStream#version_id}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration(
            database_name=database_name,
            role_arn=role_arn,
            table_name=table_name,
            catalog_id=catalog_id,
            region=region,
            version_id=version_id,
        )

        return typing.cast(None, jsii.invoke(self, "putSchemaConfiguration", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="inputFormatConfiguration")
    def input_format_configuration(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationOutputReference, jsii.get(self, "inputFormatConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="outputFormatConfiguration")
    def output_format_configuration(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationOutputReference, jsii.get(self, "outputFormatConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="schemaConfiguration")
    def schema_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationOutputReference", jsii.get(self, "schemaConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="inputFormatConfigurationInput")
    def input_format_configuration_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration], jsii.get(self, "inputFormatConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="outputFormatConfigurationInput")
    def output_format_configuration_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration], jsii.get(self, "outputFormatConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaConfigurationInput")
    def schema_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration"], jsii.get(self, "schemaConfigurationInput"))

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
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "role_arn": "roleArn",
        "table_name": "tableName",
        "catalog_id": "catalogId",
        "region": "region",
        "version_id": "versionId",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        role_arn: builtins.str,
        table_name: builtins.str,
        catalog_id: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#database_name KinesisFirehoseDeliveryStream#database_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#table_name KinesisFirehoseDeliveryStream#table_name}.
        :param catalog_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#catalog_id KinesisFirehoseDeliveryStream#catalog_id}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#region KinesisFirehoseDeliveryStream#region}.
        :param version_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#version_id KinesisFirehoseDeliveryStream#version_id}.
        '''
        if __debug__:
            def stub(
                *,
                database_name: builtins.str,
                role_arn: builtins.str,
                table_name: builtins.str,
                catalog_id: typing.Optional[builtins.str] = None,
                region: typing.Optional[builtins.str] = None,
                version_id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument version_id", value=version_id, expected_type=type_hints["version_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "database_name": database_name,
            "role_arn": role_arn,
            "table_name": table_name,
        }
        if catalog_id is not None:
            self._values["catalog_id"] = catalog_id
        if region is not None:
            self._values["region"] = region
        if version_id is not None:
            self._values["version_id"] = version_id

    @builtins.property
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#database_name KinesisFirehoseDeliveryStream#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#table_name KinesisFirehoseDeliveryStream#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def catalog_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#catalog_id KinesisFirehoseDeliveryStream#catalog_id}.'''
        result = self._values.get("catalog_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#region KinesisFirehoseDeliveryStream#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#version_id KinesisFirehoseDeliveryStream#version_id}.'''
        result = self._values.get("version_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationOutputReference",
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

    @jsii.member(jsii_name="resetCatalogId")
    def reset_catalog_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalogId", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetVersionId")
    def reset_version_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersionId", []))

    @builtins.property
    @jsii.member(jsii_name="catalogIdInput")
    def catalog_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogIdInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="versionIdInput")
    def version_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionIdInput"))

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
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

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
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionId"))

    @version_id.setter
    def version_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "retry_duration": "retryDuration"},
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                retry_duration: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument retry_duration", value=retry_duration, expected_type=type_hints["retry_duration"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if retry_duration is not None:
            self._values["retry_duration"] = retry_duration

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def retry_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.'''
        result = self._values.get("retry_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfigurationOutputReference",
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

    @jsii.member(jsii_name="resetRetryDuration")
    def reset_retry_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryDuration", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="retryDurationInput")
    def retry_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryDurationInput"))

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
    @jsii.member(jsii_name="retryDuration")
    def retry_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retryDuration"))

    @retry_duration.setter
    def retry_duration(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryDuration", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationOutputReference",
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

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions(
            enabled=enabled,
            log_group_name=log_group_name,
            log_stream_name=log_stream_name,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="putDataFormatConversionConfiguration")
    def put_data_format_conversion_configuration(
        self,
        *,
        input_format_configuration: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration, typing.Dict[str, typing.Any]],
        output_format_configuration: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration, typing.Dict[str, typing.Any]],
        schema_configuration: typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration, typing.Dict[str, typing.Any]],
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param input_format_configuration: input_format_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#input_format_configuration KinesisFirehoseDeliveryStream#input_format_configuration}
        :param output_format_configuration: output_format_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#output_format_configuration KinesisFirehoseDeliveryStream#output_format_configuration}
        :param schema_configuration: schema_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#schema_configuration KinesisFirehoseDeliveryStream#schema_configuration}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration(
            input_format_configuration=input_format_configuration,
            output_format_configuration=output_format_configuration,
            schema_configuration=schema_configuration,
            enabled=enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putDataFormatConversionConfiguration", [value]))

    @jsii.member(jsii_name="putDynamicPartitioningConfiguration")
    def put_dynamic_partitioning_configuration(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration(
            enabled=enabled, retry_duration=retry_duration
        )

        return typing.cast(None, jsii.invoke(self, "putDynamicPartitioningConfiguration", [value]))

    @jsii.member(jsii_name="putProcessingConfiguration")
    def put_processing_configuration(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        processors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration(
            enabled=enabled, processors=processors
        )

        return typing.cast(None, jsii.invoke(self, "putProcessingConfiguration", [value]))

    @jsii.member(jsii_name="putS3BackupConfiguration")
    def put_s3_backup_configuration(
        self,
        *,
        bucket_arn: builtins.str,
        role_arn: builtins.str,
        buffer_interval: typing.Optional[jsii.Number] = None,
        buffer_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions", typing.Dict[str, typing.Any]]] = None,
        compression_format: typing.Optional[builtins.str] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffer_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.
        :param buffer_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param compression_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.
        :param error_output_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration(
            bucket_arn=bucket_arn,
            role_arn=role_arn,
            buffer_interval=buffer_interval,
            buffer_size=buffer_size,
            cloudwatch_logging_options=cloudwatch_logging_options,
            compression_format=compression_format,
            error_output_prefix=error_output_prefix,
            kms_key_arn=kms_key_arn,
            prefix=prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putS3BackupConfiguration", [value]))

    @jsii.member(jsii_name="resetBufferInterval")
    def reset_buffer_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferInterval", []))

    @jsii.member(jsii_name="resetBufferSize")
    def reset_buffer_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferSize", []))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetCompressionFormat")
    def reset_compression_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressionFormat", []))

    @jsii.member(jsii_name="resetDataFormatConversionConfiguration")
    def reset_data_format_conversion_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataFormatConversionConfiguration", []))

    @jsii.member(jsii_name="resetDynamicPartitioningConfiguration")
    def reset_dynamic_partitioning_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamicPartitioningConfiguration", []))

    @jsii.member(jsii_name="resetErrorOutputPrefix")
    def reset_error_output_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorOutputPrefix", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetProcessingConfiguration")
    def reset_processing_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessingConfiguration", []))

    @jsii.member(jsii_name="resetS3BackupConfiguration")
    def reset_s3_backup_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BackupConfiguration", []))

    @jsii.member(jsii_name="resetS3BackupMode")
    def reset_s3_backup_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BackupMode", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsOutputReference, jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="dataFormatConversionConfiguration")
    def data_format_conversion_configuration(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputReference, jsii.get(self, "dataFormatConversionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="dynamicPartitioningConfiguration")
    def dynamic_partitioning_configuration(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfigurationOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfigurationOutputReference, jsii.get(self, "dynamicPartitioningConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationOutputReference", jsii.get(self, "processingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="s3BackupConfiguration")
    def s3_backup_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationOutputReference", jsii.get(self, "s3BackupConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="bucketArnInput")
    def bucket_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferIntervalInput")
    def buffer_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferSizeInput")
    def buffer_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionFormatInput")
    def compression_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFormatConversionConfigurationInput")
    def data_format_conversion_configuration_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration], jsii.get(self, "dataFormatConversionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamicPartitioningConfigurationInput")
    def dynamic_partitioning_configuration_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration], jsii.get(self, "dynamicPartitioningConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="errorOutputPrefixInput")
    def error_output_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorOutputPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="processingConfigurationInput")
    def processing_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration"], jsii.get(self, "processingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BackupConfigurationInput")
    def s3_backup_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration"], jsii.get(self, "s3BackupConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BackupModeInput")
    def s3_backup_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BackupModeInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketArn")
    def bucket_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketArn"))

    @bucket_arn.setter
    def bucket_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="bufferInterval")
    def buffer_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferInterval"))

    @buffer_interval.setter
    def buffer_interval(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferInterval", value)

    @builtins.property
    @jsii.member(jsii_name="bufferSize")
    def buffer_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferSize"))

    @buffer_size.setter
    def buffer_size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferSize", value)

    @builtins.property
    @jsii.member(jsii_name="compressionFormat")
    def compression_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compressionFormat"))

    @compression_format.setter
    def compression_format(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressionFormat", value)

    @builtins.property
    @jsii.member(jsii_name="errorOutputPrefix")
    def error_output_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorOutputPrefix"))

    @error_output_prefix.setter
    def error_output_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorOutputPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

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
    @jsii.member(jsii_name="s3BackupMode")
    def s3_backup_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3BackupMode"))

    @s3_backup_mode.setter
    def s3_backup_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BackupMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3Configuration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3Configuration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3Configuration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3Configuration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "processors": "processors"},
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        processors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                processors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument processors", value=processors, expected_type=type_hints["processors"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if processors is not None:
            self._values["processors"] = processors

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def processors(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors"]]]:
        '''processors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        result = self._values.get("processors")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationOutputReference",
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

    @jsii.member(jsii_name="putProcessors")
    def put_processors(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProcessors", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetProcessors")
    def reset_processors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessors", []))

    @builtins.property
    @jsii.member(jsii_name="processors")
    def processors(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsList":
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsList", jsii.get(self, "processors"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="processorsInput")
    def processors_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors"]]], jsii.get(self, "processorsInput"))

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
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "parameters": "parameters"},
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors:
    def __init__(
        self,
        *,
        type: builtins.str,
        parameters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                parameters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters"]]]:
        '''parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsList",
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
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsOutputReference",
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

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersList":
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersList", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters"]]], jsii.get(self, "parametersInput"))

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
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "parameter_name": "parameterName",
        "parameter_value": "parameterValue",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters:
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        parameter_value: builtins.str,
    ) -> None:
        '''
        :param parameter_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.
        :param parameter_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.
        '''
        if __debug__:
            def stub(
                *,
                parameter_name: builtins.str,
                parameter_value: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
        self._values: typing.Dict[str, typing.Any] = {
            "parameter_name": parameter_name,
            "parameter_value": parameter_value,
        }

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.'''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.'''
        result = self._values.get("parameter_value")
        assert result is not None, "Required property 'parameter_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersList",
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
    ) -> "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersOutputReference",
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
    @jsii.member(jsii_name="parameterNameInput")
    def parameter_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterValueInput")
    def parameter_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterValueInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @parameter_name.setter
    def parameter_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterName", value)

    @builtins.property
    @jsii.member(jsii_name="parameterValue")
    def parameter_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterValue"))

    @parameter_value.setter
    def parameter_value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_arn": "bucketArn",
        "role_arn": "roleArn",
        "buffer_interval": "bufferInterval",
        "buffer_size": "bufferSize",
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "compression_format": "compressionFormat",
        "error_output_prefix": "errorOutputPrefix",
        "kms_key_arn": "kmsKeyArn",
        "prefix": "prefix",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration:
    def __init__(
        self,
        *,
        bucket_arn: builtins.str,
        role_arn: builtins.str,
        buffer_interval: typing.Optional[jsii.Number] = None,
        buffer_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions", typing.Dict[str, typing.Any]]] = None,
        compression_format: typing.Optional[builtins.str] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffer_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.
        :param buffer_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param compression_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.
        :param error_output_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.
        '''
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if __debug__:
            def stub(
                *,
                bucket_arn: builtins.str,
                role_arn: builtins.str,
                buffer_interval: typing.Optional[jsii.Number] = None,
                buffer_size: typing.Optional[jsii.Number] = None,
                cloudwatch_logging_options: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions, typing.Dict[str, typing.Any]]] = None,
                compression_format: typing.Optional[builtins.str] = None,
                error_output_prefix: typing.Optional[builtins.str] = None,
                kms_key_arn: typing.Optional[builtins.str] = None,
                prefix: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument buffer_interval", value=buffer_interval, expected_type=type_hints["buffer_interval"])
            check_type(argname="argument buffer_size", value=buffer_size, expected_type=type_hints["buffer_size"])
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument compression_format", value=compression_format, expected_type=type_hints["compression_format"])
            check_type(argname="argument error_output_prefix", value=error_output_prefix, expected_type=type_hints["error_output_prefix"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_arn": bucket_arn,
            "role_arn": role_arn,
        }
        if buffer_interval is not None:
            self._values["buffer_interval"] = buffer_interval
        if buffer_size is not None:
            self._values["buffer_size"] = buffer_size
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if compression_format is not None:
            self._values["compression_format"] = compression_format
        if error_output_prefix is not None:
            self._values["error_output_prefix"] = error_output_prefix
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def buffer_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.'''
        result = self._values.get("buffer_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def buffer_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.'''
        result = self._values.get("buffer_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions"]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions"], result)

    @builtins.property
    def compression_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.'''
        result = self._values.get("compression_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_output_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.'''
        result = self._values.get("error_output_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                log_group_name: typing.Optional[builtins.str] = None,
                log_stream_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.'''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.'''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference",
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

    @jsii.member(jsii_name="resetLogGroupName")
    def reset_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupName", []))

    @jsii.member(jsii_name="resetLogStreamName")
    def reset_log_stream_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreamName", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamNameInput")
    def log_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamNameInput"))

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
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))

    @log_stream_name.setter
    def log_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationOutputReference",
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

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        value = KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions(
            enabled=enabled,
            log_group_name=log_group_name,
            log_stream_name=log_stream_name,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="resetBufferInterval")
    def reset_buffer_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferInterval", []))

    @jsii.member(jsii_name="resetBufferSize")
    def reset_buffer_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferSize", []))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetCompressionFormat")
    def reset_compression_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressionFormat", []))

    @jsii.member(jsii_name="resetErrorOutputPrefix")
    def reset_error_output_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorOutputPrefix", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference, jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="bucketArnInput")
    def bucket_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferIntervalInput")
    def buffer_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferSizeInput")
    def buffer_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionFormatInput")
    def compression_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="errorOutputPrefixInput")
    def error_output_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorOutputPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketArn")
    def bucket_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketArn"))

    @bucket_arn.setter
    def bucket_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="bufferInterval")
    def buffer_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferInterval"))

    @buffer_interval.setter
    def buffer_interval(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferInterval", value)

    @builtins.property
    @jsii.member(jsii_name="bufferSize")
    def buffer_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferSize"))

    @buffer_size.setter
    def buffer_size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferSize", value)

    @builtins.property
    @jsii.member(jsii_name="compressionFormat")
    def compression_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compressionFormat"))

    @compression_format.setter
    def compression_format(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressionFormat", value)

    @builtins.property
    @jsii.member(jsii_name="errorOutputPrefix")
    def error_output_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorOutputPrefix"))

    @error_output_prefix.setter
    def error_output_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorOutputPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "access_key": "accessKey",
        "buffering_interval": "bufferingInterval",
        "buffering_size": "bufferingSize",
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "name": "name",
        "processing_configuration": "processingConfiguration",
        "request_configuration": "requestConfiguration",
        "retry_duration": "retryDuration",
        "role_arn": "roleArn",
        "s3_backup_mode": "s3BackupMode",
    },
)
class KinesisFirehoseDeliveryStreamHttpEndpointConfiguration:
    def __init__(
        self,
        *,
        url: builtins.str,
        access_key: typing.Optional[builtins.str] = None,
        buffering_interval: typing.Optional[jsii.Number] = None,
        buffering_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions", typing.Dict[str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration", typing.Dict[str, typing.Any]]] = None,
        request_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration", typing.Dict[str, typing.Any]]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
        role_arn: typing.Optional[builtins.str] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#url KinesisFirehoseDeliveryStream#url}.
        :param access_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#access_key KinesisFirehoseDeliveryStream#access_key}.
        :param buffering_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_interval KinesisFirehoseDeliveryStream#buffering_interval}.
        :param buffering_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_size KinesisFirehoseDeliveryStream#buffering_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#name KinesisFirehoseDeliveryStream#name}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param request_configuration: request_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#request_configuration KinesisFirehoseDeliveryStream#request_configuration}
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        '''
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if isinstance(processing_configuration, dict):
            processing_configuration = KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration(**processing_configuration)
        if isinstance(request_configuration, dict):
            request_configuration = KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration(**request_configuration)
        if __debug__:
            def stub(
                *,
                url: builtins.str,
                access_key: typing.Optional[builtins.str] = None,
                buffering_interval: typing.Optional[jsii.Number] = None,
                buffering_size: typing.Optional[jsii.Number] = None,
                cloudwatch_logging_options: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions, typing.Dict[str, typing.Any]]] = None,
                name: typing.Optional[builtins.str] = None,
                processing_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration, typing.Dict[str, typing.Any]]] = None,
                request_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration, typing.Dict[str, typing.Any]]] = None,
                retry_duration: typing.Optional[jsii.Number] = None,
                role_arn: typing.Optional[builtins.str] = None,
                s3_backup_mode: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument access_key", value=access_key, expected_type=type_hints["access_key"])
            check_type(argname="argument buffering_interval", value=buffering_interval, expected_type=type_hints["buffering_interval"])
            check_type(argname="argument buffering_size", value=buffering_size, expected_type=type_hints["buffering_size"])
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
            check_type(argname="argument request_configuration", value=request_configuration, expected_type=type_hints["request_configuration"])
            check_type(argname="argument retry_duration", value=retry_duration, expected_type=type_hints["retry_duration"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "url": url,
        }
        if access_key is not None:
            self._values["access_key"] = access_key
        if buffering_interval is not None:
            self._values["buffering_interval"] = buffering_interval
        if buffering_size is not None:
            self._values["buffering_size"] = buffering_size
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if name is not None:
            self._values["name"] = name
        if processing_configuration is not None:
            self._values["processing_configuration"] = processing_configuration
        if request_configuration is not None:
            self._values["request_configuration"] = request_configuration
        if retry_duration is not None:
            self._values["retry_duration"] = retry_duration
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if s3_backup_mode is not None:
            self._values["s3_backup_mode"] = s3_backup_mode

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#url KinesisFirehoseDeliveryStream#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#access_key KinesisFirehoseDeliveryStream#access_key}.'''
        result = self._values.get("access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def buffering_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_interval KinesisFirehoseDeliveryStream#buffering_interval}.'''
        result = self._values.get("buffering_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def buffering_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffering_size KinesisFirehoseDeliveryStream#buffering_size}.'''
        result = self._values.get("buffering_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions"]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#name KinesisFirehoseDeliveryStream#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def processing_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration"]:
        '''processing_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        '''
        result = self._values.get("processing_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration"], result)

    @builtins.property
    def request_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration"]:
        '''request_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#request_configuration KinesisFirehoseDeliveryStream#request_configuration}
        '''
        result = self._values.get("request_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration"], result)

    @builtins.property
    def retry_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.'''
        result = self._values.get("retry_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_backup_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.'''
        result = self._values.get("s3_backup_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamHttpEndpointConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                log_group_name: typing.Optional[builtins.str] = None,
                log_stream_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.'''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.'''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptionsOutputReference",
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

    @jsii.member(jsii_name="resetLogGroupName")
    def reset_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupName", []))

    @jsii.member(jsii_name="resetLogStreamName")
    def reset_log_stream_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreamName", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamNameInput")
    def log_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamNameInput"))

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
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))

    @log_stream_name.setter
    def log_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationOutputReference",
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

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        value = KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions(
            enabled=enabled,
            log_group_name=log_group_name,
            log_stream_name=log_stream_name,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="putProcessingConfiguration")
    def put_processing_configuration(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        processors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        value = KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration(
            enabled=enabled, processors=processors
        )

        return typing.cast(None, jsii.invoke(self, "putProcessingConfiguration", [value]))

    @jsii.member(jsii_name="putRequestConfiguration")
    def put_request_configuration(
        self,
        *,
        common_attributes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes", typing.Dict[str, typing.Any]]]]] = None,
        content_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param common_attributes: common_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#common_attributes KinesisFirehoseDeliveryStream#common_attributes}
        :param content_encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#content_encoding KinesisFirehoseDeliveryStream#content_encoding}.
        '''
        value = KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration(
            common_attributes=common_attributes, content_encoding=content_encoding
        )

        return typing.cast(None, jsii.invoke(self, "putRequestConfiguration", [value]))

    @jsii.member(jsii_name="resetAccessKey")
    def reset_access_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessKey", []))

    @jsii.member(jsii_name="resetBufferingInterval")
    def reset_buffering_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferingInterval", []))

    @jsii.member(jsii_name="resetBufferingSize")
    def reset_buffering_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferingSize", []))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetProcessingConfiguration")
    def reset_processing_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessingConfiguration", []))

    @jsii.member(jsii_name="resetRequestConfiguration")
    def reset_request_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestConfiguration", []))

    @jsii.member(jsii_name="resetRetryDuration")
    def reset_retry_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryDuration", []))

    @jsii.member(jsii_name="resetRoleArn")
    def reset_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleArn", []))

    @jsii.member(jsii_name="resetS3BackupMode")
    def reset_s3_backup_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BackupMode", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptionsOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptionsOutputReference, jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationOutputReference", jsii.get(self, "processingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="requestConfiguration")
    def request_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationOutputReference", jsii.get(self, "requestConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="accessKeyInput")
    def access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferingIntervalInput")
    def buffering_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferingSizeInput")
    def buffering_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferingSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="processingConfigurationInput")
    def processing_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration"], jsii.get(self, "processingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="requestConfigurationInput")
    def request_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration"], jsii.get(self, "requestConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="retryDurationInput")
    def retry_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BackupModeInput")
    def s3_backup_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BackupModeInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKey")
    def access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessKey"))

    @access_key.setter
    def access_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKey", value)

    @builtins.property
    @jsii.member(jsii_name="bufferingInterval")
    def buffering_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferingInterval"))

    @buffering_interval.setter
    def buffering_interval(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="bufferingSize")
    def buffering_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferingSize"))

    @buffering_size.setter
    def buffering_size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferingSize", value)

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
    @jsii.member(jsii_name="retryDuration")
    def retry_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retryDuration"))

    @retry_duration.setter
    def retry_duration(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryDuration", value)

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
    @jsii.member(jsii_name="s3BackupMode")
    def s3_backup_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3BackupMode"))

    @s3_backup_mode.setter
    def s3_backup_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BackupMode", value)

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "processors": "processors"},
)
class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        processors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                processors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument processors", value=processors, expected_type=type_hints["processors"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if processors is not None:
            self._values["processors"] = processors

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def processors(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors"]]]:
        '''processors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        result = self._values.get("processors")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationOutputReference",
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

    @jsii.member(jsii_name="putProcessors")
    def put_processors(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProcessors", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetProcessors")
    def reset_processors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessors", []))

    @builtins.property
    @jsii.member(jsii_name="processors")
    def processors(
        self,
    ) -> "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsList":
        return typing.cast("KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsList", jsii.get(self, "processors"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="processorsInput")
    def processors_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors"]]], jsii.get(self, "processorsInput"))

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
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "parameters": "parameters"},
)
class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors:
    def __init__(
        self,
        *,
        type: builtins.str,
        parameters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                parameters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters"]]]:
        '''parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsList",
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
    ) -> "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsOutputReference",
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

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersList":
        return typing.cast("KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersList", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters"]]], jsii.get(self, "parametersInput"))

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
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "parameter_name": "parameterName",
        "parameter_value": "parameterValue",
    },
)
class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters:
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        parameter_value: builtins.str,
    ) -> None:
        '''
        :param parameter_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.
        :param parameter_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.
        '''
        if __debug__:
            def stub(
                *,
                parameter_name: builtins.str,
                parameter_value: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
        self._values: typing.Dict[str, typing.Any] = {
            "parameter_name": parameter_name,
            "parameter_value": parameter_value,
        }

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.'''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.'''
        result = self._values.get("parameter_value")
        assert result is not None, "Required property 'parameter_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersList",
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
    ) -> "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersOutputReference",
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
    @jsii.member(jsii_name="parameterNameInput")
    def parameter_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterValueInput")
    def parameter_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterValueInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @parameter_name.setter
    def parameter_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterName", value)

    @builtins.property
    @jsii.member(jsii_name="parameterValue")
    def parameter_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterValue"))

    @parameter_value.setter
    def parameter_value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "common_attributes": "commonAttributes",
        "content_encoding": "contentEncoding",
    },
)
class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration:
    def __init__(
        self,
        *,
        common_attributes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes", typing.Dict[str, typing.Any]]]]] = None,
        content_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param common_attributes: common_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#common_attributes KinesisFirehoseDeliveryStream#common_attributes}
        :param content_encoding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#content_encoding KinesisFirehoseDeliveryStream#content_encoding}.
        '''
        if __debug__:
            def stub(
                *,
                common_attributes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes, typing.Dict[str, typing.Any]]]]] = None,
                content_encoding: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument common_attributes", value=common_attributes, expected_type=type_hints["common_attributes"])
            check_type(argname="argument content_encoding", value=content_encoding, expected_type=type_hints["content_encoding"])
        self._values: typing.Dict[str, typing.Any] = {}
        if common_attributes is not None:
            self._values["common_attributes"] = common_attributes
        if content_encoding is not None:
            self._values["content_encoding"] = content_encoding

    @builtins.property
    def common_attributes(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes"]]]:
        '''common_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#common_attributes KinesisFirehoseDeliveryStream#common_attributes}
        '''
        result = self._values.get("common_attributes")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes"]]], result)

    @builtins.property
    def content_encoding(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#content_encoding KinesisFirehoseDeliveryStream#content_encoding}.'''
        result = self._values.get("content_encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#name KinesisFirehoseDeliveryStream#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#value KinesisFirehoseDeliveryStream#value}.
        '''
        if __debug__:
            def stub(*, name: builtins.str, value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#name KinesisFirehoseDeliveryStream#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#value KinesisFirehoseDeliveryStream#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesList",
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
    ) -> "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesOutputReference",
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
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

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
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationOutputReference",
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

    @jsii.member(jsii_name="putCommonAttributes")
    def put_common_attributes(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCommonAttributes", [value]))

    @jsii.member(jsii_name="resetCommonAttributes")
    def reset_common_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommonAttributes", []))

    @jsii.member(jsii_name="resetContentEncoding")
    def reset_content_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentEncoding", []))

    @builtins.property
    @jsii.member(jsii_name="commonAttributes")
    def common_attributes(
        self,
    ) -> KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesList:
        return typing.cast(KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesList, jsii.get(self, "commonAttributes"))

    @builtins.property
    @jsii.member(jsii_name="commonAttributesInput")
    def common_attributes_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes]]], jsii.get(self, "commonAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="contentEncodingInput")
    def content_encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentEncodingInput"))

    @builtins.property
    @jsii.member(jsii_name="contentEncoding")
    def content_encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentEncoding"))

    @content_encoding.setter
    def content_encoding(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentEncoding", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamKinesisSourceConfiguration",
    jsii_struct_bases=[],
    name_mapping={"kinesis_stream_arn": "kinesisStreamArn", "role_arn": "roleArn"},
)
class KinesisFirehoseDeliveryStreamKinesisSourceConfiguration:
    def __init__(
        self,
        *,
        kinesis_stream_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param kinesis_stream_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kinesis_stream_arn KinesisFirehoseDeliveryStream#kinesis_stream_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        '''
        if __debug__:
            def stub(
                *,
                kinesis_stream_arn: builtins.str,
                role_arn: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument kinesis_stream_arn", value=kinesis_stream_arn, expected_type=type_hints["kinesis_stream_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "kinesis_stream_arn": kinesis_stream_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def kinesis_stream_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kinesis_stream_arn KinesisFirehoseDeliveryStream#kinesis_stream_arn}.'''
        result = self._values.get("kinesis_stream_arn")
        assert result is not None, "Required property 'kinesis_stream_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamKinesisSourceConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamKinesisSourceConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamKinesisSourceConfigurationOutputReference",
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
    @jsii.member(jsii_name="kinesisStreamArnInput")
    def kinesis_stream_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kinesisStreamArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisStreamArn")
    def kinesis_stream_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kinesisStreamArn"))

    @kinesis_stream_arn.setter
    def kinesis_stream_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kinesisStreamArn", value)

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamKinesisSourceConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamKinesisSourceConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamKinesisSourceConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamKinesisSourceConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_jdbcurl": "clusterJdbcurl",
        "data_table_name": "dataTableName",
        "password": "password",
        "role_arn": "roleArn",
        "username": "username",
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "copy_options": "copyOptions",
        "data_table_columns": "dataTableColumns",
        "processing_configuration": "processingConfiguration",
        "retry_duration": "retryDuration",
        "s3_backup_configuration": "s3BackupConfiguration",
        "s3_backup_mode": "s3BackupMode",
    },
)
class KinesisFirehoseDeliveryStreamRedshiftConfiguration:
    def __init__(
        self,
        *,
        cluster_jdbcurl: builtins.str,
        data_table_name: builtins.str,
        password: builtins.str,
        role_arn: builtins.str,
        username: builtins.str,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions", typing.Dict[str, typing.Any]]] = None,
        copy_options: typing.Optional[builtins.str] = None,
        data_table_columns: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration", typing.Dict[str, typing.Any]]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
        s3_backup_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration", typing.Dict[str, typing.Any]]] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cluster_jdbcurl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cluster_jdbcurl KinesisFirehoseDeliveryStream#cluster_jdbcurl}.
        :param data_table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#data_table_name KinesisFirehoseDeliveryStream#data_table_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#password KinesisFirehoseDeliveryStream#password}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#username KinesisFirehoseDeliveryStream#username}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param copy_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#copy_options KinesisFirehoseDeliveryStream#copy_options}.
        :param data_table_columns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#data_table_columns KinesisFirehoseDeliveryStream#data_table_columns}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        :param s3_backup_configuration: s3_backup_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_configuration KinesisFirehoseDeliveryStream#s3_backup_configuration}
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        '''
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if isinstance(processing_configuration, dict):
            processing_configuration = KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration(**processing_configuration)
        if isinstance(s3_backup_configuration, dict):
            s3_backup_configuration = KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration(**s3_backup_configuration)
        if __debug__:
            def stub(
                *,
                cluster_jdbcurl: builtins.str,
                data_table_name: builtins.str,
                password: builtins.str,
                role_arn: builtins.str,
                username: builtins.str,
                cloudwatch_logging_options: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions, typing.Dict[str, typing.Any]]] = None,
                copy_options: typing.Optional[builtins.str] = None,
                data_table_columns: typing.Optional[builtins.str] = None,
                processing_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration, typing.Dict[str, typing.Any]]] = None,
                retry_duration: typing.Optional[jsii.Number] = None,
                s3_backup_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration, typing.Dict[str, typing.Any]]] = None,
                s3_backup_mode: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cluster_jdbcurl", value=cluster_jdbcurl, expected_type=type_hints["cluster_jdbcurl"])
            check_type(argname="argument data_table_name", value=data_table_name, expected_type=type_hints["data_table_name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument copy_options", value=copy_options, expected_type=type_hints["copy_options"])
            check_type(argname="argument data_table_columns", value=data_table_columns, expected_type=type_hints["data_table_columns"])
            check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
            check_type(argname="argument retry_duration", value=retry_duration, expected_type=type_hints["retry_duration"])
            check_type(argname="argument s3_backup_configuration", value=s3_backup_configuration, expected_type=type_hints["s3_backup_configuration"])
            check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_jdbcurl": cluster_jdbcurl,
            "data_table_name": data_table_name,
            "password": password,
            "role_arn": role_arn,
            "username": username,
        }
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if copy_options is not None:
            self._values["copy_options"] = copy_options
        if data_table_columns is not None:
            self._values["data_table_columns"] = data_table_columns
        if processing_configuration is not None:
            self._values["processing_configuration"] = processing_configuration
        if retry_duration is not None:
            self._values["retry_duration"] = retry_duration
        if s3_backup_configuration is not None:
            self._values["s3_backup_configuration"] = s3_backup_configuration
        if s3_backup_mode is not None:
            self._values["s3_backup_mode"] = s3_backup_mode

    @builtins.property
    def cluster_jdbcurl(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cluster_jdbcurl KinesisFirehoseDeliveryStream#cluster_jdbcurl}.'''
        result = self._values.get("cluster_jdbcurl")
        assert result is not None, "Required property 'cluster_jdbcurl' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#data_table_name KinesisFirehoseDeliveryStream#data_table_name}.'''
        result = self._values.get("data_table_name")
        assert result is not None, "Required property 'data_table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#password KinesisFirehoseDeliveryStream#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#username KinesisFirehoseDeliveryStream#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions"]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions"], result)

    @builtins.property
    def copy_options(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#copy_options KinesisFirehoseDeliveryStream#copy_options}.'''
        result = self._values.get("copy_options")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_table_columns(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#data_table_columns KinesisFirehoseDeliveryStream#data_table_columns}.'''
        result = self._values.get("data_table_columns")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def processing_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration"]:
        '''processing_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        '''
        result = self._values.get("processing_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration"], result)

    @builtins.property
    def retry_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.'''
        result = self._values.get("retry_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def s3_backup_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration"]:
        '''s3_backup_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_configuration KinesisFirehoseDeliveryStream#s3_backup_configuration}
        '''
        result = self._values.get("s3_backup_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration"], result)

    @builtins.property
    def s3_backup_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.'''
        result = self._values.get("s3_backup_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamRedshiftConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                log_group_name: typing.Optional[builtins.str] = None,
                log_stream_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.'''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.'''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsOutputReference",
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

    @jsii.member(jsii_name="resetLogGroupName")
    def reset_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupName", []))

    @jsii.member(jsii_name="resetLogStreamName")
    def reset_log_stream_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreamName", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamNameInput")
    def log_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamNameInput"))

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
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))

    @log_stream_name.setter
    def log_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamRedshiftConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationOutputReference",
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

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        value = KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions(
            enabled=enabled,
            log_group_name=log_group_name,
            log_stream_name=log_stream_name,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="putProcessingConfiguration")
    def put_processing_configuration(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        processors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        value = KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration(
            enabled=enabled, processors=processors
        )

        return typing.cast(None, jsii.invoke(self, "putProcessingConfiguration", [value]))

    @jsii.member(jsii_name="putS3BackupConfiguration")
    def put_s3_backup_configuration(
        self,
        *,
        bucket_arn: builtins.str,
        role_arn: builtins.str,
        buffer_interval: typing.Optional[jsii.Number] = None,
        buffer_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions", typing.Dict[str, typing.Any]]] = None,
        compression_format: typing.Optional[builtins.str] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffer_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.
        :param buffer_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param compression_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.
        :param error_output_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.
        '''
        value = KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration(
            bucket_arn=bucket_arn,
            role_arn=role_arn,
            buffer_interval=buffer_interval,
            buffer_size=buffer_size,
            cloudwatch_logging_options=cloudwatch_logging_options,
            compression_format=compression_format,
            error_output_prefix=error_output_prefix,
            kms_key_arn=kms_key_arn,
            prefix=prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putS3BackupConfiguration", [value]))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetCopyOptions")
    def reset_copy_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyOptions", []))

    @jsii.member(jsii_name="resetDataTableColumns")
    def reset_data_table_columns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataTableColumns", []))

    @jsii.member(jsii_name="resetProcessingConfiguration")
    def reset_processing_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessingConfiguration", []))

    @jsii.member(jsii_name="resetRetryDuration")
    def reset_retry_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryDuration", []))

    @jsii.member(jsii_name="resetS3BackupConfiguration")
    def reset_s3_backup_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BackupConfiguration", []))

    @jsii.member(jsii_name="resetS3BackupMode")
    def reset_s3_backup_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BackupMode", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsOutputReference, jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationOutputReference", jsii.get(self, "processingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="s3BackupConfiguration")
    def s3_backup_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationOutputReference", jsii.get(self, "s3BackupConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterJdbcurlInput")
    def cluster_jdbcurl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterJdbcurlInput"))

    @builtins.property
    @jsii.member(jsii_name="copyOptionsInput")
    def copy_options_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "copyOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTableColumnsInput")
    def data_table_columns_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTableColumnsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataTableNameInput")
    def data_table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataTableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="processingConfigurationInput")
    def processing_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration"], jsii.get(self, "processingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="retryDurationInput")
    def retry_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BackupConfigurationInput")
    def s3_backup_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration"], jsii.get(self, "s3BackupConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BackupModeInput")
    def s3_backup_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BackupModeInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterJdbcurl")
    def cluster_jdbcurl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterJdbcurl"))

    @cluster_jdbcurl.setter
    def cluster_jdbcurl(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterJdbcurl", value)

    @builtins.property
    @jsii.member(jsii_name="copyOptions")
    def copy_options(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "copyOptions"))

    @copy_options.setter
    def copy_options(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyOptions", value)

    @builtins.property
    @jsii.member(jsii_name="dataTableColumns")
    def data_table_columns(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataTableColumns"))

    @data_table_columns.setter
    def data_table_columns(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataTableColumns", value)

    @builtins.property
    @jsii.member(jsii_name="dataTableName")
    def data_table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataTableName"))

    @data_table_name.setter
    def data_table_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataTableName", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="retryDuration")
    def retry_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retryDuration"))

    @retry_duration.setter
    def retry_duration(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryDuration", value)

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
    @jsii.member(jsii_name="s3BackupMode")
    def s3_backup_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3BackupMode"))

    @s3_backup_mode.setter
    def s3_backup_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BackupMode", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "processors": "processors"},
)
class KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        processors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                processors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument processors", value=processors, expected_type=type_hints["processors"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if processors is not None:
            self._values["processors"] = processors

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def processors(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors"]]]:
        '''processors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        result = self._values.get("processors")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationOutputReference",
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

    @jsii.member(jsii_name="putProcessors")
    def put_processors(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProcessors", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetProcessors")
    def reset_processors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessors", []))

    @builtins.property
    @jsii.member(jsii_name="processors")
    def processors(
        self,
    ) -> "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsList":
        return typing.cast("KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsList", jsii.get(self, "processors"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="processorsInput")
    def processors_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors"]]], jsii.get(self, "processorsInput"))

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
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "parameters": "parameters"},
)
class KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors:
    def __init__(
        self,
        *,
        type: builtins.str,
        parameters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                parameters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters"]]]:
        '''parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsList",
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
    ) -> "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsOutputReference",
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

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersList":
        return typing.cast("KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersList", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters"]]], jsii.get(self, "parametersInput"))

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
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "parameter_name": "parameterName",
        "parameter_value": "parameterValue",
    },
)
class KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters:
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        parameter_value: builtins.str,
    ) -> None:
        '''
        :param parameter_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.
        :param parameter_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.
        '''
        if __debug__:
            def stub(
                *,
                parameter_name: builtins.str,
                parameter_value: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
        self._values: typing.Dict[str, typing.Any] = {
            "parameter_name": parameter_name,
            "parameter_value": parameter_value,
        }

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.'''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.'''
        result = self._values.get("parameter_value")
        assert result is not None, "Required property 'parameter_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersList",
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
    ) -> "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersOutputReference",
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
    @jsii.member(jsii_name="parameterNameInput")
    def parameter_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterValueInput")
    def parameter_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterValueInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @parameter_name.setter
    def parameter_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterName", value)

    @builtins.property
    @jsii.member(jsii_name="parameterValue")
    def parameter_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterValue"))

    @parameter_value.setter
    def parameter_value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_arn": "bucketArn",
        "role_arn": "roleArn",
        "buffer_interval": "bufferInterval",
        "buffer_size": "bufferSize",
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "compression_format": "compressionFormat",
        "error_output_prefix": "errorOutputPrefix",
        "kms_key_arn": "kmsKeyArn",
        "prefix": "prefix",
    },
)
class KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration:
    def __init__(
        self,
        *,
        bucket_arn: builtins.str,
        role_arn: builtins.str,
        buffer_interval: typing.Optional[jsii.Number] = None,
        buffer_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions", typing.Dict[str, typing.Any]]] = None,
        compression_format: typing.Optional[builtins.str] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffer_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.
        :param buffer_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param compression_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.
        :param error_output_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.
        '''
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if __debug__:
            def stub(
                *,
                bucket_arn: builtins.str,
                role_arn: builtins.str,
                buffer_interval: typing.Optional[jsii.Number] = None,
                buffer_size: typing.Optional[jsii.Number] = None,
                cloudwatch_logging_options: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions, typing.Dict[str, typing.Any]]] = None,
                compression_format: typing.Optional[builtins.str] = None,
                error_output_prefix: typing.Optional[builtins.str] = None,
                kms_key_arn: typing.Optional[builtins.str] = None,
                prefix: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument buffer_interval", value=buffer_interval, expected_type=type_hints["buffer_interval"])
            check_type(argname="argument buffer_size", value=buffer_size, expected_type=type_hints["buffer_size"])
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument compression_format", value=compression_format, expected_type=type_hints["compression_format"])
            check_type(argname="argument error_output_prefix", value=error_output_prefix, expected_type=type_hints["error_output_prefix"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_arn": bucket_arn,
            "role_arn": role_arn,
        }
        if buffer_interval is not None:
            self._values["buffer_interval"] = buffer_interval
        if buffer_size is not None:
            self._values["buffer_size"] = buffer_size
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if compression_format is not None:
            self._values["compression_format"] = compression_format
        if error_output_prefix is not None:
            self._values["error_output_prefix"] = error_output_prefix
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def buffer_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.'''
        result = self._values.get("buffer_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def buffer_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.'''
        result = self._values.get("buffer_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions"]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions"], result)

    @builtins.property
    def compression_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.'''
        result = self._values.get("compression_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_output_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.'''
        result = self._values.get("error_output_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                log_group_name: typing.Optional[builtins.str] = None,
                log_stream_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.'''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.'''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference",
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

    @jsii.member(jsii_name="resetLogGroupName")
    def reset_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupName", []))

    @jsii.member(jsii_name="resetLogStreamName")
    def reset_log_stream_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreamName", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamNameInput")
    def log_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamNameInput"))

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
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))

    @log_stream_name.setter
    def log_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationOutputReference",
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

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        value = KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions(
            enabled=enabled,
            log_group_name=log_group_name,
            log_stream_name=log_stream_name,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="resetBufferInterval")
    def reset_buffer_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferInterval", []))

    @jsii.member(jsii_name="resetBufferSize")
    def reset_buffer_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferSize", []))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetCompressionFormat")
    def reset_compression_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressionFormat", []))

    @jsii.member(jsii_name="resetErrorOutputPrefix")
    def reset_error_output_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorOutputPrefix", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference, jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="bucketArnInput")
    def bucket_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferIntervalInput")
    def buffer_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferSizeInput")
    def buffer_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionFormatInput")
    def compression_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="errorOutputPrefixInput")
    def error_output_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorOutputPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketArn")
    def bucket_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketArn"))

    @bucket_arn.setter
    def bucket_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="bufferInterval")
    def buffer_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferInterval"))

    @buffer_interval.setter
    def buffer_interval(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferInterval", value)

    @builtins.property
    @jsii.member(jsii_name="bufferSize")
    def buffer_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferSize"))

    @buffer_size.setter
    def buffer_size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferSize", value)

    @builtins.property
    @jsii.member(jsii_name="compressionFormat")
    def compression_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compressionFormat"))

    @compression_format.setter
    def compression_format(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressionFormat", value)

    @builtins.property
    @jsii.member(jsii_name="errorOutputPrefix")
    def error_output_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorOutputPrefix"))

    @error_output_prefix.setter
    def error_output_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorOutputPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamS3Configuration",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_arn": "bucketArn",
        "role_arn": "roleArn",
        "buffer_interval": "bufferInterval",
        "buffer_size": "bufferSize",
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "compression_format": "compressionFormat",
        "error_output_prefix": "errorOutputPrefix",
        "kms_key_arn": "kmsKeyArn",
        "prefix": "prefix",
    },
)
class KinesisFirehoseDeliveryStreamS3Configuration:
    def __init__(
        self,
        *,
        bucket_arn: builtins.str,
        role_arn: builtins.str,
        buffer_interval: typing.Optional[jsii.Number] = None,
        buffer_size: typing.Optional[jsii.Number] = None,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions", typing.Dict[str, typing.Any]]] = None,
        compression_format: typing.Optional[builtins.str] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.
        :param buffer_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.
        :param buffer_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param compression_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.
        :param error_output_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.
        '''
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if __debug__:
            def stub(
                *,
                bucket_arn: builtins.str,
                role_arn: builtins.str,
                buffer_interval: typing.Optional[jsii.Number] = None,
                buffer_size: typing.Optional[jsii.Number] = None,
                cloudwatch_logging_options: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions, typing.Dict[str, typing.Any]]] = None,
                compression_format: typing.Optional[builtins.str] = None,
                error_output_prefix: typing.Optional[builtins.str] = None,
                kms_key_arn: typing.Optional[builtins.str] = None,
                prefix: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument buffer_interval", value=buffer_interval, expected_type=type_hints["buffer_interval"])
            check_type(argname="argument buffer_size", value=buffer_size, expected_type=type_hints["buffer_size"])
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument compression_format", value=compression_format, expected_type=type_hints["compression_format"])
            check_type(argname="argument error_output_prefix", value=error_output_prefix, expected_type=type_hints["error_output_prefix"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_arn": bucket_arn,
            "role_arn": role_arn,
        }
        if buffer_interval is not None:
            self._values["buffer_interval"] = buffer_interval
        if buffer_size is not None:
            self._values["buffer_size"] = buffer_size
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if compression_format is not None:
            self._values["compression_format"] = compression_format
        if error_output_prefix is not None:
            self._values["error_output_prefix"] = error_output_prefix
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#bucket_arn KinesisFirehoseDeliveryStream#bucket_arn}.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#role_arn KinesisFirehoseDeliveryStream#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def buffer_interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_interval KinesisFirehoseDeliveryStream#buffer_interval}.'''
        result = self._values.get("buffer_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def buffer_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#buffer_size KinesisFirehoseDeliveryStream#buffer_size}.'''
        result = self._values.get("buffer_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions"]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions"], result)

    @builtins.property
    def compression_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#compression_format KinesisFirehoseDeliveryStream#compression_format}.'''
        result = self._values.get("compression_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_output_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#error_output_prefix KinesisFirehoseDeliveryStream#error_output_prefix}.'''
        result = self._values.get("error_output_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#kms_key_arn KinesisFirehoseDeliveryStream#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#prefix KinesisFirehoseDeliveryStream#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamS3Configuration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                log_group_name: typing.Optional[builtins.str] = None,
                log_stream_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.'''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.'''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptionsOutputReference",
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

    @jsii.member(jsii_name="resetLogGroupName")
    def reset_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupName", []))

    @jsii.member(jsii_name="resetLogStreamName")
    def reset_log_stream_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreamName", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamNameInput")
    def log_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamNameInput"))

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
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))

    @log_stream_name.setter
    def log_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamS3ConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamS3ConfigurationOutputReference",
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

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        value = KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions(
            enabled=enabled,
            log_group_name=log_group_name,
            log_stream_name=log_stream_name,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="resetBufferInterval")
    def reset_buffer_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferInterval", []))

    @jsii.member(jsii_name="resetBufferSize")
    def reset_buffer_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBufferSize", []))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetCompressionFormat")
    def reset_compression_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressionFormat", []))

    @jsii.member(jsii_name="resetErrorOutputPrefix")
    def reset_error_output_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorOutputPrefix", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptionsOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptionsOutputReference, jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="bucketArnInput")
    def bucket_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferIntervalInput")
    def buffer_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="bufferSizeInput")
    def buffer_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bufferSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionFormatInput")
    def compression_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="errorOutputPrefixInput")
    def error_output_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorOutputPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketArn")
    def bucket_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketArn"))

    @bucket_arn.setter
    def bucket_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="bufferInterval")
    def buffer_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferInterval"))

    @buffer_interval.setter
    def buffer_interval(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferInterval", value)

    @builtins.property
    @jsii.member(jsii_name="bufferSize")
    def buffer_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bufferSize"))

    @buffer_size.setter
    def buffer_size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bufferSize", value)

    @builtins.property
    @jsii.member(jsii_name="compressionFormat")
    def compression_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compressionFormat"))

    @compression_format.setter
    def compression_format(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressionFormat", value)

    @builtins.property
    @jsii.member(jsii_name="errorOutputPrefix")
    def error_output_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorOutputPrefix"))

    @error_output_prefix.setter
    def error_output_prefix(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorOutputPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamS3Configuration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamS3Configuration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamS3Configuration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamS3Configuration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamServerSideEncryption",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "key_arn": "keyArn", "key_type": "keyType"},
)
class KinesisFirehoseDeliveryStreamServerSideEncryption:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key_arn: typing.Optional[builtins.str] = None,
        key_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#key_arn KinesisFirehoseDeliveryStream#key_arn}.
        :param key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#key_type KinesisFirehoseDeliveryStream#key_type}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                key_arn: typing.Optional[builtins.str] = None,
                key_type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
            check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if key_arn is not None:
            self._values["key_arn"] = key_arn
        if key_type is not None:
            self._values["key_type"] = key_type

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#key_arn KinesisFirehoseDeliveryStream#key_arn}.'''
        result = self._values.get("key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#key_type KinesisFirehoseDeliveryStream#key_type}.'''
        result = self._values.get("key_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamServerSideEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamServerSideEncryptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamServerSideEncryptionOutputReference",
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

    @jsii.member(jsii_name="resetKeyArn")
    def reset_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyArn", []))

    @jsii.member(jsii_name="resetKeyType")
    def reset_key_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyType", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="keyArnInput")
    def key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="keyTypeInput")
    def key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyTypeInput"))

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
    @jsii.member(jsii_name="keyArn")
    def key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyArn"))

    @key_arn.setter
    def key_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyArn", value)

    @builtins.property
    @jsii.member(jsii_name="keyType")
    def key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyType"))

    @key_type.setter
    def key_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamServerSideEncryption]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamServerSideEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamServerSideEncryption],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamServerSideEncryption],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "hec_endpoint": "hecEndpoint",
        "hec_token": "hecToken",
        "cloudwatch_logging_options": "cloudwatchLoggingOptions",
        "hec_acknowledgment_timeout": "hecAcknowledgmentTimeout",
        "hec_endpoint_type": "hecEndpointType",
        "processing_configuration": "processingConfiguration",
        "retry_duration": "retryDuration",
        "s3_backup_mode": "s3BackupMode",
    },
)
class KinesisFirehoseDeliveryStreamSplunkConfiguration:
    def __init__(
        self,
        *,
        hec_endpoint: builtins.str,
        hec_token: builtins.str,
        cloudwatch_logging_options: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions", typing.Dict[str, typing.Any]]] = None,
        hec_acknowledgment_timeout: typing.Optional[jsii.Number] = None,
        hec_endpoint_type: typing.Optional[builtins.str] = None,
        processing_configuration: typing.Optional[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration", typing.Dict[str, typing.Any]]] = None,
        retry_duration: typing.Optional[jsii.Number] = None,
        s3_backup_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hec_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_endpoint KinesisFirehoseDeliveryStream#hec_endpoint}.
        :param hec_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_token KinesisFirehoseDeliveryStream#hec_token}.
        :param cloudwatch_logging_options: cloudwatch_logging_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        :param hec_acknowledgment_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_acknowledgment_timeout KinesisFirehoseDeliveryStream#hec_acknowledgment_timeout}.
        :param hec_endpoint_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_endpoint_type KinesisFirehoseDeliveryStream#hec_endpoint_type}.
        :param processing_configuration: processing_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        :param retry_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.
        :param s3_backup_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.
        '''
        if isinstance(cloudwatch_logging_options, dict):
            cloudwatch_logging_options = KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions(**cloudwatch_logging_options)
        if isinstance(processing_configuration, dict):
            processing_configuration = KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration(**processing_configuration)
        if __debug__:
            def stub(
                *,
                hec_endpoint: builtins.str,
                hec_token: builtins.str,
                cloudwatch_logging_options: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions, typing.Dict[str, typing.Any]]] = None,
                hec_acknowledgment_timeout: typing.Optional[jsii.Number] = None,
                hec_endpoint_type: typing.Optional[builtins.str] = None,
                processing_configuration: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration, typing.Dict[str, typing.Any]]] = None,
                retry_duration: typing.Optional[jsii.Number] = None,
                s3_backup_mode: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument hec_endpoint", value=hec_endpoint, expected_type=type_hints["hec_endpoint"])
            check_type(argname="argument hec_token", value=hec_token, expected_type=type_hints["hec_token"])
            check_type(argname="argument cloudwatch_logging_options", value=cloudwatch_logging_options, expected_type=type_hints["cloudwatch_logging_options"])
            check_type(argname="argument hec_acknowledgment_timeout", value=hec_acknowledgment_timeout, expected_type=type_hints["hec_acknowledgment_timeout"])
            check_type(argname="argument hec_endpoint_type", value=hec_endpoint_type, expected_type=type_hints["hec_endpoint_type"])
            check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
            check_type(argname="argument retry_duration", value=retry_duration, expected_type=type_hints["retry_duration"])
            check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "hec_endpoint": hec_endpoint,
            "hec_token": hec_token,
        }
        if cloudwatch_logging_options is not None:
            self._values["cloudwatch_logging_options"] = cloudwatch_logging_options
        if hec_acknowledgment_timeout is not None:
            self._values["hec_acknowledgment_timeout"] = hec_acknowledgment_timeout
        if hec_endpoint_type is not None:
            self._values["hec_endpoint_type"] = hec_endpoint_type
        if processing_configuration is not None:
            self._values["processing_configuration"] = processing_configuration
        if retry_duration is not None:
            self._values["retry_duration"] = retry_duration
        if s3_backup_mode is not None:
            self._values["s3_backup_mode"] = s3_backup_mode

    @builtins.property
    def hec_endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_endpoint KinesisFirehoseDeliveryStream#hec_endpoint}.'''
        result = self._values.get("hec_endpoint")
        assert result is not None, "Required property 'hec_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hec_token(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_token KinesisFirehoseDeliveryStream#hec_token}.'''
        result = self._values.get("hec_token")
        assert result is not None, "Required property 'hec_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloudwatch_logging_options(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions"]:
        '''cloudwatch_logging_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#cloudwatch_logging_options KinesisFirehoseDeliveryStream#cloudwatch_logging_options}
        '''
        result = self._values.get("cloudwatch_logging_options")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions"], result)

    @builtins.property
    def hec_acknowledgment_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_acknowledgment_timeout KinesisFirehoseDeliveryStream#hec_acknowledgment_timeout}.'''
        result = self._values.get("hec_acknowledgment_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def hec_endpoint_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#hec_endpoint_type KinesisFirehoseDeliveryStream#hec_endpoint_type}.'''
        result = self._values.get("hec_endpoint_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def processing_configuration(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration"]:
        '''processing_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processing_configuration KinesisFirehoseDeliveryStream#processing_configuration}
        '''
        result = self._values.get("processing_configuration")
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration"], result)

    @builtins.property
    def retry_duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#retry_duration KinesisFirehoseDeliveryStream#retry_duration}.'''
        result = self._values.get("retry_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def s3_backup_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#s3_backup_mode KinesisFirehoseDeliveryStream#s3_backup_mode}.'''
        result = self._values.get("s3_backup_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamSplunkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                log_group_name: typing.Optional[builtins.str] = None,
                log_stream_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.'''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.'''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsOutputReference",
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

    @jsii.member(jsii_name="resetLogGroupName")
    def reset_log_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupName", []))

    @jsii.member(jsii_name="resetLogStreamName")
    def reset_log_stream_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreamName", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamNameInput")
    def log_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamNameInput"))

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
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))

    @log_stream_name.setter
    def log_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamSplunkConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationOutputReference",
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

    @jsii.member(jsii_name="putCloudwatchLoggingOptions")
    def put_cloudwatch_logging_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_group_name KinesisFirehoseDeliveryStream#log_group_name}.
        :param log_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#log_stream_name KinesisFirehoseDeliveryStream#log_stream_name}.
        '''
        value = KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions(
            enabled=enabled,
            log_group_name=log_group_name,
            log_stream_name=log_stream_name,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLoggingOptions", [value]))

    @jsii.member(jsii_name="putProcessingConfiguration")
    def put_processing_configuration(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        processors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        value = KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration(
            enabled=enabled, processors=processors
        )

        return typing.cast(None, jsii.invoke(self, "putProcessingConfiguration", [value]))

    @jsii.member(jsii_name="resetCloudwatchLoggingOptions")
    def reset_cloudwatch_logging_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLoggingOptions", []))

    @jsii.member(jsii_name="resetHecAcknowledgmentTimeout")
    def reset_hec_acknowledgment_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHecAcknowledgmentTimeout", []))

    @jsii.member(jsii_name="resetHecEndpointType")
    def reset_hec_endpoint_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHecEndpointType", []))

    @jsii.member(jsii_name="resetProcessingConfiguration")
    def reset_processing_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessingConfiguration", []))

    @jsii.member(jsii_name="resetRetryDuration")
    def reset_retry_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryDuration", []))

    @jsii.member(jsii_name="resetS3BackupMode")
    def reset_s3_backup_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BackupMode", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptions")
    def cloudwatch_logging_options(
        self,
    ) -> KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsOutputReference:
        return typing.cast(KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsOutputReference, jsii.get(self, "cloudwatchLoggingOptions"))

    @builtins.property
    @jsii.member(jsii_name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationOutputReference":
        return typing.cast("KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationOutputReference", jsii.get(self, "processingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLoggingOptionsInput")
    def cloudwatch_logging_options_input(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions], jsii.get(self, "cloudwatchLoggingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="hecAcknowledgmentTimeoutInput")
    def hec_acknowledgment_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hecAcknowledgmentTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="hecEndpointInput")
    def hec_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hecEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="hecEndpointTypeInput")
    def hec_endpoint_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hecEndpointTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="hecTokenInput")
    def hec_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hecTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="processingConfigurationInput")
    def processing_configuration_input(
        self,
    ) -> typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration"]:
        return typing.cast(typing.Optional["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration"], jsii.get(self, "processingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="retryDurationInput")
    def retry_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BackupModeInput")
    def s3_backup_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BackupModeInput"))

    @builtins.property
    @jsii.member(jsii_name="hecAcknowledgmentTimeout")
    def hec_acknowledgment_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hecAcknowledgmentTimeout"))

    @hec_acknowledgment_timeout.setter
    def hec_acknowledgment_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hecAcknowledgmentTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="hecEndpoint")
    def hec_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hecEndpoint"))

    @hec_endpoint.setter
    def hec_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hecEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="hecEndpointType")
    def hec_endpoint_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hecEndpointType"))

    @hec_endpoint_type.setter
    def hec_endpoint_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hecEndpointType", value)

    @builtins.property
    @jsii.member(jsii_name="hecToken")
    def hec_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hecToken"))

    @hec_token.setter
    def hec_token(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hecToken", value)

    @builtins.property
    @jsii.member(jsii_name="retryDuration")
    def retry_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retryDuration"))

    @retry_duration.setter
    def retry_duration(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryDuration", value)

    @builtins.property
    @jsii.member(jsii_name="s3BackupMode")
    def s3_backup_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3BackupMode"))

    @s3_backup_mode.setter
    def s3_backup_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BackupMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "processors": "processors"},
)
class KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        processors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.
        :param processors: processors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                processors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument processors", value=processors, expected_type=type_hints["processors"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if processors is not None:
            self._values["processors"] = processors

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#enabled KinesisFirehoseDeliveryStream#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def processors(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors"]]]:
        '''processors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#processors KinesisFirehoseDeliveryStream#processors}
        '''
        result = self._values.get("processors")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationOutputReference",
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

    @jsii.member(jsii_name="putProcessors")
    def put_processors(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProcessors", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetProcessors")
    def reset_processors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessors", []))

    @builtins.property
    @jsii.member(jsii_name="processors")
    def processors(
        self,
    ) -> "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsList":
        return typing.cast("KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsList", jsii.get(self, "processors"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="processorsInput")
    def processors_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors"]]], jsii.get(self, "processorsInput"))

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
    ) -> typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration]:
        return typing.cast(typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "parameters": "parameters"},
)
class KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors:
    def __init__(
        self,
        *,
        type: builtins.str,
        parameters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                parameters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#type KinesisFirehoseDeliveryStream#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters"]]]:
        '''parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameters KinesisFirehoseDeliveryStream#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsList",
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
    ) -> "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsOutputReference",
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

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersList":
        return typing.cast("KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersList", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters"]]], jsii.get(self, "parametersInput"))

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
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "parameter_name": "parameterName",
        "parameter_value": "parameterValue",
    },
)
class KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters:
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        parameter_value: builtins.str,
    ) -> None:
        '''
        :param parameter_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.
        :param parameter_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.
        '''
        if __debug__:
            def stub(
                *,
                parameter_name: builtins.str,
                parameter_value: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
        self._values: typing.Dict[str, typing.Any] = {
            "parameter_name": parameter_name,
            "parameter_value": parameter_value,
        }

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_name KinesisFirehoseDeliveryStream#parameter_name}.'''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/kinesis_firehose_delivery_stream#parameter_value KinesisFirehoseDeliveryStream#parameter_value}.'''
        result = self._values.get("parameter_value")
        assert result is not None, "Required property 'parameter_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersList",
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
    ) -> "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.kinesisFirehoseDeliveryStream.KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersOutputReference",
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
    @jsii.member(jsii_name="parameterNameInput")
    def parameter_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterValueInput")
    def parameter_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterValueInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterName"))

    @parameter_name.setter
    def parameter_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterName", value)

    @builtins.property
    @jsii.member(jsii_name="parameterValue")
    def parameter_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterValue"))

    @parameter_value.setter
    def parameter_value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KinesisFirehoseDeliveryStream",
    "KinesisFirehoseDeliveryStreamConfig",
    "KinesisFirehoseDeliveryStreamElasticsearchConfiguration",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsOutputReference",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessors",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsList",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsOutputReference",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParameters",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersList",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorsParametersOutputReference",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfig",
    "KinesisFirehoseDeliveryStreamElasticsearchConfigurationVpcConfigOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3Configuration",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfiguration",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationDynamicPartitioningConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessors",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsList",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParameters",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersList",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorsParametersOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference",
    "KinesisFirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfiguration",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptions",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationCloudwatchLoggingOptionsOutputReference",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfiguration",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessors",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsList",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsOutputReference",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParameters",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersList",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationProcessingConfigurationProcessorsParametersOutputReference",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfiguration",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributes",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesList",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationCommonAttributesOutputReference",
    "KinesisFirehoseDeliveryStreamHttpEndpointConfigurationRequestConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamKinesisSourceConfiguration",
    "KinesisFirehoseDeliveryStreamKinesisSourceConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamRedshiftConfiguration",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsOutputReference",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessors",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsList",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsOutputReference",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParameters",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersList",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorsParametersOutputReference",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutputReference",
    "KinesisFirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamS3Configuration",
    "KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions",
    "KinesisFirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptionsOutputReference",
    "KinesisFirehoseDeliveryStreamS3ConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamServerSideEncryption",
    "KinesisFirehoseDeliveryStreamServerSideEncryptionOutputReference",
    "KinesisFirehoseDeliveryStreamSplunkConfiguration",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsOutputReference",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationOutputReference",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessors",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsList",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsOutputReference",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParameters",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersList",
    "KinesisFirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorsParametersOutputReference",
]

publication.publish()
