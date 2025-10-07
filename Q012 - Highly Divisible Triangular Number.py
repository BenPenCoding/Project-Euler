def getNumFactors(num):

    flooredSqrtNum = int(num**0.5)

    numFactors = 0

    for i in range(1,flooredSqrtNum+1):

        if num % i == 0:

            numFactors += 1

    return numFactors * 2

triangleNum = 0

i = 1

while True:

    triangleNum += i

    if getNumFactors(triangleNum) > 500:

        print(triangleNum)
        break

    i += 1
