def factorial(n):
    if n > 1:
        result = n * factorial(n-1)
        return result
    else:
        return 1

number = int(input("Enter the number to find factorial: "))
print(factorial(number))