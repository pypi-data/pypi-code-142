import psutil
from rich.console import Console
from rich.table import Table


def get_processes():
    processes = []
    for proc in psutil.process_iter():
        try:
            # just to trigger AccessDenied if proceed
            proc.memory_info()
            processes.append(proc)
        except psutil.AccessDenied:
            pass
    return processes


def get_sort_key(proc: psutil.Process, sort_by: str, name_level: int):
    match sort_by:
        case 'pid':
            return proc.pid
        case 'name':
            return get_name_by_level(proc, name_level)
        case 'mem':
            return proc.memory_info().rss


def get_name_by_level(proc: psutil.Process, name_level: int):
    info = ''
    match name_level:
        case 1:
            info = proc.name()
        case 2:
            info = proc.exe()
        case 3:
            info = ' '.join(proc.cmdline())
    if not info:
        info = proc.name()
    return info


def display_memproc(name_level: int = 1, sort_by: str = 'mem', sort_reverse: bool = False):
    table = Table()
    table.add_column('PID')
    table.add_column('Name')
    table.add_column('Mem')
    processes = get_processes()
    processes.sort(key=lambda p: get_sort_key(p, sort_by, name_level), reverse=sort_reverse)
    for proc in processes:
        try:
            mem = proc.memory_info().rss / 2**20
            info = get_name_by_level(proc, name_level)
            table.add_row(str(proc.pid), info, f'{mem:.02f} MB')
        except psutil.AccessDenied:
            pass
    console = Console()
    console.print(table)
