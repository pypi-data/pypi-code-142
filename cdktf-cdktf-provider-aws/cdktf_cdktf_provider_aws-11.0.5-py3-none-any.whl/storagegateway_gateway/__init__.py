'''
# `aws_storagegateway_gateway`

Refer to the Terraform Registory for docs: [`aws_storagegateway_gateway`](https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway).
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


class StoragegatewayGateway(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.storagegatewayGateway.StoragegatewayGateway",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway aws_storagegateway_gateway}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        gateway_name: builtins.str,
        gateway_timezone: builtins.str,
        activation_key: typing.Optional[builtins.str] = None,
        average_download_rate_limit_in_bits_per_sec: typing.Optional[jsii.Number] = None,
        average_upload_rate_limit_in_bits_per_sec: typing.Optional[jsii.Number] = None,
        cloudwatch_log_group_arn: typing.Optional[builtins.str] = None,
        gateway_ip_address: typing.Optional[builtins.str] = None,
        gateway_type: typing.Optional[builtins.str] = None,
        gateway_vpc_endpoint: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        maintenance_start_time: typing.Optional[typing.Union["StoragegatewayGatewayMaintenanceStartTime", typing.Dict[str, typing.Any]]] = None,
        medium_changer_type: typing.Optional[builtins.str] = None,
        smb_active_directory_settings: typing.Optional[typing.Union["StoragegatewayGatewaySmbActiveDirectorySettings", typing.Dict[str, typing.Any]]] = None,
        smb_file_share_visibility: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        smb_guest_password: typing.Optional[builtins.str] = None,
        smb_security_strategy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tape_drive_type: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["StoragegatewayGatewayTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway aws_storagegateway_gateway} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param gateway_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_name StoragegatewayGateway#gateway_name}.
        :param gateway_timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_timezone StoragegatewayGateway#gateway_timezone}.
        :param activation_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#activation_key StoragegatewayGateway#activation_key}.
        :param average_download_rate_limit_in_bits_per_sec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#average_download_rate_limit_in_bits_per_sec StoragegatewayGateway#average_download_rate_limit_in_bits_per_sec}.
        :param average_upload_rate_limit_in_bits_per_sec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#average_upload_rate_limit_in_bits_per_sec StoragegatewayGateway#average_upload_rate_limit_in_bits_per_sec}.
        :param cloudwatch_log_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#cloudwatch_log_group_arn StoragegatewayGateway#cloudwatch_log_group_arn}.
        :param gateway_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_ip_address StoragegatewayGateway#gateway_ip_address}.
        :param gateway_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_type StoragegatewayGateway#gateway_type}.
        :param gateway_vpc_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_vpc_endpoint StoragegatewayGateway#gateway_vpc_endpoint}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#id StoragegatewayGateway#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance_start_time: maintenance_start_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#maintenance_start_time StoragegatewayGateway#maintenance_start_time}
        :param medium_changer_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#medium_changer_type StoragegatewayGateway#medium_changer_type}.
        :param smb_active_directory_settings: smb_active_directory_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_active_directory_settings StoragegatewayGateway#smb_active_directory_settings}
        :param smb_file_share_visibility: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_file_share_visibility StoragegatewayGateway#smb_file_share_visibility}.
        :param smb_guest_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_guest_password StoragegatewayGateway#smb_guest_password}.
        :param smb_security_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_security_strategy StoragegatewayGateway#smb_security_strategy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#tags StoragegatewayGateway#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#tags_all StoragegatewayGateway#tags_all}.
        :param tape_drive_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#tape_drive_type StoragegatewayGateway#tape_drive_type}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#timeouts StoragegatewayGateway#timeouts}
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
                gateway_name: builtins.str,
                gateway_timezone: builtins.str,
                activation_key: typing.Optional[builtins.str] = None,
                average_download_rate_limit_in_bits_per_sec: typing.Optional[jsii.Number] = None,
                average_upload_rate_limit_in_bits_per_sec: typing.Optional[jsii.Number] = None,
                cloudwatch_log_group_arn: typing.Optional[builtins.str] = None,
                gateway_ip_address: typing.Optional[builtins.str] = None,
                gateway_type: typing.Optional[builtins.str] = None,
                gateway_vpc_endpoint: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                maintenance_start_time: typing.Optional[typing.Union[StoragegatewayGatewayMaintenanceStartTime, typing.Dict[str, typing.Any]]] = None,
                medium_changer_type: typing.Optional[builtins.str] = None,
                smb_active_directory_settings: typing.Optional[typing.Union[StoragegatewayGatewaySmbActiveDirectorySettings, typing.Dict[str, typing.Any]]] = None,
                smb_file_share_visibility: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                smb_guest_password: typing.Optional[builtins.str] = None,
                smb_security_strategy: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tape_drive_type: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[StoragegatewayGatewayTimeouts, typing.Dict[str, typing.Any]]] = None,
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
        config = StoragegatewayGatewayConfig(
            gateway_name=gateway_name,
            gateway_timezone=gateway_timezone,
            activation_key=activation_key,
            average_download_rate_limit_in_bits_per_sec=average_download_rate_limit_in_bits_per_sec,
            average_upload_rate_limit_in_bits_per_sec=average_upload_rate_limit_in_bits_per_sec,
            cloudwatch_log_group_arn=cloudwatch_log_group_arn,
            gateway_ip_address=gateway_ip_address,
            gateway_type=gateway_type,
            gateway_vpc_endpoint=gateway_vpc_endpoint,
            id=id,
            maintenance_start_time=maintenance_start_time,
            medium_changer_type=medium_changer_type,
            smb_active_directory_settings=smb_active_directory_settings,
            smb_file_share_visibility=smb_file_share_visibility,
            smb_guest_password=smb_guest_password,
            smb_security_strategy=smb_security_strategy,
            tags=tags,
            tags_all=tags_all,
            tape_drive_type=tape_drive_type,
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

    @jsii.member(jsii_name="putMaintenanceStartTime")
    def put_maintenance_start_time(
        self,
        *,
        hour_of_day: jsii.Number,
        day_of_month: typing.Optional[builtins.str] = None,
        day_of_week: typing.Optional[builtins.str] = None,
        minute_of_hour: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param hour_of_day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#hour_of_day StoragegatewayGateway#hour_of_day}.
        :param day_of_month: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#day_of_month StoragegatewayGateway#day_of_month}.
        :param day_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#day_of_week StoragegatewayGateway#day_of_week}.
        :param minute_of_hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#minute_of_hour StoragegatewayGateway#minute_of_hour}.
        '''
        value = StoragegatewayGatewayMaintenanceStartTime(
            hour_of_day=hour_of_day,
            day_of_month=day_of_month,
            day_of_week=day_of_week,
            minute_of_hour=minute_of_hour,
        )

        return typing.cast(None, jsii.invoke(self, "putMaintenanceStartTime", [value]))

    @jsii.member(jsii_name="putSmbActiveDirectorySettings")
    def put_smb_active_directory_settings(
        self,
        *,
        domain_name: builtins.str,
        password: builtins.str,
        username: builtins.str,
        domain_controllers: typing.Optional[typing.Sequence[builtins.str]] = None,
        organizational_unit: typing.Optional[builtins.str] = None,
        timeout_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#domain_name StoragegatewayGateway#domain_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#password StoragegatewayGateway#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#username StoragegatewayGateway#username}.
        :param domain_controllers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#domain_controllers StoragegatewayGateway#domain_controllers}.
        :param organizational_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#organizational_unit StoragegatewayGateway#organizational_unit}.
        :param timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#timeout_in_seconds StoragegatewayGateway#timeout_in_seconds}.
        '''
        value = StoragegatewayGatewaySmbActiveDirectorySettings(
            domain_name=domain_name,
            password=password,
            username=username,
            domain_controllers=domain_controllers,
            organizational_unit=organizational_unit,
            timeout_in_seconds=timeout_in_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putSmbActiveDirectorySettings", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#create StoragegatewayGateway#create}.
        '''
        value = StoragegatewayGatewayTimeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetActivationKey")
    def reset_activation_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivationKey", []))

    @jsii.member(jsii_name="resetAverageDownloadRateLimitInBitsPerSec")
    def reset_average_download_rate_limit_in_bits_per_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageDownloadRateLimitInBitsPerSec", []))

    @jsii.member(jsii_name="resetAverageUploadRateLimitInBitsPerSec")
    def reset_average_upload_rate_limit_in_bits_per_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageUploadRateLimitInBitsPerSec", []))

    @jsii.member(jsii_name="resetCloudwatchLogGroupArn")
    def reset_cloudwatch_log_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLogGroupArn", []))

    @jsii.member(jsii_name="resetGatewayIpAddress")
    def reset_gateway_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGatewayIpAddress", []))

    @jsii.member(jsii_name="resetGatewayType")
    def reset_gateway_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGatewayType", []))

    @jsii.member(jsii_name="resetGatewayVpcEndpoint")
    def reset_gateway_vpc_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGatewayVpcEndpoint", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaintenanceStartTime")
    def reset_maintenance_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceStartTime", []))

    @jsii.member(jsii_name="resetMediumChangerType")
    def reset_medium_changer_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMediumChangerType", []))

    @jsii.member(jsii_name="resetSmbActiveDirectorySettings")
    def reset_smb_active_directory_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmbActiveDirectorySettings", []))

    @jsii.member(jsii_name="resetSmbFileShareVisibility")
    def reset_smb_file_share_visibility(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmbFileShareVisibility", []))

    @jsii.member(jsii_name="resetSmbGuestPassword")
    def reset_smb_guest_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmbGuestPassword", []))

    @jsii.member(jsii_name="resetSmbSecurityStrategy")
    def reset_smb_security_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmbSecurityStrategy", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTapeDriveType")
    def reset_tape_drive_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTapeDriveType", []))

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
    @jsii.member(jsii_name="ec2InstanceId")
    def ec2_instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ec2InstanceId"))

    @builtins.property
    @jsii.member(jsii_name="endpointType")
    def endpoint_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointType"))

    @builtins.property
    @jsii.member(jsii_name="gatewayId")
    def gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayId"))

    @builtins.property
    @jsii.member(jsii_name="gatewayNetworkInterface")
    def gateway_network_interface(
        self,
    ) -> "StoragegatewayGatewayGatewayNetworkInterfaceList":
        return typing.cast("StoragegatewayGatewayGatewayNetworkInterfaceList", jsii.get(self, "gatewayNetworkInterface"))

    @builtins.property
    @jsii.member(jsii_name="hostEnvironment")
    def host_environment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostEnvironment"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceStartTime")
    def maintenance_start_time(
        self,
    ) -> "StoragegatewayGatewayMaintenanceStartTimeOutputReference":
        return typing.cast("StoragegatewayGatewayMaintenanceStartTimeOutputReference", jsii.get(self, "maintenanceStartTime"))

    @builtins.property
    @jsii.member(jsii_name="smbActiveDirectorySettings")
    def smb_active_directory_settings(
        self,
    ) -> "StoragegatewayGatewaySmbActiveDirectorySettingsOutputReference":
        return typing.cast("StoragegatewayGatewaySmbActiveDirectorySettingsOutputReference", jsii.get(self, "smbActiveDirectorySettings"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "StoragegatewayGatewayTimeoutsOutputReference":
        return typing.cast("StoragegatewayGatewayTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="activationKeyInput")
    def activation_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activationKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="averageDownloadRateLimitInBitsPerSecInput")
    def average_download_rate_limit_in_bits_per_sec_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "averageDownloadRateLimitInBitsPerSecInput"))

    @builtins.property
    @jsii.member(jsii_name="averageUploadRateLimitInBitsPerSecInput")
    def average_upload_rate_limit_in_bits_per_sec_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "averageUploadRateLimitInBitsPerSecInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogGroupArnInput")
    def cloudwatch_log_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudwatchLogGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayIpAddressInput")
    def gateway_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayNameInput")
    def gateway_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayTimezoneInput")
    def gateway_timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayTimezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayTypeInput")
    def gateway_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayVpcEndpointInput")
    def gateway_vpc_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayVpcEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceStartTimeInput")
    def maintenance_start_time_input(
        self,
    ) -> typing.Optional["StoragegatewayGatewayMaintenanceStartTime"]:
        return typing.cast(typing.Optional["StoragegatewayGatewayMaintenanceStartTime"], jsii.get(self, "maintenanceStartTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="mediumChangerTypeInput")
    def medium_changer_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mediumChangerTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="smbActiveDirectorySettingsInput")
    def smb_active_directory_settings_input(
        self,
    ) -> typing.Optional["StoragegatewayGatewaySmbActiveDirectorySettings"]:
        return typing.cast(typing.Optional["StoragegatewayGatewaySmbActiveDirectorySettings"], jsii.get(self, "smbActiveDirectorySettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="smbFileShareVisibilityInput")
    def smb_file_share_visibility_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "smbFileShareVisibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="smbGuestPasswordInput")
    def smb_guest_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "smbGuestPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="smbSecurityStrategyInput")
    def smb_security_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "smbSecurityStrategyInput"))

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
    @jsii.member(jsii_name="tapeDriveTypeInput")
    def tape_drive_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tapeDriveTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["StoragegatewayGatewayTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["StoragegatewayGatewayTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="activationKey")
    def activation_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activationKey"))

    @activation_key.setter
    def activation_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activationKey", value)

    @builtins.property
    @jsii.member(jsii_name="averageDownloadRateLimitInBitsPerSec")
    def average_download_rate_limit_in_bits_per_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "averageDownloadRateLimitInBitsPerSec"))

    @average_download_rate_limit_in_bits_per_sec.setter
    def average_download_rate_limit_in_bits_per_sec(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageDownloadRateLimitInBitsPerSec", value)

    @builtins.property
    @jsii.member(jsii_name="averageUploadRateLimitInBitsPerSec")
    def average_upload_rate_limit_in_bits_per_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "averageUploadRateLimitInBitsPerSec"))

    @average_upload_rate_limit_in_bits_per_sec.setter
    def average_upload_rate_limit_in_bits_per_sec(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageUploadRateLimitInBitsPerSec", value)

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudwatchLogGroupArn"))

    @cloudwatch_log_group_arn.setter
    def cloudwatch_log_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudwatchLogGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayIpAddress")
    def gateway_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayIpAddress"))

    @gateway_ip_address.setter
    def gateway_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayName")
    def gateway_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayName"))

    @gateway_name.setter
    def gateway_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayName", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayTimezone")
    def gateway_timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayTimezone"))

    @gateway_timezone.setter
    def gateway_timezone(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayTimezone", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayType")
    def gateway_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayType"))

    @gateway_type.setter
    def gateway_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayType", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayVpcEndpoint")
    def gateway_vpc_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayVpcEndpoint"))

    @gateway_vpc_endpoint.setter
    def gateway_vpc_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayVpcEndpoint", value)

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
    @jsii.member(jsii_name="mediumChangerType")
    def medium_changer_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mediumChangerType"))

    @medium_changer_type.setter
    def medium_changer_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mediumChangerType", value)

    @builtins.property
    @jsii.member(jsii_name="smbFileShareVisibility")
    def smb_file_share_visibility(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "smbFileShareVisibility"))

    @smb_file_share_visibility.setter
    def smb_file_share_visibility(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smbFileShareVisibility", value)

    @builtins.property
    @jsii.member(jsii_name="smbGuestPassword")
    def smb_guest_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "smbGuestPassword"))

    @smb_guest_password.setter
    def smb_guest_password(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smbGuestPassword", value)

    @builtins.property
    @jsii.member(jsii_name="smbSecurityStrategy")
    def smb_security_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "smbSecurityStrategy"))

    @smb_security_strategy.setter
    def smb_security_strategy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smbSecurityStrategy", value)

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
    @jsii.member(jsii_name="tapeDriveType")
    def tape_drive_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tapeDriveType"))

    @tape_drive_type.setter
    def tape_drive_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tapeDriveType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.storagegatewayGateway.StoragegatewayGatewayConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "gateway_name": "gatewayName",
        "gateway_timezone": "gatewayTimezone",
        "activation_key": "activationKey",
        "average_download_rate_limit_in_bits_per_sec": "averageDownloadRateLimitInBitsPerSec",
        "average_upload_rate_limit_in_bits_per_sec": "averageUploadRateLimitInBitsPerSec",
        "cloudwatch_log_group_arn": "cloudwatchLogGroupArn",
        "gateway_ip_address": "gatewayIpAddress",
        "gateway_type": "gatewayType",
        "gateway_vpc_endpoint": "gatewayVpcEndpoint",
        "id": "id",
        "maintenance_start_time": "maintenanceStartTime",
        "medium_changer_type": "mediumChangerType",
        "smb_active_directory_settings": "smbActiveDirectorySettings",
        "smb_file_share_visibility": "smbFileShareVisibility",
        "smb_guest_password": "smbGuestPassword",
        "smb_security_strategy": "smbSecurityStrategy",
        "tags": "tags",
        "tags_all": "tagsAll",
        "tape_drive_type": "tapeDriveType",
        "timeouts": "timeouts",
    },
)
class StoragegatewayGatewayConfig(cdktf.TerraformMetaArguments):
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
        gateway_name: builtins.str,
        gateway_timezone: builtins.str,
        activation_key: typing.Optional[builtins.str] = None,
        average_download_rate_limit_in_bits_per_sec: typing.Optional[jsii.Number] = None,
        average_upload_rate_limit_in_bits_per_sec: typing.Optional[jsii.Number] = None,
        cloudwatch_log_group_arn: typing.Optional[builtins.str] = None,
        gateway_ip_address: typing.Optional[builtins.str] = None,
        gateway_type: typing.Optional[builtins.str] = None,
        gateway_vpc_endpoint: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        maintenance_start_time: typing.Optional[typing.Union["StoragegatewayGatewayMaintenanceStartTime", typing.Dict[str, typing.Any]]] = None,
        medium_changer_type: typing.Optional[builtins.str] = None,
        smb_active_directory_settings: typing.Optional[typing.Union["StoragegatewayGatewaySmbActiveDirectorySettings", typing.Dict[str, typing.Any]]] = None,
        smb_file_share_visibility: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        smb_guest_password: typing.Optional[builtins.str] = None,
        smb_security_strategy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tape_drive_type: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["StoragegatewayGatewayTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param gateway_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_name StoragegatewayGateway#gateway_name}.
        :param gateway_timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_timezone StoragegatewayGateway#gateway_timezone}.
        :param activation_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#activation_key StoragegatewayGateway#activation_key}.
        :param average_download_rate_limit_in_bits_per_sec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#average_download_rate_limit_in_bits_per_sec StoragegatewayGateway#average_download_rate_limit_in_bits_per_sec}.
        :param average_upload_rate_limit_in_bits_per_sec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#average_upload_rate_limit_in_bits_per_sec StoragegatewayGateway#average_upload_rate_limit_in_bits_per_sec}.
        :param cloudwatch_log_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#cloudwatch_log_group_arn StoragegatewayGateway#cloudwatch_log_group_arn}.
        :param gateway_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_ip_address StoragegatewayGateway#gateway_ip_address}.
        :param gateway_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_type StoragegatewayGateway#gateway_type}.
        :param gateway_vpc_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_vpc_endpoint StoragegatewayGateway#gateway_vpc_endpoint}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#id StoragegatewayGateway#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maintenance_start_time: maintenance_start_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#maintenance_start_time StoragegatewayGateway#maintenance_start_time}
        :param medium_changer_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#medium_changer_type StoragegatewayGateway#medium_changer_type}.
        :param smb_active_directory_settings: smb_active_directory_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_active_directory_settings StoragegatewayGateway#smb_active_directory_settings}
        :param smb_file_share_visibility: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_file_share_visibility StoragegatewayGateway#smb_file_share_visibility}.
        :param smb_guest_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_guest_password StoragegatewayGateway#smb_guest_password}.
        :param smb_security_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_security_strategy StoragegatewayGateway#smb_security_strategy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#tags StoragegatewayGateway#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#tags_all StoragegatewayGateway#tags_all}.
        :param tape_drive_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#tape_drive_type StoragegatewayGateway#tape_drive_type}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#timeouts StoragegatewayGateway#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(maintenance_start_time, dict):
            maintenance_start_time = StoragegatewayGatewayMaintenanceStartTime(**maintenance_start_time)
        if isinstance(smb_active_directory_settings, dict):
            smb_active_directory_settings = StoragegatewayGatewaySmbActiveDirectorySettings(**smb_active_directory_settings)
        if isinstance(timeouts, dict):
            timeouts = StoragegatewayGatewayTimeouts(**timeouts)
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
                gateway_name: builtins.str,
                gateway_timezone: builtins.str,
                activation_key: typing.Optional[builtins.str] = None,
                average_download_rate_limit_in_bits_per_sec: typing.Optional[jsii.Number] = None,
                average_upload_rate_limit_in_bits_per_sec: typing.Optional[jsii.Number] = None,
                cloudwatch_log_group_arn: typing.Optional[builtins.str] = None,
                gateway_ip_address: typing.Optional[builtins.str] = None,
                gateway_type: typing.Optional[builtins.str] = None,
                gateway_vpc_endpoint: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                maintenance_start_time: typing.Optional[typing.Union[StoragegatewayGatewayMaintenanceStartTime, typing.Dict[str, typing.Any]]] = None,
                medium_changer_type: typing.Optional[builtins.str] = None,
                smb_active_directory_settings: typing.Optional[typing.Union[StoragegatewayGatewaySmbActiveDirectorySettings, typing.Dict[str, typing.Any]]] = None,
                smb_file_share_visibility: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                smb_guest_password: typing.Optional[builtins.str] = None,
                smb_security_strategy: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tape_drive_type: typing.Optional[builtins.str] = None,
                timeouts: typing.Optional[typing.Union[StoragegatewayGatewayTimeouts, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument gateway_name", value=gateway_name, expected_type=type_hints["gateway_name"])
            check_type(argname="argument gateway_timezone", value=gateway_timezone, expected_type=type_hints["gateway_timezone"])
            check_type(argname="argument activation_key", value=activation_key, expected_type=type_hints["activation_key"])
            check_type(argname="argument average_download_rate_limit_in_bits_per_sec", value=average_download_rate_limit_in_bits_per_sec, expected_type=type_hints["average_download_rate_limit_in_bits_per_sec"])
            check_type(argname="argument average_upload_rate_limit_in_bits_per_sec", value=average_upload_rate_limit_in_bits_per_sec, expected_type=type_hints["average_upload_rate_limit_in_bits_per_sec"])
            check_type(argname="argument cloudwatch_log_group_arn", value=cloudwatch_log_group_arn, expected_type=type_hints["cloudwatch_log_group_arn"])
            check_type(argname="argument gateway_ip_address", value=gateway_ip_address, expected_type=type_hints["gateway_ip_address"])
            check_type(argname="argument gateway_type", value=gateway_type, expected_type=type_hints["gateway_type"])
            check_type(argname="argument gateway_vpc_endpoint", value=gateway_vpc_endpoint, expected_type=type_hints["gateway_vpc_endpoint"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument maintenance_start_time", value=maintenance_start_time, expected_type=type_hints["maintenance_start_time"])
            check_type(argname="argument medium_changer_type", value=medium_changer_type, expected_type=type_hints["medium_changer_type"])
            check_type(argname="argument smb_active_directory_settings", value=smb_active_directory_settings, expected_type=type_hints["smb_active_directory_settings"])
            check_type(argname="argument smb_file_share_visibility", value=smb_file_share_visibility, expected_type=type_hints["smb_file_share_visibility"])
            check_type(argname="argument smb_guest_password", value=smb_guest_password, expected_type=type_hints["smb_guest_password"])
            check_type(argname="argument smb_security_strategy", value=smb_security_strategy, expected_type=type_hints["smb_security_strategy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument tape_drive_type", value=tape_drive_type, expected_type=type_hints["tape_drive_type"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "gateway_name": gateway_name,
            "gateway_timezone": gateway_timezone,
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
        if activation_key is not None:
            self._values["activation_key"] = activation_key
        if average_download_rate_limit_in_bits_per_sec is not None:
            self._values["average_download_rate_limit_in_bits_per_sec"] = average_download_rate_limit_in_bits_per_sec
        if average_upload_rate_limit_in_bits_per_sec is not None:
            self._values["average_upload_rate_limit_in_bits_per_sec"] = average_upload_rate_limit_in_bits_per_sec
        if cloudwatch_log_group_arn is not None:
            self._values["cloudwatch_log_group_arn"] = cloudwatch_log_group_arn
        if gateway_ip_address is not None:
            self._values["gateway_ip_address"] = gateway_ip_address
        if gateway_type is not None:
            self._values["gateway_type"] = gateway_type
        if gateway_vpc_endpoint is not None:
            self._values["gateway_vpc_endpoint"] = gateway_vpc_endpoint
        if id is not None:
            self._values["id"] = id
        if maintenance_start_time is not None:
            self._values["maintenance_start_time"] = maintenance_start_time
        if medium_changer_type is not None:
            self._values["medium_changer_type"] = medium_changer_type
        if smb_active_directory_settings is not None:
            self._values["smb_active_directory_settings"] = smb_active_directory_settings
        if smb_file_share_visibility is not None:
            self._values["smb_file_share_visibility"] = smb_file_share_visibility
        if smb_guest_password is not None:
            self._values["smb_guest_password"] = smb_guest_password
        if smb_security_strategy is not None:
            self._values["smb_security_strategy"] = smb_security_strategy
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if tape_drive_type is not None:
            self._values["tape_drive_type"] = tape_drive_type
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
    def gateway_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_name StoragegatewayGateway#gateway_name}.'''
        result = self._values.get("gateway_name")
        assert result is not None, "Required property 'gateway_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def gateway_timezone(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_timezone StoragegatewayGateway#gateway_timezone}.'''
        result = self._values.get("gateway_timezone")
        assert result is not None, "Required property 'gateway_timezone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def activation_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#activation_key StoragegatewayGateway#activation_key}.'''
        result = self._values.get("activation_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def average_download_rate_limit_in_bits_per_sec(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#average_download_rate_limit_in_bits_per_sec StoragegatewayGateway#average_download_rate_limit_in_bits_per_sec}.'''
        result = self._values.get("average_download_rate_limit_in_bits_per_sec")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def average_upload_rate_limit_in_bits_per_sec(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#average_upload_rate_limit_in_bits_per_sec StoragegatewayGateway#average_upload_rate_limit_in_bits_per_sec}.'''
        result = self._values.get("average_upload_rate_limit_in_bits_per_sec")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cloudwatch_log_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#cloudwatch_log_group_arn StoragegatewayGateway#cloudwatch_log_group_arn}.'''
        result = self._values.get("cloudwatch_log_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gateway_ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_ip_address StoragegatewayGateway#gateway_ip_address}.'''
        result = self._values.get("gateway_ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gateway_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_type StoragegatewayGateway#gateway_type}.'''
        result = self._values.get("gateway_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gateway_vpc_endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#gateway_vpc_endpoint StoragegatewayGateway#gateway_vpc_endpoint}.'''
        result = self._values.get("gateway_vpc_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#id StoragegatewayGateway#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_start_time(
        self,
    ) -> typing.Optional["StoragegatewayGatewayMaintenanceStartTime"]:
        '''maintenance_start_time block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#maintenance_start_time StoragegatewayGateway#maintenance_start_time}
        '''
        result = self._values.get("maintenance_start_time")
        return typing.cast(typing.Optional["StoragegatewayGatewayMaintenanceStartTime"], result)

    @builtins.property
    def medium_changer_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#medium_changer_type StoragegatewayGateway#medium_changer_type}.'''
        result = self._values.get("medium_changer_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def smb_active_directory_settings(
        self,
    ) -> typing.Optional["StoragegatewayGatewaySmbActiveDirectorySettings"]:
        '''smb_active_directory_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_active_directory_settings StoragegatewayGateway#smb_active_directory_settings}
        '''
        result = self._values.get("smb_active_directory_settings")
        return typing.cast(typing.Optional["StoragegatewayGatewaySmbActiveDirectorySettings"], result)

    @builtins.property
    def smb_file_share_visibility(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_file_share_visibility StoragegatewayGateway#smb_file_share_visibility}.'''
        result = self._values.get("smb_file_share_visibility")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def smb_guest_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_guest_password StoragegatewayGateway#smb_guest_password}.'''
        result = self._values.get("smb_guest_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def smb_security_strategy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#smb_security_strategy StoragegatewayGateway#smb_security_strategy}.'''
        result = self._values.get("smb_security_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#tags StoragegatewayGateway#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#tags_all StoragegatewayGateway#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tape_drive_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#tape_drive_type StoragegatewayGateway#tape_drive_type}.'''
        result = self._values.get("tape_drive_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["StoragegatewayGatewayTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#timeouts StoragegatewayGateway#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["StoragegatewayGatewayTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewayGatewayConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.storagegatewayGateway.StoragegatewayGatewayGatewayNetworkInterface",
    jsii_struct_bases=[],
    name_mapping={},
)
class StoragegatewayGatewayGatewayNetworkInterface:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewayGatewayGatewayNetworkInterface(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StoragegatewayGatewayGatewayNetworkInterfaceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.storagegatewayGateway.StoragegatewayGatewayGatewayNetworkInterfaceList",
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
    ) -> "StoragegatewayGatewayGatewayNetworkInterfaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StoragegatewayGatewayGatewayNetworkInterfaceOutputReference", jsii.invoke(self, "get", [index]))

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


class StoragegatewayGatewayGatewayNetworkInterfaceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.storagegatewayGateway.StoragegatewayGatewayGatewayNetworkInterfaceOutputReference",
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
    @jsii.member(jsii_name="ipv4Address")
    def ipv4_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv4Address"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StoragegatewayGatewayGatewayNetworkInterface]:
        return typing.cast(typing.Optional[StoragegatewayGatewayGatewayNetworkInterface], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StoragegatewayGatewayGatewayNetworkInterface],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[StoragegatewayGatewayGatewayNetworkInterface],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.storagegatewayGateway.StoragegatewayGatewayMaintenanceStartTime",
    jsii_struct_bases=[],
    name_mapping={
        "hour_of_day": "hourOfDay",
        "day_of_month": "dayOfMonth",
        "day_of_week": "dayOfWeek",
        "minute_of_hour": "minuteOfHour",
    },
)
class StoragegatewayGatewayMaintenanceStartTime:
    def __init__(
        self,
        *,
        hour_of_day: jsii.Number,
        day_of_month: typing.Optional[builtins.str] = None,
        day_of_week: typing.Optional[builtins.str] = None,
        minute_of_hour: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param hour_of_day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#hour_of_day StoragegatewayGateway#hour_of_day}.
        :param day_of_month: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#day_of_month StoragegatewayGateway#day_of_month}.
        :param day_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#day_of_week StoragegatewayGateway#day_of_week}.
        :param minute_of_hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#minute_of_hour StoragegatewayGateway#minute_of_hour}.
        '''
        if __debug__:
            def stub(
                *,
                hour_of_day: jsii.Number,
                day_of_month: typing.Optional[builtins.str] = None,
                day_of_week: typing.Optional[builtins.str] = None,
                minute_of_hour: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument hour_of_day", value=hour_of_day, expected_type=type_hints["hour_of_day"])
            check_type(argname="argument day_of_month", value=day_of_month, expected_type=type_hints["day_of_month"])
            check_type(argname="argument day_of_week", value=day_of_week, expected_type=type_hints["day_of_week"])
            check_type(argname="argument minute_of_hour", value=minute_of_hour, expected_type=type_hints["minute_of_hour"])
        self._values: typing.Dict[str, typing.Any] = {
            "hour_of_day": hour_of_day,
        }
        if day_of_month is not None:
            self._values["day_of_month"] = day_of_month
        if day_of_week is not None:
            self._values["day_of_week"] = day_of_week
        if minute_of_hour is not None:
            self._values["minute_of_hour"] = minute_of_hour

    @builtins.property
    def hour_of_day(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#hour_of_day StoragegatewayGateway#hour_of_day}.'''
        result = self._values.get("hour_of_day")
        assert result is not None, "Required property 'hour_of_day' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def day_of_month(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#day_of_month StoragegatewayGateway#day_of_month}.'''
        result = self._values.get("day_of_month")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def day_of_week(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#day_of_week StoragegatewayGateway#day_of_week}.'''
        result = self._values.get("day_of_week")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minute_of_hour(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#minute_of_hour StoragegatewayGateway#minute_of_hour}.'''
        result = self._values.get("minute_of_hour")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewayGatewayMaintenanceStartTime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StoragegatewayGatewayMaintenanceStartTimeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.storagegatewayGateway.StoragegatewayGatewayMaintenanceStartTimeOutputReference",
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

    @jsii.member(jsii_name="resetDayOfMonth")
    def reset_day_of_month(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDayOfMonth", []))

    @jsii.member(jsii_name="resetDayOfWeek")
    def reset_day_of_week(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDayOfWeek", []))

    @jsii.member(jsii_name="resetMinuteOfHour")
    def reset_minute_of_hour(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinuteOfHour", []))

    @builtins.property
    @jsii.member(jsii_name="dayOfMonthInput")
    def day_of_month_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfMonthInput"))

    @builtins.property
    @jsii.member(jsii_name="dayOfWeekInput")
    def day_of_week_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfWeekInput"))

    @builtins.property
    @jsii.member(jsii_name="hourOfDayInput")
    def hour_of_day_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hourOfDayInput"))

    @builtins.property
    @jsii.member(jsii_name="minuteOfHourInput")
    def minute_of_hour_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minuteOfHourInput"))

    @builtins.property
    @jsii.member(jsii_name="dayOfMonth")
    def day_of_month(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayOfMonth"))

    @day_of_month.setter
    def day_of_month(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfMonth", value)

    @builtins.property
    @jsii.member(jsii_name="dayOfWeek")
    def day_of_week(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayOfWeek"))

    @day_of_week.setter
    def day_of_week(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfWeek", value)

    @builtins.property
    @jsii.member(jsii_name="hourOfDay")
    def hour_of_day(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hourOfDay"))

    @hour_of_day.setter
    def hour_of_day(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hourOfDay", value)

    @builtins.property
    @jsii.member(jsii_name="minuteOfHour")
    def minute_of_hour(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minuteOfHour"))

    @minute_of_hour.setter
    def minute_of_hour(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minuteOfHour", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StoragegatewayGatewayMaintenanceStartTime]:
        return typing.cast(typing.Optional[StoragegatewayGatewayMaintenanceStartTime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StoragegatewayGatewayMaintenanceStartTime],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[StoragegatewayGatewayMaintenanceStartTime],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.storagegatewayGateway.StoragegatewayGatewaySmbActiveDirectorySettings",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "password": "password",
        "username": "username",
        "domain_controllers": "domainControllers",
        "organizational_unit": "organizationalUnit",
        "timeout_in_seconds": "timeoutInSeconds",
    },
)
class StoragegatewayGatewaySmbActiveDirectorySettings:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        password: builtins.str,
        username: builtins.str,
        domain_controllers: typing.Optional[typing.Sequence[builtins.str]] = None,
        organizational_unit: typing.Optional[builtins.str] = None,
        timeout_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#domain_name StoragegatewayGateway#domain_name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#password StoragegatewayGateway#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#username StoragegatewayGateway#username}.
        :param domain_controllers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#domain_controllers StoragegatewayGateway#domain_controllers}.
        :param organizational_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#organizational_unit StoragegatewayGateway#organizational_unit}.
        :param timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#timeout_in_seconds StoragegatewayGateway#timeout_in_seconds}.
        '''
        if __debug__:
            def stub(
                *,
                domain_name: builtins.str,
                password: builtins.str,
                username: builtins.str,
                domain_controllers: typing.Optional[typing.Sequence[builtins.str]] = None,
                organizational_unit: typing.Optional[builtins.str] = None,
                timeout_in_seconds: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument domain_controllers", value=domain_controllers, expected_type=type_hints["domain_controllers"])
            check_type(argname="argument organizational_unit", value=organizational_unit, expected_type=type_hints["organizational_unit"])
            check_type(argname="argument timeout_in_seconds", value=timeout_in_seconds, expected_type=type_hints["timeout_in_seconds"])
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
            "password": password,
            "username": username,
        }
        if domain_controllers is not None:
            self._values["domain_controllers"] = domain_controllers
        if organizational_unit is not None:
            self._values["organizational_unit"] = organizational_unit
        if timeout_in_seconds is not None:
            self._values["timeout_in_seconds"] = timeout_in_seconds

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#domain_name StoragegatewayGateway#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#password StoragegatewayGateway#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#username StoragegatewayGateway#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_controllers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#domain_controllers StoragegatewayGateway#domain_controllers}.'''
        result = self._values.get("domain_controllers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def organizational_unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#organizational_unit StoragegatewayGateway#organizational_unit}.'''
        result = self._values.get("organizational_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#timeout_in_seconds StoragegatewayGateway#timeout_in_seconds}.'''
        result = self._values.get("timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewayGatewaySmbActiveDirectorySettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StoragegatewayGatewaySmbActiveDirectorySettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.storagegatewayGateway.StoragegatewayGatewaySmbActiveDirectorySettingsOutputReference",
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

    @jsii.member(jsii_name="resetDomainControllers")
    def reset_domain_controllers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomainControllers", []))

    @jsii.member(jsii_name="resetOrganizationalUnit")
    def reset_organizational_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganizationalUnit", []))

    @jsii.member(jsii_name="resetTimeoutInSeconds")
    def reset_timeout_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutInSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="activeDirectoryStatus")
    def active_directory_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activeDirectoryStatus"))

    @builtins.property
    @jsii.member(jsii_name="domainControllersInput")
    def domain_controllers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "domainControllersInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationalUnitInput")
    def organizational_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationalUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInSecondsInput")
    def timeout_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="domainControllers")
    def domain_controllers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "domainControllers"))

    @domain_controllers.setter
    def domain_controllers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainControllers", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="organizationalUnit")
    def organizational_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationalUnit"))

    @organizational_unit.setter
    def organizational_unit(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationalUnit", value)

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
    @jsii.member(jsii_name="timeoutInSeconds")
    def timeout_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutInSeconds"))

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutInSeconds", value)

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
    ) -> typing.Optional[StoragegatewayGatewaySmbActiveDirectorySettings]:
        return typing.cast(typing.Optional[StoragegatewayGatewaySmbActiveDirectorySettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StoragegatewayGatewaySmbActiveDirectorySettings],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[StoragegatewayGatewaySmbActiveDirectorySettings],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.storagegatewayGateway.StoragegatewayGatewayTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class StoragegatewayGatewayTimeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#create StoragegatewayGateway#create}.
        '''
        if __debug__:
            def stub(*, create: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/storagegateway_gateway#create StoragegatewayGateway#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoragegatewayGatewayTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StoragegatewayGatewayTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.storagegatewayGateway.StoragegatewayGatewayTimeoutsOutputReference",
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

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StoragegatewayGatewayTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StoragegatewayGatewayTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StoragegatewayGatewayTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[StoragegatewayGatewayTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StoragegatewayGateway",
    "StoragegatewayGatewayConfig",
    "StoragegatewayGatewayGatewayNetworkInterface",
    "StoragegatewayGatewayGatewayNetworkInterfaceList",
    "StoragegatewayGatewayGatewayNetworkInterfaceOutputReference",
    "StoragegatewayGatewayMaintenanceStartTime",
    "StoragegatewayGatewayMaintenanceStartTimeOutputReference",
    "StoragegatewayGatewaySmbActiveDirectorySettings",
    "StoragegatewayGatewaySmbActiveDirectorySettingsOutputReference",
    "StoragegatewayGatewayTimeouts",
    "StoragegatewayGatewayTimeoutsOutputReference",
]

publication.publish()
