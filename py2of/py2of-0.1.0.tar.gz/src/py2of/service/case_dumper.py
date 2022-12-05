from dataclasses import dataclass
from pathlib import Path
from typing import Any
from typing import Mapping

from py2of.service.dumper import Dumper


@dataclass()
class CaseDumper:
    case: Mapping[Path, Mapping[str, Any]]

    def dump(self, dump_dir: Path) -> None:
        for path, content in self.case.items():
            Dumper(content).write(dump_dir / path)
