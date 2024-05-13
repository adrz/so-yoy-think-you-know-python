def get_print(x=None):
    x.append(4)
    return x


y = [1, 2, 3]

print(get_print(y))
print(y)
