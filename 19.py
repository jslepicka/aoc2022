import os
import re
from collections import defaultdict
from multiprocessing import Pool
from math import prod
from itertools import repeat

def solve(blueprint, minutes, part2=False):
    blueprint_num, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = [int(x) for x in re.findall(r'\d+', blueprint)]
    #print(f'blueprint {blueprint_num}')
    #print(ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian)
    max_ore = max(ore_ore, clay_ore, obsidian_ore, geode_ore)

    stack = []
    stack.append((0, 1, 0, 0, 0, 0, 0, 0, 0))
    best = defaultdict(int)
    prev_states = {}
    while stack:
        minute, o_r, c_r, ob_r, g_r, o_i, c_i, ob_i, g_i = stack.pop(0)
        state = (minute, o_r, c_r, ob_r, g_r, o_i, c_i, ob_i, g_i)
        best[minute] = max(best[minute], g_i)
        if state in prev_states:
            continue
        prev_states[state] = 1
        if minute <= minutes and g_i >= best[minute] - 1: #have to subtract one here (or remove check completely) or I get an off by one error in part 2 blueprint 2.  ick.
            if ob_i >= geode_obsidian and o_i >= geode_ore:
                k = (minute + 1, o_r, c_r, ob_r, g_r + 1, o_i + o_r - geode_ore, c_i + c_r, ob_i + ob_r - geode_obsidian, g_i + g_r)
                stack.insert(0, k)
                continue
            else:
                if o_i >= obsidian_ore and c_i >= obsidian_clay and ob_r < geode_obsidian:
                    k = (minute + 1, o_r, c_r, ob_r + 1, g_r, o_i + o_r - obsidian_ore, c_i + c_r - obsidian_clay, ob_i + ob_r, g_i + g_r)
                    stack.insert(0, k)
                if o_i >= clay_ore and c_r < obsidian_clay:
                    k = (minute + 1, o_r, c_r + 1, ob_r, g_r, o_i + o_r - clay_ore, c_i + c_r, ob_i + ob_r, g_i + g_r)
                    stack.insert(0, k)
                if o_i >= ore_ore and o_r < max_ore:
                    k = (minute + 1, o_r + 1, c_r, ob_r, g_r, o_i + o_r - ore_ore, c_i + c_r, ob_i + ob_r, g_i + g_r)
                    stack.insert(0, k)
                k = (minute + 1, o_r, c_r, ob_r, g_r, o_i + o_r, c_i + c_r, ob_i + ob_r, g_i + g_r)
                stack.insert(0, k)
    quality = best[minutes] if part2 else best[minutes] * blueprint_num
    return quality

def part1(input):
    num_threads = 16
    with Pool(num_threads) as p:
        result = p.starmap(solve, zip(input, repeat(24)))
    return sum(result)

def part2(input):
    num_threads = 16
    with Pool(num_threads) as p:
        result = p.starmap(solve, zip(input[:3], repeat(32), repeat(True)))
    return prod(result)

def main():
    day=os.path.basename(__file__).split('.')[0]
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines() if x.strip() != ""]

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()