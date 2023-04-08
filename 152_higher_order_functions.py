# Higher Order Function HOC
# A function that accepts in its parameters another function
# A function that returns another function

def higher_order_function(function):
    function()


def hoc2():
    def function():
        return 5
    return function
