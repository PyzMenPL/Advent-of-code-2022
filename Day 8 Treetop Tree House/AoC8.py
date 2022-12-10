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
    suma = 0

    for column in range(0, grid_range):
        for row in range(0, grid_range):
            # If the tree is on the edge
            if row == 0 or row == grid_range - 1 or column == 0 or column == grid_range - 1:
                suma += 1

            # If the tree is not on the edge
            else:
                # Jeżeli drzewo jest widoczne prestaje być dalej sprawdzane
                already_visible = False

                if not already_visible:
                    # Length from start to current place
                    # len(grid[0:column]) -> 99*1, 99*2, 99*3, ..., 99*98
                    for i in range(1, len(grid[0:column]) + 1):
                        # If we approach the same or higher tree from top
                        if grid[column][row] <= grid[column - i][row]:
                            suma -= 1
                            break

                        # If we have maximal i and the loop is still working,
                        # this means that the tree is visible
                        if i == len(grid[0:column]):
                            already_visible = True

                    # If the tree is not visible, nothing will change. Otherwise, suma += 1
                    suma += 1

                if not already_visible:
                    for i in range(1, len(grid[column:grid_range - 1]) + 1):
                        # If we approach the same or higher tree from bottom
                        if grid[column][row] <= grid[column + i][row]:
                            suma -= 1
                            break

                        if i == len(grid[column:grid_range - 1]):
                            already_visible = True

                    suma += 1

                if not already_visible:
                    for i in range(1, len(grid[column][row:grid_range])):
                        # If we approach the same or higher tree from right
                        if grid[column][row] <= grid[column][row + i]:
                            suma -= 1
                            break

                        if i == len(grid[column][row:grid_range])-1:
                            already_visible = True

                    suma += 1

                if not already_visible:
                    for i in range(1, len(grid[column][0:row]) + 1):
                        # If we approach the same or higher tree from left
                        if grid[column][row] <= grid[column][row - i]:
                            suma -= 1
                            break

                        if i == len(grid[column][0:row])-1:
                            already_visible = True

                    suma += 1

    print(suma)
