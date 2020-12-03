import unittest as UT
from board import Board
from npc import NPC
from game import GameService as Game
class Tests(UT.TestCase):
    
    def testBoard(self):
        B = Board(5, 5)
        self.assertEqual(B.Size.Width, 5)
        self.assertEqual(B.Size.Height, 5)
        v = B.Get(1, 1)
        self.assertEqual(v, 0)
        B.Set(1, 1, -1)
        v = B.Get(1, 1)
        self.assertEqual(v, -1)
        self.assertRaises(ValueError, B.Set, 1, 1, 0)
        self.assertEqual(v, -1)
        B.Set(1, 1, 0, True)
        v = B.Get(1, 1)
        self.assertEqual(v, 0)
    
    def testNpc(self):
        B = Board(7, 7)
        B.Set(1, 1, 1)
        C = NPC(B)
        for i in range(1, 500):
            C.FirstMove()
            x, y, v = B.Moves[1][0], B.Moves[1][1], B.Moves[1][2]
            self.assertTrue([x, y] != [1, 1])
            self.assertTrue(x >= 0)
            self.assertTrue(x < 7)
            self.assertTrue(y >= 0)
            self.assertTrue(y < 7)
            B.Set(x, y, 0, True)
        self.assertEqual(C.hScore(1, 1, 1), 1)
        B.Set(1, 2, 1)
        self.assertEqual(C.hScore(1, 1, 1), 2)
        B.Set(1, 3, 1)
        self.assertEqual(C.hScore(1, 1, 1), 3)
        B.Set(1, 4, 1)
        self.assertEqual(C.hScore(1, 1, 1), 4)
        B.Set(1, 5, 1)
        self.assertEqual(C.hScore(1, 1, 1), 5)
        # Same idea applies for vScore, d1Score, d2Score, therefore we assume that if this works then those work as well
        # Checking the defense
        B.Set(1, 5, 0, True)
        B.Set(1, 4, 0, True)
        x, y = C.FindBlockMove()
        self.assertEqual(x, 1)
        self.assertEqual(y, 0)
        # Checking the offensive
        B.Set(2, 1, -1)
        B.Set(2, 2, -1)
        B.Set(2, 3, -1)
        x, y, v = C.FindBestMove()
        self.assertEqual(x, 2)
        self.assertEqual(y, 0)
        self.assertEqual(v, 4)
    
    def testGame(self):
        B = Board(7, 7)
        G = Game(B)
        # Placing cases have been tested above, the placement happens correctly.. making sure game knows when its a tie
        for i in range(5):
            B.Set(1, i, 1)
        self.assertTrue(G.CheckForWinner())
        # The win functions are the same as the score ones, except the score ones return the count; no need for further testing
        





