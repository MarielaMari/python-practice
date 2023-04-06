# Dunder Methods
# Do not modify
# Only somethimes, when you really need to, you can do so!
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):  # sometimes we need to modify a dunder method
        return 5

    def __call__(self):  # note: __call__ is used under the hood to call a function!
        return ('yess??')

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])
