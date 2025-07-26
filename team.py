from Player import Player
import time

class Team():
    def __init__(self, team_id, name, coach):
        # self._team_id = int(team_id)
        # self._name = str(name)
        # self._coach = str(coach)
        # self._players = []
        # Lỗi = tắt chương trình?

        # fix
        self.team_id = team_id #int
        self._name = name
        self._coach = coach
        self._players = []

    @property
    def team_id(self):
        return self._team_id if hasattr(self,"team_id") else None
    @team_id.setter
    def team_id(self,t_id):
        try:
            t_id = int(t_id)
        except ValueError:
            raise ValueError("ID đội không hợp lệ.")
        self._team_id = t_id

    @property
    def name(self):
        return self._name

    @property
    def coach(self):
        return self._coach

    @property
    def players(self):
        return self._players

#------------------------------------------------------------------------------------
    def add_player(self, player: Player):
        self._players.append(player)

    def remove_player(self, player_id):
        print(f"Đang tìm kiếm ID {player_id}...")
        for id in self._players:
            if id.player_id == player_id:
                self._players.remove(id)
                print(f"Đã xoá cầu thủ {id.name}")
            else:
                print("Không tìm thấy cầu thủ")

    def get_player_by_number(self, number):
        for num in self._players:
            if num.number == number:
                print(f"Tên: {num.name}, Số áo: {num.number}")
            else:
                print("không tìm thấy cầu thủ")

    def get_total_players(self):
        so_thanh_vien = len(self._players)
        return f"Số thành viên của đội là {so_thanh_vien}"



