import typer


app = typer.Typer()


@app.callback()
def callback():
    """
    Awesome Portal Gun
    """


@app.command()
def common(upper: bool = typer.Option(False, help="Say hi uppercase.")):
    if upper:
        text = "HI MATE!" 
    else:
        text = "Hi mate!" 
    typer.echo(text)


@app.command()
def official():
    typer.echo("Hello, sir!")

@app.command()
def test():
    print("Test OK!")
