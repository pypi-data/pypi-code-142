import sys

from geppetto import text_to_command

if len(sys.argv) == 2:
  r = text_to_command(sys.argv[1])
  print(r['choices'][0]["text"])