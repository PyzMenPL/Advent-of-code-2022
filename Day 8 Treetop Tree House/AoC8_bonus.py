import numpy as np


with open('input.txt', 'r') as oFile:
    # If you want to use test file change to 5
    grid_range = 99
    # Declaring grid
    grid = np.zeros((grid_range, grid_range), dtype=int)

    # Fill the grid according to input file
    pre_column = 0
    for line in oFile:
        line = line.strip()
        for row in range(0, len(line)):
            grid[pre_column][row] = line[row]

        pre_column += 1

    # Declare the output
    max_scenic = 0

    for column in range(0, grid_range):
        for row in range(0, grid_range):
            # Lis of elements that we will multiply
            suma = [0, 0, 0, 0]

            # If the tree is on the edge
            if row == 0 or row == grid_range - 1 or column == 0 or column == grid_range - 1:
                continue

            # If the tree is not on the edge
            else:
                # If is seen from top
                # Length from start to current place
                # len(grid[0:column]) -> 99*1, 99*2, 99*3, ..., 99*98
                for i in range(1, len(grid[0:column]) + 1):
                    suma[0] += 1
                    # If we approach the same higher tree
                    if grid[column][row] <= grid[column - i][row]:
                        break

                # If is seen from bottom
                for i in range(1, len(grid[column:grid_range - 1]) + 1):
                    suma[1] += 1
                    # If we approach the same higher tree
                    if grid[column][row] <= grid[column + i][row]:
                        break

                # If is seen from right
                for i in range(1, len(grid[column][row:grid_range])):
                    suma[2] += 1
                    # If we approach the same higher tree
                    if grid[column][row] <= grid[column][row + i]:
                        break

                # If is seen from left
                for i in range(1, len(grid[column][0:row]) + 1):
                    suma[3] += 1
                    # If we approach the same higher tree
                    if grid[column][row] <= grid[column][row - i]:
                        break

                # Check if current scenic score is higher than the max one
                suma[0] = suma[0] * suma[1] * suma[2] * suma[3]
                if suma[0] > max_scenic:
                    max_scenic = suma[0]

    print(max_scenic)
