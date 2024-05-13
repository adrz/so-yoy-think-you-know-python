a = "hello"
b = "hello"

c = "hello!"
d = "hello!"


print(f"a is b: {a is b}")
print(f"c is d: {c is d}")


"""
String interning is a method of storing only one copy of each distinct string value, which must be immutable. Python (specifically the CPython implementation) automates string interning for certain strings to improve memory efficiency and comparison speed. This mostly happens with small and simple strings.
However, whether or not strings are interned isn't just a matter of length or simplicity; it also depends on how the string is created. Python automatically interns strings that look like identifiers, i.e., strings that could be Python variable names. This typically includes strings that are composed of letters, digits, and underscores and do not start with a digit.
In the example you provided, the strings a and b are both set to "hello!". Here, the string "hello!" includes a non-alphanumeric character (!), which typically would mean the string is not interned. However, Python's behavior can vary based on implementation and the context in which the strings are created:
"""
