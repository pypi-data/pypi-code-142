from zefactor.api.transform.transform import Transform

class TransformManager:

  # Deterimines the case of a token given the prior casing and the next char
  # Cases are either 'upper', 'lower', 'title', or 'none' and if not set Python's None
  def _resolve_case(self, current_case, next_char):
    if(current_case == "none"):
      return current_case

    if(current_case is None):
      if(next_char.isupper()):
        return "title"
      else:
        return "lower"
    else:
      if(next_char.isupper()):
        if(current_case == "title"):
          return "upper"
        elif(current_case == "lower"):
          return "none"
        return current_case
      else:
        if(current_case == "title" or current_case == "lower"):
          return current_case
        else:
          return "none"

  # Outputs a list of operations to apply to replace tokens
  def _classify(self, raw_text, find_tokens):

    transform = Transform()

    case = None
    delimiter = ""

    find_tokens_index = 0
    char_index = 0

    first_raw = False
    for char in raw_text:

      if(first_raw):
        if(char.isalnum()):
          delimiter = ""
          transform.push(case, delimiter)
          if(char.isupper()):
            case = "title"
          else:
            case = "lower"
          char_index = char_index + 1
        else:
          delimiter = char
          transform.push(case, delimiter)
          case = None
        # Reset default values
        delimiter = ""
        first_raw = False
        continue


      case = self._resolve_case(case, char)
      
      if(char.lower() != find_tokens[find_tokens_index][char_index]):
        raise "Classification error"

      char_index = char_index + 1
      first_raw = False

      if(char_index == len(find_tokens[find_tokens_index])):
        find_tokens_index = find_tokens_index + 1
        char_index = 0
        first_raw = True

    # The last token always has a null delimiter.
    delimiter = ""
    transform.push(case, delimiter)

    return transform

  # Computes replacements for the search tokens attempting to follow similar casing and stylistic rules
  def _compute_replacement(self, raw_text, find_tokens, replace_tokens):
  
    transform = self._classify(raw_text, find_tokens)
    return transform.apply(replace_tokens)

  def compute_replacement_map(self, input_texts, find_tokens, replace_tokens):
    replacement_map = {}
    for input_text in input_texts:
      replacement = self._compute_replacement(input_text, find_tokens, replace_tokens)
      replacement_map[input_text] = replacement

    return replacement_map
