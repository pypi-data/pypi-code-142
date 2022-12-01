import typer


app = typer.Typer()


@app.callback()
def callback():
    """
    Awesome Portal Gun
    """


@app.command()
def common():
    typer.echo("Hi mate!")


@app.command()
def official():
    typer.echo("Hello, sir!")

#@app.command()
#def test():
#    print("Test OK!")
