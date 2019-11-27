from enemy import Enemy
from location import SQUARE_SIZE


class EnemyBrain(Enemy):
    '''
    This class generates the brain (AI) to the enemies. This class is responsible of moving
    the enemy and a enemy brain is equipped
    with an algorithm for determining what a robot should do depending of player's location, possible obstacles ect.
    In other words, a enemy brain is capable of controlling the actions of a teh enemy's body.
    '''
    def __init__(self, enemy_body):
        self.body = enemy_body

    def move_enemy(self):
        pass

    def check_front(self):
        '''
        This method checks if the enemy can move forward.

        Returns boolean value stating whether the player can move (return True) or not (returns False)
        '''
        if not self.body.is_destroyed():
            cur_position = self.body.get_location()   # cur_position is the current position of the enemy's center point
            facing = self.body.get_facing()             # facing of the enemy body (RIGHT or LEFT)
            dist = self.body.STEP + SQUARE_SIZE/2
            relative = cur_position.get_relative(facing, dist)
            if not relative.location_is_empty_enemy():
                return False
            return True
        return False

    def find_player(self):
        pass

    def get_type(self):
        pass
