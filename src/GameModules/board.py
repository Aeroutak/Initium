class Board:
    def __init__(self, boardFile):
        self.boardFile = boardFile
        self.board = open(self.boardFile, "r")

    def boardSize(self):
        firstline = self.board.readline()
        print(firstline)