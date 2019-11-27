from game import Game
from player import Player
from location import Location
from enemy import Enemy
from attackingenemy import AttackingEnemy
from turningenemy import TurningEnemy
from dumbenemy import DumbEnemy


def load_game(filename):
    '''
    This method loads the information stored in given file and creates a Game instance based on that information.

    Parameter filename is a string stating the name of the file: string

    Returns game that the method created or if this methods fails to work returns None: Game()
    Returns an error message if the game wasn't loaded successfully: string
    '''
    # Open the given file and check if opening is successful.
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        message = "Given file was not found!\n"
        return None, message

    # Here we create the game instance that will be returned
    game = Game()

    # Start reading the file
    # First the game information
    current_line = file.readline()
    header_parts = current_line.split(" ")

    # Check if the file type is correct for our game.
    if header_parts[0] != "Tasohyppelypeli":
        message = "Unknown file type\n"
        return None, message

    if header_parts[1].strip().lower() != "tallennustiedosto":
        message = "Unknown file type\n"
        return None, message

    # Reading the information about player, enemies and squares
    current_line = file.readline()
    while current_line != '':
        # First we have to process the text to find correct values.
        current_line = current_line.strip(" ").lower()
        header_parts = current_line.split(":")
        header_parts[0] = header_parts[0].strip()
        # Here we read the blocks that contain specific information.
        if header_parts[0] == "#player" and game.get_player() is None:
            game = read_player_data(game, file)
            if game is None:
                return None, "Something went wrong while loading the player. Try again!\n"
        elif header_parts[0] == "#enemies":
            game = read_enemy_data(game, file)
            if game is None:
                return None, "Something went wrong while loading enemies. Try again!\n"
        elif header_parts[0] == "#squares":
            game = read_square_data(game, file)
            if game is None:
                return None, "Something went wrong while loading squares. Try again!\n"


        current_line = file.readline()



    message = ""
    return game, message


def read_player_data(game, file):
    '''
    This method is responsible of reading the player data from the file.
    This method reads lines until next # mark is found and returns the updated game instance.
    Method also returns cursor to the next # mark that the method encounters.

    Parameter game is a Game instance: Game()
    Parameter file is the file that the method reads: text file

    Returns a updated Game instance: Game()
    '''
    # Init player information to test if the player creation was successful
    player = None
    player_x = None
    player_y = None
    player_facing = None
    # we record the cursor position to return the cursor to the next # mark.
    last_pos = file.tell()
    current_line = file.readline()
    player_initialized = False
    while current_line != '' and current_line[0] != '#':
        # First we have to process the text to find correct values.
        current_line = current_line.strip(" ")
        header_parts = current_line.split(":")
        header_parts[0] = header_parts[0].strip()
        # Init the player and start setting the values of player
        if header_parts[0] == "Player_name":
            header_parts[1] = header_parts[1].strip()
            # Init the player with the given name
            player = Player(header_parts[1])
            player_initialized = True

        elif header_parts[0] == "Player_X" and player_initialized:
            header_parts[1] = header_parts[1].strip()
            # read the X coordinate of the player
            player_x = float(header_parts[1])

        elif header_parts[0] == "Player_Y" and player_initialized:
            header_parts[1] = header_parts[1].strip()
            # read the Y coordinate of the player
            player_y = float(header_parts[1])

        elif header_parts[0] == "Player_Facing" and player_initialized:
            header_parts[1] = header_parts[1].strip()
            # read the Y coordinate of the player
            player_facing = int(header_parts[1])

        last_pos = file.tell()
        current_line = file.readline()
    file.seek(last_pos)

    # Combine player_x and player_y to get the location of player
    # Check if the player was correctly initialized
    if player is not None and player_facing is not None and player_x is not None and player_y is not None:
        player_location = Location(player_x, player_y, game)
        game.add_player(player, player_location, player_facing)
    else:
        return None
    return game


def read_enemy_data(game, file):
    '''
    This method is responsible of reading the enemy data from the file.
    This method reads lines until next # mark is found and returns the updated game instance.
    Method also returns cursor to the next # mark that the method encounters.

    Parameter game is a Game instance: Game()
    Parameter file is the file that the method reads: text file

    Returns a updated Game instance: Game()
    '''
    # Init enemy information to test if the enemy creation was successful
    enemy = None
    enemy_x = None
    enemy_y = None
    enemy_facing = None
    # we record the cursor position to return the cursor to the next # mark.
    last_pos = file.tell()
    current_line = file.readline()
    enemy_initialized = False
    while current_line != '' and current_line[0] != '#':
        # First we have to process the text to find correct values.
        current_line = current_line.strip(" ")
        header_parts = current_line.split(":")
        header_parts[0] = header_parts[0].strip()
        # Init the enemy and start setting the values of enemy
        if header_parts[0] == "Enemy_name":
            header_parts[1] = header_parts[1].strip()
            # Init the enemy with the given name and based on the name set a brain
            enemy = Enemy(header_parts[1])
            if enemy.get_name() == "Attacker":
                attacking_brain = AttackingEnemy(enemy)
                enemy.set_brain(attacking_brain)
            elif enemy.get_name() == "Turner":
                turning_brain = TurningEnemy(enemy)
                enemy.set_brain(turning_brain)
            elif enemy.get_name() == "Dumb":
                dumb_brain = DumbEnemy(enemy)
                enemy.set_brain(dumb_brain)
            else:
                return None
            enemy_initialized = True

        elif header_parts[0] == "Enemy_X" and enemy_initialized:
            header_parts[1] = header_parts[1].strip()
            # read the X coordinate of the enemy
            enemy_x = float(header_parts[1])

        elif header_parts[0] == "Enemy_Y" and enemy_initialized:
            header_parts[1] = header_parts[1].strip()
            # read the Y coordinate of the enemy
            enemy_y = float(header_parts[1])

        elif header_parts[0] == "Enemy_Facing" and enemy_initialized:
            header_parts[1] = header_parts[1].strip()
            # read the Y coordinate of the enemy
            enemy_facing = int(header_parts[1])

        last_pos = file.tell()
        current_line = file.readline()
    file.seek(last_pos)

    # Combine enemy_x and enemy_y to get the location of enemy
    # Check if the enemy was correctly initialized
    if enemy is not None and enemy_facing is not None and enemy_x is not None and enemy_y is not None:
        enemy_location = Location(enemy_x, enemy_y, game)
        game.add_enemy(enemy, enemy_location, enemy_facing)
    else:
        return None
    return game


def read_square_data(game, file):
    '''
    This method is responsible of reading the square data from the file.
    This method reads lines until next # mark is found and returns the updated game instance.
    Method also returns cursor to the next # mark that the method encounters.

    Parameter game is a Game instance: Game()
    Parameter file is the file that the method reads: text file

    Returns a updated Game instance: Game()
    '''
    # Init square information to test if the square creation was successful
    square_type = None
    square_x = None
    square_y = None
    # we record the cursor position to return the cursor to the next # mark.
    last_pos = file.tell()
    current_line = file.readline()
    square_initialized = False
    while current_line != '' and current_line[0] != '#':
        # First we have to process the text to find correct values.
        current_line = current_line.strip(" ")
        header_parts = current_line.split(":")
        header_parts[0] = header_parts[0].strip()
        # Init the square and start setting the values of square
        if header_parts[0] == "Square_Type":
            header_parts[1] = header_parts[1].strip()
            # Save the square type as we will use it later
            if header_parts[1] == "Element":
                square_type = "Element"
            elif header_parts[1] == "Armament":
                square_type = "Armament"
            else:
                return None
            square_initialized = True

        elif header_parts[0] == "Square_X" and square_initialized:
            header_parts[1] = header_parts[1].strip()
            # read the X coordinate of the square
            square_x = float(header_parts[1])

        elif header_parts[0] == "Square_Y" and square_initialized:
            header_parts[1] = header_parts[1].strip()
            # read the Y coordinate of the square
            square_y = float(header_parts[1])

        last_pos = file.tell()
        current_line = file.readline()
    file.seek(last_pos)

    # Combine square_x and square_y to get the location of square
    # Check if the square was correctly initialized
    if square_type is not None and square_x is not None and square_y is not None:
        square_location = Location(square_x, square_y, game)
        if square_type == "Element":
            game.add_element(square_location)
        elif square_type == "Armament":
            game.add_armament(square_location)
    else:
        return None

    return game



