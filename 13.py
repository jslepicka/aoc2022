import os
import functools
        
def check_order(a, b):
    p1 = a.copy()
    p2 = b.copy()
    while p1 and p2:
        left = p1.pop(0)
        right = p2.pop(0)
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return 1
            elif right < left:
                return -1
        elif isinstance(left, int) or isinstance(right, int):
            if isinstance(left, int):
                result=check_order([left], right)
            else:
                result=check_order(left, [right])
            if result is not None:
                return result
        else:
            result = check_order(left, right)
            if result is not None:
                return result
    if len(p1) == 0 and len(p2) == 0:
        return None
    elif len(p1) == 0:
        return 1
    elif len(p2) == 0:
        return -1

def part1(input):
    result = 0
    for i, x in enumerate(input):
        if check_order(x[0],x[1]) == 1:
            result += i + 1
    return result

def part2(input):
    all_packets = []
    all_packets.append([[2]])
    all_packets.append([[6]])
    for x in input:
        all_packets.append(x[0])
        all_packets.append(x[1])
    sorted_packets = sorted(all_packets, key=functools.cmp_to_key(check_order), reverse=True)
    return (sorted_packets.index([[2]])+1) * (sorted_packets.index([[6]])+1)

def main():
    input = []
    day=os.path.basename(__file__).split('.')[0]
    with open(day + ".txt") as file:
        for i in file.read().split("\n\n"):
            list1, list2 = i.splitlines()
            input.append([eval(list1), eval(list2)])

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()