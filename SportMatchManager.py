from team import Team
from match import Match

class SportMatchManager:
    def __init__(self):
        self.teams = []
        self.matches = []

    def add_team(self, team:Team):
        self.teams.append(team)

    def get_team_by_name(self, name: str):
        for team in self.teams:
            if team.name == name:
                return team
        return None

    def schedule_match(self,match:Match):
        self.matches.append(match)

    def list_matches(self):
        show = "\n===== Các trận đã diễn ra ====="
        for i,match in enumerate(self.matches,1):
            show += f"\n{i}. {match.print_match_summary()}\n--------------------------------------------"
        return show

    def get_top_scorer(self):
        total_points = {}
        for match in self.matches:
            for score in match.score_events:
                if score.player in total_points:
                    total_points[score.player] += score.points
                else:
                    total_points[score.player] = score.points
        return max(total_points, key=lambda player: total_points[player])

    def get_highest_scoring_match(self):
        total_points = {}
        for match in self.matches:
            for score in match.score_events:
                if match in total_points:
                    total_points[match] += score.points
                else:
                    total_points[match] = score.points
        return max(total_points, key=lambda match: total_points[match])

