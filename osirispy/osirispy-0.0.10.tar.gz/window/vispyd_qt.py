import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)



class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.openFileNameDialog()
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)

        N=42
        xmin=0
        xmax=40
        ymin=0
        ymax=20
        extent=[xmin,xmax,ymin,ymax]
        im=self.canvas.axes.imshow(np.random.random((N,N)),cmap="afmhot",aspect='auto',origin="lower",extent=extent)
        #sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        self.toolbar = NavigationToolbar(self.canvas, None)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        bar = self.menuBar()

        bar.setNativeMenuBar(False)

        file = bar.addMenu("File")

        act=file.addAction("New")
        act.triggered.connect(self.update_plot)
        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Choose File", "","HDF5 Files (*.h5);;All Files (*)", options=options)
        if fileName:
            return fileName

    def update_plot(self):
        # Drop off the first y element, append a new one.
        self.canvas.axes.cla()  # Clear the canvas.
        N=42
        xmin=0
        xmax=40
        ymin=0
        ymax=20
        extent=[xmin,xmax,ymin,ymax]
        im=self.canvas.axes.imshow(np.random.random((N,N)),cmap="afmhot",aspect='auto',origin="lower",extent=extent)
        
        # Trigger the canvas to update and redraw.
        self.canvas.draw()        

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()