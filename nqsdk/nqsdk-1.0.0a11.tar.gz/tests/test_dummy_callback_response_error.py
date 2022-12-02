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


import pytest

from nqsdk.abstract.message import SentMeta
from nqsdk.consts import DEFAULT_CALLBACK_CODE_ERROR
from nqsdk.dummy.callback import DummyCallbackResponse
from nqsdk.enums import CallbackStatus


class TestDummyCallbackResponseError:
    @pytest.mark.parametrize("error_message", ["Unexpected error.", "Error.", "Bar."])
    def test_response(
        self,
        sent_meta: SentMeta,
        error_message: str,
    ):
        response = DummyCallbackResponse(
            status=CallbackStatus.FAILED, meta=sent_meta, error=error_message
        )

        assert response.status == CallbackStatus.FAILED
        assert response.get_code() == DEFAULT_CALLBACK_CODE_ERROR
        assert response.get_content_type() == "application/json"
        assert response.get_content() == {"error": error_message}
        assert response.error == error_message
        assert response.meta == sent_meta

    def test_response_empty_error(
        self,
        sent_meta: SentMeta,
    ):
        response = DummyCallbackResponse(status=CallbackStatus.FAILED, meta=sent_meta)

        assert response.status == CallbackStatus.FAILED
        assert response.get_code() == DEFAULT_CALLBACK_CODE_ERROR
        assert not response.get_content_type()
        assert not response.get_content()
        assert not response.error
        assert response.meta == sent_meta
