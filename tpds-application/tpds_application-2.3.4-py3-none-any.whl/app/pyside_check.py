import subprocess

def pyside2_check():
    # Check if PySide2 and azure packages are installed
    try:
        import PySide2
    except (ModuleNotFoundError, ImportError) as e:
        def run_command(command):
            process = subprocess.Popen(
                            command,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            universal_newlines=True)
            # Poll process.stdout to show stdout live
            while True:
                output = process.stdout.readline()
                if (output == '') and (process.poll() is not None):
                    break
                if output:
                    print(output.strip())
                rc = process.poll()
            return rc
        # Start pyside2 installation through pip
        run_command(['python', '-m', 'pip', 'install', 'pyside2'])
