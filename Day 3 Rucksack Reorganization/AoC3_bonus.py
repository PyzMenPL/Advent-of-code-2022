with open('03input.txt', 'r') as oFile:
    # Lista elementów, które pojawiają się w obu listach
    both = []

    # Lista elementów, w jednej grupie
    group = []

    for line in oFile:
        # Dodajemy każdą linijkę
        group.append(set(line[:-1]))

        # Jeżeli mamy 3 elfy w grupie
        if len(group) == 3:
            # Dla każdego znaku w najmniejszym zbiorze
            for letter in min(group):
                # Sprawdź, czy występuje w reszcie
                if letter in group[group.index(min(group)) - 1] and letter in group[group.index(min(group)) - 2]:
                    # Przydziel do listy
                    both.append(letter)

            # Po znalezieniu grupy 3 elfów wyczyść listę group
            group = []

    # Bez żadnych obaw! Wygenerowałem to :D
    values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
              'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
              'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34,
              'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45,
              'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

    # Suma wyników
    suma = 0

    for letter in both:
        suma += values[letter]

    print(suma)
    