import typer


app = typer.Typer()


@app.callback()
def callback():
    """
    Awesome Portal Gun
    """


@app.command(upper: bool = typer.Option(False, help="Is uppercase."))
def common():         
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
