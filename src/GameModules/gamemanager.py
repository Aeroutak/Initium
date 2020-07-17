from .unit import Unit

import random

def bound(low, high, value):
    return max(low, min(high, value))

class GameManager:
    def __init__(self):
        pass

    def combat(self, attackingunit, defendingunit):
        if random.random() < attackingunit.hit:
            defendingunit.changecurrentstat(1, -attackingunit.dmg)
        print(defendingunit.currenthp)
        if random.random() < defendingunit.hit: #need to add a deathcheck somewhere here
            attackingunit.changecurrentstat(1, -defendingunit.dmg)
        print(attackingunit.currenthp)

    def checkdestroyUnit(self, destroyedunit):
        if(destroyedunit.isDestroyed):
            destroyedunit.status = "DESTROYED"