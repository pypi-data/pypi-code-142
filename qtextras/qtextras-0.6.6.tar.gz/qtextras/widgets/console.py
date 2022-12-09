from pyqtgraph.Qt import QtCore, QtWidgets

# Taken directly from https://stackoverflow.com/a/20610786/9463643
try:
    from qtconsole.inprocess import QtInProcessKernelManager
    from qtconsole.rich_jupyter_widget import RichJupyterWidget
except Exception:  # noqa
    # Many things can cause this statement to fail: Kernel already spawned elsewhere,
    # IPython not installed, etc. In any case, pyqtgraph console is an OK fallback
    from pyqtgraph.console import ConsoleWidget
else:

    class ConsoleWidget(RichJupyterWidget):
        """
        Convenience class for a live IPython console widget. We can replace the
        standard banner using the customBanner argument
        """

        def __init__(self, text=None, *args, **kwargs):
            if text:
                self.banner = text
            super().__init__(*args, **kwargs)
            self.kernel_manager = kernel_manager = QtInProcessKernelManager()
            kernel_manager.start_kernel()
            # kernel_manager.kernel.gui = 'qt5'
            self.kernel_client = kernel_client = self._kernel_manager.client()
            kernel_client.start_channels()

            def stop():
                kernel_client.stop_channels()
                kernel_manager.shutdown_kernel()

            self.exit_requested.connect(stop)

            namespace = kwargs.get("namespace", {})
            namespace.setdefault("__console__", self)
            self.pushVariables(namespace)
            parent = kwargs.get("parent", None)
            if parent is not None:
                self.setParent(parent)

        def pushVariables(self, variableDict):
            """
            Given a dictionary containing name / value pairs, push those variables to
            the IPython console widget
            """
            self.kernel_manager.kernel.shell.push(variableDict)

        def clearTerminal(self):
            """
            Clears the terminal
            """
            self._control.clear()

        def printText(self, text):
            """
            Prints some plain text to the console
            """
            self._append_plain_text(text)

        def executeCommand(self, command):
            """
            Execute a command in the frame of the console widget
            """
            self._execute(command, False)


# Sometimes, exceptions in the Ipython stack make it difficult to spawn an ipython
# console even if it is importable Wrap around this issue with a Pyqtgraph console if
# needed
def safeSpawnDevConsole(window: QtWidgets.QMainWindow = None, **consoleLocals):
    """
    Opens a console that allows dynamic interaction with current variables. If IPython
    is on your system, a qt console will be loaded. Otherwise, a (less capable)
    standard pyqtgraph console will be used.
    """
    # "dict" default is to use repr instead of string for internal elements,
    # so expanding into string here ensures repr is not used
    consoleLocals.update(window=window)
    nsPrintout = [f"{k}: {v}" for k, v in consoleLocals.items()]
    text = f"Starting console with variables:\n" f"{nsPrintout}"
    # Broad exception is fine, fallback is good enough. Too many edge cases to properly
    # diagnose when Pycharm's event loop is sync-able with the Jupyter dev console
    try:
        console = ConsoleWidget(parent=window, namespace=consoleLocals, text=text)
    except Exception:  # noqa
        # Ipy kernel can have issues for many reasons. Always be ready to
        # fall back to traditional console
        from pyqtgraph.console import ConsoleWidget as PGConsoleWidget

        console = PGConsoleWidget(parent=window, namespace=consoleLocals, text=text)
    console.setWindowFlag(QtCore.Qt.WindowType.Window)
    console.show()
