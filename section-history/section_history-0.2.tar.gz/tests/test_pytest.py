from turtle import up
from section_history.__main__ import main
from section_history.entry import Entry
from pathlib import Path
from git.repo import Repo
from datetime import datetime
from datetime import date
import pytest
import time
import typer
import os
from section_history.cache import Cache, StoreResult

# Fixture to set up git repo!!
@pytest.fixture
def set_up_repo(tmp_path: Path):
    repo_path = tmp_path / "repo"
    repo = Repo.init(repo_path)  # type: ignore

    # This function just creates an empty file ...
    myfile = repo_path / "text.md"
    myfile.touch()
    reqID = "REQ333"
    myfile.write_text(
        f'<requirement id = "{reqID}" source="jsiwj"> This is THE requirement</requirement>'
    )
    repo.index.add(["text.md"])
    repo.index.commit(
        "initial commit", commit_date=date(2022, 7, 21).strftime("%Y-%m-%d %H:%M:%S")
    )
    myfile.write_text(
        f'<requirement id = "{reqID}" source="jsiwj"> Second changed text</requirement>'
    )
    repo.git.add(["text.md"])
    repo.index.commit(
        "second commit", commit_date=date(2022, 7, 22).strftime("%Y-%m-%d %H:%M:%S")
    )
    return [reqID, repo_path, myfile, repo]


# Fixture to create an Entry object
@pytest.fixture
def create_entry():
    filename = "./"
    commit = "h2gjf3ojeorr456"
    author = "Povel Ramel"
    date = datetime.now()
    text = '<requirement id = "REQ111"> Test requirement </requirement>'
    reqid = "REQ111"
    message = "Fixed typo in requirement"
    entry = Entry(filename, commit, author, date, text, reqid, message)
    return entry


# Fixture to set up config file
@pytest.fixture
def create_config_file(set_up_repo):
    repo_path = set_up_repo[1]
    section_history_dir = Path(repo_path) / ".sectionHistory"
    section_history_dir.mkdir()
    config_file = section_history_dir / "config.ini"
    config_file.touch()
    config_file.write_text(
        f'[regex_section]\nregex_val = <requirement *id *= *"([^"]+)".*?<\/requirement>'
    )
    return config_file


def test_commmit_to_temp_repo(set_up_repo, create_config_file):
    reqID = set_up_repo[0]
    repo_path = set_up_repo[1]
    entries = main(
        repo_path,
        reqID,
        update_cache=False,
        cache_path="",
        highlight_diff=False,
    )
    assert (
        entries[0].text
        == f'<requirement id = "{reqID}" source="jsiwj"> Second changed text</requirement>'
        and entries[1].text
        == f'<requirement id = "{reqID}" source="jsiwj"> This is THE requirement</requirement>'
    )


def test_more_than_two_commit_in_repo(set_up_repo, create_config_file):
    reqID = set_up_repo[0]
    repo_path = set_up_repo[1]
    myfile = set_up_repo[2]
    repo = set_up_repo[3]

    myfile.write_text(
        f'<requirement id = "{reqID}" source="jsiwj"> Third changed text</requirement>'
    )
    repo.git.add(u=True)
    repo.index.commit(
        "third commit", commit_date=date(2022, 7, 23).strftime("%Y-%m-%d %H:%M:%S")
    )
    entries = main(
        repo_path, reqID, update_cache=False, cache_path="", highlight_diff=False
    )
    assert (
        entries[1].text
        == f'<requirement id = "{reqID}" source="jsiwj"> Second changed text</requirement>'
        and entries[0].text
        == f'<requirement id = "{reqID}" source="jsiwj"> Third changed text</requirement>'
    )


def test_add_another_reqid_to_repo(set_up_repo, create_config_file):
    repo_path = set_up_repo[1]
    myfile = set_up_repo[2]
    repo = set_up_repo[3]
    reqID = "REQ444"
    myfile.write_text(
        f'<requirement id = "{reqID}" source="jsiwj"> New requirement text</requirement>'
    )
    repo.git.add(u=True)
    repo.index.commit(
        "third commit - with new reqid",
        commit_date=date(2022, 7, 23).strftime("%Y-%m-%d %H:%M:%S"),
    )
    entries = main(repo_path, reqID, update_cache=False, cache_path="")
    assert (
        entries[0].text
        == f'<requirement id = "{reqID}" source="jsiwj"> New requirement text</requirement>'
    )


def test_remove_file_in_repo(set_up_repo, create_config_file):
    reqID = set_up_repo[0]
    repo_path = set_up_repo[1]
    repo = set_up_repo[3]

    fileToDelete = repo_path / "fileToDelete.md"
    fileToDelete.touch()
    repo.index.add(["fileToDelete.md"])
    repo.index.commit(
        "third commit - add the file to delete",
        commit_date=date(2022, 7, 23).strftime("%Y-%m-%d %H:%M:%S"),
    )

    fileToDelete.unlink()
    repo.git.add(u=True)
    repo.index.commit(
        "fourth commit - after deleting the file",
        commit_date=date(2022, 7, 24).strftime("%Y-%m-%d %H:%M:%S"),
    )
    entries = main(repo_path, reqID, update_cache=False, cache_path="")
    assert (
        entries[0].text
        == f'<requirement id = "{reqID}" source="jsiwj"> Second changed text</requirement>'
    )


def test_submodule(tmp_path: Path, set_up_repo, create_config_file):
    submodule_path = tmp_path / "submoduleRepo"
    submodule_repo = Repo.init(submodule_path)

    submyfile = submodule_path / "subtext.md"
    submyfile.touch()
    submodule_repo.index.add(["subtext.md"])
    submodule_repo.index.commit(
        "initial commit to submodule",
        commit_date=date(2022, 7, 23).strftime("%Y-%m-%d %H:%M:%S"),
    )

    reqID = set_up_repo[0]
    repo_path = set_up_repo[1]
    repo = set_up_repo[3]

    repo.git.submodule("add", "../submoduleRepo")
    repo.index.commit(
        "third commit - adding submodule",
        commit_date=date(2022, 7, 24).strftime("%Y-%m-%d %H:%M:%S"),
    )
    entries = main(repo_path, reqID, update_cache=False, cache_path="")
    assert (
        entries[0].text
        == f'<requirement id = "{reqID}" source="jsiwj"> Second changed text</requirement>'
    )


def test_that_requirement_in_submodule_not_counted(
    tmp_path: Path, set_up_repo, create_config_file
):
    reqID = set_up_repo[0]
    repo_path = set_up_repo[1]
    repo = set_up_repo[3]
    submodule_path = tmp_path / "submoduleRepo"
    submodule_repo = Repo.init(submodule_path)
    req2 = "REQ000"

    submyfile = submodule_path / "subtext.md"
    submyfile.touch()
    submyfile.write_text(
        f'<requirement id = "{req2}" source="jsiwj"> Third changed text</requirement>'
    )
    submodule_repo.index.add(["subtext.md"])
    submodule_repo.index.commit(
        "initial commit to submodule",
        commit_date=date(2022, 7, 23).strftime("%Y-%m-%d %H:%M:%S"),
    )

    repo.git.submodule("add", "../submoduleRepo")
    repo.index.commit(
        "third commit - adding submodule",
        commit_date=date(2022, 7, 24).strftime("%Y-%m-%d %H:%M:%S"),
    )
    main(repo_path, update_cache=True, cache_path="", force=False)
    entries = main(repo_path, req2, update_cache=False, cache_path="")
    assert len(entries) == 0


def test_renamed_submodule(tmp_path: Path, set_up_repo, create_config_file):
    submodule_path = tmp_path / "submoduleRepo"
    submodule_repo = Repo.init(submodule_path)
    print(submodule_path)
    submyfile = submodule_path / "subtext.md"
    submyfile.touch()
    submodule_repo.index.add(["subtext.md"])
    submodule_repo.index.commit(
        "initial commit to submodule",
        commit_date=date(2022, 7, 23).strftime("%Y-%m-%d %H:%M:%S"),
    )

    reqID = set_up_repo[0]
    repo_path = set_up_repo[1]
    print(repo_path)
    repo = set_up_repo[3]

    repo.git.submodule("add", "../submoduleRepo")
    repo.index.commit(
        "third commit - adding submodule",
        commit_date=date(2022, 7, 24).strftime("%Y-%m-%d %H:%M:%S"),
    )

    submodule = repo.submodules[0]
    submodule.move("renamedsubmoduleRepo")
    output = repo.submodule_update(recursive=False)
    print(output)
    repo.index.commit(
        "fourth commit - renaming submodule",
        commit_date=date(2022, 7, 24).strftime("%Y-%m-%d %H:%M:%S"),
    )
    main(repo_path, update_cache=True, cache_path="", force=False)
    entries = main(repo_path, reqID, update_cache=False, cache_path="")
    assert (
        entries[0].text
        == f'<requirement id = "{reqID}" source="jsiwj"> Second changed text</requirement>'
    )


def test_that_requirement_in_submodule_not_counted(
    tmp_path: Path, set_up_repo, create_config_file
):
    reqID = set_up_repo[0]
    repo_path = set_up_repo[1]
    repo = set_up_repo[3]
    submodule_path = tmp_path / "submoduleRepo"
    submodule_repo = Repo.init(submodule_path)
    req2 = "REQ000"

    submyfile = submodule_path / "subtext.md"
    submyfile.touch()
    submyfile.write_text(
        f'<requirement id = "{req2}" source="jsiwj"> Third changed text</requirement>'
    )
    submodule_repo.index.add(["subtext.md"])
    submodule_repo.index.commit(
        "initial commit to submodule",
        commit_date=date(2022, 7, 23).strftime("%Y-%m-%d %H:%M:%S"),
    )

    repo.git.submodule("add", "../submoduleRepo")
    repo.index.commit(
        "third commit - adding submodule",
        commit_date=date(2022, 7, 24).strftime("%Y-%m-%d %H:%M:%S"),
    )
    main(repo_path, update_cache=True, cache_path="")
    entries = main(repo_path, req2, update_cache=False, cache_path="")
    assert len(entries) == 0


def test_renamed_submodule(tmp_path: Path, set_up_repo, create_config_file):
    submodule_path = tmp_path / "submoduleRepo"
    submodule_repo = Repo.init(submodule_path)
    print(submodule_path)
    submyfile = submodule_path / "subtext.md"
    submyfile.touch()
    submodule_repo.index.add(["subtext.md"])
    submodule_repo.index.commit(
        "initial commit to submodule",
        commit_date=date(2022, 7, 23).strftime("%Y-%m-%d %H:%M:%S"),
    )

    reqID = set_up_repo[0]
    repo_path = set_up_repo[1]
    print(repo_path)
    repo = set_up_repo[3]

    repo.git.submodule("add", "../submoduleRepo")
    repo.index.commit(
        "third commit - adding submodule",
        commit_date=date(2022, 7, 24).strftime("%Y-%m-%d %H:%M:%S"),
    )

    submodule = repo.submodules[0]
    submodule.move("renamedsubmoduleRepo")
    output = repo.submodule_update(recursive=False)
    print(output)
    repo.index.commit(
        "fourth commit - renaming submodule",
        commit_date=date(2022, 7, 24).strftime("%Y-%m-%d %H:%M:%S"),
    )
    main(repo_path, update_cache=True, cache_path="")
    entries = main(repo_path, reqID, update_cache=False, cache_path="")
    assert (
        entries[0].text
        == f'<requirement id = "{reqID}" source="jsiwj"> Second changed text</requirement>'
    )


def test_entry_convert_to_string(create_entry):
    assert (
        str(create_entry)
        == f"\nFile: {create_entry.file} \nCommit: {create_entry.commit} \nAuthor: {create_entry.author} \nDate: {create_entry.date} \nCommit message: {create_entry.message} \n\n{create_entry.text}"
    )


def test_id_does_not_exist(set_up_repo, create_config_file):
    reqID = "REQ222"
    directory = set_up_repo[1]
    main(directory, update_cache=True, cache_path="", force=False)
    assert (
        main(directory, reqID, update_cache=False, cache_path="") == []
    )  # should maybe return an error message...


def test_path_does_not_exist():
    reqID = "REQ123"
    directory = "/pathdoesnotexist"
    with pytest.raises(Exception, match="Path does not exist"):
        main(directory, reqID)


def test_path_not_repo(tmp_path: Path):
    reqID = "REQ123"
    directory = tmp_path
    with pytest.raises(Exception, match="Path is not a repository"):
        main(directory, reqID)


def test_different_branch_name(set_up_repo, create_config_file):
    reqID = set_up_repo[0]
    repo_path = set_up_repo[1]
    repo = set_up_repo[3]
    current_branch = repo.create_head("new_branch")
    current_branch.checkout()
    entries = main(repo_path, reqID, update_cache=False, cache_path="")
    assert (
        entries[0].text
        == f'<requirement id = "{reqID}" source="jsiwj"> Second changed text</requirement>'
    )


def test_path_not_root(set_up_repo, create_config_file):
    root_directory = set_up_repo[1]
    repo = set_up_repo[3]

    subdirectory = root_directory / "newdirectory"
    subdirectory.mkdir()
    sub_file = subdirectory / "text2.md"
    sub_file.touch()

    reqID = "REQ133"
    sub_file.write_text(
        f'<requirement id = "{reqID}" source="jsiwj"> This is a new requirement in the third commit </requirement>'
    )

    repo.index.add(["newdirectory/text2.md"])
    repo.index.commit(
        "third commit", commit_date=date(2022, 7, 23).strftime("%Y-%m-%d %H:%M:%S")
    )

    sub_file.touch()
    sub_file.write_text(
        f'<requirement id = "{reqID}" source="jsiwj"> This requirement is in the fourth commit test_path_not_root.</requirement>'
    )
    repo.git.add(u=True)
    repo.index.commit(
        "fourth commit", commit_date=date(2022, 7, 24).strftime("%Y-%m-%d %H:%M:%S")
    )
    entries = main(subdirectory, reqID, update_cache=False, cache_path="")
    assert (
        entries[0].text
        == f'<requirement id = "{reqID}" source="jsiwj"> This requirement is in the fourth commit test_path_not_root.</requirement>'
        and entries[1].text
        == f'<requirement id = "{reqID}" source="jsiwj"> This is a new requirement in the third commit </requirement>'
    )


def test_only_files_in_subdirectory_added_to_cache(set_up_repo, create_config_file):
    root_reqID = set_up_repo[0]
    root_directory = set_up_repo[1]
    root_file = set_up_repo[2]
    repo = set_up_repo[3]

    subdirectory = root_directory / "subdirectory"
    subdirectory.mkdir()
    sub_file = subdirectory / "subtext.md"
    sub_file.touch()

    reqID = "REQ122"
    sub_file.write_text(
        f'<requirement id = "{reqID}" source="jsiwj"> This is a new requirement in file in subdirectory </requirement>'
    )

    repo.index.add(["subdirectory/subtext.md"])
    repo.index.commit(
        "third commit", commit_date=date(2022, 7, 23).strftime("%Y-%m-%d %H:%M:%S")
    )
    root_file.write_text(
        f'<requirement id = "{root_reqID}" source="jsiwj"> Updated requirement in file in root </requirement>'
    )
    sub_file.write_text(
        f'<requirement id = "{reqID}" source="jsiwj"> Updated requirement in file in subdirectory </requirement>'
    )
    repo.git.add(u=True)
    repo.index.commit(
        "fourth commit", commit_date=date(2022, 7, 24).strftime("%Y-%m-%d %H:%M:%S")
    )
    entries = main(subdirectory, root_reqID, update_cache=False, cache_path="")
    assert len(entries) == 0


def test_remove_cache(set_up_repo):
    cache = Cache(set_up_repo[1])
    cache_dir = cache.remove_cache()
    assert cache_dir.is_dir() == False


def test_check_cache_not_stored(create_entry, set_up_repo):
    cache = Cache(set_up_repo[1])
    cache.remove_cache()
    assert cache.check_commit_in_cache(create_entry.commit) == StoreResult.NOT_STORED


def test_check_cache_already_stored(create_entry, set_up_repo):
    cache = Cache(set_up_repo[1])
    cache.remove_cache()
    cache.store(create_entry)
    assert (
        cache.check_commit_in_cache(create_entry.commit) == StoreResult.ALREADY_STORED
    )


def test_cache_store(create_entry, set_up_repo):
    cache = Cache(set_up_repo[1])
    cache.remove_cache()
    cache.store(create_entry)
    assert (
        cache.get_cached_history(create_entry.id)[0].text
        == '<requirement id = "REQ111"> Test requirement </requirement>'
    )


def test_get_cache_ordered(create_entry, set_up_repo):
    cache = Cache(set_up_repo[1])
    cache.remove_cache()
    cache.store(create_entry)
    filename = "./"
    commit = "egdoj2w4ldprrg94"
    author = "Povel Ramel"
    date = datetime.now()
    text = '<requirement id = "REQ111"> Test new requirement </requirement>'
    reqid = "REQ111"
    message = "This is a commit message"
    entry = Entry(filename, commit, author, date, text, reqid, message)
    cache.store(entry)
    history = cache.get_cached_history(reqid)
    assert (
        all(history[i].date >= history[i + 1].date for i in range(len(history) - 1))
        == True
    )


def test_run_main_twice(set_up_repo, create_config_file):
    reqID = set_up_repo[0]
    repo_path = set_up_repo[1]
    entries_first = main(repo_path, reqID, update_cache=False, cache_path="")
    entries_second = main(repo_path, reqID, update_cache=False, cache_path="")

    assert entries_first == entries_second


def test_run_update_main_twice(set_up_repo, create_config_file):
    reqID = set_up_repo[0]
    repo_path = set_up_repo[1]
    main(repo_path, update_cache=True, cache_path="", force=False)
    main(repo_path, update_cache=True, cache_path="", force=False)
    entries = main(repo_path, reqID, update_cache=False, cache_path="")
    assert (
        entries[0].text
        == f'<requirement id = "{reqID}" source="jsiwj"> Second changed text</requirement>'
    )


def test_create_cache_if_empty(set_up_repo, create_config_file):
    reqID = set_up_repo[0]
    repo_path = set_up_repo[1]
    cache = Cache(repo_path)
    main(repo_path, update_cache=True, cache_path="", force=False)
    entries_manual_update = main(repo_path, reqID, update_cache=False, cache_path="")
    cache.remove_cache()
    entries_auto_creation = main(repo_path, reqID, update_cache=False, cache_path="")
    assert entries_auto_creation == entries_manual_update


def test_missing_req_id(set_up_repo, create_config_file):
    reqID = None
    repo_path = set_up_repo[1]
    with pytest.raises(typer.BadParameter, match="Missing argument 'REQ_ID'"):
        main(repo_path, reqID, update_cache=False, cache_path="")


def test_cache_path(set_up_repo, create_config_file):
    reqID = set_up_repo[0]
    repo_path = set_up_repo[1]
    cachedir = repo_path / "cachedir"
    cachedir.mkdir()
    entries = main(repo_path, reqID, update_cache=False, cache_path=cachedir)
    assert (
        entries[0].text
        == f'<requirement id = "{reqID}" source="jsiwj"> Second changed text</requirement>'
    )


def test_config_file_does_not_exist(set_up_repo, capfd):
    reqID = set_up_repo[0]
    repo_path = set_up_repo[1]
    with pytest.raises(
        Exception, match="config.ini does not exist in .sectionHistory directory"
    ):
        main(repo_path, reqID)


# Check that we are retrieving the first commit in the repo, i.e. if that contains a requirement
def test_first_commit(tmp_path: Path):
    repo_path = tmp_path / "repo"
    repo = Repo.init(repo_path)  # type: ignore

    section_history_dir = Path(repo_path) / ".sectionHistory"
    section_history_dir.mkdir()
    config_file = section_history_dir / "config.ini"
    config_file.touch()
    config_file.write_text(
        f'[regex_section]\nregex_val = <requirement *id *= *"([^"]+)".*?<\/requirement>'
    )

    # This function just creates an empty file ...
    myfile = repo_path / "text.md"
    myfile.touch()
    reqID = "REQ111"
    myfile.write_text(
        f'<requirement id = "{reqID}" source="jsiwj"> This is a requirement</requirement>'
    )
    repo.index.add(["text.md"])
    repo.index.commit(
        "initial commit", commit_date=date(2022, 7, 21).strftime("%Y-%m-%d %H:%M:%S")
    )
    for i in range(3):
        with myfile.open("a") as f:
            f.write("Not changing requirement - just changing the file")
        repo.git.add(u=True)
        day = 22 + i
        repo.index.commit(
            f"{i} commit", commit_date=date(2022, 7, day).strftime("%Y-%m-%d %H:%M:%S")
        )
    myfile.write_text(
        f'<requirement id = "{reqID}" source="jsiwj"> This is an updated requirement</requirement>'
    )
    repo.git.add(["text.md"])
    repo.index.commit(
        f"last commit", commit_date=date(2022, 7, 25).strftime("%Y-%m-%d %H:%M:%S")
    )
    entries = main(repo_path, reqID, update_cache=False, cache_path="")
    assert entries[0].message.startswith("last commit")
    assert entries[1].message.startswith("initial commit")


# Check that we retrieve the correct first requirement if the first commit does not contain a file (i.e. a requirement)
def test_empy_first_commit(tmp_path: Path):
    repo_path = tmp_path / "repo"
    repo = Repo.init(repo_path)  # type: ignore

    section_history_dir = Path(repo_path) / ".sectionHistory"
    section_history_dir.mkdir()
    config_file = section_history_dir / "config.ini"
    config_file.touch()
    config_file.write_text(
        f'[regex_section]\nregex_val = <requirement *id *= *"([^"]+)".*?<\/requirement>'
    )

    myfile = repo_path / "text.md"
    myfile.touch()
    repo.index.add(["text.md"])
    repo.index.commit(
        "initial commit", commit_date=date(2022, 7, 21).strftime("%Y-%m-%d %H:%M:%S")
    )

    reqID = "REQ555"
    myfile.write_text(
        f'<requirement id = "{reqID}" source="jsiwj"> This is a requirement</requirement>'
    )
    repo.index.add(["text.md"])
    repo.index.commit(
        "first commit with req",
        commit_date=date(2022, 7, 22).strftime("%Y-%m-%d %H:%M:%S"),
    )
    for i in range(2):
        with myfile.open("a") as f:
            f.write("Not changing requirement - just changing the file")
        repo.git.add(u=True)
        day = 23 + i
        repo.index.commit(
            f"{i+1} commit with req",
            commit_date=date(2022, 7, day).strftime("%Y-%m-%d %H:%M:%S"),
        )

    myfile.write_text(
        f'<requirement id = "{reqID}" source="jsiwj"> This is an updated requirement</requirement>'
    )
    repo.git.add(["text.md"])
    repo.index.commit(
        f"last commit", commit_date=date(2022, 7, 26).strftime("%Y-%m-%d %H:%M:%S")
    )
    entries = main(repo_path, reqID, update_cache=False, cache_path="")
    assert entries[0].message.startswith("last commit")
    assert entries[1].message.startswith("first commit with req")


def test_regex_not_valid(set_up_repo):
    reqID = set_up_repo[0]
    repo_path = set_up_repo[1]
    repo = set_up_repo[3]
    section_history_dir = Path(repo_path) / ".sectionHistory"
    section_history_dir.mkdir()
    config_file = section_history_dir / "config.ini"
    config_file.touch()
    config_file.write_text(f"[regex_section]\nregex_val = [")
    with pytest.raises(
        Exception, match="The provided regex is not valid, update config.ini"
    ):
        main(repo_path, reqID, update_cache=True, cache_path="", force=False)


# default fixture capfd used to catch output in terminal to assert
def test_highlight_diff_multiple_commits(set_up_repo, create_config_file, capfd):
    reqID = set_up_repo[0]
    repo_path = set_up_repo[1]
    myfile = set_up_repo[2]
    repo = set_up_repo[3]

    myfile.write_text(f'<requirement id = "{reqID}" source="jsiwj"> ? </requirement>')
    repo.git.add(u=True)
    repo.index.commit(
        "third commit", commit_date=date(2022, 7, 23).strftime("%Y-%m-%d %H:%M:%S")
    )
    main(repo_path, update_cache=True, cache_path="", force=False)
    main(repo_path, reqID, update_cache=False, cache_path="", highlight_diff=True)
    out, err = capfd.readouterr()
    assert (
        '\x1b[38;2;255;255;255m<requirement id = "REQ333" source="jsiwj"> \x1b[38;2;255;255;255m\x1b[38;2;255;0;0mSecond\x1b[38;2;255;255;255m\x1b[38;2;0;255;0m?\x1b[38;2;255;255;255m\x1b[38;2;255;255;255m \x1b[38;2;255;255;255m\x1b[38;2;255;0;0mchanged text\x1b[38;2;255;255;255m\x1b[38;2;255;255;255m</requirement>\x1b[38;2;255;255;255m\n'
        in out
    )


def test_config_file_not_formatted_correctly(set_up_repo):
    reqID = set_up_repo[0]
    repo_path = set_up_repo[1]
    section_history_dir = Path(repo_path) / ".sectionHistory"
    section_history_dir.mkdir()
    config_file = section_history_dir / "config.ini"
    config_file.touch()
    config_file.write_text(
        f'[INCORRECT HEADER]\nINCORRECTVALUENAME = <requirement *id *= *"([^"]+)".*?<\/requirement>'
    )
    with pytest.raises(Exception, match="config.ini not formatted correctly"):
        main(repo_path, reqID)


def test_only_one_commit_in_repo(tmp_path: Path):
    repo_path = tmp_path / "repo"
    repo = Repo.init(repo_path)

    section_history_dir = Path(repo_path) / ".sectionHistory"
    section_history_dir.mkdir()
    config_file = section_history_dir / "config.ini"
    config_file.touch()
    config_file.write_text(
        f'[regex_section]\nregex_val = <requirement *id *= *"([^"]+)".*?<\/requirement>'
    )

    myfile = repo_path / "new_text.md"
    myfile.touch()
    reqID = "REQ333"
    myfile.write_text(
        f'<requirement id = "{reqID}" source="jsiwj"> This is THE requirement</requirement>'
    )
    repo.index.add(["new_text.md"])
    repo.index.commit(
        "initial commit", commit_date=date(2022, 7, 21).strftime("%Y-%m-%d %H:%M:%S")
    )
    entries = main(repo_path, reqID, update_cache=False, cache_path="")
    assert len(entries) == 1


def test_cache_force_flag(set_up_repo, create_config_file):
    reqID = set_up_repo[0]
    repo_path = set_up_repo[1]
    myfile = set_up_repo[2]
    repo = set_up_repo[3]

    main(repo_path, update_cache=True, cache_path="", force=False)

    myfile.write_text(
        f'<requirement id = "{reqID}" source="jsiwj"> Original requirement </requirement>'
    )
    repo.git.add(u=True)
    repo.index.commit(
        "new initial commit",
        commit_date=date(2022, 7, 20).strftime("%Y-%m-%d %H:%M:%S"),
    )

    main(repo_path, update_cache=True, cache_path="", force=True)
    entries = main(repo_path, reqID, update_cache=False, cache_path="")
    assert (
        entries[2].text
        == f'<requirement id = "{reqID}" source="jsiwj"> Original requirement </requirement>'
    )


def test_whiteline_change(set_up_repo, create_config_file):
    repo_path = set_up_repo[1]
    myfile = set_up_repo[2]
    repo = set_up_repo[3]
    reqID = "REQ444"
    myfile.write_text(
        f'<requirement id = "{reqID}" source="jsiwj"> New requirement text</requirement>'
    )
    repo.git.add(u=True)
    repo.index.commit(
        "third commit - with new reqid",
        commit_date=date(2022, 7, 23).strftime("%Y-%m-%d %H:%M:%S"),
    )
    myfile.touch()
    myfile.write_text(
        f'<requirement id = "{reqID}" source="jsiwj">\n New requirement  text</requirement>'
    )
    repo.git.add(u=True)
    repo.index.commit(
        "fourth commit", commit_date=date(2022, 7, 24).strftime("%Y-%m-%d %H:%M:%S")
    )
    entries = main(repo_path, reqID, update_cache=False, cache_path="")
    assert (
        entries[0].text
        == f'<requirement id = "{reqID}" source="jsiwj"> New requirement text</requirement>'
        and len(entries) == 1
    )


def test_cache_path_output(set_up_repo, create_config_file, capfd):
    repo_path = set_up_repo[1]
    cache = Cache(repo_path)
    main(repo_path, update_cache=True, cache_path="", force=False)
    out, err = capfd.readouterr()
    assert out.split("\n")[2] == f"Cache location: {cache.get_cache_dir()}"
