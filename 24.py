import os
from copy import deepcopy

height = 0
width = 0
valleys = {}
blizzards = {}

def draw(valley):
    for y in range(height):
        for x in range(width):
            print(valley[(x, y)], end="")
        print()

def get_valley(time):
    if time in valleys:
        return valleys[time]
    else:
        valley = {}
        for y in range(height):
            for x in range(width):
                if (x, y) in blizzards:
                    new_x = (x + blizzards[(x,y)][0] * time) % width
                    new_y = (y + blizzards[(x,y)][1] * time) % height
                    valley[(new_x,new_y)] = 'B'
        for y in range(height):
            for x in range(width):
                if (x, y) not in valley:
                    valley[(x, y)] = '.'
        valleys[time] = valley
        return valley

def go(start_time = 1, reverse=False):
    start = (0, -1)
    end = (width - 1, height)
    if reverse:
        start, end = end, start
    stack = [(start, start_time)]
    dirs = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    visited = set()
    while stack:
        e, steps = stack.pop(0)
        if e == end:
            return steps - 1
        valley = get_valley(steps)
        for d in dirs:
            new_e = (e[0] + d[0], e[1] + d[1])
            if new_e == end or new_e == start or (new_e in valley and valley[new_e] == '.'):
                if (new_e, steps + 1) not in visited:
                    visited.add((new_e, steps + 1))
                    stack.append((new_e, steps + 1))

def part1():
    return go()

def part2():
    a = go()
    b = go(a, True)
    c = go(b)
    return c

def main():
    global height
    global width
    global valleys
    global blizzards
    day=os.path.basename(__file__).split('.')[0]
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines() if x.strip() != ""]
    
    for y, line in enumerate(input[1:-1]):
        height = y + 1
        width = len(line) - 2
        for x, object in enumerate(line[1:-1]):
            dir = None
            if object == '>':
                dir = (1, 0)
            elif object == '<':
                dir = (-1, 0)
            elif object == '^':
                dir = (0, -1)
            elif object == 'v':
                dir = (0, 1)
            if dir:
                blizzards[(x, y)] = dir

    print("Part 1: " + str(part1()))
    print("Part 2: " + str(part2()))

if __name__ == "__main__":
    main()