def part1(input):
    return None

def part2(input):
    return None

def main():
    input = []
    with open("x.txt") as file:
        input = [x.strip() for x in file.readlines() if x.strip() != ""]

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()