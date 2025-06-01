def factorial(number):
    result = 1
    for num in range(1, number+1):
        result *= num

    return result

number = int(input("Enter the number to find factorial: "))
print(factorial(number))