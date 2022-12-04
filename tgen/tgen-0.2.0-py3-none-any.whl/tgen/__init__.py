import random
from typing import Optional

import umsgpack

BEGIN_MARK = "_B"
END_MARK = "_E"

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
