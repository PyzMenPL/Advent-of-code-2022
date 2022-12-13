# Test = 31
import numpy as np

with open('test.txt', 'r') as oFile:
    # Saving file into list
    file = oFile.read().splitlines()

    alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
                'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22,
                'x': 23, 'y': 24, 'z': 25}

    # Getting width and height of the file and saving it into grid variable
    grid = np.zeros((len(file), len(file[0])), dtype=str)

    # XY of starting position and finish position
    start_pos = []
    end_pos = []

    # Changing the array contents
    for col in range(0, len(file)):
        for row in range(0, len(file[col])):
            grid[col][row] = file[col][row]

            # Assigning start and finish value
            if file[col][row] == "S":
                start_pos = [row, col]
            elif file[col][row] == "E":
                end_pos = [row, col]

    print(grid)
    # Grid indexing starts with zero!
    print(start_pos)
    print(end_pos)

    """
    How to day 12
    
    There is starting point (S), and there is end point (E) to find the shortest way
    we have to use Pitagoras theorem (twierdzenie Pitagorasa). 
    
    #1
    We move towards the (E)
    
    #2
    If we approach big height difference and we have multiple move opportunities we save our current
    location + previous location + amount of steps + direction that we are going to go (so if
    something goes wrong we can go back to it) and check:
        
        1st If we can move closer to (E)
        2nd If we can move further from (E)
        
    The way you are going to decide which direction is better is by using Pitagoras theorem. You 
    calculate it for X and Y of the desired locations and compare them (the lower the better).
        
    If we will appear in situation where our previous location is the only way to go, we change our
    current location to last saved position, and move in a different direction so we don't end up in
    the same situation again.
    
    #3
    If our location is equal to end point location we print amount of steps, and exit()
    """
