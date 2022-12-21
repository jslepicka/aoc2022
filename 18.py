import os

def part1(input):
    area = len(input) * 6
    for a in input:
        for b in input:
            if a[0] == b[0] and a[1] == b[1] and abs(a[2] - b[2]) == 1:
                area -= 1
            if a[0] == b[0] and a[2] == b[2] and abs(a[1] - b[1]) == 1:
                area -= 1
            if a[1] == b[1] and a[2] == b[2] and abs(a[0] - b[0]) == 1:
                area -= 1
    return area

def get_neighbors(point, minp, maxp):
    dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    neighbors = []
    for d in dirs:
        p = tuple(point[i] + d[i] for i in range(3))
        if any([p[i] < minp[i] or p[i] > maxp[i] for i in range(3)]):
            continue
        neighbors.append(p)
    return neighbors
           

def part2(input):
    area = len(input) * 6
    min_x, max_x = min(a[0] for a in input), max(a[0] for a in input)
    min_y, max_y = min(a[1] for a in input), max(a[1] for a in input)
    min_z, max_z = min(a[2] for a in input), max(a[2] for a in input)
    area = 0
    minp = (min_x - 1, min_y - 1, min_z - 1)
    maxp  = (max_x + 1, max_y + 1, max_z + 1)
    stack = [minp]
    visited = set(minp)
    while stack:
        c = stack.pop(0)
        neighbors = get_neighbors(c, minp, maxp)
        for n in neighbors:
            if n in visited:
                continue
            if n in input:
                area += 1
            else:
                visited.add(n)
                stack.append(n)

    return area

def main():
    cubes = []
    day=os.path.basename(__file__).split('.')[0]
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines() if x.strip() != ""]
        for i in input:
            x, y, z = i.split(',')
            cubes.append((int(x), int(y), int(z)))

    print("Part 1: " + str(part1(cubes)))
    print("Part 2: " + str(part2(cubes)))

if __name__ == "__main__":
    main()