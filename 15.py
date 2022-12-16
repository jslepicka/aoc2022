import os
import re
from multiprocessing import Pool

def merge_ranges(ranges):
    ranges = iter(sorted(ranges))
    ret = [next(ranges)]
    for r in ranges:
        start, end = r
        prev_start = ret[-1][0]
        prev_end = ret[-1][1]
        if start > prev_end:
            ret.append(r)
        else:
            ret[-1] = prev_start, max(prev_end, end)
    return ret

def get_ranges(sensors, beacons, row):
    ranges = []
    for s, b in zip(sensors, beacons):
        sx, sy = s[0], s[1]
        bx, by = b[0], b[1]
        #print(f'sensor: {[sx, sy]}, beacon: {[bx, by]}')
        s_to_b = abs(sx-bx) + abs(sy-by)
        #print(f'sensor to beacon distance: {s_to_b}')
        s_to_r = abs(row-sy)
        if s_to_r <= s_to_b:
            num_points = 1 + (s_to_b - s_to_r) * 2
            #print(f"touches row: {d}")
            #print(f'points: {num_points}')
            r1 = sx-num_points//2
            r2 = sx+num_points//2 + 1
            ranges.append((r1, r2))
    return ranges

def part1(sensors, beacons, row):
    ranges = get_ranges(sensors, beacons, row)
    merged = merge_ranges(ranges)
    locations = 0
    for x in merged:
        locations += x[1] - x[0]
    for x in merged:
        for b in set(beacons):
            if b[1] == row and b[0] >= x[0] and b[0] <= (x[1]+1):
                locations -= 1
    return locations

def part2(sensors, beacons):
    for row in (range(0, 4000000+1)):
        ranges = get_ranges(sensors, beacons, row)
        merged = merge_ranges(ranges)
        if len(merged) > 1:
            return merged[0][1] * 4000000 + row
    return None

def p2thread(sensors, beacons, start, end):
    for row in (range(start, end)):
        ranges = get_ranges(sensors, beacons, row)
        d = list(merge_ranges(ranges))
        if len(d) > 1:
            return d[0][1] * 4000000 + row
    return None   

def part2_mt(sensors, beacons, max_row):
    num_threads = 16
    if max_row % num_threads != 0:
        print("max_row not evenly divisible by # of threads")
        return None
    rows_per_thread = 4000000 // num_threads
    thread_args = []
    for i in range(num_threads):
        start = i * rows_per_thread
        end = start + rows_per_thread
        if i == num_threads - 1:
            end += 1
        thread_args.append((sensors, beacons, start, end))
    with Pool(num_threads) as p:
        ret = p.starmap(p2thread, thread_args)
    for x in ret:
        if x is not None:
            return x
    return None

def main():
    day=os.path.basename(__file__).split('.')[0]
    sensors = []
    beacons = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines() if x.strip() != ""]
        for i in input:
            sx, sy, bx, by = re.findall(r'-*\d+', i)
            sensors.append((int(sx), int(sy)))
            beacons.append((int(bx), int(by)))

    print("Part 1: " + str(part1(sensors, beacons, 2000000)))
    print("Part 2: " + str(part2_mt(sensors, beacons, 4000000)))

if __name__ == "__main__":
    main()