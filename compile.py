

class Some_class:
    def __init__(self, n):
        self.last_number = n
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.last_number:
            self.num += 1
            return self.num - 1
        raise StopIteration


a = Some_class(6)
for i in a:
    print(i)


