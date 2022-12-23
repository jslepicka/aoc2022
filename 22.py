import os

def part1(bb, path):
    board = {}
    for y, b in enumerate(bb.split("\n"), 1):
        for x, s in enumerate(b, 1):
            if s != ' ':
                board[(x, y)] = s

    dirs = {'R': (1, 0), 'D': (0, 1), 'L': (-1, 0), 'U': (0, -1)}
    y = 1
    x = min([x for x, y in board if y == 1])
    dir = 'R'
    
    for p in path:
        if isinstance(p, int):
            steps = p
            for _ in range(steps):
                x2, y2 = x + dirs[dir][0], y + dirs[dir][1]
                if (x2, y2) in board:
                    if board[(x2, y2)] == '#': #stop
                        break
                    else:
                        x, y = x2, y2
                else:
                    if dir == 'R':
                        x2 = min([xx for xx, yy in board if yy == y])
                    elif dir == 'L':
                        x2 = max([xx for xx, yy in board if yy == y])
                    elif dir == 'U':
                        y2 = max([yy for xx, yy in board if xx == x])
                    elif dir == 'D':
                        y2 = min([yy for xx, yy in board if xx == x])
                    if board[(x2, y2)] == '#':
                        break
                    else:
                        x, y = x2, y2
        else:
            dir_index = list(dirs.keys()).index(dir)
            dir_index = (dir_index + (1 if p == 'R' else -1)) % len(dirs.keys())
            dir = list(dirs.keys())[dir_index]


    
    return 1000 * y + 4 * x + list(dirs.keys()).index(dir)

def part2(bb, path):
    boards = {}
    for y, b in enumerate(bb.split("\n"), 1):
        for x, s in enumerate(b, 1):
            board_number = ((y-1) // 50) * 3 + (x - 1) // 50
            if board_number not in boards:
                boards[board_number] = {}
            if s != ' ':
                xx = ((x - 1) % 50) + 1
                yy = ((y - 1) % 50) + 1
                boards[board_number][(xx, yy)] = s
                #print(f'{board_number}: {xx},{yy} {s}')
    dirs = {'R': (1, 0), 'D': (0, 1), 'L': (-1, 0), 'U': (0, -1)}

    board_number = 1
    y = 1
    x = min([x for x, y in boards[board_number] if y == 1])
    dir = 'R'
    next_dir = None
    next_board = None
    for p in path:
        if isinstance(p, int):
            steps = p
            for _ in range(steps):
                x2, y2 = x + dirs[dir][0], y + dirs[dir][1]
                if (x2, y2) in boards[board_number]:
                    if boards[board_number][(x2, y2)] == '#': #stop
                        break
                    else:
                        x, y = x2, y2
                else:
                    if board_number == 1:
                        if dir == 'R':
                            next_board = 2
                            next_dir = 'R'
                            x2 = 1
                            y2 = y
                        elif dir == 'D':
                            next_board = 4
                            next_dir = 'D'
                            x2 = x
                            y2 = 1
                        elif dir == 'L':
                            next_board = 6
                            next_dir = 'R'
                            x2 = 1
                            y2 = 51 - y
                        elif dir == 'U':
                            next_board = 9
                            next_dir = 'R'
                            x2 = 1
                            y2 = x
                    elif board_number == 2:
                        if dir == 'R':
                            next_board = 7
                            next_dir = 'L'
                            x2 = 50
                            y2 = 51 - y
                        elif dir == 'D':
                            next_board = 4
                            next_dir = 'L'
                            x2 = 50
                            y2 = x
                        elif dir == 'L':
                            next_board = 1
                            next_dir = 'L'
                            x2 = 50
                            y2 = y
                        elif dir == 'U':
                            next_board = 9
                            next_dir = 'U'
                            x2 = x
                            y2 = 50
                    elif board_number == 4:
                        if dir == 'R':
                            next_board = 2
                            next_dir = 'U'
                            x2 = y
                            y2 = 50
                        elif dir == 'D':
                            next_board = 7
                            next_dir = 'D'
                            x2 = x
                            y2 = 1
                        elif dir == 'L':
                            next_board = 6
                            next_dir = 'D'
                            x2 = y
                            y2 = 1
                        elif dir == 'U':
                            next_board = 1
                            next_dir = 'U'
                            x2 = x
                            y2 = 50
                    elif board_number == 6:
                        if dir == 'R':
                            next_board = 7
                            next_dir = 'R'
                            x2 = 1
                            y2 = y
                        elif dir == 'D':
                            next_board = 9
                            next_dir = 'D'
                            x2 = x
                            y2 = 1
                        elif dir == 'L':
                            next_board = 1
                            next_dir = 'R'
                            x2 = 1
                            y2 = 51 - y
                        elif dir == 'U':
                            next_board = 4
                            next_dir = 'R'
                            x2 = 1
                            y2 = x
                    elif board_number == 7:
                        if dir == 'R':
                            next_board = 2
                            next_dir = 'L'
                            x2 = 50
                            y2 = 51 - y
                        elif dir == 'D':
                            next_board = 9
                            next_dir = 'L'
                            x2 = 50
                            y2 = x
                        elif dir == 'L':
                            next_board = 6
                            next_dir = 'L'
                            x2 = 50
                            y2 = y
                        elif dir == 'U':
                            next_board = 4
                            next_dir = 'U'
                            x2 = x
                            y2 = 50
                    elif board_number == 9:
                        if dir == 'R':
                            next_board = 7
                            next_dir = 'U'
                            x2 = y
                            y2 = 50
                        elif dir == 'D':
                            next_board = 2
                            next_dir = 'D'
                            x2 = x
                            y2 = 1
                        elif dir == 'L':
                            next_board = 1
                            next_dir = 'D'
                            x2 = y
                            y2 = 1
                        elif dir == 'U':
                            next_board = 6
                            next_dir = 'U'
                            x2 = x
                            y2 = 50
                    else:
                        print("how did I get here?")
                        return
                    if boards[next_board][(x2, y2)] == '#':
                        break
                    else:
                        board_number = next_board
                        dir = next_dir
                        x, y = x2, y2
        else:
            dir_index = list(dirs.keys()).index(dir)
            dir_index = (dir_index + (1 if p == 'R' else -1)) % len(dirs.keys())
            dir = list(dirs.keys())[dir_index]
    board_y = (board_number // 3) * 50
    board_x = (board_number % 3) * 50

    return 1000 * (board_y + y) + 4 * (board_x + x) + list(dirs.keys()).index(dir)

def main():
    day=os.path.basename(__file__).split('.')[0]
    with open(day + ".txt") as file:
        bb, pp = file.read().split("\n\n")
    board = {}
    num = ""
    path = []
    for p in pp:
        if p == 'L' or p == 'R':
            if num != "":
                path.append(int(num))
                num = ""
                path.append(p)
        else:
            num += p
    if num != "":
        path.append(int(num))

    print("Part 1: " + str(part1(bb, path)))
    print("Part 2: " + str(part2(bb, path)))

if __name__ == "__main__":
    main()