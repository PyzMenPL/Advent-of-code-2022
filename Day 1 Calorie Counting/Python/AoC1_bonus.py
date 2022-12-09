with open('input.txt', 'r') as oFile:
    maxCal = [0, 0, 0]
    elf = []
    for line in oFile:
        # If we reached end of amount of calories per one elf
        if line == "\n":
            if sum(elf) > min(maxCal):
                maxCal[maxCal.index(min(maxCal))] = sum(elf)
            elf = []
        # If line is a number
        else:
            elf.append(int(line))

    print(sum(maxCal))
