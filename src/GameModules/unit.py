def my_function():
    print("Hello World!")

class Unit:
    #basic unit with basic parameters.
    def __init__(self, type, power, recovery):
        self.type = type
        self.rp = power
        self.recovery = recovery
        #Basic parameters
        self.maxhp = 10
        self.currenthp = 10
        self.hit = 0.8
        self.speed = 5
        self.dmg = 3
        self.mov = 4
        self.maxreactorpower = 10
        self.currentreactorpower = 10
        self.status = "ALIVE"

    def changehp(self, difference):
        self.currenthp += difference
        if(self.currenthp > self.maxhp):
            self.currenthp = self.maxhp
        if(self.currenthp < 0):
            self.status = "DESTROYED"


