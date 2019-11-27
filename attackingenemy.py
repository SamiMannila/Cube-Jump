from enemybrain import EnemyBrain
from location import RIGHT, LEFT
from game import SQUARE_SIZE


class AttackingEnemy(EnemyBrain):
    '''
    This class is responsible of creating enemy brain to the Attacking type enemy.
    Attacking enemy is aware of its own location and checks the location of player before it moves.
    Attacking enemy moves forward until it faces an obstacle or drops out of the game board to some gap.
    If Attacking enemy collides with obstacle it turns around and keeps moving.
    If Attacking enemy "sees" the player, it tries to move towards player with increased speed
    for distance of three squares.
    '''

    SPRINT_COUNTER = 0

    def find_player(self):
        '''
        This method looks for the player in front of the enemy.
        If the player is closer than 5 square sizes (110 steps) of the enemy
        method will return True, otherwise False: boolean

        Note! This method only checks for the player in same plane as the enemy can not jump.
        '''
        facing = self.body.get_facing()             # the facing of the enemy
        player = self.body.get_game().get_player()  # the player in the game
        player_location = player.get_location()     # location of the player
        player_x = player_location.get_x()          # x coordinate
        player_y = player_location.get_y()          # y coordinate
        enemy_location = self.body.get_location()   # location of the enemy
        enemy_x = enemy_location.get_x()            # x coordinate
        enemy_y = enemy_location.get_y()            # y coordinate
        distance = player_location.distance(enemy_location)

        if player_y < enemy_y + SQUARE_SIZE or player_y > enemy_y - SQUARE_SIZE:
            if facing == RIGHT and player_x > enemy_x and distance < self.body.STEP*110:
                return True
            if facing == LEFT and player_x < enemy_x and distance < self.body.STEP*110:
                return True
        return False

    def move_enemy(self):
        '''
        Moves enemy body. If the player comes closer than three square sizes
        the enemy attacks towards the player with doubled speed
        '''
        if self.find_player() and AttackingEnemy.SPRINT_COUNTER <= 110:
            AttackingEnemy.SPRINT_COUNTER += 2
            if self.check_front():
                self.body.move(self.body.get_facing())
                if self.check_front():
                    self.body.move(self.body.get_facing())
            else:
                self.body.turn()
                self.body.move(self.body.get_facing())
        else:
            AttackingEnemy.SPRINT_COUNTER = 0
            if self.check_front():
                self.body.move(self.body.get_facing())
            else:
                self.body.turn()
                self.body.move(self.body.get_facing())

    def get_type(self):
        '''
        Returns string stating the type of the enemy.
        '''
        return "Attacking"

