def get_sections(pairs):
        return [set(range(pairs[i][0], pairs[i][1]+1)) for i in range(0,2)]

def part1(input):
    return sum(sections[0].issubset(sections[1]) or sections[1].issubset(sections[0])
        for sections in [get_sections(i) for i in input]
    )

def part2(input):
    return sum(len(sections[0] & sections[1]) > 0
        for sections in [get_sections(i) for i in input]
    )

def main():
    input = []
    with open("4.txt") as file:
        input = [
            [
                [int(section) for section in (sections[0]).split('-')],
                [int(section) for section in (sections[1]).split('-')]
            ] for sections in 
            [pair.split(',') for pair in
                [x.strip() for x in file.readlines() if x.strip() != ""]
            ]
        ]
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()