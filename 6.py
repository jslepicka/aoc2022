import os
from collections import Counter

def get_marker_pos(input, marker_len):
    for i in range(marker_len, len(input)):
        chars = input[i-marker_len:i]
        counter = Counter(chars)
        if len(counter) == marker_len:
            return i
    return None

def part1(input):
    return get_marker_pos(input, 4)

def part2(input):
    return get_marker_pos(input, 14)

def main():
    day=os.path.basename(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = file.readline().strip()

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()