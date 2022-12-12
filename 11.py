import os
from copy import deepcopy

class Monkey:
    def __init__(self):
        self.items = []
        self.operation = None
        self.divisor = None
        self.true_target = None
        self.false_target = None
        self.inspect_count = 0

def do_rounds(monkeys, num_rounds, part2=False):
    if part2:
        lcm = 1
        for i in range(len(monkeys)):
            lcm *= monkeys[i].divisor

    for _ in range(num_rounds):
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            for _ in range(len(monkey.items)):
                item = monkey.items.pop(0)
                monkey.inspect_count += 1
                if part2:
                    worry_level = monkey.operation(item) % lcm
                else:
                    worry_level = monkey.operation(item) // 3
                if worry_level % monkey.divisor == 0:
                    monkeys[monkey.true_target].items.append(worry_level)
                else:
                    monkeys[monkey.false_target].items.append(worry_level)
    sorted_monkeys = [v for k,v in sorted(monkeys.items(), key=lambda x: x[1].inspect_count, reverse=True)]
    return sorted_monkeys[0].inspect_count * sorted_monkeys[1].inspect_count

def part1(monkeys):
    return do_rounds(monkeys, 20)

def part2(monkeys):
    return do_rounds(monkeys, 10000, part2=True)

def main():
    monkeys = {}
    day=os.path.basename(__file__).split('.')[0]
    with open(day + ".txt") as file:
        input = [x.splitlines() for x in file.read().split("\n\n")]
    for note in input:
        monkey = Monkey()
        monkey_index = int(note[0].split()[-1].split(':')[0])
        monkeys[monkey_index] = monkey
        for item in note[1].split()[2:]:
            monkey.items.append(int(item.split(',')[0]))
        exec("monkey.operation = lambda old: " + ' '.join(note[2].split()[3:]))
        monkey.divisor = int(note[3].split()[-1])
        monkey.true_target = int(note[4].split()[-1])
        monkey.false_target = int(note[5].split()[-1])
 
    print("Part 1: " + str(part1(deepcopy(monkeys))))
    print("Part 2: " + str(part2(deepcopy(monkeys))))

if __name__ == "__main__":
    main()