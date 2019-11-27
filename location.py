from game import SQUARE_SIZE
import math

LEFT = -1
RIGHT = 1
UP = 2
DOWN = -2


class Location():
    '''
    The class represents pairs of
    integers that specify locations on a two-dimensional grid.
    As is common in programming environments, the x values
    increase towards the right (east) and the y values
    increase downwards (south). A coordinate object is immutable
    after creation.
    '''

    def __init__(self, x, y, world):
        '''
        Creates new coordinate pair.

        Parameter x is x coordinate: int
        Parameter y is y coordinate: int
        '''
        self.x = x          # fixed value
        self.y = y          # fixed value
        self.game = world   # Game()

    def get_x(self):
        '''
        Returns the x coordinate (int)
        '''
        return self.x

    def get_y(self):
        '''
        Returns the y coordinate (int)
        '''
        return self.y

    def change_location(self, change_in_x, change_in_y):
        '''
        Changes the value of X and Y coordinates

        Parameters change_in_X and change_in_Y is the amount of the change (either negative or positive):int
        '''
        self.x = self.get_x() + change_in_x
        self.y = self.get_y() + change_in_y

    def get_relative(self, direction, distance):
        '''
        Returns the coordinates that are a distance away to these ones, in the given direction.

        Parameter direction: tuple
        Prameter distance: int

        Returns the neighboring coordinates (Coordinates)
        '''
        if direction == RIGHT:
            return Location(self.get_x() + distance, self.get_y(), self.game)
        elif direction == LEFT:
            return Location(self.get_x() - distance, self.get_y(), self.game)
        elif direction == UP:
            return Location(self.get_x(), self.get_y() - distance, self.game)
        elif direction == DOWN:
            return Location(self.get_x(), self.get_y() + distance, self.game)

    @staticmethod
    def get_directions():
        '''
        Returns a list of all possible directions: LEFT, RIGHT, UP, DOWN
        '''
        return [LEFT, RIGHT, UP, DOWN]

    def location_is_empty_player(self):
        '''
        Checks if the coordinate is empty.

        Returns boolean value stating whether the location contains a character.
        If there is character returns True, False otherwise: boolean
        '''
        square = self.game.get_square(self)
        if square.is_element_square():
            return False
        if square.is_armament_square():         # if player hits armament square player is awarded with weapon
            player = self.game.get_player()
            if not player.get_weapon():         # player can only collect one weapon from each armament box
                weapon = True
                player.set_weapon(weapon)
                square.is_armament = False
        for enemy in self.game.get_enemies():
            if self.distance(enemy.get_location()) < SQUARE_SIZE/2 and enemy.is_destroyed() is False:
                self.game.get_player().destroy()
                return False
        return True

    def location_is_empty_enemy(self):
        '''
        Checks if the coordinate is empty.

        Returns boolean value stating whether the location contains a character.
        If there is character returns True, False otherwise: boolean
        '''
        square = self.game.get_square(self)
        if square.is_element_square():
            return False
        if self.distance(self.game.get_player().get_location()) < SQUARE_SIZE/2:
            self.game.get_player().destroy()
            return False
        return True

    def location_is_empty_bullet(self):
        '''
        Checks if the coordinate is empty.

        Returns boolean value stating whether the location contains a character.
        If there is character returns True, False otherwise: boolean
        '''
        square = self.game.get_square(self)
        if square.is_element_square():
            return False
        for enemy in self.game.get_enemies():
            if self.distance(enemy.get_location()) < SQUARE_SIZE/2:
                enemy.destroy()
                return False
        return True

    def distance(self, new_location):
        '''
        Counts the distance between to locations

        Parameters location_1 and location_2 are location objects: Location

        Returns the absolute value of the distance
        '''
        x1 = self.get_x()
        y1 = self.get_y()
        x2 = new_location.get_x()
        y2 = new_location.get_y()
        distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        return abs(distance)
