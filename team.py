from stats import Stats
class Team:
    def __eq__(self, other):
        return self.id == other.id

    def __init__(self, id):
        self.games = 0
        self.id = id

        # # offense
        # self.runs = 0
        # self.ab = 0
        # self.hits = 0
        # self.doubles = 0
        # self.triples = 0
        # self.homeruns = 0
        # self.hbp = 0
        # self.bb = 0
        # self.ibb = 0
        # self.ks = 0
        # self.sb = 0
        # self.cs = 0
        # self.sac_fly = 0

        # # defense
        # self.runs_allowed = 0
        # self.ab_allowed = 0
        # self.hits_allowed = 0
        # self.doubles_allowed = 0
        # self.triples_allowed = 0
        # self.homeruns_allowed = 0
        # self.hbp_allowed = 0
        # self.bb_allowed = 0
        # self.ibb_allowed = 0
        # self.ks_allowed = 0
        # self.sb_allowed = 0
        # self.cs_allowed = 0
        # self.sac_fly_allowed = 0

        self.offensive_stats = Stats()
        self.defensive_stats = Stats()

    def __str__(self):
        output = f'{str(self.id)}'
        return output

    def ops(self):
        return self.offensive_stats.ops()

    def ops_allowed(self):
        return self.defensive_stats.ops()

    def runs_pg(self):
        return self.offensive_stats.runs / self.games

    def runs_allowed_pg(self):
        return self.defensive_stats.runs / self.games
