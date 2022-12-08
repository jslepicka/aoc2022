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

def get_map_max(map):
    max_x = max(map.keys(), key=lambda x: x[0])[0]
    max_y = max(map.keys(), key=lambda x: x[1])[1]
    return max_x, max_y

def part1(trees):
    num_visible = 0
    max_x, max_y = get_map_max(trees)
    for y in range(0, max_y+1):
        for x in range(0, max_x+1):
            if is_visible(trees, x, y):
                num_visible += 1
    return num_visible

def part2(trees):
    scores = {}
    max_x, max_y = get_map_max(trees)
    for y in range(0, max_y+1):
        for x in range(0, max_x+1):
            scores[(x,y)] = get_score(trees, x, y)
    return max(scores.values())

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