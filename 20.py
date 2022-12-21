import os

def decrypt(input, multiplier = 1, rounds = 1):
    seq = []
    for i, n in enumerate(input):
        seq.append((i, n * multiplier))
    seq_len = len(seq)

    orig = seq.copy()
    for _ in range(rounds):
        for i, n in orig:
            src = seq.index((i, n))
            dst = (src + n) % (seq_len - 1)
            a = seq.pop(src)
            seq.insert(dst, a)

    zero_index = [x[1] for x in seq].index(0)
    return sum([seq[(zero_index + i) % seq_len][1] for i in [1000, 2000, 3000]])

def part1(input):
    return decrypt(input)

def part2(input):
    return decrypt(input, 811589153, 10)

def main():
    day=os.path.basename(__file__).split('.')[0]
    with open(day + ".txt") as file:
        input = [int(x) for x in [x.strip() for x in file.readlines() if x.strip() != ""]]

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()