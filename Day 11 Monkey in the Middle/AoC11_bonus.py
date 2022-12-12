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

    def execute_order_66(self, modulo) -> list:
        """Command that makes the monkey go brrrrr"""
        list_of_commands = []
        for item in range(0, len(self.items)):
            # We are using pop() because items has to be removed, and we are lowering the worry level at the same time
            new_item = int(self.inspect(self.items.pop(0)) % modulo)

            # Deciding who the receiver will be inside append()
            list_of_commands.append({new_item: self.test(new_item)})

        return list_of_commands

    def inspect(self, item) -> int:
        """Item inspection"""
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
        """Finding out if the number is dividable by self. dividable"""
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

        # Empty line means that we are done with our monkey and that we can focus on another one
        elif line == '\n':
            line_index = 0

    # Creating list of with len(monkeys) elements
    inspections = [0] * len(monkeys)

    # Getting the biggest number that can divide every new worry level of an item
    mod = 1
    for monkey in monkeys:
        mod *= monkey.dividable

    # 20 rounds * amount of monkeys
    for i in range(0, 10000):
        for monkey in monkeys:
            # Heart of the program
            commands = monkey.execute_order_66(mod)

            for command in commands:
                # Counting inspections
                inspections[monkeys.index(monkey)] += 1

                # Executing commands
                for key, value in command.items():
                    monkeys[value].items.append(key)

    # Getting the monkey business score
    inspections.sort()
    print(inspections[-1] * inspections[-2])
