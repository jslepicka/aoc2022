import os

def snafu_to_decimal(snafu):
    digits = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
    place = 1
    number = 0
    for i in reversed(snafu):
        digit = digits[i]
        number += digit * place
        place *= 5
    return number

def decimal_to_snafu(decimal):
    ret = ""
    while decimal != 0:
        ret += "012=-"[decimal % 5]
        decimal = (decimal + 2) // 5
    return ''.join(reversed(ret))

def part1(input):
    ret = 0
    for i in input:
        ret += snafu_to_decimal(i)
    return decimal_to_snafu(ret)

def part2(input):
    return None

def main():
    day=os.path.basename(__file__).split('.')[0]
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines() if x.strip() != ""]

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()