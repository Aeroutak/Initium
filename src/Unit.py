class Unit:
    #basic unit with basic parameters.
    def __init__(self, type, power, recovery):
        self.type = type;
        self.rp = power;
        self.recovery = recovery;
        #Basic parameters
        self.hp = 10;
        self.hit = 0.8;
        self.dmg = 3;
        self.mov = 4;