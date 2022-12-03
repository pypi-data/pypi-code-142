'''
# `aws_vpn_connection`

Refer to the Terraform Registory for docs: [`aws_vpn_connection`](https://www.terraform.io/docs/providers/aws/r/vpn_connection).
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


class VpnConnection(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.vpnConnection.VpnConnection",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection aws_vpn_connection}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        customer_gateway_id: builtins.str,
        type: builtins.str,
        enable_acceleration: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        local_ipv4_network_cidr: typing.Optional[builtins.str] = None,
        local_ipv6_network_cidr: typing.Optional[builtins.str] = None,
        outside_ip_address_type: typing.Optional[builtins.str] = None,
        remote_ipv4_network_cidr: typing.Optional[builtins.str] = None,
        remote_ipv6_network_cidr: typing.Optional[builtins.str] = None,
        static_routes_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        transit_gateway_id: typing.Optional[builtins.str] = None,
        transport_transit_gateway_attachment_id: typing.Optional[builtins.str] = None,
        tunnel1_dpd_timeout_action: typing.Optional[builtins.str] = None,
        tunnel1_dpd_timeout_seconds: typing.Optional[jsii.Number] = None,
        tunnel1_ike_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_inside_cidr: typing.Optional[builtins.str] = None,
        tunnel1_inside_ipv6_cidr: typing.Optional[builtins.str] = None,
        tunnel1_log_options: typing.Optional[typing.Union["VpnConnectionTunnel1LogOptions", typing.Dict[str, typing.Any]]] = None,
        tunnel1_phase1_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        tunnel1_phase1_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_phase1_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_phase1_lifetime_seconds: typing.Optional[jsii.Number] = None,
        tunnel1_phase2_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        tunnel1_phase2_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_phase2_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_phase2_lifetime_seconds: typing.Optional[jsii.Number] = None,
        tunnel1_preshared_key: typing.Optional[builtins.str] = None,
        tunnel1_rekey_fuzz_percentage: typing.Optional[jsii.Number] = None,
        tunnel1_rekey_margin_time_seconds: typing.Optional[jsii.Number] = None,
        tunnel1_replay_window_size: typing.Optional[jsii.Number] = None,
        tunnel1_startup_action: typing.Optional[builtins.str] = None,
        tunnel2_dpd_timeout_action: typing.Optional[builtins.str] = None,
        tunnel2_dpd_timeout_seconds: typing.Optional[jsii.Number] = None,
        tunnel2_ike_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_inside_cidr: typing.Optional[builtins.str] = None,
        tunnel2_inside_ipv6_cidr: typing.Optional[builtins.str] = None,
        tunnel2_log_options: typing.Optional[typing.Union["VpnConnectionTunnel2LogOptions", typing.Dict[str, typing.Any]]] = None,
        tunnel2_phase1_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        tunnel2_phase1_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_phase1_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_phase1_lifetime_seconds: typing.Optional[jsii.Number] = None,
        tunnel2_phase2_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        tunnel2_phase2_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_phase2_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_phase2_lifetime_seconds: typing.Optional[jsii.Number] = None,
        tunnel2_preshared_key: typing.Optional[builtins.str] = None,
        tunnel2_rekey_fuzz_percentage: typing.Optional[jsii.Number] = None,
        tunnel2_rekey_margin_time_seconds: typing.Optional[jsii.Number] = None,
        tunnel2_replay_window_size: typing.Optional[jsii.Number] = None,
        tunnel2_startup_action: typing.Optional[builtins.str] = None,
        tunnel_inside_ip_version: typing.Optional[builtins.str] = None,
        vpn_gateway_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection aws_vpn_connection} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param customer_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#customer_gateway_id VpnConnection#customer_gateway_id}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#type VpnConnection#type}.
        :param enable_acceleration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#enable_acceleration VpnConnection#enable_acceleration}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#id VpnConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param local_ipv4_network_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#local_ipv4_network_cidr VpnConnection#local_ipv4_network_cidr}.
        :param local_ipv6_network_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#local_ipv6_network_cidr VpnConnection#local_ipv6_network_cidr}.
        :param outside_ip_address_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#outside_ip_address_type VpnConnection#outside_ip_address_type}.
        :param remote_ipv4_network_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#remote_ipv4_network_cidr VpnConnection#remote_ipv4_network_cidr}.
        :param remote_ipv6_network_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#remote_ipv6_network_cidr VpnConnection#remote_ipv6_network_cidr}.
        :param static_routes_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#static_routes_only VpnConnection#static_routes_only}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tags VpnConnection#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tags_all VpnConnection#tags_all}.
        :param transit_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#transit_gateway_id VpnConnection#transit_gateway_id}.
        :param transport_transit_gateway_attachment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#transport_transit_gateway_attachment_id VpnConnection#transport_transit_gateway_attachment_id}.
        :param tunnel1_dpd_timeout_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_dpd_timeout_action VpnConnection#tunnel1_dpd_timeout_action}.
        :param tunnel1_dpd_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_dpd_timeout_seconds VpnConnection#tunnel1_dpd_timeout_seconds}.
        :param tunnel1_ike_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_ike_versions VpnConnection#tunnel1_ike_versions}.
        :param tunnel1_inside_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_inside_cidr VpnConnection#tunnel1_inside_cidr}.
        :param tunnel1_inside_ipv6_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_inside_ipv6_cidr VpnConnection#tunnel1_inside_ipv6_cidr}.
        :param tunnel1_log_options: tunnel1_log_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_log_options VpnConnection#tunnel1_log_options}
        :param tunnel1_phase1_dh_group_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_dh_group_numbers VpnConnection#tunnel1_phase1_dh_group_numbers}.
        :param tunnel1_phase1_encryption_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_encryption_algorithms VpnConnection#tunnel1_phase1_encryption_algorithms}.
        :param tunnel1_phase1_integrity_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_integrity_algorithms VpnConnection#tunnel1_phase1_integrity_algorithms}.
        :param tunnel1_phase1_lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_lifetime_seconds VpnConnection#tunnel1_phase1_lifetime_seconds}.
        :param tunnel1_phase2_dh_group_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_dh_group_numbers VpnConnection#tunnel1_phase2_dh_group_numbers}.
        :param tunnel1_phase2_encryption_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_encryption_algorithms VpnConnection#tunnel1_phase2_encryption_algorithms}.
        :param tunnel1_phase2_integrity_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_integrity_algorithms VpnConnection#tunnel1_phase2_integrity_algorithms}.
        :param tunnel1_phase2_lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_lifetime_seconds VpnConnection#tunnel1_phase2_lifetime_seconds}.
        :param tunnel1_preshared_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_preshared_key VpnConnection#tunnel1_preshared_key}.
        :param tunnel1_rekey_fuzz_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_rekey_fuzz_percentage VpnConnection#tunnel1_rekey_fuzz_percentage}.
        :param tunnel1_rekey_margin_time_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_rekey_margin_time_seconds VpnConnection#tunnel1_rekey_margin_time_seconds}.
        :param tunnel1_replay_window_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_replay_window_size VpnConnection#tunnel1_replay_window_size}.
        :param tunnel1_startup_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_startup_action VpnConnection#tunnel1_startup_action}.
        :param tunnel2_dpd_timeout_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_dpd_timeout_action VpnConnection#tunnel2_dpd_timeout_action}.
        :param tunnel2_dpd_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_dpd_timeout_seconds VpnConnection#tunnel2_dpd_timeout_seconds}.
        :param tunnel2_ike_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_ike_versions VpnConnection#tunnel2_ike_versions}.
        :param tunnel2_inside_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_inside_cidr VpnConnection#tunnel2_inside_cidr}.
        :param tunnel2_inside_ipv6_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_inside_ipv6_cidr VpnConnection#tunnel2_inside_ipv6_cidr}.
        :param tunnel2_log_options: tunnel2_log_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_log_options VpnConnection#tunnel2_log_options}
        :param tunnel2_phase1_dh_group_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_dh_group_numbers VpnConnection#tunnel2_phase1_dh_group_numbers}.
        :param tunnel2_phase1_encryption_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_encryption_algorithms VpnConnection#tunnel2_phase1_encryption_algorithms}.
        :param tunnel2_phase1_integrity_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_integrity_algorithms VpnConnection#tunnel2_phase1_integrity_algorithms}.
        :param tunnel2_phase1_lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_lifetime_seconds VpnConnection#tunnel2_phase1_lifetime_seconds}.
        :param tunnel2_phase2_dh_group_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_dh_group_numbers VpnConnection#tunnel2_phase2_dh_group_numbers}.
        :param tunnel2_phase2_encryption_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_encryption_algorithms VpnConnection#tunnel2_phase2_encryption_algorithms}.
        :param tunnel2_phase2_integrity_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_integrity_algorithms VpnConnection#tunnel2_phase2_integrity_algorithms}.
        :param tunnel2_phase2_lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_lifetime_seconds VpnConnection#tunnel2_phase2_lifetime_seconds}.
        :param tunnel2_preshared_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_preshared_key VpnConnection#tunnel2_preshared_key}.
        :param tunnel2_rekey_fuzz_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_rekey_fuzz_percentage VpnConnection#tunnel2_rekey_fuzz_percentage}.
        :param tunnel2_rekey_margin_time_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_rekey_margin_time_seconds VpnConnection#tunnel2_rekey_margin_time_seconds}.
        :param tunnel2_replay_window_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_replay_window_size VpnConnection#tunnel2_replay_window_size}.
        :param tunnel2_startup_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_startup_action VpnConnection#tunnel2_startup_action}.
        :param tunnel_inside_ip_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel_inside_ip_version VpnConnection#tunnel_inside_ip_version}.
        :param vpn_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#vpn_gateway_id VpnConnection#vpn_gateway_id}.
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
                customer_gateway_id: builtins.str,
                type: builtins.str,
                enable_acceleration: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                id: typing.Optional[builtins.str] = None,
                local_ipv4_network_cidr: typing.Optional[builtins.str] = None,
                local_ipv6_network_cidr: typing.Optional[builtins.str] = None,
                outside_ip_address_type: typing.Optional[builtins.str] = None,
                remote_ipv4_network_cidr: typing.Optional[builtins.str] = None,
                remote_ipv6_network_cidr: typing.Optional[builtins.str] = None,
                static_routes_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                transit_gateway_id: typing.Optional[builtins.str] = None,
                transport_transit_gateway_attachment_id: typing.Optional[builtins.str] = None,
                tunnel1_dpd_timeout_action: typing.Optional[builtins.str] = None,
                tunnel1_dpd_timeout_seconds: typing.Optional[jsii.Number] = None,
                tunnel1_ike_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel1_inside_cidr: typing.Optional[builtins.str] = None,
                tunnel1_inside_ipv6_cidr: typing.Optional[builtins.str] = None,
                tunnel1_log_options: typing.Optional[typing.Union[VpnConnectionTunnel1LogOptions, typing.Dict[str, typing.Any]]] = None,
                tunnel1_phase1_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
                tunnel1_phase1_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel1_phase1_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel1_phase1_lifetime_seconds: typing.Optional[jsii.Number] = None,
                tunnel1_phase2_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
                tunnel1_phase2_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel1_phase2_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel1_phase2_lifetime_seconds: typing.Optional[jsii.Number] = None,
                tunnel1_preshared_key: typing.Optional[builtins.str] = None,
                tunnel1_rekey_fuzz_percentage: typing.Optional[jsii.Number] = None,
                tunnel1_rekey_margin_time_seconds: typing.Optional[jsii.Number] = None,
                tunnel1_replay_window_size: typing.Optional[jsii.Number] = None,
                tunnel1_startup_action: typing.Optional[builtins.str] = None,
                tunnel2_dpd_timeout_action: typing.Optional[builtins.str] = None,
                tunnel2_dpd_timeout_seconds: typing.Optional[jsii.Number] = None,
                tunnel2_ike_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel2_inside_cidr: typing.Optional[builtins.str] = None,
                tunnel2_inside_ipv6_cidr: typing.Optional[builtins.str] = None,
                tunnel2_log_options: typing.Optional[typing.Union[VpnConnectionTunnel2LogOptions, typing.Dict[str, typing.Any]]] = None,
                tunnel2_phase1_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
                tunnel2_phase1_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel2_phase1_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel2_phase1_lifetime_seconds: typing.Optional[jsii.Number] = None,
                tunnel2_phase2_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
                tunnel2_phase2_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel2_phase2_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel2_phase2_lifetime_seconds: typing.Optional[jsii.Number] = None,
                tunnel2_preshared_key: typing.Optional[builtins.str] = None,
                tunnel2_rekey_fuzz_percentage: typing.Optional[jsii.Number] = None,
                tunnel2_rekey_margin_time_seconds: typing.Optional[jsii.Number] = None,
                tunnel2_replay_window_size: typing.Optional[jsii.Number] = None,
                tunnel2_startup_action: typing.Optional[builtins.str] = None,
                tunnel_inside_ip_version: typing.Optional[builtins.str] = None,
                vpn_gateway_id: typing.Optional[builtins.str] = None,
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
        config = VpnConnectionConfig(
            customer_gateway_id=customer_gateway_id,
            type=type,
            enable_acceleration=enable_acceleration,
            id=id,
            local_ipv4_network_cidr=local_ipv4_network_cidr,
            local_ipv6_network_cidr=local_ipv6_network_cidr,
            outside_ip_address_type=outside_ip_address_type,
            remote_ipv4_network_cidr=remote_ipv4_network_cidr,
            remote_ipv6_network_cidr=remote_ipv6_network_cidr,
            static_routes_only=static_routes_only,
            tags=tags,
            tags_all=tags_all,
            transit_gateway_id=transit_gateway_id,
            transport_transit_gateway_attachment_id=transport_transit_gateway_attachment_id,
            tunnel1_dpd_timeout_action=tunnel1_dpd_timeout_action,
            tunnel1_dpd_timeout_seconds=tunnel1_dpd_timeout_seconds,
            tunnel1_ike_versions=tunnel1_ike_versions,
            tunnel1_inside_cidr=tunnel1_inside_cidr,
            tunnel1_inside_ipv6_cidr=tunnel1_inside_ipv6_cidr,
            tunnel1_log_options=tunnel1_log_options,
            tunnel1_phase1_dh_group_numbers=tunnel1_phase1_dh_group_numbers,
            tunnel1_phase1_encryption_algorithms=tunnel1_phase1_encryption_algorithms,
            tunnel1_phase1_integrity_algorithms=tunnel1_phase1_integrity_algorithms,
            tunnel1_phase1_lifetime_seconds=tunnel1_phase1_lifetime_seconds,
            tunnel1_phase2_dh_group_numbers=tunnel1_phase2_dh_group_numbers,
            tunnel1_phase2_encryption_algorithms=tunnel1_phase2_encryption_algorithms,
            tunnel1_phase2_integrity_algorithms=tunnel1_phase2_integrity_algorithms,
            tunnel1_phase2_lifetime_seconds=tunnel1_phase2_lifetime_seconds,
            tunnel1_preshared_key=tunnel1_preshared_key,
            tunnel1_rekey_fuzz_percentage=tunnel1_rekey_fuzz_percentage,
            tunnel1_rekey_margin_time_seconds=tunnel1_rekey_margin_time_seconds,
            tunnel1_replay_window_size=tunnel1_replay_window_size,
            tunnel1_startup_action=tunnel1_startup_action,
            tunnel2_dpd_timeout_action=tunnel2_dpd_timeout_action,
            tunnel2_dpd_timeout_seconds=tunnel2_dpd_timeout_seconds,
            tunnel2_ike_versions=tunnel2_ike_versions,
            tunnel2_inside_cidr=tunnel2_inside_cidr,
            tunnel2_inside_ipv6_cidr=tunnel2_inside_ipv6_cidr,
            tunnel2_log_options=tunnel2_log_options,
            tunnel2_phase1_dh_group_numbers=tunnel2_phase1_dh_group_numbers,
            tunnel2_phase1_encryption_algorithms=tunnel2_phase1_encryption_algorithms,
            tunnel2_phase1_integrity_algorithms=tunnel2_phase1_integrity_algorithms,
            tunnel2_phase1_lifetime_seconds=tunnel2_phase1_lifetime_seconds,
            tunnel2_phase2_dh_group_numbers=tunnel2_phase2_dh_group_numbers,
            tunnel2_phase2_encryption_algorithms=tunnel2_phase2_encryption_algorithms,
            tunnel2_phase2_integrity_algorithms=tunnel2_phase2_integrity_algorithms,
            tunnel2_phase2_lifetime_seconds=tunnel2_phase2_lifetime_seconds,
            tunnel2_preshared_key=tunnel2_preshared_key,
            tunnel2_rekey_fuzz_percentage=tunnel2_rekey_fuzz_percentage,
            tunnel2_rekey_margin_time_seconds=tunnel2_rekey_margin_time_seconds,
            tunnel2_replay_window_size=tunnel2_replay_window_size,
            tunnel2_startup_action=tunnel2_startup_action,
            tunnel_inside_ip_version=tunnel_inside_ip_version,
            vpn_gateway_id=vpn_gateway_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTunnel1LogOptions")
    def put_tunnel1_log_options(
        self,
        *,
        cloudwatch_log_options: typing.Optional[typing.Union["VpnConnectionTunnel1LogOptionsCloudwatchLogOptions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_log_options: cloudwatch_log_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#cloudwatch_log_options VpnConnection#cloudwatch_log_options}
        '''
        value = VpnConnectionTunnel1LogOptions(
            cloudwatch_log_options=cloudwatch_log_options
        )

        return typing.cast(None, jsii.invoke(self, "putTunnel1LogOptions", [value]))

    @jsii.member(jsii_name="putTunnel2LogOptions")
    def put_tunnel2_log_options(
        self,
        *,
        cloudwatch_log_options: typing.Optional[typing.Union["VpnConnectionTunnel2LogOptionsCloudwatchLogOptions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_log_options: cloudwatch_log_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#cloudwatch_log_options VpnConnection#cloudwatch_log_options}
        '''
        value = VpnConnectionTunnel2LogOptions(
            cloudwatch_log_options=cloudwatch_log_options
        )

        return typing.cast(None, jsii.invoke(self, "putTunnel2LogOptions", [value]))

    @jsii.member(jsii_name="resetEnableAcceleration")
    def reset_enable_acceleration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAcceleration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocalIpv4NetworkCidr")
    def reset_local_ipv4_network_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalIpv4NetworkCidr", []))

    @jsii.member(jsii_name="resetLocalIpv6NetworkCidr")
    def reset_local_ipv6_network_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalIpv6NetworkCidr", []))

    @jsii.member(jsii_name="resetOutsideIpAddressType")
    def reset_outside_ip_address_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutsideIpAddressType", []))

    @jsii.member(jsii_name="resetRemoteIpv4NetworkCidr")
    def reset_remote_ipv4_network_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoteIpv4NetworkCidr", []))

    @jsii.member(jsii_name="resetRemoteIpv6NetworkCidr")
    def reset_remote_ipv6_network_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoteIpv6NetworkCidr", []))

    @jsii.member(jsii_name="resetStaticRoutesOnly")
    def reset_static_routes_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStaticRoutesOnly", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTransitGatewayId")
    def reset_transit_gateway_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransitGatewayId", []))

    @jsii.member(jsii_name="resetTransportTransitGatewayAttachmentId")
    def reset_transport_transit_gateway_attachment_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransportTransitGatewayAttachmentId", []))

    @jsii.member(jsii_name="resetTunnel1DpdTimeoutAction")
    def reset_tunnel1_dpd_timeout_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1DpdTimeoutAction", []))

    @jsii.member(jsii_name="resetTunnel1DpdTimeoutSeconds")
    def reset_tunnel1_dpd_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1DpdTimeoutSeconds", []))

    @jsii.member(jsii_name="resetTunnel1IkeVersions")
    def reset_tunnel1_ike_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1IkeVersions", []))

    @jsii.member(jsii_name="resetTunnel1InsideCidr")
    def reset_tunnel1_inside_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1InsideCidr", []))

    @jsii.member(jsii_name="resetTunnel1InsideIpv6Cidr")
    def reset_tunnel1_inside_ipv6_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1InsideIpv6Cidr", []))

    @jsii.member(jsii_name="resetTunnel1LogOptions")
    def reset_tunnel1_log_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1LogOptions", []))

    @jsii.member(jsii_name="resetTunnel1Phase1DhGroupNumbers")
    def reset_tunnel1_phase1_dh_group_numbers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1Phase1DhGroupNumbers", []))

    @jsii.member(jsii_name="resetTunnel1Phase1EncryptionAlgorithms")
    def reset_tunnel1_phase1_encryption_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1Phase1EncryptionAlgorithms", []))

    @jsii.member(jsii_name="resetTunnel1Phase1IntegrityAlgorithms")
    def reset_tunnel1_phase1_integrity_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1Phase1IntegrityAlgorithms", []))

    @jsii.member(jsii_name="resetTunnel1Phase1LifetimeSeconds")
    def reset_tunnel1_phase1_lifetime_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1Phase1LifetimeSeconds", []))

    @jsii.member(jsii_name="resetTunnel1Phase2DhGroupNumbers")
    def reset_tunnel1_phase2_dh_group_numbers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1Phase2DhGroupNumbers", []))

    @jsii.member(jsii_name="resetTunnel1Phase2EncryptionAlgorithms")
    def reset_tunnel1_phase2_encryption_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1Phase2EncryptionAlgorithms", []))

    @jsii.member(jsii_name="resetTunnel1Phase2IntegrityAlgorithms")
    def reset_tunnel1_phase2_integrity_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1Phase2IntegrityAlgorithms", []))

    @jsii.member(jsii_name="resetTunnel1Phase2LifetimeSeconds")
    def reset_tunnel1_phase2_lifetime_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1Phase2LifetimeSeconds", []))

    @jsii.member(jsii_name="resetTunnel1PresharedKey")
    def reset_tunnel1_preshared_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1PresharedKey", []))

    @jsii.member(jsii_name="resetTunnel1RekeyFuzzPercentage")
    def reset_tunnel1_rekey_fuzz_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1RekeyFuzzPercentage", []))

    @jsii.member(jsii_name="resetTunnel1RekeyMarginTimeSeconds")
    def reset_tunnel1_rekey_margin_time_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1RekeyMarginTimeSeconds", []))

    @jsii.member(jsii_name="resetTunnel1ReplayWindowSize")
    def reset_tunnel1_replay_window_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1ReplayWindowSize", []))

    @jsii.member(jsii_name="resetTunnel1StartupAction")
    def reset_tunnel1_startup_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel1StartupAction", []))

    @jsii.member(jsii_name="resetTunnel2DpdTimeoutAction")
    def reset_tunnel2_dpd_timeout_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2DpdTimeoutAction", []))

    @jsii.member(jsii_name="resetTunnel2DpdTimeoutSeconds")
    def reset_tunnel2_dpd_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2DpdTimeoutSeconds", []))

    @jsii.member(jsii_name="resetTunnel2IkeVersions")
    def reset_tunnel2_ike_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2IkeVersions", []))

    @jsii.member(jsii_name="resetTunnel2InsideCidr")
    def reset_tunnel2_inside_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2InsideCidr", []))

    @jsii.member(jsii_name="resetTunnel2InsideIpv6Cidr")
    def reset_tunnel2_inside_ipv6_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2InsideIpv6Cidr", []))

    @jsii.member(jsii_name="resetTunnel2LogOptions")
    def reset_tunnel2_log_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2LogOptions", []))

    @jsii.member(jsii_name="resetTunnel2Phase1DhGroupNumbers")
    def reset_tunnel2_phase1_dh_group_numbers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2Phase1DhGroupNumbers", []))

    @jsii.member(jsii_name="resetTunnel2Phase1EncryptionAlgorithms")
    def reset_tunnel2_phase1_encryption_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2Phase1EncryptionAlgorithms", []))

    @jsii.member(jsii_name="resetTunnel2Phase1IntegrityAlgorithms")
    def reset_tunnel2_phase1_integrity_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2Phase1IntegrityAlgorithms", []))

    @jsii.member(jsii_name="resetTunnel2Phase1LifetimeSeconds")
    def reset_tunnel2_phase1_lifetime_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2Phase1LifetimeSeconds", []))

    @jsii.member(jsii_name="resetTunnel2Phase2DhGroupNumbers")
    def reset_tunnel2_phase2_dh_group_numbers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2Phase2DhGroupNumbers", []))

    @jsii.member(jsii_name="resetTunnel2Phase2EncryptionAlgorithms")
    def reset_tunnel2_phase2_encryption_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2Phase2EncryptionAlgorithms", []))

    @jsii.member(jsii_name="resetTunnel2Phase2IntegrityAlgorithms")
    def reset_tunnel2_phase2_integrity_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2Phase2IntegrityAlgorithms", []))

    @jsii.member(jsii_name="resetTunnel2Phase2LifetimeSeconds")
    def reset_tunnel2_phase2_lifetime_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2Phase2LifetimeSeconds", []))

    @jsii.member(jsii_name="resetTunnel2PresharedKey")
    def reset_tunnel2_preshared_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2PresharedKey", []))

    @jsii.member(jsii_name="resetTunnel2RekeyFuzzPercentage")
    def reset_tunnel2_rekey_fuzz_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2RekeyFuzzPercentage", []))

    @jsii.member(jsii_name="resetTunnel2RekeyMarginTimeSeconds")
    def reset_tunnel2_rekey_margin_time_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2RekeyMarginTimeSeconds", []))

    @jsii.member(jsii_name="resetTunnel2ReplayWindowSize")
    def reset_tunnel2_replay_window_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2ReplayWindowSize", []))

    @jsii.member(jsii_name="resetTunnel2StartupAction")
    def reset_tunnel2_startup_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnel2StartupAction", []))

    @jsii.member(jsii_name="resetTunnelInsideIpVersion")
    def reset_tunnel_inside_ip_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTunnelInsideIpVersion", []))

    @jsii.member(jsii_name="resetVpnGatewayId")
    def reset_vpn_gateway_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpnGatewayId", []))

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
    @jsii.member(jsii_name="coreNetworkArn")
    def core_network_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "coreNetworkArn"))

    @builtins.property
    @jsii.member(jsii_name="coreNetworkAttachmentArn")
    def core_network_attachment_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "coreNetworkAttachmentArn"))

    @builtins.property
    @jsii.member(jsii_name="customerGatewayConfiguration")
    def customer_gateway_configuration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerGatewayConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="routes")
    def routes(self) -> "VpnConnectionRoutesList":
        return typing.cast("VpnConnectionRoutesList", jsii.get(self, "routes"))

    @builtins.property
    @jsii.member(jsii_name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transitGatewayAttachmentId"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1Address")
    def tunnel1_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel1Address"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1BgpAsn")
    def tunnel1_bgp_asn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel1BgpAsn"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1BgpHoldtime")
    def tunnel1_bgp_holdtime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel1BgpHoldtime"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1CgwInsideAddress")
    def tunnel1_cgw_inside_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel1CgwInsideAddress"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1LogOptions")
    def tunnel1_log_options(self) -> "VpnConnectionTunnel1LogOptionsOutputReference":
        return typing.cast("VpnConnectionTunnel1LogOptionsOutputReference", jsii.get(self, "tunnel1LogOptions"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1VgwInsideAddress")
    def tunnel1_vgw_inside_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel1VgwInsideAddress"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2Address")
    def tunnel2_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel2Address"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2BgpAsn")
    def tunnel2_bgp_asn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel2BgpAsn"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2BgpHoldtime")
    def tunnel2_bgp_holdtime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel2BgpHoldtime"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2CgwInsideAddress")
    def tunnel2_cgw_inside_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel2CgwInsideAddress"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2LogOptions")
    def tunnel2_log_options(self) -> "VpnConnectionTunnel2LogOptionsOutputReference":
        return typing.cast("VpnConnectionTunnel2LogOptionsOutputReference", jsii.get(self, "tunnel2LogOptions"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2VgwInsideAddress")
    def tunnel2_vgw_inside_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel2VgwInsideAddress"))

    @builtins.property
    @jsii.member(jsii_name="vgwTelemetry")
    def vgw_telemetry(self) -> "VpnConnectionVgwTelemetryList":
        return typing.cast("VpnConnectionVgwTelemetryList", jsii.get(self, "vgwTelemetry"))

    @builtins.property
    @jsii.member(jsii_name="customerGatewayIdInput")
    def customer_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAccelerationInput")
    def enable_acceleration_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableAccelerationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="localIpv4NetworkCidrInput")
    def local_ipv4_network_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localIpv4NetworkCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="localIpv6NetworkCidrInput")
    def local_ipv6_network_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localIpv6NetworkCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="outsideIpAddressTypeInput")
    def outside_ip_address_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outsideIpAddressTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteIpv4NetworkCidrInput")
    def remote_ipv4_network_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remoteIpv4NetworkCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteIpv6NetworkCidrInput")
    def remote_ipv6_network_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remoteIpv6NetworkCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="staticRoutesOnlyInput")
    def static_routes_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "staticRoutesOnlyInput"))

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
    @jsii.member(jsii_name="transitGatewayIdInput")
    def transit_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transitGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="transportTransitGatewayAttachmentIdInput")
    def transport_transit_gateway_attachment_id_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transportTransitGatewayAttachmentIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1DpdTimeoutActionInput")
    def tunnel1_dpd_timeout_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel1DpdTimeoutActionInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1DpdTimeoutSecondsInput")
    def tunnel1_dpd_timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel1DpdTimeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1IkeVersionsInput")
    def tunnel1_ike_versions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel1IkeVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1InsideCidrInput")
    def tunnel1_inside_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel1InsideCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1InsideIpv6CidrInput")
    def tunnel1_inside_ipv6_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel1InsideIpv6CidrInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1LogOptionsInput")
    def tunnel1_log_options_input(
        self,
    ) -> typing.Optional["VpnConnectionTunnel1LogOptions"]:
        return typing.cast(typing.Optional["VpnConnectionTunnel1LogOptions"], jsii.get(self, "tunnel1LogOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase1DhGroupNumbersInput")
    def tunnel1_phase1_dh_group_numbers_input(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "tunnel1Phase1DhGroupNumbersInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase1EncryptionAlgorithmsInput")
    def tunnel1_phase1_encryption_algorithms_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel1Phase1EncryptionAlgorithmsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase1IntegrityAlgorithmsInput")
    def tunnel1_phase1_integrity_algorithms_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel1Phase1IntegrityAlgorithmsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase1LifetimeSecondsInput")
    def tunnel1_phase1_lifetime_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel1Phase1LifetimeSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase2DhGroupNumbersInput")
    def tunnel1_phase2_dh_group_numbers_input(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "tunnel1Phase2DhGroupNumbersInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase2EncryptionAlgorithmsInput")
    def tunnel1_phase2_encryption_algorithms_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel1Phase2EncryptionAlgorithmsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase2IntegrityAlgorithmsInput")
    def tunnel1_phase2_integrity_algorithms_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel1Phase2IntegrityAlgorithmsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase2LifetimeSecondsInput")
    def tunnel1_phase2_lifetime_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel1Phase2LifetimeSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1PresharedKeyInput")
    def tunnel1_preshared_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel1PresharedKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1RekeyFuzzPercentageInput")
    def tunnel1_rekey_fuzz_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel1RekeyFuzzPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1RekeyMarginTimeSecondsInput")
    def tunnel1_rekey_margin_time_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel1RekeyMarginTimeSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1ReplayWindowSizeInput")
    def tunnel1_replay_window_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel1ReplayWindowSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel1StartupActionInput")
    def tunnel1_startup_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel1StartupActionInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2DpdTimeoutActionInput")
    def tunnel2_dpd_timeout_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel2DpdTimeoutActionInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2DpdTimeoutSecondsInput")
    def tunnel2_dpd_timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel2DpdTimeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2IkeVersionsInput")
    def tunnel2_ike_versions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel2IkeVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2InsideCidrInput")
    def tunnel2_inside_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel2InsideCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2InsideIpv6CidrInput")
    def tunnel2_inside_ipv6_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel2InsideIpv6CidrInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2LogOptionsInput")
    def tunnel2_log_options_input(
        self,
    ) -> typing.Optional["VpnConnectionTunnel2LogOptions"]:
        return typing.cast(typing.Optional["VpnConnectionTunnel2LogOptions"], jsii.get(self, "tunnel2LogOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase1DhGroupNumbersInput")
    def tunnel2_phase1_dh_group_numbers_input(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "tunnel2Phase1DhGroupNumbersInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase1EncryptionAlgorithmsInput")
    def tunnel2_phase1_encryption_algorithms_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel2Phase1EncryptionAlgorithmsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase1IntegrityAlgorithmsInput")
    def tunnel2_phase1_integrity_algorithms_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel2Phase1IntegrityAlgorithmsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase1LifetimeSecondsInput")
    def tunnel2_phase1_lifetime_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel2Phase1LifetimeSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase2DhGroupNumbersInput")
    def tunnel2_phase2_dh_group_numbers_input(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "tunnel2Phase2DhGroupNumbersInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase2EncryptionAlgorithmsInput")
    def tunnel2_phase2_encryption_algorithms_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel2Phase2EncryptionAlgorithmsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase2IntegrityAlgorithmsInput")
    def tunnel2_phase2_integrity_algorithms_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tunnel2Phase2IntegrityAlgorithmsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase2LifetimeSecondsInput")
    def tunnel2_phase2_lifetime_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel2Phase2LifetimeSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2PresharedKeyInput")
    def tunnel2_preshared_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel2PresharedKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2RekeyFuzzPercentageInput")
    def tunnel2_rekey_fuzz_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel2RekeyFuzzPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2RekeyMarginTimeSecondsInput")
    def tunnel2_rekey_margin_time_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel2RekeyMarginTimeSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2ReplayWindowSizeInput")
    def tunnel2_replay_window_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tunnel2ReplayWindowSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnel2StartupActionInput")
    def tunnel2_startup_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnel2StartupActionInput"))

    @builtins.property
    @jsii.member(jsii_name="tunnelInsideIpVersionInput")
    def tunnel_inside_ip_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tunnelInsideIpVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnGatewayIdInput")
    def vpn_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpnGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="customerGatewayId")
    def customer_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerGatewayId"))

    @customer_gateway_id.setter
    def customer_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerGatewayId", value)

    @builtins.property
    @jsii.member(jsii_name="enableAcceleration")
    def enable_acceleration(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableAcceleration"))

    @enable_acceleration.setter
    def enable_acceleration(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAcceleration", value)

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
    @jsii.member(jsii_name="localIpv4NetworkCidr")
    def local_ipv4_network_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localIpv4NetworkCidr"))

    @local_ipv4_network_cidr.setter
    def local_ipv4_network_cidr(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localIpv4NetworkCidr", value)

    @builtins.property
    @jsii.member(jsii_name="localIpv6NetworkCidr")
    def local_ipv6_network_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localIpv6NetworkCidr"))

    @local_ipv6_network_cidr.setter
    def local_ipv6_network_cidr(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localIpv6NetworkCidr", value)

    @builtins.property
    @jsii.member(jsii_name="outsideIpAddressType")
    def outside_ip_address_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outsideIpAddressType"))

    @outside_ip_address_type.setter
    def outside_ip_address_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outsideIpAddressType", value)

    @builtins.property
    @jsii.member(jsii_name="remoteIpv4NetworkCidr")
    def remote_ipv4_network_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remoteIpv4NetworkCidr"))

    @remote_ipv4_network_cidr.setter
    def remote_ipv4_network_cidr(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteIpv4NetworkCidr", value)

    @builtins.property
    @jsii.member(jsii_name="remoteIpv6NetworkCidr")
    def remote_ipv6_network_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remoteIpv6NetworkCidr"))

    @remote_ipv6_network_cidr.setter
    def remote_ipv6_network_cidr(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteIpv6NetworkCidr", value)

    @builtins.property
    @jsii.member(jsii_name="staticRoutesOnly")
    def static_routes_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "staticRoutesOnly"))

    @static_routes_only.setter
    def static_routes_only(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "staticRoutesOnly", value)

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
    @jsii.member(jsii_name="transitGatewayId")
    def transit_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transitGatewayId"))

    @transit_gateway_id.setter
    def transit_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitGatewayId", value)

    @builtins.property
    @jsii.member(jsii_name="transportTransitGatewayAttachmentId")
    def transport_transit_gateway_attachment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transportTransitGatewayAttachmentId"))

    @transport_transit_gateway_attachment_id.setter
    def transport_transit_gateway_attachment_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transportTransitGatewayAttachmentId", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1DpdTimeoutAction")
    def tunnel1_dpd_timeout_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel1DpdTimeoutAction"))

    @tunnel1_dpd_timeout_action.setter
    def tunnel1_dpd_timeout_action(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1DpdTimeoutAction", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1DpdTimeoutSeconds")
    def tunnel1_dpd_timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel1DpdTimeoutSeconds"))

    @tunnel1_dpd_timeout_seconds.setter
    def tunnel1_dpd_timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1DpdTimeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1IkeVersions")
    def tunnel1_ike_versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel1IkeVersions"))

    @tunnel1_ike_versions.setter
    def tunnel1_ike_versions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1IkeVersions", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1InsideCidr")
    def tunnel1_inside_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel1InsideCidr"))

    @tunnel1_inside_cidr.setter
    def tunnel1_inside_cidr(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1InsideCidr", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1InsideIpv6Cidr")
    def tunnel1_inside_ipv6_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel1InsideIpv6Cidr"))

    @tunnel1_inside_ipv6_cidr.setter
    def tunnel1_inside_ipv6_cidr(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1InsideIpv6Cidr", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase1DhGroupNumbers")
    def tunnel1_phase1_dh_group_numbers(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "tunnel1Phase1DhGroupNumbers"))

    @tunnel1_phase1_dh_group_numbers.setter
    def tunnel1_phase1_dh_group_numbers(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            def stub(value: typing.List[jsii.Number]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1Phase1DhGroupNumbers", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase1EncryptionAlgorithms")
    def tunnel1_phase1_encryption_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel1Phase1EncryptionAlgorithms"))

    @tunnel1_phase1_encryption_algorithms.setter
    def tunnel1_phase1_encryption_algorithms(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1Phase1EncryptionAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase1IntegrityAlgorithms")
    def tunnel1_phase1_integrity_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel1Phase1IntegrityAlgorithms"))

    @tunnel1_phase1_integrity_algorithms.setter
    def tunnel1_phase1_integrity_algorithms(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1Phase1IntegrityAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase1LifetimeSeconds")
    def tunnel1_phase1_lifetime_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel1Phase1LifetimeSeconds"))

    @tunnel1_phase1_lifetime_seconds.setter
    def tunnel1_phase1_lifetime_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1Phase1LifetimeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase2DhGroupNumbers")
    def tunnel1_phase2_dh_group_numbers(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "tunnel1Phase2DhGroupNumbers"))

    @tunnel1_phase2_dh_group_numbers.setter
    def tunnel1_phase2_dh_group_numbers(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            def stub(value: typing.List[jsii.Number]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1Phase2DhGroupNumbers", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase2EncryptionAlgorithms")
    def tunnel1_phase2_encryption_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel1Phase2EncryptionAlgorithms"))

    @tunnel1_phase2_encryption_algorithms.setter
    def tunnel1_phase2_encryption_algorithms(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1Phase2EncryptionAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase2IntegrityAlgorithms")
    def tunnel1_phase2_integrity_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel1Phase2IntegrityAlgorithms"))

    @tunnel1_phase2_integrity_algorithms.setter
    def tunnel1_phase2_integrity_algorithms(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1Phase2IntegrityAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1Phase2LifetimeSeconds")
    def tunnel1_phase2_lifetime_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel1Phase2LifetimeSeconds"))

    @tunnel1_phase2_lifetime_seconds.setter
    def tunnel1_phase2_lifetime_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1Phase2LifetimeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1PresharedKey")
    def tunnel1_preshared_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel1PresharedKey"))

    @tunnel1_preshared_key.setter
    def tunnel1_preshared_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1PresharedKey", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1RekeyFuzzPercentage")
    def tunnel1_rekey_fuzz_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel1RekeyFuzzPercentage"))

    @tunnel1_rekey_fuzz_percentage.setter
    def tunnel1_rekey_fuzz_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1RekeyFuzzPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1RekeyMarginTimeSeconds")
    def tunnel1_rekey_margin_time_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel1RekeyMarginTimeSeconds"))

    @tunnel1_rekey_margin_time_seconds.setter
    def tunnel1_rekey_margin_time_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1RekeyMarginTimeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1ReplayWindowSize")
    def tunnel1_replay_window_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel1ReplayWindowSize"))

    @tunnel1_replay_window_size.setter
    def tunnel1_replay_window_size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1ReplayWindowSize", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel1StartupAction")
    def tunnel1_startup_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel1StartupAction"))

    @tunnel1_startup_action.setter
    def tunnel1_startup_action(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel1StartupAction", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2DpdTimeoutAction")
    def tunnel2_dpd_timeout_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel2DpdTimeoutAction"))

    @tunnel2_dpd_timeout_action.setter
    def tunnel2_dpd_timeout_action(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2DpdTimeoutAction", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2DpdTimeoutSeconds")
    def tunnel2_dpd_timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel2DpdTimeoutSeconds"))

    @tunnel2_dpd_timeout_seconds.setter
    def tunnel2_dpd_timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2DpdTimeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2IkeVersions")
    def tunnel2_ike_versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel2IkeVersions"))

    @tunnel2_ike_versions.setter
    def tunnel2_ike_versions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2IkeVersions", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2InsideCidr")
    def tunnel2_inside_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel2InsideCidr"))

    @tunnel2_inside_cidr.setter
    def tunnel2_inside_cidr(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2InsideCidr", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2InsideIpv6Cidr")
    def tunnel2_inside_ipv6_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel2InsideIpv6Cidr"))

    @tunnel2_inside_ipv6_cidr.setter
    def tunnel2_inside_ipv6_cidr(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2InsideIpv6Cidr", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase1DhGroupNumbers")
    def tunnel2_phase1_dh_group_numbers(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "tunnel2Phase1DhGroupNumbers"))

    @tunnel2_phase1_dh_group_numbers.setter
    def tunnel2_phase1_dh_group_numbers(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            def stub(value: typing.List[jsii.Number]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2Phase1DhGroupNumbers", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase1EncryptionAlgorithms")
    def tunnel2_phase1_encryption_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel2Phase1EncryptionAlgorithms"))

    @tunnel2_phase1_encryption_algorithms.setter
    def tunnel2_phase1_encryption_algorithms(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2Phase1EncryptionAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase1IntegrityAlgorithms")
    def tunnel2_phase1_integrity_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel2Phase1IntegrityAlgorithms"))

    @tunnel2_phase1_integrity_algorithms.setter
    def tunnel2_phase1_integrity_algorithms(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2Phase1IntegrityAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase1LifetimeSeconds")
    def tunnel2_phase1_lifetime_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel2Phase1LifetimeSeconds"))

    @tunnel2_phase1_lifetime_seconds.setter
    def tunnel2_phase1_lifetime_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2Phase1LifetimeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase2DhGroupNumbers")
    def tunnel2_phase2_dh_group_numbers(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "tunnel2Phase2DhGroupNumbers"))

    @tunnel2_phase2_dh_group_numbers.setter
    def tunnel2_phase2_dh_group_numbers(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            def stub(value: typing.List[jsii.Number]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2Phase2DhGroupNumbers", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase2EncryptionAlgorithms")
    def tunnel2_phase2_encryption_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel2Phase2EncryptionAlgorithms"))

    @tunnel2_phase2_encryption_algorithms.setter
    def tunnel2_phase2_encryption_algorithms(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2Phase2EncryptionAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase2IntegrityAlgorithms")
    def tunnel2_phase2_integrity_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnel2Phase2IntegrityAlgorithms"))

    @tunnel2_phase2_integrity_algorithms.setter
    def tunnel2_phase2_integrity_algorithms(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2Phase2IntegrityAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2Phase2LifetimeSeconds")
    def tunnel2_phase2_lifetime_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel2Phase2LifetimeSeconds"))

    @tunnel2_phase2_lifetime_seconds.setter
    def tunnel2_phase2_lifetime_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2Phase2LifetimeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2PresharedKey")
    def tunnel2_preshared_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel2PresharedKey"))

    @tunnel2_preshared_key.setter
    def tunnel2_preshared_key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2PresharedKey", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2RekeyFuzzPercentage")
    def tunnel2_rekey_fuzz_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel2RekeyFuzzPercentage"))

    @tunnel2_rekey_fuzz_percentage.setter
    def tunnel2_rekey_fuzz_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2RekeyFuzzPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2RekeyMarginTimeSeconds")
    def tunnel2_rekey_margin_time_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel2RekeyMarginTimeSeconds"))

    @tunnel2_rekey_margin_time_seconds.setter
    def tunnel2_rekey_margin_time_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2RekeyMarginTimeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2ReplayWindowSize")
    def tunnel2_replay_window_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tunnel2ReplayWindowSize"))

    @tunnel2_replay_window_size.setter
    def tunnel2_replay_window_size(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2ReplayWindowSize", value)

    @builtins.property
    @jsii.member(jsii_name="tunnel2StartupAction")
    def tunnel2_startup_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnel2StartupAction"))

    @tunnel2_startup_action.setter
    def tunnel2_startup_action(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnel2StartupAction", value)

    @builtins.property
    @jsii.member(jsii_name="tunnelInsideIpVersion")
    def tunnel_inside_ip_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnelInsideIpVersion"))

    @tunnel_inside_ip_version.setter
    def tunnel_inside_ip_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tunnelInsideIpVersion", value)

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
    @jsii.member(jsii_name="vpnGatewayId")
    def vpn_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpnGatewayId"))

    @vpn_gateway_id.setter
    def vpn_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnGatewayId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.vpnConnection.VpnConnectionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "customer_gateway_id": "customerGatewayId",
        "type": "type",
        "enable_acceleration": "enableAcceleration",
        "id": "id",
        "local_ipv4_network_cidr": "localIpv4NetworkCidr",
        "local_ipv6_network_cidr": "localIpv6NetworkCidr",
        "outside_ip_address_type": "outsideIpAddressType",
        "remote_ipv4_network_cidr": "remoteIpv4NetworkCidr",
        "remote_ipv6_network_cidr": "remoteIpv6NetworkCidr",
        "static_routes_only": "staticRoutesOnly",
        "tags": "tags",
        "tags_all": "tagsAll",
        "transit_gateway_id": "transitGatewayId",
        "transport_transit_gateway_attachment_id": "transportTransitGatewayAttachmentId",
        "tunnel1_dpd_timeout_action": "tunnel1DpdTimeoutAction",
        "tunnel1_dpd_timeout_seconds": "tunnel1DpdTimeoutSeconds",
        "tunnel1_ike_versions": "tunnel1IkeVersions",
        "tunnel1_inside_cidr": "tunnel1InsideCidr",
        "tunnel1_inside_ipv6_cidr": "tunnel1InsideIpv6Cidr",
        "tunnel1_log_options": "tunnel1LogOptions",
        "tunnel1_phase1_dh_group_numbers": "tunnel1Phase1DhGroupNumbers",
        "tunnel1_phase1_encryption_algorithms": "tunnel1Phase1EncryptionAlgorithms",
        "tunnel1_phase1_integrity_algorithms": "tunnel1Phase1IntegrityAlgorithms",
        "tunnel1_phase1_lifetime_seconds": "tunnel1Phase1LifetimeSeconds",
        "tunnel1_phase2_dh_group_numbers": "tunnel1Phase2DhGroupNumbers",
        "tunnel1_phase2_encryption_algorithms": "tunnel1Phase2EncryptionAlgorithms",
        "tunnel1_phase2_integrity_algorithms": "tunnel1Phase2IntegrityAlgorithms",
        "tunnel1_phase2_lifetime_seconds": "tunnel1Phase2LifetimeSeconds",
        "tunnel1_preshared_key": "tunnel1PresharedKey",
        "tunnel1_rekey_fuzz_percentage": "tunnel1RekeyFuzzPercentage",
        "tunnel1_rekey_margin_time_seconds": "tunnel1RekeyMarginTimeSeconds",
        "tunnel1_replay_window_size": "tunnel1ReplayWindowSize",
        "tunnel1_startup_action": "tunnel1StartupAction",
        "tunnel2_dpd_timeout_action": "tunnel2DpdTimeoutAction",
        "tunnel2_dpd_timeout_seconds": "tunnel2DpdTimeoutSeconds",
        "tunnel2_ike_versions": "tunnel2IkeVersions",
        "tunnel2_inside_cidr": "tunnel2InsideCidr",
        "tunnel2_inside_ipv6_cidr": "tunnel2InsideIpv6Cidr",
        "tunnel2_log_options": "tunnel2LogOptions",
        "tunnel2_phase1_dh_group_numbers": "tunnel2Phase1DhGroupNumbers",
        "tunnel2_phase1_encryption_algorithms": "tunnel2Phase1EncryptionAlgorithms",
        "tunnel2_phase1_integrity_algorithms": "tunnel2Phase1IntegrityAlgorithms",
        "tunnel2_phase1_lifetime_seconds": "tunnel2Phase1LifetimeSeconds",
        "tunnel2_phase2_dh_group_numbers": "tunnel2Phase2DhGroupNumbers",
        "tunnel2_phase2_encryption_algorithms": "tunnel2Phase2EncryptionAlgorithms",
        "tunnel2_phase2_integrity_algorithms": "tunnel2Phase2IntegrityAlgorithms",
        "tunnel2_phase2_lifetime_seconds": "tunnel2Phase2LifetimeSeconds",
        "tunnel2_preshared_key": "tunnel2PresharedKey",
        "tunnel2_rekey_fuzz_percentage": "tunnel2RekeyFuzzPercentage",
        "tunnel2_rekey_margin_time_seconds": "tunnel2RekeyMarginTimeSeconds",
        "tunnel2_replay_window_size": "tunnel2ReplayWindowSize",
        "tunnel2_startup_action": "tunnel2StartupAction",
        "tunnel_inside_ip_version": "tunnelInsideIpVersion",
        "vpn_gateway_id": "vpnGatewayId",
    },
)
class VpnConnectionConfig(cdktf.TerraformMetaArguments):
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
        customer_gateway_id: builtins.str,
        type: builtins.str,
        enable_acceleration: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        local_ipv4_network_cidr: typing.Optional[builtins.str] = None,
        local_ipv6_network_cidr: typing.Optional[builtins.str] = None,
        outside_ip_address_type: typing.Optional[builtins.str] = None,
        remote_ipv4_network_cidr: typing.Optional[builtins.str] = None,
        remote_ipv6_network_cidr: typing.Optional[builtins.str] = None,
        static_routes_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        transit_gateway_id: typing.Optional[builtins.str] = None,
        transport_transit_gateway_attachment_id: typing.Optional[builtins.str] = None,
        tunnel1_dpd_timeout_action: typing.Optional[builtins.str] = None,
        tunnel1_dpd_timeout_seconds: typing.Optional[jsii.Number] = None,
        tunnel1_ike_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_inside_cidr: typing.Optional[builtins.str] = None,
        tunnel1_inside_ipv6_cidr: typing.Optional[builtins.str] = None,
        tunnel1_log_options: typing.Optional[typing.Union["VpnConnectionTunnel1LogOptions", typing.Dict[str, typing.Any]]] = None,
        tunnel1_phase1_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        tunnel1_phase1_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_phase1_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_phase1_lifetime_seconds: typing.Optional[jsii.Number] = None,
        tunnel1_phase2_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        tunnel1_phase2_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_phase2_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel1_phase2_lifetime_seconds: typing.Optional[jsii.Number] = None,
        tunnel1_preshared_key: typing.Optional[builtins.str] = None,
        tunnel1_rekey_fuzz_percentage: typing.Optional[jsii.Number] = None,
        tunnel1_rekey_margin_time_seconds: typing.Optional[jsii.Number] = None,
        tunnel1_replay_window_size: typing.Optional[jsii.Number] = None,
        tunnel1_startup_action: typing.Optional[builtins.str] = None,
        tunnel2_dpd_timeout_action: typing.Optional[builtins.str] = None,
        tunnel2_dpd_timeout_seconds: typing.Optional[jsii.Number] = None,
        tunnel2_ike_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_inside_cidr: typing.Optional[builtins.str] = None,
        tunnel2_inside_ipv6_cidr: typing.Optional[builtins.str] = None,
        tunnel2_log_options: typing.Optional[typing.Union["VpnConnectionTunnel2LogOptions", typing.Dict[str, typing.Any]]] = None,
        tunnel2_phase1_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        tunnel2_phase1_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_phase1_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_phase1_lifetime_seconds: typing.Optional[jsii.Number] = None,
        tunnel2_phase2_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        tunnel2_phase2_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_phase2_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        tunnel2_phase2_lifetime_seconds: typing.Optional[jsii.Number] = None,
        tunnel2_preshared_key: typing.Optional[builtins.str] = None,
        tunnel2_rekey_fuzz_percentage: typing.Optional[jsii.Number] = None,
        tunnel2_rekey_margin_time_seconds: typing.Optional[jsii.Number] = None,
        tunnel2_replay_window_size: typing.Optional[jsii.Number] = None,
        tunnel2_startup_action: typing.Optional[builtins.str] = None,
        tunnel_inside_ip_version: typing.Optional[builtins.str] = None,
        vpn_gateway_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param customer_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#customer_gateway_id VpnConnection#customer_gateway_id}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#type VpnConnection#type}.
        :param enable_acceleration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#enable_acceleration VpnConnection#enable_acceleration}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#id VpnConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param local_ipv4_network_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#local_ipv4_network_cidr VpnConnection#local_ipv4_network_cidr}.
        :param local_ipv6_network_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#local_ipv6_network_cidr VpnConnection#local_ipv6_network_cidr}.
        :param outside_ip_address_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#outside_ip_address_type VpnConnection#outside_ip_address_type}.
        :param remote_ipv4_network_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#remote_ipv4_network_cidr VpnConnection#remote_ipv4_network_cidr}.
        :param remote_ipv6_network_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#remote_ipv6_network_cidr VpnConnection#remote_ipv6_network_cidr}.
        :param static_routes_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#static_routes_only VpnConnection#static_routes_only}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tags VpnConnection#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tags_all VpnConnection#tags_all}.
        :param transit_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#transit_gateway_id VpnConnection#transit_gateway_id}.
        :param transport_transit_gateway_attachment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#transport_transit_gateway_attachment_id VpnConnection#transport_transit_gateway_attachment_id}.
        :param tunnel1_dpd_timeout_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_dpd_timeout_action VpnConnection#tunnel1_dpd_timeout_action}.
        :param tunnel1_dpd_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_dpd_timeout_seconds VpnConnection#tunnel1_dpd_timeout_seconds}.
        :param tunnel1_ike_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_ike_versions VpnConnection#tunnel1_ike_versions}.
        :param tunnel1_inside_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_inside_cidr VpnConnection#tunnel1_inside_cidr}.
        :param tunnel1_inside_ipv6_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_inside_ipv6_cidr VpnConnection#tunnel1_inside_ipv6_cidr}.
        :param tunnel1_log_options: tunnel1_log_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_log_options VpnConnection#tunnel1_log_options}
        :param tunnel1_phase1_dh_group_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_dh_group_numbers VpnConnection#tunnel1_phase1_dh_group_numbers}.
        :param tunnel1_phase1_encryption_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_encryption_algorithms VpnConnection#tunnel1_phase1_encryption_algorithms}.
        :param tunnel1_phase1_integrity_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_integrity_algorithms VpnConnection#tunnel1_phase1_integrity_algorithms}.
        :param tunnel1_phase1_lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_lifetime_seconds VpnConnection#tunnel1_phase1_lifetime_seconds}.
        :param tunnel1_phase2_dh_group_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_dh_group_numbers VpnConnection#tunnel1_phase2_dh_group_numbers}.
        :param tunnel1_phase2_encryption_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_encryption_algorithms VpnConnection#tunnel1_phase2_encryption_algorithms}.
        :param tunnel1_phase2_integrity_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_integrity_algorithms VpnConnection#tunnel1_phase2_integrity_algorithms}.
        :param tunnel1_phase2_lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_lifetime_seconds VpnConnection#tunnel1_phase2_lifetime_seconds}.
        :param tunnel1_preshared_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_preshared_key VpnConnection#tunnel1_preshared_key}.
        :param tunnel1_rekey_fuzz_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_rekey_fuzz_percentage VpnConnection#tunnel1_rekey_fuzz_percentage}.
        :param tunnel1_rekey_margin_time_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_rekey_margin_time_seconds VpnConnection#tunnel1_rekey_margin_time_seconds}.
        :param tunnel1_replay_window_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_replay_window_size VpnConnection#tunnel1_replay_window_size}.
        :param tunnel1_startup_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_startup_action VpnConnection#tunnel1_startup_action}.
        :param tunnel2_dpd_timeout_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_dpd_timeout_action VpnConnection#tunnel2_dpd_timeout_action}.
        :param tunnel2_dpd_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_dpd_timeout_seconds VpnConnection#tunnel2_dpd_timeout_seconds}.
        :param tunnel2_ike_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_ike_versions VpnConnection#tunnel2_ike_versions}.
        :param tunnel2_inside_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_inside_cidr VpnConnection#tunnel2_inside_cidr}.
        :param tunnel2_inside_ipv6_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_inside_ipv6_cidr VpnConnection#tunnel2_inside_ipv6_cidr}.
        :param tunnel2_log_options: tunnel2_log_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_log_options VpnConnection#tunnel2_log_options}
        :param tunnel2_phase1_dh_group_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_dh_group_numbers VpnConnection#tunnel2_phase1_dh_group_numbers}.
        :param tunnel2_phase1_encryption_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_encryption_algorithms VpnConnection#tunnel2_phase1_encryption_algorithms}.
        :param tunnel2_phase1_integrity_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_integrity_algorithms VpnConnection#tunnel2_phase1_integrity_algorithms}.
        :param tunnel2_phase1_lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_lifetime_seconds VpnConnection#tunnel2_phase1_lifetime_seconds}.
        :param tunnel2_phase2_dh_group_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_dh_group_numbers VpnConnection#tunnel2_phase2_dh_group_numbers}.
        :param tunnel2_phase2_encryption_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_encryption_algorithms VpnConnection#tunnel2_phase2_encryption_algorithms}.
        :param tunnel2_phase2_integrity_algorithms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_integrity_algorithms VpnConnection#tunnel2_phase2_integrity_algorithms}.
        :param tunnel2_phase2_lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_lifetime_seconds VpnConnection#tunnel2_phase2_lifetime_seconds}.
        :param tunnel2_preshared_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_preshared_key VpnConnection#tunnel2_preshared_key}.
        :param tunnel2_rekey_fuzz_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_rekey_fuzz_percentage VpnConnection#tunnel2_rekey_fuzz_percentage}.
        :param tunnel2_rekey_margin_time_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_rekey_margin_time_seconds VpnConnection#tunnel2_rekey_margin_time_seconds}.
        :param tunnel2_replay_window_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_replay_window_size VpnConnection#tunnel2_replay_window_size}.
        :param tunnel2_startup_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_startup_action VpnConnection#tunnel2_startup_action}.
        :param tunnel_inside_ip_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel_inside_ip_version VpnConnection#tunnel_inside_ip_version}.
        :param vpn_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#vpn_gateway_id VpnConnection#vpn_gateway_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(tunnel1_log_options, dict):
            tunnel1_log_options = VpnConnectionTunnel1LogOptions(**tunnel1_log_options)
        if isinstance(tunnel2_log_options, dict):
            tunnel2_log_options = VpnConnectionTunnel2LogOptions(**tunnel2_log_options)
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
                customer_gateway_id: builtins.str,
                type: builtins.str,
                enable_acceleration: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                id: typing.Optional[builtins.str] = None,
                local_ipv4_network_cidr: typing.Optional[builtins.str] = None,
                local_ipv6_network_cidr: typing.Optional[builtins.str] = None,
                outside_ip_address_type: typing.Optional[builtins.str] = None,
                remote_ipv4_network_cidr: typing.Optional[builtins.str] = None,
                remote_ipv6_network_cidr: typing.Optional[builtins.str] = None,
                static_routes_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                transit_gateway_id: typing.Optional[builtins.str] = None,
                transport_transit_gateway_attachment_id: typing.Optional[builtins.str] = None,
                tunnel1_dpd_timeout_action: typing.Optional[builtins.str] = None,
                tunnel1_dpd_timeout_seconds: typing.Optional[jsii.Number] = None,
                tunnel1_ike_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel1_inside_cidr: typing.Optional[builtins.str] = None,
                tunnel1_inside_ipv6_cidr: typing.Optional[builtins.str] = None,
                tunnel1_log_options: typing.Optional[typing.Union[VpnConnectionTunnel1LogOptions, typing.Dict[str, typing.Any]]] = None,
                tunnel1_phase1_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
                tunnel1_phase1_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel1_phase1_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel1_phase1_lifetime_seconds: typing.Optional[jsii.Number] = None,
                tunnel1_phase2_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
                tunnel1_phase2_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel1_phase2_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel1_phase2_lifetime_seconds: typing.Optional[jsii.Number] = None,
                tunnel1_preshared_key: typing.Optional[builtins.str] = None,
                tunnel1_rekey_fuzz_percentage: typing.Optional[jsii.Number] = None,
                tunnel1_rekey_margin_time_seconds: typing.Optional[jsii.Number] = None,
                tunnel1_replay_window_size: typing.Optional[jsii.Number] = None,
                tunnel1_startup_action: typing.Optional[builtins.str] = None,
                tunnel2_dpd_timeout_action: typing.Optional[builtins.str] = None,
                tunnel2_dpd_timeout_seconds: typing.Optional[jsii.Number] = None,
                tunnel2_ike_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel2_inside_cidr: typing.Optional[builtins.str] = None,
                tunnel2_inside_ipv6_cidr: typing.Optional[builtins.str] = None,
                tunnel2_log_options: typing.Optional[typing.Union[VpnConnectionTunnel2LogOptions, typing.Dict[str, typing.Any]]] = None,
                tunnel2_phase1_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
                tunnel2_phase1_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel2_phase1_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel2_phase1_lifetime_seconds: typing.Optional[jsii.Number] = None,
                tunnel2_phase2_dh_group_numbers: typing.Optional[typing.Sequence[jsii.Number]] = None,
                tunnel2_phase2_encryption_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel2_phase2_integrity_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
                tunnel2_phase2_lifetime_seconds: typing.Optional[jsii.Number] = None,
                tunnel2_preshared_key: typing.Optional[builtins.str] = None,
                tunnel2_rekey_fuzz_percentage: typing.Optional[jsii.Number] = None,
                tunnel2_rekey_margin_time_seconds: typing.Optional[jsii.Number] = None,
                tunnel2_replay_window_size: typing.Optional[jsii.Number] = None,
                tunnel2_startup_action: typing.Optional[builtins.str] = None,
                tunnel_inside_ip_version: typing.Optional[builtins.str] = None,
                vpn_gateway_id: typing.Optional[builtins.str] = None,
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
            check_type(argname="argument customer_gateway_id", value=customer_gateway_id, expected_type=type_hints["customer_gateway_id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument enable_acceleration", value=enable_acceleration, expected_type=type_hints["enable_acceleration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument local_ipv4_network_cidr", value=local_ipv4_network_cidr, expected_type=type_hints["local_ipv4_network_cidr"])
            check_type(argname="argument local_ipv6_network_cidr", value=local_ipv6_network_cidr, expected_type=type_hints["local_ipv6_network_cidr"])
            check_type(argname="argument outside_ip_address_type", value=outside_ip_address_type, expected_type=type_hints["outside_ip_address_type"])
            check_type(argname="argument remote_ipv4_network_cidr", value=remote_ipv4_network_cidr, expected_type=type_hints["remote_ipv4_network_cidr"])
            check_type(argname="argument remote_ipv6_network_cidr", value=remote_ipv6_network_cidr, expected_type=type_hints["remote_ipv6_network_cidr"])
            check_type(argname="argument static_routes_only", value=static_routes_only, expected_type=type_hints["static_routes_only"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument transit_gateway_id", value=transit_gateway_id, expected_type=type_hints["transit_gateway_id"])
            check_type(argname="argument transport_transit_gateway_attachment_id", value=transport_transit_gateway_attachment_id, expected_type=type_hints["transport_transit_gateway_attachment_id"])
            check_type(argname="argument tunnel1_dpd_timeout_action", value=tunnel1_dpd_timeout_action, expected_type=type_hints["tunnel1_dpd_timeout_action"])
            check_type(argname="argument tunnel1_dpd_timeout_seconds", value=tunnel1_dpd_timeout_seconds, expected_type=type_hints["tunnel1_dpd_timeout_seconds"])
            check_type(argname="argument tunnel1_ike_versions", value=tunnel1_ike_versions, expected_type=type_hints["tunnel1_ike_versions"])
            check_type(argname="argument tunnel1_inside_cidr", value=tunnel1_inside_cidr, expected_type=type_hints["tunnel1_inside_cidr"])
            check_type(argname="argument tunnel1_inside_ipv6_cidr", value=tunnel1_inside_ipv6_cidr, expected_type=type_hints["tunnel1_inside_ipv6_cidr"])
            check_type(argname="argument tunnel1_log_options", value=tunnel1_log_options, expected_type=type_hints["tunnel1_log_options"])
            check_type(argname="argument tunnel1_phase1_dh_group_numbers", value=tunnel1_phase1_dh_group_numbers, expected_type=type_hints["tunnel1_phase1_dh_group_numbers"])
            check_type(argname="argument tunnel1_phase1_encryption_algorithms", value=tunnel1_phase1_encryption_algorithms, expected_type=type_hints["tunnel1_phase1_encryption_algorithms"])
            check_type(argname="argument tunnel1_phase1_integrity_algorithms", value=tunnel1_phase1_integrity_algorithms, expected_type=type_hints["tunnel1_phase1_integrity_algorithms"])
            check_type(argname="argument tunnel1_phase1_lifetime_seconds", value=tunnel1_phase1_lifetime_seconds, expected_type=type_hints["tunnel1_phase1_lifetime_seconds"])
            check_type(argname="argument tunnel1_phase2_dh_group_numbers", value=tunnel1_phase2_dh_group_numbers, expected_type=type_hints["tunnel1_phase2_dh_group_numbers"])
            check_type(argname="argument tunnel1_phase2_encryption_algorithms", value=tunnel1_phase2_encryption_algorithms, expected_type=type_hints["tunnel1_phase2_encryption_algorithms"])
            check_type(argname="argument tunnel1_phase2_integrity_algorithms", value=tunnel1_phase2_integrity_algorithms, expected_type=type_hints["tunnel1_phase2_integrity_algorithms"])
            check_type(argname="argument tunnel1_phase2_lifetime_seconds", value=tunnel1_phase2_lifetime_seconds, expected_type=type_hints["tunnel1_phase2_lifetime_seconds"])
            check_type(argname="argument tunnel1_preshared_key", value=tunnel1_preshared_key, expected_type=type_hints["tunnel1_preshared_key"])
            check_type(argname="argument tunnel1_rekey_fuzz_percentage", value=tunnel1_rekey_fuzz_percentage, expected_type=type_hints["tunnel1_rekey_fuzz_percentage"])
            check_type(argname="argument tunnel1_rekey_margin_time_seconds", value=tunnel1_rekey_margin_time_seconds, expected_type=type_hints["tunnel1_rekey_margin_time_seconds"])
            check_type(argname="argument tunnel1_replay_window_size", value=tunnel1_replay_window_size, expected_type=type_hints["tunnel1_replay_window_size"])
            check_type(argname="argument tunnel1_startup_action", value=tunnel1_startup_action, expected_type=type_hints["tunnel1_startup_action"])
            check_type(argname="argument tunnel2_dpd_timeout_action", value=tunnel2_dpd_timeout_action, expected_type=type_hints["tunnel2_dpd_timeout_action"])
            check_type(argname="argument tunnel2_dpd_timeout_seconds", value=tunnel2_dpd_timeout_seconds, expected_type=type_hints["tunnel2_dpd_timeout_seconds"])
            check_type(argname="argument tunnel2_ike_versions", value=tunnel2_ike_versions, expected_type=type_hints["tunnel2_ike_versions"])
            check_type(argname="argument tunnel2_inside_cidr", value=tunnel2_inside_cidr, expected_type=type_hints["tunnel2_inside_cidr"])
            check_type(argname="argument tunnel2_inside_ipv6_cidr", value=tunnel2_inside_ipv6_cidr, expected_type=type_hints["tunnel2_inside_ipv6_cidr"])
            check_type(argname="argument tunnel2_log_options", value=tunnel2_log_options, expected_type=type_hints["tunnel2_log_options"])
            check_type(argname="argument tunnel2_phase1_dh_group_numbers", value=tunnel2_phase1_dh_group_numbers, expected_type=type_hints["tunnel2_phase1_dh_group_numbers"])
            check_type(argname="argument tunnel2_phase1_encryption_algorithms", value=tunnel2_phase1_encryption_algorithms, expected_type=type_hints["tunnel2_phase1_encryption_algorithms"])
            check_type(argname="argument tunnel2_phase1_integrity_algorithms", value=tunnel2_phase1_integrity_algorithms, expected_type=type_hints["tunnel2_phase1_integrity_algorithms"])
            check_type(argname="argument tunnel2_phase1_lifetime_seconds", value=tunnel2_phase1_lifetime_seconds, expected_type=type_hints["tunnel2_phase1_lifetime_seconds"])
            check_type(argname="argument tunnel2_phase2_dh_group_numbers", value=tunnel2_phase2_dh_group_numbers, expected_type=type_hints["tunnel2_phase2_dh_group_numbers"])
            check_type(argname="argument tunnel2_phase2_encryption_algorithms", value=tunnel2_phase2_encryption_algorithms, expected_type=type_hints["tunnel2_phase2_encryption_algorithms"])
            check_type(argname="argument tunnel2_phase2_integrity_algorithms", value=tunnel2_phase2_integrity_algorithms, expected_type=type_hints["tunnel2_phase2_integrity_algorithms"])
            check_type(argname="argument tunnel2_phase2_lifetime_seconds", value=tunnel2_phase2_lifetime_seconds, expected_type=type_hints["tunnel2_phase2_lifetime_seconds"])
            check_type(argname="argument tunnel2_preshared_key", value=tunnel2_preshared_key, expected_type=type_hints["tunnel2_preshared_key"])
            check_type(argname="argument tunnel2_rekey_fuzz_percentage", value=tunnel2_rekey_fuzz_percentage, expected_type=type_hints["tunnel2_rekey_fuzz_percentage"])
            check_type(argname="argument tunnel2_rekey_margin_time_seconds", value=tunnel2_rekey_margin_time_seconds, expected_type=type_hints["tunnel2_rekey_margin_time_seconds"])
            check_type(argname="argument tunnel2_replay_window_size", value=tunnel2_replay_window_size, expected_type=type_hints["tunnel2_replay_window_size"])
            check_type(argname="argument tunnel2_startup_action", value=tunnel2_startup_action, expected_type=type_hints["tunnel2_startup_action"])
            check_type(argname="argument tunnel_inside_ip_version", value=tunnel_inside_ip_version, expected_type=type_hints["tunnel_inside_ip_version"])
            check_type(argname="argument vpn_gateway_id", value=vpn_gateway_id, expected_type=type_hints["vpn_gateway_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "customer_gateway_id": customer_gateway_id,
            "type": type,
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
        if enable_acceleration is not None:
            self._values["enable_acceleration"] = enable_acceleration
        if id is not None:
            self._values["id"] = id
        if local_ipv4_network_cidr is not None:
            self._values["local_ipv4_network_cidr"] = local_ipv4_network_cidr
        if local_ipv6_network_cidr is not None:
            self._values["local_ipv6_network_cidr"] = local_ipv6_network_cidr
        if outside_ip_address_type is not None:
            self._values["outside_ip_address_type"] = outside_ip_address_type
        if remote_ipv4_network_cidr is not None:
            self._values["remote_ipv4_network_cidr"] = remote_ipv4_network_cidr
        if remote_ipv6_network_cidr is not None:
            self._values["remote_ipv6_network_cidr"] = remote_ipv6_network_cidr
        if static_routes_only is not None:
            self._values["static_routes_only"] = static_routes_only
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if transit_gateway_id is not None:
            self._values["transit_gateway_id"] = transit_gateway_id
        if transport_transit_gateway_attachment_id is not None:
            self._values["transport_transit_gateway_attachment_id"] = transport_transit_gateway_attachment_id
        if tunnel1_dpd_timeout_action is not None:
            self._values["tunnel1_dpd_timeout_action"] = tunnel1_dpd_timeout_action
        if tunnel1_dpd_timeout_seconds is not None:
            self._values["tunnel1_dpd_timeout_seconds"] = tunnel1_dpd_timeout_seconds
        if tunnel1_ike_versions is not None:
            self._values["tunnel1_ike_versions"] = tunnel1_ike_versions
        if tunnel1_inside_cidr is not None:
            self._values["tunnel1_inside_cidr"] = tunnel1_inside_cidr
        if tunnel1_inside_ipv6_cidr is not None:
            self._values["tunnel1_inside_ipv6_cidr"] = tunnel1_inside_ipv6_cidr
        if tunnel1_log_options is not None:
            self._values["tunnel1_log_options"] = tunnel1_log_options
        if tunnel1_phase1_dh_group_numbers is not None:
            self._values["tunnel1_phase1_dh_group_numbers"] = tunnel1_phase1_dh_group_numbers
        if tunnel1_phase1_encryption_algorithms is not None:
            self._values["tunnel1_phase1_encryption_algorithms"] = tunnel1_phase1_encryption_algorithms
        if tunnel1_phase1_integrity_algorithms is not None:
            self._values["tunnel1_phase1_integrity_algorithms"] = tunnel1_phase1_integrity_algorithms
        if tunnel1_phase1_lifetime_seconds is not None:
            self._values["tunnel1_phase1_lifetime_seconds"] = tunnel1_phase1_lifetime_seconds
        if tunnel1_phase2_dh_group_numbers is not None:
            self._values["tunnel1_phase2_dh_group_numbers"] = tunnel1_phase2_dh_group_numbers
        if tunnel1_phase2_encryption_algorithms is not None:
            self._values["tunnel1_phase2_encryption_algorithms"] = tunnel1_phase2_encryption_algorithms
        if tunnel1_phase2_integrity_algorithms is not None:
            self._values["tunnel1_phase2_integrity_algorithms"] = tunnel1_phase2_integrity_algorithms
        if tunnel1_phase2_lifetime_seconds is not None:
            self._values["tunnel1_phase2_lifetime_seconds"] = tunnel1_phase2_lifetime_seconds
        if tunnel1_preshared_key is not None:
            self._values["tunnel1_preshared_key"] = tunnel1_preshared_key
        if tunnel1_rekey_fuzz_percentage is not None:
            self._values["tunnel1_rekey_fuzz_percentage"] = tunnel1_rekey_fuzz_percentage
        if tunnel1_rekey_margin_time_seconds is not None:
            self._values["tunnel1_rekey_margin_time_seconds"] = tunnel1_rekey_margin_time_seconds
        if tunnel1_replay_window_size is not None:
            self._values["tunnel1_replay_window_size"] = tunnel1_replay_window_size
        if tunnel1_startup_action is not None:
            self._values["tunnel1_startup_action"] = tunnel1_startup_action
        if tunnel2_dpd_timeout_action is not None:
            self._values["tunnel2_dpd_timeout_action"] = tunnel2_dpd_timeout_action
        if tunnel2_dpd_timeout_seconds is not None:
            self._values["tunnel2_dpd_timeout_seconds"] = tunnel2_dpd_timeout_seconds
        if tunnel2_ike_versions is not None:
            self._values["tunnel2_ike_versions"] = tunnel2_ike_versions
        if tunnel2_inside_cidr is not None:
            self._values["tunnel2_inside_cidr"] = tunnel2_inside_cidr
        if tunnel2_inside_ipv6_cidr is not None:
            self._values["tunnel2_inside_ipv6_cidr"] = tunnel2_inside_ipv6_cidr
        if tunnel2_log_options is not None:
            self._values["tunnel2_log_options"] = tunnel2_log_options
        if tunnel2_phase1_dh_group_numbers is not None:
            self._values["tunnel2_phase1_dh_group_numbers"] = tunnel2_phase1_dh_group_numbers
        if tunnel2_phase1_encryption_algorithms is not None:
            self._values["tunnel2_phase1_encryption_algorithms"] = tunnel2_phase1_encryption_algorithms
        if tunnel2_phase1_integrity_algorithms is not None:
            self._values["tunnel2_phase1_integrity_algorithms"] = tunnel2_phase1_integrity_algorithms
        if tunnel2_phase1_lifetime_seconds is not None:
            self._values["tunnel2_phase1_lifetime_seconds"] = tunnel2_phase1_lifetime_seconds
        if tunnel2_phase2_dh_group_numbers is not None:
            self._values["tunnel2_phase2_dh_group_numbers"] = tunnel2_phase2_dh_group_numbers
        if tunnel2_phase2_encryption_algorithms is not None:
            self._values["tunnel2_phase2_encryption_algorithms"] = tunnel2_phase2_encryption_algorithms
        if tunnel2_phase2_integrity_algorithms is not None:
            self._values["tunnel2_phase2_integrity_algorithms"] = tunnel2_phase2_integrity_algorithms
        if tunnel2_phase2_lifetime_seconds is not None:
            self._values["tunnel2_phase2_lifetime_seconds"] = tunnel2_phase2_lifetime_seconds
        if tunnel2_preshared_key is not None:
            self._values["tunnel2_preshared_key"] = tunnel2_preshared_key
        if tunnel2_rekey_fuzz_percentage is not None:
            self._values["tunnel2_rekey_fuzz_percentage"] = tunnel2_rekey_fuzz_percentage
        if tunnel2_rekey_margin_time_seconds is not None:
            self._values["tunnel2_rekey_margin_time_seconds"] = tunnel2_rekey_margin_time_seconds
        if tunnel2_replay_window_size is not None:
            self._values["tunnel2_replay_window_size"] = tunnel2_replay_window_size
        if tunnel2_startup_action is not None:
            self._values["tunnel2_startup_action"] = tunnel2_startup_action
        if tunnel_inside_ip_version is not None:
            self._values["tunnel_inside_ip_version"] = tunnel_inside_ip_version
        if vpn_gateway_id is not None:
            self._values["vpn_gateway_id"] = vpn_gateway_id

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
    def customer_gateway_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#customer_gateway_id VpnConnection#customer_gateway_id}.'''
        result = self._values.get("customer_gateway_id")
        assert result is not None, "Required property 'customer_gateway_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#type VpnConnection#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable_acceleration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#enable_acceleration VpnConnection#enable_acceleration}.'''
        result = self._values.get("enable_acceleration")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#id VpnConnection#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_ipv4_network_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#local_ipv4_network_cidr VpnConnection#local_ipv4_network_cidr}.'''
        result = self._values.get("local_ipv4_network_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_ipv6_network_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#local_ipv6_network_cidr VpnConnection#local_ipv6_network_cidr}.'''
        result = self._values.get("local_ipv6_network_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def outside_ip_address_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#outside_ip_address_type VpnConnection#outside_ip_address_type}.'''
        result = self._values.get("outside_ip_address_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remote_ipv4_network_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#remote_ipv4_network_cidr VpnConnection#remote_ipv4_network_cidr}.'''
        result = self._values.get("remote_ipv4_network_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remote_ipv6_network_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#remote_ipv6_network_cidr VpnConnection#remote_ipv6_network_cidr}.'''
        result = self._values.get("remote_ipv6_network_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def static_routes_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#static_routes_only VpnConnection#static_routes_only}.'''
        result = self._values.get("static_routes_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tags VpnConnection#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tags_all VpnConnection#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def transit_gateway_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#transit_gateway_id VpnConnection#transit_gateway_id}.'''
        result = self._values.get("transit_gateway_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transport_transit_gateway_attachment_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#transport_transit_gateway_attachment_id VpnConnection#transport_transit_gateway_attachment_id}.'''
        result = self._values.get("transport_transit_gateway_attachment_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel1_dpd_timeout_action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_dpd_timeout_action VpnConnection#tunnel1_dpd_timeout_action}.'''
        result = self._values.get("tunnel1_dpd_timeout_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel1_dpd_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_dpd_timeout_seconds VpnConnection#tunnel1_dpd_timeout_seconds}.'''
        result = self._values.get("tunnel1_dpd_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel1_ike_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_ike_versions VpnConnection#tunnel1_ike_versions}.'''
        result = self._values.get("tunnel1_ike_versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel1_inside_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_inside_cidr VpnConnection#tunnel1_inside_cidr}.'''
        result = self._values.get("tunnel1_inside_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel1_inside_ipv6_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_inside_ipv6_cidr VpnConnection#tunnel1_inside_ipv6_cidr}.'''
        result = self._values.get("tunnel1_inside_ipv6_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel1_log_options(self) -> typing.Optional["VpnConnectionTunnel1LogOptions"]:
        '''tunnel1_log_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_log_options VpnConnection#tunnel1_log_options}
        '''
        result = self._values.get("tunnel1_log_options")
        return typing.cast(typing.Optional["VpnConnectionTunnel1LogOptions"], result)

    @builtins.property
    def tunnel1_phase1_dh_group_numbers(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_dh_group_numbers VpnConnection#tunnel1_phase1_dh_group_numbers}.'''
        result = self._values.get("tunnel1_phase1_dh_group_numbers")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def tunnel1_phase1_encryption_algorithms(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_encryption_algorithms VpnConnection#tunnel1_phase1_encryption_algorithms}.'''
        result = self._values.get("tunnel1_phase1_encryption_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel1_phase1_integrity_algorithms(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_integrity_algorithms VpnConnection#tunnel1_phase1_integrity_algorithms}.'''
        result = self._values.get("tunnel1_phase1_integrity_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel1_phase1_lifetime_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase1_lifetime_seconds VpnConnection#tunnel1_phase1_lifetime_seconds}.'''
        result = self._values.get("tunnel1_phase1_lifetime_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel1_phase2_dh_group_numbers(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_dh_group_numbers VpnConnection#tunnel1_phase2_dh_group_numbers}.'''
        result = self._values.get("tunnel1_phase2_dh_group_numbers")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def tunnel1_phase2_encryption_algorithms(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_encryption_algorithms VpnConnection#tunnel1_phase2_encryption_algorithms}.'''
        result = self._values.get("tunnel1_phase2_encryption_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel1_phase2_integrity_algorithms(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_integrity_algorithms VpnConnection#tunnel1_phase2_integrity_algorithms}.'''
        result = self._values.get("tunnel1_phase2_integrity_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel1_phase2_lifetime_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_phase2_lifetime_seconds VpnConnection#tunnel1_phase2_lifetime_seconds}.'''
        result = self._values.get("tunnel1_phase2_lifetime_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel1_preshared_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_preshared_key VpnConnection#tunnel1_preshared_key}.'''
        result = self._values.get("tunnel1_preshared_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel1_rekey_fuzz_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_rekey_fuzz_percentage VpnConnection#tunnel1_rekey_fuzz_percentage}.'''
        result = self._values.get("tunnel1_rekey_fuzz_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel1_rekey_margin_time_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_rekey_margin_time_seconds VpnConnection#tunnel1_rekey_margin_time_seconds}.'''
        result = self._values.get("tunnel1_rekey_margin_time_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel1_replay_window_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_replay_window_size VpnConnection#tunnel1_replay_window_size}.'''
        result = self._values.get("tunnel1_replay_window_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel1_startup_action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel1_startup_action VpnConnection#tunnel1_startup_action}.'''
        result = self._values.get("tunnel1_startup_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel2_dpd_timeout_action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_dpd_timeout_action VpnConnection#tunnel2_dpd_timeout_action}.'''
        result = self._values.get("tunnel2_dpd_timeout_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel2_dpd_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_dpd_timeout_seconds VpnConnection#tunnel2_dpd_timeout_seconds}.'''
        result = self._values.get("tunnel2_dpd_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel2_ike_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_ike_versions VpnConnection#tunnel2_ike_versions}.'''
        result = self._values.get("tunnel2_ike_versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel2_inside_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_inside_cidr VpnConnection#tunnel2_inside_cidr}.'''
        result = self._values.get("tunnel2_inside_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel2_inside_ipv6_cidr(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_inside_ipv6_cidr VpnConnection#tunnel2_inside_ipv6_cidr}.'''
        result = self._values.get("tunnel2_inside_ipv6_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel2_log_options(self) -> typing.Optional["VpnConnectionTunnel2LogOptions"]:
        '''tunnel2_log_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_log_options VpnConnection#tunnel2_log_options}
        '''
        result = self._values.get("tunnel2_log_options")
        return typing.cast(typing.Optional["VpnConnectionTunnel2LogOptions"], result)

    @builtins.property
    def tunnel2_phase1_dh_group_numbers(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_dh_group_numbers VpnConnection#tunnel2_phase1_dh_group_numbers}.'''
        result = self._values.get("tunnel2_phase1_dh_group_numbers")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def tunnel2_phase1_encryption_algorithms(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_encryption_algorithms VpnConnection#tunnel2_phase1_encryption_algorithms}.'''
        result = self._values.get("tunnel2_phase1_encryption_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel2_phase1_integrity_algorithms(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_integrity_algorithms VpnConnection#tunnel2_phase1_integrity_algorithms}.'''
        result = self._values.get("tunnel2_phase1_integrity_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel2_phase1_lifetime_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase1_lifetime_seconds VpnConnection#tunnel2_phase1_lifetime_seconds}.'''
        result = self._values.get("tunnel2_phase1_lifetime_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel2_phase2_dh_group_numbers(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_dh_group_numbers VpnConnection#tunnel2_phase2_dh_group_numbers}.'''
        result = self._values.get("tunnel2_phase2_dh_group_numbers")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def tunnel2_phase2_encryption_algorithms(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_encryption_algorithms VpnConnection#tunnel2_phase2_encryption_algorithms}.'''
        result = self._values.get("tunnel2_phase2_encryption_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel2_phase2_integrity_algorithms(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_integrity_algorithms VpnConnection#tunnel2_phase2_integrity_algorithms}.'''
        result = self._values.get("tunnel2_phase2_integrity_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tunnel2_phase2_lifetime_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_phase2_lifetime_seconds VpnConnection#tunnel2_phase2_lifetime_seconds}.'''
        result = self._values.get("tunnel2_phase2_lifetime_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel2_preshared_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_preshared_key VpnConnection#tunnel2_preshared_key}.'''
        result = self._values.get("tunnel2_preshared_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel2_rekey_fuzz_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_rekey_fuzz_percentage VpnConnection#tunnel2_rekey_fuzz_percentage}.'''
        result = self._values.get("tunnel2_rekey_fuzz_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel2_rekey_margin_time_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_rekey_margin_time_seconds VpnConnection#tunnel2_rekey_margin_time_seconds}.'''
        result = self._values.get("tunnel2_rekey_margin_time_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel2_replay_window_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_replay_window_size VpnConnection#tunnel2_replay_window_size}.'''
        result = self._values.get("tunnel2_replay_window_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tunnel2_startup_action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel2_startup_action VpnConnection#tunnel2_startup_action}.'''
        result = self._values.get("tunnel2_startup_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tunnel_inside_ip_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#tunnel_inside_ip_version VpnConnection#tunnel_inside_ip_version}.'''
        result = self._values.get("tunnel_inside_ip_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpn_gateway_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#vpn_gateway_id VpnConnection#vpn_gateway_id}.'''
        result = self._values.get("vpn_gateway_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnConnectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.vpnConnection.VpnConnectionRoutes",
    jsii_struct_bases=[],
    name_mapping={},
)
class VpnConnectionRoutes:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnConnectionRoutes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnConnectionRoutesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.vpnConnection.VpnConnectionRoutesList",
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
    def get(self, index: jsii.Number) -> "VpnConnectionRoutesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VpnConnectionRoutesOutputReference", jsii.invoke(self, "get", [index]))

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


class VpnConnectionRoutesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.vpnConnection.VpnConnectionRoutesOutputReference",
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
    @jsii.member(jsii_name="destinationCidrBlock")
    def destination_cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationCidrBlock"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VpnConnectionRoutes]:
        return typing.cast(typing.Optional[VpnConnectionRoutes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[VpnConnectionRoutes]) -> None:
        if __debug__:
            def stub(value: typing.Optional[VpnConnectionRoutes]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.vpnConnection.VpnConnectionTunnel1LogOptions",
    jsii_struct_bases=[],
    name_mapping={"cloudwatch_log_options": "cloudwatchLogOptions"},
)
class VpnConnectionTunnel1LogOptions:
    def __init__(
        self,
        *,
        cloudwatch_log_options: typing.Optional[typing.Union["VpnConnectionTunnel1LogOptionsCloudwatchLogOptions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_log_options: cloudwatch_log_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#cloudwatch_log_options VpnConnection#cloudwatch_log_options}
        '''
        if isinstance(cloudwatch_log_options, dict):
            cloudwatch_log_options = VpnConnectionTunnel1LogOptionsCloudwatchLogOptions(**cloudwatch_log_options)
        if __debug__:
            def stub(
                *,
                cloudwatch_log_options: typing.Optional[typing.Union[VpnConnectionTunnel1LogOptionsCloudwatchLogOptions, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cloudwatch_log_options", value=cloudwatch_log_options, expected_type=type_hints["cloudwatch_log_options"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cloudwatch_log_options is not None:
            self._values["cloudwatch_log_options"] = cloudwatch_log_options

    @builtins.property
    def cloudwatch_log_options(
        self,
    ) -> typing.Optional["VpnConnectionTunnel1LogOptionsCloudwatchLogOptions"]:
        '''cloudwatch_log_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#cloudwatch_log_options VpnConnection#cloudwatch_log_options}
        '''
        result = self._values.get("cloudwatch_log_options")
        return typing.cast(typing.Optional["VpnConnectionTunnel1LogOptionsCloudwatchLogOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnConnectionTunnel1LogOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.vpnConnection.VpnConnectionTunnel1LogOptionsCloudwatchLogOptions",
    jsii_struct_bases=[],
    name_mapping={
        "log_enabled": "logEnabled",
        "log_group_arn": "logGroupArn",
        "log_output_format": "logOutputFormat",
    },
)
class VpnConnectionTunnel1LogOptionsCloudwatchLogOptions:
    def __init__(
        self,
        *,
        log_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_arn: typing.Optional[builtins.str] = None,
        log_output_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param log_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_enabled VpnConnection#log_enabled}.
        :param log_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_group_arn VpnConnection#log_group_arn}.
        :param log_output_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_output_format VpnConnection#log_output_format}.
        '''
        if __debug__:
            def stub(
                *,
                log_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                log_group_arn: typing.Optional[builtins.str] = None,
                log_output_format: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument log_enabled", value=log_enabled, expected_type=type_hints["log_enabled"])
            check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
            check_type(argname="argument log_output_format", value=log_output_format, expected_type=type_hints["log_output_format"])
        self._values: typing.Dict[str, typing.Any] = {}
        if log_enabled is not None:
            self._values["log_enabled"] = log_enabled
        if log_group_arn is not None:
            self._values["log_group_arn"] = log_group_arn
        if log_output_format is not None:
            self._values["log_output_format"] = log_output_format

    @builtins.property
    def log_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_enabled VpnConnection#log_enabled}.'''
        result = self._values.get("log_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def log_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_group_arn VpnConnection#log_group_arn}.'''
        result = self._values.get("log_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_output_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_output_format VpnConnection#log_output_format}.'''
        result = self._values.get("log_output_format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnConnectionTunnel1LogOptionsCloudwatchLogOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnConnectionTunnel1LogOptionsCloudwatchLogOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.vpnConnection.VpnConnectionTunnel1LogOptionsCloudwatchLogOptionsOutputReference",
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

    @jsii.member(jsii_name="resetLogEnabled")
    def reset_log_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogEnabled", []))

    @jsii.member(jsii_name="resetLogGroupArn")
    def reset_log_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupArn", []))

    @jsii.member(jsii_name="resetLogOutputFormat")
    def reset_log_output_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogOutputFormat", []))

    @builtins.property
    @jsii.member(jsii_name="logEnabledInput")
    def log_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "logEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupArnInput")
    def log_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="logOutputFormatInput")
    def log_output_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logOutputFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="logEnabled")
    def log_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "logEnabled"))

    @log_enabled.setter
    def log_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupArn")
    def log_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupArn"))

    @log_group_arn.setter
    def log_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="logOutputFormat")
    def log_output_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logOutputFormat"))

    @log_output_format.setter
    def log_output_format(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logOutputFormat", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VpnConnectionTunnel1LogOptionsCloudwatchLogOptions]:
        return typing.cast(typing.Optional[VpnConnectionTunnel1LogOptionsCloudwatchLogOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpnConnectionTunnel1LogOptionsCloudwatchLogOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[VpnConnectionTunnel1LogOptionsCloudwatchLogOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VpnConnectionTunnel1LogOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.vpnConnection.VpnConnectionTunnel1LogOptionsOutputReference",
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

    @jsii.member(jsii_name="putCloudwatchLogOptions")
    def put_cloudwatch_log_options(
        self,
        *,
        log_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_arn: typing.Optional[builtins.str] = None,
        log_output_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param log_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_enabled VpnConnection#log_enabled}.
        :param log_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_group_arn VpnConnection#log_group_arn}.
        :param log_output_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_output_format VpnConnection#log_output_format}.
        '''
        value = VpnConnectionTunnel1LogOptionsCloudwatchLogOptions(
            log_enabled=log_enabled,
            log_group_arn=log_group_arn,
            log_output_format=log_output_format,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLogOptions", [value]))

    @jsii.member(jsii_name="resetCloudwatchLogOptions")
    def reset_cloudwatch_log_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLogOptions", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogOptions")
    def cloudwatch_log_options(
        self,
    ) -> VpnConnectionTunnel1LogOptionsCloudwatchLogOptionsOutputReference:
        return typing.cast(VpnConnectionTunnel1LogOptionsCloudwatchLogOptionsOutputReference, jsii.get(self, "cloudwatchLogOptions"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogOptionsInput")
    def cloudwatch_log_options_input(
        self,
    ) -> typing.Optional[VpnConnectionTunnel1LogOptionsCloudwatchLogOptions]:
        return typing.cast(typing.Optional[VpnConnectionTunnel1LogOptionsCloudwatchLogOptions], jsii.get(self, "cloudwatchLogOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VpnConnectionTunnel1LogOptions]:
        return typing.cast(typing.Optional[VpnConnectionTunnel1LogOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpnConnectionTunnel1LogOptions],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[VpnConnectionTunnel1LogOptions]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.vpnConnection.VpnConnectionTunnel2LogOptions",
    jsii_struct_bases=[],
    name_mapping={"cloudwatch_log_options": "cloudwatchLogOptions"},
)
class VpnConnectionTunnel2LogOptions:
    def __init__(
        self,
        *,
        cloudwatch_log_options: typing.Optional[typing.Union["VpnConnectionTunnel2LogOptionsCloudwatchLogOptions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_log_options: cloudwatch_log_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#cloudwatch_log_options VpnConnection#cloudwatch_log_options}
        '''
        if isinstance(cloudwatch_log_options, dict):
            cloudwatch_log_options = VpnConnectionTunnel2LogOptionsCloudwatchLogOptions(**cloudwatch_log_options)
        if __debug__:
            def stub(
                *,
                cloudwatch_log_options: typing.Optional[typing.Union[VpnConnectionTunnel2LogOptionsCloudwatchLogOptions, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cloudwatch_log_options", value=cloudwatch_log_options, expected_type=type_hints["cloudwatch_log_options"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cloudwatch_log_options is not None:
            self._values["cloudwatch_log_options"] = cloudwatch_log_options

    @builtins.property
    def cloudwatch_log_options(
        self,
    ) -> typing.Optional["VpnConnectionTunnel2LogOptionsCloudwatchLogOptions"]:
        '''cloudwatch_log_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#cloudwatch_log_options VpnConnection#cloudwatch_log_options}
        '''
        result = self._values.get("cloudwatch_log_options")
        return typing.cast(typing.Optional["VpnConnectionTunnel2LogOptionsCloudwatchLogOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnConnectionTunnel2LogOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.vpnConnection.VpnConnectionTunnel2LogOptionsCloudwatchLogOptions",
    jsii_struct_bases=[],
    name_mapping={
        "log_enabled": "logEnabled",
        "log_group_arn": "logGroupArn",
        "log_output_format": "logOutputFormat",
    },
)
class VpnConnectionTunnel2LogOptionsCloudwatchLogOptions:
    def __init__(
        self,
        *,
        log_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_arn: typing.Optional[builtins.str] = None,
        log_output_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param log_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_enabled VpnConnection#log_enabled}.
        :param log_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_group_arn VpnConnection#log_group_arn}.
        :param log_output_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_output_format VpnConnection#log_output_format}.
        '''
        if __debug__:
            def stub(
                *,
                log_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                log_group_arn: typing.Optional[builtins.str] = None,
                log_output_format: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument log_enabled", value=log_enabled, expected_type=type_hints["log_enabled"])
            check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
            check_type(argname="argument log_output_format", value=log_output_format, expected_type=type_hints["log_output_format"])
        self._values: typing.Dict[str, typing.Any] = {}
        if log_enabled is not None:
            self._values["log_enabled"] = log_enabled
        if log_group_arn is not None:
            self._values["log_group_arn"] = log_group_arn
        if log_output_format is not None:
            self._values["log_output_format"] = log_output_format

    @builtins.property
    def log_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_enabled VpnConnection#log_enabled}.'''
        result = self._values.get("log_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def log_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_group_arn VpnConnection#log_group_arn}.'''
        result = self._values.get("log_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_output_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_output_format VpnConnection#log_output_format}.'''
        result = self._values.get("log_output_format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnConnectionTunnel2LogOptionsCloudwatchLogOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnConnectionTunnel2LogOptionsCloudwatchLogOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.vpnConnection.VpnConnectionTunnel2LogOptionsCloudwatchLogOptionsOutputReference",
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

    @jsii.member(jsii_name="resetLogEnabled")
    def reset_log_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogEnabled", []))

    @jsii.member(jsii_name="resetLogGroupArn")
    def reset_log_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogGroupArn", []))

    @jsii.member(jsii_name="resetLogOutputFormat")
    def reset_log_output_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogOutputFormat", []))

    @builtins.property
    @jsii.member(jsii_name="logEnabledInput")
    def log_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "logEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupArnInput")
    def log_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="logOutputFormatInput")
    def log_output_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logOutputFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="logEnabled")
    def log_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "logEnabled"))

    @log_enabled.setter
    def log_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupArn")
    def log_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupArn"))

    @log_group_arn.setter
    def log_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="logOutputFormat")
    def log_output_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logOutputFormat"))

    @log_output_format.setter
    def log_output_format(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logOutputFormat", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VpnConnectionTunnel2LogOptionsCloudwatchLogOptions]:
        return typing.cast(typing.Optional[VpnConnectionTunnel2LogOptionsCloudwatchLogOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpnConnectionTunnel2LogOptionsCloudwatchLogOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[VpnConnectionTunnel2LogOptionsCloudwatchLogOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VpnConnectionTunnel2LogOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.vpnConnection.VpnConnectionTunnel2LogOptionsOutputReference",
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

    @jsii.member(jsii_name="putCloudwatchLogOptions")
    def put_cloudwatch_log_options(
        self,
        *,
        log_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        log_group_arn: typing.Optional[builtins.str] = None,
        log_output_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param log_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_enabled VpnConnection#log_enabled}.
        :param log_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_group_arn VpnConnection#log_group_arn}.
        :param log_output_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/vpn_connection#log_output_format VpnConnection#log_output_format}.
        '''
        value = VpnConnectionTunnel2LogOptionsCloudwatchLogOptions(
            log_enabled=log_enabled,
            log_group_arn=log_group_arn,
            log_output_format=log_output_format,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLogOptions", [value]))

    @jsii.member(jsii_name="resetCloudwatchLogOptions")
    def reset_cloudwatch_log_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLogOptions", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogOptions")
    def cloudwatch_log_options(
        self,
    ) -> VpnConnectionTunnel2LogOptionsCloudwatchLogOptionsOutputReference:
        return typing.cast(VpnConnectionTunnel2LogOptionsCloudwatchLogOptionsOutputReference, jsii.get(self, "cloudwatchLogOptions"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogOptionsInput")
    def cloudwatch_log_options_input(
        self,
    ) -> typing.Optional[VpnConnectionTunnel2LogOptionsCloudwatchLogOptions]:
        return typing.cast(typing.Optional[VpnConnectionTunnel2LogOptionsCloudwatchLogOptions], jsii.get(self, "cloudwatchLogOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VpnConnectionTunnel2LogOptions]:
        return typing.cast(typing.Optional[VpnConnectionTunnel2LogOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpnConnectionTunnel2LogOptions],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[VpnConnectionTunnel2LogOptions]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.vpnConnection.VpnConnectionVgwTelemetry",
    jsii_struct_bases=[],
    name_mapping={},
)
class VpnConnectionVgwTelemetry:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnConnectionVgwTelemetry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnConnectionVgwTelemetryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.vpnConnection.VpnConnectionVgwTelemetryList",
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
    def get(self, index: jsii.Number) -> "VpnConnectionVgwTelemetryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VpnConnectionVgwTelemetryOutputReference", jsii.invoke(self, "get", [index]))

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


class VpnConnectionVgwTelemetryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.vpnConnection.VpnConnectionVgwTelemetryOutputReference",
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
    @jsii.member(jsii_name="acceptedRouteCount")
    def accepted_route_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "acceptedRouteCount"))

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @builtins.property
    @jsii.member(jsii_name="lastStatusChange")
    def last_status_change(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastStatusChange"))

    @builtins.property
    @jsii.member(jsii_name="outsideIpAddress")
    def outside_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outsideIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="statusMessage")
    def status_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusMessage"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VpnConnectionVgwTelemetry]:
        return typing.cast(typing.Optional[VpnConnectionVgwTelemetry], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[VpnConnectionVgwTelemetry]) -> None:
        if __debug__:
            def stub(value: typing.Optional[VpnConnectionVgwTelemetry]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VpnConnection",
    "VpnConnectionConfig",
    "VpnConnectionRoutes",
    "VpnConnectionRoutesList",
    "VpnConnectionRoutesOutputReference",
    "VpnConnectionTunnel1LogOptions",
    "VpnConnectionTunnel1LogOptionsCloudwatchLogOptions",
    "VpnConnectionTunnel1LogOptionsCloudwatchLogOptionsOutputReference",
    "VpnConnectionTunnel1LogOptionsOutputReference",
    "VpnConnectionTunnel2LogOptions",
    "VpnConnectionTunnel2LogOptionsCloudwatchLogOptions",
    "VpnConnectionTunnel2LogOptionsCloudwatchLogOptionsOutputReference",
    "VpnConnectionTunnel2LogOptionsOutputReference",
    "VpnConnectionVgwTelemetry",
    "VpnConnectionVgwTelemetryList",
    "VpnConnectionVgwTelemetryOutputReference",
]

publication.publish()
