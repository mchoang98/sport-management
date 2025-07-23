from abc import ABC
class ScoreEvent(ABC):
    pass


class Match():
    def __init__(self, match_id, team1, team2, date, location):
        self.match_id = int(match_id)
        self.team1 = team1
        self.team2 = team2
        self.date = str(date)
        self.location = str(location)
        self.score_events = []
    
    def add_score_event(self, event: ScoreEvent):
        self.score_events.append(event)

    @property
    def get_score(self):
        return set(self.team1.points, self.team2.points)












