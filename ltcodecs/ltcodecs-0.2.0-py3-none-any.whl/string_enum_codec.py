from bitstring import ConstBitStream
from .varint_codec import VarintCodec
from .field_codec import FieldCodec
from typing import List, Optional


class StringEnumCodec(FieldCodec):
    def __init__(self, entries: List[str], unknown_value: Optional[str] = None,
                 case_sensitive: bool = False, strip: bool = False, **kwargs):
        if case_sensitive:
            self.entries = entries
        else:
            self.entries = [e.lower() for e in entries]
        self.case_sensitive = case_sensitive
        self.strip = strip

        if isinstance(unknown_value, str):
            self.unknown_value = unknown_value
            min_value = -1
        else:
            self.unknown_value = None
            min_value = 0

        self.string_index_codec = VarintCodec(min_value=min_value, max_value=len(self.entries))

    def encode(self, value: str):
        if not self.case_sensitive:
            value = value.lower()
        if self.strip:
            value = value.strip()

        if value in self.entries:
            index = self.entries.index(value)
            compressed_value = self.entries[index]
        else:
            if self.unknown_value:
                index = -1
                compressed_value = self.unknown_value
            else:
                index = 0
                compressed_value = self.entries[index]

        encoded_index, _ = self.string_index_codec.encode(index)

        return encoded_index, compressed_value

    def decode(self, encoded_bits: ConstBitStream):
        index = self.string_index_codec.decode(encoded_bits)
        if index < 0:
            return self.unknown_value
        else:
            return self.entries[index]

    @property
    def max_length_bits(self):
        return self.string_index_codec.max_length_bits

    @property
    def min_length_bits(self):
        return self.string_index_codec.max_length_bits