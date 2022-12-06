with open('input.txt', 'r') as oFile:
    for line in oFile:
        # Starting from 4 because we don't check unnecessary 3 first letters
        for index in range(4, len(line) + 1):
            # If there are 4 unique values before index
            if len(set(line[index - 4: index])) == 4:
                print(index)
                break
