
import unittest

from game import *
from location import *
from player import *
from enemy import *
from attackingenemy import *
from dumbenemy import *
from turningenemy import *


class Test(unittest.TestCase):
    '''
    Some tests for the Game-project.
    '''
    def setUp(self):
        self.game = Game()
        x = 0
        y = self.game.get_height() * SQUARE_SIZE
        while y >= 25 * SQUARE_SIZE:  # creates the ground for the game (everything is ground
            while x <= 60 * SQUARE_SIZE:  # starting from 25:th square counting from the top
                element_coordinates = Location(x, y, self.game)
                self.game.add_element(element_coordinates)
                x += SQUARE_SIZE
            x = 0
            y = y - SQUARE_SIZE

        y = 20 * SQUARE_SIZE
        x = 20 * SQUARE_SIZE
        while x <= 25 * SQUARE_SIZE:  # creates a plane to game where player can jump on
            element_coordinates = Location(x, y, self.game)
            self.game.add_element(element_coordinates)
            x += SQUARE_SIZE

        y = 15 * SQUARE_SIZE
        x = 30 * SQUARE_SIZE
        while x <= 35 * SQUARE_SIZE:  # creates a plane to game where player can jump on
            element_coordinates = Location(x, y, self.game)
            self.game.add_element(element_coordinates)
            x += SQUARE_SIZE

        # few random stones on the ground
        x = 25 * SQUARE_SIZE
        y = 24 * SQUARE_SIZE
        element_coordinates = Location(x, y, self.game)
        self.game.add_element(element_coordinates)

        x = 56 * SQUARE_SIZE
        y = 24 * SQUARE_SIZE
        element_coordinates = Location(x, y, self.game)
        self.game.add_element(element_coordinates)

        # armament square
        x = 32 * SQUARE_SIZE
        y = 20 * SQUARE_SIZE
        armament_coordinates = Location(x, y, self.game)
        self.game.add_armament(armament_coordinates)

        # armament square
        x = 2 * SQUARE_SIZE
        y = 20 * SQUARE_SIZE
        armament_coordinates = Location(x, y, self.game)
        self.game.add_armament(armament_coordinates)

        y = 25 * SQUARE_SIZE
        x = 70 * SQUARE_SIZE
        element_coordinates = Location(x - 1, y - 1, self.game)
        self.game.add_element(element_coordinates)
        while x <= 75 * SQUARE_SIZE:  # creates a plane to game where player can jump on
            element_coordinates = Location(x, y, self.game)
            self.game.add_element(element_coordinates)
            x += SQUARE_SIZE
        element_coordinates = Location(x, y - 1, self.game)
        self.game.add_element(element_coordinates)

        y = 20 * SQUARE_SIZE
        x = 80 * SQUARE_SIZE
        while x <= 82 * SQUARE_SIZE:  # creates a plane to game where player can jump on
            element_coordinates = Location(x, y, self.game)
            self.game.add_element(element_coordinates)
            x += SQUARE_SIZE

        y = 20 * SQUARE_SIZE
        x = 89 * SQUARE_SIZE
        i = 0
        while i < 5 * SQUARE_SIZE:  # stairs
            element_coordinates = Location(x + i, y + i, self.game)
            self.game.add_element(element_coordinates)
            i += SQUARE_SIZE

        y = 20 * SQUARE_SIZE
        x = 95 * SQUARE_SIZE
        while x <= 100 * SQUARE_SIZE:  # creates a plane to game where player can jump on
            element_coordinates = Location(x, y, self.game)
            self.game.add_element(element_coordinates)
            x += SQUARE_SIZE

        # few random stones on the ground
        x = 95 * SQUARE_SIZE
        y = 15 * SQUARE_SIZE
        element_coordinates = Location(x, y, self.game)
        self.game.add_element(element_coordinates)

        x = 100 * SQUARE_SIZE
        y = 10 * SQUARE_SIZE
        element_coordinates = Location(x, y, self.game)
        self.game.add_element(element_coordinates)

        x = 105 * SQUARE_SIZE
        y = 5 * SQUARE_SIZE
        element_coordinates = Location(x, y, self.game)
        self.game.add_element(element_coordinates)

        y = 10 * SQUARE_SIZE
        x = 110 * SQUARE_SIZE
        while x <= 120 * SQUARE_SIZE:  # creates a plane to game where player can jump on
            element_coordinates = Location(x, y, self.game)
            self.game.add_element(element_coordinates)
            x += SQUARE_SIZE

        player_location = Location(1 * SQUARE_SIZE, SQUARE_SIZE * 24.5, self.game)  # creating the player
        player = Player("Sami")
        self.game.add_player(player, player_location, RIGHT)

        dumb_enemy_location = Location(SQUARE_SIZE * 55, SQUARE_SIZE * 24.5, self.game)  # creating the Dumb enemy
        dumb_body = Enemy("Dumb")
        dumb_brain = DumbEnemy(dumb_body)
        dumb_body.set_brain(dumb_brain)
        self.game.add_enemy(dumb_body, dumb_enemy_location, LEFT)

        dumb_enemy_location = Location(SQUARE_SIZE * 72, SQUARE_SIZE * 24.5, self.game)  # creating the Dumb enemy
        dumb_body = Enemy("Dumb")
        dumb_brain = DumbEnemy(dumb_body)
        dumb_body.set_brain(dumb_brain)
        self.game.add_enemy(dumb_body, dumb_enemy_location, LEFT)

        turning_enemy_location = Location(SQUARE_SIZE * 50, SQUARE_SIZE * 24.5, self.game)  # creating the Turning enemy
        turning_body = Enemy("Turner")
        turning_brain = TurningEnemy(turning_body)
        turning_body.set_brain(turning_brain)
        self.game.add_enemy(turning_body, turning_enemy_location, LEFT)

        attacking_enemy_location = Location(SQUARE_SIZE * 45, SQUARE_SIZE * 24.5,
                                            self.game)  # creating the Turning enemy
        attacking_body = Enemy("Attacker")
        attacking_brain = AttackingEnemy(attacking_body)
        attacking_body.set_brain(attacking_brain)
        self.game.add_enemy(attacking_body, attacking_enemy_location, LEFT)

    def test_add_element(self):
        '''
        Test if adding a game board element works correctly.
        Tests the game board dimensions and two element squares.
        '''
        self.assertEqual(self.game.get_width(), 120, "Game dimensions are wrong (width)!")
        self.assertEqual(self.game.get_height(), 30, "Game dimensions are wrong (height)!")
        test_coordinate = Location(20*SQUARE_SIZE, 35*SQUARE_SIZE, self.game)
        self.assertEqual(True, self.game.get_square(test_coordinate).is_element_square(), "Square status is incorrect.")
        test_coordinate_2 = Location(25*SQUARE_SIZE, 30*SQUARE_SIZE, self.game)
        self.assertEqual(True, self.game.get_square(test_coordinate_2).is_element_square(), "Square status is incorrect.")

    def test_add_player(self):
        '''
        Test if adding player works correctly.
        Tests the player name, facing and location.
        '''
        self.assertEqual("Sami", self.game.get_player().get_name(), "Wrong player name!")
        self.assertEqual(RIGHT, self.game.get_player().get_facing(), "Incorrect facing of the player!")
        self.assertEqual(SQUARE_SIZE, self.game.get_player().get_location().get_x(), "Wrong X coordinate!")
        self.assertEqual(SQUARE_SIZE*24.5, self.game.get_player().get_location().get_y(), "Wrong Y coordinate!")

    def test_add_enemy(self):
        '''
        Test if adding enemy works correctly.
        Tests the enemy name, facing and location.
        '''
        self.assertEqual("Dumb", self.game.get_enemies()[0].get_name(), "Incorrect enemy name")
        self.assertEqual(LEFT, self.game.get_enemies()[0].get_facing(), "Incorrect facing of the enemy")
        self.assertEqual(SQUARE_SIZE * 55, self.game.get_enemies()[0].get_location().get_x(), "Incorrect X coordinate!")
        self.assertEqual(SQUARE_SIZE * 24.5, self.game.get_enemies()[0].get_location().get_y(), "Incorrect Y coordinate!")

    def test_enemy_step(self):
        '''
        Tests if enemy can take one step forward.
        Lets test Turning enemy.
        We first test if moving the body will work and then we try using the brain to move the enemy.
        '''
        enemy = self.game.get_enemies()[1]
        enemy.move(enemy.get_facing())
        self.assertEqual(SQUARE_SIZE * 72 - Enemy.STEP, enemy.get_location().get_x(), "Enemy step failed")
        turning_brain = enemy.get_brain()
        turning_brain.move_enemy()
        self.assertEqual(SQUARE_SIZE * 72 - Enemy.STEP*2, enemy.get_location().get_x(), "Enemy step failed")

    def test_turning_enemy_turn(self):
        '''
        Tests if Turning enemy turns after 220 steps.
        '''
        enemy = self.game.get_enemies()[2]
        turning_brain = enemy.get_brain()
        for i in range(221):
            turning_brain.move_enemy()
        self.assertEqual(RIGHT, enemy.get_facing())

    def test_player_move(self):
        '''
        Tests if player can move.
        '''
        player = self.game.get_player()
        player.move(RIGHT)
        self.assertEqual(1*SQUARE_SIZE + Player.STEP, player.get_location().get_x())

    def test_player_collision_detection(self):
        '''
        Tests whether player can realise that it can't move forward because of the obstacle in front of it.
        '''
        element_coordinates = Location(1*SQUARE_SIZE+4, SQUARE_SIZE*24.5, self.game)
        self.game.add_element(element_coordinates)
        self.assertEqual(True, self.game.get_square(element_coordinates).is_element_square(), "Square status is incorrect.")
        player = self.game.get_player()
        self.assertEqual(False, player.move(RIGHT))
        self.assertEqual(False, player.is_destroyed())

    def test_enemy_collision_detection(self):
        '''
        Tests whether enemy can realise that it can't move forward because of the obstacle in front of it.
        '''
        element_coordinates = Location(SQUARE_SIZE * 55 - 4, SQUARE_SIZE * 24.5, self.game)
        self.game.add_element(element_coordinates)
        self.assertEqual(True, self.game.get_square(element_coordinates).is_element_square(), "Square status is incorrect.")
        enemy = self.game.get_enemies()[0]
        dumb_brain = enemy.get_brain()
        self.assertEqual(False, dumb_brain.move_enemy())
        self.assertEqual(RIGHT, enemy.get_facing())

    def test_player_enemy_collision_1(self):
        '''
        Tests if the player enemy collision. Player moving and hitting enemy.
        '''
        dumb_enemy_location = Location(SQUARE_SIZE+5, SQUARE_SIZE * 24.5, self.game)  # creating the Dumb enemy
        dumb_body = Enemy("Dumb_Collision")
        dumb_brain = DumbEnemy(dumb_body)
        dumb_body.set_brain(dumb_brain)
        self.game.add_enemy(dumb_body, dumb_enemy_location, LEFT)
        player = self.game.get_player()
        player.move(RIGHT)
        self.assertEqual(True, player.is_destroyed())

    def test_player_enemy_collision_2(self):
        '''
        Tests if the player enemy collision. Enemy hitting player.
        '''
        dumb_enemy_location = Location(SQUARE_SIZE+4, SQUARE_SIZE * 24.5, self.game)  # creating the Dumb enemy
        dumb_body = Enemy("Dumb_Collision")
        dumb_brain = DumbEnemy(dumb_body)
        dumb_body.set_brain(dumb_brain)
        self.game.add_enemy(dumb_body, dumb_enemy_location, LEFT)
        dumb_brain.move_enemy()
        self.assertEqual(True, self.game.get_player().is_destroyed())

    def test_attacking_enemy_1(self):
        '''
        Test if Attacking enemy brain work correctly when no player around.
        '''
        enemy = self.game.get_enemies()[3]
        attacking_brain = enemy.get_brain()
        self.assertEqual(False, attacking_brain.find_player())

    def test_attacking_enemy_2(self):
        '''
        Test if Attacking enemy brain work correctly when enemy should find player.
        '''
        attacking_enemy_location = Location(SQUARE_SIZE * 2, SQUARE_SIZE * 24.5, self.game)  # creating the Turning enemy
        attacking_body = Enemy("Attacker")
        attacking_brain = AttackingEnemy(attacking_body)
        attacking_body.set_brain(attacking_brain)
        self.game.add_enemy(attacking_body, attacking_enemy_location, LEFT)
        self.assertEqual(True, attacking_brain.find_player())

    def test_attacking_enemy_3(self):
        '''
        Tests if Attacking enemy brain moves the body correctly when enemy finds player.
        '''
        attacking_enemy_location = Location(SQUARE_SIZE * 3, SQUARE_SIZE * 24.5, self.game)  # creating the Turning enemy
        attacking_body = Enemy("Attacker")
        attacking_brain = AttackingEnemy(attacking_body)
        attacking_body.set_brain(attacking_brain)
        self.game.add_enemy(attacking_body, attacking_enemy_location, LEFT)
        attacking_brain.move_enemy()
        self.assertEqual(SQUARE_SIZE * 3 - 2*attacking_body.STEP, attacking_body.get_location().get_x())
        counter = 0
        while not self.game.get_player().is_destroyed():
            attacking_brain.move_enemy()
            counter += 1                                # the enemy should move 11 times before it hits the player
        self.assertEqual(11, counter)                    # remember the shape of the enemy and player
        self.assertEqual(RIGHT, attacking_body.get_facing())


if __name__ == "__main__":
    unittest.main()