class Operation:
    def __init__(self, num) -> None:
        self.num = num

    def __add__(self, other):
        return self.num + other.num
    
    def __sub__(self, other):
        return self.num - other.num
    
    def __mul__(self, other):
        return self.num * other.num
    
n1 = Operation(5)
n2 = Operation(4)

sum = n1 + n2
print(sum)

diff = n1 - n2
print(diff)

mul = n1 * n2
print(mul)