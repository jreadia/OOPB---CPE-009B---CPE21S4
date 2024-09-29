from Character import Character

class Novice(Character):
    def basicAttack(self, character):
        character.reduceHp(self.getDamage())
        print(f"{self.getUsername()} performed Basic Attack! - {self.getDamage()}")


# # Testing
# character1 = Novice("Pablo")
# print(character1.getUsername())
# print(character1.getHp())