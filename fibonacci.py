def fibonacci(number):
    series = []
    previous = 0
    current = 1

    for i in range(number):
        result = previous + current
        series.append(result)
        previous = current
        current = result

    return series

number = int(input("Enter the number: "))
result = fibonacci(number)
print(result)