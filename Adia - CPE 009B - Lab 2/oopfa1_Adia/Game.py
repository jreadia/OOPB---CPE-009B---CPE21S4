import random

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

class Novice(Character):
    def __init__(self, name):
        super().__init__(name, 100, 10)

class Swordsman(Character):
    def __init__(self, name):
        super().__init__(name, 150, 20)

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 120, 15)

class Magician(Character):
    def __init__(self, name):
        super().__init__(name, 100, 25)

class Monster(Character):
    def __init__(self):
        super().__init__("Monster", 200, 15)

class Game:
    def __init__(self):
        self.player1_wins = 0
        self.player2_wins = 0

    def select_role(self, player_name, is_novice=False):
        if is_novice:
            return Novice(player_name)
        roles = {
            '1': Swordsman,
            '2': Archer,
            '3': Magician
        }
        print(f"Select role for {player_name}:")
        print("1. Swordsman")
        print("2. Archer")
        print("3. Magician")
        choice = input("Enter choice: ")
        return roles[choice](player_name)

    def single_player_mode(self):
        player = self.select_role("Player", is_novice=True)
        wins = 0
        while True:
            monster = Monster()
            if self.battle(player, monster):
                wins += 1
                if wins == 2:
                    print("You can now select a new role!")
                    player = self.select_role("Player")
            else:
                break

    def player_vs_player_mode(self):
        player1 = self.select_role("Player 1")
        player2 = self.select_role("Player 2")
        self.battle(player1, player2)

    def battle(self, player1, player2):
        players = [player1, player2]
        random.shuffle(players)
        while player1.is_alive() and player2.is_alive():
            attacker = players.pop(0)
            defender = players[0]
            damage = attacker.attack
            defender.take_damage(damage)
            print(f"{attacker.name} attacks {defender.name} for {damage} damage.")
            print(f"{defender.name} has {defender.hp} HP left.")
            players.append(attacker)
        if player1.is_alive():
            print(f"{player1.name} wins!")
            self.player1_wins += 1
            return True
        else:
            print(f"{player2.name} wins!")
            self.player2_wins += 1
            return False

    def start(self):
        while True:
            print("Select game mode:")
            print("1. Single Player")
            print("2. Player vs Player")
            print("3. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                self.single_player_mode()
            elif choice == '2':
                self.player_vs_player_mode()
            elif choice == '3':
                print("Exiting game.")
                break
            else:
                print("Invalid choice. Exiting game.")
                break

if __name__ == "__main__":
    game = Game()
    game.start()