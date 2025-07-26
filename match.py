from Score_event import ScoreEvent
from Team import Team

class Match():
    def __init__(self, match_id, team1: Team, team2:Team, date, location):
        # self.match_id = int(match_id)
        # same lỗi = tắt chương trình + input thì không cần str() nữa.

        self.match_id = match_id
        self._team1 = team1
        self._team2 = team2
        self._date = date
        self._location = location
        self._score_events = []

    @property
    def match_id(self):
        return self._match_id
    @match_id.setter
    def match_id(self,m_id):
        try:
            m_id = int(m_id)
        except ValueError:
            raise ValueError("ID trận đấu không hợp lệ.")
        self._match_id = m_id

    @property
    def team1(self):
        return self._team1

    @property
    def team2(self):
        return self._team2

    @property
    def date(self):
        return self._date

    @property
    def location(self):
        return self._location

    @property
    def score_events(self):
        return self._score_events

#------------------------------------------------------------------------------------

    """
    __init__(): khởi tạo trận đấu
    add_score_event(event: ScoreEvent): thêm sự kiện ghi điểm vào danh sách
    get_score(): trả về tổng điểm của hai đội dạng tuple (score_team1, score_team2)
    get_winner(): trả về tên đội thắng, hoặc "Draw"
    print_match_summary(): in thông tin tổng hợp trận đấu
    """

    def add_score_event(self, event: ScoreEvent):
        self.score_events.append(event)

    def get_score(self):
        return tuple(self.team1.points, self.team2.points)

    def get_winner(self):
        score1 = self.team1.points
        score2 = self.team2.points
        return self.team1 if score1 > score2 else (self.team2 if score1 < score2 else "Draw")

    def print_match_summary(self):
        return f"""ID trận đấu: {self.match_id}
Trận đấu giữa 2 đội:
    {self.team1.name} ({self.team1.team_id}) vs {self.team2.name} ({self.team2.team_id})
Ngày diễn ra: {self.date}
Địa điểm: {self.location}"""













