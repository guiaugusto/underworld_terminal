class Character():

    def __init__(self):
        self.name = self.get_username()
        self.level = 1
        self.hp = 0
        self.mp = 0
        self.sp = 0

        # Attributes
        self.strength = 0
        self.constitution = 0
        self.dexterity = 0
        self.agility = 0
        self.intelligence = 0
        self.perception = 10
        self.charisma = 10

    def get_username(self):
        """
        Method to get username of character.
        """

        name = input('Insira o nome do personagem: ')

        return name
