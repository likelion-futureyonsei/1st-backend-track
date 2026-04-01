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
    pass

def search_by_name(lion_list):
    """이름으로 검색"""
    # TODO: 빈 리스트 방어 → 이름 입력 → 순회하며 검색 → 결과 출력
    pass

def filter_by_track(lion_list):
    """트랙별 조회"""
    # TODO: 빈 리스트 방어 → 트랙 입력 → 해당 트랙만 모아서 출력
    pass

def show_menu():
    """메뉴 출력"""
    # TODO: 메뉴 번호와 기능명 출력
    pass

lion_list = []

while True:
    show_menu()
    choice = input("선택: ")

    # TODO: choice에 따라 적절한 함수 호출
    # TODO: 잘못된 입력은 else로 방어

    pass