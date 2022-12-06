#
# Copyright 2022-present Linaro Limited
#
# SPDX-License-Identifier: MIT

from urllib.parse import ParseResult, urlparse
import yaml
import logging
import subprocess

from pathlib import Path
from tuxtrigger.inputvalidation import YamlValidator
from tuxtrigger.exceptions import TuxtriggerException

LOG = logging.getLogger("tuxtrigger")


def yaml_load(data):
    return yaml.load(data, Loader=yaml.FullLoader)


def yaml_file_read(file_path: Path):
    with file_path.open("r") as file:
        loaded_yaml = yaml_load(file)
    return loaded_yaml


def yaml_file_write(data_input, file_path: Path):
    with file_path.open("w") as writer:
        yaml.dump(data_input, writer, default_flow_style=False, sort_keys=False)


def create_repo_list(data_input):
    if data_input is None:
        raise TuxtriggerException("Data input is none")
    for item in data_input["repositories"]:
        yield YamlValidator(**item)


def compare_sha(url_key, branch_name, input_dict, data_yaml_file) -> bool:
    if data_yaml_file is None:
        LOG.warning("\t*** Data Input is none, not able to compare sha")
        LOG.debug(f'\t-> sha: {input_dict[branch_name]["sha"]}')
        return False
    if branch_name not in data_yaml_file[url_key]:
        LOG.warning("\t*** Branch not found in yaml file")
        LOG.debug(f"\t*** branch name: {branch_name}")
        return False
    if (
        not input_dict[branch_name]["sha"]
        == data_yaml_file[url_key][branch_name]["sha"]
    ):
        LOG.info(
            f'\t-> sha: {input_dict[branch_name]["sha"]} vs \
        previous sha {data_yaml_file[url_key][branch_name]["sha"]}'
        )
        return True
    LOG.info(f'\t-> sha: {input_dict[branch_name]["sha"]}')
    LOG.info("\t-> no changes")
    return False


def create_squad_project(url: ParseResult, branch_name: str, prefix=None) -> str:
    url_fragment = (url.path).split("/")
    url_fragment = list(filter(None, url_fragment))
    if prefix is None:
        return f'{(url_fragment[-1]).replace(".git","")}-{branch_name.replace("/","-")}'
    return f'{prefix}-{(url_fragment[-1]).replace(".git","")}-{branch_name.replace("/","-")}'


def run_lsremote(repository: str, branch: str) -> dict:
    value_dict = dict()
    git_result = subprocess.run(
        ["git", "ls-remote", repository, branch],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    splited_value = git_result.stdout.split()
    value_dict[branch] = {"sha": "", "ref": ""}
    if git_result.returncode != 0:
        return value_dict

    if splited_value:
        value_dict[branch] = {"sha": splited_value[0], "ref": splited_value[1]}

    return value_dict


def run_lsremote_regex(repository: str, regex: str) -> dict:
    value_dict = dict()  # type: dict[str, str]
    git_result = subprocess.run(
        ["git", "ls-remote", "--refs", repository, regex],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if git_result.returncode != 0:
        return value_dict

    splited_value = git_result.stdout.split("\n")
    for value in splited_value:
        if len(value) > 1:
            temp_list = value.split("\t")
            branch_list = temp_list[1].split("/")
            branch = "/".join(branch_list[int(len(branch_list) / -2) :])  # noqa: E203
            value_dict[branch] = temp_list[0]
    return value_dict


def create_dynamic_configuration(yaml_data):
    if yaml_data is None:
        raise TuxtriggerException(
            "*** Not able to generate data - config file not read"
        )
    LOG.debug("* Generating configuration")
    for repo in yaml_data["repositories"]:
        if "branches" not in repo.keys():
            repo["branches"] = []
        LOG.debug(f'Checking repository - {repo.get("url")}')
        if "regex" in repo:
            LOG.info(
                f'* Regex value present in config - {repo["regex"]} , looking for branches'
            )
            git_branch_updated = run_lsremote_regex(repo.get("url"), repo.get("regex"))
            for new_branch in git_branch_updated:
                if new_branch in str(repo["branches"]):
                    LOG.info(f"** Branch {new_branch} in config file, skip the branch")
                    continue
                repo["branches"].append(
                    {
                        "name": new_branch,
                        "squad_project": create_squad_project(
                            urlparse(repo.get("url").rstrip("/")),
                            new_branch,
                            repo.get("squad_project_prefix"),
                        ),
                        "plan": repo.get("default_plan"),
                    }
                )
            LOG.info("* Dynamic Config Generated")
    LOG.debug(f"updated yaml_data: {yaml_data}")
    return yaml_data


def pre_tux_run(script_path, repo_url, branch, branch_value_dict, repo_changed):
    if script_path is None:
        LOG.info("** No script path provided")
        return
    if not repo_changed:
        LOG.info("** Repo not changed, Script not invoked")
        return
    new_sha = branch_value_dict[branch]["sha"]
    script_result = subprocess.run(
        [script_path, repo_url, branch, new_sha],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if script_result.returncode != 0:
        LOG.warning("script was not invoked properly")
        raise TuxtriggerException(
            f"** Script was not invoked properly - {script_result.stderr}"
        )
    LOG.info(f"stdout: {script_result.stdout}")
    LOG.info(f"*** Script {script_path} performed astonishingly wonderful")
