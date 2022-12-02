"""
Copyright (c) 2022 Inqana Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from typing import Union
from unittest.mock import Mock

import pytest
from rest_framework.request import Request

from nqsdk.abstract.callback import CallbackResponse
from nqsdk.abstract.message import AckMeta, DeliveredMeta, SentMeta
from nqsdk.dummy.provider import DummyProvider
from nqsdk.enums import CallbackStatus


class TestDummyCallbacks:
    @staticmethod
    def _assert_common(
        sent_meta: SentMeta,
        response: CallbackResponse,
        response_meta: Union[DeliveredMeta, AckMeta],
    ):
        assert response.status == CallbackStatus.OK
        assert response.get_code() == 200
        assert response.get_content_type() == "application/json"
        assert response.get_content() == {"message_id": sent_meta.ext_id}
        assert not response.error
        assert response.meta == sent_meta

        assert response_meta.attempt_uid == sent_meta.attempt_uid
        assert response_meta.ext_id == sent_meta.ext_id
        assert response_meta.dt_sent == sent_meta.dt_sent
        assert isinstance(response_meta, (DeliveredMeta, AckMeta))
        if isinstance(response_meta, DeliveredMeta):
            assert response_meta.dt_delivered
            assert response_meta.dt_delivered.tzinfo
        else:
            assert response_meta.dt_ack
            assert response_meta.dt_ack.tzinfo

    @pytest.mark.repeat(20)
    def test_callback(
        self,
        sent_meta: SentMeta,
    ):
        provider = DummyProvider(config={}, callback_urls={})
        response, response_meta = provider.handle_callback(
            request=Mock(spec=Request), meta=sent_meta
        )

        self._assert_common(sent_meta=sent_meta, response=response, response_meta=response_meta)

    def test_delivered(
        self,
        sent_meta: SentMeta,
    ):
        provider = DummyProvider(config={}, callback_urls={})
        response, delivered_meta = provider.handle_delivered(
            request=Mock(spec=Request), meta=sent_meta
        )

        self._assert_common(sent_meta=sent_meta, response=response, response_meta=delivered_meta)

    def test_ack(
        self,
        sent_meta: SentMeta,
    ):
        provider = DummyProvider(config={}, callback_urls={})
        response, ack_meta = provider.handle_ack(request=Mock(spec=Request), meta=sent_meta)

        self._assert_common(sent_meta=sent_meta, response=response, response_meta=ack_meta)
