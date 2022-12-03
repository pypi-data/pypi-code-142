from zefactor.api.finder.match_result import MatchResult

# Given a list of tokens like [ happy, turtle ]
# It will check against a stream of characters to see if they match

PLACEHOLDER = " " # Need a non-alphanumeric symbol
class FindScanner:

  def __init__(self, find_tokens):
    self.match_result_state = MatchResult.CONTINUE
    self._match_chars = [PLACEHOLDER] + list(PLACEHOLDER.join(find_tokens)) + [PLACEHOLDER]
    self._input = []
    self._first = True

  def _set_result(match_result):
    if self.match_result_state == MatchResult.CONTINUE:
      self.match_result_state = match_result
    else:
      # Occurs if find scanner is tasked to check a char when it is already in a final state
      raise Exception("FindScanner final state overridden")

  def input(self):
    start = 0
    end = len(self._input)
    if not self._input[0].isalnum():
      start += 1
    if not self._input[-1].isalnum():
      end -= 1
    return "".join(self._input[start:end])

  def _check_next(self, char):
    if len(self._match_chars) == 0:
      return MatchResult.NO_MATCH

    match_char = self._match_chars.pop(0)
    if self._first:
      self._first = False
      if char.isalnum():
        return MatchResult.NO_MATCH

    if match_char == PLACEHOLDER:
      if char.isalnum():
        return self._check_next(char)
      else:
        return self._continue()
    elif match_char.upper() == char.upper():
      return self._continue()
    else:
      return MatchResult.NO_MATCH


  def check_next(self, char):
    self._input.append(char)
    return self._check_next(char)

  def _continue(self):
    if len(self._match_chars) == 0:
      return MatchResult.MATCH
    else:
      return MatchResult.CONTINUE

