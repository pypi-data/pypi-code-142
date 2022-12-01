"""Description.
Application en ligne de commande pour la modification de l'exercice adaptatif.
"""
from .latex_fin import document
from rich import print
from sympy import Rational
import typer

app = typer.Typer()

@app.command()
def original():
    document()
    print("Les fichier .tex et .pdf sont dans le dossier")

@app.command()
def modify(h: int = 4, l: int = 2, gh: Rational = Rational(1,4), gl: Rational = Rational(1,2)):
    document(h,l,gh,gl)
    print("Les fichier .tex et .pdf sont dans le dossier")