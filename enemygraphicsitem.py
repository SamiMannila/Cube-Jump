from PyQt5 import QtGui
from graphicsitem import GraphicsItem


class EnemyGraphicsItem(GraphicsItem):
    '''
    The class EnemyGraphicsItem extends QGraphicsPolygonItem to link it together to the physical
    representation of a Enemy. The QGraphicsPolygonItem handles the drawing, while the
    Player knows its own location and status.
    '''
    def colorItem(self):
        '''
        Use different colors for different enemy types.
        '''
        type = self.item.get_brain().get_type()
        if not self.item.is_destroyed():
            if type == "Attacking":
                brush = QtGui.QColor(144, 8, 8)
            elif type == "Dumb":
                brush = QtGui.QColor(228, 117, 5)
            else:       # Turning
                brush = QtGui.QColor(123, 117, 111)
        else:           # Destroyed
            brush = QtGui.QColor(255, 255, 255)
        self.setBrush(brush)


