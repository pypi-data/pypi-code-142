import random
from typing import Optional

import umsgpack

BEGIN_MARK = "\0"
END_MARK = "\0\0"

TextGeneratorModel = dict[str, set[str]]


class TextGenerator:
    model: TextGeneratorModel

    def __init__(self, model: Optional[TextGeneratorModel] = None):
        if model is None:
            self.model = {}
        else:
            self.model = model

    @classmethod
    def load(cls, raw: bytes):
        """Deserialize model from msgpack."""

        unpacked = umsgpack.unpackb(raw)
        model = {k: set(v) for k, v in unpacked.items()}
        return cls(model)

    @classmethod
    def from_samples(cls, samples: list[str]):
        """Create generator and feed with given `samples`."""

        generator = cls()
        generator.feed_bulk(samples)
        return generator

    def dump(self) -> bytes:
        """Serialize model to msgpack."""

        packable_model = {k: list(v) for k, v in self.model.items()}
        return umsgpack.packb(packable_model)

    def feed_bulk(self, samples: list[str]):
        """Feed text generation model with multiple samples."""

        for sample in samples:
            self.feed(sample)

    def feed(self, sample: str) -> None:
        """Feed text generation model."""

        tokens = [BEGIN_MARK] + sample.split() + [END_MARK]
        for i in range(len(tokens) - 1):
            if tokens[i] not in self.model:
                self.model[tokens[i]] = {tokens[i + 1]}
            else:
                self.model[tokens[i]].add(tokens[i + 1])

    def generate(self, start_token=BEGIN_MARK) -> str:
        """Generate a text.

        Raises IndexError if the model is empty."""

        if len(self.model) == 0:
            raise IndexError("Model is empty")

        if start_token not in self.model:
            raise ValueError("Start token does not exist in model")

        current = random.choice(list(self.model[start_token]))
        result = [start_token] if start_token != BEGIN_MARK else []
        while current in self.model and current != END_MARK:
            result.append(current)
            current = random.choice(list(self.model[current]))
        return " ".join(result)

    def merge(self, other: "TextGenerator") -> None:
        """Merge other model."""

        for k, v in other.model.items():
            if k not in self.model:
                self.model[k] = v
            else:
                self.model[k].union(v)
