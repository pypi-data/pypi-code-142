import tkinter as tk
from tkinter import filedialog as fd

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import pyco.basis

class pc:
    BasisObject = pyco.basis.BasisObject
    

class Venster(pc.BasisObject):
    """
    Verzorgt uitvoer in nieuw venster gebruik makend van tkinter bibliotheek.
    """

    def __init__(self,
                 breedte:int=600,
                 hoogte:int=600,
                 titel:str='pyco'):
        super().__init__()

        self.breedte = breedte
        self.hoogte = hoogte

        self.root = tk.Tk()
        self.root.title(titel)
        self.root.geometry('{}x{}'.format(self.breedte, self.hoogte))


class TekstVenster(Venster):
    """
    Popup venster met tekstvak en scrollbalk.
    """

    def __init__(self, tekst:str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        s = tk.Scrollbar(self.root, width=20)
        s.pack(side=tk.RIGHT, fill=tk.Y)

        t = tk.Text(self.root, yscrollcommand=s.set, width=self.breedte-22)
        t.insert(tk.INSERT, tekst)
        t.config(state='disabled')
        t.pack(side=tk.LEFT, fill=tk.BOTH)
        s.config(command=t.yview)

        self.root.focus_force()
        self.root.mainloop()


class FiguurVenster(Venster):
    """
    Popup venster met pyco.Figuur object.
    """

    def __init__(self, figuur, *args, **kwargs):
        super().__init__(*args, **kwargs)

        canvas = FigureCanvasTkAgg(figuur.fig, master=self.root)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1.0)
        canvas.draw()

        self.root.focus_force()
        self.root.mainloop()

class BestandsnaamVenster(Venster):
    """
    Popup venster om bestandsnaam te vragen.

    venster = BestandsnaamVenster(extensie='jpg')
    bestandsnaam = venster.bestandsnaam

    if bestandsnaam is None:
        'geannuleerd'
    else:
        tekst = 'dit is wat tekst'
        with open(bestandsnaam, 'w') as f:
            f.write(tekst)
    """

    def __init__(self, extensie:str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.root.geometry('10x10')
        self.bestandsnaam = None

        def popup():
            bestand = fd.asksaveasfilename(
                title='Bewaar als',
                filetypes=['{}-bestand {}'.format(extensie.upper(), extensie)],
                defaultextension=extensie)

            self.bestandsnaam = bestand if len(bestand) > 0 and isinstance(bestand, str) else None

            try:
                self.root.destroy()
            except:
                pass

        # btn = tk.Button(self.root, text='Bewaar als', command=lambda:klik())
        # btn.pack(side = tk.TOP, pady = 20)
        popup()

        # self.root.mainloop()
