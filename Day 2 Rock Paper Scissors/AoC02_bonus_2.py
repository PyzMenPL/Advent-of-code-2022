with open('02input.txt', 'r') as oFile:
    suma = 0
    for line in oFile:
        # Rock
        if line[0] == 'A':
            # Draw
            if line[2] == 'Y':
                # Draw + rock
                suma += 3 + 1
            # Win
            elif line[2] == 'Z':
                # Win + paper
                suma += 6 + 2
            else:
                # Lost + scissors
                suma += 3

        # Paper
        if line[0] == 'B':
            # Draw
            if line[2] == 'Y':
                # Draw + paper
                suma += 3 + 2
            # Win
            elif line[2] == 'Z':
                # Win + scissors
                suma += 6 + 3
            else:
                # Lost + rock
                suma += 1

        # Scissors
        elif line[0] == 'C':
            # Draw
            if line[2] == 'Y':
                # Draw + scissors
                suma += 3 + 3
            # Win
            elif line[2] == 'Z':
                # Win + rock
                suma += 6 + 1
            else:
                # Lost + paper
                suma += 2

print(suma)
