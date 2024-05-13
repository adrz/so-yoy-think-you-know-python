class A:
    def say(self):
        print("A says hello")


class B(A):
    def say(self):
        print("B says hello")


class C(A):
    def say(self):
        print("C says hello")


class D(B, C):
    pass


D().say()
