import os

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get_path_len(heightmap, start_pos, end_pos):
    stack = []
    visited = {}
    stack.append((start_pos, 0))
    visited[start_pos] = 1
    while stack:
        pos, step = stack.pop(0)
        height = heightmap[pos]
        if pos == end_pos:
            return step
        for dx, dy in dirs:
            next = pos[0] + dx, pos[1] + dy
            if next in heightmap and next not in visited:
                next_height = heightmap[next]
                if next_height - height < 2:
                    visited[next] = 1
                    stack.append((next, step + 1))
    return None

def part1(heightmap, start_pos, end_pos):
    return get_path_len(heightmap, start_pos, end_pos)

def part2(heightmap, end_pos):
    starting_positions = []
    for pos in heightmap:
        if heightmap[pos] == 0:
            starting_positions.append(pos)
    return min(path_len for path_len in [
            get_path_len(heightmap, pos, end_pos) for pos in starting_positions
        ] if path_len is not None)

def main():
    heightmap = {}
    day=os.path.basename(__file__).split('.')[0]
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines() if x.strip() != ""]
        for y, line in enumerate(input):
            for x, height in enumerate(line):
                if height == 'S':
                    height = 'a'
                    start_pos = (x, y)
                elif height == 'E':
                    height = 'z'
                    end_pos = (x, y)
                heightmap[(x,y)] = ord(height) - ord('a')

    print("Part 1: " + str(part1(heightmap, start_pos, end_pos)))
    print("Part 2: " + str(part2(heightmap, end_pos)))

if __name__ == "__main__":
    main()