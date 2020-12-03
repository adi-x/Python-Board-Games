import random as r
class NPC:
    def __init__(self, board):
        self.Board = board
        self.FirstMoved = True # No separate case for the First Move
        self.ct=0
    
    def Move(self):
        x, y = self.FindBestMove()
        self.Board.Set(x, y, -1)

    def Evaluate(self):
        if len(self.Board.Moves) < 9: # There certainly cannot be a victory for either piece with only 9 pieces on the board 
            return 0
        #for Piece in [-1, 1]: 
        for Move in self.Board.Moves: # For each piece placed we try to see if it is a part of a line of length 5
            #if Move[2] == Piece:
                i = Move[0]
                j = Move[1]
                Piece = Move[2]
                if self.Board.Get(i, j) == Piece:
                    if max(self.hScore(Piece, i, j), self.vScore(Piece, i, j), self.d1Score(Piece, i, j), self.d2Score(Piece, i, j)) == 5:
                        return -1 * Piece * 500 # 500 for bot, -500 for user
        return 0

    def hScore(self, Piece, i, j):
        Score = 0
        for k in range(j, j + 5):
            if self.Board.Get(i, k) != Piece:
                break
            Score += 1
        return Score

    def vScore(self, Piece, i, j):
        Score = 0
        for k in range(i, i + 5):
            if self.Board.Get(k, j) != Piece:
                break
            Score += 1
        return Score
    
    def d1Score(self, Piece, i, j):
        Score = 0        
        for k in range(5):
            if self.Board.Get(i + k, j + k) != Piece:
                break
            Score += 1
        return Score
    
    def d2Score(self, Piece, i, j):
        Score = 0
        for k in range(5):
            if self.Board.Get(i + k, j - k) != Piece:
                break
            Score += 1
        return Score
    
    def isMovesLeft(self):
        return len(self.Board.Moves) != self.Board.Size.Width * self.Board.Size.Height # Optimization
        '''
        for i in range(self.Board.Size.Height): 
            for j in range(self.Board.Size.Width):
                if self.Board.Get(i, j) == 0:
                    return True
        return False
        '''
    
    def minimax(self, depth, isMax, alpha, beta):
        score = self.Evaluate()
        if score != 0: # If either the maximizer or the minimizer won the game return their score
            return score
        
        if self.isMovesLeft() == False: # tie
            return 0
        
        # For efficiency we only go up to the depth of 3 (checking up to 3 moves ahead)
        if depth >= 3:
            return 0
        
        # The computer is the maximizer
        if isMax == True:
            best = -500000 # -inf
            for i in range(self.Board.Size.Height):
                for j in range(self.Board.Size.Width):
                    self.ct = self.ct + 1
                    if self.Board.Get(i, j) == 0:
                        self.Board.Set(i, j, -1)
                        val = self.minimax(depth + 1, not isMax, alpha, beta)
                        best = max(best, val)
                        alpha = max(alpha, best)
                        self.Board.Set(i, j, 0, True)
                        if beta <= alpha:
                            break
            return best
        else:
            best = 500000 # inf
            for i in range(self.Board.Size.Height):
                for j in range(self.Board.Size.Width):
                    self.ct = self.ct + 1
                    if self.Board.Get(i, j) == 0:
                        self.Board.Set(i, j, 1)
                        val = self.minimax(depth + 1, not isMax, alpha, beta)
                        best = min(best, val)
                        beta = min(beta, best)
                        self.Board.Set(i, j, 0, True)
                        if beta <= alpha:
                            break
            return best
        
    def FindBestMove(self):
        # Finds the move with the biggest score based on the minimax function by checking the score of each possible placement on the board
        best = -500000
        x = -1
        y = -1
        for i in range(self.Board.Size.Height):
            for j in range(self.Board.Size.Width):
                if self.Board.Get(i, j) == 0:
                    self.Board.Set(i, j, -1)
                    val = self.minimax(0, False, -500000, 500000)
                    self.Board.Set(i, j, 0, True)
                    if val > best:
                        x = i
                        y = j
                        best = val
        print(str(self.ct))
        return x, y
