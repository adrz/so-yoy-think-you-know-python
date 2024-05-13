x = 10


def change_x(new_x):
    x = new_x


change_x(20)
print(x)


"""
In this Python code, the key concept at play is the scope of variables. The variable x is defined outside the function change_x, making it a global variable. Within the function change_x, when we assign a value to x, Python treats x as a new local variable because it's being assigned within the function's scope. Hence, the global variable x remains unchanged.
The line x = new_x does not modify the global x but creates a new local variable x within the function. Therefore, after the function call change_x(20), the original global x remains as 10. The function modifies only the local x, not the global x.
To modify the global x within the function, you need to explicitly declare x as global inside the function:

to modify 

def change_x(new_x):
    global x
    x = new_x


"""
