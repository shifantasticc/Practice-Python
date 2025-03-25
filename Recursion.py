def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print(f"Factorial of {num} doesn't exist")
elif num == 0:
    print(f"Factorial of {num} is 0")
else :
    print(f"Factorial of {num} is {factorial(num)}")
