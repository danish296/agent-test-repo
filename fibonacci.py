def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

number = int(input("Enter the number of terms: "))

print("Fibonacci series:")
for i in fibonacci(number):
    print(i, end="  ")
