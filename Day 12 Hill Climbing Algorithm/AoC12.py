# Test = 31
import numpy as np
import math

with open('input.txt', 'r') as oFile:
    # Saving file into list
    file = oFile.read().splitlines()

    alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
                'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22,
                'x': 23, 'y': 24, 'z': 25}

    # Getting width and height of the file and saving it into grid variable
    grid = np.zeros((len(file), len(file[0])), dtype=int)

    my_pos = []
    dst_pos = []
    steps = 0

    # Changing the array contents
    for col in range(0, len(file)):
        for row in range(0, len(file[col])):
            # Assigning start and finish value
            if file[col][row] == "S":
                my_pos = [row, col]
                # Start value == -1
                grid[col][row] = 0
                continue
            elif file[col][row] == "E":
                dst_pos = [row, col]
                # End value == 26
                grid[col][row] = 26
            else:
                grid[col][row] = alphabet[file[col][row]]

    print(grid)

    for col in grid:
        for row in col:
            print(row, end=" ")
        print()

    print("Pozycja startowa: ", my_pos)
    print("Pozycja docelowa: ", dst_pos)
    """
    How to day 12
    
    There is starting point (S), and there is end point (E) to find the shortest way
    we have to use Pitagoras theorem (twierdzenie Pitagorasa). 
    
    #1
    We move towards the (E)
        1st calculate Pitagoras theorem for all possible moves
        2nd Choose the smallest one
    
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

    moves_from_snapshot = ()
    position_snapshots = []
    my_prev_pos = ()
    times = 100

    # Main loop
    while grid[my_pos[1]][my_pos[0]] != 26:

        # Możliwe do wykonania ruchy
        available_moves = []

        # If we are not going back to our snapshot
        if not moves_from_snapshot:

            # Stwórz listę wszystkich możliwych ruchów (4 ruchy)
            all_moves = (
                # Góra
                (my_pos[0], my_pos[1] + 1),
                # Dół
                (my_pos[0], my_pos[1] - 1),
                # Prawo
                (my_pos[0] + 1, my_pos[1]),
                # Lewo
                (my_pos[0] - 1, my_pos[1]))

            for move in all_moves:
                # 1. Indeksy grid miejsca docelowego zawsze powinny być dodatnie.
                # Czyli jeżeli nie są dodatnie, to znaczy, że są poza grid
                if move[0] < 0 or move[1] < 0:
                    continue

                # 1. a) Indeksy nie powinny wykraczać poza tabelę.
                # Jeżeli nie przekraczamy maksymalnego x lub y
                if move[0] >= len(grid[0]) or move[1] >= len(grid):
                    continue

                # 2. wartość miejsca docelowego jest równa, o jeden mniejsza lub o jeden większa
                value_of_my_pos = grid[my_pos[1]][my_pos[0]]
                acceptable_values = [value_of_my_pos - 1, value_of_my_pos, value_of_my_pos + 1]

                if grid[move[1]][move[0]] in acceptable_values:
                    available_moves.append(move)

            # When we are starting we don't have previous position, so we have to check if this isn't our first move
            if my_prev_pos:
                # Deleting previous position to prevent going back
                try:
                    del available_moves[available_moves.index(my_prev_pos)]
                except ValueError:
                    pass
        else:
            # If we are going back to our snapshot
            available_moves = moves_from_snapshot[:]
            moves_from_snapshot = []

        print(available_moves)

        # Użyj twierdzenia Pitagorasa, aby dowiedzieć się, która droga będzie krótsza
        distances_to_end_points = {}

        for move in available_moves:
            # Jeżeli moja pozycja jest na takiej samej wysokości co ta docelowa nie korzystaj z Pitagorasa
            if move[1] == dst_pos[1]:
                # Długość pomiędzy punktami
                distances_to_end_points[abs(move[0] - dst_pos[0])] = move
                # print(move, abs(move[0]-dst_pos[0]))
                continue

            # Jeżeli wartości y są różne skorzystaj ze wzory Pitagorasa
            missing_point = [move[0], dst_pos[1]]

            # Deklaracja a, b i c
            a = abs(move[1] - missing_point[1]) ** 2
            b = abs(dst_pos[0] - missing_point[0]) ** 2
            c = math.sqrt(a + b)
            # print(move, missing_point, a, b, c)

            # Zapisanie odległości między punktami jako klucz, a pola jako wartość
            distances_to_end_points[c] = move

        # print(distances_to_end_points)

        # Przenieś się do lepszej pozycji
        try:
            lepsza_pozycja = distances_to_end_points[min(distances_to_end_points)]
            my_prev_pos = tuple(my_pos[:])
            my_pos[0] = lepsza_pozycja[0]
            my_pos[1] = lepsza_pozycja[1]
            print("Przeszedłem do ", my_pos)
            steps += 1
        except ValueError:
            del position_snapshots[-1]
            # When distances_to_end_points is empty
            print("Utknąłem!")
            print("Cofam się do: ", position_snapshots[-1]["position"])
            my_pos = position_snapshots[-1]["position"]
            moves_from_snapshot = position_snapshots[-1]["possible moves"]
            steps = position_snapshots[-1]["steps"]
            del position_snapshots[-1]

        # If we have multiple directions we could go make snapshot
        if len(available_moves) > 1:
            del available_moves[available_moves.index(lepsza_pozycja)]
            snapshot = {"position": my_pos[:], "possible moves": available_moves[:], "steps": steps}
            position_snapshots.append(snapshot)

        # print("Możliwe ruchy: ", available_moves)
        # print("Dystanse do konca: ", distances_to_end_points)
        times -= 1
        if times == 0:
            break

        # print(grid[my_pos[0]][my_pos[1]])
        """
        1. Na czym polega aktualny problem?
        
        Jest sobie miejsce na tej zasadzie: 
        
        0 0 2 20
        0 0 2 20
        2 2 2 26
        
        Nasz podróżnik trafiając do prawego dolnego narożnika zer nie może się cofnąć (bo to zabrania mu program),
        ale może pójść do góry. Teraz sytuacja wygląda podobnie, nie może się cofnąć (zbliżyć do celu), dlatego 
        wybiera jego jedyną możliwość czyli ruch w lewo. Całość się zapętla.
        
        Trzeba wymyślić jeszcze jakiś dodatkowy mechanizm zapobiegający powtarzaniu się.
        
        2. Aby elf zawsze szedł najkrótszą drogą, można sprawdzić twierdzeniem Pitagorasa nasz obecny punkt z wszystkimi
        poprzednimi. Jeżeli uzyskana w ten sposób ścieżka ma mniejszą liczbę kroków niż ta pierwotna zastępujemy naszą
        dotychczasową liczbę kroków tymi nowymi.
        """

    print(steps)
