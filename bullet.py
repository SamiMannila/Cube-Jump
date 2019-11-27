from location import Location
import random


class Bullet():
    '''
    Represents the armament that player can have in it's repository and can use to destroy enemies.
    '''

    FRAME_STEP = 11

    def __init__(self):
        '''
        Creates a new weapon

        Parameter game is the world where the player is
        Parameter player_facing is the facing of the player
        '''
        self.hit_points = None       # fixed value
        self.shot_count = None       # fixed value
        self.game = None             # fixed value
        self.location = None         # most-recent holder
        self.target_x = None         # most-recent holder
        self.target_y = None         # most-recent holder
        self.in_air = True           # most-recent holder
        self.slope_value = 0         # most-recent holder
        self.fly_counter = 0         # most-recent holder
        self.set_weapon_details()

    def set_location(self, location):
        '''
        Sets the player to certain location

        Parameter location is instance of class Location: Location
        '''
        self.location = location

    def get_location(self):
        '''
        Returns the current location of the player, and if the player is not set to game returns None: Location
        (as the location isn't set)
        '''
        return self.location

    def set_game(self, game, location):
        '''
        Places the player in the given game at the specified
        coordinates at the Game. This method is supposed to be used from the
        add_player method in the Game class.
        This makes sure that enemy will be part of the correct Game.

        Parameter game is the game_board in which the enemy will be placed: Game

        Parameter location is the coordinates at which the enemy is placed at the Game: Location

        Returns False if the square at the given location is not empty or
        the robot is already located in some world (the given one or some other world), True otherwise: boolean
        '''

        result_square = game.get_square(location)
        if not result_square.is_empty() or self.get_game() is not None:
            return False
        else:
            self.game = game
            self.location = location
            return True

    def get_game(self):
        '''
        Returns the game in which the player is in: Game
        '''
        return self.game

    def set_weapon_details(self):
        '''
        Gives a random value to weapons hit points between 10 - 100 and random amount of shots between 5 - 30
        '''
        self.hit_points = random.randint(10, 100 + 1)
        self.shot_count = random.randint(5, 30 + 1)

    def set_target(self, target_x, target_y):
        '''
        Sets a target location to the bullet to move towards.

        Parameter target_x is the X coordinate that the player clicked: int
        Parameter target_y is the Y coordinate that the player clicked: int
        '''
        self.target_x = target_x
        self.target_y = target_y

    def fly(self):
        '''
        Makes the bullet fly closer to the set target
        '''
        if self.in_air:
            cur_x = self.get_location().get_x()
            cur_y = self.get_location().get_y()
            if self.fly_counter == 0:
                self.slope_value = self.count_slope()
            coordinates = Location(cur_x + self.FRAME_STEP, self.slope_value*self.FRAME_STEP + cur_y, self.game)
            if self.check_next_location(coordinates):
                self.set_location(coordinates)
                self.fly_counter += 1
        if self.fly_counter > 300:
            self.in_air = False

    def check_next_location(self, next_location):
        '''
        This method checks if the item can move forward.

        Returns boolean value stating whether the player can move (return True) or not (returns False)
        '''
        if not next_location.location_is_empty_bullet():
            self.in_air = False
            return False
        return True

    def count_slope(self):
        '''
        Counts the slope between bullet's current position and the target position

        Returns the value of the slope (kulmakerroin): float
        '''
        slope = 0
        if not self.target_x - self.get_location().get_x() == 0:
            slope = (self.target_y - self.get_location().get_y())/(self.target_x - self.get_location().get_x())
        return slope

    def is_in_air(self):
        '''
        Returns a boolean value stating whether the bullet is in the air
        '''
        return self.in_air

