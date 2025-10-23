sample = "abcmadamdad"

def extract_substring(sample, size):
    sub = []
    for i in range(len(sample) - size + 1):
        sub_string = ""
        for j in range(size):
            sub_string += sample[i + j]
            
        sub.append(sub_string)
            
    return sub
    
def find_palindrome(sample):
    palindrome_string = []
    for length in range(3, len(sample)+1):
        sub = extract_substring(sample, length)
        
        for i in sub:
            if i == i[::-1]:
                palindrome_string.append(i)
    
    return palindrome_string

find_palindrome(sample)