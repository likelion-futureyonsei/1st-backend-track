print ("🦁 아기 사자 명단 관리 프로그램입니다.")

baby_lions = []

while True:
    name = input ("✏️  아기 사자 이름을 입력하세요 (종료하려면 q 입력): ")
    if name == "q":
        print ("\n📌  이름 입력을 종료합니다.")
        break
    elif name == "":
        print ("⚠️  이름이 비어있습니다. 다시 입력해주세요.")
    else :
        baby_lions.append(name)
        print (f"✅  '{name}' 이(가) 등록되었습니다.")

print("\n📋 현재 아기 사자 명단입니다.")
for i, lion in enumerate(baby_lions, start=1):
    print(f"🦁  {i}. {lion}")