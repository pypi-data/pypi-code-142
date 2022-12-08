import psutil
from rich.console import Console
from rich.table import Table


def get_sort_key(sort_by: str, process: psutil.Process):
    match sort_by:
        case 'pid':
            return process.pid
        case 'name':
            return process.name()
        case 'mem':
            return process.memory_info().rss


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


def display_memproc(sort_by: str = 'mem'):
    table = Table()
    table.add_column('PID')
    table.add_column('Name')
    table.add_column('Mem')
    processes = get_processes()
    reverse = sort_by[0] == '-'
    processes.sort(key=lambda p: get_sort_key(sort_by.strip('-+'), p), reverse=reverse)
    for proc in processes:
        try:
            mem = proc.memory_info().rss / 2**20
            table.add_row(str(proc.pid), proc.name(), f'{mem:.02f} MB')
        except psutil.AccessDenied:
            pass
    console = Console()
    console.print(table)
