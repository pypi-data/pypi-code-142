import os
import sys
from rich.console import Console
from database import create_note, delete_note, edit_note_content, edit_note_name, add_token
from pygithub import create_github_note, edit_github_note_name, edit_github_note_content, delete_github_note, check_token_validity
from terminal import clear, Help, print_board, print_table

console = Console()


def app():

    userInput = input("🦄 ")

    match userInput:
        case "1":
            note_name = input("Name: ")
            note_content = input("Content: ")
            create_note(note_name, note_content)
            create_github_note(note_name, note_content)
            print_table()
            app()

        case "2":
            note_name = str(input("Note name: "))
            new_name = str(input("New name: "))
            edit_note_name(note_name, new_name)
            edit_github_note_name(note_name, new_name)
            print_table()
            app()

        case "3":
            note_name = str(input("Note name: "))
            new_content = str(input("New content: "))
            edit_note_content(note_name, new_content)
            edit_github_note_content(note_name, new_content)
            print_table()
            app()

        case "4":
            note_name = str(input("Note name: "))
            delete_note(note_name)
            delete_github_note(note_name)
            print_table()
            app()

        case "help":
            Help()
            app()

        case "quit":
            console.print("exited successfully!", style="orchid1")
            os._exit(0)

        case "board":
            print_board()
            app()

        case "add-token":
            console.print("Adding token requires restart!", style="yellow3")
            token = input("Enter github personal access token: ")
            token_valid =  check_token_validity(token)
            if token_valid:
                add_token(token)
            else:
                console.print(
                    "[red]Invalid token[/] -- please check your token or add a new one", style="light_coral")

        case _:
            console.print("oops! invalid text input 😓", style="orchid2")
            console.print(
                "use [orchid2]help[/] to list all existing input", style="indian_red1")
            app()


if __name__ == "__main__":
    try:
        print_table()
        app()
    except (KeyboardInterrupt, EOFError):
        clear()
        sys.exit(0)
