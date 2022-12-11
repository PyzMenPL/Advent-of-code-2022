class Monkey:
    def __init__(self) -> None:
        # Starting items
        self.items = []
        # Checking the operation
        self.addition = True
        self.operation_number = 0
        self.operation_outcome = 0
        # Number that we check if is dividable
        self.dividable = 0
        # Target monkeys
        self.true_target = 0
        self.false_target = 0
        # How many times monkey inspected item
        self.inspections = 0

    def execute_order_66(self) -> dict:
        commands = {}
        for item in self.items:
            if item == 74:
                print("Tutaj!")
            new_item = self.inspect(item)

            new_item = int(float(new_item)/3)
            print(new_item)

            receiver = self.test(new_item)

            commands[new_item] = receiver

        self.items = []
        return commands

    def inspect(self, item) -> int:
        lista = [item]
        #print("Item: ", lista)
        #print("Operation: ", self.operation_number)
        self.inspections += 1
        if self.operation_number == 'old':
            if self.addition:
                return item + item
            else:
                return item * item
        else:
            if self.addition:
                return item + self.operation_number
            else:
                return item * self.operation_number

    def test(self, item_to_test) -> int:
        #print(item_to_test)
        #print(self.dividable)
        if item_to_test % self.dividable == 0:
            return self.true_target
        else:
            return self.false_target


with open('input.txt', 'r') as oFile:
    # Index in this list will tell us with which monkey are we dealing with
    monkeys = []
    line_index = 0
    for line in oFile:
        line_index += 1

        if line_index == 1:
            monkeys.append(Monkey())

        # 1st line tells us the index of our monkey. In our case it is useless
        # 2nd line tells us what starting item our monkey has
        if line_index == 2:
            for number in line[18:].split(', '):
                monkeys[-1].items.append(int(number))

        # 3rd line tells us what operation monkey needs to process
        elif line_index == 3:
            # Checking if we are dealing with addition or multiplication
            if line[23] == '*':
                monkeys[-1].addition = False

            if line[25:] == 'old\n':
                monkeys[-1].operation_number = line[25:].strip()
            else:
                monkeys[-1].operation_number = int(line[25:])

        # 4th line tells us by which number we divide
        elif line_index == 4:
            monkeys[-1].dividable = int(line[21:])

        # 5th line tells us to which monkey we throw our item if test is true
        elif line_index == 5:
            monkeys[-1].true_target = int(line[-2])

        # 5th line tells us to which monkey we throw our item if test is false
        elif line_index == 6:
            monkeys[-1].false_target = int(line[-2])

        elif line == '\n':
            line_index = 0

    # Range 80 because 20 * 4rounds
    for i in range(0, 80):
        # Ordered monkeys
        print("Małpa ", i % len(monkeys), " ma ", monkeys[i % len(monkeys)].items)
        commands = monkeys[i % len(monkeys)].execute_order_66()

        for key, value in commands.items():
            print("Małpa ", value, " dostaje ", key)
            monkeys[value].items.append(key)

        print("Małpa ", i % len(monkeys), " ma ", monkeys[i % len(monkeys)].items)

    inspections = {}
    for i in range(0, len(monkeys)):
        inspections[i] = monkeys[i].inspections

    outcome = 1

    for i in sorted(inspections.values())[-2:]:
        outcome *= i

    print(outcome)
