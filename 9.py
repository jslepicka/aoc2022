import os
from typing import NamedTuple

MOVES = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1)
}

class Coord(NamedTuple):
    x: int
    y: int
    def move(self, dx, dy):
        return Coord(self.x + dx, self.y + dy)

def is_touching(a, b):
    if abs(a.x - b.x) > 1 or abs(a.y - b.y) > 1:
        return False
    return True

def get_next_pos(head, tail):
    x, y = tail
    if head.x != tail.x:
        x = x + 1 if head.x > tail.x else x - 1
    if head.y != tail.y:
        y = y + 1 if head.y > tail.y else y - 1
    return x, y

def simulate_rope(motions, num_knots):
    knot_pos = [Coord(0,0) for _ in range(num_knots)]
    visited = [{Coord(0,0): 1} for _ in range(num_knots)]
    for dir, steps in motions:
        dx, dy = MOVES[dir]
        for _ in range(steps):
            knot_pos[0] = knot_pos[0].move(dx, dy)
            visited[0][knot_pos[0]] = 1
            for k in range(1, num_knots):
                if not is_touching(knot_pos[k], knot_pos[k-1]):
                    knot_pos[k] = Coord(*get_next_pos(knot_pos[k-1], knot_pos[k]))
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