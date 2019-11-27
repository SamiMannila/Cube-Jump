from PyQt5 import QtWidgets, QtGui, QtCore
from location import RIGHT
from game import SQUARE_SIZE


class GraphicsItem(QtWidgets.QGraphicsPolygonItem):
    '''
    This class represents all graphics items of the game. We use this class since otherwise we would have to
    copy multiple lines of code.
    '''
    def __init__(self, item):
        # let's call init for the parent object
        super(GraphicsItem, self).__init__()
        self.item = item
        self.square_size = SQUARE_SIZE
        self.constructTriangleVertices()
        self.colorItem()
        self.updateAll()

    # let's borrow the triangle structure from robots.py from our course
    # we will upgrade this later to achieve more interesting game characters
    # This is just for creating the first look of the game.

    def constructTriangleVertices(self):
        '''
        This method sets the shape of this item into a box.

        The QGraphicsPolygonItem can be in the shape of any polygon.
        We use triangles to represent robots, as it makes it easy to
        show the current facing of the item.
        '''
        # Create a new QPolygon object
        box = QtGui.QPolygonF()

        # Add the corners of a triangle to the the polygon object

        box.append(QtCore.QPointF(self.square_size, 0))  # Tip
        box.append(QtCore.QPointF(0, 0))  # Tip
        box.append(QtCore.QPointF(0, self.square_size))    # Bottom-left
        box.append(QtCore.QPointF(self.square_size, self.square_size))     # Bottom-right

        # Set this newly created polygon as this Item's polygon.
        self.setPolygon(box)

        # Set the origin of transformations to the center of the triangle.
        # This makes it easier to rotate this Item.
        self.setTransformOriginPoint(SQUARE_SIZE/2, SQUARE_SIZE/2)

    def updateAll(self):
        '''
        Updates the visual representation to correctly resemble the current
        location, direction and status of the parent item.
        '''
        self.updatePosition()
        self.updateFacing()
        self.colorItem()

    def updatePosition(self):
        '''
        Update the coordinates of this item to match the attached item.

        See: For setting the position of this GraphicsItem, see
        QGraphicsPolygonItem at http://doc.qt.io/qt-5/qgraphicspolygonitem.html
        and its parent class QGraphicsItem at http://doc.qt.io/qt-5/qgraphicsitem.html
        '''
        x = self.item.location.get_x()
        y = self.item.location.get_y()
        self.setPos(x - SQUARE_SIZE/2, y - SQUARE_SIZE/2)

    def updateFacing(self):
        '''
        Update the facing of this item to match the attached item.
        '''
        facing = self.item.get_facing()
        if facing == RIGHT:
            facing_deg = 90
        else:
            facing_deg = 270
        self.setRotation(facing_deg)

    def colorItem(self):
        '''
        Color the item.
        '''
        pass
