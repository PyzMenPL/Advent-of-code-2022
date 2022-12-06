with open('input.txt', 'r') as oFile:
    preparation = True
    crates = [[], [], [], [], [], [], [], [], []]

    for line in oFile:
        # Starting to rearrange the lists after the empty line
        if line == '\n':
            preparation = False

        elif preparation and '[' in line:
            # Assigning values to correct lists
            for index in range(1, len(line) + 1):
                if index % 4 == 0 and line[index - 3] != ' ':
                    crates[int(index / 4 - 1)].insert(0, line[index - 3])

        elif not preparation:
            # Extracting numbers from lines of code
            line = line.split()
            command = [int(line[1]), int(line[3]), int(line[5])]

            # -(command[0]) is the range that we want to replace
            # command[1] - 1 is the index of source list
            # command[2] - 1 is the index of destination list

            # Replacing crates as intended
            for letter in reversed(crates[command[1] - 1][-(command[0]):]):
                crates[command[2] - 1].append(letter)

            del crates[command[1] - 1][-(command[0]):]

    # Printing the output
    for index in range(0, len(crates)):
        print(crates[index][-1], end='')
    print(' ')
