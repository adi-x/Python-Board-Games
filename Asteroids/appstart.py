from board import Board
from ui import UserInterface
from game import Game
from tests import Test as TestClass

if __name__ == "__main__":
    TranslationTable = {0: " ", 1: "E", 2: "*", 3: "X", 4:"-"}
    Test = TestClass()
    Test.TestFire()
    Grid = Board(TranslationTable)
    _Game = Game(Grid)
    _Game.GridSetup()
    UI = UserInterface(Grid, _Game)
    UI.Start()