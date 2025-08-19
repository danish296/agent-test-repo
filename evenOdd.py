def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0

# Get input from the user
number = int(input("Enter an integer: "))

# Check if the number is even or odd
if is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")