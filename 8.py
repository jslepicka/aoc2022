import os
from functools import reduce

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_blocked_in_dir(trees, x, y, dx, dy):
    tree_height = trees[(x,y)]
    while True:
        x, y = x+dx, y+dy
        try:
            t = trees[(x,y)]
        except KeyError:
            break
        if t >= tree_height:
            return True
    return False

def is_visible(trees, x, y):
    blocked_dirs = sum([is_blocked_in_dir(trees, x, y, dx, dy) for dx, dy in dirs])
    if blocked_dirs == 4:
        return False
    return True

def get_score_in_dir(trees, x, y, dx, dy):
    tree_height = trees[(x,y)]
    score = 0
    while True:
        x, y = x+dx, y+dy
        try:
            t = trees[(x,y)]
        except KeyError:
            break
        if t <= tree_height:
            score += 1
        if t >= tree_height:
            break
    return score

def get_score(trees, x, y):
    score = reduce(lambda x, y: x * y, [get_score_in_dir(trees, x, y, dx, dy) for dx, dy in dirs])
    return score

def part1(trees):
    num_visible = sum([is_visible(trees, x, y) for x, y in trees.keys()])
    return num_visible

def part2(trees):
    return max([get_score(trees, x, y) for x, y in trees.keys()])

def main():
    day=os.path.basename(__file__).split('.')[0]
    trees = {}
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines() if x.strip() != ""]
        for y, line in enumerate(input):
            for x, tree in enumerate(line):
                trees[(x,y)] = int(tree)

    print("Part 1: " + str(part1(trees)))
    print("Part 2: " + str(part2(trees)))

if __name__ == "__main__":
    main()