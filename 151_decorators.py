# Decorators look lie: @
# FUNCTIONS in python act like VARIABLES do! So, decorators are possible exactly because Functions act like Variables
def hello():
    print("helloooo")


greet = hello
print(greet())
