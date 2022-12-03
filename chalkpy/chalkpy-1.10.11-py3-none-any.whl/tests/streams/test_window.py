from typing import Any, cast

import pytest
from pydantic import BaseModel
from typing_extensions import TypeGuard

from chalk import OnlineResolver, online
from chalk.features import Features, feature, features, has_one
from chalk.streams import KafkaSource, Windowed, stream, windowed


@features
class GrandchildWindow:
    id: str
    grandchildfeat: Windowed[str] = windowed("10m", "20m", max_staleness="1h")


@features
class ChildWindow:
    id: str
    childfeat: Windowed[str] = windowed("10m", "20m", max_staleness="1h")
    grand: GrandchildWindow = has_one(lambda: ChildWindow.id == GrandchildWindow.id)


@features
class StreamFeaturesWindow:
    uid: str = feature(primary=True)
    scalar_feature: Windowed[str] = windowed("10m", "20m", max_staleness="1h")
    scalar_feature_2: Windowed[str] = windowed("10m", "20m", max_staleness="1h")
    basic: str

    child_id: str
    child: ChildWindow = has_one(lambda: StreamFeaturesWindow.child_id == ChildWindow.id)


@online
def with_children(
    r: StreamFeaturesWindow.scalar_feature(window="10m"),
    r1: StreamFeaturesWindow.child.childfeat["20m"],
    r2: StreamFeaturesWindow.child.grand.grandchildfeat("10m"),
) -> StreamFeaturesWindow.basic:
    print(r, r2, r1)
    return ""


def test_has_one_windows():
    assert resolver(with_children).inputs[0].root_fqn == "stream_features_window.scalar_feature__600__"
    assert resolver(with_children).inputs[1].root_fqn == "stream_features_window.child.childfeat__1200__"
    assert resolver(with_children).inputs[2].root_fqn == "stream_features_window.child.grand.grandchildfeat__600__"


class KafkaMessage(BaseModel):
    val_a: str


s = KafkaSource(bootstrap_server="bootstrap-server", topic="topic")


class TopicMessage(BaseModel):
    val_a: str
    val_a: str
    val_a: str


@stream(source=s)
def fn(
    message: TopicMessage,
) -> Features[StreamFeaturesWindow.uid, StreamFeaturesWindow.scalar_feature, StreamFeaturesWindow.scalar_feature_2]:
    return StreamFeaturesWindow(
        uid="123",
        scalar_feature="xyz",
        scalar_feature_2="abc",
    )


def resolver(x: Any) -> TypeGuard[OnlineResolver]:
    return cast(OnlineResolver, x)


@online
def accessing_via_brackets(r: StreamFeaturesWindow.scalar_feature["10m"]) -> StreamFeaturesWindow.basic:
    pass


def test_missing_window_error_message():
    with pytest.raises(TypeError) as e:

        @online
        def accessing_via_brackets(r: StreamFeaturesWindow.scalar_feature["40m"]) -> StreamFeaturesWindow.basic:
            pass

    assert str(e.value) == (
        "Unsupported window duration '40m' for 'stream_features_window.scalar_feature'. 10m, 20m are supported."
    )


def test_windowed_inputs():
    assert resolver(accessing_via_brackets).inputs[0].fqn == "stream_features_window.scalar_feature__600__"
    assert resolver(with_children).inputs[0].fqn == "stream_features_window.scalar_feature__600__"


def test_resolver_requiring_all_windows():
    with pytest.raises(ValueError):

        @online
        def badboi(r: StreamFeaturesWindow.scalar_feature) -> StreamFeaturesWindow.basic:
            pass


def test_require_whole_thing():
    with pytest.raises(ValueError):

        @online
        def badboi(r: StreamFeaturesWindow.scalar_feature) -> StreamFeaturesWindow.basic:
            pass
