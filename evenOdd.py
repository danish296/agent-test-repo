#This is created by AI agent kickStart by Danish Akhtar
def is_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Get input from the user
num = int(input("Enter an integer: "))

# Determine if the number is even or odd
result = is_even_odd(num)

# Print the result
print(f"{num} is {result}")
