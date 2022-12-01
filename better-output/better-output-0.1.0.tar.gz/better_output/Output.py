import sys


class Output:
    def __init__(self):
        self._output = ""

    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, value):
        old = self._output
        self._output = value
        old_lines = old.splitlines()
        new_lines = value.splitlines()
        if len(old_lines) != 0:
            # move cursor to top of old output
            sys.stdout.write(f"\u001b[{len(old_lines)}F")
        for i in range(len(old_lines)):
            if i < len(new_lines):
                if old_lines[i] != new_lines[i]:
                    sys.stdout.write(f"\u001b[2K{new_lines[i]}")
                sys.stdout.write("\u001b[1E")  # move cursor down one
            else:
                sys.stdout.write(f"\u001b[2K")
                sys.stdout.write("\u001b[1E")
        if len(new_lines) > len(old_lines):
            for i in range(len(new_lines)-len(old_lines)):
                sys.stdout.write(f"\u001b[2K{new_lines[i+len(old_lines)]}\n")
        sys.stdout.flush()

    def print(self, text):
        self.output += text + "\n"

    def setOutput(self, text):
        self.output = text

    def insertLine(self, index, line):
        lines = self.output.splitlines()
        lines.insert(index, line)
        self.output = "\n".join(lines)
