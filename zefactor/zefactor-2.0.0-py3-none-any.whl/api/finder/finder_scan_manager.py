from zefactor.api.finder.match_result import MatchResult
from zefactor.api.finder.find_scanner import FindScanner

class FinderScanManager:

  def __init__(self, find_tokens):
    self._find_tokens = find_tokens
    self._find_scanners = []
    self._matches = set()

    self.check_next(" ")

  def check_next(self, char):

    find_scanner = FindScanner(self._find_tokens)
    self._find_scanners.append(find_scanner)

    new_find_scanners = []
    for find_scanner in self._find_scanners:
      result = find_scanner.check_next(char)
      if result == MatchResult.NO_MATCH:
        pass
      elif result == MatchResult.CONTINUE:
        new_find_scanners.append(find_scanner)
      elif result == MatchResult.MATCH:
        self._matches.add(find_scanner.input())
    self._find_scanners = new_find_scanners

  def matches(self):
    self.check_next(" ")
    return list(self._matches)
