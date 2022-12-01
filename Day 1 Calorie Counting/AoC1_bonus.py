with open('01input.txt', 'r') as oFile:
    maxCal = [0, 0, 0]
    elf = []
    for line in oFile:
        if line == "\n":
            if sum(elf) > min(maxCal):
                maxCal[maxCal.index(min(maxCal))] = sum(elf)
            elf = []
        else:
            elf.append(int(line.replace('\n', '')))

    print(sum(maxCal))
