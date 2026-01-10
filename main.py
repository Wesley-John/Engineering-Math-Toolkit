from algebra import solve_linear, solve_quadratic
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
            print(f"Solving the equation {a}x + {b} = 0 ...")
            print("Result:", solve_linear(a, b))

        elif choice == 2:
            a = get_float("Enter a: ")
            b = get_float("Enter b: ")
            c = get_float("Enter c: ")
            print(f"Solving the equation {a}x^2 + {b}x + {c} = 0 ...")
            print("Result:", solve_quadratic(a, b, c))

        elif choice == 0:
            print("Exiting Engineering Math Toolkit. Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()