def get_non_empty_input(prompt):
    """빈 입력을 막는 함수"""
    while True:
        value = input(prompt).strip()
        if len(value) > 0:
            return value
        print("⚠️ 빈 값은 입력할 수 없습니다.")

def register_lion(lion_list):
    """아기사자 등록"""
    print("\n[ 아기 사자 등록 ]")
    name = get_non_empty_input("✏️ 이름: ")
    track = get_non_empty_input("✏️ 트랙 (예: 백엔드, 프론트엔드): ")
    cohort = get_non_empty_input("✏️ 기수: ")
    
    # 딕셔너리 형태로 리스트에 추가
    lion_list.append({"name": name, "track": track, "cohort": cohort})
    print(f"✅ '{name}' 이(가) 성공적으로 등록되었습니다.")

def search_by_name(lion_list):
    """이름으로 검색"""
    print("\n[ 이름으로 검색 ]")
    if not lion_list: # 빈 리스트 방어
        print("⚠️ 등록된 아기 사자가 없습니다.")
        return
        
    search_name = get_non_empty_input("🔍 검색할 이름을 입력하세요: ")
    
    found = False
    for lion in lion_list:
        if lion["name"] == search_name:
            print(f"🦁 이름: {lion['name']}, 트랙: {lion['track']}, 기수: {lion['cohort']}")
            found = True
            
    if not found:
        print("⚠️ 일치하는 이름이 없습니다.")

def filter_by_track(lion_list):
    """트랙별 조회"""
    print("\n[ 트랙별 조회 ]")
    if not lion_list: # 빈 리스트 방어
        print("⚠️ 등록된 아기 사자가 없습니다.")
        return
        
    search_track = get_non_empty_input("🔍 조회할 트랙을 입력하세요: ")
    
    found = False
    for lion in lion_list:
        if lion["track"] == search_track:
            print(f"🦁 이름: {lion['name']}, 트랙: {lion['track']}, 기수: {lion['cohort']}")
            found = True
            
    if not found:
        print("⚠️ 해당 트랙에 등록된 아기 사자가 없습니다.")

def show_menu():
    """메뉴 출력"""
    print("\n" + "="*30)
    print("🦁 아기 사자 관리 프로그램 🦁")
    print("1. 아기 사자 등록")
    print("2. 이름으로 검색")
    print("3. 트랙별 조회")
    print("4. 프로그램 종료")
    print("="*30)

# 메인 로직 시작
lion_list = []

while True:
    show_menu()
    choice = input("선택: ").strip()

    if choice == '1':
        register_lion(lion_list)
    elif choice == '2':
        search_by_name(lion_list)
    elif choice == '3':
        filter_by_track(lion_list)
    elif choice == '4':
        print("\n📌 프로그램을 종료합니다.")
        break
    else:
        # 잘못된 입력 방어
        print("⚠️ 잘못된 입력입니다. 1~4 사이의 번호를 선택해주세요.")