class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age


player1 = PlayerCharacter('Mari', 199)
print(player1.name)
print(player1.age)

# Dictionary would give you the same output... so, learn how to use classes!
player2 = {'name': 'Mari', 'age': 199}
print(player2['name'])
print(player2['age'])
