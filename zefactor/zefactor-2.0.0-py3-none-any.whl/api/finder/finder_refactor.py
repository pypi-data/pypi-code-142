from zefactor.api.finder.finder_scan_manager import FinderScanManager
from io import StringIO

class FinderRefactor:

  def __init__(self):
    pass

  def scan_text(self, text, find_tokens):
    input_fd = StringIO(text)
    for item in self._scan(input_fd, find_tokens):
      yield item

  def scan_file(self, filepath, find_tokens):
    try:
      first_char = True
      with open(filepath, "r") as input_fd:
        for item in self._scan(input_fd, find_tokens):
          yield item
    except UnicodeDecodeError:
      print("[WARNING] could not decode: " + filepath + " as utf-8, skipping refactor.")
      #if(not self._suppress_warnings):

  # Scans files and finds flexible matching patterns to the search tokens.
  def _scan(self, input_fd, find_tokens):

    finder_scan_manager = FinderScanManager(find_tokens)
    finder_scan_manager.check_next(" ") # Pad beginning with space

    while True:

      char = input_fd.read(1)
      check_char = char
      if not char:
        check_char = " "

      finder_scan_manager.check_next(check_char)

      if not char:
        finder_scan_manager.check_next(" ") # Pad ending with space
        return finder_scan_manager.matches()
