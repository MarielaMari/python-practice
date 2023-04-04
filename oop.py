# OOP

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name #attributes, unique, dynamic
        self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter("Cindy", 33)
player2 = PlayerCharacter("Tommy", 26)
print()
print(player1)
print(player2)
