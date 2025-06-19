def fibonacci(number):
    if number > 2:
        result = fibonacci(number - 1) + fibonacci(number - 2)
        return result

    elif number == 1 or number == 2:
        return 1
    

number = int(input("Enter the number: "))
result = fibonacci(number)
print(result)