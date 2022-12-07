import asyncio
import time
from typing import Optional, List

import nest_asyncio
from grpclib.client import Channel, Configuration
from grpclib.events import SendRequest, listen

from octave_sdk.grpc.quantummachines.octave.api.v1 import (
    OctaveServiceStub,
    OctaveModule,
    ModuleReference,
    UpdateResponse,
    ControlRequest,
    UpdateRequest,
    SaveRequest,
    AquireRequest,
    RecallRequest,
    ListRequest,
    GetVersionRequest,
    MonitorRequest,
    ExploreRequest,
    IdentifyRequest,
)

"""
# OctaveClient
#
#   This is a gRPC based Octave. The standard setup is the whole Octave product.
#   Namely, we access the SOM on its motherboard via ethernet and from there
#   communicate with all the boards via the main PIC.
#
#   A temporary alternative is using a mini SOM eval board which is connected
#   to a mini motherboard, directly into the serial lines of its PIC.
#
#   The specific variation is passed to the constructor.
"""


def _build_grpclib_channel(host, port, octave_name: Optional = None, credentials: Optional = None) -> Channel:
    channel = Channel(
        host=host,
        port=port,
        ssl=credentials is not None,
        config=Configuration(),
    )

    if octave_name is not None:

        async def send_request(event: SendRequest):
            event.metadata["x-grpc-service"] = octave_name

        listen(channel, SendRequest, send_request)

    return channel


class MonitorResult:
    def __init__(self, results_pb):
        self.modules = {
            OctaveModule.OCTAVE_MODULE_RF_UPCONVERTER: [None for module_index in range(5)],
            OctaveModule.OCTAVE_MODULE_RF_DOWNCONVERTER: [None for module_index in range(2)],
            OctaveModule.OCTAVE_MODULE_IF_DOWNCONVERTER: [None for module_index in range(2)],
            OctaveModule.OCTAVE_MODULE_SYNTHESIZER: [None for module_index in range(6)],
            OctaveModule.OCTAVE_MODULE_SOM: [
                None,
            ],
        }
        for module in results_pb.modules:
            self.modules[module.module.type][module.module.index - 1] = module.temperature

    def __repr__(self):
        res = ""
        for module_type, temperatures in self.modules.items():
            res += module_type.name[14:] + "s\n"
            res += "   " + " ".join(f"{ind + 1:6d}" for ind in range(len(temperatures))) + "\n"
            res += "     " + "".join("  n.c  " if temp is None else f" {temp:2.2f} " for temp in temperatures) + "\n"

        return res


class ExploreResult:
    def __init__(self, results_pb):
        self.modules = {
            OctaveModule.OCTAVE_MODULE_RF_UPCONVERTER: [None for module_index in range(5)],
            OctaveModule.OCTAVE_MODULE_RF_DOWNCONVERTER: [None for module_index in range(2)],
            OctaveModule.OCTAVE_MODULE_IF_DOWNCONVERTER: [None for module_index in range(2)],
            OctaveModule.OCTAVE_MODULE_SYNTHESIZER: [None for module_index in range(6)],
            OctaveModule.OCTAVE_MODULE_MOTHERBOARD: [None for module_index in range(1)],
        }
        for module in results_pb.modules:
            self.modules[module.module.type][module.module.index - 1] = module.id

    def __repr__(self):
        module_types = [
            OctaveModule.OCTAVE_MODULE_RF_UPCONVERTER,
            OctaveModule.OCTAVE_MODULE_RF_DOWNCONVERTER,
            OctaveModule.OCTAVE_MODULE_IF_DOWNCONVERTER,
            OctaveModule.OCTAVE_MODULE_SYNTHESIZER,
        ]

        m_id = self.modules[OctaveModule.OCTAVE_MODULE_MOTHERBOARD][0]
        if m_id is None or m_id == "":
            res = "MOTHERBOARD [\x1b[38;5;208m???\x1b[0m]\n"
        else:
            res = f"MOTHERBOARD [\x1b[38;5;154m{m_id}\x1b[0m]\n"

        res += "    RF_UPCONVs          RF_DOWNCONVs        IF_DOWNCONVs        " "SYNTHESIZERs\n"
        for index in range(6):
            res += "     "
            for t in module_types:
                if index < len(self.modules[t]):
                    m_id = self.modules[t][index]
                    if m_id is None:
                        res += f"\x1b[38;5;241m{index+1}. {'---':17s}\x1b[0m"
                    elif m_id == "":
                        res += f"{index+1}. \x1b[38;5;208m{'???':17s}\x1b[0m"
                    else:
                        res += f"{index+1}. \x1b[38;5;154m{m_id:17s}\x1b[0m"
                else:
                    res += f"{'':20s}"
            res += "\n"

        return res


class OctaveClient:
    def __init__(self, host: str, port: int, octave_name: str = None):
        self._host = host
        self._port = port
        self._octave_name = octave_name
        self._loop = None
        self._build_channel()
        super().__init__()

    def _build_channel(self):
        if self._loop is not None and (not self._loop.is_closed()):
            return None
        else:
            if hasattr(self, "_channel") and self._channel is not None:
                try:
                    self._channel.close()
                except BaseException:
                    pass
            try:
                current_loop = asyncio.get_event_loop()
            except BaseException:
                current_loop = asyncio.new_event_loop()
            self._loop = current_loop
            asyncio.set_event_loop(self._loop)
            self._channel = _build_grpclib_channel(host=self._host, port=self._port, octave_name=self._octave_name)
            self._service = OctaveServiceStub(self._channel)

    def _run_async(self, coro):
        self._build_channel()
        if self._loop:
            asyncio.set_event_loop(self._loop)
            nest_asyncio.apply(self._loop)
            return self._loop.run_until_complete(coro)
        else:
            asyncio.set_event_loop(self._loop)
            return self._loop.run_until_complete(coro)

    def __del__(self):
        self._service = None
        if hasattr(self, "_channel") and self._channel is not None:
            self._channel.close()

    def _control(self, w_data=b"", r_length=0):
        control_request = ControlRequest(w_data=w_data, r_length=r_length)
        return self._run_async(self._service.control(control_request))

    def update(self, updates):
        update_request = UpdateRequest(updates=updates)
        response: UpdateResponse = self._run_async(self._service.update(update_request))
        if not response.success:
            raise Exception(f"Octave update failed: {response.error_message}")
        return response

    def debug_set(
        self,
        monitor_enabled: bool = None,
        monitor_timeout: int = None,
        monitor_print_rate: int = None,
        monitor_update_fan: bool = None,
        uart_debug_mode: bool = None,
        print_updates: bool = None,
    ):
        if monitor_timeout is not None:
            if monitor_timeout < 1 or monitor_timeout > 15:
                print("OctaveClientBase.debug_set   ERROR    monitor_timeout should be" " 1..15")
                return
        else:
            monitor_timeout = 0x00

        if monitor_print_rate is not None:
            if monitor_print_rate < 0 or monitor_print_rate > 255:
                print(
                    "OctaveClientBase.debug_set   ERROR    monitor_print_rate should either 0 (no printings) or 1..255"
                )
                return

        activate = 0x00
        state = 0x00

        if monitor_enabled is not None:
            activate |= 0x01
            state |= 0x01 if monitor_enabled else 0x00

        if uart_debug_mode is not None:
            activate |= 0x02
            state |= 0x02 if uart_debug_mode else 0x00

        if print_updates is not None:
            activate |= 0x04
            state |= 0x04 if print_updates else 0x00

        if monitor_print_rate is not None:
            activate |= 0x08
        else:
            monitor_print_rate = 0

        if monitor_update_fan is not None:
            activate |= 0x10
            state |= 0x10 if monitor_update_fan else 0x00

        res = (
            self._control(
                w_data=bytes([0xFF, 0xFF, activate, state, monitor_timeout, monitor_print_rate]),
                r_length=1,
            )
        ).r_data
        return res

    def save_modules(self, m_id: str = None, module_refs=None, overwrite=True):
        module_refs = module_refs if module_refs else []
        save_request = SaveRequest(
            id="default" if m_id is None else m_id, modules=module_refs, overwrite=overwrite, timestamp=int(time.time())
        )

        return self._run_async(self._service.save(save_request))

    def aquire_modules(self, modules: List[ModuleReference], use_cache=True):
        aquire_request = AquireRequest(modules=modules, use_cache=use_cache)
        res = self._run_async(self._service.aquire(aquire_request))
        if len(modules) == 1 and len(res.state.updates) == 1:
            return res.state.updates[0]

        return res

    def recall(self, m_id: str = None):
        recall_request = RecallRequest(id="default" if m_id is None else m_id)
        return self._run_async(self._service.recall(recall_request))

    def configs(self):
        list_request = ListRequest()
        res = self._run_async(self._service.list(list_request))
        return res.save_infos

    def version(self):
        get_vestion_request = GetVersionRequest()
        return self._run_async(self._service.get_version(get_vestion_request))

    def monitor(self, sense_only=True):
        monitor_request = MonitorRequest(sense_only=sense_only)
        res = self._run_async(self._service.monitor(monitor_request))
        return MonitorResult(res)

    def explore(self):
        explore_request = ExploreRequest()
        res = self._run_async(self._service.explore(explore_request))
        return ExploreResult(res)

    def identify(self):
        identify_request = IdentifyRequest()
        return self._run_async(self._service.identify(identify_request))
