def factorial(num):

    facNum = 1

    for i in range(num,0,-1):
        facNum *= i

    return facNum

stringNum = str(factorial(100))

sum = 0 

for char in stringNum:

    sum += int(char)

print(sum)


