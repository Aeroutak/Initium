extends Node


# Declare member variables here. Examples:
var boardSize : int = 10
	#Tile states
var hasUnit: bool = false
var hasObstruction: bool = false
var hasObjective: bool = false


# Called when the node enters the scene tree for the first time.
func _ready():
	add_to_group("TileContainer")
	for i in range(boardSize):
		for j in range(boardSize):
			i

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
