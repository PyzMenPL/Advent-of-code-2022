with open('input.txt', 'r') as oFile:
    suma = 0
    for line in oFile:
        # Rock
        if line[2] == 'X':
            suma += 1
        # Paper
        elif line[2] == 'Y':
            suma += 2
        # Scissors
        elif line[2] == 'Z':
            suma += 3

        # Win
        if line == 'A Y\n' or line == 'B Z\n' or line == 'C X\n':
            suma += 6
        # Draw
        elif line == 'A X\n' or line == 'B Y\n' or line == 'C Z\n':
            suma += 3
        # You don't have to check if you are losing,
        # because it doesn't change the output

print(suma)
