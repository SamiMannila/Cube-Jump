from PyQt5 import QtWidgets, QtCore, QtGui
from game import SQUARE_SIZE


class BulletGraphicsItem(QtWidgets.QGraphicsPolygonItem):
    '''
    This class represents the 2d representation of the bullet that player can shoot enemies with.
    '''
    def __init__(self, item):
        # let's call init for the parent object
        super(BulletGraphicsItem, self).__init__()
        self.item = item
        self.square_size = SQUARE_SIZE
        self.constructTriangleVertices()
        self.updateAll()

    def constructTriangleVertices(self):
        '''
        This method sets the shape of this item into a triangle.

        The QGraphicsPolygonItem can be in the shape of any polygon.
        We use triangles to represent robots, as it makes it easy to
        show the current facing of the item.
        '''
        # Create a new QPolygon object
        triangle = QtGui.QPolygonF()

        # Add the corners of a triangle to the the polygon object
        triangle.append(QtCore.QPointF(self.square_size / 11, 0))  # Tip
        triangle.append(QtCore.QPointF(0, self.square_size / 5.5))  # Bottom-left
        triangle.append(QtCore.QPointF(self.square_size / 5.5, self.square_size / 5.5))  # Bottom-right

        # Set this newly created polygon as this Item's polygon.
        self.setPolygon(triangle)

        # Set the origin of transformations to the center of the triangle.
        # This makes it easier to rotate this Item.
        self.setTransformOriginPoint(SQUARE_SIZE / 5.5, SQUARE_SIZE / 5.5)

    def updateAll(self):
        '''
        Updates the visual representation to correctly resemble the current
        location, direction and status of the parent item.
        '''
        self.updatePosition()
        self.color_bullet()

    def updatePosition(self):
        '''
        Update the coordinates of this item to match the attached item.

        See: For setting the position of this GraphicsItem, see
        QGraphicsPolygonItem at http://doc.qt.io/qt-5/qgraphicspolygonitem.html
        and its parent class QGraphicsItem at http://doc.qt.io/qt-5/qgraphicsitem.html
        '''
        x = self.item.location.get_x()
        y = self.item.location.get_y()
        self.setPos(x - SQUARE_SIZE/5.5, y - SQUARE_SIZE/5.5)

    def color_bullet(self):
        '''
        Change the color of bullet and make the bullet disappear.
        '''
        if not self.item.is_in_air():
            self.setPen(QtGui.QColor(181, 210, 251))
            self.setBrush(QtGui.QColor(181, 210, 251))
            self.setZValue(-1)


