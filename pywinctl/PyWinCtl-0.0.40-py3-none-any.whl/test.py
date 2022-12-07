import pywinctl as pwc
import tkinter as tk


class Window(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("My Overlay")
        self.overrideredirect(True)
        # self.attributes("-topmost", True)
        # self.attributes("-toolwindow", True)

        self.counter = 0
        self.label = tk.Label(text=str(self.counter), bg="black", fg="white", font="FreeSans 14")
        self.label.pack(fill=tk.BOTH, expand=1)

        self.wait_visibility(self)  # Required to assure window is already created before getting its object
        self.attributes("-alpha", 0.7)
        self.geometry('{0}x{1}+{2}+{3}'.format(100, 100, 200, 100))
        self.pwcWindow = pwc.Window(self.frame())

        self.display()

    def display(self):
        self.pwcWindow.alwaysOnTop()
        self.counter += 1
        self.label.configure(text=str(self.counter))
        self.after(1000, self.display)


root = Window()
root.mainloop()


