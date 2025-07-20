from abc import ABC


class Player(ABC):
    pass


class Team():
    def __init__(self, team_id, name, coach):
        self.team_id = int(team_id)
        self.name = str(name)
        self.coach = str(coach)
        self.players = []

    def add_player(self, player: Player):
        self.players.append(player)

    def remove_player(self, player_id: int):
        for id in self.players:
            if id.player_id == player_id:
                self.players.remove(id)
                print(f"Đã xoá cầu thủ {id.name}")
            else:
                print("Không tìm thấy cầu thủ")

    def get_player_by_number(self, number: int):
        for num in self.players:
            if num.number == number:
                print(f"Tên: {num.name}, Số áo: {num.number}")
            else:
                print("không tìm thấy cầu thủ")

    def get_total_players(self):
        so_thanh_vien = len(self.players)
        print(f"Số thành viên của đội là {so_thanh_vien}")
