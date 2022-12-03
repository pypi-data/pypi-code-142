from dataclasses import dataclass, field
from typing import List

import yaml
from dacite import from_dict


@dataclass
class ClonePath:
    src: str
    dest: str


@dataclass
class Clone:
    name: str
    paths: List[ClonePath]
    default: bool = False


@dataclass
class Config:
    base_path: str = ""
    clones: List[Clone] = field(default_factory=list)


def load_config(path: str) -> Config:
    with open(path) as f:
        config = yaml.safe_load(f)
    return from_dict(Config, config)
