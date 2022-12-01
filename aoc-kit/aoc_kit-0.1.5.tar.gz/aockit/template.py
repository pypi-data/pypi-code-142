import argparse
from datetime import date
from pathlib import Path


template = """from aockit import get_input


def part1():
    data = get_input({year}, {day})


def part2():
    data = get_input({year}, {day})


if __name__ == "__main__":
    part1()
    part2()
"""


def ensure_path(year: int, day: int):
    p = Path("./") / str(year) / str(day)
    if not p.exists():
        p.mkdir(parents=True)


def get_full_path(year: int, day: int) -> Path:
    return Path("./") / str(year) / str(day) / "main.py"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", type=int)
    parser.add_argument("--year", type=int)
    args = parser.parse_args()

    today = date.today()
    if (not args.year or not args.day) and\
        (today.month != 12 or today.day > 25):
        print("Day and Year need to be specified if not in december.")
        return

    year = args.year if args.year else today.year
    day = args.day if args.day else today.day

    ensure_path(year, day)

    path = get_full_path(year, day)
    if path.exists():
        print(f"A file already exists at _{path}_. Aborting.")
        return

    with open(path, "w") as f:
        f.write(template.format(year=year, day=day))


if __name__ == "__main__":
    main()
