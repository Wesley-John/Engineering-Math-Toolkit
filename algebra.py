import math

def solve_linear(a, b):
    if a == 0:
        if b == 0:
            return "Infinite solutions"
        else:
            return "No solution"
    
    return -b / a

def solve_quadratic(a, b, c):
    if a == 0:
        return solve_linear(b, c)
    
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant))/(2*a)
        root2 = (-b - math.sqrt(discriminant))/(2*a)

        return (root1, root2)
    
    elif discriminant == 0:
        root = -b/(2*a)
        return (root,)
    else:
        real_part = -b/(2*a)
        imaginary_part = math.sqrt(-discriminant)/(2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return (root1, root2)
