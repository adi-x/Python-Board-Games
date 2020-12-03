from board import Board as Board
from game import Game as GameService
class Test:
    def TestFire(self):
        TranslationTable = {0: " ", 1: "E", 2: "*", 3: "X", 4:"-"}
        Grid = Board(TranslationTable)
        GS = GameService(Grid)
        Grid.Set(3, 3, 1) # Placing earth
        assert GS.Fire("A1") == 3
        assert Grid.Get(0, 0) == 4
        assert GS.Fire("D4") == 0
        assert Grid.Get(3, 3) == 1
        Grid.Set(1, 1, 3)
        assert GS.Fire("B2") == 1
        assert Grid.Get(1, 1) == 4
        Grid.Set(2, 2, 2)
        assert GS.Fire("C3") == 2
        assert Grid.Get(2, 2) == 2
        try:
            GS.Fire("AA")
            assert False
        except:
            assert True
        
        try:
            GS.Fire("1A")
            assert False
        except:
            assert True
        
        try:
            GS.Fire("A10")
            assert False
        except:
            assert True


