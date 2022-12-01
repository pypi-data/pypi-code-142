from dataclasses import dataclass, field
from cooptools.commandDesignPattern.commandProtocol import CommandProtocol
from cooptools.commandDesignPattern.exceptions import ResolveStateException
from typing import List, Tuple, TypeVar, Dict
import threading
import copy

T = TypeVar('T')

@dataclass
class CommandController:
    init_state: T
    command_stack: List[CommandProtocol] = field(default_factory=list)
    cache_interval: int = 100
    _cached_states: List[Tuple[T, int]] = field(default_factory=list, init=False)
    cursor: int = field(default=-1, init=False)
    _lock: threading.RLock = field(default_factory=threading.RLock, init=False)

    def __post_init__(self):
        self._cache_state(self.init_state)

    def _cache_state(self, state):
        self._cached_states.append((state, self.cursor))

    def _needsLock(foo):
        def magic(self, *args, **kwargs):
            with self._lock:
                print(f"lock acquired")
                ret = foo(self, *args, **kwargs)
            print(f"Lock released")
            return ret
        return magic

    @_needsLock
    def execute(self, commands: List[CommandProtocol]) -> T:
        print("Executing...")
        # delete any registered commands after the current cursor
        del self.command_stack[self.cursor + 1:]

        # delete any cached states after the current cursor
        for ii, cache in [(ii, x) for ii, x in enumerate(self._cached_states) if x[1] > self.cursor]:
            del self._cached_states[ii]

        # add new commands
        for command in commands:
            self.command_stack.append(command)
            self.cursor += 1

        # resolve
        latest_state = self.resolve()

        # determine to cache
        if self.cursor - self._cached_states[-1][1] > self.cache_interval:
            self._cache_state(latest_state)

        return latest_state

    def resolve(self, idx: int = None) -> T:
        command = None

        if idx is None:
            idx = self.cursor

        if idx == -1:
            return self.init_state

        try:
            state, cached_idx = next(iter(reversed([(x, cached_idx) for x, cached_idx in self._cached_states if cached_idx < idx])))
            state = copy.deepcopy(state)

            # execute the commands in the stack up to the cursor
            for command in self.command_stack[cached_idx + 1:idx + 1]:
                state = command.execute(state)
                if state is None:
                    raise Exception("The command.execute() operation returned a None value")
            return state
        except Exception as e:
            # raise the exception on the command that failed
            raise ResolveStateException(command=command, inner=e)

    @_needsLock
    def undo(self) -> T:
        # move cursor back in time
        if self.cursor > -1:
            self.cursor -= 1

        return self.resolve()

    @_needsLock
    def redo(self) -> T:
        # move cursor forward in time
        if self.cursor < len(self.command_stack):
            self.cursor += 1

        return self.resolve()

    @property
    def CachedStates(self) -> List[Tuple[T, int]]:
        return self._cached_states

    @property
    def ActiveCommands(self):
        return self.command_stack[:self.cursor + 1]

    @property
    def State(self) -> T:
        return self.resolve()