class Character():
    def __init__(self, username):
        self.__username = username
        self.__hp = 100
        self.__mana = 100
        self.__damage = 5
        self.__str = 0 # Strength stat
        self.__vit = 0 # Vitality stat
        self.__int = 0 # Intelligence stat
        self.__agi = 0 # Agility stat

    # Username Getter and Setter
    def getUsername(self):
        return self.__username
    def setUsername(self, new_username):
        self.__username = new_username

    # HP Getter and Setter
    def getHp(self):
        return self.__hp
    def setHp(self, new_hp):
        self.__hp = new_hp

    # Damage Getter and Setter
    def getDamage(self):
        return self.__damage
    def setDamage(self, new_damage):
        self.__damage = new_damage

    # Strength Getter and Setter
    def getStr(self):
        return self.__str
    def setStr(self, new_str):
        self.__str = new_str

    # Vitality Getter and Setter
    def getVit(self):
        return self.__vit
    def setVit(self, new_vit):
        self.__vit = new_vit

    # Intelligence Getter and Setter
    def getInt(self):
        return self.__int
    def setInt(self, new_int):
        self.__int = new_int

    # Agility Getter and Setter
    def getAgi(self):
        return self.__agi
    def setAgi(self, new_agi):
        self.__agi = new_agi

    # Reduce or increase HP
    def reduceHp(self, damage_amount):
        self.__hp = self.__hp - damage_amount
    def addHp(self, heal_amount):
        self.__hp = self.__hp + heal_amount

# # Testing
# character1 = Character("Pablo")
# print(character1.__username)
# print(character1.getUsername())