with open('test2.txt', 'r') as oFile:
    tails_XY = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    tails_prev_XY = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    head_current_XY = [0, 0]
    head_prev_XY = []

    tail_cords = []
    for line in oFile:
        print(line)
        direction, amount = line.split()
        for i in range(0, int(amount)):
            #input()
            head_prev_XY = head_current_XY[:]

            if direction == 'U':
                print("Głowa rusza się w górę")
                head_current_XY[1] += 1
            elif direction == 'D':
                head_current_XY[1] -= 1
                print("Głowa rusza się w dół")
            elif direction == 'R':
                head_current_XY[0] += 1
                print("Głowa rusza się w prawo")
            elif direction == 'L':
                head_current_XY[0] -= 1
                print("Głowa rusza się w lewo")

            print("Głowa: ", head_current_XY)

            for index in range(0, len(tails_XY)):
                print("Ogon ", index, ": ", "\t\t", tails_XY[index])
                print("Wcześniej: ", "\t", tails_prev_XY[index])
                if index == 0:
                    # 1. If it is in the same place
                    if tails_XY[index] == head_current_XY:
                        continue
                    # 2. If is above or under
                    if (tails_XY[index][1] == head_current_XY[1] + 1 and tails_XY[index][0] == head_current_XY[0]) or (
                            tails_XY[index][1] == head_current_XY[1] - 1 and tails_XY[index][0] == head_current_XY[0]):
                        continue
                    # 3. If is to the right or to the left
                    if (tails_XY[index][0] == head_current_XY[0] + 1 and tails_XY[index][1] == head_current_XY[1]) or (
                            tails_XY[index][0] == head_current_XY[0] - 1 and tails_XY[index][1] == head_current_XY[1]):
                        continue
                    # 4. If it is diagonal
                    # - top left
                    # - top right
                    # - bottom left
                    # - bottom right
                    if (tails_XY[index][0] == head_current_XY[0] - 1 and tails_XY[index][1] == head_current_XY[
                        1] + 1) or (
                            tails_XY[index][0] == head_current_XY[0] + 1 and tails_XY[index][1] == head_current_XY[
                        1] + 1) or (
                            tails_XY[index][0] == head_current_XY[0] - 1 and tails_XY[index][1] == head_current_XY[
                        1] - 1) or (
                            tails_XY[index][0] == head_current_XY[0] + 1 and tails_XY[index][1] == head_current_XY[
                        1] - 1):
                        continue

                    # Because we are the tail right behind the head
                    tails_prev_XY[0] = tails_XY[0][:]
                    tails_XY[0] = head_prev_XY[:]

                # If we are not the first tail
                else:
                    # 1. If it is in the same place
                    if tails_XY[index] == tails_XY[index - 1]:
                        continue
                    # 2. If is above or under
                    if (tails_XY[index][1] == tails_XY[index - 1][1] + 1 and tails_XY[index][0] == tails_XY[index - 1][
                        0]) or (
                            tails_XY[index][1] == tails_XY[index - 1][1] - 1 and tails_XY[index][0] ==
                            tails_XY[index - 1][0]):
                        continue
                    # 3. If is to the right or to the left
                    if (tails_XY[index][0] == tails_XY[index - 1][0] + 1 and tails_XY[index][1] == tails_XY[index - 1][
                        1]) or (
                            tails_XY[index][0] == tails_XY[index - 1][0] - 1 and tails_XY[index][1] ==
                            tails_XY[index - 1][1]):
                        continue
                    # 4. If it is diagonal
                    # - top left
                    # - top right
                    # - bottom left
                    # - bottom right
                    if (tails_XY[index][0] == tails_XY[index - 1][0] - 1 and tails_XY[index][1] == tails_XY[index - 1][
                        1] + 1) or (
                            tails_XY[index][0] == tails_XY[index - 1][0] + 1 and tails_XY[index][1] ==
                            tails_XY[index - 1][
                                1] + 1) or (
                            tails_XY[index][0] == tails_XY[index - 1][0] - 1 and tails_XY[index][1] ==
                            tails_XY[index - 1][
                                1] - 1) or (
                            tails_XY[index][0] == tails_XY[index - 1][0] + 1 and tails_XY[index][1] ==
                            tails_XY[index - 1][
                                1] - 1):
                        continue

                    tails_prev_XY[index] = tails_XY[index][:]
                    tails_XY[index] = tails_prev_XY[index - 1][:]

                print("Ogon się ruszył do ", tails_XY[index])

                # Because we are interested only in last tail
                if index == len(tails_XY) - 1:
                    tail_cords.append(tuple(tails_XY[-1]))
                print(' ')

    print(set(tail_cords))

    # print(tail_cords)

    print(len(set(tail_cords)))
    print("3389 is too high")
