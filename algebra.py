import math

a = 0
b = 0

def solve_linear(a, b):
    if a == 0:
        if b == 0:
            return "Infinite solutions"
        else:
            return "No solution"
    
    return -b / a

print("Solving the equation {}x + {} = 0 ...".format(a, b))
result = solve_linear(a, b)
print("The solution is x =", result)