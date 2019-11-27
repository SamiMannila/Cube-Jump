from enemybrain import EnemyBrain


class TurningEnemy(EnemyBrain):
    '''
    This class is responsible of creating enemy brain to the Turning type enemy.
    Turning enemy is only aware of its own location and doesn't care about the player.
    Turning enemy moves forward 220 times after it turns and moves 220 times forward again
    until it faces an obstacle, collides with player
    or drops out of the game board to some gap. If TurningEnemy collides with obstacle or player it turns around.
    '''
    TURN_COUNTER = 0

    def move_enemy(self):
        '''
        Moves enemy body
        '''
        TurningEnemy.TURN_COUNTER += 1
        if self.check_front() and TurningEnemy.TURN_COUNTER <= 220:
            self.body.move(self.body.get_facing())
        else:
            self.body.turn()
            self.body.move(self.body.get_facing())
            TurningEnemy.TURN_COUNTER = 0

    def get_type(self):
        '''
        Returns string stating the type of the enemy.
        '''
        return "Turning"
