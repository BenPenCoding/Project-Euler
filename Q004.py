largestPalindrome = 0

def isNumberPaldindromic(num):
    
    num = str(num)

    if num == num[::-1]:

        return True

    else:

        return False

products = {a * b for a in range(100, 1000) for b in range(a, 1000)}

products = sorted(products, reverse = True)

for num in products:

    if isNumberPaldindromic(num):

        print(num) 
        break