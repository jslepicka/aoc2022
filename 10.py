import os

class Cpu:
    cycles = {
        "noop": 1,
        "addx": 2
    }

    def __init__(self, program):
        self.program = program
        self.reset()
    
    def reset(self):
        self.pc = 0
        self.available_cycles = 0
        self.required_cycles = 0
        self.opcode = None
        self.operands = None
        self.fetch_opcode = True
        self.x = 1

    def run(self, num_cycles):
        for _ in range(num_cycles):
            self.clock()

    def clock(self):
        self.available_cycles += 1

        if self.fetch_opcode:
            self.opcode, *self.operands = self.program[self.pc].split()
            self.pc += 1
            self.required_cycles = self.cycles[self.opcode]
            self.fetch_opcode = False
        
        if self.required_cycles <= self.available_cycles:
            self.available_cycles -= self.required_cycles
            self.fetch_opcode = True
            self.execute()
        
    def execute(self):
        match self.opcode:
            case 'noop':
                pass
            case 'addx':
                self.x += int(self.operands[0])

def part1(input):
    cpu = Cpu(input)
    current_cycle = 0
    stops = [20, 60, 100, 140, 180, 220]
    signal_strength = 0
    for stop in stops:
        num_cycles = stop - current_cycle - 1
        cpu.run(num_cycles)
        current_cycle += num_cycles
        signal_strength += cpu.x * (current_cycle+1)
    return signal_strength

def part2(input):
    out = ""
    cpu = Cpu(input)
    for y in range(6):
        for x in range(40):
            out += '\u2588' if abs(x-cpu.x) < 2 else ' '
            cpu.clock()
        out += '\n'
    return out

def main():
    day=os.path.basename(__file__).split('.')[0]
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines() if x.strip() != ""]

    print("Part 1: " + str(part1(input)))
    print("Part 2:\n" + str(part2(input)))

if __name__ == "__main__":
    main()