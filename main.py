#UDEMY 197;
#THIS FILE WAS CREATED FOR THE TEST.PY - TESTING!!!
#initially we started with simple code like:
# def do_stuff(num)
#   return int(num) + 5
# Can keep adding to the code until has no errors anymore

def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return '_please, enter a number_'
    except ValueError as err:
        return err
