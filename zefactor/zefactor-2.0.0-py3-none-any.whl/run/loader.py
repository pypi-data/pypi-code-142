import sys
import logging
from zind.api.file_filter_token import FilterToken
from zind.api.core_find import Find

# Project specific wrapper around argparse
class Loader:

  def __init__(self):
    self._file_filter_tokens = []
    self._interactive = True
    self._skip_refactor = False
    self._skip_rename = False
    self._auto_confirm = False
    self._find_tokens = []
    self._replace_tokens = []
    self._cwd = "."

  def print_arg_error(self, bad_arg):
    print("Error: Unknown input argument: " + bad_arg)

  def print_help(self):
    print("Usage: [-g INCLUDE_FILE ] \t# Only refactor files with matching filename.")
    print("       [-ge EXCLUDE_FILE ] \t# Exclude refactoring files with matching filename.")
    print("       [-f FIND_TOKEN ] \t# Tokens to be replace.")
    print("       [-r REPLACE_TOKEN ] \t# Replacement tokens.")
    print("       [-sn --skip-rename ] \t# Skip renaming files.")
    print("       [-c --confirm ] \t\t# Confirm updates automatically. ")

  def run(self):

    # Setup logging
    logging.basicConfig()
    logging.getLogger().setLevel(logging.WARN)

    index = 1
    input_key = None
    expect_directory = False
    for index in range(1, len(sys.argv)):
      arg = sys.argv[index]

      if(input_key is not None):
        if(input_key == "-f"):
          self._find_tokens.append(arg)
        elif(input_key == "-r"):
          self._replace_tokens.append(arg)
        else:
          parsed = self.load_file_filter_token(input_key, arg)
          if(not parsed):
            self.print_arg_error(sys.argv[index -1])
            self.print_help()
            return False
        input_key = None
      elif(expect_directory):
        self._cwd = arg
        expect_directory
      # Must check '-vv' before '-v'
      elif(arg.startswith('-vv')):
        logging.getLogger().setLevel(logging.DEBUG)
      elif(arg.startswith('-v')):
        logging.getLogger().setLevel(logging.INFO)
      elif(arg == "-d" or arg == "--directory"):
        expect_directory = True
      elif(arg == "-f" or arg == "-r"):
        input_key = arg
      elif(arg == "-y"):
        self._interactive = False
      elif(arg == "-c" or arg == "--confirm"):
        self._auto_confirm = True
      elif(arg.startswith('-g')):
        input_key = arg[2:]
      elif(arg.startswith('--g')):
        input_key = arg[3:]
      elif(arg.startswith('-sr') or arg.startswith('--skip-refactor')):
        self._skip_refactor = True
      elif(arg.startswith('-sn') or arg.startswith('--skip-rename')):
        self._skip_rename = True
      else:
        if(not (arg.startswith('-h') or arg.startswith('--help'))):
            self.print_arg_error(arg)
        self.print_help()
        return False

    return True
    
  def load_file_filter_token(self, input_key, token):
    input_chars = [char for char in input_key]

    inclusive = True
    regex = False
    filename_only = False
    case_sensitive = False

    for char in input_chars:
      if(char == "e"):
        inclusive = False
      elif(char == "r"):
        regex = True
      elif(char == "f"):
        filename_only = True
      else:
        return False

    filter_token = FilterToken(token, inclusive, regex, filename_only, case_sensitive)
    self._file_filter_tokens.append(filter_token)
    return True

  def get_file_filter_tokens(self):
    return self._file_filter_tokens

  def get_find_tokens(self):
    return self._find_tokens

  def get_replace_tokens(self):
    return self._replace_tokens

  def is_interactive(self):
    return self._interactive

  def is_auto_confirm(self):
    return self._auto_confirm

  def is_skip_refactor(self):
    return self._skip_refactor

  def is_skip_rename(self):
    return self._skip_rename

  def add_find_token(self, find_token):
    self._find_tokens.append(find_token)

  def add_replace_token(self, replace_token):
    self._replace_tokens.append(replace_token)

  def get_cwd(self):
    return self._cwd
