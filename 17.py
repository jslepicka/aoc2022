import os

pieces = [
    [(0, 0), (1, 0), (2, 0), (3, 0)], #line
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)], #plus
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], #backwards L
    [(0, 0), (0, 1), (0, 2), (0, 3)], #I
    [(0, 0), (1, 0), (0, 1), (1, 1)] #square
]

def translate_piece(piece, x, y):
    translated = []
    for p in piece:
        translated.append((p[0] + x, p[1] + y))
    return translated


def run_game(input, iterations, detect_cycle = False):
    sequence_cache = {}
    board = {}
    piece_index = 0
    gas_len = len(input)
    gas_index = 0
    completed = {}
    for i in range(iterations):
        piece = pieces[piece_index]
        piece_index = (piece_index + 1) % (len(pieces))
        #place 2 left of wall and 3 above highest on board
        piece_x = 2
        if len(board.keys()) == 0:
            piece_y = 4
        else:
            piece_y = max([y for x, y in board.keys()]) + 4
        #print(f'spawning piece at {piece_x}, {piece_y}')
        stopped = False
        while not stopped:
            gas = input[gas_index]
            gas_index = (gas_index + 1) % gas_len
            dir = 1 if gas == '>' else -1
            translated = translate_piece(piece, piece_x + dir, piece_y)
            can_shift = True
            for p in translated:
                if p in board or p[0] < 0 or p[0] > 6:
                    can_shift = False
                    break
            if can_shift:
                piece_x += dir

            translated = translate_piece(piece, piece_x, piece_y - 1)

            for p in translated:
                if p in board or p[1] == 0:
                    stopped = True
            if stopped:
                #print(f'placing piece at {piece_x}, {piece_y}')
                placement = translate_piece(piece, piece_x, piece_y)
                for p in placement:
                    board[p] = 1
                a = 1
                top = max(y for x,y in placement)
                complete = True
                #example doesn't seem to have any complete rows, so this doesn't work there.
                #it does work for my puzzle input though.
                for x in range(7):
                    if (x, top) not in board:
                        complete = False
                        break
                if complete:
                    #print(f'flat at iter {i} height {top} piece {piece_index} gas {gas_index}')
                    k = (piece_index, gas_index)
                    if k in completed:
                        #print(f'detected cycle at {i}')
                        last_i, last_top = completed[k]
                        if detect_cycle:
                            return (i, top, i - last_i, top - last_top)
                    
                    completed[k] = (i, top)
            else:
                piece_y -= 1

    return (max(y for x,y in board), None, None, None, None)

def part1(input):
    return run_game(input, 2022)[0]

def part2(input):
    cycle_detected_at, height_at_detected, cycle_len, cycle_height = run_game(input, 10000000, True)
    a = (1_000_000_000_000 - cycle_detected_at) // cycle_len
    b = (1_000_000_000_000 - cycle_detected_at) % cycle_len

    a *= cycle_height
    a += height_at_detected
    extra = run_game(input, cycle_detected_at + b)[0]
    extra -= height_at_detected
    
    return a+extra

def main():
    day=os.path.basename(__file__).split('.')[0]
    with open(day + ".txt") as file:
        input = list(file.readline().strip())

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()