class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


buddy = Dog("Buddy")
scooby = Dog("Scooby")
buddy.add_trick("roll over")
scooby.add_trick("play dead")
print(buddy.tricks)
