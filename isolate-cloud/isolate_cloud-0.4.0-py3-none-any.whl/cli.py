import typer

import isolate_cloud.auth as auth

def main(command: str):
    if command == 'login':
        auth.login()
        exit(0)

    if command == "hello":
        print(f"Hello, {auth.USER.info['name']}")


if __name__ == "__main__":
    typer.run(main)
