sample = ['eat', 'hat', 'ate', 'tea', 'ath', 'test', 'etst']

words = []
for word in sample:
    word1 = list(word)
    word1.sort()
    word2 = "".join(word1)
    words.append(word2)

word_index = {}
index = 0
for word in words:
    if word_index.get(word):
        word_index[word].append(index)
    
    else:
        word_index[word] = [index]

    index += 1

grouped_list = []
for key, value in word_index.items():
    list1 = []
    for i in value:
        list1.append(sample[i])

    grouped_list.append(list1)

print(grouped_list)

# This program was asked in Accenture Interview
# Program can be optimized