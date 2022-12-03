import sys
from zefactor.input.loader import Loader
from zefactor.run.auto_runner import AutoRunner
from zefactor.input.prompt.prompt_runner import PromptRunner

class RunnerManager:

  def __init__(self):
    pass;

  def run(self):

    loader = Loader()
    continue_run = loader.run()
    if(not continue_run):
      sys.exit(1)

    child_runner = None
    if(loader.is_interactive()):
      child_runner = PromptRunner(loader)
    else:
      child_runner = AutoRunner(loader)

    child_runner.run()

def main():
  runner = RunnerManager()
  runner.run()
