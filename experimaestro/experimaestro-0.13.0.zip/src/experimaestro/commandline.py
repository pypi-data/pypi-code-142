"""Command line jobs"""

from collections import ChainMap
import json
import os
import io
from pathlib import Path
from typing import Optional, Union, Callable, Dict
import itertools
import psutil

from experimaestro.utils import logger
from .scheduler import Job, JobError, JobState
from .connectors import Process, Redirect, RedirectType, Connector
from .scheduler import Workspace
from .core.objects import Config


# 5 seconds wait for locking file
LOCKFILE_WAIT_DURATION = 5


class NamedPipeRedirections:
    """List of named pipes"""

    def __init__(self):
        self.outputRedirections: List[Path] = []
        self.errorRedirections: List[Path] = []

    def redirections(self):
        return itertools.chain(self.outputRedirections, self.errorRedirections)


EMPTY_REDIRECTIONS = NamedPipeRedirections()


class CommandPart:
    def __init__(self):
        self.inputRedirect = Redirect.inherit()
        self.outputRedirect = Redirect.inherit()
        self.errorRedirect = Redirect.inherit()

    def forEach(self, f: Callable[["CommandPart"], None]):
        f(self)

    def output(self, context: "CommandContext", out: io.TextIOBase):
        raise NotImplementedError("output for %s" % self.__class__)


class AbstractCommandComponent(CommandPart):
    pass


class CommandContext:
    def __init__(
        self,
        workspace: Workspace,
        connector: Connector,
        path: Path,
        name: str,
        config: Config,
    ):
        self.workspace = workspace
        self.connector = connector
        self.path = path
        self.name = name
        self.config = config
        self.namedPipeRedirectionsMap: Dict["CommandPart", NamedPipeRedirections] = {}
        self.auxiliary: Dict[str, int] = {}

    def getAuxiliaryFile(self, name, suffix):
        ix = self.auxiliary.get(name, 0) + 1
        self.auxiliary[name] = ix
        if ix == 1:
            return self.path / ("%s%s" % (name, suffix))
        return self.path / ("%s-%d%s" % (name, ix, suffix))

    def relpath(self, path):
        return self.connector.resolve(path, self.path)

    def getNamedRedirections(
        self, key: "CommandPart", create: bool
    ) -> NamedPipeRedirections:
        x = self.namedPipeRedirectionsMap.get(key, None)
        if x:
            return x

        if not create:
            return EMPTY_REDIRECTIONS

        x = NamedPipeRedirections()
        self.namedPipeRedirectionsMap[key] = x
        return x

    def writeRedirection(self, out, redirect, stream):
        raise NotImplementedError()

    def printRedirections(
        self, stream: int, out, outputRedirect: Redirect, outputRedirects
    ):
        raise NotImplementedError()


class CommandPath(AbstractCommandComponent):
    def __init__(self, path: Union[Path, str]):
        super().__init__()
        self.path = Path(path)

    def output(self, context, out):
        out.write(context.relpath(self.path))

    def __repr__(self):
        return "Path({})".format(self.path)


class CommandString(AbstractCommandComponent):
    def __init__(self, string: str):
        super().__init__()
        self.string = string

    def output(self, context, out):
        out.write(self.string)

    def __repr__(self):
        return "String({})".format(self.string)


class CommandParameters(AbstractCommandComponent):
    def output(self, context: CommandContext, out: io.TextIOBase):
        path = context.getAuxiliaryFile("params", ".json")
        with path.open("wt") as fileout:
            context.config.__xpm__.outputjson(fileout, context)
        out.write(context.relpath(path))


class AbstractCommand(CommandPart):
    def reorder(self):
        raise NotImplementedError()

    def output(self, context: CommandContext, out: io.TextIOBase):
        list = self.reorder()
        detached = 0

        if len(list) > 1:
            out.write("(\n")

        for command in list:
            # Write files
            namedRedirections = context.getNamedRedirections(command, False)

            # Write named pipes
            def mkfifo(file: Path):
                out.write(" mkfifo {}" % context.relpath(file))

            for file in namedRedirections.redirections():
                mkfifo(file)

            if command.inputRedirect.type == RedirectType.FILE:
                out.write(
                    " cat {} | ".format(context.relpath(command.inputRedirect.path))
                )

            command.output(context, out)

            context.printRedirections(
                1, out, command.outputRedirect, namedRedirections.outputRedirections
            )
            context.printRedirections(
                2, out, command.errorRedirect, namedRedirections.errorRedirections
            )

            out.write('|| checkerror "${PIPESTATUS[@]}" || exit $?')

        # Monitors detached jobs
        for i in range(detached):
            out.write("wait $CHILD_{} || exit $?%\n".format(i))

        if len(list) > 1:
            out.write(")\n")


class Command(AbstractCommand):
    def __init__(self):
        super().__init__()
        self.components = []

    def add(self, component: AbstractCommandComponent):
        self.components.append(component)

    def __repr__(self):
        return "Command({})".format(",".join(str(c) for c in self.components))

    def output(self, context, out):
        first = True
        for c in self.components:
            if first:
                first = False
            else:
                out.write(" ")
            c.output(context, out)

    def forEach(self, f: Callable[["CommandPart"], None]):
        f(self)
        for c in self.components:
            c.forEach(f)


class CommandLine(AbstractCommand):
    """A command line is composed of one or more commands"""

    def __init__(self):
        super().__init__()
        self.commands = []

    def add(self, command: Command):
        self.commands.append(command)

    def forEach(self, f: Callable[["CommandPart"], None]):
        f(self)
        for command in self.commands:
            command.forEach(f)

    def reorder(self):
        return self.commands


class CommandLineJob(Job):
    def __init__(
        self,
        commandline: CommandLine,
        parameters,
        workspace: Optional[Workspace] = None,
        launcher=None,
        dryrun=False,
    ):
        super().__init__(
            parameters, workspace=workspace, launcher=launcher, dryrun=dryrun
        )
        self.commandline = commandline

    async def aio_process(self) -> Optional[Process]:
        """Returns the process if there is one"""
        if self._process:
            return self._process

        if self.pidpath.is_file():
            # Get from pidpath file
            from experimaestro.connectors import Process

            pinfo = json.loads(self.pidpath.read_text())
            p = Process.fromDefinition(self.launcher.connector, pinfo)
            if p is None:
                return None

            if await p.aio_isrunning():
                return p

            return None

        return None

    @property
    def environ(self):
        return ChainMap(
            self.workspace.environment.environ,
            self.launcher.environ if self.launcher else {},
        )

    @property
    def notificationURL(self):
        if self.launcher and self.launcher.notificationURL:
            return self.launcher.notificationURL
        return self.workspace.notificationURL

    async def aio_run(self):
        if self._process:
            return self._process

        assert self.launcher is not None, "No launcher defined for this job"

        # Use the lock during preparation
        logger.info("Running job %s...", self)

        scriptbuilder = self.launcher.scriptbuilder()
        processbuilder = self.launcher.processbuilder()
        donepath = self.donepath

        # Check again if done (now that we have locked)
        if donepath.is_file():
            logger.info("Job %s is already done", self)
            return JobState.DONE

        # Now we can write the script
        scriptbuilder.lockfiles.append(self.lockpath)
        scriptbuilder.command = self.commandline
        scriptbuilder.notificationURL = self.notificationURL
        scriptPath = scriptbuilder.write(self)

        processbuilder.environ = self.environ
        processbuilder.command.append(self.launcher.connector.resolve(scriptPath))
        processbuilder.stderr = Redirect.file(self.stderr)
        processbuilder.stdout = Redirect.file(self.stdout)

        logger.info("Starting job %s", self.jobpath)
        self._process = processbuilder.start()

        with self.pidpath.open("w") as fp:
            json.dump(self._process.tospec(), fp)

        self.state = JobState.RUNNING
        logger.info("Process started (%s)", self._process)
        return self._process


class CommandLineTask:
    def __init__(self, commandline: CommandLine):
        self.commandline = commandline

    def __call__(self, pyobject, *, launcher=None, workspace=None, dryrun=False) -> Job:
        return CommandLineJob(
            self.commandline,
            pyobject,
            launcher=launcher,
            workspace=workspace,
            dryrun=dryrun,
        )
