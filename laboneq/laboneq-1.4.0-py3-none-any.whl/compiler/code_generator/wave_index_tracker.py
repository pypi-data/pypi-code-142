# Copyright 2022 Zurich Instruments AG
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Dict, Tuple, Any, Optional, List


class WaveIndexTracker:
    def __init__(self):
        self._wave_indices: Dict[str, Tuple[int, Any]] = {}
        self._next_wave_index: int = 0

    def lookup_index_by_wave_id(self, wave_id: str) -> Optional[int]:
        return self._wave_indices.get(wave_id)

    def create_index_for_wave(self, wave_id: str, signal_type: str) -> Optional[int]:
        assert wave_id not in self._wave_indices
        if signal_type == "csv":
            # For CSV store only the signature, do not allocate an index
            self._wave_indices[wave_id] = (-1, signal_type)
            return

        index = self._next_wave_index
        self._next_wave_index += 1
        self._wave_indices[wave_id] = (index, signal_type)
        return index

    def add_numbered_wave(self, wave_id: str, signal_type: str, index):
        self._wave_indices[wave_id] = (index, signal_type)

    def wave_indices(self) -> Dict[str, List[int, Any]]:
        # Cast entries to list. This will end up in the compiled experiment, and we want
        # invariance under serialization + deserialization, but the JSON decoder
        # produces lists, not tuples.
        return {k: list(v) for k, v in self._wave_indices.items()}
