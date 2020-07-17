from GameModules.board import Board
from GameModules.unit import Unit
from GameModules.tile import Tile
from GameModules.gamemanager import GameManager

board1 = Board("Maps/Map1.txt")
board1.boardSize()

game = GameManager()
unit1 = Unit("Melee", 10, 20)
unit2 = Unit("Ranged", 50, 50)

game.combat(unit1, unit2)