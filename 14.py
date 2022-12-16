import os

def draw_map(input):
    x_min = min(input, key=lambda p: p[0])[0]
    x_max = max(input, key=lambda p: p[0])[0]
    height = max(input, key=lambda p: p[1])[1] + 1

    for y in range(height):
        for x in range(x_min, x_max + 1):
            if (x, y) in input:
                print(input[(x,y)], end="")
            else:
                print(" ", end="")
        print()

def drop_sand(map, floor=None, sx=500, sy=0):
    if map[(500, 0)] == 'o':
        return False
    if floor is None:
        floors = [(x, y) for x, y in map.keys() if x == sx and y > sy]
        if len(floors) == 0:
            return False
    while True:
        if floor and sy == floor-1:
            map[(sx, sy)] = 'o'
            return True
        if (sx, sy+1) in map: #we hit something
            if (sx-1, sy+1) not in map:
                return drop_sand(map, floor, sx-1, sy+1)
            elif (sx+1, sy+1) not in map:
                return drop_sand(map, floor, sx+1, sy+1)
            else:
                map[(sx, sy)] = 'o'
                return True
        else:
            sy += 1

def part1(map):
    i = 0
    while True:
        if not drop_sand(map):
            return i
        i += 1

def part2(map):
    floor = max([k[1] for k in map.keys()]) + 2
    i = 0
    while True:
        if not drop_sand(map, floor):
            return i
        i += 1

def main():
    day=os.path.basename(__file__).split('.')[0]
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines() if x.strip() != ""]
    map = {}
    map[(500, 0)] = '+'
    for i in input:
        points =  [p for p in [c.split(',') for c in i.split(" -> ")]]
        for p1, p2 in zip(points, points[1:]):
            x1, y1 = int(p1[0]), int(p1[1])
            x2, y2 = int(p2[0]), int(p2[1])
            y_start, y_end = min(y1, y2), max(y1, y2)
            x_start, x_end = min(x1, x2), max(x1, x2)
            for y in range(y_start, y_end+1):
                for x in range(x_start, x_end+1):
                    map[(x, y)] = '#'
    draw_map(map)
    print("Part 1: " + str(part1(map.copy())))
    print("Part 2: " + str(part2(map.copy())))

if __name__ == "__main__":
    main()