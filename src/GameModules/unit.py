def bound(low, high, value):
    return max(low, min(high, value))

class Unit:
    #basic unit with basic parameters.
    def __init__(self, type, power, recovery):
        self.type = type
        self.rp = power
        self.recovery = recovery
        #Basic parameters
        self.maxhp = 10
        self.currenthp = self.maxhp
        self.hit = 0.8
        self.speed = 5
        self.dmg = 3
        self.mov = 4
        self.maxreactorpower = 10
        self.currentreactorpower = self.maxreactorpower
        self.status = "ALIVE"

    def changecurrentstat(self, type, difference):
        if type == 1:
            self.currenthp += difference
            bound(0, self.maxhp, self.currenthp)
        else:
            self.currentreactorpower += difference
            bound(0, self.maxreactorpower, self.currentreactorpower)

    def isDestroyed(self):
        return self.currenthp == 0





