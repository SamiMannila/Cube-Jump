from PyQt5 import QtWidgets, QtGui, QtCore

from graphicsitem import GraphicsItem


class PlayerGraphicsItem(GraphicsItem):
    '''
    The class PlayerGraphicsItem extends QGraphicsPolygonItem to link it together to the physical
    representation of a Player. The QGraphicsPolygonItem handles the drawing, while the
    Player knows its own location and status.
    '''
    def colorItem(self):
        '''
        Color the player.
        '''
        brush = QtGui.QBrush(1)
        self.setBrush(brush)

