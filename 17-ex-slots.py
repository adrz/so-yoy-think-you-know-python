class Example:
    __slots__ = ["a", "b"]

    def __init__(self):
        self.a = 1
        self.b = 2


class ExampleChild(Example):
    def __init__(self):
        super().__init__()
        self.c = 3


e = ExampleChild()
print(e.__dict__)
