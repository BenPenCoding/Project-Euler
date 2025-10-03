from sympy import *

maxN = 0
aTimesB = 0

for a in range(-1000, 1001):

    if a % 2 != 0:

        for b in range(-1000, 1001): 
            
            if b & 2 != 0:

                n = 0
                while isprime((n ** 2) + (a * n) + b):
                    n += 1
                    
                if n > maxN:
                    maxN = n
                    aTimesB = a*b

print(aTimesB)
