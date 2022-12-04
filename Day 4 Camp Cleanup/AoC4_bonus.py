with open("input.txt", "r") as oFile:
    suma = 0
    for line in oFile:
        # Separating start and end for both elf's ranges
        line_list = line.replace('-', ' ').replace(',', ' ').split(' ')

        # Creating sets based on given ranges
        set1 = set(range(int(line_list[0]), int(line_list[1]) + 1))
        set2 = set(range(int(line_list[2]), int(line_list[3]) + 1))

        # Condition
        if set1.intersection(set2) or set2.intersection(set1):
            suma += 1

    print(suma)
