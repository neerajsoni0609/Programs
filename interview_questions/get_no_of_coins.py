'''
Get Minimum Number of coins required for Payment
N = number f coins
X = Amount to be paid
coins = [list of coins]
if payment cannot be done than expect -1
'''

def coin(N, X, coins):
    count = 0
    for i in range(N-1, -1, -1):
        if coins[i] <= X:
            factor = X // coins[i]
            count += factor
            
            X = X - (factor * coins[i])
            
    if X > 0:
        return -1
    return count
        
output = coin(3, 25, [1, 4, 6])
print(output)