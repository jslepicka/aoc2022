def get_sections(pairs):
        return [set(range(pairs[i][0], pairs[i][1]+1)) for i in range(0,2)]

def part1(input):
    count = 0
    for i in input:
        sections1, sections2 = get_sections(i)
        if sections1.issubset(sections2) or sections2.issubset(sections1):
            count += 1
    return count

def part2(input):
    count = 0
    for i in input:
        sections1, sections2 = get_sections(i)
        if len(sections1 & sections2) > 0:
            count += 1
    return count

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