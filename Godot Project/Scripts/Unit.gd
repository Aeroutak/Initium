extends Node

class Unit:
	
	var unitClass : int
	
	var displayTexture : Texture
	
	var healthPoints : int = 16
	var hitChance : float = 0.85
	var damage : int = 6
	var critChance : int = 5
	var attackSpeed : int = 6
	var movement :  int = 2
	
	func _init (unitClass, displayTexture, healthPoints, hitChances, damage, critChance, attackSpeed, movement):
		var rng = RandomNumberGenerator.new()
		rng.randomize()
		
		self.unitClass = unitClass
		self.displayTexture = displayTexture
		self.healthPoints = healthPoints
		self.hitChances = hitChances
		self.damage = damage
		self.critChance = critChance
		self.attackSpeed = attackSpeed
		self.movement = movement
		
	func tryHit (self, enemyUnit):
		var hitCheck = rng.randf()
		var critCheck = rng.randf()
		var damageDealt = 0
		
		if (hitCheck < self.hitChance)
			damageDealt = self.damage
			if(critCheck < self.critChance)
			damageDealth *= 3
			
		enemyUnit.healthPoints -= damageDealt
		
	func combat (self, enemyUnit):
		tryHit(self, enemyUnit)
		tryHit(enemyUnit, self)
		if(self.attackSpeed - enemyUnit.attackSpeed >= 4)
		tryHit(self, enemyUnit)
		
	
