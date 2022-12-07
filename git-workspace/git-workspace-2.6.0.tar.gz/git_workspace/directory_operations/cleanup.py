# -*- coding: UTF-8 -*-
__author__ = 'Aki Mäkinen'

import os
import shutil

from git_workspace.helpers.input import yes_no_input

__DEFAULT_ARCHIVE_DIR = ".git-ws-archived-repositories"


def __get_git_directories(root_dir, exclude=None):
    directories = []
    for item in os.walk(root_dir):
        if not item[0].endswith(".git"):
            continue
        directory = item[0][:-5].replace(root_dir, "")
        if directory.startswith("/"):
            directory = directory[1:]
        if (exclude is None) or (exclude is not None and not directory.startswith(exclude)):
            directories.append(directory)
    return directories


def __remove_empty_groups(ws, archived_repositories):
    for repo in archived_repositories:
        examinable_part = repo
        while examinable_part:
            head, tail = os.path.split(examinable_part)
            path_to_examine = os.path.join(ws, head, tail)
            if os.path.exists(path_to_examine) and len(os.listdir(path_to_examine)) == 0:
                answer = yes_no_input(f"The following directory is now empty: {path_to_examine}. Remove it?")
                if answer is True:
                    try:
                        shutil.rmtree(path_to_examine)
                    except FileNotFoundError:
                        print(f"Failed to delete {path_to_examine}: the directory was not found.")
                else:
                    print(f"Leaving {path_to_examine} intact.")
            examinable_part = head


def cleanup_to_archive(ws, repositories):
    git_directories = __get_git_directories(ws, __DEFAULT_ARCHIVE_DIR)

    directories_from_repositories = [item.get("directory") for item in repositories]

    movable_directories = []
    if len(movable_directories) > 0:
        for directory in git_directories:
            if directory not in directories_from_repositories:
                movable_directories.append(directory)

        for item in movable_directories:
            shutil.move(os.path.join(ws, item), os.path.join(ws, __DEFAULT_ARCHIVE_DIR, item))

        print("Attempting to cleanup empty directories.")
        __remove_empty_groups(ws, movable_directories)
    else:
        print("Nothing to move into the archive.")
        print()
    dir = __get_git_directories(os.path.join(ws, __DEFAULT_ARCHIVE_DIR))

    print(f"{__DEFAULT_ARCHIVE_DIR} now contains the following repositories:")
    for item in dir:
        print(f"    {item}")
    print()
