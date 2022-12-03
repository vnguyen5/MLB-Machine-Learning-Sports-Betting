class Stats:
    def __init__(self):
        self.runs = 0
        self.ab = 0
        self.hits = 0
        self.doubles = 0
        self.triples = 0
        self.homeruns = 0
        self.hbp = 0
        self.bb = 0
        self.ibb = 0
        self.ks = 0
        self.sb = 0
        self.cs = 0
        self.sac_fly = 0

    def onbase(self):
        return (self.hits + self.bb + self.ibb + self.hbp) / (self.ab + self.bb + self.ibb + self.hbp + self.sac_fly)

    def slugging(self):
        return ((self.hits - self.doubles - self.triples - self.homeruns) + 2 * self.doubles + 3 * self.triples + 4 * self.homeruns) / self.ab
    
    def ops(self):
        return self.onbase() + self.slugging()
