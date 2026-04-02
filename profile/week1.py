def get_non_empty_input(prompt):
    """빈 입력을 막는 함수"""
    while True:
        value = input(prompt).strip()
        if len(value) > 0:
            return value
        # 템플릿의 오류 메시지를 사진 조건에 맞게 수정
        print("⚠️ 이름이 비어있습니다. 다시 입력해주세요.")

print("🦁 아기 사자 명단 관리 프로그램입니다.")
lion_list = []

while True:
    # 템플릿의 함수를 활용해 빈 입력을 안전하게 방어
    name = get_non_empty_input("✏️ 아기 사자 이름을 입력하세요 (종료하려면 q 입력): ")
    
    if name == 'q':
        print("\n📌 이름 입력을 종료합니다.\n")
        break
        
    lion_list.append(name)
    print(f"✅ '{name}' 이(가) 등록되었습니다.")

print("📋 현재 아기 사자 명단입니다.")
for i, lion in enumerate(lion_list, 1):
    print(f"🦁 {i}. {lion}")