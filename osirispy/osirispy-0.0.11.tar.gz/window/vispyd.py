from tkinter.filedialog import askopenfilename

filename = askopenfilename(filetypes=[("HDF5 Files","*.h5")])


print(filename)
import sys
sys.path.insert( 0,"/Users/pardalio/Documents/Dev/plots/data_read/osirispy")
import osirispy as ospy
#import osirispy as ospy

import numpy as np
import matplotlib.pyplot as plt
import h5py 

data=ospy.read(filename)



import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig = Figure(figsize=(5, 4), dpi=120)
t = np.arange(0, 3, .01)
ax = fig.add_subplot()

match data.datatype:
    case "grid":
        xax=data.axis[0].ax_arr
        ax.plot(xax,data.data)
        ax.set_xlabel(data.axis[0].name)
        ax.set_ylabel(data.name)
        if(data.dims==2):
            yax=data.axis[1].ax_arr
            ax.imshow(data.data,extent=[xax[0],xax[-1],yax[0],yax[-1]],
                aspect="auto",origin="lower",cmap="afmhot",vmin=0,vmax=1e-28)
            ax.set_ylabel(data.axis[0].name)
        if(data.dims==3):
            slice_idx=data.axis[2].ax_arr.nx//2
            ax.imshow(data.data[:,:,slice_idx],extent=[xax[0],xax[-1],yax[0],yax[-1]],
                aspect="auto",origin="lower",cmap="afmhot",vmin=0,vmax=1e-28)

    case "particles":
        ax.scatter(data.data["x1"],data.data["x2"],c="k",s=1)
        ax.set_xlabel(data.label["x1"])
        ax.set_ylabel(data.label["x2"])
    case "tracks-2":
        for part in range(len(tracks1.data["x1"])):
            ax.plot(data.data["x1"][part],data.data["p2"][part],c="k")
        ax.set_xlabel(data.label["x1"])
        ax.set_ylabel(data.label["x2"])

    case _:
        exit()




canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()

# pack_toolbar=False will make it easier to use a layout manager later on.
toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()

"""
frame = tkinter.Frame(root)
frame.pack( fill=tkinter.BOTH, expand=True)
button_quit = tkinter.Button(master=frame, text="Axes", command=root.destroy)
button_quit.pack(side=tkinter.LEFT, anchor="w")


button_quit2 = tkinter.Button(master=frame, text="Data", command=root.destroy)
button_quit2.pack(side=tkinter.LEFT, anchor="w", expand=True)

"""

toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

tkinter.mainloop()
