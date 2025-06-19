from functools import reduce

list1 = [1, 2, 3, 4, 5]

double = list(map(lambda x: x*2, list1))
print(double)

filter1 = list(filter(lambda x: x%2 == 0, list1))
print(filter1)

reduce1 = reduce((lambda x, y: x+y), list1)
print(reduce1)