from location import RIGHT, LEFT, UP, DOWN, Location
from game import SQUARE_SIZE


class Player():
    '''
    This class represents the character which reacts to user inputs in two dimensional grid worlds.

    A player is equipped with the various capabilities:

    - It can sense its own surroundings (location, facing, the world that it is in).

    - It can move forward.

    - It can turn around.

    - It can sense whether it is alive or not.

    - It can have weapon in its repository

    - It can collect points
    '''

    STEP = SQUARE_SIZE/5
    GRAVITATION = 0.1

    def __init__(self, name):
        '''
        Creates a new player with the given name.

        Parameter name is the name of the bot: string
        '''
        self.set_name(name)             # most-recent holder
        self.shape = None               # fixed value
        self.location = None            # most-recent holder
        self.game = None                # fixed value
        self.destroyed = False          # flag
        self.facing = None              # most-recent holder
        self.weapon = None              # most-recent holder
        self.points = 0                 # most-recent holder
        self.falling = None             # flag
        self.jump_speed = 0             # most-recent holder

    def set_name(self, name):
        '''
        Sets the name of the enemy.
        Default name is "Samsonator" but user can also set custom name.

        Parameter name is the new name of the enemy: string
        '''
        if not name:
            self.name = "Samsonator"  # most-recent holder
        else:
            self.name = name

    def get_name(self):
        '''
        Returns the name of the player
        '''
        return self.name

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

    def set_game(self, game, location, facing):
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
            self.facing = facing
            return True

    def get_game(self):
        '''
        Returns the game in which the player is in: Game
        '''
        return self.game

    def set_facing(self, facing):
        '''
        Sets the facing as the parameter orders
        '''
        self.facing = facing

    def get_facing(self):
        '''
        Returns the direction the robot is facing: int
        '''
        return self.facing

    def set_weapon(self, weapon):
        '''
        Sets a weapon to player.

        Parameter weapon is boolean.
        '''
        self.weapon = weapon

    def get_weapon(self):
        '''
        Returns boolean value stating whether player has weapon or not.
        '''
        return self.weapon

    def shoot(self):
        '''
        Uses the weapon of the player and shoots with it. For example the rifle speed and impact force
        can be customised. Player will shoot when mouse is clicked somewhere on the screen
        and in to the direction of mouse click.
        '''
        pass

    def set_points(self, amount):
        '''
        Sets the given amount of points to player.

        Parameter amount is the number of points that will be added to player: int
        '''
        self.points += amount

    def get_points(self):
        '''
        Returns the number of points of the player: int
        '''
        return self.points

    def is_destroyed(self):
        '''
        Returns boolean value stating whether the player is destroyed or not
        '''
        return self.destroyed

    def turn(self):
        '''
        Turns the player around, if the
        player is alive. If the enemy is destroyed, the method does nothing.

        We use global variables RIGHT and LEFT which are defined in Location. This method checks for the current
        facing and turns the enemy to the opposite direction.
        '''
        if not self.is_destroyed():
            if self.facing == RIGHT:
                self.facing = LEFT
            else:
                self.facing = RIGHT

    def turn_to(self, facing):
        '''
        Turns player to wanted direction, if the
        player is alive. If the enemy is destroyed, the method does nothing.
        '''
        if not self.facing == facing:
            self.turn()

    def move(self, facing):
        '''
        Moves the player 5 pixels to the current facing.
        A destroyed player can't move. enemy, player or
        game's playground elements can't overlap. Player doesn't have to move a square by square as they
        can move smoothly pixelwise. Although, player has the shape of a square (at least when we consider
        the collisions) and the coordinates of the player as measured from the center of the enemy's "shell".
        So we determine weather the player collides with some element if the colliding element comes closer than
        half square size to the player. If player collides with a wall it turns to another direction.
        When player and enemy collide player dies.

        Parameter facing is the current facing of the player: Facing (RIGHT/LEFT)
        Parameter square_size is the size of the squares at the

        Returns a boolean value: TRUE if the movement succeeded and FALSE otherwise
        '''
        if not self.is_destroyed():
            if self.check_front():
                cur_x = self.get_location().get_x()
                cur_y = self.get_location().get_y()
                if facing == RIGHT:
                    coordinates = Location(cur_x + Player.STEP, cur_y, self.game)
                    self.set_location(coordinates)
                else:
                    coordinates = Location(cur_x - Player.STEP, cur_y, self.game)
                    self.set_location(coordinates)
                return True
            else:
                return False

    def check_front(self):
        '''
        This method checks if the item can move forward.

        Returns boolean value stating whether the player can move (return True) or not (returns False)
        '''
        cur_position = self.get_location()     # cur_position is the current position of the enemy's center point
        facing = self.get_facing()             # facing of the player (RIGHT or LEFT)
        dist = self.STEP + SQUARE_SIZE/2
        relative = cur_position.get_relative(facing, dist)
        if not relative.location_is_empty_player():
            return False
        return True

    def jump(self, jump_speed):
        '''
        Makes the player jump.
        '''
        self.jump_speed = jump_speed
        if not self.is_destroyed():
            if self.check_up_or_down(UP, Player.STEP*self.jump_speed):
                new_y = self.get_location().get_y() - Player.STEP*self.jump_speed
                coordinates = Location(self.get_location().get_x(), new_y, self.game)
                self.set_location(coordinates)
            else:
                self.jump_speed = 0

    def destroy(self):
        '''
        Destroys the player
        '''
        self.destroyed = True

    def check_up_or_down(self, facing, jump_distance):
        '''
        Returns boolean value stating whether player can move down or up: boolean
        Player can move (return True) and not (return False)
        '''
        cur_position = self.get_location()          # cur_position is the current position of the enemy's center point
        dist = jump_distance + SQUARE_SIZE/2
        relative = cur_position.get_relative(facing, dist)
        if not relative.location_is_empty_player():
            return False
        return True

    def is_falling(self):
        '''
        This method is created to make the code easier to understand at GUI. Changes the value of self.falling.

        Returns boolean value stating whether the player is falling or not: boolean
        '''
        if self.check_up_or_down(DOWN, Player.STEP):
            self.falling = True
        else:
            self.falling = False
        return self.falling

