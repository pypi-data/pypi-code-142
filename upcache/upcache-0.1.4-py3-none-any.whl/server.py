from internal.tcp import run_cache_server
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        run_cache_server(sys.argv[1], True)
    else:
        print(f"Usage: {sys.executable} {sys.argv[0]} <socket-file>")
