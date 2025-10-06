numList = []

for i in range(1000):
    
    if i % 3 == 0:
        numList.append(i)

    elif i % 5 == 0 and i not in numList:
        numList.append(i)

    else:
        pass

print(sum(numList))