num1, num2, num3 = 1, 2, 0

numList = []

while num1 + num2 < 4000000:
    num3 = num1 + num2 

    if num3 % 2 == 0:
        numList.append(num3)

    num1 = num2
    num2 = num3

print(sum(numList) + 2)
