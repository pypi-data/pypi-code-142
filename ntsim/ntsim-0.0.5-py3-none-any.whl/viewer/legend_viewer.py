import OpenGL.GL as GL

import pyqtgraph as pg
from pyqtgraph.opengl import GLAxisItem, GLGraphicsItem, GLGridItem, GLViewWidget
from pyqtgraph.Qt import QtCore, QtGui

from particle import Particle
import ntsim.utils.pdg_colors as dict_colors

from collections import Counter
import numpy as np

class GLPainterItem(GLGraphicsItem.GLGraphicsItem):
    def __init__(self, **kwds):
        super().__init__()
        glopts = kwds.pop('glOptions', 'additive')
        self.setGLOptions(glopts)

    def configure(self, particle_id, cascades):
        self.particle_id = particle_id
        self.cascade_id = cascades

    def paint(self):
        self.setupGLState()

        painter = QtGui.QPainter(self.view())
        particle_types = Counter([track[0] for track in self.particle_id.values()])
        cascade_types = Counter([track for track in self.cascade_id['pdgid']])
#        total_types = particle_types + cascade_types
        indent = 30
        tab = 0
        painter.setPen(QtCore.Qt.GlobalColor.white)
        painter.drawText(tab, 15, 'Tracks:')
        for particle in particle_types.most_common():
            if particle[0] in dict_colors.pdg_colors:
                self.draw(painter, particle[0], particle[1], dict_colors.pdg_colors[particle[0]], tab, indent)
            else:
                self.draw(painter, particle[0], particle[1], [122, 122, 122], tab, indent)
            indent += 15
        indent = 30
        tab = 120
        painter.setPen(QtCore.Qt.GlobalColor.white)
        painter.drawText(tab, 15, 'Cascades:')
        for cascade in cascade_types.most_common():
            if cascade[0] in dict_colors.pdg_colors:
                self.draw(painter, cascade[0], cascade[1], dict_colors.pdg_colors[cascade[0]], tab, indent)
            else:
                self.draw(painter, cascade[0], cascade[1], [122, 122, 122], tab, indent)
            indent += 15
        painter.end()

    def draw(self, painter, particle, number_of_particles, color_particle, tab, indent):
        painter.setPen(QtGui.QColor(*color_particle))
        painter.setRenderHints(QtGui.QPainter.RenderHint.Antialiasing | QtGui.QPainter.RenderHint.TextAntialiasing)

        rect = self.view().rect()
        af = QtCore.Qt.AlignmentFlag
        tf = QtCore.Qt.TextFlag

        info = f"{Particle.from_pdgid(particle)} : {number_of_particles}"
        painter.drawText(tab, indent, info)

    def clean_view():
        painter = None
