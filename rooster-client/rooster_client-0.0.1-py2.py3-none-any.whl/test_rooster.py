#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Created By   : Wieger Bontekoe <wieger.bontekoe@productsup.com>
# Created Date : 2022-12-03
#
# Copyright (c) 2022, Products Up GmbH
#
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# ---------------------------------------------------------------------------
""" FILE DESCRIPTION."""
# ---------------------------------------------------------------------------
# Imports from here.
# ---------------------------------------------------------------------------
#
import unittest
from pathlib import Path

import toml

from rooster_client import rooster


class TestRooster(unittest.TestCase):
    def setup_stub(self):
        # tag::setup[]
        # Load the configuration
        config = toml.load(str(Path.home()) + "/.rooster")

        # Create the metadata for the login credentials
        metadata = rooster.get_credentials_metadata(
            username=config.get("Credentials").get("Username"),
            password=config.get("Credentials").get("Password"),
        )

        # create the HTTP2 channel
        channel = rooster.get_channel(config.get("Server"))

        # create the stub (the "server" connection)
        stub = rooster.get_stub(channel)
        # end::setup[]

        return metadata, channel, stub

    def test_ansible_inventory(self):
        metadata, channel, stub = self.setup_stub()

        # tag::sample[]
        # request the ansible inventory in JSON format
        print(rooster.ansible_inventory(metadata, stub))
        # end::sample[]

    def test_group_create(self):
        metadata, channel, stub = self.setup_stub()

        # tag::group_create[]
        group = rooster.create_group(
            rooster.api_pb2.Group(name="somegroup", enabled=True), metadata, stub
        )
        print(group)
        # end::group_create[]

    def test_host_create(self):
        metadata, channel, stub = self.setup_stub()

        group = rooster.create_group(
            rooster.api_pb2.Group(name="somegroup2", enabled=True), metadata, stub
        )

        # tag::host_create[]
        host = rooster.api_pb2.Host(
            address="foo.bar.com",
            hostname="foo",
            domain="bar.com",
            enabled=True,
            monitored=True,
        )

        # the Host message expects a Groups message and in there we can append the group
        # we made before
        host.groups.groups.append(group)

        host = rooster.create_host(host, metadata, stub)
        print(host)
        # end::host_create[]

    def test_group_get(self):
        metadata, channel, stub = self.setup_stub()

        # tag::group_get[]
        group = rooster.get_group(
            rooster.api_pb2.Group(name="somegroup"), metadata, stub
        )
        print(group)
        # end::group_get[]

    def test_host_get(self):
        metadata, channel, stub = self.setup_stub()

        # tag::host_get[]
        host = rooster.get_host(
            rooster.api_pb2.Host(address="foo.bar.com"), metadata, stub
        )
        print(host)
        # end::host_get[]


if __name__ == "__main__":
    unittest.main()
