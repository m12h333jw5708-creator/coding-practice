#플레이어 클래스
class Player:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.player_class = "none"
        self.level = 1
        self.exp = 0
        self.hp = 100
        self.mp = 100
        self.atk = 0
        self.def_stat = 0
        self.gold = 0
        self.gear = "none"
    def show_status(self):
        print("===== STATUS =====")
        print(f"Name: {self.name}")
        print(f"Class: {self.player_class}")
        print(f"Level: {self.level}")
        print(f"Exp: {self.exp}")
        print(f"HP: {self.hp}")
        print(f"MP: {self.mp}")
        print(f"Atk: {self.atk}")
        print(f"Def: {self.def_stat}")
        print(f"Gold: {self.gold}")
        print(f"Gear: {self.gear}")
        print("==================")
    def choose_class(self):
        print(f"Name: {self.name}")
        print("Choose your class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Rogue")
        while True:
            choice = input("Enter your choice: ")
            if choice == "1":
                self.player_class = "Warrior"
                self.hp = 150
                self.mp = 50
                self.atk = 25
                self.def_stat = 20
                self.gear = "Rusty Sword"
                print("You became a Warrior!")
                break
            elif choice == "2":
                self.player_class = "Mage"
                self.hp = 80
                self.mp = 180
                self.atk = 35
                self.def_stat = 8
                self.gear = "Wooden Staff"
                print("You became a Mage!")
                break
            elif choice == "3":
                self.player_class = "Rogue"
                self.hp = 110
                self.mp = 80
                self.atk = 30
                self.def_stat = 12
                self.gear = "Old Dagger"
                print("You became a Rogue!")
                break
            else :
                print("Invalid choice!")