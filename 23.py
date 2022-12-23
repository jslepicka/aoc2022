import os
from collections import defaultdict

def draw_map(input):
    x_min = min(input, key=lambda p: p[0])[0]
    x_max = max(input, key=lambda p: p[0])[0]
    y_min = min(input, key=lambda p: p[1])[1]
    y_max = max(input, key=lambda p: p[1])[1]
    height = max(input, key=lambda p: p[1])[1] + 1

    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if (x, y) in input:
                print(input[(x,y)], end="")
            else:
                print(" ", end="")
        print()

def solve(elves, round_limit=None):
    dir_index = 0
    dirs = [
        [(0, -1), (1, -1), (-1, -1)],   # N, NE, NE
        [(0, 1), (1, 1), (-1, 1)],      # S, SE, SW
        [(-1, 0), (-1, -1), (-1, 1)],   # W, NW, SW
        [(1, 0), (1, -1), (1, 1)]       # E, NE, SE
    ]

    round = 0
    while True:
        round += 1
        proposed_locs = defaultdict(int)
        for e in elves:
            elves[e] = None
            #if no other elves around, do nothing
            found_neighbor = False
            for di in range(4):
                for dd in range(3):
                    d = dirs[di][dd]
                    xx, yy = e[0] + d[0], e[1] + d[1]
                    if (xx, yy) in elves:
                        found_neighbor = True
            if not found_neighbor:
                elves[e] = e
                continue

            search_dir = dir_index
            for _ in range(4):
                found_neighbor = False
                for d in dirs[search_dir]:
                    px, py = e[0] + d[0], e[1] + d[1]
                    if (px, py) in elves:
                        found_neighbor = True
                        break
                if found_neighbor:
                    search_dir = (search_dir + 1) % 4
                    continue
                else:
                    move = dirs[search_dir][0]
                    move_to = (e[0] + move[0], e[1] + move[1])
                    proposed_locs[move_to] += 1
                    elves[e] = move_to
                    break
            if elves[e] is None:
                elves[e] = e

        #now we have proposed moves
        next_elves = {}
        for e in elves:
            if proposed_locs.get(elves[e], 0) > 1:
                #two elves proposing same location, don't move
                next_elves[e] = None
            else:
                next_elves[elves[e]] = None
        elves = next_elves
        dir_index = (dir_index + 1) % 4
        if round_limit == round:
            x_min = min(elves.keys(), key=lambda x:x[0])[0]
            x_max = max(elves.keys(), key=lambda x:x[0])[0]
            y_min = min(elves.keys(), key=lambda x:x[1])[1]
            y_max = max(elves.keys(), key=lambda x:x[1])[1]
            width = x_max - x_min + 1
            height = y_max - y_min + 1
            empty = width * height - len(elves)
            return empty
        elif round_limit is None and len(proposed_locs) == 0:
            return round

def part1(elves):
    return solve(elves, round_limit=10)

def part2(elves):
    return solve(elves)

def main():
    day=os.path.basename(__file__).split('.')[0]
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines() if x.strip() != ""]
    elves = {}
    grove = {}
    for y, line in enumerate(input):
        for x, a in enumerate(line):
            if a == '#':
                elves[(x, y)] = None
            grove[(x, y)] = a

    # temp = {}
    # for e in elves.keys():
    #     temp[e] = '#'
    # draw_map(temp)
    print("Part 1: " + str(part1(elves.copy())))
    print("Part 2: " + str(part2(elves.copy())))

if __name__ == "__main__":
    main()