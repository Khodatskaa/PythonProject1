n = int(input(": "))

if n < 0:
    print("Unknown operation number")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    print(f"The factorial of {n} is {factorial}")