#You always want to give meaningful errors to your users.

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'please, enter numbers {err}')


print(sum('1', 2))
