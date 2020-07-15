class Board:
    def __init__(self, boardFile):
        self.boardFile = boardFile
        self.board = open(self.boardFile, "r")

    def boardSize(self):
        print(self.board.read())