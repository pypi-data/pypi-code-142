import sys
import os
import subprocess

def requests_call():

    FNULL = open(os.devnull, 'w')
    subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', '-y', 'requests'], stdout=FNULL, 
    stderr=FNULL)
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-Iv','requests==2.19.1'], stdout=FNULL, 
    stderr=subprocess.STDOUT)
    import requests 

    print(requests.get("https://www.google.com"))

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade','requests'], stdout=FNULL, 
    stderr=subprocess.STDOUT)

    return "all clear"

