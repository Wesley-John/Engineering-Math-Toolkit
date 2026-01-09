def get_int(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print(f"Invalid Input. '{prompt}' is not an integer. Please try again.")

def get_float(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print(f"Invalid Input. '{prompt}' is not a decimal. Please try again.")