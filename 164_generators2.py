# Generators are iterable (using __iter__ or iterate under the hood), but NOT all iterable are generators!
# for example, range is generator and it is iterable, but list is iterable but it is not a generator!


def generator_function():
    for i in range(100):
        yield i  # using it instead of return and append from the code above

        # Yield pauses the function
g = generator_function(100)
next(g)
next(g)
print(next(g))
