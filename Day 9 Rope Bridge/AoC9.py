with open('input.txt', 'r') as oFile:
    tail_XY = [0, 0]
    head_current_XY = [0, 0]
    head_prev_XY = []

    # Because we start from zero
    tail_cords = [(tail_XY[0], tail_XY[1])]
    for line in oFile:
        direction, amount = line.split()
        # For every move
        for i in range(0, int(amount)):
            head_prev_XY = head_current_XY[:]

            # Check direction
            if direction == 'U':
                head_current_XY[1] += 1
            elif direction == 'D':
                head_current_XY[1] -= 1
            elif direction == 'R':
                head_current_XY[0] += 1
            elif direction == 'L':
                head_current_XY[0] -= 1

            # Check position
            # 1. If it is in the same place
            if tail_XY == head_current_XY:
                continue
            # 2. If is directly above or under
            if (tail_XY[1] == head_current_XY[1] + 1 and tail_XY[0] == head_current_XY[0]) or (
                    tail_XY[1] == head_current_XY[1] - 1 and tail_XY[0] == head_current_XY[0]):
                continue
            # 3. If is to the right or to the left
            if (tail_XY[0] == head_current_XY[0] + 1 and tail_XY[1] == head_current_XY[1]) or (
                    tail_XY[0] == head_current_XY[0] - 1 and tail_XY[1] == head_current_XY[1]):
                continue
            # 4. If it is diagonal
                # - top left
                # - top right
                # - bottom left
                # - bottom right
            if (tail_XY[0] == head_current_XY[0] - 1 and tail_XY[1] == head_current_XY[1] + 1) or (
                    tail_XY[0] == head_current_XY[0] + 1 and tail_XY[1] == head_current_XY[1] + 1) or (
                    tail_XY[0] == head_current_XY[0] - 1 and tail_XY[1] == head_current_XY[1] - 1) or (
                    tail_XY[0] == head_current_XY[0] + 1 and tail_XY[1] == head_current_XY[1] - 1):
                continue

            # If the head is far from tail, move to previous head position
            tail_XY = head_prev_XY[:]

            tail_cords.append(tuple(tail_XY))

    # Print output
    print(len(set(tail_cords)))
