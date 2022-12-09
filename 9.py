import os

MOVES = {
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

def simulate_rope(motions, num_knots):
    knot_pos = [(0,0) for _ in range(num_knots)]
    visited = [{(0,0): 1} for _ in range(num_knots)]
    for dir, steps in motions:
        dx, dy = MOVES[dir]
        for _ in range(steps):
            knot_pos[0] = knot_pos[0][0] + dx, knot_pos[0][1] + dy
            visited[0][knot_pos[0]] = 1
            for k in range(1, num_knots):
                if not is_touching(knot_pos[k], knot_pos[k-1]):
                    knot_pos[k] = get_next_pos(knot_pos[k-1], knot_pos[k])
                    visited[k][knot_pos[k]] = 1
    return visited

def main():
    day=os.path.basename(__file__).split('.')[0]
    with open(day + ".txt") as file:
        motions = [
            (dir, int(steps)) for dir, steps in [
                motion.split() for motion in [
                    x.strip() for x in file.readlines() if x.strip() != ""
                ]
            ]
        ]
    
    visited = simulate_rope(motions, 10)
    print("Part 1: " + str(len(visited[1])))
    print("Part 2: " + str(len(visited[9])))

if __name__ == "__main__":
    main()