import re
import subprocess
from typing import Set, Dict, Tuple, Generator, Iterator

import fire
import jsonpickle


def comment_to_tickets(comment: str) -> Set[str]:
    return set(re.findall(r"\w+-\d+", comment))


def raw_stats_line_to_tuple(raw_stats_line: str) -> Tuple[int, int]:
    split = raw_stats_line.split("\t", 2)
    return int(split[0]), int(split[1])


class Ticket(object):
    def __init__(self, ticket_id, additions=0, deletions=0) -> None:
        super().__init__()
        self.ticket_id = ticket_id
        self.additions = additions
        self.deletions = deletions

    def add_stats(self, stats_tuple: Tuple[int, int]):
        self.additions += stats_tuple[0]
        self.deletions += stats_tuple[1]

    def __eq__(self, other: object) -> bool:
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __repr__(self):
        return "Ticket(ticket_id={}, additions={}, deletions={})".format(
            self.ticket_id, self.additions, self.deletions
        )


def gather_stats(stdin: Iterator[str]) -> Dict[str, Ticket]:
    next(stdin)  # skip first <end>
    result = {}
    for line in stdin:
        assert line.startswith("<start>")

        next(stdin)  # ignore hash

        # skip everything in the comments except first line
        comment: str = next(stdin)
        for comment_line in stdin:
            if comment_line.startswith("<br>"):
                break

        # extract ticket ids from the comment
        ticket_ids = comment_to_tickets(comment)
        for ticket_id in ticket_ids:
            if ticket_id not in result.keys():
                result[ticket_id] = Ticket(ticket_id)

        # skip analyzing stat info if there is no empty line before it (because stats info does not exist)
        empty_line = next(stdin)
        if empty_line.strip() != "":
            continue

        # process stat info
        for raw_stats_line in stdin:
            if raw_stats_line.startswith("<end>"):
                break

            stats: tuple[int, int] = raw_stats_line_to_tuple(raw_stats_line)
            for ticket_id in ticket_ids:
                result[ticket_id].add_stats(stats)
    return result


def is_git_repo(git_repo_dir: str) -> bool:
    return (
        subprocess.run(
            ["git", "-C", git_repo_dir, "rev-parse", "--is-inside-work-tree"]
        ).returncode
        == 0
    )


def git_log(git_repo_dir: str) -> Generator[str, None, None]:
    process = subprocess.Popen(
        [
            "git",
            "-C",
            git_repo_dir,
            "log",
            "--numstat",
            "--pretty=tformat:<end>%n<start>%n%H%n%s%n<br>",
        ],
        text=True,
        stdout=subprocess.PIPE,
    )
    while True:
        output = process.stdout.readline()
        if output == "" and process.poll() is not None:
            break
        if output:
            yield str(output.strip())
    if process.poll() != 0:
        raise Exception


def main(repo: str = "."):
    """
    Generate statistics with JIRA tickets

    Calls `git log` and groups data by JIRA ticket. An output has the following structure:
    {
      "RD-3550": {
        "ticket_id": "RD-3550",
        "additions": 603,
        "deletions": 141
      },
      ...
    }

    :param repo: Git repository for which to create statistics
    :return:
    """
    if not is_git_repo(repo):
        exit(1)
    git_log_output = git_log(repo)
    stats = gather_stats(git_log_output)
    stats_as_json = jsonpickle.encode(stats, unpicklable=False, indent=2)
    print(stats_as_json)


def fire_main():
    fire.Fire(main)


if __name__ == "__main__":
    fire_main()
