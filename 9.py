import os

moves = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1)
}

def is_touching(a, b):
    if abs(a[0] - b[0]) > 1:
        return False
    if abs(a[1] - b[1]) > 1:
        return False
    return True

def get_next_pos(head, tail):
    x, y = tail
    if head[0] != tail[0]:
        x = x + 1 if head[0] > tail[0] else x - 1
    if head[1] != tail[1]:
        y = y + 1 if head[1] > tail[1] else y - 1
    return x, y

def simulate_rope(input, num_knots):
    knot_pos = [(0,0) for _ in range(num_knots)]
    visited = [{(0,0): 1} for _ in range(num_knots)]
    for i in input:
        dir, steps = i
        dx, dy = moves[dir]
        for _ in range(steps):
            knot_pos[0] = knot_pos[0][0] + dx, knot_pos[0][1] + dy
            visited[0][knot_pos[0]] = 1
            for k in range(1, num_knots):
                if not is_touching(knot_pos[k], knot_pos[k-1]):
                    knot_pos[k] = get_next_pos(knot_pos[k-1], knot_pos[k])
                    visited[k][knot_pos[k]] = 1
    return len(visited[-1])

def part1(input):
    return simulate_rope(input, 2)

def part2(input):
    return simulate_rope(input, 10)

def main():
    day=os.path.basename(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [
            (dir, int(steps)) for dir, steps in [
                motions.split() for motions in [
                    x.strip() for x in file.readlines() if x.strip() != ""
                ]
            ]
        ]

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()