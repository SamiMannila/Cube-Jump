from location import LEFT, RIGHT, Location
from game import SQUARE_SIZE


class Enemy():
    '''
    This class represents enemies which inhabit two dimensional grid worlds.
     To be more precise each instance represents a enemy body and basic functionality of such enemy.
     Each enemy is assosiated with a "enemybrain" that controls the body of the enemy and determines
     what functionality is activated and when

     A enemy is equipped with the various capabilities:

     - It can sense its own surroundings (location, facing, the world that it is in).

     - It can move forward.

     - It can turn around.

     - It can sense whether it is alive or not.
     '''

    STEP = SQUARE_SIZE/22

    def __init__(self, name):

        '''
        Creates a new enemy with the given name. The newly
        created enemy is initially just a "block" until
        it's given a enemy brain later using the method
        set_brain().

        Parameter name is the name of the bot: string

        See set_brain(EnemyBrain)
        See set_name(name)
        '''

        self.set_name(name)
        self.shape = None           # fixed value
        self.location = None        # most-recent holder
        self.game = None            # fixed value
        self.destroyed = False      # flag
        self.brain = None           # most-recent holder
        self.facing = None          # most-recent holder

    def set_name(self, name):
        '''
        Sets the name of the enemy.
        Default name is "Incognito" but user can also set custom name.

        Parameter name is the new name of the enemy: string
        '''
        if not name:
            self.name = "Incognito"   # most-recent holder
        else:
            self.name = name

    def get_name(self):
        '''
        Returns the name of the enemy:string
        '''
        return self.name

    def set_brain(self, new_brain):
        '''
        Sets a "brain" for the enemy.
        This will aslo replace the current brain of the enemy, but this is not where we are hoping to use
        this function.

        Parameter new_brain is the artificial intelligence that controls the enemy:
        EnemyBrainType1/EnemyBrainType2/EnemyBrainType3/... object
        '''

        self.brain = new_brain

    def get_brain(self):
        '''
        Returns the enemy's brain: EnemyBrainType1/EnemyBrainType2/EnemyBrainType3/... object
        '''
        return self.brain

    def set_location(self, location):
        '''
        Sets the enemy to certain location

        Parameter location is instance of class Location: Location
        '''
        self.location = location

    def get_location(self):
        '''
        Returns the current location of the enemy, and if the enemy is not set to game returns None: Location
        (as the location isn't set)
        '''
        return self.location

    def get_location_square(self):
        '''
        Returns the square that the enemy is in: Square
        '''
        return self.get_game().get_square(self.get_location())

    def set_game(self, game, location, facing):
        '''
        Places the enemy in the given game at the specified
        coordinates at the Game. This method is supposed to be used from the
        add_enemy method in the Game class.
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
        Returns the game in which the enemy is in: Game
        '''
        return self.game

    def set_facing(self, facing):
        '''
        Sets the facing as the parameter order it to
        '''
        self.facing = facing

    def get_facing(self):
        '''
        Returns the direction the robot is facing: int
        '''
        return self.facing

    def is_destroyed(self):
        '''
        Returns boolean value stating whether the enemy is destroyed or not
        '''
        return self.destroyed

    def turn(self):
        '''
        Turns the enemy around, if the
        enemy is alive. If the enemy is destroyed, the method does nothing.

        We use global variables RIGHT and LEFT which are defined in Location. This method checks for the current
        facing and turns the enemy to the opposite direction.
        '''
        if not self.is_destroyed():
            if self.facing == RIGHT:
                self.facing = LEFT
            else:
                self.facing = RIGHT

    def move(self, facing):
        '''
        Moves the enemy one step to the direction of facing.
        A destroyed enemy can't move. Two enemies, player or
        game's playground elements can't overlap. Enemies doesn't have to move a square by square as they
        can move smoothly pixelwise. Although, every enemy has the shape of a square (at least when we consider
        the collisions) and the coordinates of the enemy as measured from the center of the enemy's "shell".
        So we determine weather the enemy collides with some element if the colliding element comes closer than
        half square size to the enemy. If enemy collides with a wall or with another enemy
        it turns to another direction. If the enemy collides with the player enemy stops for two (2) seconds
        and then continues it's original movement. When player and enemy collide player dies.

        Parameter facing is the wanted facing of the enemy: Facing (RIGHT/LEFT)
        Parameter square_size is the size of the squares at the

        Returns a boolean value: TRUE if the movement succeeded and FALSE otherwise
        '''
        cur_x = self.get_location().get_x()
        cur_y = self.get_location().get_y()
        if not self.destroyed:
            if facing == RIGHT:
                coordinates = Location(cur_x + Enemy.STEP, cur_y, self.game)
                self.set_location(coordinates)
            else:
                coordinates = Location(cur_x - Enemy.STEP, cur_y, self.game)
                self.set_location(coordinates)
            return True

    def destroy(self):
        '''
        Destroys the enemy, making it unoperational
        '''
        self.destroyed = True


