import texttable
class Board:
    def __init__(self, translate):
        self.Grid = [0] * (7 * 7)
        self.Translation = translate
        self._Cheat = False
        self.AlienShips = []

    @property
    def AlienShipCount(self):
        return len(self.AlienShips)

    def Get(self, x, y):
        return self.Grid[7 * x + y]

    def Set(self, x, y, Value):
        self.Grid[7 * x + y] = Value
    
    def Cheat(self):
        self._Cheat = not self._Cheat
    
    def __str__(self):
        Keeper = self.Translation[3]
        if self._Cheat == False:
            self.Translation[3] = self.Translation[0]
        View = texttable.Texttable()
        Rows = [[" ", "A", "B", "C", "D", "E", "F", "G"]]
        RowCount = 1
        for i in range(7):
            Row = [RowCount]
            RowCount += 1
            for j in range(7):
                Row.append(self.Translation[self.Get(i, j)])
            Rows.append(Row)
        View.add_rows(Rows, True)
        self.Translation[3] = Keeper
        return View.draw()
    


