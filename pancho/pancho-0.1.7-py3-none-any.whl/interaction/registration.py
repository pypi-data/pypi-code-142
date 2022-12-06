from ..definitions import contracts
from ..interaction.messages import Event, dump_payload


class EventRegistrator:
    def __init__(
        self,
        data_vendor: contracts.EventRegistratorDataVendor,
        frame_name: contracts.EventRegistratorFrameName
    ):
        self._data_vendor = data_vendor
        self._frame_name = frame_name

    async def register(self, stream: contracts.MessageStream):
        data = []
        filtered = stream.filter(lambda m: isinstance(m, Event))
        for event in filtered:
            data.append(dict(
                id=event.id,
                created_at=event.created_at,
                event_type=type(event).__name__,
                actor_id=event.actor_id,
                context=dump_payload(event)
            ))
        if data:
            await self._data_vendor.insert({
                self._frame_name: data
            })
