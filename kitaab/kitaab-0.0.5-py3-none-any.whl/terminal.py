'''
    This module has functions that print content on terminal.
'''

import os
from rich.console import Console
from rich.columns import Columns
from rich import box, print
from rich.panel import Panel
from rich.table import Table
from database import get_all_notes
from pygithub import display_github_connection

console = Console()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    print('')
    console.print(" 1 --> New note", style="orchid2")
    console.print(" 2 --> Edit name", style="pale_violet_red1")
    console.print(" 3 --> Edit content", style="light_coral")
    console.print(" 4 --> Delete note", style="red3")
    display_github_connection()


def Help():
    console.print(
        " type add-token --> setup github integration ", style="red3")
    console.print(" type board --> view notes as board ", style="light_coral")
    console.print(" type quit -->  to exit ", style="pale_violet_red1")


def print_table():
    '''
        Creating table using Rich.
    '''

    clear()
    table = Table(title="Al-kitaab", title_style="indian_red1",
                  style="indian_red1", box=box.ROUNDED)

    table.add_column("🌵", style="orange3")
    table.add_column("Name", style="orchid1", header_style="orange3")
    table.add_column("Content", style="medium_spring_green",
                     header_style="orange3")
    table.add_column("Last Modified", style="yellow1",
                     justify="center", header_style="orange3")

    # get all notes from database
    notes = get_all_notes()
    for idx, note in enumerate(notes, start=1):
        table.add_row(str(idx), note["title"], note["content"], note["dateAdded"])
    console.print(table)
    menu()


# BOARD VIEW
def get_content(note):
    '''
        getting content for board view.
    '''

    content = note["content"]
    title = note["title"]
    return f"[medium_spring_green]{content}\n[orchid1]{title}"


def print_board():
    '''
        building board view with Rich.
    '''

    notes = get_all_notes()
    if notes == []:
        console.print("notebook is empty", style='yellow3')
    else:
        note_renderables = [Panel(get_content(note), expand=True,  border_style="indian_red1")for note in notes]
        console.print(Columns(note_renderables))
