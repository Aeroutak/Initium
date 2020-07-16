from .unit import Unit

import random

def bound(low, high, value):
    return max(low, min(high, value))

class GameManager:
    def __init__(self):
        pass

    def combat(self, attackingunit, defendingunit):
        if random.random() < attackingunit.hit:
            defendingunit.changehp(attackingunit.dmg)
        if random.random() < defendingunit.hit & defendingunit.isDestroyed == False:
            attackingunit.changehp(defendingunit.dmg)

    def checkdestroyUnit(self, destroyedunit):
        if(destroyedunit.isDestroyed):
            destroyedunit.status = "DESTROYED"