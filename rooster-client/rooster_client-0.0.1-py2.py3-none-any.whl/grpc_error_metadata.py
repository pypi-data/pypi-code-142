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
from pprint import pprint

import grpc
from google.rpc import error_details_pb2, status_pb2

# from https://medium.com/kuranda-labs-engineering/gracefully-handling-grpc-errors-in-a-go-server-python-client-setup-9805a5464692


def is_status_detail(x):
    """Return True if a metadata is a grpc-status-details"""
    if (
        hasattr(x, "key")
        and (hasattr(x, "value"))
        and x.key.startswith("grpc-status-details")
    ):
        return True
    return False


def get_status_metadata(err: grpc.RpcError):
    """Extracts error details from a grpc.RpcError.
    Returns a status object and a list of details.
    """

    pprint(err)

    if not isinstance(err, grpc.RpcError):
        raise ValueError(type(err))

    metadata = err.trailing_metadata()
    if len(metadata) == 0:
        return status_pb2.Status(), None

    # get only metadata relevant to status details
    status_md = [x for x in metadata if is_status_detail(x)]
    if status_md:
        for md in status_md:
            st = status_pb2.Status()
            # there should be exactly one status for every RpcError
            # so MergeFromString should at worst append more details
            # but never override st.message and st.code in every loop
            st.MergeFromString(md.value)

    # no details
    if len(st.details) == 0:
        return (st, None)

    # st.details contains a protobuf 'any' type so it is packed
    # In order to access it from Python we have to unpack it
    unpacked = []
    for det in st.details:
        val = unpack_details(det)
        unpacked.append(val)
    st.ClearField("details")
    return (st, unpacked)


def unpack_details(grpc_detail):
    """Unpack a grpc status detail field (which is a protobuf 'any' type)."""
    if grpc_detail.Is(error_details_pb2.BadRequest.DESCRIPTOR):
        val = error_details_pb2.BadRequest()
        grpc_detail.Unpack(val)
        return val
    elif grpc_detail.Is(error_details_pb2.PreconditionFailure.DESCRIPTOR):
        val = error_details_pb2.PreconditionFailure()
        grpc_detail.Unpack(val)
        return val
    elif grpc_detail.Is(error_details_pb2.RetryInfo.DESCRIPTOR):
        val = error_details_pb2.RetryInfo()
        grpc_detail.Unpack(val)
        return val
    elif grpc_detail.Is(error_details_pb2.DebugInfo.DESCRIPTOR):
        val = error_details_pb2.DebugInfo()
        grpc_detail.Unpack(val)
        return val
    elif grpc_detail.Is(error_details_pb2.QuotaFailure.DESCRIPTOR):
        val = error_details_pb2.QuotaFailure()
        grpc_detail.Unpack(val)
        return val
    elif grpc_detail.Is(error_details_pb2.RequestInfo.DESCRIPTOR):
        val = error_details_pb2.RequestInfo()
        grpc_detail.Unpack(val)
        return val
    elif grpc_detail.Is(error_details_pb2.ResourceInfo.DESCRIPTOR):
        val = error_details_pb2.ResourceInfo()
        grpc_detail.Unpack(val)
        return val
    elif grpc_detail.Is(error_details_pb2.Help.DESCRIPTOR):
        val = error_details_pb2.Help()
        grpc_detail.Unpack(val)
        return val
    elif grpc_detail.Is(error_details_pb2.LocalizedMessage.DESCRIPTOR):
        val = error_details_pb2.LocalizedMessage()
        grpc_detail.Unpack(val)
        return val
    else:
        raise ValueError(grpc_detail.type_url)
