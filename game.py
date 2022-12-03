class Game:
    def __init__(self, away, home, home_win):
        self.away = away
        self.home = home

        # self.p_away = p_away
        # self.p_home = p_home
        self.home_win = home_win

    def series(self):
        return {
            'team_away': self.away.id,
            'games_away': self.away.games,
            'runs_away': self.away.runs_pg(),
            'ops_away': self.away.ops(),
            'runs_allowed_away' : self.away.runs_allowed_pg(),
            'ops_allowed_away': self.away.ops_allowed(),

            'team_home': self.home.id,
            'games_home': self.home.games,
            'runs_home': self.home.runs_pg(),
            'ops_home': self.home.ops(),
            'runs_allowed_home' : self.home.runs_allowed_pg(),
            'ops_allowed_home': self.home.ops_allowed(),

            'home_win': int(self.home_win)
        }
