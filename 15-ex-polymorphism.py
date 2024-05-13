class MyBaseClass:
    def __init__(self, value):
        self.value = value


class TimesSeven(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 7


class PlusNine(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 9


class R(PlusNine, TimesSeven):
    def __init__(self, value):
        super().__init__(value)
