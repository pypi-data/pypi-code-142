from .assets import get_logo_path_low_res
from . import __version__
from pathlib import Path
import tkinter

class About(tkinter.Toplevel):
    def __init__(self) -> None:
        super().__init__()

        self.set_widgets()

    def set_widgets(self) -> None:
        self.title('About YAQN')
        self.resizable(False, False)

        # Set the logo of YAQN as the first half of the window
        self.image_frame: tkinter.Frame = tkinter.Frame(self)
        self.image_frame.pack(side=tkinter.TOP)

        # Define the logo as a tkinter image object
        logo_path: Path = get_logo_path_low_res()
        self.logo_image: tkinter.PhotoImage = tkinter.PhotoImage(file=logo_path)

        # Put the image object to a label
        self.image_label: tkinter.Label = tkinter.Label(
            self,
            image=self.logo_image
        )
        self.image_label.pack(
            padx=50,
            pady=(10, 5)
        )

        # Set the texts
        self.text_frame: tkinter.Frame = tkinter.Frame(self)
        self.text_frame.pack()

        # Set the title of the app and make it bold
        font_title: tkinter.font.Font = tkinter.font.Font(weight='bold')

        self.title: tkinter.Label = tkinter.Label(
            self.text_frame,
            text='YAQN',
            font=font_title
        )
        self.title.pack()

        # Set the subtitle
        self.subtitle: tkinter.Label = tkinter.Label(
            self.text_frame,
            text='Yet Another Quick Note'
        )
        self.subtitle.pack()

        # Set the version number and make it smaller
        font_little: tkinter.font.Font = tkinter.font.Font(size=12)

        self.version: tkinter.Label = tkinter.Label(
            self.text_frame,
            text=f'Version {__version__}',
            font=font_little
        )
        self.version.pack(
            pady=(0, 5)
        )

        # Set the created by section
        self.created_by_frame: tkinter.Frame = tkinter.Frame(self)
        self.created_by_frame.pack(side=tkinter.BOTTOM)

        self.kutu_label: tkinter.Label = tkinter.Label(
            self.created_by_frame,
            text='Created with ♥ by\nKutu (@kutu-dev)',
            font=font_little
        )
        self.kutu_label.pack()

        self.other_authors_label: tkinter.Label = tkinter.Label(
            self.created_by_frame,
            text='App icon created by\n\'vladlucha\' in MacOS Icons',
            font=font_little
        )
        self.other_authors_label.pack(
            pady=(0, 25)
        )