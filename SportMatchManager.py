class SportMatchManager:
    def __init__(self):
        self.teams = []
        self.matches = []

    def add_team(self, team):
        self.teams.append(team)

    def get_team_by_name(self, name: str):
        for team in self.teams:
            if team.name == name:
                return team
        return None



# Để anh làm cái này cho. -Hùng-