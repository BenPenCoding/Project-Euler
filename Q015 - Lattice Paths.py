grid = [[0] * 21 for i in range(21)]

for i in range(21):

    grid[0][i] = 1

for i in range(21):

    grid[i][0] = 1

for row in range(1,21):

    for column in range(1,21):

        grid[row][column] = grid[row-1][column] + grid[row][column-1]

print(grid[20][20])

