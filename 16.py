import os
import re
from multiprocessing import Pool

def solve(valves, valve_to_int, minutes, valve_states = 0):
    stack = []
    stack.append(('AA', 0, valve_states)) #loc, minute, pressure_loss, valve_states
    prev_states = {}

    for minute in range(minutes):
        next_stack = []
        for loc, pressure_loss, valve_states in stack:
            #if we've already been at this location, with this valve_state, we don't
            #need to go down this path again
            state = (loc, valve_states)
            if state in prev_states:
                continue
            prev_states[state] = pressure_loss
            if valves[loc]['flow_rate'] != 0:
                v = valve_to_int[loc]
                if v & valve_states == 0:
                    loss_over_time = valves[loc]['flow_rate'] * (minutes - minute - 1)
                    #we have an option to turn on the valve without moving
                    next_stack.append((loc, pressure_loss+loss_over_time,valve_states | v))
            next = valves[loc]['next']
            for n in next:
                next_stack.append((n, pressure_loss,valve_states))
        stack = next_stack

    return max(prev_states.values())

def part1(valves, valve_to_int):
    return solve(valves, valve_to_int, 30)

def p2thread(valves, valve_to_int, start, end):
    results = []
    for i in range(start, end):
        me = solve(valves, valve_to_int, 26, i & 0x7FFF)
        elephant = solve(valves, valve_to_int, 26, (~i) & 0x7FFF)
        loss = me + elephant
        results.append(loss)
    return max(results)
        
def part2(valves, valve_to_int):
    num_threads = 16
    count_per_thread = 32768//num_threads
    thread_args = []
    for i in range(num_threads):
        start = i * count_per_thread
        end = start + count_per_thread
        thread_args.append((valves, valve_to_int, start, end))
    with Pool(num_threads) as p:
        result = p.starmap(p2thread, thread_args)
    return max(result)

def main():
    valve_to_int = {}
    valves = {}
    valve_states = {}
    day=os.path.basename(__file__).split('.')[0]
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines() if x.strip() != ""]
        for i in input:
            m = re.match(r'Valve (..).+=(\d+);.+valve[s]* (.+)$', i)
            if m:
                valve = m.group(1)
                flow_rate = int(m.group(2))
                next = [x.strip() for x in m.group(3).split(",")]
                valves[valve] = {"flow_rate": flow_rate, "next": next}
                valve_states[valve] = False
    i = 0
    for v in sorted(valves):
        if valves[v]['flow_rate'] != 0:
            valve_to_int[v] = 1 << i
            i += 1
    print("Part 1: " + str(part1(valves, valve_to_int)))
    print("Part 2: " + str(part2(valves, valve_to_int)))

if __name__ == "__main__":
    main()