#UDEMY 197;
#THIS FILE WAS CREATED FOR THE TEST.PY - TESTING!!!
#initially we started with simple code like:
# def do_stuff(num)
#   return int(num) + 5
# Can keep adding to the code until has no errors anymore

def do_stuff(num):
    try:
        return int(num) + 5
    except ValueError as err:
        return err
