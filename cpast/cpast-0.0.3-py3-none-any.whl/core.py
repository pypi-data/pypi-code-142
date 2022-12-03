import os


def format_date(date: str, time: str) -> str:
    return f'"{date}T{time}"'


def prepare_vars(formatted_date: str):
    os.environ['GIT_AUTHOR_DATE'] = formatted_date
    os.environ['GIT_COMMITTER_DATE'] = formatted_date


def run(date: str, time: str, msg: str):
    formatted_date: str = format_date(date, time)
    prepare_vars(formatted_date)
    os.system(f'git commit -m "{msg}"')
