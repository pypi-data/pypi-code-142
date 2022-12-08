import psutil
from rich.console import Console
from rich.table import Table


def get_processes():
    processes = []
    for process in psutil.process_iter():
        try:
            # just to trigger AccessDenied if proceed
            process.memory_info()
            processes.append(process)
        except psutil.AccessDenied:
            pass
    return processes


def display_memproc():
    table = Table()
    table.add_column('PID')
    table.add_column('Name')
    table.add_column('Mem')
    processes = get_processes()
    processes.sort(key=lambda p: p.memory_info().rss)
    for proc in processes:
        try:
            mem = proc.memory_info().rss / 2**20
            table.add_row(str(proc.pid), proc.name(), f'{mem:.02f}MB')
        except psutil.AccessDenied:
            pass
    console = Console()
    console.print(table)
