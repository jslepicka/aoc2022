def get_priority(item):
    if item.islower():
        priority = ord(item) - ord('a') + 1
    else:
        priority = ord(item) - ord('A') + 27
    return priority

def part1(input):
    total_pri = 0
    for contents in input:
        middle = len(contents)//2
        first = contents[:middle]
        second = contents[middle:]
        item = ''.join(set(first) & set(second))
        total_pri += get_priority(item)
    return total_pri

def part2(input):
    total_pri = 0
    for i in range(0,len(input)//3):
        item = ''.join(set(input[i*3]) & set(input[i*3+1]) & set(input[i*3+2]))
        total_pri += get_priority(item)
    return total_pri

def main():
    input = []
    with open("3.txt") as file:
        input = [x.strip() for x in file.readlines() if x.strip() != ""]

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()