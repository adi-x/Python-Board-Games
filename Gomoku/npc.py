import random as r
class NPC:
    def __init__(self, board):
        self.Board = board
        self.FirstMoved = False

    def FirstMove(self): # the first move will be a random one
        self.FirstMoved = True
        randX = r.randint(1, self.Board.Size.Height) - 1
        randY = r.randint(1, self.Board.Size.Width) - 1
        if self.Board.Get(randX, randY) != 0:
            self.FirstMove()
        else:
            self.Board.Set(randX, randY, -1)
    
    def Move(self):
        # Checking if we are one move away from winning...
        x, y, score = self.FindBestMove()
        if score == 5:
            self.Board.Set(x, y, -1)
            return
        # Checking if we need to defend...
        x1, y1 = self.FindBlockMove()
        if x1 != -1 and y1 != -1:
            self.Board.Set(x1, y1, -1)
        # If we don't need to defend then we'll go on to the offensive...
        else:
            self.Board.Set(x, y, -1)

    # Offensive:
    def FindHighestScore(self, Piece): # Getting the longest line on the board after a fake placement
        maxS = 0
        for i in range(self.Board.Size.Height):
            for j in range(self.Board.Size.Width):
                if self.Board.Get(i, j) == Piece:
                    localMaxS = max(self.hScore(Piece, i, j), self.vScore(Piece, i, j), self.d1Score(Piece, i, j), self.d2Score(Piece, i, j))
                    if localMaxS > maxS:
                        maxS = localMaxS
        return maxS

    def hScore(self, Piece, i, j): # Gets the length of a line that starts at A(i, j) horizontally
        Score = 0
        for k in range(j, j + 5):
            if self.Board.Get(i, k) != Piece:
                break
            Score += 1
        return Score

    def vScore(self, Piece, i, j): # Gets the length of a line that starts at A(i, j) vertically
        Score = 0
        for k in range(i, i + 5):
            if self.Board.Get(k, j) != Piece:
                break
            Score += 1
        return Score
    
    def d1Score(self, Piece, i, j): # Gets the length of a line that starts at A(i, j) diagonally
        Score = 0
        for k in range(5):
            if self.Board.Get(i + k, j + k) != Piece:
                break
            Score += 1
        return Score
    
    def d2Score(self, Piece, i, j): # Gets the length of a line that starts at A(i, j) diagonally
        Score = 0
        for k in range(5):
            if self.Board.Get(i + k, j - k) != Piece:
                break
            Score += 1
        return Score
    
    def FindBestMove(self): # Finding the best place which would produce the longest line by repetitivily falsily placing pieces. The final placement will be the one which produces the longest line
        maxScore = 0
        maxI = -1
        maxJ = -1
        for i in range(self.Board.Size.Height):
            for j in range(self.Board.Size.Width):
                if self.Board.Get(i, j) == 0:
                    self.Board.Set(i, j, -1)
                    Score = self.FindHighestScore(-1)
                    if maxScore < Score:
                        maxScore = Score
                        maxI = i
                        maxJ = j
                    self.Board.Set(i, j, 0, True)
        return maxI, maxJ, maxScore

    # Defensive
    def FindBlockMove(self): # Tries to see if the opponent is approaching victory and attempts to block it
        maxI = -1
        maxJ = -1
        for i in range(self.Board.Size.Height):
            for j in range(self.Board.Size.Width):
                if self.Board.Get(i, j) == 0:
                    self.Board.Set(i, j, 1)
                    Score = self.FindHighestScore(1)
                    if Score == 5:
                        maxI = i
                        maxJ = j
                    if Score == 4:
                        if self.hScore(1, i, j) == 4:
                            if self.Board.Get(i, j-1) == 0 or self.Board.Get(i, j + 4) == 0:
                                maxI = i
                                maxJ = j
                        elif self.vScore(1, i, j) == 4:
                            if self.Board.Get(i-1, j) == 0 or self.Board.Get(i+4, j) == 0:
                                maxI = i
                                maxJ = j
                        elif self.d1Score(1, i, j) == 4:
                            if self.Board.Get(i-1, j-1) == 0 or self.Board.Get(i+4, j+4) == 0:
                                maxI = i
                                maxJ = j
                        elif self.d2Score(1, i, j) == 4:
                            if self.Board.Get(i-1, j+1) == 0 or self.Board.Get(i+4, j-4) == 0:
                                maxI = i
                                maxJ = j
                    self.Board.Set(i, j, 0, True)
                    if maxI != -1 and maxJ != -1:
                        return maxI, maxJ
        return maxI, maxJ