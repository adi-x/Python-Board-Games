import texttable as t
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtTest
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5 import QtGui
from game import GameService
from time import sleep
import threading as th
class GraphicalUserInterface(QWidget):
    def __init__(self, board):
        super().__init__()
        self.Board = board
        self.BoardGui = None
        self.Game = GameService(self.Board)
        self.CanPlace = False
        self.initUI()
        self.Closed = False
        self.Loop()
    
    def initUI(self):      
        self.setGeometry(400, 150, 0, 0)
        self.setFixedSize(self.Board.Size.Width * 40, self.Board.Size.Height * 40 + 40)
        self.setWindowTitle('Gomoku')
        self.CreateBoard()
        self.show()

    def ButtonClick(self):
        if self.CanPlace == True:
            self.X = self.sender().property("i")
            self.Y = self.sender().property("j")
            if self.Board.Get(self.X, self.Y) == 0:
                self.CanPlace = False
    @property
    def Title(self):
        return self.__Title.getText()

    @Title.setter
    def Title(self, value):
        self.__Title.setText(value)

    def closeEvent(self, event):
        super().closeEvent(event)
        sys.exit()

    def CreateBoard(self):
        self.BoardGui = []
        Title = QLabel("", self)
        self.__Title = Title
        Title.setGeometry(0, 0, self.Board.Size.Width * 40, 40)
        Title.setFont(QtGui.QFont("Calibri", 16, QtGui.QFont.Bold))
        Title.setAlignment(Qt.AlignCenter)
        for i in range(self.Board.Size.Height):
            Line = []
            for j in range(self.Board.Size.Width):
                button_obj = QPushButton(" ", self)
                button_obj.setCheckable(True)
                button_obj.setGeometry(j * 40, 40 + i * 40, 40, 40)
                button_obj.setProperty("i", i)
                button_obj.setProperty("j", j)
                button_obj.setCheckable(False)
                button_obj.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
                button_obj.clicked.connect(self.ButtonClick)
                button_obj.setContentsMargins(0,0,0,0)
                button_obj.setStyleSheet("Text-align:center")
                Line.append(button_obj)
            self.BoardGui.append(Line)
        
    def ShowBoard(self):
        for i in range(self.Board.Size.Height):
            for j in range(self.Board.Size.Width):
                if self.Board.Get(i, j) == 0:
                    self.BoardGui[i][j].setText(" ")
                elif self.Board.Get(i, j) == 1:
                    self.BoardGui[i][j].setText("⚪")
                elif self.Board.Get(i, j) == -1:
                    self.BoardGui[i][j].setText("⚫")
                    
    def Visualize(self, x, y):
        if self.Board.Get(x, y) == 0:
            self.BoardGui[x][y].setText("⚪")
            self.Title = "It is the computer's turn to place a piece..."

    def PlayerMove(self):
        self.Title = "It is your turn to place a piece on the board..."
        self.CanPlace = True
        while self.CanPlace == True:
            QtTest.QTest.qWait(100)
        self.Visualize(self.X, self.Y)
        QtTest.QTest.qWait(100)
        
        Answer = self.Game.PlacePiece(self.X, self.Y)
        return Answer
    
    def Loop(self):
        while True:
            Response = self.PlayerMove()
            if self.Closed == True:
                break
            if Response != True:
                self.ShowBoard()
                if Response == False:
                    self.Title = "The computer has won!"
                    self.ShowBoard()
                    break
                if Response == 0:
                    self.Title = "No more moves available!"
                    self.ShowBoard()
                    break
            else:
                self.Title = "You have won!"
                self.ShowBoard()
                break
            self.ShowBoard()
    
def Start(board):
    app = QApplication(sys.argv)
    gui = GraphicalUserInterface(board)
    sys.exit(app.exec_())