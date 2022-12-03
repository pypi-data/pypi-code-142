import unittest

from bind_sdk.requests_payload.debin_payload import DebinPayload
from bind_sdk.options.currency import Currency
from bind_sdk.options.concept import Concept


class TestRequestPayloads(unittest.TestCase):
    def test_debin_payload(self):
        dbp = DebinPayload(
            "origin-id-1000",
            "ElbarbaCaja",
            Currency.ARS.value,
            100,
            Concept.FAC.value,
            54,
        )
        self.assertTrue(type(dbp.to_json()) == dict)
