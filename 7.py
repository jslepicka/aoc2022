import os

class dentry:
    def __init__(self, parent, name):
        self.name = name
        self.parent = parent
        self.children = {}
        self.size = 0
        if parent is None:
            self.path = "/"
        elif parent.path == "/":
            self.path = "/" + self.name
        else:
            self.path = self.parent.path + "/" + self.name
            
    def add_size(self, size):
        self.size += size
        if self.parent is not None:
            self.parent.add_size(size)

    def mkdir(self, dir):
        newdir = dentry(self, dir)
        self.children[dir] = newdir
        return newdir

def scan_disk(input):
    found_dirs = {}
    root = dentry(None, "/")
    found_dirs["/"] = root
    curdir = root
    for i in [i.split() for i in input]:
        if i[0] == "$":
            if i[1] == "cd":
                dir = i[2]
                if dir == "/":
                    curdir = root
                elif dir == "..":
                    curdir = curdir.parent
                else:
                    if dir in curdir.children:
                        curdir = curdir.children[dir]
                    else:
                        curdir = curdir.mkdir(dir)
                        found_dirs[curdir.path] = curdir
        else:
            if i[0] == "dir":
                dir = i[1]
                if dir not in curdir.children:
                    newdir = curdir.mkdir(dir)
                    found_dirs[newdir.path] = newdir
            else:
                size = int(i[0])
                curdir.add_size(size)
    return found_dirs  

def part1(found_dirs):
    total = 0
    for dir in found_dirs:
        size = found_dirs[dir].size
        if size <= 100000:
            total += size
    return total

def part2(found_dirs):
    total_disk_space = 70000000
    needed_space = 30000000
    unused_space = total_disk_space - found_dirs["/"].size

    sorted_dirs = dict(sorted(found_dirs.items(), key=lambda item: item[1].size))
    for dir in sorted_dirs:
        size = sorted_dirs[dir].size
        if unused_space + size >= needed_space:
            return size
    return None

def main():
    day=os.path.basename(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines() if x.strip() != ""]
    
    found_dirs = scan_disk(input)
    print("Part 1: " + str(part1(found_dirs)))
    print("Part 2: " + str(part2(found_dirs)))

if __name__ == "__main__":
    main()