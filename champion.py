class Champion:
    def __init__(self, name: str, kda: str, kda_whole: str, cs: str, cs_min: str, win_rate: str, games_played: str):
        self.name = name
        self.kda = kda
        self.kda_whole = kda_whole
        self.cs = cs
        self.cs_min = cs_min
        self.win_rate = win_rate
        self.games_played = games_played

    def get_all(self):
        return [self.name,
                self.kda,
                self.kda_whole,
                self.cs,
                self.cs_min,
                self.win_rate,
                self.games_played]

    def get_name(self):
        return self.name

    def get_kda(self):
        return self.kda

    def get_kda_whole(self):
        return self.kda_whole

    def get_cs(self):
        return self.cs

    def get_win_rate(self):
        return self.win_rate

    def get_games_played(self):
        return self.games_played
