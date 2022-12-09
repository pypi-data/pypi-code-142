import psutil
from rich.console import Console
from rich.table import Table

from memproc.lib.process import Process, ProcNameLevel

from . import utils


class ProcessPool:
    def __init__(
        self,
        name_level: int,
        sort_by: str,
        sort_reverse: bool,
        show_total: bool,
        units: str,
    ):
        self.name_level = name_level
        self.show_total = show_total
        self.units = units.upper()
        self.processes = self._get_processes(name_level, units)
        self.mem = sum(p.mem for p in self.processes)
        self.processes.sort(key=lambda p: getattr(p, sort_by), reverse=sort_reverse)

    def _get_processes(self, name_level: int, units: str) -> list:
        processes = []
        for proc in psutil.process_iter():
            try:
                # just to trigger AccessDenied if proceed
                proc.memory_info()
            except psutil.AccessDenied:
                pass
            else:
                p = Process(proc, name_level, self.units)
                processes.append(p)
        return processes

    @property
    def humanized_mem(self):
        hmem = utils.convert_mem(self.mem, self.units)
        return f'{hmem:.02f} {self.units}'

    def show(self):
        table = Table(show_lines=self.name_level == ProcNameLevel.CMDLINE)
        table.add_column('PID')
        table.add_column('Name')
        table.add_column('Mem')
        for proc in self.processes:
            table.add_row(*proc.as_table_row())
        if self.show_total:
            table.add_section()
            table.add_row('', 'TOTAL', self.humanized_mem, style='purple')
        console = Console()
        console.print(table)
