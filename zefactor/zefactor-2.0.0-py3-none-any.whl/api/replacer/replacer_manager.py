import os
from io import StringIO
from zefactor.api.replacer.replacer import Replacer

class ReplacerManager:

  def __init__(self):
    self._replacer = Replacer()

  def apply_text(self, text, replacement_map):
    input_fd = StringIO(text)
    output_fd = StringIO()
    self._replacer.apply_replacements(input_fd, output_fd, replacement_map)
    return output_fd.getvalue()

  def apply(self, read_filepath, write_filepath, replacement_map):

    with open(read_filepath, "r") as input_fd:
      with open(write_filepath, "w") as output_fd:
        self._replacer.apply_replacements(input_fd, output_fd, replacement_map)
