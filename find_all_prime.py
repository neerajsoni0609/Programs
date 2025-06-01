class Prime:
    def __init__(self) -> None:
        self.number = int(input("Enter the number uptil where you want to generate the prime number list: "))

    def find_all_prime(self):
        self.primes = []
        for num in range(1, self.number+1):
            for i in range(2, num//2):
                if num % i == 0:
                    break
            else:
                self.primes.append(num)

        return self.primes

prime = Prime().find_all_prime()
print(prime)