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
import grpc

from rooster_client import api_pb2, api_pb2_grpc

# ---------------------------------------------------------------------------
# Imports from here.
# ---------------------------------------------------------------------------
#


class Rooster:
    """Rooster Main Class"""

    def ansible_inventory(metadata: tuple, stub: api_pb2_grpc.DynInvStub):
        """_summary_

        Args:
            metadata (tuple): _description_
            stub (api_pb2_grpc.DynInvStub): _description_

        Returns:
            _type_: _description_
        """
        request = api_pb2.InventoryQuery(enabled=api_pb2.Selected(selected=True))
        inv = stub.InventoryJson(request=request, metadata=metadata)

        ba = bytearray([])

        for raw in inv:
            ba.extend(raw.data)

        return ba.decode("utf-8")

    def get_credentials_metadata(username: str, password: str):
        return (("username", username), ("password", password))

    def get_channel(address: str, ssl=False):
        if ssl:
            cc = grpc.ssl_channel_credentials()
            channel = grpc.secure_channel(address, cc)
        else:
            channel = grpc.insecure_channel(address)

        return channel

    def get_stub(channel):
        return api_pb2_grpc.DynInvStub(channel)

    def create_host(host: api_pb2.Host, metadata: tuple, stub: api_pb2_grpc.DynInvStub):
        request = api_pb2.Modify(host=host)

        try:
            response = stub.CreateHost(request=request, metadata=metadata)
            logging.info("Created Host: %s", response.uuid.uuid)
            return response

        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.ALREADY_EXISTS:
                logging.error("Error creating Host: %s", e.details())
            else:
                raise e
        except Exception as e:
            raise e

    def create_group(
        group: api_pb2.Group, metadata: tuple, stub: api_pb2_grpc.DynInvStub
    ):
        request = api_pb2.Modify(group=group)

        try:
            response = stub.CreateGroup(request=request, metadata=metadata)
            logging.info("Created Group: %s", response.uuid.uuid)
            return response

        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.ALREADY_EXISTS:
                logging.error("Error creating Group: %s", e.details())
            else:
                raise e
        except Exception as e:
            raise e

    def get_host(host: api_pb2.Host, metadata: tuple, stub: api_pb2_grpc.DynInvStub):
        try:
            response = stub.GetHost(request=host, metadata=metadata)
            return response

        except grpc.RpcError as e:
            raise e
        except Exception as e:
            raise e

    def get_group(group: api_pb2.Group, metadata: tuple, stub: api_pb2_grpc.DynInvStub):
        try:
            response = stub.GetGroup(request=group, metadata=metadata)
            return response

        except grpc.RpcError as e:
            raise e
        except Exception as e:
            raise e
