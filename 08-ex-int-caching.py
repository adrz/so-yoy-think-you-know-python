a = 256
b = 256
c = 257
d = 257
e = -10
f = -10
print(a is b)
print(c is d)
print(e is f)


"""
Explanation:
Python caches small integers, which are integers between -5 and 256. This range of integers is pre-allocated (interned) at the startup of Python. This means any variable in this range points to the same memory address for any specific value.
a = 256; b = 256: Since 256 is within the interned range, both a and b refer to the same memory address. Therefore, print(a is b) outputs True.
c = 257; d = 257: The integers 257 are outside of the interned range. Therefore, Python may create separate objects in memory for each assignment. Thus, print(c is d) typically outputs False, indicating that c and d do not refer to the same object in memory.
"""
