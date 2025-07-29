from match import Match
from player import Player
from score_event import ScoreEvent
from SportMatchManager import SportMatchManager
from team import Team
import time
#=================================================

def menu():
    print("""
----------------------------------
|    QUẢN LÝ TRẬN ĐẤU BÓNG ĐÁ    |
----------------------------------""")
    print("|1. Quản lý đội.                |")
    print("|2. Quản lý trận đấu.           |")
    print("|3. Thoát.                      |")
    print("---------------------------------")

    return input("Chọn chức năng (1-3): ")

#================================================================================================================================================
SMM_sys = SportMatchManager()

def add(team):
    try:
        amount = int(input("Số lượng thành viên muốn thêm (Chỉ từ 5 đến 11 thành viên): "))
    except ValueError:
        print("Số lượng người không hợp lệ. (Vui lòng nhập số)")
        return
    if (amount<5 or amount>11) or ((team.get_total_players() + amount) > 11):
        print("Số lượng thành viên không hợp lệ/vượt quá giới hạn. (Chỉ từ 5 đến 11 thành viên)")
        return

    for i in range(amount):
        player_id = input("Nhập mã cầu thủ: ")
        if any(player_id == str(p.player_id) for p in team.players):
            print("ID người chơi này đã tồn tại trong đội.")
            continue

        player_name = input("Nhập tên cầu thủ: ")
        player_number = input("Nhập số áo cầu thủ: ")
        player_position = input("Vị trí thi đấu: ")
        day_ob = input("Ngày sinh (Năm-Tháng-Ngày): ")
        performance_score = input("Điểm phong độ (Số thực): ")

        counter = 0
        try:
            team.add_player(Player(player_id, player_name, player_number, player_position, day_ob, performance_score))
            counter += 1
        except ValueError as e:
            print(f"Lỗi khi thêm thành viên: {e}")
            continue
    print("Lập đội thành công.")
    print(f"Đã thêm {counter} thành viên vào đội.")
    time.sleep(0.5)

#================================================================================================================================================

while True:
    choice = menu()
    if choice == "1":
        def Team_Management():
            print("|======== Quản Lý Đội ========|")
            print("|1. Tạo đội mới.              |")
            print("|2. Danh sách các đội.        |")
            print("|3. Thêm thành viên.          |")
            print("|4. Xóa thành viên. (Bằng ID) |")
            print("|5. Quay về.                  |")
            print("|=============================|")

            return input("Chọn chức năng (1-4): ")

        while True:
            user_team_choice = Team_Management()

            #--------------------------------------------------------------------------------------------------
            if user_team_choice == "1":
                team_id = input("Nhập ID đội: ")
                # for team in SMM_sys.teams:
                #     if team_id == str(team.team_id):
                #         print("ID này đã tồn tại.")
                #         time.sleep(0.5)
                #         continue
                if any(team_id == str(team.team_id) for team in SMM_sys.teams):
                    print("ID này đã tồn tại.")
                    time.sleep(0.5)
                    continue
                team_name = input("Nhập tên đội: ")
                coach = input("Nhập tên huấn luyện viên: ")
                try:
                    new_team = Team(team_id, team_name, coach)
                except ValueError as e:
                    print(f"Lỗi khi thêm đội: {e}")
                    continue

                add(new_team)
            #--------------------------------------------------------------------------------------------------
            elif user_team_choice == "2":
                if not SMM_sys.teams:
                    print("Danh sách rỗng")
                    continue
                print("----- Danh sách các đội -----")
                for i,team in enumerate(SMM_sys.teams,1):
                    print(f"{i}. ID: {team.team_id} | Tên: {team.name} | HLV: {team.coach}")
                input(">")
            #--------------------------------------------------------------------------------------------------
            elif user_team_choice == "3":
                teamadd_id = input("Nhập ID đội muốn thêm thành viên: ")
                try:
                    team_to_add = SMM_sys.get_team_by_id(teamadd_id)
                except ValueError as e:
                    print(f"Lỗi khi tìm đội cùng ID: {e}")
                    continue

                add(team_to_add)
            #--------------------------------------------------------------------------------------------------
            elif user_team_choice == "4":
                teamrem_id = input("Nhập ID đội muốn xóa thành viên: ")
                try:
                    team_to_rem = SMM_sys.get_team_by_id(teamrem_id)
                except ValueError as e:
                    print(f"Lỗi khi tìm đội cùng ID: {e}")
                    continue
                playerrem_id = input("Nhập ID thành viên muốn xóa: ")
                try:
                    team_to_rem.remove_player(playerrem_id)
                except ValueError as e:
                    print(f"Lỗi khi xóa thành viên: {e}")
            #--------------------------------------------------------------------------------------------------
            elif user_team_choice == "5":
                print("Quay về màn hình chính...")
                break

#================================================================================================================================================
    elif choice == "2":
        def Match_Management():
            print("|====== Quản Lý Trận Đấu ======|")
            print("|1. Lập trận đấu mới.          |")
            print("|2. Thêm sự kiện ghi bàn.      |")
            print("|3. Hiển thị sự kiện.          |")
            print("|4. Quay về.                   |")
            print("|==============================|")

            return input("Chọn chức năng (1-4): ")

        while True:
            user_match_choice = Match_Management()

            #--------------------------------------------------------------------------------------------------
            if user_match_choice == "1":
                id_match = input("Nhập ID trận đấu mới: ")
                team1_id = input("Nhập ID đội 1: ")
                team2_id = input("Nhập ID đội 2: ")
                match_date = input("Ngày tổ chức: ")
                match_location = input("Địa điểm tổ chức: ")

                try:
                    SMM_sys.schedule_match(Match(id_match, SMM_sys.get_team_by_id(team1_id), SMM_sys.get_team_by_id(team2_id), match_date, match_location))
                except ValueError as e:
                    print(f"Lỗi khi thêm trận đấu: {e}")
                    continue
                print("Đã thêm trận đấu.")
                time.sleep(0.5)
            #--------------------------------------------------------------------------------------------------
            if user_match_choice == "2":
                match = input("Nhập ID trận đấu muốn thêm sự kiện: ")
                print("Đang tìm kiếm...")
                time.sleep(0.5)

                found = False
                for m in SMM_sys.matches:
                    if str(m.match_id) == match:
                        print("Đã tìm thấy trận đấu.")
                        found = True
                        time.sleep(0.2)
                        m.print_match_summary()
                        time = input("Nhập thời gian ghi bàn (Phút): ")
                        score_team = input("Nhập đội ghi bàn (1 hoặc 2): ")
                        while score_team not in ["1","2"]:
                            print()
                            print(f"Lựa chọn không hợp lệ, vui lòng nhập 1 hoặc 2.")
                            score_team = input("Nhập đội ghi bàn (1 hoặc 2): ")
                        score_type = input("Nhập loại ghi bàn: ")
                        points = input("Nhập số điểm: ")
                        try:
                            m.add_score_event(ScoreEvent(time, score_team, score_type, points))
                            print("Đã thêm sự kiện ghi bàn.")
                        except ValueError as e:
                            print(f"Lỗi khi thêm sự kiện: {e}")
                        break

                if not found:
                    print("Không tìm thấy trận đấu")
                time.sleep(0.5)
            #--------------------------------------------------------------------------------------------------
            if user_match_choice == "3":
                match = input("Nhập ID trận đấu muốn hiển thị: ")
                print("Đang tìm kiếm...")
                time.sleep(0.5)
                found = False
                for m in SMM_sys.matches:
                    if str(m.match_id) == match:
                        print("Đã tìm thấy trận đấu.")
                        found = True
                        time.sleep(0.2)
                        for event in m.score_events:
                            event.get_description()
                if found:
                    input(">")
                else:
                    print("Không tìm thấy trận đấu")
                time.sleep(0.5)

#================================================================================================================================================
    elif choice == "3":
        print("Đang thoát chương trình...")
        break

#================================
    else:
        print("Không hợp lệ.")
        time.sleep(0.5)
        continue