"""Parse strings or bytes into Python objects.
"""
import io
import ipaddress
import logging
import pkgutil
import re
from typing import List

import textfsm

import routeviews.types
from routeviews import exceptions

logger = logging.getLogger(__name__)


def IPAddr(ipaddr_raw: str) -> routeviews.types.IPAddr:
    """Parse an ip address.

    Args:
        ipaddr_raw (List[str]): List of IP Address strings.

    Returns:
        routeviews.types.IPAddrList: The IP Addresses found in the provided data.

    Examples:

    Works well for IPv4 address parsing:

        >>> IPAddr('1.2.3.4')
        IPv4Address('1.2.3.4')
        >>> IPAddr('1.2.3.4:5000')
        IPv4Address('1.2.3.4')
        >>> IPAddr('1.2.3.4/32')
        IPv4Address('1.2.3.4')

    Also works for IPv6 parsing:

        >>> IPAddr('fe80::1234')
        IPv6Address('fe80::1234')
        >>> IPAddr('[fe80::1234]:6000')
        IPv6Address('fe80::1234')
        >>> IPAddr('fe80::1234/128')
        IPv6Address('fe80::1234')
    """
    def remove_cidr(ipaddr):
        return ipaddr_raw.split('/')[0]

    def remove_ipv6_port(ipaddr):
        matches = re.match(r'\[(.*)\]:\d+', ipaddr)
        if matches:
            return matches.group(1)
        return ipaddr

    def remove_ipv4_port(ipaddr) -> str:
        matches = re.match(r'(\d+\.\d+\.\d+\.\d+):\d+', ipaddr)
        if matches:
            return matches.group(1)
        return ipaddr

    try:
        ipaddr = remove_cidr(ipaddr_raw)
        ipaddr = remove_ipv6_port(ipaddr)
        ipaddr = remove_ipv4_port(ipaddr)
        return ipaddress.ip_address(ipaddr)
    except (ValueError, AttributeError):
        raise exceptions.ParseError(f'Unable to parse IP Address: "{ipaddr_raw}"')


def IPAddrList(ipaddrs_raw: List[str]) -> routeviews.types.IPAddrList:
    """Parse ip addresses.

    Args:
        ipaddrs_raw (List[str]): List of IP Address strings.

    Returns:
        routeviews.types.IPAddrList: The IP Addresses found in the provided data.
    """
    ipaddrs = [IPAddr(ip) for ip in ipaddrs_raw]
    return list(filter(None, ipaddrs))


def template_parse(raw_text, template='bgp_summary'):
    """Parse some text using a textfsm template.

    Args:
        raw_text (str): The text to be parsed.
        template (str, optional): Which template to use, from this package's
        "templates/" folder. Defaults to 'bgp_summary'.

    Returns:
        List[Dict]: List of the results returned by TextFSM.

    Example:
        >>> template_parse('''IPv4 Unicast Summary:
        ... BGP router identifier 128.223.51.15, local AS number 6447 vrf-id 0
        ... ... omitted for brevity...
        ... Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
        ... 5.189.255.107   4     141011   1088896     59504        0    0    0 01w0d16h       314845        0 HUIZE''')
        [{'ROUTER_ID': '128.223.51.15', ..., 'STATE_PFXRCD': '314845'}]
    """
    # Setup our TextFSM instance to parse raw_text
    pkg_name = __name__.split('.')[0]
    template_name = f'templates/{template}.textfsm'
    try:
        textfsm_template = pkgutil.get_data(pkg_name, template_name)
        if not textfsm_template:
            raise FileNotFoundError()
    except FileNotFoundError:
        raise exceptions.MissingTemplateError(
                f'Unable to locate TextFSM template {template} in package {pkg_name}'
                f'\n"`pip install --force-reinstall {pkg_name}`" may fix this.')
    parser = textfsm.TextFSM(io.BytesIO(textfsm_template))
    results = parser.ParseText(raw_text)

    # Combine : to make the returned data more useful
    return [
        dict(zip(parser.header, textfsm_result))
        for textfsm_result in results
    ]
