def get_non_empty_input(prompt):
    
    while True:
        value = input(prompt).strip()
        if len(value) > 0:
            return value
        
        print("⚠️ 이름이 비어있습니다. 다시 입력해주세요.")

print("🦁 아기 사자 명단 관리 프로그램입니다.")
lion_list = []

while True:
    
    name = get_non_empty_input("✏️ 아기 사자 이름을 입력하세요 (종료하려면 q 입력): ")
    
    if name == 'q':
        print("\n📌 이름 입력을 종료합니다.\n")
        break
        
    lion_list.append(name)
    print(f"✅ '{name}' 이(가) 등록되었습니다.")

print("📋 현재 아기 사자 명단입니다.")
for i, lion in enumerate(lion_list, 1):
    print(f"🦁 {i}. {lion}")