def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")
