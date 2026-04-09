def get_non_empty_input(prompt):
    """빈 입력을 막는 함수"""
    while True:
        value = input(prompt).strip()
        if len(value) > 0:
            return value
        print("⚠️ 빈 값은 입력할 수 없습니다.")

def register_lion(lion_list):
    """아기사자 등록"""
    # TODO: 이름, 트랙, 기수를 입력받아 dict로 lion_list에 추가
    name = get_non_empty_input("이름: ")
    track = get_non_empty_input("트랙: ")
    generation = get_non_empty_input("기수: ")

    lion = {
        "name": name,
        "track": track,
        "generation": generation
    }

    lion_list.append(lion)
    print("아기사자가 등록되었습니다.")

def search_by_name(lion_list):
    """이름으로 검색"""
    # TODO: 빈 리스트 방어 → 이름 입력 → 순회하며 검색 → 결과 출력
    if len(lion_list) == 0:
        print("등록된 아기사자가 없습니다.")
        return

    name = get_non_empty_input("검색할 이름: ")
    found = False

    for lion in lion_list:
        if lion["name"] == name:
            print("이름:", lion["name"])
            print("트랙:", lion["track"])
            print("기수:", lion["generation"])
            found = True
            break

    if found == False:
        print("해당 이름의 아기사자를 찾을 수 없습니다.")

def filter_by_track(lion_list):
    """트랙별 조회"""
    # TODO: 빈 리스트 방어 → 트랙 입력 → 해당 트랙만 모아서 출력
    if len(lion_list) == 0:
        print("등록된 아기사자가 없습니다.")
        return

    track = get_non_empty_input("조회할 트랙: ")
    filtered_lions = []

    for lion in lion_list:
        if lion["track"] == track:
            filtered_lions.append(lion)

    if len(filtered_lions) == 0:
        print("해당 트랙의 아기사자가 없습니다.")
    else:
        for lion in filtered_lions:
            print("이름:", lion["name"])
            print("트랙:", lion["track"])
            print("기수:", lion["generation"])
            print()

def show_menu():
    """메뉴 출력"""
    # TODO: 메뉴 번호와 기능명 출력
    print("\n===== 아기사자 관리 프로그램 =====")
    print("1. 아기사자 등록")
    print("2. 이름으로 검색")
    print("3. 트랙별 조회")
    print("4. 종료")
lion_list = []

while True:
    show_menu()
    choice = input("선택: ")
    # TODO: choice에 따라 적절한 함수 호출
    # TODO: 잘못된 입력은 else로 방어

    if choice == "1":
        register_lion(lion_list)
    elif choice == "2":
        search_by_name(lion_list)
    elif choice == "3":
        filter_by_track(lion_list)
    elif choice == "4":
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 번호를 입력하세요.")