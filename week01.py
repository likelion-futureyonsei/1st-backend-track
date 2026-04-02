lion_list=[]
print("아기사자 명단 관리 프로그램입니다.")

for _ in range(25):
    name=input("이름을 입력하세요.(종료하려면 q 입력): ")
    if name == 'q':
        print("이름 입력을 종료합니다.")
        break
    if name.strip()=="":
        print("이름이 비었습니다. 다시 입력해주세요.")
        continue
    lion_list.append(name)
    print(f"'{name}'이(가) 등록되었습니다.")

print("\n현재 아기사자 명단입니다.")

for i in range(len(lion_list)):
    print(f"{i+1}. {lion_list[i]}")