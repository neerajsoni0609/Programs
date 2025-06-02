def check_prime(num):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
        
    return True

num = int(input("Enter numner to check if it is prime: "))
result = check_prime(num)
print(result)