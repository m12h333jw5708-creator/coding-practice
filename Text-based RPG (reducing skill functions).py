import random
import copy

#플레이어 클래스
class Player:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.player_class = "none"
        self.level = 1
        self.exp = 0
        self.max_hp = 100
        self.hp = 100
        self.mp = 100
        self.atk = 0
        self.def_stat = 0
        self.gold = 0
        self.skill = "none"
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
        print(f"Skill: {self.skill}")
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
                self.max_hp = 150
                self.hp = 150
                self.mp = 50
                self.atk = 25
                self.def_stat = 20
                self.skill = "Steel Strike"
                self.gear = "Rusty Sword"
                print("You became a Warrior!")
                break
            elif choice == "2":
                self.player_class = "Mage"
                self.max_hp = 80
                self.hp = 80
                self.mp = 180
                self.atk = 35
                self.def_stat = 8
                self.skill = "Fireball"
                self.gear = "Wooden Staff"
                print("You became a Mage!")
                break
            elif choice == "3":
                self.player_class = "Rogue"
                self.max_hp = 110
                self.hp = 110
                self.mp = 80
                self.atk = 30
                self.def_stat = 12
                self.gear = "Old Dagger"
                self.skill = "Shadow Stab"
                print("You became a Rogue!")
                break
            else :
                print("Invalid choice!")
    def level_up(self):
        while self.exp >= 100:
            if self.exp >= 100:
                self.exp = (player.exp - 100)
                self.level += 1
                self.hp += 15
                self.max_hp += 15
                self.mp += 15
                self.atk += 3
                self.def_stat += 3
                print("=====================")
                print("level up!!")
                print(f"now your level is : {player.level}!!")
    def heal(self):
        if self.hp < self.max_hp:
            self.hp = self.max_hp
            print("I've recovered my strength")
#몬스터 클래스
class Monster:
    def __init__(self, name, hp, atk, def_stat, exp, gold):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.def_stat = def_stat
        self.exp = exp
        self.gold = gold

#슬라임 구현
green_slime = Monster("Green Slime", 30, 5, 2, 10, 5)
blue_slime = Monster("Blue Slime", 50, 7, 4, 18, 8)
red_slime = Monster("Red Slime", 35, 12, 3, 22, 10)
yellow_slime = Monster("Yellow Slime", 45, 10, 6, 30, 15)
poison_slime = Monster("Poison Slime", 60, 9, 5, 40, 20)
dark_slime = Monster("Dark Slime", 90, 15, 8, 70, 35)
metal_slime = Monster("Metal Slime", 40, 8, 25, 100, 50)
king_slime = Monster("King Slime", 300, 25, 15, 300, 150)

#고블린 구현
goblin = Monster("Goblin", 60, 12, 5, 50, 25)
goblin_archer = Monster("Goblin Archer", 50, 18, 3, 70, 35)
goblin_warrior = Monster("Goblin Warrior", 90, 20, 10, 100, 50)
goblin_chief = Monster("Goblin Chief", 180, 30, 15, 200, 100)

#늑대 구현
wild_wolf = Monster("Wild Wolf", 70, 15, 6, 60, 30)
gray_wolf = Monster("Gray Wolf", 100, 22, 8, 90, 45)
dire_wolf = Monster("Dire Wolf", 150, 30, 12, 150, 80)
alpha_wolf = Monster("Alpha Wolf", 250, 40, 18, 250, 150)

#오크 구현
orc = Monster("Orc", 180, 25, 15, 150, 80)
orc_warrior = Monster("Orc Warrior", 250, 35, 20, 220, 120)
orc_berserker = Monster("Orc Berserker", 220, 50, 10, 300, 180)
orc_king = Monster("Orc King", 500, 60, 30, 600, 400)

slime_list = [green_slime, blue_slime, red_slime, yellow_slime, poison_slime, dark_slime, metal_slime, king_slime]
goblin_list = [goblin, goblin_archer, goblin_warrior, goblin_chief]
wolf_list = [wild_wolf, gray_wolf, dire_wolf, alpha_wolf]
orc_list = [orc, orc_warrior, orc_berserker, orc_king]


#배틀 함수 구현
def enemy_creation(player, monster_list):
    enemy = copy.copy(random.choice(monster_list))
    print("=====================")
    print(f"{enemy.name} appeared!")
    print("Battle Start!")
    print(f"Monster HP: {enemy.hp}")
    print(f"Player HP: {player.hp}")
    return enemy

def select_player_action():
    while True:
        try:
            print("====== Battle Menu =====")
            print("1. attack")
            print("2. skill")
            print("3. Run away")
            action = int(input("Enter your choice: "))
            if action > 4:
                print("Invalid choice")
            else:
                return action
        except ValueError:
            print("invalid input")

def player_attacks(action, enemy, player):
    if action == 1:
        if (player.atk - enemy.def_stat) <= 0:
            print("Monster's defense is too strong to attack")
            win_or_lose = "continue"
            return win_or_lose
        elif (player.atk - enemy.def_stat) > 0:
            enemy.hp -= (player.atk - enemy.def_stat)
            if enemy.hp <= 0:
                print("Victory!!")
                win_or_lose = "victory"
                return win_or_lose
            elif enemy.hp > 0:
                print(f"Monster's remaining physical strength : {enemy.hp}")
                win_or_lose = "continue"
                return win_or_lose


def player_skill(action, enemy, player):
    if action == 2:
        if player.skill == "Steel Strike":
            drainage = 1.5
            additional_damage = 10
        elif player.skill == "Fireball":
            drainage = 1.8
            additional_damage = 20
        elif player.skill == "Shadow Stab":
            drainage = 2.0
            additional_damage = 0
        def calculation_results(drainage, additional_damage, player, enemy):
            damage = player.atk * drainage + additional_damage - enemy.def_stat
            print(f"you use {player.skill}!!")
            if damage <= 0:
                print("Monster's defense is too strong to skill")
                return "continue"
            else :
                enemy.hp -= damage
                if enemy.hp <= 0:
                    return "Victory"
                elif enemy.hp > 0:
                    print(f"Monster's remaining physical strength : {enemy.hp}")
                    return "continue"
        return calculation_results(drainage, additional_damage, player, enemy)

def monster_attacks(enemy, player):
    if (enemy.atk - player.def_stat) > 0:
        player.hp -= (enemy.atk - player.def_stat)
        if player.hp <= 0:
            print("Defeat")
            win_or_lose = "defeat"
            return win_or_lose
        elif player.hp > 0:
            print(f"player's remaining physical strength : {player.hp}")
            win_or_lose = "continue"
            return win_or_lose
    elif (enemy.atk - player.def_stat) <= 0:
        print("player's defense is too strong to attack")
        win_or_lose = "continue"
        return win_or_lose

def processing_the_outcome_of_the_battle(win_or_lose, enemy, player):
    if win_or_lose == "victory":
        player.exp += enemy.exp
        print(f"EXP +{enemy.exp}")
        player.gold += enemy.gold
        print(f"Gold +{enemy.gold}")
    elif win_or_lose == "defeat":
        pass

def to_run_away(action):
    if action == 3:
        run_way = random.randint(1, 10)
        if run_way > 3:
            print("Run away, successful")
            run_away_result = "success"
            return run_away_result
        else :
            print("Failed to run away!")
            run_away_result = "failure"
            return run_away_result

def battle(player, monster_list):
    enemy = enemy_creation(player, monster_list)

    while True:
        action = select_player_action()
        if action == 1:
            win_or_lose = player_attacks(action, enemy, player)
            if win_or_lose == "victory":
                processing_the_outcome_of_the_battle(win_or_lose, enemy, player)
                break
            elif win_or_lose == "continue":
                a = monster_attacks(enemy, player)
                if a == "defeat":
                    processing_the_outcome_of_the_battle(a, enemy, player)
                    break
        if action == 2:
            win_or_lose = player_skill(action, enemy, player)
            if win_or_lose == "victory":
                processing_the_outcome_of_the_battle(win_or_lose, enemy, player)
                break
            elif win_or_lose == "continue":
                a = monster_attacks(enemy, player)
                if a == "defeat":
                    processing_the_outcome_of_the_battle(win_or_lose, enemy, player)
                    break
        elif action == 3:
            run_away_result = to_run_away(action)
            if run_away_result == "failure":
                monster_attacks(enemy, player)
            elif run_away_result == "success":
                break

#플레이어 생성
player = Player()
player.choose_class()


while True:
    try:
        player.level_up()
        player.heal()
        print("===== Main Menu =====")
        print("1. Enter Dungeon")
        print("2. Check Status")
        print("3. Exit Game")
        print("=====================")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            while True:
                player.heal()
                print("1. slime Dungeon")
                print("2. goblin Dungeon")
                print("3. wolf Dungeon")
                print("4. Orc Dungeon")
                print("5. exit")
                dungeon = input("Enter your Dungeon: ")
                if dungeon == "1":
                    battle(player, slime_list)
                elif dungeon == "2":
                    battle(player, goblin_list)
                elif dungeon == "3":
                    battle(player, wolf_list)
                elif dungeon == "4":
                    battle(player, orc_list)
                elif dungeon == "5":
                    break
                else :
                    print("Invalid choice!")
        elif choice == 2:
            player.show_status()
        elif choice == 3:
            print("Shut down the game.")
            break
        else :
            print("Invalid choice!")
    except ValueError:
        print("Invalid choice!")