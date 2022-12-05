import os
from collections import deque
import copy

def move_crates(stacks, steps, crane_model=9000):
    for step in steps:
        (_, count, _, src, _, dst) = step.split()
        count = int(count)
        src = int(src)
        dst = int(dst)
        move = ""
        for _ in range(count):
            move += stacks[src].pop()
        if crane_model == 9001:
            move = reversed(move)
        for crate in move:
            stacks[dst].append(crate)
    top_crates = ""
    for i in range(1, max(stacks.keys()) + 1):
        top_crates += stacks[i][-1]
    return top_crates

def part1(stacks, steps):
    return move_crates(stacks, steps)

def part2(stacks, steps):
    return move_crates(stacks, steps, crane_model=9001)

def main():
    day=os.path.basename(__file__).split('.')[0]
    stacks = {}
    with open(day + ".txt") as file:
        stacks_in, steps = file.read().split("\n\n")

    stacks_in = stacks_in.splitlines()
    steps = steps.splitlines()
    for s in stacks_in:
        for i, crate in enumerate(s[1::4]):
            if crate != " ":
                stack_number = i + 1
                if stack_number not in stacks:
                    stacks[stack_number] = deque()
                stacks[stack_number].appendleft(crate)

    print("Part 1: " + str(part1(copy.deepcopy(stacks), steps)))
    print("Part 2: " + str(part2(stacks, steps)))

if __name__ == "__main__":
    main()