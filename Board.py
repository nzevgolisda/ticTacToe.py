from random import randint as rand
from Square import Square
class Board:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.id = 'O'
        self.win = False
        self.winner = None
        self.pair = []
        self.index = [['i', 'j']]
        self.squares = self.createSquares()
        self.board = self.createBoard()
    def createSquares(self):
        self.squares = []
        for i in range(self.m):
            row = []
            for j in range(self.n):
                row.append(Square(i, j))
            self.squares.append(row)
        return self.squares
    def createBoard(self):
        self.board = []
        for i in range(self.m):
            row = []
            for j in range(self.n):
                row.append(self.squares[i][j])
            self.board.append(row)
        return self.board
    def checkRowWin(self):
        for i in range(self.m):
            if self.win == False:
                k = 0
                a = self.board[i][0].value
                for j in range(self.n):
                    b = self.board[i][j].value
                    if a == b and a == self.id:
                        k += 1
                if k == self.n:
                    self.win = True
                    return self.id
            else:
                break
    def checkColWin(self):
        for i in range(self.m):
            if self.win == False:
                k = 0
                a = self.board[i][0].value
                for j in range(self.n):
                    b = self.board[j][i].value
                    if a == b and a == self.id:
                        k += 1
                if k == self.n:
                    self.win = True
                    return self.id
            else:
                break
    def checkDiagWin(self):
        k = 0 # for [i][i] diagonal
        for i in range(self.m):
            if self.win == False:
                a = self.board[0][0].value
                b = self.board[i][i].value
                if a == b and a == self.id:
                    k += 1
        if k == self.m:
            self.win = True
            return self.id
        w = 0 # for other diagonal
        for i in range(self.m):
            if self.win == False:
                a = self.board[0][self.m-1].value
                b = self.board[i][self.m-1-i].value
                if a == b and a == self.id:
                    w += 1
        if w == self.m:
            self.win = True
            return self.id
    def checkPair(self):
        self.pair = ['i', 'j']
        while self.pair in self.index:
            i = rand(0, self.m-1)
            j = rand(0, self.n-1)
            self.pair = [i, j]
            if self.pair not in self.index:
                self.index.append(self.pair)
                sq = self.board[i][j]
                sq.value = self.id
                break
    def changeId(self):
        if self.id == 'O':
            self.id = 'X'
        elif self.id == 'X':
            self.id = 'O'
    
    def printWin(self):
        print('Player ' + self.id + ' won')
    def printDraw(self):
        print('Players made a draw')    
    def __str__(self):
        s = ''
        for i in range(self.m):
            s1 = '| '
            for j in range(self.n):
                s1 += str(self.board[i][j]) + ' | '
            s += s1 + '\n'
        return s