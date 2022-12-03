#from xonsh.main import setup
import os

__version__="0.9.3a"

USERNAME = os.environ.get("USERNAME", 'root')
HOME = os.environ.get('HOME', f'/home/{USERNAME}' if USERNAME != 'root' else '/root')
ASSISTANT_PATH = f"{HOME}/.assistant" if USERNAME != "root" else "/usr/share/assistant"

I18N, L10N = (x for x in os.environ.get('LANG', "en_EN.UTF-8").split(".")[0].split("_"))


#setup()

#del setup
