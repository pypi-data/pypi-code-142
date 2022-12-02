import subprocess
import win32gui, win32con
import re


class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        bla = str(win32gui.GetWindowText(hwnd))
        if re.match(wildcard, bla) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        try:
          win32gui.ShowWindow(self._handle, win32con.SW_SHOWNORMAL)
          win32gui.SetForegroundWindow(self._handle)
        except:
          subprocess.run('"C:\\Users\\enzo\\AppData\\Local\\SourceTree\\SourceTree.exe" "C:\\Users\\enzo\\B&H\\bhpy"', shell=True)

j=0
def i():
  global j
  j+=1
  return j

subprocess.run("code setup.py", shell=True)
input(f'{i()}. Update setup.py [version, download_url(future), install_requires]...')
subprocess.run("code pyproject.toml", shell=True)
input(f'{i()}. Update pyproject.toml [version, Download(future), dependencies]...')

subprocess.run("py -m pip install --upgrade pip", shell=True)
subprocess.run("py -m pip install --upgrade build", shell=True)
subprocess.run("py -m build", shell=True)

version = input(f'{i()}. Enter Version number:')
subprocess.run(f"pip install --upgrade dist/bhpy-{version}.tar.gz", shell=True)

input(f'{i()}. Check if the package works like intended...')

w = WindowMgr()
w.find_window_wildcard(".*Sourcetree.*")
w.set_foreground()
msg = input(f'{i()}. Checkout dev brach and stage changes for commit\   Enter commit message:')
#subprocess.run(f"git commit -m '{msg}'", shell=True)
w.set_foreground()
input(f'{i()}. Merge into main branch...')

subprocess.run('"C:\\Program Files\\Mozilla Firefox\\firefox.exe" -new-tab "https://github.com/bhmarscheck/bhpy/releases/new"', shell=True)
input(f'{i()}. Create release on github:\n    - Title: V 0.0.0(-beta)\n    - Tag: v0.0.0(-alpha/-beta)\n   Press ENTER to continue...')
input(f'{i()}. Check download url...')

subprocess.run("py -m pip install --upgrade twine", shell=True)
subprocess.run("py -m twine upload dist/*", shell=True)

yesNo = input('Reinstall from repo?(Y/n)')
if yesNo in ['y','Y','Yes','yes','YES',None,'']:
  subprocess.run("pip install --upgrade --force-reinstall bhpy", shell=True)
  input(f'{i()}. Test the updated package...')
input('Release done...')
