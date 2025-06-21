sample1 = ['a','b','c','d']
sample2 = [1, 2, 3, 4, 5]

output = []

if len(sample1) > len(sample2):
    length = len(sample1)
else:
    length = len(sample2)

def get_value(list, index):
    try:
        value = list[index]
    except IndexError:
        value = None

    return value

for i in range(length):
    output1 = get_value(sample1, i)
    output2 = get_value(sample2, i)
    
    output.append((output1, output2))
    
print(output)