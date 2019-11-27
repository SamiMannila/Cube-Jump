from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QGraphicsRectItem, QMessageBox

from playergraphicsitem import PlayerGraphicsItem
from enemygraphicsitem import EnemyGraphicsItem
from location import LEFT
from bullet import Bullet
from bulletgraphicsitem import BulletGraphicsItem
from savegame import *
from loadgame import *


class StartingWindow(QtWidgets.QMainWindow):
    '''
    This class creates a starting screen for user.
    '''
    def __init__(self):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget())  # QMainWindow must have a centralWidget to be able to add layouts
        self.horizontal = QtWidgets.QHBoxLayout()   # Horizontal main layout
        self.centralWidget().setLayout(self.horizontal)
        self.message = ""                           # most-recent holder

        self.init_window()

    def init_window(self):
        '''
        Sets up the window.
        '''
        self.button1 = QtWidgets.QPushButton("Start level 1", self)
        self.button3 = QtWidgets.QPushButton("Create level", self)
        self.button2 = QtWidgets.QPushButton("Load level", self)
        self.button4 = QtWidgets.QPushButton("Quit", self)
        self.button1.move(153, 165)
        self.button2.move(153, 190)
        self.button3.move(247, 165)
        self.button4.move(247, 190)
        self.button1.clicked.connect(self.init_level_1)
        self.button3.clicked.connect(self.init_editor)
        self.button2.clicked.connect(self.load_button)
        self.button4.clicked.connect(self.quit_button)
        self.setGeometry(400, 250, 500, 300)
        self.setWindowTitle('Tasohyppelypeli')
        self.label = QtWidgets.QLabel("\n\n\n\n\nWelcome to my game!\n\n"\
                                      + "Choose one of the options below\n to get started.")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.horizontal.addWidget(self.label)
        self.show()

    def init_level_1(self):
        '''
        This method is responsible for initializing the level 1 of the game.
        '''
        self.initiate_level_1()
        self.next = GUI(self.game)
        self.close()

    def quit_button(self):
        '''
        This method closes the game when Quit button is pressed.
        '''
        self.close()

    def init_editor(self):
        '''
        This method is responsible for initializing the level editor of the game
        '''
        self.editor = LevelEditor()
        self.close()

    def load_button(self):
        '''
        Thi method asks for the filename to which the game/level will be saved.
        '''
        filename, ok_pressed = QtWidgets.QInputDialog.getText(self, "Load level", self.message\
                                                              + "Enter filename:", QtWidgets.QLineEdit.Normal, "")
        if ok_pressed and filename != '':
            game, self.message = load_game(filename)
            if game is None:
                self.load_button()
            else:
                self.next = GUI(game)
                self.close()
        elif ok_pressed and filename == '':
            self.load_button()

    def initiate_level_1(self):
        '''
        This method initiates the game
        '''
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

        attacking_enemy_location = Location(SQUARE_SIZE * 45, SQUARE_SIZE * 24.5, self.game)  # creating the Turning enemy
        attacking_body = Enemy("Attacker")
        attacking_brain = AttackingEnemy(attacking_body)
        attacking_body.set_brain(attacking_brain)
        self.game.add_enemy(attacking_body, attacking_enemy_location, LEFT)


class GUI(QtWidgets.QMainWindow):
    '''
    The class GUI handles the drawing of a Game and allows user to
    interact with it.
    '''

    KEY_A_STATUS = False
    KEY_D_STATUS = False
    KEY_W_STATUS = False
    JUMP_SPEED = 2.5
    WINDOW_X = 1 * SQUARE_SIZE - 100

    def __init__(self, game):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget())  # QMainWindow must have a centralWidget to be able to add layouts
        self.horizontal = QtWidgets.QHBoxLayout()   # Horizontal main layout
        self.centralWidget().setLayout(self.horizontal)
        self.game = game
        self.square_size = SQUARE_SIZE
        # for testing if the player or enemies already have graphics item.
        self.player_graphics = NotImplemented

        self.added_enemies = []
        self.added_enemy_graphics = []

        self.added_bullets = []
        self.added_bullet_graphics = []

        self.init_window()
        self.add_game_grid()
        self.add_player_graphics_item()
        self.add_enemy_graphics_items()

        # Set a timer to call the update function periodically
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_items)
        self.timer.start(10)  # Milliseconds

    def init_window(self):
        '''
        Sets up the window.
        '''
        self.button_help = QtWidgets.QPushButton("Help", self)
        self.button_back = QtWidgets.QPushButton("Back to Menu", self)
        self.button_help.clicked.connect(self.help_button)
        self.button_back.clicked.connect(self.back_to_start)
        self.button_back.move(10, 20)
        self.button_help.move(10, 42)
        self.button_back.resize(120, 30)
        self.button_help.resize(120, 30)
        self.setGeometry(300, 0, 1300, 700)
        self.setWindowTitle('Tasohyppelypeli')
        self.show()

        # Add a scene for drawing 2d objects
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 1250, 660)
        scroll = QtWidgets.QScrollArea()
        scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # Add a view for showing the scene
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)

    @staticmethod
    def help_button():
        '''
        This method opens message box when user clicks the help button.
        '''
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("How to play the game?")
        msgBox.setInformativeText("Press a some of the commands to move\nand click screen if you want to shoot" \
                                  + " with players weapon. You can collect weapon from the"
                                  + " Armament box (yellow box).\n\n"\
                                  + "You will complete the level when the player character reaches the right end of the"\
                                  + " game area.\n"\
                                  + "\n\nCommands:\nA: Move left\n" \
                                  + "D: Move right\nW: Jump")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        msgBox.exec_()

    def update_window(self):
        '''
        Makes the window follow the player.
        '''
        if GUI.WINDOW_X != self.game.get_player().get_location().get_x() - 100:
            GUI.WINDOW_X += (self.game.get_player().get_location().get_x() - 100 - GUI.WINDOW_X)
        self.scene.setSceneRect(self.game.get_player().get_location().get_x() - 100, 0, 1250, 660)

    def add_game_grid(self):
        '''
        Adds an QGraphicsItem for each square in the game.
        Qt uses QGraphicsItems to draw objects in the QGraphicsScene.
        QGraphicsRectItem is a subclass of QGraphicsItem, and is useful for
        easily drawing rectangular items.
        This method should only be called once, otherwise it creates duplicates!
        '''
        x = 0
        y = 0
        for i in range(self.game.get_width()):
            for j in range(self.game.get_height()):
                new_square = QGraphicsRectItem(x, y, self.square_size, self.square_size)
                self.scene.addItem(new_square)
                if self.game.get_square(Location(x, y, self.game)).is_element_square():     # ground
                    new_square.setBrush(QtGui.QColor(21, 73, 8))
                    new_square.setPen(QtGui.QColor(21, 73, 8))
                elif self.game.get_square(Location(x, y, self.game)).is_armament_square():  # weapon box
                    new_square.setBrush(QtGui.QColor(244, 206, 66))
                    new_square.setPen(QtGui.QColor(244, 206, 66))
                else:
                    new_square.setBrush(QtGui.QColor(181, 210, 251))                        # sky
                    new_square.setPen(QtGui.QColor(181, 210, 251))
                y += self.square_size
            x += self.square_size
            y = 0

    def add_player_graphics_item(self):
        '''
        Adds a PlayerGraphicsItem for the player. If player already has a graphics item this method does nothing.
        '''
        if self.player_graphics == NotImplemented:
            player_graphics = PlayerGraphicsItem(self.game.get_player())
            self.scene.addItem(player_graphics)
            self.player_graphics = player_graphics

    def add_enemy_graphics_items(self):
        '''
        Adds a EnemyGraphicsItem for every enemy. If enemy already has a graphics item this method does nothing.
        '''
        for enemy in self.game.get_enemies():
            if enemy not in self.added_enemies:
                enemy_graphics = EnemyGraphicsItem(enemy)
                self.scene.addItem(enemy_graphics)
                self.added_enemy_graphics.append(enemy_graphics)
            self.added_enemies.append(enemy)

    def add_bullet_graphics_items(self):
        '''
        Adds a BulletGraphicsItem for every bullet. If bullet already has a graphics item this method does nothing
        '''
        for bullet in self.game.get_bullets():
            if bullet not in self.added_bullets:
                bullet_graphics = BulletGraphicsItem(bullet)
                self.scene.addItem(bullet_graphics)
                self.added_bullet_graphics.append(bullet_graphics)
            self.added_bullets.append(bullet)

    def update_items(self):
        '''
        Iterates over all items and updates their position to match
        their physical representations in the game.

        Also moves the players physical location.
        '''
        self.update_window()
        player = self.game.get_player()
        if GUI.KEY_A_STATUS:                    # this is used to move the player LEFT
            player.turn_to(LEFT)
            player.move(LEFT)
        if GUI.KEY_D_STATUS:                    # this is used to move the player RIGHT
            player.turn_to(RIGHT)
            player.move(RIGHT)
        if GUI.KEY_W_STATUS and not player.is_falling():    # this is used to make the player JUMP
            player.jump(GUI.JUMP_SPEED)

        if player.is_falling():                 # this is used to make player that is not standing on element fall
            player.jump(player.jump_speed)
            player.jump_speed -= Player.GRAVITATION

        self.player_graphics.updateAll()
        for enemy_graphics in self.added_enemy_graphics:
            enemy_graphics.item.get_brain().move_enemy()
            enemy_graphics.updateAll()

        for bullet_graphics in self.added_bullet_graphics:
            if bullet_graphics.item.is_in_air():
                bullet_graphics.item.fly()
            bullet_graphics.updateAll()

        if player.get_location().get_y() > 29*SQUARE_SIZE:
            player.destroy()

        if player.get_location().get_x() > 119 *SQUARE_SIZE:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Congratulations!\nYou completed the level :D")
            msgBox.setInformativeText("Back to Main menu")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setDefaultButton(QMessageBox.Ok)
            msgBox.exec_()
            if msgBox.result() == QMessageBox.Ok:
                self.back_to_start()

        if player.is_destroyed():
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("You lost!\nBetter luck next time :(")
            msgBox.setInformativeText("Back to Main menu")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setDefaultButton(QMessageBox.Ok)
            msgBox.exec_()
            if msgBox.result() == QMessageBox.Ok:
                self.back_to_start()

    def back_to_start(self):
        '''
        This method closes the current window and takes user to the starting window.
        '''
        self.starting = StartingWindow()
        GUI.KEY_A_STATUS = False
        GUI.KEY_D_STATUS = False
        GUI.KEY_W_STATUS = False
        self.timer.stop()
        self.close()

    def keyPressEvent(self, e):
        '''
        Detects the keypress of specific keys
        '''
        if e.key() == QtCore.Qt.Key_A:
            GUI.KEY_A_STATUS = True
        elif e.key() == QtCore.Qt.Key_D:
            GUI.KEY_D_STATUS = True
        elif e.key() == QtCore.Qt.Key_W:
            GUI.KEY_W_STATUS = True

    def keyReleaseEvent(self, QKeyEvent):
        '''
        Detects the release of specific keys
        '''
        if QKeyEvent.key() == QtCore.Qt.Key_A and not QKeyEvent.isAutoRepeat():
            GUI.KEY_A_STATUS = False
        elif QKeyEvent.key() == QtCore.Qt.Key_D and not QKeyEvent.isAutoRepeat():
            GUI.KEY_D_STATUS = False
        elif QKeyEvent.key() == QtCore.Qt.Key_W and not QKeyEvent.isAutoRepeat():
            GUI.KEY_W_STATUS = False

    def mousePressEvent(self, QMouseEvent):
        '''
        Detects the mouse press of the player and shoots a bullet towards the mouse location.
        '''
        player = self.game.get_player()
        player_location = player.get_location()
        player_x = player_location.get_x()
        player_y = player_location.get_y()
        x = QMouseEvent.x() + GUI.WINDOW_X
        y = QMouseEvent.y() - SQUARE_SIZE/2
        if self.game.get_player().get_weapon():
            bullet = Bullet()
            self.game.add_bullet(bullet, player_location)
            self.add_bullet_graphics_items()
            bullet.set_target(x, y)


class LevelEditor(QtWidgets.QMainWindow):
    '''
    This class is responsible of creating editor which user can interact with and create new levels.
    '''

    KEY_A_STATUS = False
    KEY_T_STATUS = False
    KEY_D_STATUS = False
    KEY_P_STATUS = False
    KEY_E_STATUS = False
    KEY_W_STATUS = False
    KEY_Right_STATUS = False
    KEY_Left_STATUS = False

    X_MOVEMENT = 0

    def __init__(self):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget())  # QMainWindow must have a centralWidget to be able to add layouts
        self.horizontal = QtWidgets.QHBoxLayout()   # Horizontal main layout
        self.centralWidget().setLayout(self.horizontal)
        self.game = Game()                          # Game instance
        self.square_size = SQUARE_SIZE              # fixed value
        self.square_graphics = []                   # list of square graphics of the game
        self.player_graphics = NotImplemented
        self.added_enemies = []
        self.added_enemy_graphics = []

        self.init_window()
        self.add_game_grid()
        self.update_game_view()

        # Set a timer to call the update function periodically
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_window)
        self.timer.start()  # Milliseconds

    def init_window(self):
        '''
        Sets up the window.
        '''
        self.button1 = QtWidgets.QPushButton("Save level", self)
        self.button2 = QtWidgets.QPushButton("Back to Menu", self)
        self.button3 = QtWidgets.QPushButton("Help", self)
        self.button1.move(10, 20)
        self.button2.move(10, 42)
        self.button3.move(10, 64)
        self.button1.resize(120, 30)
        self.button2.resize(120, 30)
        self.button3.resize(120, 30)
        self.button1.clicked.connect(self.save_button)
        self.button2.clicked.connect(self.back_to_start)
        self.button3.clicked.connect(self.help_button)

        self.setGeometry(0, 0, 1300, 700)
        self.setWindowTitle('Kenttäeditori')
        self.show()

        # Add a scene for drawing 2d objects
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 1250, 660)
        scroll = QtWidgets.QScrollArea()
        scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # Add a view for showing the scene
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)

    @staticmethod
    def help_button():
        '''
        This method opens message box when user clicks the help button.
        '''
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("How to create your own level?")
        msgBox.setInformativeText("Press a command and click screen where you want to place the"\
                                  + " object. User completes the level when player"\
                                  + " reaches the right side of the game area."\
                                  + "\n\nNote! Enemies don't obey gravity and thus it is a good policy to add"\
                                  + " the ground elements before you start adding the enemies."\
                                  + "\n\nCommands:\nA: Add an attacking enemy\n"\
                                  + "T: Add a turning enemy\nD: Add a dumb enemy\nP: Add a player\n"\
                                  + "W: Add an armament box\nE: Add an element square\n"\
                                  + "S: Move to the left on the scene\nF: Move to the right on the scene")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        msgBox.exec_()

    def back_to_start(self):
        '''
        This method closes the current window and takes user to the starting window.
        '''
        self.starting = StartingWindow()
        GUI.KEY_A_STATUS = False
        GUI.KEY_D_STATUS = False
        GUI.KEY_W_STATUS = False
        self.timer.stop()
        self.close()

    def save_button(self):
        '''
        This method asks for the filename to which the game/level will be saved.
        '''
        filename, ok_pressed = QtWidgets.QInputDialog.getText(self, "Save level", "Save the level as text file\n"\
                                                              + "Enter filename:", QtWidgets.QLineEdit.Normal, "")
        if ok_pressed and filename != '':
            saved_successfully = save_game(self.game, filename)
            if not saved_successfully:
                self.save_button()
        elif ok_pressed and filename == '':
            self.save_button()

    def update_window(self):
        '''
        Makes the window follow the player.
        '''
        if LevelEditor.KEY_Right_STATUS:
            LevelEditor.X_MOVEMENT += 50
            if LevelEditor.X_MOVEMENT > 63*SQUARE_SIZE:
                LevelEditor.X_MOVEMENT = 63*SQUARE_SIZE
        elif LevelEditor.KEY_Left_STATUS:
            LevelEditor.X_MOVEMENT -= 50
            if LevelEditor.X_MOVEMENT < 0:
                LevelEditor.X_MOVEMENT = 0
        self.scene.setSceneRect(LevelEditor.X_MOVEMENT, 0, 1250, 660)

    def add_game_grid(self):
        '''
        Adds an QGraphicsItem for each square in the game.
        Qt uses QGraphicsItems to draw objects in the QGraphicsScene.
        QGraphicsRectItem is a subclass of QGraphicsItem, and is useful for
        easily drawing rectangular items.
        This method should only be called once, otherwise it creates duplicates!
        '''
        x = 0
        y = 0
        for i in range(self.game.get_width()):
            for j in range(self.game.get_height()):
                new_square = QGraphicsRectItem(0, 0, self.square_size, self.square_size)
                new_square.setPos(x, y)
                self.square_graphics.append(new_square)
                self.scene.addItem(new_square)
                y += self.square_size
            x += self.square_size
            y = 0

    def add_player_graphics_item(self):
        '''
        Adds a PlayerGraphicsItem for the player. If player already has a graphics item this method does nothing.
        '''
        if self.player_graphics == NotImplemented:
            player_graphics = PlayerGraphicsItem(self.game.get_player())
            self.scene.addItem(player_graphics)
            self.player_graphics = player_graphics

    def add_enemy_graphics_items(self):
        '''
        Adds a EnemyGraphicsItem for every enemy. If enemy already has a graphics item this method does nothing.
        '''
        for enemy in self.game.get_enemies():
            if enemy not in self.added_enemies:
                enemy_graphics = EnemyGraphicsItem(enemy)
                self.scene.addItem(enemy_graphics)
                self.added_enemy_graphics.append(enemy_graphics)
            self.added_enemies.append(enemy)

    def mousePressEvent(self, QMouseEvent):
        '''
        Detects the mouse press of the user.
        '''
        x = QMouseEvent.x() - SQUARE_SIZE/2 + LevelEditor.X_MOVEMENT
        y = QMouseEvent.y() - SQUARE_SIZE/2
        self.update_game(x, y)

    def keyPressEvent(self, e):
        '''
        Detects the keypress of specific keys
        '''
        if e.key() == QtCore.Qt.Key_A:          # Adding attacking enemy
            LevelEditor.KEY_A_STATUS = True
        elif e.key() == QtCore.Qt.Key_T:        # Adding turning enemy
            LevelEditor.KEY_T_STATUS = True
        elif e.key() == QtCore.Qt.Key_D:        # Adding dumb enemy
            LevelEditor.KEY_D_STATUS = True
        elif e.key() == QtCore.Qt.Key_P:        # Adding player
            LevelEditor.KEY_P_STATUS = True
        elif e.key() == QtCore.Qt.Key_E:        # Adding element
            LevelEditor.KEY_E_STATUS = True
        elif e.key() == QtCore.Qt.Key_W:        # Adding armament box
            LevelEditor.KEY_W_STATUS = True
        elif e.key() == QtCore.Qt.Key_F:    # to move while creating the level
            LevelEditor.KEY_Right_STATUS = True
        elif e.key() == QtCore.Qt.Key_S:    # to move while creating the level
            LevelEditor.KEY_Left_STATUS = True

    def keyReleaseEvent(self, e):
        '''
        Detects the release of specific keys
        '''
        if e.key() == QtCore.Qt.Key_A and not e.isAutoRepeat():          # Adding attacking enemy
            LevelEditor.KEY_A_STATUS = False
        elif e.key() == QtCore.Qt.Key_T and not e.isAutoRepeat():        # Adding turning enemy
            LevelEditor.KEY_T_STATUS = False
        elif e.key() == QtCore.Qt.Key_D and not e.isAutoRepeat():        # Adding dumb enemy
            LevelEditor.KEY_D_STATUS = False
        elif e.key() == QtCore.Qt.Key_P and not e.isAutoRepeat():        # Adding player
            LevelEditor.KEY_P_STATUS = False
        elif e.key() == QtCore.Qt.Key_E and not e.isAutoRepeat():        # Adding element
            LevelEditor.KEY_E_STATUS = False
        elif e.key() == QtCore.Qt.Key_W and not e.isAutoRepeat():        # Adding armament box
            LevelEditor.KEY_W_STATUS = False
        elif e.key() == QtCore.Qt.Key_F and not e.isAutoRepeat():    # to move while creating the level
            LevelEditor.KEY_Right_STATUS = False
        elif e.key() == QtCore.Qt.Key_S and not e.isAutoRepeat():    # to move while creating the level
            LevelEditor.KEY_Left_STATUS = False

    def update_game(self, x, y):
        '''
        Adds element to the square that has been clicked by the user if the square is empty. If the square is already
        full this method fails to do nothing.
        '''
        location = Location(x, y, self.game)
        if LevelEditor.KEY_E_STATUS:
            self.game.add_element(location)                     # creating element
        elif LevelEditor.KEY_W_STATUS:
            self.game.add_armament(location)                    # creating armament box
        elif LevelEditor.KEY_P_STATUS:
            player = Player("Sami")                             # creating player
            self.game.add_player(player, location, RIGHT)
            self.add_player_graphics_item()
        elif LevelEditor.KEY_A_STATUS:                          # creating the Attacking enemy
            attacking_body = Enemy("Attacker")
            attacking_brain = AttackingEnemy(attacking_body)
            attacking_body.set_brain(attacking_brain)
            self.game.add_enemy(attacking_body, location, LEFT)
            self.add_enemy_graphics_items()
        elif LevelEditor.KEY_T_STATUS:                          # creating the Turning enemy
            turning_body = Enemy("Turner")
            turning_brain = TurningEnemy(turning_body)
            turning_body.set_brain(turning_brain)
            self.game.add_enemy(turning_body, location, LEFT)
            self.add_enemy_graphics_items()
        elif LevelEditor.KEY_D_STATUS:                          # creating the Dumb enemy
            dumb_body = Enemy("Dumb")
            dumb_brain = DumbEnemy(dumb_body)
            dumb_body.set_brain(dumb_brain)
            self.game.add_enemy(dumb_body, location, LEFT)
            self.add_enemy_graphics_items()

        self.update_game_view()

    def update_game_view(self):
        '''
        Updates the screen to match the game that user is creating. As user clicks a square and presses
        a some of the status keys new element, enemy, armament box or player will be created.
        '''
        for square in self.square_graphics:
            if self.game.get_square(Location(square.scenePos().x(), square.scenePos().y(), self.game)).is_element_square():
                square.setBrush(QtGui.QColor(21, 73, 8))    # ground
                square.setPen(QtGui.QColor(21, 73, 8))
            elif self.game.get_square(Location(square.scenePos().x(), square.scenePos().y(), self.game)).is_armament_square():
                square.setBrush(QtGui.QColor(244, 206, 66)) # weapon box
                square.setPen(QtGui.QColor(244, 206, 66))
            else:
                square.setBrush(QtGui.QColor(181, 210, 251))  # sky
                square.setPen(QtGui.QColor(181, 210, 251))
