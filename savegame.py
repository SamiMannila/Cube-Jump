import datetime
from location import Location, SQUARE_SIZE, RIGHT


def save_game(game, filename):
    '''
    This method saves the information stored in parameter game.

    Parameter game is the Game class instance to be saved: Game()
    Parameter filename is a string stating the name of the file: string

    Returns a True if saving game was successful, otherwise False: boolean
    '''
    try:
        file = open(filename, "w")
    except IOError:
        return False

    file.write("Tasohyppelypeli tallennustiedosto\n\n")
    file.write("#Game information\n")
    file.write("Saved: {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
    file.write("Created by Sami Mannila.\n")
    file.write("Copyright © 2019 Sami Mannila. All rights reserved.\n\n")

    # Saving the player information
    file.write("#Player\n\n")
    player = game.get_player()
    if player is not None:
        player_name = player.get_name()
        player_x = player.get_location().get_x()
        player_y = player.get_location().get_y()
        player_facing = player.get_facing()
        file.write("Player_name: {}\n".format(player_name))
        file.write("Player_X: {}\n".format(player_x))
        file.write("Player_Y: {}\n".format(player_y))
        file.write("Player_Facing: {}\n\n".format(player_facing))

    else:   # Here we set the default values of player
        player_name = "Incognito"
        player_x = SQUARE_SIZE
        player_y = SQUARE_SIZE
        player_facing = RIGHT
        file.write("Player_name: {}\n".format(player_name))
        file.write("Player_X: {}\n".format(player_x))
        file.write("Player_Y: {}\n".format(player_y))
        file.write("Player_Facing: {}\n\n".format(player_facing))

    # Saving the information of enemies
    list_of_enemies = game.get_enemies()
    for enemy in list_of_enemies:
        file.write("#Enemies\n\n")
        enemy_name = enemy.get_name()
        enemy_x = enemy.get_location().get_x()
        enemy_y = enemy.get_location().get_y()
        enemy_facing = enemy.get_facing()
        file.write("Enemy_name: {}\n".format(enemy_name))
        file.write("Enemy_X: {}\n".format(enemy_x))
        file.write("Enemy_Y: {}\n".format(enemy_y))
        file.write("Enemy_Facing: {}\n\n".format(enemy_facing))

    # Saving the information of the squares
    x = 0
    y = 0
    for i in range(game.get_width()):
        for j in range(game.get_height()):
            if game.get_square(Location(x, y, game)).is_element_square():  # ground
                file.write("#Squares\n\n")
                file.write("Square_Type: Element\n")
                file.write("Square_X: {}\n".format(x))
                file.write("Square_Y: {}\n\n".format(y))
            elif game.get_square(Location(x, y, game)).is_armament_square():  # weapon box
                file.write("#Squares\n\n")
                file.write("Square_Type: Armament\n")
                file.write("Square_X: {}\n".format(x))
                file.write("Square_Y: {}\n\n".format(y))

            y += SQUARE_SIZE
        x += SQUARE_SIZE
        y = 0

    file.write("#END")
    file.close()
    return True


