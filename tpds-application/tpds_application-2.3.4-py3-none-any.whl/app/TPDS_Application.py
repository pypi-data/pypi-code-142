import os
import sys
import subprocess

from PySide2.QtCore import QDir, QLockFile
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMessageBox
from PySide2.QtGui import QIcon

from tpds.settings import TrustPlatformSettings
from .pyside_check import pyside2_check
from .app import TPDSApplication
from .control import shutdown

def handle_env_check():
    if sys.platform == 'darwin':
        apple_script = """display dialog "Environmental variables are not set correctly or updated. \nTry reinstalling the application" with title "Environment Checks" with icon caution buttons {"OK"}"""
        subprocess.call(['osascript', '-e', apple_script])
        sys.exit()
    else:
        print((
            'Environmental variables are not set correctly or updated.'
            '\nTry reinstalling the application'))
        sys.exit()


"""
# Get requirements file path
if os.getenv('CONDA_PREFIX') not in os.path.abspath(__file__):
    handle_env_check()
"""


def run_app():
    print("This prompt runs Trust Platform GUI, Do NOT close this window.")

    # Configuration system
    # A default configuraiton is built here.
    # Upon start, the user is prompted with a Settings window to override
    # and complete the data set.
    # it is then saved into $HOME/.trustplatform/TPDS_config.json
    config = TrustPlatformSettings()

    if os.getenv('CONDA_PREFIX') is not None:
        # Find and add conda path
        config.settings.conda_path = os.getenv('CONDA_PREFIX')
        # Find and add tpds_core path
#        config.settings.local_path = os.path.join(os.getenv(
#                                            'CONDA_PREFIX'), 'tpds_core')
    # Define a default log file if there is none
    config.settings.log_file = os.path.join(
        QDir.homePath(),
        '.trustplatform',
        'trustplatform.log')
    # Write the above default configuration locally
    config.save()

    # Mainl
    if os.environ.get('XDG_SESSION_TYPE') == 'wayland':
        # This silences the warning locally in ubuntu and seems to resolve some issues
        os.environ['XDG_SESSION_TYPE'] = 'xcb'
        # This uses the qtwayland5 wayland extension which improve performance in wayland based
        # environments - it still throws the warning however
#        os.environ['QT_QPA_PLATFORM'] = 'wayland'

    if sys.platform == 'darwin':
        os.environ['QT_MAC_WANTS_LAYER'] = '1'

    # Clean up old instances if they exist
    if QApplication.instance():
        shutdown()

    # Start the Qt application
    _app = TPDSApplication()
    sys.exit(_app.exec_())

def tpds_app_launch():
    try:
        lock_file = QLockFile(QDir.tempPath() + '/tpds.lock')
        if lock_file.tryLock():
            pyside2_check()
            run_app()
        else:
            exit_app = QApplication(sys.argv)
            config = TrustPlatformSettings()
            # Add application icon
            icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'app.ico')
            exit_app.setWindowIcon(QIcon(icon_path))
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Information)
            error_message.setWindowTitle('Duplicate')
            error_message.setText((
                '''<font color=#0000ff><b>Application is already running</b></font><br>
                <br>Only one instance is allowed. Click OK to close this<br>'''))
            error_message.setStandardButtons(QMessageBox.Ok)
            error_message.exec()
    finally:
        lock_file.unlock()


if __name__ == '__main__':
    tpds_app_launch()
