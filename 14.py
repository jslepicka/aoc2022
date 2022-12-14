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
        coords = i.split(" -> ")
        last_point = None
        for x, y in [(int(x), int(y)) for x, y in [c.split(',') for c in coords]]:
            if last_point is None:
                map[(x,y)] = "#"
                last_point = (x, y)
                #print(f'start line at {x, y}')
            else:
                if last_point[0] == x: #x coords same, move in y dir
                    y_start, y_end = last_point[1], y
                    #print(f'drawing vertically from {x, y_start} to {x, y_end}')
                    if y_start > y_end:
                        dir = -1
                        y_end -= 1
                    else:
                        dir = 1
                        y_end += 1
                    for yy in range(y_start, y_end, dir):
                        map[(x, yy)] = '#'
                        last_point = (x, yy)
                elif last_point[1] == y: #y coords same, move in x dir
                    x_start, x_end = last_point[0], x
                    #print(f'drawing horizontally from {x_start, y} to {x_end, y}')
                    if x_start > x_end:
                        dir = -1
                        x_end -= 1
                    else:
                        dir = 1
                        x_end += 1
                    for xx in range(x_start, x_end, dir):
                        map[(xx, y)] = '#'
                        last_point = (xx, y)

    print("Part 1: " + str(part1(map.copy())))
    print("Part 2: " + str(part2(map.copy())))

if __name__ == "__main__":
    main()