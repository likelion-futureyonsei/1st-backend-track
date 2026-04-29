class Member:
    def __init__(self, name, track, generation):
        if name == "":
            raise ValueError("이름은 비어 있을 수 없습니다.")
        if track == "":
            raise ValueError("트랙은 비어 있을 수 없습니다.")
        if generation == "":
            raise ValueError("기수는 비어 있을 수 없습니다.")

        self.name = name
        self.track = track
        self.generation = generation

    def get_role(self):
        return "멤버"


class Lion(Member):
    def get_role(self):
        return "아기사자"


class Staff(Member):
    def get_role(self):
        return "운영진"


class SimplePrinter:
    def print_members(self, members):
        print("\n📋 멤버 목록")

        if len(members) == 0:
            print("등록된 멤버가 없습니다.")
            return

        for i in range(len(members)):
            member = members[i]
            print(
                member.get_role() + " : "
                + member.name + " | "
                + member.track + " | "
                + member.generation + "기"
            )


class NameSorter:
    def sort(self, members):
        return sorted(members, key=lambda member: member.name)


class GenerationSorter:
    def sort(self, members):
        return sorted(members, key=lambda member: member.generation)


class MemberManager:
    def __init__(self, printer, sorter):
        self.members = []
        self.printer = printer
        self.sorter = sorter

    def add_member(self, member):
        self.members.append(member)

    def show_members(self):
        sorted_members = self.sorter.sort(self.members)
        self.printer.print_members(sorted_members)


def input_member_info():
    name = input("이름: ").strip()
    track = input("트랙: ").strip()
    generation = input("기수: ").strip()

    return name, track, generation


def main():
    printer = SimplePrinter()
    sorter = NameSorter()
    manager = MemberManager(printer, sorter)

    while True:
        print("\n🦁 아기사자 관리 프로그램")
        print("1. 아기사자 등록")
        print("2. 운영진 등록")
        print("3. 명단 출력")
        print("4. 종료")

        choice = input("기능을 선택하세요: ").strip()

        if choice == "1":
            try:
                name, track, generation = input_member_info()
                lion = Lion(name, track, generation)
                manager.add_member(lion)
                print("✅ 아기사자가 등록되었습니다.")
            except ValueError as error:
                print("⚠️ " + str(error))

        elif choice == "2":
            try:
                name, track, generation = input_member_info()
                staff = Staff(name, track, generation)
                manager.add_member(staff)
                print("✅ 운영진이 등록되었습니다.")
            except ValueError as error:
                print("⚠️ " + str(error))

        elif choice == "3":
            manager.show_members()

        elif choice == "4":
            print("프로그램을 종료합니다.")
            break

        else:
            print("⚠️ 잘못된 선택입니다.")


main()