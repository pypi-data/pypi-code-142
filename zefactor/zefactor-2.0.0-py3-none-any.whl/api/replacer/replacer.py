class Replacer:

  def _get_max_buffer_size(self, replacement_map):
    max_size = 0
    for replacement_key in replacement_map:
      if len(replacement_key) > max_size:
        max_size = len(replacement_key)
    return max_size + 2 # Must start and end with non alphanumeric char

  def _check(self, buffer, replacement_key):
    if len(buffer) - 2 < len(replacement_key):
      return False

    count = 1
    for char in replacement_key:
      buffer_char = buffer[count:count + 1]
      if buffer_char != char or buffer_char == '\n': # Never match across line breaks
        return False
      count += 1

    # Must terminate with non alphanumeric
    if buffer[count:count + 1].isalnum():
      return False

    return True

  def apply_replacements(self, input_fd, output_fd, replacement_map):

    start = True
    end = False
    buffer = " " # Pad start of input with non alphanumeric

    max_buffer_size = self._get_max_buffer_size(replacement_map)

    while True:
      char = input_fd.read(1)

      if char:
        buffer += char
      elif not end:
        end = True
        buffer += " " # Pad end of input with non alphanumeric
      if len(buffer) == 1:
        return

      if char and len(buffer) < max_buffer_size:
        continue

      match_found = False
      if not buffer[0].isalnum(): # Must start with a non alphanumeric char
        for replacement_key in replacement_map:
          if self._check(buffer, replacement_key):
            match_found = True

            if not start: # Do not write padded start
              output_fd.write(buffer[0])
            else:
              start = False
              
            output_fd.write(replacement_map[replacement_key])
            buffer = buffer[len(replacement_key) + 1:]
            break

      if not match_found:

        if not start: # Do not write padded start
          output_fd.write(buffer[0])
        else:
          start = False
        buffer = buffer[1:]
