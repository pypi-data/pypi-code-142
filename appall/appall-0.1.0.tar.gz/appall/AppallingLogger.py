DEFAULT_COLUMN_WIDTH = 100


class LogBufferEntry:
    def __init__(self, message: str = None):
        self._messages = [] if message is None else [message]

    def push(self, message: str):
        self._messages.append(message)

    def print(self, log: callable, column_width: int = DEFAULT_COLUMN_WIDTH):
        printed_string = "f'"

        if len(self._messages) < 1:
            raise ValueError('Nothing to print')

        for message in self._messages:
            printed_string += f'{{"{message}":{column_width}}}'

        log(eval(printed_string + "'"))


class LogBuffer:
    def __init__(self):
        self._entries = []
        self._current_entry_id = None

    def push(self, message: str):
        if self._current_entry_id is None:
            self._entries.append(LogBufferEntry(message))
        elif self._current_entry_id < len(self._entries):
            self._entries[self._current_entry_id].push(message)
            self._current_entry_id += 1
        else:
            self._entries[0].push(message)
            self._current_entry_id = 1

    def loop(self):
        if self._current_entry_id is None:
            self._current_entry_id = 0
        else:
            raise ValueError('Buffer is already looped')

    def print(self, log: callable, column_width: int = DEFAULT_COLUMN_WIDTH):
        for entry in self._entries:
            entry.print(log, column_width)


class AppallingLogger:
    def __init__(self, log: callable = None, sep: str = " "):
        self._log = print if log is None else log
        self._sep = sep
        self._buffer = LogBuffer()

    def log(self, *messages: str):
        # self._log(self._sep.join(message))
        self._buffer.push(self._sep.join(messages))

    def loop(self):
        self._buffer.loop()

    def print(self, column_width: int = DEFAULT_COLUMN_WIDTH):
        self._buffer.print(self._log, column_width)
