def iterator(n):
    for i in range(n):
        yield i


my_it = iterator(10)

while (j := next(my_it)) < 5:
    print(j)

my_it = iterator(10)
while (j := next(my_it)) < 5:
    print(j)
    j = 10
