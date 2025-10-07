def getChainLength(num):

    count = 0
    
    while num != 1:

        if num % 2 == 0:

            num /= 2

        else:

            num = (3 * num) + 1

        count += 1

    return count + 1

largestChain = 0

largestChainStartingNumber = 0

for i in range(2,999999):
    
    length = getChainLength(i)
    
    if length > largestChain:

        largestChainStartingNumber = i
        largestChain = length

print(largestChainStartingNumber)










