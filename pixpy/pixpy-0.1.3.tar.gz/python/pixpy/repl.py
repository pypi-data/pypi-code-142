import pixpy as pix
import pixpy.editor as editor

screen = None
console: pix.Console = None
canvas = None
textedit = None

editing = False

scope = None


def cprint(*text, end='\n'):
    for t in text:
        console.write(str(t))
    console.write(end)


def edit():
    global editing
    console.cancel_line()
    editing = True


def help():
    console.write("Sorry, not yet!\n")


def list():
    i = 1
    for line in textedit.get_lines():
        console.write(f"{i:02} {''.join(line)}\n")
        i += 1


def run():
    code = textedit.get_text()
    try:
        exec(code, None, scope)
    except Exception as e:
        console.write(f"\n## {e}\n> ")


def run_line(line):
    try:
        return eval(line, None, scope)
    except SyntaxError as e:
        exec(line, None, scope)
        return None


def run_repl():
    global screen, console, canvas, editing, textedit, scope
    screen = pix.open_display(width=1280, height=720)
    console = pix.Console(cols=1280 // 8, rows=720 // 16)
    canvas = pix.Image(size=screen.size)
    canvas.clear_mask = 0xffffff00
    history = []
    pos = 0
    textedit = editor.TextEdit()

    scope = {}

    scope['print'] = cprint

    console.write("pixpy REPL\n")
    console.write('> ')
    console.get_line()
    while pix.run_loop():
        if editing:
            textedit.update(pix.all_events())
            if textedit.want_to_quit:
                editing = False
                textedit.want_to_quit = False
                console.get_line()
        for e in pix.all_events():
            if type(e) == pix.event.Key:
                if e.key == pix.key.UP:
                    if pos > 0:
                        pos -= 1
                        console.set_line(history[pos])
                if e.key == pix.key.DOWN:
                    if pos < len(history):
                        pos += 1
                        if pos < len(history):
                            console.set_line(history[pos])
                        else:
                            console.set_line("")
            if type(e) == pix.event.Text:
                line = e.text.rstrip()
                history.append(line)
                pos = len(history)
                console.write("\n")
                try:
                    s = run_line(line)
                    if s is not None:
                        console.write(f":{s}\n> ")
                    else:
                        console.write("> ")
                except NameError as e:
                    console.write(f"## {e}\n> ")
                except Exception as e:
                    console.write(f"## {e}\n> ")
                if not editing:
                    console.get_line()

        if editing:
            textedit.render(screen.context)
        else:
            console.render(screen.context)

        screen.draw(canvas)
        screen.swap()


if __name__ == "__main__":
    run_repl()
