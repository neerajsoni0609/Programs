input_list = [3, 1, 4, 6, 5, 3]

def find_triplets(list1):
    list2 = []
    for i in input_list:
        list2.append(i**2)
        
    output_list = []
    list_len = len(list2)
    for i in range(list_len):
        for j in range(i+1, list_len):
            
            if ((list2[i] + list2[j]) in list2):
                hypotenuse_index = list2.index(list2[i] + list2[j])
                output_list.append([list1[hypotenuse_index], list1[j], list1[i]])
                
    return output_list
result = find_triplets(input_list)
print(result)

# Asked in Cybage client interview