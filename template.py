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
    name =get_non_empty_input("🦁   이름을 입력하세요: ")
    track = get_non_empty_input("📚   트랙을 입력하세요: ")
    gen = get_non_empty_input("🎓   기수를 입력하세요: ")
    lion_list.append({
        "이름": name,
        "트랙": track,
        "기수": gen
    })
    print("✅ '" + name + "' 이(가) 등록되었습니다.")
    print()
    pass

def search_by_name(lion_list):
    """이름으로 검색"""
    # TODO: 빈 리스트 방어 → 이름 입력 → 순회하며 검색 → 결과 출력
    if len(lion_list) == 0:
        print("⚠️ 등록된 아기사자가 없습니다.")
        print()
        return
    
    target_name = get_non_empty_input("🔍 검색할 이름을 입력하세요: ")
    found = False
    
    for lion in lion_list:
        if lion["이름"] == target_name:
            print("이름: " + lion["이름"] + ", 트랙: " + lion["트랙"] + ", 기수: " + lion["기수"])
            found = True
            
    if found == False:
        print("⚠️   해당 이름의 아기사자를 찾을 수 없습니다.")

    print()
    pass

def filter_by_track(lion_list):
    """트랙별 조회"""
    # TODO: 빈 리스트 방어 → 트랙 입력 → 해당 트랙만 모아서 출력
    if len(lion_list) == 0:
        print("등록된 아기사자 없음")
        return
    
    track = get_non_empty_input("📂 조회할 트랙을 입력하세요: ")
    found = False
    
    for lion in lion_list:
        if lion["트랙"] == track:
            print("이름: " + lion["이름"] + ", 트랙: " + lion["트랙"] + ", 기수: " + lion["기수"])
            found = True

    if found == False:
        print("⚠️   해당 트랙의 아기사자가 없습니다.")
    
    print()
    pass

def show_menu():
    """메뉴 출력"""
    # TODO: 메뉴 번호와 기능명 출력
    print("1. 아기사자 등록")
    print("2. 이름으로 검색")
    print("3. 트랙별 조회")
    print("4. 종료")
    pass

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
        print("📌 프로그램을 종료합니다.")
        break
    else:
        print("⚠️ 잘못된 입력입니다.")

    pass