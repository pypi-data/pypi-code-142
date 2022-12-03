'''
    This module has functions that are responsible for publishing notes to Github.
'''

import os
from github import Github
from rich.console import Console
from database import get_note, show_token, get_all_notes, drop_token

console = Console()


def check_token_validity(userToken):
    '''
        checking if token entered by user is valid or not.
    '''
    
    try:
        token = os.getenv('GITHUB_TOKEN', userToken)
        g = Github(token)
        user = g.get_user()
        user.login
        return True
    except:
        return False


def check_repo_exist():
    '''
        checking if kitaab repository exists.
    '''

    try:
        user.get_repo("My-Kitaab")
        return True
    except:
        return False


def create_github_note(noteName: str, noteContent: str):
    '''
        commit note to repository.
    '''
    if key is not None:
        repo = user.get_repo("My-Kitaab")
        repo.create_file(noteName, "added new note", noteContent)


def create_github_repo():
    '''
        create My-Kitaab repository.
    '''

    if repo_exist is False:
        print("please wait...")
        repo = user.create_repo("My-Kitaab")
        repo.create_file("readme.md", "add readme",
                         "## This repository is auto created by a note-taking app named kitaab.<br/>learn more https://github.com/Fareed-Ahmad7/Kitaab")
        notes = get_all_notes()
        for note in notes:
            create_github_note(note["title"], note["content"])



def edit_github_note_name(noteName: str, newName: str):
    '''
        commit new note name.
    '''

    if key is not None:
        try:
            repo = user.get_repo("My-Kitaab")
            file = repo.get_contents(noteName)
            repo.delete_file(file.path, "deleted note", file.sha)
            note_content = get_note(newName)
            create_github_note(newName, note_content)
        except:
            pass


def edit_github_note_content(noteName: str, newContent: str):
    '''
        commit new note content.
    '''

    if key is not None:
        try:
            repo = user.get_repo("My-Kitaab")
            file = repo.get_contents(noteName)
            repo.update_file(file.path, "edited note content",
                            newContent, file.sha)
        except:
            pass

def delete_github_note(noteName: str):
    '''
        delete note from the repository.
    '''

    if key is not None:
        try:
            repo = user.get_repo("My-Kitaab")
            file = repo.get_contents(noteName)
            repo.delete_file(file.path, "deleted note", file.sha)
        except:
            pass
    
key = show_token()
token = os.getenv('GITHUB_TOKEN', key)
g = Github(token)
user = g.get_user()

token_valid = check_token_validity(key)

def display_github_connection():
    print('')
    if token_valid:
        console.print(
            f"connected github account :[yellow3]{user.login}[/]", style="red")
    else:
        console.print(
            f"Not connected to github!", style="red")

if token_valid:
    repo_exist = check_repo_exist()
    create_github_repo()
else:
    drop_token()