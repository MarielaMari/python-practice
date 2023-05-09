def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            next(iterator)
        except StopIteration:
            break


special_for([1, 2, 3])


#How does RANGE works under the hood

class myGen():
    def __init__(self, first, last):
        self.first = first
        self.last = last