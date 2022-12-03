class Transform:

  def __init__(self):
    self._transforms = []

  # Add a new transform the list
  def push(self, case, delimiter):
    transform = (case, delimiter)
    self._transforms.append(transform)

  # Apply transforms in order to the input replace tokens
  def apply(self, replace_tokens):

    replacement_text = ""

    for i in range(min(len(self._transforms), len(replace_tokens))):
      case, delimiter = self._transforms[i]
      replace_token = replace_tokens[i]

      if(case == "upper"):
        replace_token = replace_token.upper()
      elif(case == "title"):
        replace_token = replace_token.title()
      elif(case == "lower"):
        replace_token = replace_token.lower()

      replacement_text = replacement_text + replace_token
      if(i < len(replace_tokens) - 1):
        replacement_text = replacement_text + delimiter

    # If there are more replace tokens than find tokens then use the last case and delimiter to guess how to transform them
    diff = len(replace_tokens) - len(self._transforms)
    last_delimiter = None
    last_case = None
    if(diff > 0):
      last_delimiter = self._transforms[-2][1]
      last_case = self._transforms[-1][0]

    for i in range(0, diff):
      replace_token = replace_tokens[i + len(self._transforms)]
      if(last_case == "upper"):
        replace_token = replace_token.upper()
      elif(last_case == "title"):
        replace_token = replace_token.title()
      elif(last_case == "lower"):
        replace_token = replace_token.lower()
      replacement_text = replacement_text + last_delimiter + replace_token

    return replacement_text

  def __str__(self):
    tokens = []
    for case, delimiter in self._transforms:
      tokens.append("(" + case + ", '" + delimiter + "')")
    return "[" + " ".join(tokens) + "]"
