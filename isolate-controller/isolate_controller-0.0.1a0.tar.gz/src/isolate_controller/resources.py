from __future__ import annotations
from typing import Optional

from dataclasses import dataclass

from isolate_controller import definitions



GPU_K8S_PROPERTY = "nvidia.com/gpu"

@dataclass(frozen=True)
class Limits:
    cpu: float
    memory: str
    gpu: Optional[int] = None

    def to_kubernetes(self) -> dict[str, str]:
        limit_dict = {
            "cpu": str(self.cpu),
            "memory": self.memory,
        }

        if self.gpu is not None:
            limit_dict[GPU_K8S_PROPERTY] = str(self.gpu)

        return limit_dict


@dataclass(frozen=True)
class MachineConfiguration:
    # TODO: remove name?
    name: str
    limits: Limits


MACHINE_TYPES = {
    "XS": MachineConfiguration("XS", Limits(0.25, f"256Mi")),
    "S": MachineConfiguration("S", Limits(0.50, f"1Gi")),
    "M": MachineConfiguration("M", Limits(2, f"8Gi")),
    "L": MachineConfiguration("L", Limits(4, f"32Gi")),
    "XL": MachineConfiguration("XL", Limits(8, f"128Gi")),
    "GPU": MachineConfiguration("GPU", Limits(8, f"64Gi", gpu=1)),
}

DEFAULT_MACHINE_TYPE = "S"
DEFAULT_MACHINE = MACHINE_TYPES[DEFAULT_MACHINE_TYPE]


class InvalidMachineRequirements(Exception):
    """When the given machine requirements can not be satisfied."""


def parse_machine_requirements(
    requirements: definitions.MachineRequirements,
) -> MachineConfiguration:
    machine_type = requirements.machine_type or DEFAULT_MACHINE_TYPE
    if machine_type not in MACHINE_TYPES:
        raise InvalidMachineRequirements(
            f"{machine_type!r} is not a supported machine type."
        )

    machine_configuration = MACHINE_TYPES[machine_type]
    return machine_configuration
