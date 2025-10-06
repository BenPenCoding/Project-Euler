def isNumberDivisible(num):

    for i in range(1,21):

        if num % i != 0:

            return False

    return True

i = 2

while True:

    if isNumberDivisible(i):

        print(i)
        break

    i += 2