#
# cf:
#   https://docs.ansible.com/ansible/latest/dev_guide/developing_inventory.html
#
import glob
import os
import re
import sys
from copy import copy

from ansible.errors import AnsibleParserError
from ansible.module_utils.common.text.converters import to_native
from ansible.utils.display import Display

from ansible.plugins.inventory import BaseInventoryPlugin

try:
    # If ever ansible changes their internal api, don't break
    from ansible.cli.inventory import INTERNAL_VARS
except ImportError:
    INTERNAL_VARS = frozenset(
        [
            "ansible_diff_mode",
            "ansible_config_file",
            "ansible_facts",
            "ansible_forks",
            "ansible_inventory_sources",
            "ansible_limit",
            "ansible_playbook_python",
            "ansible_run_tags",
            "ansible_skip_tags",
            "ansible_verbosity",
            "ansible_version",
            "inventory_dir",
            "inventory_file",
            "inventory_hostname",
            "inventory_hostname_short",
            "groups",
            "group_names",
            "omit",
            "playbook_dir",
        ],
    )

try:
    import cerberus
    import exrex
    import yaml
    from boltons.iterutils import remap, unique

    HAS_DEPENDENCIES = True
except ImportError:
    HAS_DEPENDENCIES = False


DOCUMENTATION = r"""
name: roster
plugin_type: inventory
author:
  - Julien Lecomte (julien@lecomte.at)
short_description: 'Roster is an Ansible yaml inventory plugin with focus on groups applied to hosts.'
requirements:
  - boltons
  - cerberus
  - exrex
description:
  - 'Roster is an Ansible inventory plugin with focus on groups applied to hosts instead of hosts included in groups. It supports ranges (eg: "[0:9]"), regex hostnames (eg: "(dev|prd)-srv"), file inclusions, and variable merging.'
options:
  plugin:
    description: Required field that must always be set to 'roster' for this plugin to recognize it as it's own.
    type: str
    required: true
    choices:
      - roster
"""

EXAMPLES = """
---
# roster.yml
plugin: roster
"""

SCHEMA = r"""
---
include:
  type: list
  default: []
  schema:
    type: string

vars: &vars
  type: dict
  default: {}
  keysrules:
    type: string
    # source: VALID_VAR_REGEX from ansible/playbook/conditional.py
    regex: '^[_A-Za-z]\w*$'

groups:
  type: dict
  default: {}
  keysrules: &group_name
    type: string
    # source: _SAFE_GROUP from somewhere
    regex: '^[_A-Za-z]\w*$'
  valuesrules:
    type: dict
    default: {}
    nullable: true
    schema:
      vars: *vars
      parents:
        type: list
        default: []
        schema: *group_name

hosts:
  type: dict
  default: {}
  keysrules:
    type: string
    # Accept almost anything and validate later
    regex: '^\S+$'
  valuesrules:
    type: dict
    default: {}
    nullable: true
    schema:
      vars: *vars
      groups:
        type: list
        default: []
        schema: *group_name
"""
schema = yaml.safe_load(SCHEMA)

# match a 'flat' part of hostname, that is without [], ()
flat_name_re = re.compile(r"^([^\[\(\]\)]+)")

# match a simple char class
range_seq_re = re.compile(r"^(\[(?:\d+:\d+)\])")
range_seq_parts = re.compile(r"^\[(\d+):(\d+)\]$")

# match a group
group_class_re = re.compile(r"^(\((?:[^\)\s]+)\))")


# ------------------------------------------------------------------------------
# Roster main part
def _recompose_host(hostname, display):
    # convert foo[0-9]bar into parts, eg: foo, [0-9], and bar
    # we'll only exrex the regex'y parts
    #
    # The point being desktop[0-9].example.com should be treated as desktop[0-9]\.example\.com
    # There's probably a much easier way
    #
    # Convert range to regex
    def convert_range_to_regex(value, display):
        match = range_seq_parts.fullmatch(value)
        first = int(match[1])
        second = int(match[2]) + 1

        if first >= second:
            raise Exception(f"Range sequence [{first}:{second}] is invalid")

        fmt = "{:d}"
        if len(match[1]) > 1 and match[1][0] == "0":
            cnt = len(match[1])
            fmt = "{:0" + str(cnt) + "d}"

        retval = "(" + "|".join([str(fmt).format(x) for x in range(first, second)]) + ")"
        retval = exrex.simplify(retval)
        display.vvv(f"    Expand range sequence [{first}:{second}] with '{fmt}' format generates '{retval}'")
        return retval

    retval = []

    original = hostname
    display.vv(f"Splitting hostname = '{hostname}' via exrex...")
    while hostname:
        display.vvv(f"  Current hostname = '{hostname}'")
        for what in [
            [flat_name_re, "plain", re.escape],
            [range_seq_re, "range", lambda x: convert_range_to_regex(x, display)],
            [group_class_re, "group", lambda x: x],
        ]:
            match = what[0].match(hostname)
            if bool(match):
                part = match[0]
                display.vvv(f"    Found {what[1]} section '{part}'")
                retval.append(what[2](part))
                hostname = hostname[len(part) :]
                break
        else:
            raise Exception(f"Failed to recompose range sequence or regex from '{original}'")

    return "".join(retval)


def _split_hosts(hosts: dict, display: Display) -> dict:
    """
    Split hostname if we find a potential regex.

    Parameters
    ----------
    hosts: dict
        Dict of hostname

    display: Display
        Ansible display object

    Returns
    ------
    dict:
        Input, or new array of hostname
    """

    def is_regex(k):
        return "(" in k or "[" in k or ")" in k or "]" in k

    # Is there at least one hostname to split?
    split_required = [True for k in hosts.keys() if is_regex(k)]
    if not split_required:
        return hosts

    retval = {}
    for hostname, item in hosts.items():
        # Skip the item with has no regex by placing it into output list
        if not is_regex(hostname):
            retval[hostname] = item
            continue

        # Ensure we don't reach a memory limit with a sane arbitrary default
        exrex_hostname = _recompose_host(hostname, display)
        display.vv(f'Counting hostnames for "{hostname}"')
        count = exrex.count(exrex_hostname)
        display.vv(f'Generating {count} hostnames from "{hostname}"')
        if count > 1000:
            raise Exception(f'Extraction of the regex hostname "{hostname}" would generate {count} hostnames')

        for hostname in exrex.generate(exrex_hostname):
            retval[hostname] = item

    return retval


class RosterInventoryReader:
    def __init__(self, filepath: str, display: Display):

        """
        Create a roster reader, reading files and offering a data getter

        Parameters
        ----------
        filepath: str
            Main file to read

        display: Display
            Ansible display object
        """
        self._display = display
        self._data = {"vars": {}, "groups": {}, "hosts": {}}
        self._included_files = []
        self._read(filepath, os.path.dirname(filepath))

    @property
    def data(self):
        return self._data

    def _read(self, filepath: str, source_dir: str) -> None:
        """
        Read a file, extracting it's data, and checking recursivity.
        Uses self._included_files.

        Parameters
        ----------
        filepath: str
            File to read

        source_dir: str
            Source location of top file

        Returns
        ------
        dict:
            Input, or new array of hostname
        """
        if filepath in self._included_files:
            raise Exception(f'Recursive infinite dependency loop detected with file "{filepath}"')
        self._included_files.append(filepath)
        self._read_data(filepath, source_dir)
        self._included_files.pop()

    def _read_data(self, filepath: str, source_dir: str) -> None:
        """
        Search all yaml files and their 'include'

        :param filepath: yaml file path to be read and included
        :returns: None
        """

        def remove_hidden_keys(_path, key, _value):
            # drop all items that start with a dot ('.')
            if isinstance(key, str) and (key[0] == "."):
                return False
            # default: keep the item
            return True

        self._display.vv(f'Roster reading file "{filepath}"')

        data = None
        try:
            with open(filepath, encoding="UTF-8") as fd:
                data = yaml.safe_load(fd)
        except yaml.scanner.ScannerError as err:
            err_msg = str(err.problem_mark).strip()
            self._display.warning(f'Syntax error in "{filepath}": {err_msg}: {err.problem}')
        except Exception as err:
            # by default this error should be blocking.
            # - this means that if you checkout a repo with git crypt"ed files, then the plugin will choke on
            #   the binary file and not run with a potentially harmful or empty variable value.
            raise Exception(f'While reading "{filepath}": {to_native(err)}.') from None

        if not data:
            self._display.vv(f'File "{filepath}" is empty')
            return

        # drop hidden fields
        data = remap(data, visit=remove_hidden_keys)
        # drop the 'plugin', it's not needed anymore
        data.pop("plugin", None)

        validator = cerberus.Validator(schema)
        if not validator.validate(data):
            raise Exception("YAML schema validation error: " + str(validator.errors))

        includes = data.pop("include", [])
        for pathname in includes:
            searchpath = pathname

            if not os.path.isabs(searchpath):
                searchpath = os.path.join(source_dir, searchpath)

            files = glob.glob(searchpath, recursive=True)
            if not files:
                # if escaped version is the same, then pathname didn't contain wildcards
                if glob.escape(searchpath) != searchpath:
                    self._display.warning(f'No include files found in path: "{pathname}", included from "{filepath}"')
                else:
                    raise AnsibleParserError(f'Include file not found: "{pathname}", included from "{filepath}"')
            else:
                for file in files:
                    self._read(file, os.path.dirname(file))

        # if a file contains a var, group or host with the same name as previously
        # encountered
        for key in data.keys():
            for k, v in (data[key] or {}).items():
                if k in self._data[key]:
                    self._display.warning(f'Overwriting value "{key}.{k}" in file "{filepath}"')
                self._data[key][k] = v


class RosterInventoryValidator:
    def __init__(self, data: dict, display: Display):
        """
        Create a roster validator, checking keys and ensuring it's valid

        Parameters
        ----------
        data: dict
            Parsed roster file

        display: Display
            Ansible display object
        """
        self._display = display

        self._data = self._validate_data(data)
        self._validate_hosts()
        self._validate_groups()
        self._validate_uniqueness()

    @property
    def data(self):
        return self._data

    @staticmethod
    def _validate_reserved_keyword(name: str) -> bool:
        """
        Raise an exception if keyword is reserved.

        Parameters
        ----------
        name: str
            Any word, name, string
        """
        if name not in INTERNAL_VARS:
            return
        raise Exception(f'Ansible reserved keyword "{name}" is used as a variable name in playbook.')

    def _validate_data(self, data: dict) -> dict:
        """
        Validate the yaml data against a known and valid schema.

        Parameters
        ----------
        data: dict
            Roster inventory

        Returns
        -------
        dict
            Roster inventory
        """
        # discard any invalid files with no hosts
        if not (data or {}).get("hosts"):
            raise AnsibleParserError("Inventory file has no hosts declared")

        def _validate_section(section, key, group_key):
            self._validate_reserved_keyword(key)
            # Add missing keys
            if not data[section].get(key):
                data[section][key] = {}
            if not data[section][key].get("vars"):
                data[section][key]["vars"] = {}
            if not data[section][key].get(group_key):
                data[section][key][group_key] = []
            # Validate variable names
            for k in data[section][key]["vars"].keys():
                self._validate_reserved_keyword(k)

        # Fill in missing parts
        for key in ["vars", "host", "groups"]:
            if not data.get(key):
                data[key] = {}

        for k in data["vars"].keys():
            self._validate_reserved_keyword(k)

        for host in data["hosts"]:
            _validate_section("hosts", host, "groups")

        for group in data["groups"]:
            _validate_section("groups", group, "parents")

        return data

    def _validate_hosts(self) -> None:
        """
        Validate and fixup all root hosts.
        If a group pre-declaration is missing, warn and create.
        """
        hosts = self._data["hosts"]
        groups = self._data["groups"]

        self._display.vv("Validating hosts")
        for hostname, host in hosts.items():
            for groupname in host["groups"]:
                if groupname not in groups:
                    self._display.warning(f"Group '{groupname}' in host '{hostname}' is not declared in root 'groups'")
                    self._data["groups"][groupname] = {"vars": {}, "parents": []}

    def _validate_groups(self) -> None:
        """
        Validate and fixup all group hosts.
        If a group pre-declaration is missing, warn and create.
        """
        groups = self._data["groups"]

        self._display.vv("Validating groups")
        for groupname, group in copy(groups).items():
            for parentname in group["parents"] or []:
                if parentname not in groups:
                    self._display.warning(
                        f"Group '{parentname}' in group '{groupname}' is not declared in root 'groups'",
                    )
                    self._data["groups"][parentname] = {"vars": {}, "parents": []}

    def _validate_uniqueness(self) -> None:
        """
        Verify that host and groups all have unique names.
        """
        for host in self._data["hosts"].keys():
            for group in self._data["groups"].keys():
                if host == group:
                    self._display.warning(
                        f"Host '{host}' has same name than group '{group}'",
                    )


class RosterInventoryParser:
    def __init__(self, data, display, inventory):
        """
        Parameters
        ----------
        data: dict
            Dictionnary of hosts, groups, vars

        inventory: class
            Class to set inventory parts

        display: Display
            Ansible display object
        """
        self._display = display
        self._inventory = inventory

        # Do vars
        self._display.vv("Adding global variables")
        self._add_variables("all", data)

        # Do groups
        self._display.vv("Merging group variables")
        groups = self._merge_group_variables(data["groups"])

        self._display.vv("Calling group methods")
        for name, content in groups.items():
            self._inventory.add_group(name)
            self._add_variables(name, content)
            self._add_groups(name, content, groups)

        # Do hosts
        self._display.vv("Splitting host ranges and regex")
        hosts = _split_hosts(data["hosts"], self._display)

        self._display.vv("Calling host methods")
        for name, content in hosts.items():
            self._inventory.add_host(name)
            self._add_groups(name, content, groups)
            self._add_host_variables(name, content, groups)

        # Call reconcile to ensure "ungrouped" contains all hosts
        self._display.vv("Reconciling inventory")
        self._inventory.reconcile_inventory()

    def _add_variables(self, name: str, content: dict) -> None:
        """
        Add every key, value of "content[vars]" into the inventory at the
        location pointed by "name".

        eg: add_item_vars(name="all", { "vars": { "lang": "fr" }})

        Parameters
        ----------
        name: dict
            content name ("all", "host", "group")

        content: dict
            Dictionnary with "vars"
        """
        if not (content and content.get("vars")):
            return

        for k, v in content["vars"].items():
            self._inventory.set_variable(name, k, v)

    def _merge_group_variables(self, groups: dict) -> dict:
        """
        Merge group variables as long as they are lists.

        Parameters
        ----------
        groups: dict
            Dictionnary containing all the groups

        Returns
        -------
        dict
            Dictionnary containing all the groups
        """

        def parents_are_merged(group):
            # Return False if there's any occurence of an unmerged parent
            return not any(True for x in group["parents"] if not groups[x].get("__merged"))

        def merge_lists(groups, group, key):
            # Add parent variables to retval
            retval = []
            for groupname in group["parents"]:
                parent = groups[groupname]
                if key in parent["vars"]:
                    if key not in retval:
                        retval += parent["vars"][key]
                    else:
                        self._display.vvv(f'Skipping "{key}" duplication')
            if key in group["vars"]:
                retval += group["vars"][key]
            return retval

        # Since groups can have groups that can have other groups, we
        # need to make multiple passes
        done = False
        while not done:
            done = True

            for groupname, group in groups.items():
                if group.get("__merged"):
                    continue
                done = False

                # Parents must all be merged before handling this group
                if not parents_are_merged(group):
                    continue
                group["__merged"] = True

                # Make a list of all var keys that are lists
                keys = self.get_mergeable_variables(group, groups)
                if not keys:
                    continue

                # For every key, append them all together
                for key in keys:
                    groups[groupname]["vars"][key] = merge_lists(groups, group, key)
        return groups

    @staticmethod
    def get_mergeable_variables(content: dict, groups: dict) -> list:
        """
        Get a content's, group or host, variable keys that are lists.

        Parameters
        ----------
        content: dict
            The "hosts" or "groups" content

        groups: dict
            Dictionnary containing all the groups

        Returns
        ------
        list:
            List of keynames
        """
        # Extract every keyname of vars that are lists
        retval = [k for k, v in content["vars"].items() if isinstance(v, list)]

        # Extract the keyname of every vars for the inherited contents
        groupkey = "groups" if "groups" in content else "parents"
        for groupname in content[groupkey]:
            variables = groups[groupname]["vars"]
            retval += [k for k, v in variables.items() if isinstance(v, list)]

        return sorted(unique(retval))

    def _add_groups(self, name: str, content: dict, groups: dict) -> None:
        """
        Get a content's, group or host, variable keys that are lists.

        Parameters
        ----------
        name: str
            Name of group or host

        content: dict
            The "hosts" or "groups" content

        groups: dict
            Dictionnary containing all the groups

        Returns
        ------
        list:
            List of keynames
        """
        if not content:
            return

        groupkey = "groups" if "groups" in content else "parents"
        for group in content.get(groupkey, []):
            if group not in groups:
                self._display.warning(f'Group "{group}" not declared in root groups')
            self._inventory.add_group(group)
            # Add group as parent to group or host
            self._inventory.add_child(group, name)

    def _add_host_variables(self, name, content, groups):
        """
        Parameters
        ----------
        name: str
            Name of host

        content: dict
            The "hosts" content containing key "groups" and "vars"

        groups: dict
            Dictionnary containing all the groups

        Returns
        ------
        list:
            List of keynames
        """
        # make a list of all keys that are lists:
        merge_keys = self.get_mergeable_variables(content, groups)
        if not merge_keys:
            return self._add_variables(name, content)

        # Remove keys that are specified in vars
        for k, _v in content["vars"].items():
            if k in merge_keys:
                merge_keys.remove(k)

        for k in merge_keys:
            for parent_name in content["groups"]:
                # for the first item, we need to create the array
                if k in groups[parent_name]["vars"]:
                    if k not in content["vars"]:
                        content["vars"][k] = []

                    source = groups[parent_name]["vars"][k]
                    try:
                        if isinstance(source, str):
                            raise Exception

                        if source != content["vars"][k]:
                            content["vars"][k] += source
                        else:
                            self._display.vvv(f'Skipping "{source}" duplication')
                    except:
                        raise Exception(
                            f'Trying to concatenate value "{source}" with a list for variable "{k}"',
                        ) from None

        for k, v in content["vars"].items():
            self._inventory.set_variable(name, k, v)
        return None


# ------------------------------------------------------------------------------
# Plugin part
class InventoryModule(BaseInventoryPlugin):
    """
    Host inventory parser for roster.yml source
    """

    NAME = "julien_lecomte.roster.roster"

    def __init__(self):
        super().__init__()

        if not HAS_DEPENDENCIES:
            raise AnsibleParserError(
                "Missing Python3 dependencies. Please install the following Python3 modules: boltons cerberus exrex",
            )

        self._display = Display()

    def verify_file(self, path: str) -> bool:
        """
        Verify if file is usable by this plugin.
        Called directly by Ansible.
        To be accepted by this plugin, file must be a yaml file and contain:

        ~~~yaml
        ---
        plugin: *name*
        ~~~

        Parameters
        ----------
        path: str
            file path

        Returns
        ------
        bool:
            True if file is accepted
        """
        name = "roster"
        ext = ["yml", "yaml"]

        try:
            lpath = path.lower()
            # pylint: disable=consider-using-generator
            if not lpath.endswith(tuple(["." + e.lower() for e in ext])):
                self._display.debug(f'Roster inventory plugin ignoring "{path}": wrong file extension')
                return False

            # if file is called "roster.yml", then accept it without opening it to verify
            if os.path.basename(path) in [f"{name}.{e}" for e in ext]:
                self._display.debug(f'Roster inventory plugin accepting "{path}": exact file name match')
                return True

            self._display.debug(f'Roster inventory plugin opening "{path}"')
            with open(path, encoding="UTF-8") as fd:
                data = yaml.safe_load(fd)

            self._display.debug('Roster inventory plugin looking for "plugin" keyword')
            if data and data.get("plugin") == name:
                self._display.debug('Roster inventory plugin found "plugin" keyword')
                return True

            self._display.warning(f'Roster inventory plugin ignoring "{path}": no "plugin: {name}" key-value')

        except yaml.scanner.ScannerError as err:
            err_msg = str(err.problem_mark).strip()
            self._display.warning(f"Syntax error {err_msg}: {err.problem}")

        except Exception as err:
            self._display.warning(f"Unknown exception: {err}")

        return False

    def parse(self, inventory, loader, path: str, cache: bool = True) -> None:
        """
        Parse the file and convert into inventory.
        Called directly by Ansible.

        Parameters
        ----------
        inventory:

        loader:

        path: str
            file path, passed by ansible

        cache: bool

        Returns
        ------
        """
        try:
            self.display.debug(f"Loading roster schema ({path})")
            reader = RosterInventoryReader(path, self.display)

            self.display.debug(f"Validating roster schema ({path})")
            validator = RosterInventoryValidator(reader.data, self.display)

            self.display.debug(f"Parsing roster schema ({path})")
            RosterInventoryParser(validator.data, self.display, inventory)

        except Exception as err:
            self.display.error(f"Roster inventory plugin error: {err}")
            sys.exit(1)
