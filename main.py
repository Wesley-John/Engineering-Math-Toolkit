from algebra import solve_linear, solve_quadratic
from calculus import derivative, integrate
from plotting import plot_function
from utils import get_float, get_int
import math

def menu():
    print("\nENGINEERING MATH TOOLKIT")
    print("1. Solve linear equation: ax + b = 0")
    print("2. Solve quadratic equation: ax^2 + bx + c = 0")
    print("3. Numerical derivative")
    print("4. Numerical integration")
    print("5. Plot function")
    print("0. Exit")


def main():
    while True:
        menu()
        choice = get_int("Choose an option: ")

        if choice == 1:
            a = get_float("Enter a: ")
            b = get_float("Enter b: ")
            result = solve_linear(a, b)
            print("Result:", result)

        elif choice == 2:
            a = get_float("Enter a: ")
            b = get_float("Enter b: ")
            c = get_float("Enter c: ")
            result = solve_quadratic(a, b, c)
            print("Roots:", result)

        elif choice == 3:
            x = get_float("Point x: ")
            print("Computing derivative of f(x) = x² at x =", x)
            result = derivative(lambda t: t**2, x)
            print("Derivative ≈", result)

        elif choice == 4:
            a = get_float("Lower limit a: ")
            b = get_float("Upper limit b: ")
            n = get_int("Number of intervals n: ")
            print("Integrating f(x) = x² from", a, "to", b)
            result = integrate(lambda t: t**2, a, b, n)
            print("Integral ≈", result)

        elif choice == 5:
            print("Plotting f(x) = x²")
            plot_function(lambda t: t**2, -10, 10)

        elif choice == 0:
            print("Exiting toolkit.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()