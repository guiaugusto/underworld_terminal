import sys
sys.path.append('/underworld/character')
from character import Character

class Warrior(Character):

    def __init__(self):
        self.hp = 2000
        self.mp = 80
        self.sp = 30
        self.hp_rate = 1.02

        # Attributes
        self.strength = 15
        self.constitution = 7
        self.dexterity = 7
        self.agility = 8
        self.intelligence = 3
        self.perception = 5
        self.charisma = 5

    def normal_simple_attack(self):
        pass

    def special_simple_attack(self):
        pass

    def update_hp_rate(self, level):
        if level > 100 and level < 200:
            self.hp_rate = 1.015
        elif level > 200:
            self.hp_rate = 1.0025
