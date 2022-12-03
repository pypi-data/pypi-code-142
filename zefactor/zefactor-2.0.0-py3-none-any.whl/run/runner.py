import logging
import os
from zefactor.run.entries import Entries
from zind.api.core_find import Find

from zefactor.api.replacer.replacer_manager import ReplacerManager
from zefactor.api.transform.transform_manager import TransformManager
from zefactor.api.finder.finder_refactor import FinderRefactor

class Runner:

  def __init__(self):
    self._transform_manager = TransformManager()

  def compute_refactor(self, loader):

    find_tokens = loader.get_find_tokens()
    replace_tokens = loader.get_replace_tokens()

    file_filter_tokens = loader.get_file_filter_tokens()
    for file_filter_token in file_filter_tokens:
      logging.debug("File filter token: " + str(file_filter_token))

    find = Find()
    file_matches = find.find(loader.get_cwd(), file_filter_tokens)

    entries = Entries()
    finder_refactor = FinderRefactor()
    for file_match in file_matches:
      logging.info("Found file: " + file_match)

      if not file_match.endswith('/'):
        find_token_matches = finder_refactor.scan_file(file_match, find_tokens)

        replacement_map = self._transform_manager.compute_replacement_map(find_token_matches, find_tokens, replace_tokens)
        for find_token_match in replacement_map:
          entries.add_entry(file_match, find_token_match, replacement_map[find_token_match])

    return entries

  def apply_replacement(self, entries):
    replacer_manager = ReplacerManager()
    all_replacements_map = entries.get_replacement_mappings()
    file_mapping = entries.get_file_mapping()

    for filepath in file_mapping:
      replacement_map = {}
      for find_text in file_mapping[filepath]:
        replacement_map[find_text] = all_replacements_map[find_text]

      # Generate backup file
      backup_dir = os.path.dirname(filepath)
      backup_filepath = backup_dir + os.path.sep + os.path.basename(filepath) + ".rr.backup"
      os.rename(filepath, backup_filepath)

      replacer_manager.apply(backup_filepath, filepath, replacement_map)

  def cleanup_backup(self, entries):
    file_mapping = entries.get_file_mapping()
    
    for filepath in file_mapping:
      backup_dir = os.path.dirname(filepath)
      backup_filepath = backup_dir + os.path.sep + os.path.basename(filepath) + ".rr.backup"
      os.remove(backup_filepath)

  def revert_backup(self, entries):
    file_mapping = entries.get_file_mapping()

    for filepath in file_mapping:
      backup_dir = os.path.dirname(filepath)
      backup_filepath = backup_dir + os.path.sep + os.path.basename(filepath) + ".rr.backup"
      os.rename(backup_filepath, filepath)
