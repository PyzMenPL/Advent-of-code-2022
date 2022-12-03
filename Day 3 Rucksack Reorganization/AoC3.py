with open('03input.txt', 'r') as oFile:
    # List of items that appear in both lists
    both_lower = []
    both_upper = []

    for line in oFile:
        # Divide the line into two parts and get rid of the \n (-1 in part2)
        part1 = set(line[:int(len(line) / 2)])
        part2 = set(line[int(len(line) / 2):-1])

        # Sorting characters into appropriate lists
        for letter in part1:
            if letter in part2:
                if letter.islower():
                    both_lower.append(letter)
                else:
                    both_upper.append(letter.lower())
                break

    # No worries! I generated this :D
    values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
              'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
              'x': 24, 'y': 25, 'z': 26}

    # Total results
    suma = 0

    for letter in both_lower:
        suma += values[letter]

    for letter in both_upper:
        suma += values[letter] + 26

    print(suma)
