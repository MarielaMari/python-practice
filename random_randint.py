from random import randint

# create random number from 1 to 10

answer = randint(1, 10)
print(answer)
# user to guess a number from 1 to 10 and guess the answer
# keep playing until the number is guessed

while True:
    try:
        guess = int(input('Please, guess number from 1 to 10: '))
        if 0<guess<11:
            if guess == answer:
                print(' YOU WIN!!! ')
                break
        else:
            print('I said a NUMBER between 1 and 10!')

    except ValueError:
        print('please, enter a NUMBER.')
        continue
