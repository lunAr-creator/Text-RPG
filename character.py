class Character:
    def __init__(self):
        self.health = 0
        self.defense = 0
        self.attack = 0
        self.luck = 0

    def change_health(self, operation, new_value):
        if operation == '-':
            self.health += new_value
        else:
            self.health -= new_value

    def change_defense(self, operation, new_value):
        if operation == '-':
            self.defense += new_value
        else:
            self.defense -= new_value

    def change_attack(self, operation, new_value):
        if operation == '-':
            self.attack += new_value
        else:
            self.attack -= new_value

    def change_luck(self, operation, new_value):
        if operation == '-':
            self.luck += new_value
        else:
            self.luck -= new_value
