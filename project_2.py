class Member:
    def __init__(self, name):
        if not name:
            raise ValueError("이름은 비어 있을 수 없습니다.")
        self.name = name

    def get_role(self):
        raise NotImplementedError()

    def to_string(self):
        raise NotImplementedError()


class Lion(Member):
    def __init__(self, name, track, gen):
        super().__init__(name)

        if not track:
            raise ValueError("트랙은 비어 있을 수 없습니다.")
        if not gen:
            raise ValueError("기수는 비어 있을 수 없습니다.")

        self.track = track
        self.gen = gen

    def get_role(self):
        return "🦁 아기사자"

    def to_string(self):
        return f"- {self.get_role()} : {self.name} | {self.track} | {self.gen}"


class Staff(Member):
    def __init__(self, name):
        super().__init__(name)

    def get_role(self):
        return "🧑‍🏫 운영진"

    def to_string(self):
        return f"- {self.get_role()} : {self.name} | 운영진"

class MemberPrinter:
    @staticmethod
    def print_all(member_list):
        if not member_list:
            print("⚠️ 등록된 멤버가 없습니다.")
            return

        print("\n📋 멤버 목록")
        for m in member_list:
            print(m.to_string())


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if len(value) > 0:
            return value
        print("⚠️ 빈 값은 입력할 수 없습니다.")


def register_lion(member_list):
    try:
        name = get_non_empty_input("🦁 이름을 입력하세요: ")
        track = get_non_empty_input("📚 트랙을 입력하세요: ")
        gen = get_non_empty_input("🎓 기수를 입력하세요: ")

        lion = Lion(name, track, gen)
        member_list.append(lion)

        print("✅ 아기사자가 등록되었습니다.")

    except ValueError as e:
        print(f"⚠️ {e}")


def register_staff(member_list):
    try:
        name = get_non_empty_input("🧑‍🏫 이름을 입력하세요: ")

        staff = Staff(name)
        member_list.append(staff)

        print("✅ 운영진이 등록되었습니다.")

    except ValueError as e:
        print(f"⚠️ {e}")


def show_menu():
    print("\n📌 기능을 선택하세요")
    print("1️⃣  아기사자 등록")
    print("2️⃣  운영진 등록")
    print("3️⃣  전체 출력")
    print("4️⃣  종료")

member_list = []

while True:
    show_menu()
    choice = input("👉 선택: ")

    if choice == "1":
        register_lion(member_list)
    elif choice == "2":
        register_staff(member_list)
    elif choice == "3":
        MemberPrinter.print_all(member_list)
    elif choice == "4":

        print("👋 프로그램을 종료합니다.")
        break
    else:
        print("⚠️ 잘못된 입력입니다.")