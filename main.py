import re
from match import Match
from player import Player
from score_event import ScoreEvent
from SportMatchManager import SportMatchManager
from team import Team


def menu():
    
    while True:
        print("\n----- MENU -----")
        print("1. Thành lập đội")
        print("2. Thêm trận đấu")
        print("3. Hiện danh sách các đội")
        print("4. Thêm thành viên")
        print("5. Thêm các khoảnh khác 'Jack'")
        print("6. Thoát")

        chon = input("Chọn chức năng: ")
            
        if chon == "1":
            pattern = r"^\d{4}-\d{2}-\d{2}$"

            id_doi = int(input("Nhập id đội: "))
            ten_doi = input("Nhập tên đội: ")
            coach = input("Nhập tên huấn luyện viên: ")
            doi_moi = Team(id_doi, ten_doi, coach)

            so_luong = int(input("Số lượng thành viên (Ít nhất 5 người, tối đa 11 nguời): "))
            for i in range(so_luong):
                ma_ct = str(input("Nhập mã cầu thủ: "))
                ten_ct = str(input("Nhập tên cầu thủ: "))
                so_ct = int(input("Nhập số áo cầu thủ: "))
                vi_tri = str(input("Vị trí thi đấu: "))
                day_ob = input("Ngày sinh: ")
                
                performance_score = float(input("Điểm phong độ"))
                try:
                    doi_moi.add_player(Player(ma_ct, ten_ct, so_ct, vi_tri, day_ob, performance_score))
                except ValueError as e:
                    print(f"Lỗi khi thêm thành viên: {e}")

        elif chon == "2":
            id_match = input("Nhập id trận đấu: ")
            ten_1 = input("Nhập tên đội 1: ")
            try:
                if ten_1.get_team_by_name() is True:
                    print("Đã tìm thấy đội 1")
            except ValueError:
                print("Không tìm thấy")
            ten_2 = input("Nhập tên đội 2: ")
            try:
                if ten_2.get_team_by_name() is True:
                    print("Đã tìm thấy đội 2")
            except ValueError:
                print("Không tìm thấy")
            match_date = input("Nhập ngày tổ chức: ")
            location_match = input("Nhập địa điểm tổ chức")
            SportMatchManager.schedule_match(Match(id_match, ten_1, ten_2, match_date, location_match))
            print("Đã thêm trận đấu")

        elif chon == "3":
            if not SportMatchManager:
                print("Danh sách rỗng")
            for i in SportMatchManager.teams:
                print(i)
                print("-------------------------")
            
        elif chon == "4":
            ma_ct = str(input("Nhập mã cầu thủ: "))
            ten_ct = str(input("Nhập tên cầu thủ: "))
            so_ct = int(input("Nhập số áo cầu thủ: "))
            vi_tri = str(input("Vị trí thi đấu: "))
            day_ob = input("Ngày sinh: ")
            pattern = r"^\d{4}-\d{2}-\d{2}$"
            if not re.match(pattern, day_ob):
                raise ValueError("Ngày tháng không hợp lệ.") 
            performance_score = float(input("Điểm phong độ"))
            cau_thu_moi = Player(ma_ct, ten_ct, so_ct, vi_tri, day_ob, performance_score)
            doi_them = str(input("Nhập id đội muốn thêm"))
            if doi_moi.get_player_by_number is True:
                doi_them.append(cau_thu_moi)
                print("Đã thêm cầu thủ")
            else:
                print("Đã xảy ra lỗi")

        elif chon == "5":
            match = input("Nhập id trận đấu muốn thêm khoảnh khắc: ")
            for i in SportMatchManager.matches:
                if i.match_id == match:
                    print("Đã tìm thấy trận đấu")
                    min_score = int(input(("Nhập thời gian ghi bàn: ")))
                    team_score = input("Nhập đội ghi bàn: ")
                    type_score = input("Nhập loại điểm: ")
                    points = int(input("Nhập số điểm"))
                    khoanh_khac = ScoreEvent(min_score, team_score, type_score, points)
                    i.add_score_event(khoanh_khac)
                    print("Đã thêm khoảnh khắc")
                else:
                    print("Đã không thêm được khoảnh khắc")
                    
        elif chon == "6":
            print("Dừng lại chương trình")
            break
        
menu()





