def for_loop_alloc_speed(iter: int = 100_000):
    x = [0] * iter
    for i in range(iter):
        x[i] = i**2
    return x


def for_loop_speed(iter: int = 100_000):
    x = []
    for i in range(iter):
        x.append(i**2)
    return x


def list_comp_speed(iter: int = 100_000):
    return [i**2 for i in range(iter)]


import timeit

# run 1000 times each functions
print("for loop speed: ", timeit.timeit(for_loop_speed, number=1_000))
print("for loop alloc speed: ", timeit.timeit(for_loop_alloc_speed, number=1_000))
print("list comp speed: ", timeit.timeit(list_comp_speed, number=1_000))


"""
Efficiency: List comprehensions in Python are known for being more efficient in terms of execution speed compared to traditional for loops. This is because the list comprehension is executed as a single statement and is optimized internally to be faster and more memory-efficient.
Internal Implementation: List comprehensions are implemented in C and do not require the overhead of method calls (append) or index assignment in each iteration, which typically makes them faster.




Memory Pre-allocation: This function pre-allocates memory by initializing the list x with a fixed size ([0] * iter), and then it modifies each element. This avoids the overhead of dynamic memory allocation during the loop execution, making it faster than a simple for loop that uses append.
Direct Assignment: Directly setting the value at a specific index (x[i] = i**2) is generally faster than appending to the end of the list, as it avoids the potential resizing operations that append might trigger.
"""  # noqa
