suma = 0
with open('input.txt', 'r') as oFile:
    for line in oFile:
        # Lost
        if line[2] == 'X':
            # Rock
            if line[0] == 'A':
                # Scissors
                suma += 3
            # Paper
            elif line[0] == 'B':
                # Rock
                suma += 1
            # Scissors
            elif line[0] == 'C':
                # Paper
                suma += 2
        # Draw
        elif line[2] == 'Y':
            suma += 3
            # Rock
            if line[0] == 'A':
                # Rock
                suma += 1
            # Paper
            elif line[0] == 'B':
                # Paper
                suma += 2
            # Scissors
            elif line[0] == 'C':
                # Scissors
                suma += 3
        # Win
        elif line[2] == 'Z':
            suma += 6
            # Rock
            if line[0] == 'A':
                # Paper
                suma += 2
            # Paper
            elif line[0] == 'B':
                # Scissors
                suma += 3
            # Scissors
            elif line[0] == 'C':
                # Rock
                suma += 1

print(suma)
