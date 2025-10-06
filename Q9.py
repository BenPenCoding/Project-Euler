def checkTriplet(a, b, c):

    if (a ** 2) + (b ** 2) == (c ** 2): return True

    else: return False

def findTriplet():

    for a in range(1,999):

        for b in range(a + 1, 999):

            for c in range(b + 1, 999):

                if a + b + c == 1000:

                    if checkTriplet(a, b, c):

                        return a*b*c

print(findTriplet())
