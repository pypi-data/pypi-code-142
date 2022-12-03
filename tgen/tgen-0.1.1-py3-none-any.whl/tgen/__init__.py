import random
from typing import Optional

import umsgpack

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

    def dump(self) -> bytes:
        """Serialize model to msgpack."""

        packable_model = {k: list(v) for k, v in self.model.items()}
        return umsgpack.packb(packable_model)

    def feed(self, sample: str) -> None:
        """Feed text generation model."""

        tokens = sample.split()
        for i in range(len(tokens) - 1):
            if tokens[i] not in self.model:
                self.model[tokens[i]] = {tokens[i + 1]}
            else:
                self.model[tokens[i]].add(tokens[i + 1])

    def generate(self) -> str:
        """Generate a text.

        Raises IndexError if the model is empty."""

        if len(self.model) == 0:
            raise IndexError("Model is empty")

        current = random.choice(list(self.model.keys()))
        result = [current]
        while current in self.model:
            current = random.choice(list(self.model[current]))
            result.append(current)
        return " ".join(result)

    def merge(self, other: "TextGenerator") -> None:
        """Merge other model."""

        for k, v in other.model.items():
            if k not in self.model:
                self.model[k] = v
            else:
                self.model[k].union(v)
