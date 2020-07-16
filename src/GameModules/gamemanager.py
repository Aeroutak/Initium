from .unit import Unit
import random

class GameManager:
    def __init__(self):
        pass

    def combat(self, attackingunit, defendingunit):
        if(random.random() < attackingunit.hit):
            defendingunit.changehp(attackingunit.dmg)
        if(random.random() < defendingunit.hit):
            attackingunit.changehp(defendingunit.dmg)
