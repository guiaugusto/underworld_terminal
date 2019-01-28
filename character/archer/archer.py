import sys
sys.path.append('/underworld/character')
from character import Character

class Archer(Character):

    def __init__(self):
        self.hp = 1000
        self.mp = 150
        self.sp = 20
        self.level_rate = 1.015

        # Attributes
        self.strength = 5
        self.constitution = 2
        self.dexterity = 10
        self.agility = 15
        self.intelligence = 5
        self.perception = 5
        self.charisma = 5

    def normal_simple_attack(self):
        pass

    def special_simple_attack(self):
        pass

    def update_hp_rate(self, level):
        if level > 200 and level < 300:
            self.hp_rate = 1.005
        elif level > 300:
            self.level_rate = 1.0025
