from jsonc_parser import parser
from os import path
print(parser.JsoncParser.parse_file(path.abspath(path.expanduser('~/.config/TPython/config.jsonc'))))