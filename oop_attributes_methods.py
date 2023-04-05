# OOP

class PlayerCharacter:
    # Class Object Attribute- it is not dynamic, it is static. This is the difference from the attributes below
    membership = True

    # stick with the convention of using the name __init__ for the initialization method of a class, to ensure that other developers can easily understand and use your code.
    def __init__(self, name, age):

        if (self.membership):
            self.name = name  # attributes, unique, dynamic
            self.age = age

    def shout(self):
        # print('run')
        # return 'done'
        print(f'My name is {self.name}')


@classmethod
def adding_things(num1, num2):
    return num1+num2


player1 = PlayerCharacter("Cindy", 33)
player2 = PlayerCharacter("Tommy", 26)
player2.attack = 50
print()
print(player1)
print(PlayerCharacter.membership)
