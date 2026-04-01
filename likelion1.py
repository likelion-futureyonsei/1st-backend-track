members = []

print("🦁 아기 사자 명단 관리 프로그램입니다.")

while True:
    member = input("✏️  아기 사자 이름을 입력하세요 (종료하려면 q 입력):")
    if member == 'q' :
        print("\n 📌 이름 입력을 종료합니다.")
        break
    elif member .strip() == "" : 
        print("⚠️  이름이 비어있습니다. 다시 입력해주세요.")
    else :
        members.append(member)
        print(f"✅ '{member}' 이(가) 등록되었습니다.")


print("\n📋 현재 아기 사자 명단입니다.")

i = 1
for member in members:
    print("🦁", i,".", member)
    i += 1