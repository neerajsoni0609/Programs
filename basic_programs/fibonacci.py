def fibonacci(number):
    series = []
    previous = 0
    current = 1

    for i in range(number):
        next = previous + current
        series.append(current)
        previous, current = current, next

    return series

number = int(input("Enter the number: "))
result = fibonacci(number)
print(result)