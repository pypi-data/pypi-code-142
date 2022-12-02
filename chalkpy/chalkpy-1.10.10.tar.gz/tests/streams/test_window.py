from pydantic import BaseModel

from chalk import online
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


# @realtime
# def x(
#     thing: StreamFeaturesWindow.scalar_feature("10m"),
# ) -> Features[StreamFeaturesWindow.uid]:
#     print(thing)
#     return


# thing = StreamFeaturesWindow.scalar_feature["10m"]
# print(str(thing))
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


# wow = StreamInvoker(600, fn).invoke(None)
# wow = fn._invoke_for_seconds(600, None)
# print(wow)


@online
def requiring_windowed_feature(
    r: StreamFeaturesWindow.scalar_feature("10m"),
    r2: StreamFeaturesWindow.child.grand.grandchildfeat("10m"),
    r3: StreamFeaturesWindow.scalar_feature,
) -> StreamFeaturesWindow.basic:
    # print(r)
    # t = r
    # print(r)
    pass


inputs = requiring_windowed_feature.inputs[0]
print(inputs)

#
# assert len(set(Fetaures[...].windows)) == 1
#
#
# @stream(
#     source=s,
#     # 10, 20
# )
# def fn(
#     message: list[TopicMessage],
#     # x: StreamFeaturesWindow.scalar_feature,
# ) -> Features[StreamFeaturesWindow.scalar_feature]:
#     assert (
#         StreamFeaturesWindow(
#             scalar_feature_1="10m",
#             scalar_feature="",
#         ).scalar_feature
#         == ""
#     )
#
# @stream(
#     source=s,
#     # 10, 20
# )
# def fn(
#         message: TopicMessage,
#         y: Last[MyFC.some_feature]
#         # y: <-
#         # x: StreamFeaturesWindow.scalar_feature,
# ) -> Features[StreamFeaturesWindow.uid]:
#     print(y)
#     print(message)
#     return StreamFeaturesWindow(scalar_feature: Uniton[str, TypeDesicl[]="44")("10m")\
#
# LAG
#
# @stream(source=s)
# def fn() -> Features[StreamFeaturesWindow.uid, StreamFeaturesWindow.scalar_feature]:
#     # def fn(
#     #     messages: list[TopicMessage] = None,
#     #
#     #         y: Last[MyFC.some_feature]
#     #         # y: <-
#     #     # x: StreamFeaturesWindow.scalar_feature,
#
#     print(y)
#     print(message)
#     return StreamFeaturesWindow(scalar_feature="44", scalar_feature__600__="44")
#
#
#
# def test_window_definition():
#     pass
