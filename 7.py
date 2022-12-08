import os
from collections import defaultdict

def scan_disk(input):
    dir_sizes = defaultdict(int)
    path = []
    for i in [i.split() for i in input]:
        print(path)
        if i[0] == "$":
            if i[1] == "cd":
                dir = i[2]
                if dir == "/":
                    path = ["/"]
                elif dir == "..":
                    path.pop()
                else:
                    path.append((path[-1] if path[-1] != "/" else "") + "/" + dir)
        else:
            if i[0] != "dir":
                size = int(i[0])
                for p in path:
                    dir_sizes[p] += size
    return dir_sizes

def part1(dir_sizes):
    total = 0
    for dir in dir_sizes:
        size = dir_sizes[dir]
        if size <= 100000:
            total += size
    return total

def part2(dir_sizes):
    total_disk_space = 70000000
    needed_space = 30000000
    unused_space = total_disk_space - dir_sizes["/"]

    sorted_dirs = dict(sorted(dir_sizes.items(), key=lambda item: item[1]))
    for dir in sorted_dirs:
        size = sorted_dirs[dir]
        if unused_space + size >= needed_space:
            return size
    return None

def main():
    day=os.path.basename(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines() if x.strip() != ""]
    
    dir_sizes = scan_disk(input)
    print("Part 1: " + str(part1(dir_sizes)))
    print("Part 2: " + str(part2(dir_sizes)))

if __name__ == "__main__":
    main()