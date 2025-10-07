sumOfSquares = 0

for i in range(1, 101):

    sumOfSquares += i**2



sum = 0

for i in range(1, 101):

    sum += i

print(sumOfSquares - (sum**2))