import json
import os
import sys
import logging
from zompt.api.arrow_selection_prompt import ArrowSelectionPrompt
from zompt.api.input_prompt import InputPrompt
from zind.api.core_find import Find
from zefactor.run.entries import Entries
from zefactor.input.prompt.prompt_helper import PromptHelper
from zefactor.run.runner import Runner

class PromptRunner:

  def __init__(self, loader):
    self._prompt_helper = PromptHelper()
    self._loader = loader
    self._runner = Runner()

    self._preview_files = []
    self._preview_extended = True

  def _preview(self, use_previous=False):

    if(not use_previous):
     
      self._preview_files = [] 
      self._preview_extended = True
      find = Find()

      # Provide user a preview of matched files
      file_filter_tokens = self._loader.get_file_filter_tokens()
      file_matches = find.find(self._loader.get_cwd(), file_filter_tokens, only_files=True)

      try:
        for i in range(0,7):
          file_match = next(file_matches)
          #if(file_match is None):
          #  self._preview_extended = False
          #  break
          self._preview_files.append(file_match)
      except StopIteration:
        self._preview_extended = False

      # Check one additional file to see if the sequence stops or continues
      if(self._preview_extended):
        try:
          last_match = next(file_matches)
          if(last_match is None):
            self._preview_extended = False
        except StopIteration:
          self._preview_extended = False

    print("The following files may be edited:")
    for file_match in self._preview_files:
      print(file_match)
    if(self._preview_extended):
      print("... (continued)")
    print()

  def _count_files(self):

    count = 0
    find = Find()
    file_filter_tokens = self._loader.get_file_filter_tokens()
    file_matches = find.find(self._loader.get_cwd(), file_filter_tokens, only_files=True)
    print()
    sys.stdout.flush()

    for file_match in file_matches:
      sys.stdout.write("\r\x1b[K")
      sys.stdout.write("Files found: " + str(count) + " - " + file_match)
      sys.stdout.flush()
      count = count + 1

    sys.stdout.write("\r\x1b[K")
    sys.stdout.write("Files found: " + str(count))
    sys.stdout.flush()
    print()

  def _prompt_file_filters(self):

    print("Add a filter to only edit certain files? (use arrow keys to select)")
    print()
    add_file_filter_prompt = ArrowSelectionPrompt(["no","yes"])
    add_filter = add_file_filter_prompt.run()

    while True and add_filter == "yes":
      self._prompt_helper.clear()
      self._preview(True)

      # Get match include/exclude
      print("Is this filter including or excluding matches? (use arrow keys to select)")
      print()
      file_filter_inclusive_prompt = ArrowSelectionPrompt(["include","exclude"])
      selection = file_filter_inclusive_prompt.run()
      print()
      print()
      input_key = ""
      if(selection == "exclude"):
        input_key = input_key + "e"

      # Get match type
      #self._prompt_helper.clear()
      #self._preview(True)
      #print()
      print("What type of filter is this? (use arrow keys to select)")
      print()
      file_filter_type_prompt = ArrowSelectionPrompt(["full path","filename only","regex"])
      file_filter_type = file_filter_type_prompt.run()
      print()
      print()
      if(file_filter_type == "filename only"):
        input_key = input_key + "f"
      elif(file_filter_type == "regex"):
        input_key = input_key + "r"

      # Get match token
      #self._prompt_helper.clear()
      #self._preview(True)
      #print()
      print("Input token to match against: ", end='')
      sys.stdout.flush()
      file_filter_text_prompt = InputPrompt()
      token_text = file_filter_text_prompt.run()

      valid = self._loader.load_file_filter_token(input_key, token_text)
      if(not valid):
        print("Invalid rule: " + input_key + " was not added.")

      self._prompt_helper.clear()
      self._preview()
      self._count_files()
      if(len(self._preview_files) == 0):
        print()
        print("No matching files.")
        return False

      print()
      print("Add another rule? (use arrow keys to select)")
      print()
      continue_prompt = ArrowSelectionPrompt(["no","yes"])
      continue_selection = continue_prompt.run()
      if(continue_selection == "no"):
        break

    return True

  def _prompt_refactor_tokens(self):

    first_loop = True
    while True:

      if(not first_loop or len(self._loader.get_find_tokens()) == 0):

        if(len(self._loader.get_find_tokens()) > 0):
          self._prompt_helper.clear()
          print("Current find tokens: " + ", ".join(self._loader.get_find_tokens()))
          print()

        sys.stdout.write("Input token to find: ")
        sys.stdout.flush()
        refactor_find_prompt = InputPrompt()
        find_token_text = refactor_find_prompt.run()
        self._loader.add_find_token(find_token_text)


      self._prompt_helper.clear()
      print("Current find tokens: " + ", ".join(self._loader.get_find_tokens()))
      print()
      print("Add another token to find? (use arrow keys to select)")
      print()
      continue_prompt = ArrowSelectionPrompt(["no","yes"])
      continue_selection = continue_prompt.run()
      if(continue_selection == "no"):
        break
      print()

      first_loop = False

    self._prompt_helper.clear()
    print("Current find tokens: " + ", ".join(self._loader.get_find_tokens()))
    print()

    first_loop = True
    while True:

      if(not first_loop or len(self._loader.get_replace_tokens()) == 0):

        if(len(self._loader.get_replace_tokens()) > 0):
          self._prompt_helper.clear()
          print("Current find tokens: " + ", ".join(self._loader.get_find_tokens()))
          print("Current replace tokens: " + ", ".join(self._loader.get_replace_tokens()))
          print()

        sys.stdout.write("Input token to replace: ")
        sys.stdout.flush()
        refactor_replace_prompt = InputPrompt()
        replace_token_text = refactor_replace_prompt.run()
        self._loader.add_replace_token(replace_token_text)
 
      self._prompt_helper.clear()
      print("Current find tokens: " + ", ".join(self._loader.get_find_tokens()))
      print("Current replace tokens: " + ", ".join(self._loader.get_replace_tokens())) 
      print()
      print("Add another token to replace? (use arrow keys to select)")
      print()
      continue_prompt = ArrowSelectionPrompt(["no","yes"])
      continue_selection = continue_prompt.run()
      if(continue_selection == "no"):
        break
      print()

      first_loop = False

  def generate_command(self):

    find_tokens = self._loader.get_find_tokens()
    replace_tokens = self._loader.get_replace_tokens()

    commands = []

    file_filter_tokens = self._loader.get_file_filter_tokens()
    for file_filter_token in file_filter_tokens:
      filter_command = "-g"
      if(not file_filter_token.is_inclusive()):
        filter_command = filter_command + "e"
      if(file_filter_token.is_regex()):
        filter_command = filter_command + "r"
      if(file_filter_token.is_filename_only()):
        filter_command = filter_command + "f"

      filter_text = file_filter_token.get_token()
      filter_command = filter_command + " " + filter_text
      commands.append(filter_command)

    for find_token in find_tokens:
      commands.append("-f " + find_token)
    
    for replace_token in replace_tokens:
      commands.append("-r " + replace_token)

    return " ".join(commands)

  def _run_refactor(self):

    entries = self._runner.compute_refactor(self._loader)

    replacement_mapping = entries.get_replacement_mappings()
    edited_files = entries.get_files()

    self._prompt_helper.clear()

    print()
    command_text = self.generate_command()
    print("You can run the below command next time:")
    print("zefactor -y " + command_text)

    edited_files = entries.get_files()
    entries = self._runner.compute_refactor(self._loader) # This is called again in case any files were edited between prompts.

    if(len(edited_files) == 0):
      print()
      print("No changes detected.")
    else:
 
      # Note this list is different from the preview because it only contains files with matching tokens that will be replaced. 
      print()
      print("The following files will be edited: ")
      for i in range(0, len(edited_files)):
        print(edited_files[i])
        if(i > 7):
          print("... (continued)")
          break

      print()
      print("The following replacements are planned:")
      for find_text in replacement_mapping:
        replacement_text = replacement_mapping[find_text]
        print("    " + find_text + "  ->  " + replacement_text)

      print()

      apply_replacements = "yes"
      print("Apply changes? (use arrow keys to select)")
      print()
      apply_prompt = ArrowSelectionPrompt(["yes","no"])
      apply_replacements = apply_prompt.run()
      print()

      print()
      if(apply_replacements == "yes"):
        self._runner.apply_replacement(entries)
        print("Changes complete")
        print()

        print("Finalize Changes? (use arrow keys to select)")
        print()
        cleanup_prompt = ArrowSelectionPrompt(["yes - delete backup files", "yes - keep backup files", "no - revert changes"])
        cleanup_action = cleanup_prompt.run()
        print()
        if(cleanup_action == "yes - delete backup files"):
          self._runner.cleanup_backup(entries)
          print("Backup files removed.")
        elif(cleanup_action == "yes - keep backup files"):
          print("Backup files retained.")
        elif(cleanup_action == "no - revert changes"):
          self._runner.revert_backup(entries)
          print("Files reverted.")
          print()

  def run(self):

    try:
      self._prompt_helper.clear()
      print("Interactive mode enabled. Disable interactive mode with '-y'.")
      print()

      skip_prompt_refactor_tokens = False

      if(not self._loader.is_skip_refactor()):
        self._preview()
        skip_prompt_refactor_tokens = not self._prompt_file_filters()

        if(not skip_prompt_refactor_tokens):
          self._prompt_helper.clear()
          self._prompt_refactor_tokens()
          self._run_refactor()

#      if(not self._loader.is_skip_rename()):
#        continue_rename = "yes"
#        if(self._loader.is_skip_refactor() or skip_prompt_refactor_tokens):
#          if(skip_prompt_refactor_tokens):
#            print()
#            print("Rename files?")
#            print()
#            continue_rename_prompt = ArrowSelectionPrompt(["yes", "no"])
#            continue_rename = continue_rename_prompt.run()
#          self._prompt_helper.clear()
#          print()
#          if(continue_rename == "yes"):
#            self._prompt_refactor_tokens()
#
#        if(continue_rename == "yes"):
#
#          rename_action = "yes"
#          if(not self._loader.is_skip_refactor() and not skip_prompt_refactor_tokens):
#            print()
#            print("Rename files?")
#            print()
#            rename_prompt = ArrowSelectionPrompt(["yes", "no"])
#            rename_action = rename_prompt.run()
#            print()
#          print()
#
#          if(rename_action == "yes"):
#            self._run_rename()

    except KeyboardInterrupt: 
      pass

    print()
    print("Bye!")
