# Given an integer array A containing N distinct integers, 
# you have to find all the leaders in array A. 
# An element is a leader if it is strictly greater than all the elements to its right side.
# NOTE: The rightmost element is always a leader.

# Example Input
# Input 1:
# 	A = [16, 17, 18, 10, 5, 6]
# Sample Output - [6, 10, 18]

A = [16, 17, 18, 10, 5, 6]

def find_leader(sample):
    sample.reverse()
    
    leader = []

    counter = 0
    for i in sample:
        if counter == 0:
            leader.append(i)

        elif i > leader[-1]:
            leader.append(i)

        counter += 1

    return leader

leaders = find_leader(A)
print(leaders)