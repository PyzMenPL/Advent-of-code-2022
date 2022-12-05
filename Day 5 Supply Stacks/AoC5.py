import time


def printCollumns(crates, command = []):
    if command == []:
        print(crates)
        for crate in range(0, len(crates)):
            print('Crate ', crate, ': ', end='')
            for i in range(0, len(crates[crate])):
                print(crates[crate][i], end='')
            print(' ')
    else:
        print(' ')
        dst_list = crates[command[2] - 1]
        src_list = crates[command[1] - 1]
        del_range = -(command[0])

        # print('Bufor:')
        print(dst_list[del_range:])

        print(f"move {command[0]} from {command[1]} to {command[2]}")

        #print("Before:")
        for crate in [command[1], command[2]]:
            print('Crate ', crate, ': ', end='')
            for i in range(0, len(crates[crate])):
                print(crates[crate][i], end='')
            print(' ')

preparation = True
crates = [[], [], [], [], [], [], [], [], []]

with open('input.txt', 'r') as oFile:
    for line in oFile:
        if line == '\n' or line.replace(' ', '') == '123456789\n':
            preparation = False

            #printCollumns(crates)
            #time.sleep(10)


        elif preparation:
            # Assigning values to correct lists
            for index in range(0, len(line) + 1):
                if index % 4 == 0 and index - 2 != ' ' and index != 0:
                    crates[int(index/4 - 1)].insert(0, line[index - 3])

            # Removing ' ' from crates
            for crate in crates:
                while ' ' in crate:
                    del crates[crates.index(crate)][crate.index(' ')]

        else:
            command = []
            for letter in line:
                if letter.isdigit():
                    command.append(int(letter))

            #printCollumns(crates, command)
            #time.sleep(5)

            dst_list = crates[command[2] - 1]
            src_list = crates[command[1] - 1]
            del_range = -(command[0])

            #print(f"move {command[0]} from {command[1]} to {command[2]}")

            for letter in src_list[del_range:]:
                dst_list.append(letter)

            del src_list[del_range:]

        for index in range(0, 9):
            if len(crates[index]) != 0:
                print(crates[index][-1], end='')
                #print(crates[index][0], end='')
            else:
                print(' ', end='')
        print(' ')
        #print(crates)


