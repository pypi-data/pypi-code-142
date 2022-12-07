from pathlib import Path

import typer

from rattlesume.builder import build_document

app = typer.Typer()


@app.command()
def build(path: Path, preview: bool = False):
    doc = build_document(path)
    if preview:
        from rich import print as rprint
        from rich.markdown import Markdown

        rprint(Markdown(doc))
        return
    print(doc)


if __name__ == "__main__":
    app()
