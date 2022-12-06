from __future__ import annotations
import logging, os, re
from pathlib import Path
from datetime import datetime, timezone
from tabulate import tabulate
from .utils import ElementInfo, command
from .settings import TARGET_ISO_DIR
from .debian import parse_iso_name
from .external import external

logger = logging.getLogger(__name__)

@command(name="list")
def listiso():
    """
    List ISO files.
    """
    info_groups: dict[str,InfoGroup] = {}

    def get_or_create_info_group(path: Path|str):
        if isinstance(path, Path):
            name = path.name
        else:
            name = os.path.basename(path)
        
        if not name in info_groups:
            info_groups[name] = InfoGroup()
        return info_groups[name]


    # Get information from local ISO directory
    for path in TARGET_ISO_DIR.glob("**/*.iso"):
        group = get_or_create_info_group(path)
        group.local_infos.append(ElementInfo(path, TARGET_ISO_DIR))

    # Get information from pub ISO directory
    if external:
        for elem in external.find():
            group = get_or_create_info_group(elem.path)
            group.pub_infos.append(elem)

    # Display information
    headers = ['name', 'version', 'local dir', 'local MB', 'local modif']
    if external is not None:
        headers += ['ext dir', 'ext MB', 'ext modif']
    rows = []

    for name, group in info_groups.items():
        n = 0
        while n < max(len(group.local_infos), len(group.pub_infos)):
            edition, version, variant, arch = parse_iso_name(name)
            row = [name, version]
            
            if len(group.local_infos) > n:
                local = group.local_infos[n]
                row += [os.path.dirname(local.relative_path) or '.', local.size/1024/1024, _localdate_or_time(local.last_modified)]
            else:
                row += [None, None, None]
            
            if external is not None:
                if len(group.pub_infos) > n:
                    pub = group.pub_infos[n]
                    row += [os.path.dirname(pub.relative_path) or '.', pub.size/1024/1024, _localdate_or_time(pub.last_modified)]
                else:
                    row += [None, None, None]

            rows.append(row)
            n += 1

    table = tabulate(rows, headers=headers)
    separator = table.splitlines()[1]

    print(f"Local:    {TARGET_ISO_DIR}")
    if external:
        print(f"External: {external}")

    print(separator)
    print(table)


local_date = datetime.now().astimezone().date()

def _localdate_or_time(dt: datetime):
    if dt.date() == local_date:
        return dt.astimezone().strftime('%H:%M')
    else:
        return dt.astimezone().strftime('%Y-%m-%d')


class InfoGroup:
    def __init__(self):
        self.local_infos: list[ElementInfo] = []
        self.pub_infos: list[ElementInfo] = []
