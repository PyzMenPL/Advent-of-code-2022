class Cyclist:
    def __init__(self):
        self.cycles = 0
        self.strengths = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}

    def cycle(self, register):
        """Whenever cycle takes place"""
        # Incrementing the value by 1
        self.cycles += 1

        # Check if we have to read this register
        if self.cycles in self.strengths.keys():
            self.strengths[self.cycles] = register * self.cycles


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

    # Output the answer
    print(sum(cyclist.strengths.values()))
