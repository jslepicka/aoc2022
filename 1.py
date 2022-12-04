def get_cals_per_elf(input):
    return [sum(i) for i in input]

def part1(input):
    return max(get_cals_per_elf(input))

def part2(input):
    return sum(sorted(get_cals_per_elf(input), reverse=True)[0:3])

def main():
    input = []
    with open("1.txt") as file:
        input = [
            x for x in [
                [int(cals) for cals in elf.split("\n") if cals.isnumeric()]
                for elf in file.read().split("\n\n")
            ] if len(x) > 0
        ]

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()
