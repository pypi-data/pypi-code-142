# -*- coding: utf-8 -*-
# *******************************************************
#   ____                     _               _
#  / ___|___  _ __ ___   ___| |_   _ __ ___ | |
# | |   / _ \| '_ ` _ \ / _ \ __| | '_ ` _ \| |
# | |__| (_) | | | | | |  __/ |_ _| | | | | | |
#  \____\___/|_| |_| |_|\___|\__(_)_| |_| |_|_|
#
#  Sign up for free at http://www.comet.ml
#  Copyright (C) 2021 Comet ML INC
#  This file can not be copied and/or distributed without the express
#  permission of Comet ML Inc.
# *******************************************************

import asyncio as asyncio_module
import atexit
import calendar
import os
from datetime import datetime
from typing import Any, Awaitable, Dict, Iterable, List, Optional, Union

import comet_mpm.event

from .connection import MPM_BASE_PATH, REST_API_BASE_PATH, sanitize_url, url_join
from .constants import (
    EVENT_FEATURES,
    EVENT_PREDICTION,
    EVENT_PREDICTION_ID,
    EVENT_PREDICTION_PROBABILITY,
    EVENT_PREDICTION_VALUE,
    EVENT_TIMESTAMP,
    EVENT_WORKSPACE_NAME,
)
from .sender import get_sender
from .settings import MPMSettings, get_model


def local_timestamp() -> int:
    """Return a timestamp in a format expected by the backend (milliseconds)"""
    now = datetime.utcnow()
    timestamp_in_seconds = calendar.timegm(now.timetuple()) + (now.microsecond / 1e6)
    timestamp_in_milliseconds = int(timestamp_in_seconds * 1000)
    return timestamp_in_milliseconds


class CometMPM:
    """
    The Comet MPM class is used to upload a model's input and output features to MPM
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        workspace_name: Optional[str] = None,
        model_name: Optional[str] = None,
        model_version: Optional[str] = None,
        disabled: Optional[bool] = None,
        asyncio: bool = False,
    ):
        """
        Creates the Comet MPM Event logger object.
        Args:
            api_key: The Comet API Key
            workspace_name: The Comet Workspace Name of the model
            model_name: The Comet Model Name of the model
            model_version: The Comet Model Version of the model
            disabled: If set to True, CometMPM will not send anything to the backend.
            asyncio: Set to True if you are using an Asyncio-based framework like FastAPI.
        """

        settings_user_values = {}  # type: Dict[str, str]
        # Filter out None
        if api_key is not None:
            settings_user_values["api_key"] = api_key

        if model_name is not None:
            settings_user_values["mpm_model_name"] = model_name

        if model_version is not None:
            settings_user_values["mpm_model_version"] = model_version

        if workspace_name is not None:
            settings_user_values["mpm_workspace_name"] = workspace_name

        self._settings = get_model(
            MPMSettings,
            **settings_user_values,
        )
        if disabled:
            self.disabled = disabled  # type: bool
        else:
            self.disabled = bool(os.getenv("COMET_MPM_DISABLED"))
        self._asyncio = asyncio

        self._mpm_url = url_join(sanitize_url(self._settings.url), MPM_BASE_PATH)
        self._api_url = url_join(sanitize_url(self._settings.url), REST_API_BASE_PATH)

        if self.disabled:
            self._sender = None
        else:
            self._sender = get_sender(
                self._settings.api_key,
                self._mpm_url,
                self._settings.mpm_model_name,
                self._settings.mpm_model_version,
                max_batch_size=self._settings.mpm_max_batch_size,
                max_batch_time=self._settings.mpm_max_batch_time,
                asyncio=self._asyncio,
                batch_sending_timeout=self._settings.mpm_batch_sending_timeout,
            )

            atexit.register(self._on_end)

        # TODO: Do handshake

    LogEventsResult = Union[List[Any], Awaitable[List[Any]]]

    def _log_events(self, events: Iterable[comet_mpm.event.Event]) -> LogEventsResult:
        results = []
        for event in events:
            result = self.log_event(**event.to_dictionary())
            results.append(result)

        if self._asyncio:
            return asyncio_module.gather(*results)  # type: ignore[arg-type]
        else:
            return results

    def log_event(
        self,
        prediction_id: str,
        input_features: Optional[Dict[str, Any]] = None,
        output_value: Optional[Any] = None,
        output_probability: Optional[Any] = None,
    ) -> Optional[Awaitable[None]]:
        """
        Log a single event asynchronously to MPM. Events are identified by the
        mandatory prediction_id parameter. You can send multiple events with the
        same prediction_id, events will be merged on the backend side
        automatically.
        Args:
            prediction_id: The unique prediction ID, could be provided by the
                framework, you or a random unique value could be provided like
                str(uuid4())
            input_features: If provided must be a flat Dictionary where the
                keys are the feature name and the value are native Python
                scalars, int, floats, booleans or strings. For example:
                `{“age”: 42, “income”: 42894.89}`
            output_value: The prediction as a native Python scalar, int,
                float, boolean or string.
            output_probability: If provided, must be a float between 0 and 1
                indicating the confidence of the model in the prediction
        """
        if self.disabled:
            if self._asyncio is False:
                return None
            else:
                return asyncio_module.sleep(0)

        prediction: Dict[str, Any] = {}
        if output_value is not None:
            prediction[EVENT_PREDICTION_VALUE] = output_value
        if output_probability is not None:
            prediction[EVENT_PREDICTION_PROBABILITY] = output_probability

        event = {
            EVENT_WORKSPACE_NAME: self._settings.mpm_workspace_name,
            EVENT_PREDICTION_ID: prediction_id,
            EVENT_TIMESTAMP: local_timestamp(),
        }

        if input_features is not None:
            event[EVENT_FEATURES] = input_features

        if prediction:
            event[EVENT_PREDICTION] = prediction

        assert self._sender is not None
        return self._sender.put(event)

    def log_dataframe(  # type: ignore[no-untyped-def]
        self,
        dataframe,
        prediction_id_column: str,
        feature_columns: Optional[List[str]] = None,
        output_value_column: Optional[str] = None,
        output_probability_column: Optional[str] = None,
    ) -> LogEventsResult:
        """
        Log a pandas DataFrame to MPM.
        Every row in the dataframe will be interpreted as an event to be logged.

        Events are structured as described in .log_event() method, please refer to it
        to have the full context.

        Args:
            prediction_id_column: this column should have the prediction_id
                values for the events.
            feature_columns: if provided, this column will be used as the
                input_features parameter for the events.
            output_value_column: if provided, this column will be used as the
                output_value for the events.
            output_probability_column: if provided, this column will be used as
                the output_probability for the events.
        """
        events = []
        for row in dataframe.itertuples():
            prediction_id = str(getattr(row, prediction_id_column))
            event = comet_mpm.event.Event(prediction_id=prediction_id)
            if feature_columns is not None:
                event.input_features = {
                    key: getattr(row, key) for key in feature_columns
                }
            if output_value_column is not None:
                event.output_value = getattr(row, output_value_column)
            if output_probability_column is not None:
                event.output_probability = getattr(row, output_probability_column)

            events.append(event)

        return self._log_events(events)

    def connect(self) -> None:
        """
        When using CometMPM in asyncio mode, this coroutine needs to be awaited
        at the server start.
        """
        if self._sender is not None:
            self._sender.connect()

    def join(self, timeout: Optional[int] = None) -> Optional[Awaitable[None]]:
        """
        When using CometMPM in asyncio mode, this coroutine needs to be awaited
        at the server stop.
        """
        if timeout is None:
            timeout = self._settings.mpm_join_timeout

        if not self.disabled:
            assert self._sender is not None
            return self._sender.join(timeout)
        else:
            if self._asyncio is False:
                return None
            else:
                return asyncio_module.sleep(0)

    def _on_end(self) -> None:
        if not self.disabled:
            assert self._sender is not None
            self._sender.close()
