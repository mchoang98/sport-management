from datetime import datetime
# import re


class Player:
    def __init__(self, player_id, name, number, position, dob, performance_score):
        self.player_id = player_id
        self.name = name
        self.number = number
        self.position = position
        self.dob = dob
        self.performance_score = performance_score

    @property
    def performance_score(self):
        return self._performance_score if hasattr(self,"_performance_score") else None
    @performance_score.setter
    def performance_score(self,value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Điểm phong độ không hợp lệ.")
        self._performance_score = value

    def update_performance(self, score):
        self._performance_score = score

    def get_age(self):
        # pattern = r"^\d{4}-\d{2}-\d{2}$"
        # if not re.match(pattern,self.dob):
        #     raise ValueError("Ngày tháng không hợp lệ.")
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year


