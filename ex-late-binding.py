def create_multipliers():
    return [lambda x: i * x for i in range(5)]


for multiplier in create_multipliers():
    print(multiplier(2))


"""
This example demonstrates a common pitfall in Python known as "late binding" or "closure late binding". The issue arises because the lambda functions in the list comprehension capture the variable i, not its value at each iteration. By the time the lambda functions are called, the loop has completed, and i has settled on its final value, which is 4 (since range(5) ends at 4).
Therefore, every lambda function in the list uses 4 as the value of i when called, resulting in each function calculating 4 * x.
"""
