

class ScoreEvent:
    def __init__(self,minute,team,player,score_type,points):
        self.minute = minute # thời gian ghi bàn, chạy setter "minute"
        self._team = team
        self._player = player
        self._score_type = score_type #goal, point, spike,...
        self.points = points # chạy setter "points"

    @property
    def minute(self):
        return self._minute if hasattr(self,"_minute") else None # trả về nếu có attribute _minute
    @minute.setter
    def minute(self,value): # value: phút
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Thời gian ghi bàn không hợp lệ.")
        self._minute = value #đưa giá trị vào _minute thay vì minute

    @property
    def team(self):
        return self._team

    @property
    def player(self):
        return self._player if self._player else None # Trả về None nếu không có

    @property
    def score_type(self):
        return self._score_type

    @property
    def points(self):
        return self._points if hasattr(self,"_points") else None # trả về nếu có attribute _points
    @points.setter
    def points(self,value):
        try:
            value = int(value)
        except ValueError:
            raise ValueError(f"Điểm không hợp lệ.")
        self._points = value #đưa giá trị vào _minute thay vì minute

    def get_description(self):
        return f"""
Thời gian ghi điểm: {self.minute}
Đội ghi điểm: {self.team}
Người ghi điểm: {self.player}
Loại ghi điểm: {self.score_type}
Số điểm ghi được: {self.points}
"""