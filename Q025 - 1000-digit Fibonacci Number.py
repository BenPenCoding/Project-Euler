index = 3

p1, p2, p3 = 1, 1, 2

while True:

    p1 = p2
    p2 = p3 
    p3 = p1 + p2

    index += 1

    #print(f"F{index} = {p3}")

    if len(str(p3)) > 999:

        break

print(index)