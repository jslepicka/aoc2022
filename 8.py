import os

def is_visible(trees, x, y):
    tree_height = trees[(x,y)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    blocked = 0
    for dx, dy in dirs:
        xx, yy = x, y
        while True:
            xx, yy = xx+dx, yy+dy
            try:
                t = trees[(xx,yy)]
            except KeyError:
                break
            if t >= tree_height:
                blocked += 1
                break
    if blocked == 4:
        return False
    return True

def get_score(trees, x, y):
    score = 1
    tree_height = trees[(x,y)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in dirs:
        xx, yy = x, y
        s = 0
        while True:
            xx, yy = xx+dx, yy+dy
            try:
                t = trees[(xx,yy)]
            except KeyError:
                break
            if t <= tree_height:
                s += 1
            if t >= tree_height:
                break
        if s > 0:

            score *= s
    return score

def part1(trees):
    num_visible = sum([is_visible(trees, x, y) for x, y in trees.keys()])
    return num_visible

def part2(trees):
    return max([get_score(trees, x, y) for x, y in trees.keys()])

def main():
    day=os.path.basename(__file__).split('.')[0]
    input = []
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