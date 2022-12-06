with open('input.txt', 'r') as oFile:
    for line in oFile:
        for index in range(0, len(line) + 1):
            # If there are 4 unique values before index
            if len(set(line[index - 4 : index])) == 4:
                print(index)
                break
