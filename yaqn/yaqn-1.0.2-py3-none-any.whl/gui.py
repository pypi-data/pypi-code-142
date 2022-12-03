import tkinter
import tkinter.font
from pathlib import Path
from datetime import datetime
import sys

class Gui(tkinter.Tk):
    def __init__(self, notes_path: Path, extension: str) -> None:
        super().__init__()

        self.notes_dir_path: Path = notes_path
        self.extension = extension
        self.bind_all('<Control-Return>', self.save_note_and_exit)

        self.title('New Note')

        # Set the logo of the app and make it MacOS compatible
        logo_path: Path = Path(
            Path(__file__).parent, # Get the path to the root of the package
            'assets/logo.png'
            ).absolute()
        logo: tkinter.Image = tkinter.Image('photo', file=f'{logo_path}')
        self.tk.call('wm','iconphoto', self._w, logo)

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

    def check_note_path(self, note_path: Path) -> Path:
        if not note_path.is_file():
            return note_path
        
        datetime_now: str = datetime.now().strftime('%H%M%S-%d%m%Y')
        new_filename: str = f'{note_path.stem}-{datetime_now}{note_path.suffix}'

        return self.check_note_path(Path(note_path.parent, new_filename))

    def save_note_and_exit(self, event: tkinter.Event) -> None:
        # Set the note file
        self.notes_dir_path.mkdir(parents=True, exist_ok=True)

        # Check if the first line in the textbox is valid as a filename
        note_filename: str
        if self.input.get('1.0', '1.end') != '':
            note_filename = self.input.get('1.0', '1.end')
        else:
            note_filename = datetime.now().strftime('%H%M%S-%d%m%Y')

        # Get the note path and check if its valid
        note_path: Path = Path(self.notes_dir_path, f'{note_filename}.{self.extension}')
        note_path = self.check_note_path(note_path)

        # Get the textbox data and save it
        note:str = self.input.get('1.0', 'end-1c')

        note_path.touch()
        with open(note_path, 'w') as file:
            file.write(note)
        
        sys.exit(0)
