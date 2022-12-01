import subprocess

def runShell(cmd: list):
    return subprocess.run(cmd, capture_output = True, shell = True).stdout.decode().strip().split('\n')
