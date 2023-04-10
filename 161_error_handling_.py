# Error Handling:

while True:  # need to use a loop, otherwise the code will stop and user will not be able to enter a number
    try:
        # note: if I don't use except, the int(input('string')) would give me an error because, I am trying to convert a string to an int!
        age = int(input('what is your age?'))
        10/age
    except ValueError:
        print('please, enter a number')
        continue
    except ZeroDivisionError:
        print('please, enter age higher than 0')
        break
    else:
        print('Thank you!')
        break  # need to add break to stop running the loop after a number is added!

    finally:
        print('ok, I am finally done') #finally runs at the end no matter what! Useful for example in 
    print('can you hear me?')