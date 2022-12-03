class Entries:

  def __init__(self):
    # Map input text to replacement text
    self._replacement_mapping = {}

    # Track which files have which replacement tokens present
    self._file_mapping = {}

  def add_entry(self, filename, find_text, replace_text):
    self._replacement_mapping[find_text] = replace_text
    if(filename not in self._file_mapping):
      self._file_mapping[filename] = []

    self._file_mapping[filename].append(find_text)

  def get_replacement_mappings(self):
    return self._replacement_mapping

  def get_file_mapping(self):
    return self._file_mapping

  def get_files(self):
    return list(self._file_mapping.keys())
