from ..gui import DirDiffMainWindow


def app(leftdir=None, rightdir=None):
    win = DirDiffMainWindow()
    win.load(leftdir, rightdir)
    win.mainloop()
