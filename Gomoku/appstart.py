from consoleUI import ConsoleUserInterface
from graphicalUI import GraphicalUserInterface, Start
from board import Board
if __name__ == "__main__":
    BoardObj = Board(15, 15)
    ui = "gui"
    if ui == "gui":
        Start(BoardObj)
    elif ui == "cui":
        cmd = ConsoleUserInterface(BoardObj)
        cmd.Start()