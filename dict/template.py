def get_non_empty_input(prompt):
    # 빈 값 입력 시 
    while True:
        value = input(prompt).strip()
        if len(value) > 0:
            return value
        print("빈 값은 입력할 수 없습니다.")


def register_lion(lion_list):
    # 아기사자 등록
    name = get_non_empty_input("이름: ")
    track = get_non_empty_input("트랙: ")
    gen = get_non_empty_input("기수: ")

    lion = {
        "이름": name,
        "트랙": track,
        "기수": gen
    }

    lion_list.append(lion)
    print(f"{name}님이 등록되었습니다. ")


def search_by_name(lion_list):
    # 이름으로 검색
    if len(lion_list) == 0:
        print("등록된 아기사자가 없습니다.")
        return

    name = get_non_empty_input("검색할 이름 입력: ")
    found = False

    for lion in lion_list:
        if lion["이름"] == name:
            print(f"\n이름: {lion['이름']}\n트랙: {lion['트랙']}\n기수: {lion['기수']}")
            found = True

    if not found:
        print("해당 이름의 아기사자를 찾을 수 없습니다.")


def filter_by_track(lion_list):
    # 트랙별 조회
    if len(lion_list) == 0:
        print("등록된 아기사자가 없습니다.")
        return

    track = get_non_empty_input("조회할 트랙 입력: ")
    filtered = []

    for lion in lion_list:
        if lion["트랙"] == track:
            filtered.append(lion)

    if len(filtered) == 0:
        print("해당 트랙에 등록된 아기사자가 없습니다.")
    else:
        print(f"\n[{track}] 트랙 아기사자 목록")
        for i, lion in enumerate(filtered, 1):
            print(f"{i}. {lion['이름']} ({lion['기수']}기)")


def show_menu():
    # 메뉴 출력
    print("\n기능을 선택하세요")
    print("1. 아기사자 등록")
    print("2. 이름으로 검색")
    print("3. 트랙으로 조회")
    print("4. 종료")


# 메인 실행
lion_list = []

while True:
    show_menu()
    choice = input("\n선택: ").strip()

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
        print("1 ~ 4 중 입력하세요.")