# Acts as a service
from npc import NPC
class GameService:
    def __init__(self, board):
        self.Board = board
        self.Computer = NPC(self.Board)
    
    def PlacePiece(self, X, Y): # Every time the player places a piece the computer must also place a piece
        self.Board.Set(X, Y, 1)
        if self.CheckForWinner() == True:
            return True
        if len(self.Board.Moves) == self.Board.Size.Width * self.Board.Size.Height: # No more moves left case
            return 0
        self.ComputerTurn()
        if self.CheckForWinner() == True:
            return False
        if len(self.Board.Moves) == self.Board.Size.Width * self.Board.Size.Height: # No more moves left case
            return 0
        return None
        
    def ComputerTurn(self): # Might have different cases for the first move
        if self.Computer.FirstMoved == False:
            self.Computer.FirstMove()
        else:
            self.Computer.Move()

    def CheckForWinner(self): # Function which checks if the game is over by searching for lines of length 5
        for Piece in [-1, 1]:
            for i in range(self.Board.Size.Height):
                for j in range(self.Board.Size.Width):
                    if self.Board.Get(i, j) == Piece:
                        if self.hWin(Piece, i, j) or self.vWin(Piece, i, j) or self.dWin1(Piece, i, j) or self.dWin2(Piece, i, j):
                            return True
        return False

    def hWin(self, Piece, i, j): # Search for horizontal lines
        for k in range(j, j + 5):
            if self.Board.Get(i, k) != Piece:
                return False
        return True

    def vWin(self, Piece, i, j): # Search for vertical lines
        for k in range(i, i + 5):
            if self.Board.Get(k, j) != Piece:
                return False
        return True
    
    def dWin1(self, Piece, i, j): # Search for diagonal lines
        for k in range(5):
            if self.Board.Get(i + k, j + k) != Piece:
                return False
        return True
    
    def dWin2(self, Piece, i, j): # Search for diagonal lines
        for k in range(5):
            if self.Board.Get(i + k, j - k) != Piece:
                return False
        return True
