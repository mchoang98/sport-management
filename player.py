from datetime import datetime
# import re


class Player:
    def __init__(self, player_id, name, number, position, dob, performance_score):
        self._player_id = player_id
        self._name = name
        self._number = number
        self._position = position
        self._dob = dob
        self.performance_score = performance_score

    @property
    def player_id(self):
        return self._player_id

    @property
    def name(self):
        return self._name

    @property
    def number(self):
        return self._number

    @property
    def position(self):
        return self._position

    @property
    def dob(self):
        return self._dob

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


