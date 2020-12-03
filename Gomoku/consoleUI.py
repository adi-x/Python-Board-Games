import texttable as t
from game import GameService
class ConsoleUserInterface:
    def __init__(self, board):
        self.Board = board
        self.Game = GameService(self.Board)
    
    def ShowBoard(self):
        DisplayTable = t.Texttable(0)
        FirstRow = ["X\\Y"]
        AlignArray = ["c"]
        for i in range(1, min(9, self.Board.Size.Width) + 1):
            FirstRow.append(" {0} ".format(str(i)))
            AlignArray.append("c")
        for i in range(10, self.Board.Size.Width + 1):
            FirstRow.append(str(i) + " ")
            AlignArray.append("c")
        DisplayTable.header(FirstRow)
        DisplayTable.set_cols_align(AlignArray)
        C = 1
        for i in range(self.Board.Size.Height):
            Row = [str(C)]
            C = C + 1
            for j in range(self.Board.Size.Width):
                if self.Board.Get(i, j) == 0:
                    Row.append(" ")
                elif self.Board.Get(i, j) == 1:
                    Row.append("X")
                elif self.Board.Get(i, j) == -1:
                    Row.append("O")
            DisplayTable.add_row(Row)
        print(DisplayTable.draw())
    
    def PlayerMove(self):
        print("It is your turn to place a piece on the board. Enter the coordinates of the tile:")
        X = int(input("X = "))
        Y = int(input("Y = "))
        return self.Game.PlacePiece(X - 1, Y - 1)
    
    def Start(self):
        self.ShowBoard()
        while True:
            try:
                Response = self.PlayerMove()
                if Response != True:
                    print("It is the computer's turn to place a piece...")
                    if Response == False:
                        print("The computer has won!")
                        self.ShowBoard()
                        break
                    if Response == 0:
                        print("No more moves available!")
                        self.ShowBoard()
                        break
                else:
                    print("You have won!")
                    self.ShowBoard()
                    break
                self.ShowBoard()
            except ValueError:
                print("Invalid input data!")