from square import Square

SQUARE_SIZE = 22  # the size of the square in pixels in one direction


class Game():
    '''
    The class Game describes a two dimensional world made up
    of squares that initiate the ground, different levels, possible gaps,
    location of points and armament. It also sets enemies to the game board. The squares are
    identified by unique coordinates which range from 0...width-1 and
    0...height-1. Each square is represented by a Square object.
    '''

    def __init__(self):
        '''
        Creates a basic structure of the world where the game will be played.
        Initially the world is empty but Game reads a file
        which states the location of game board elements, enemies, points and armament.

        The game will be played at full screen mode.
        '''

        width = 120
        height = 30

        self.squares = [None] * width                   # we create basic list to use it as starting ground
        for x in range(self.get_width()):               # stepper
            self.squares[x] = [None] * height
            for y in range(self.get_height()):          # stepper
                self.squares[x][y] = Square()           # fixed value
        self.enemies = []                               # list of enemies in Game
        self.player = None                              # The player object of the game
        self.bullets = []                               # list of the bullets that are currently in the "air"

    def get_width(self):
        '''
        Returns the width of Game as squares: int
        '''
        return len(self.squares)

    def get_height(self):
        '''
        Returns the height of Game as squares: int
        '''
        return len(self.squares[0])

    def add_enemy(self, enemy, location, facing):
        '''
        Adds a new enemy to the basic world structure.
        This method also assures that the enemy is aware of its location.
        The location of enemy is not based on squares as the enemies aren't dependant of the squares.

        Parameter enemy is enemy object that will be added: Enemy
        Parameter location is the coordinates of the enemy: Location
        Parameter facing is the direction of the enemy: int

        Returns False if there is an element/another enemy at the given location or the given enemy is already
        located in some game (this or some other world), True otherwise: boolean
        '''
        enemy.set_location(location)
        enemy.set_facing(facing)
        enemy.set_game(self, location, facing)
        self.enemies.append(enemy)

    def get_enemies(self):
        '''
        Returns a list of enemies in game
        '''
        return self.enemies

    def get_bullets(self):
        '''
        Returns a list of bullets in the air in the game
        '''
        return self.bullets

    def add_player(self, player, location, facing):
        '''
        Adds a new player to the basic world structure.
        This method also assures that the player is aware of its location.
        The location of player is not based on squares as the enemies aren't dependant of the squares.
        The method also assures that only one player can be added to the game.

        Parameter player is Player instance that will be added: Player
        Parameter location is the coordinates of the enemy: Location
        Parameter facing is the direction of the enemy: int
        '''
        self.player = player                  # sets the player to the game
        self.player.set_location(location)    # initiates the location
        self.player.set_facing(facing)        # initiates the facing
        player.set_game(self, location, facing)

    def add_bullet(self, bullet, location):
        '''
        Adds a bullet in front of the player which then will fly towards clicked location.
        '''
        bullet.set_location(location)
        bullet.set_game(self, location)
        self.bullets.append(bullet)

    def get_player(self):
        '''
        Returns a player of the game.
        '''
        return self.player

    def add_element(self, location):
        '''
        Adds a game board element at the given location in the world structure, if
        possible. If the square is not empty, the method fails to
        do anything.

        Parameter location is the location of the element: Location

        Returns a boolean value indicating if the operation succeeded: boolean
        '''
        return self.get_square(location).set_element()

    def add_points(self, location):
        '''
        Adds points to the given location in the world structure, if
        possible. If the square is not empty, the method fails to
        do anything.

        Parameter location is the location of the element: Location

        Returns a boolean value indicating if the operation succeeded: boolean
        '''
        return self.get_square(location).set_points()

    def add_armament(self, location):
        '''
        Adds armament to the given location in the world structure, if
        possible. If the square is not empty, the method fails to
        do anything.

        Parameter location is the location of the element: Location

        Returns a boolean value indicating if the operation succeeded: boolean
        '''
        return self.get_square(location).set_armament()

    def get_square(self, location):
        '''
        Parameter location is a coordinate pair in the Game: Location

        Returns the square that is located at the given location. If the given parameter (location)
        point outside of the game (the world where the game is played or
        outside of the index of squares), this method returns a square that contains a game board element
        and is not located in any game: Square
        '''
        if self.test_location(location):
            return self.squares[int(location.get_x()/SQUARE_SIZE)][int(location.get_y()/SQUARE_SIZE)]
        else:
            return Square(True)

    def test_location(self, location):
        '''
        This method test whether the given location is located inside the Game

        Parameter is the coordinates to be tested: Location

        Returns boolean value, if the location belongs to the Game returns True, otherwise False: boolean
        '''
        x = location.get_x()
        y = location.get_y()
        return 0 <= x < self.get_width()*SQUARE_SIZE and 0 <= y < self.get_height()*SQUARE_SIZE
