with open('01input.txt', 'r') as oFile:
    maxCal = 0
    elf = []
    for line in oFile:
        if line == "\n":
            if sum(elf) > maxCal:
                maxCal = sum(elf)
            elf = []
        else:
            elf.append(int(line.replace('\n', '')))

    print(maxCal)
