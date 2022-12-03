from .notes import save_note
from .config import config_data
import tkinter
import tkinter.font
from pathlib import Path
import sys

class Gui(tkinter.Tk):
    def __init__(self, config: config_data) -> None:
        super().__init__()

        self.user_config: config_data = config
        self.bind_all('<Control-Return>', self.save_note_and_exit)

        self.title('New Note')

        # Set the logo of the app and make it MacOS compatible
        logo_path: Path = Path(
            Path(__file__).parent, # Get the path to the root of the package
            'assets/logo.png'
            ).absolute()
        logo: tkinter.Image = tkinter.Image('photo', file=f'{logo_path}')
        # Disable type checking because _w is a internal Tkinter var and cant be detected by type checkers
        self.tk.call('wm','iconphoto', self._w, logo)  # type: ignore

        # Set the widgets
        self.set_widgets()
        self.input.focus_set()

        # Start the loops
        self.scrollbar_loop()
        self.title_loop()

        self.mainloop()
    
    def set_widgets(self) -> None:

        font_size: tkinter.font.Font = tkinter.font.Font(size=20)

        # Input widget
        self.input = tkinter.Text(
            self,
            highlightthickness=0,
            padx=20,
            pady=20,
            font= font_size,
            height=9,
            width=30,
            )
        self.input.pack(side=tkinter.LEFT)

        # Scrollbar widget
        self.scrollbar = tkinter.Scrollbar()

        # Set the relation between the textbox and the scrollbar
        self.input.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.input.yview)

        # Clean the menu bar
        self.menu = tkinter.Menu()
        self.config(menu=self.menu)

    def title_loop(self):
        """
        Updates the title text according the first line in the textbox.
        """
        new_title: str = self.input.get('1.0', '1.end')
        if len(new_title) >= 20:
            new_title = new_title[:17] + '...'

        if new_title != '':
            self.title(new_title)
        else:
            self.title('New Note')

        self.after(1, self.title_loop)

    def scrollbar_loop(self):
        """
        Check if the number of lines has exceeded the maximum of the textbox and show or hide a scrollbar as appropriate.
        """
        number_of_lines: int = self.input.get('1.0', 'end-1c').count('\n')

        if number_of_lines > 8:
            self.scrollbar.pack(side=tkinter.RIGHT, fill='y')
        else:
            self.scrollbar.pack_forget()

        self.after(1, self.scrollbar_loop)

    def save_note_and_exit(self, event: tkinter.Event) -> None:
        save_note(
            self.input.get('1.0', '1.end'),
            self.input.get('1.0', 'end-1c'),
            self.user_config
        )
        
        sys.exit(0)
