# Can run it from the terminal with this command: python 175_random_game.py 1 2
from random import randint
import sys
# Generate a number from 1 to 10


def random_game(guess):
    answer = randint(int(sys.argv[1]), int(sys.argv[2]))

# input from user?

# check that the input is a number from 1 to 10

    while True:
        try:
            # print(answer)
            guess = int(input(f'guess a number from 1 to 10: '))
            if 0 < guess < 11:
                if guess == answer:
                    print('You are genius!')
                    break
            else:
                print('hey, bozo I said 1 to 10')
        except ValueError:
            print('please, enter a number')
            continue
# check if the number is the right guess; otherwise- ask again
