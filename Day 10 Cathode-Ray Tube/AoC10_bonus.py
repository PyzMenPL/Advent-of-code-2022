class Cyclist:
    def __init__(self):
        self.cycles = 0
        self.cycles_index = 0
        # One list one row of crt screen
        self.crt = [[], [], [], [], [], []]

    def cycle(self, register):
        """Whenever cycle takes place"""

        # If we reach the end of the line, we go back to 0, and we go down by one line
        if self.cycles % 40 == 0 and self.cycles != 0:
            self.cycles = 0
            self.cycles_index += 1

        # Declaring the values where the pixel should be lightened
        lighten = [register - 1, register, register + 1]

        # Finding out if pixel should be lightened or not
        if self.cycles in lighten:
            self.crt[self.cycles_index].append('#')
        else:
            self.crt[self.cycles_index].append('.')

        # Incrementing the amount of cycles
        self.cycles += 1


with open('input.txt', 'r') as oFile:
    cyclist = Cyclist()
    x = 1
    for line in oFile:
        # No matter what our line is we do at least one cycle
        cyclist.cycle(x)

        # If the first 4 characters are addx
        if line[:4] == 'addx':
            cyclist.cycle(x)

            # Adding the value from everything after the 5th character to x
            x += int(line[5:])

    # The choice is yours
    oldschool = True
    # I'm old school guy B)

    # Output the answer
    if oldschool:
        print(''.join(cyclist.crt[0]))
        print(''.join(cyclist.crt[1]))
        print(''.join(cyclist.crt[2]))
        print(''.join(cyclist.crt[3]))
        print(''.join(cyclist.crt[4]))
        print(''.join(cyclist.crt[5]))
    else:
        for i in range(0, len(cyclist.crt)):
            print(''.join(cyclist.crt[i]))
