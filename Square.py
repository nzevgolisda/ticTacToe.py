
class Square:
    def __init__(self, i, j):
        self.row = i
        self.col = j
        self.value = '_'
    def __str__(self):
        return str(self.value)