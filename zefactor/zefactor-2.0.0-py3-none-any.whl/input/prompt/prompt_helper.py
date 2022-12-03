from os import system, name

class PromptHelper:

  def __init__(self):
    pass

  def clear(self):

    # for windows
    if name == 'nt':
        _ = system('cls')
    
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
