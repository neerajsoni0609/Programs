sample1 = ['a','b','c', 'd']
sample2 = [1, 2, 3, 4, 5]

output = []

if len(sample1) > len(sample2):
    length = len(sample1)
else:
    length = len(sample2)

for i in range(length):
    try:
        output1 = sample1[i]
    except IndexError:
        output1 = None
    try:
        output2 = sample2[i]
    except IndexError:
        output2 = None
    
    output.append((output1, output2))
    
print(output)