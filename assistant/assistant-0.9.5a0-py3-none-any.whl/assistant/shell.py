from xonsh import shell

from assistant.cli import interactive

class AssistantShell(shell.Shell):
    def __init__(self, execer):

        super().__init__(execer)