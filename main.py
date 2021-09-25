from random import randint as rand
from Square import Square
from Board import Board
def playGame():
    self = Board(7, 7)
    print(self)
    while len(self.index) <= self.m*self.n + 1 and self.win == False and self.winner not in ['O', 'X']:
        self.checkPair()
        print(self)
        if self.checkRowWin() == self.id or self.checkColWin() == self.id or self.checkDiagWin() == self.id:
            self.printWin()
            self.win = True
            self.winner = self.id
            break
        elif len(self.index) == self.m*self.n + 1 and self.win == False:
            self.printDraw()
            self.win = True
            break
        self.changeId()
playGame()