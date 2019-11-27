import sys
from PyQt5.QtWidgets import QApplication

from gui import StartingWindow


def main():
    '''
    Creates a Game and sets player and enemies to the game.
    '''
    # Every Qt application must have one instance of QApplication.
    global app  # Use global to prevent crashing on exit
    app = QApplication(sys.argv)
    starting = StartingWindow()

    # Start the Qt event loop. (i.e. make it possible to interact with the gui)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


