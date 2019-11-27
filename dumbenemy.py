from enemybrain import EnemyBrain


class DumbEnemy(EnemyBrain):
    '''
    This class is responsible of creating enemy brain to the Dumb type enemy.
    Dumb enemy is only aware of its own location and doesn't care about the player.
    Dumb enemy only moves forward until it faces an obstacle, collides with player
    or drops out of the game board to some gap. If DumbEnemy collides with obstacle or player it turns around.
    '''

    def move_enemy(self):
        '''
        Moves enemy body
        '''
        if self.check_front():
            self.body.move(self.body.get_facing())
            return True
        else:
            self.body.turn()
            self.body.move(self.body.get_facing())
            return False

    def get_type(self):
        '''
        Returns string stating the type of the enemy.
        '''
        return "Dumb"

