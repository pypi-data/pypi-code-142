import subprocess
import os
import sys

def start_server_daemon(json_file: str) -> None:
    server_py = os.path.join(os.path.dirname(__file__), "server.py")
    subprocess.Popen([sys.executable, server_py, json_file], start_new_session=True)
