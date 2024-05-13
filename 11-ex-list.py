def fn1():
    list1 = [1, 2, 3]
    list2 = list1
    list1 += ["a", "b", "c"]
    print(list1)
    print(list2)


def fn2():
    list1 = [1, 2, 3]
    list2 = list1
    list1 = list1 + ["a", "b", "c"]
    print(list1)
    print(list2)


print("calling first function")
fn1()
print("calling second function")
fn2()


"""

In fn1(), list1 is modified in place and list1 and list2 have the reference to the same list, while in fn2() a new list is created and that changes the reference. Again we can use id() to see what’s happening under the hood.


"""


def fn1():
    list1 = [1, 2, 3]
    list2 = list1
    print(id(list1), id(list2))
    list1 += ["a", "b", "c"]
    print(id(list1), id(list2))


def fn2():
    list1 = [1, 2, 3]
    list2 = list1
    print(id(list1), id(list2))
    list1 = list1 + ["a", "b", "c"]
    print(id(list1), id(list2))


list()
