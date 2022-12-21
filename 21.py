import os

class Node:
    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.value = None
        self.left = None
        self.right = None
        self.op = None
    def calc(self):
        if self.value:
            #print(f'{self.name} returning {self.value}')
            return self.value
        else:
            l = self.left.calc()
            r = self.right.calc()
            ops = {'+': self.add, '-': self.sub, '*': self.mult, '/': self.div}
            result =  ops[self.op](l, r)
            #print(f'{self.name} {self.job} returns {result}')
            return result

    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mult(self, a, b):
        return a * b
    def div(self, a, b):
        return a / b

def build_tree(nodes, name):
    n = nodes[name]
    if n.job.isnumeric():
        n.value = int(n.job)
    else:
        left, op, right = n.job.split()
        n.left = nodes[left]
        build_tree(nodes, left)
        n.right = nodes[right] 
        build_tree(nodes, right)
        n.op = op

def part1(nodes):
    result = int(nodes['root'].calc())
    return result

def part2(nodes):
    n = nodes['root']
    #find human side
    nodes['humn'].value = None
    human_path = None
    monkey_val = None
    for x in [n.left, n.right]:
        try:
            monkey_val = int(x.calc())
        except:
            human_path = x
    test_val = 1
    prev_sign = None
    inc = 1
    #correct value for part2 is 3343167719435, but this value passes if integer division is used in node
    #nodes['humn'].value=3343167719440
    #print(nodes['root'].left.calc())
    #print(nodes['root'].right.calc())
    while True:
        nodes['humn'].value = test_val
        human_val = int(human_path.calc())
        diff = human_val - monkey_val
        #print(f'test_val:{test_val} diff:{diff}')
        if diff == 0:
            return test_val
        else:
            sign = diff < 0
            if prev_sign is not None:
                if sign == prev_sign: #sign hasn't changed, double increment
                    inc *= 2
                else:
                    inc = 1 if inc < 0 else -1
            test_val += inc
            prev_sign = sign
    return None

def main():
    day=os.path.basename(__file__).split('.')[0]
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines() if x.strip() != ""]

    nodes = {}
    for i in input:
        name, job = [x.strip() for x in i.split(':')]
        n = Node(name, job)
        nodes[name] = n
    build_tree(nodes, 'root')

    print("Part 1: " + str(part1(nodes)))
    print("Part 2: " + str(part2(nodes)))

if __name__ == "__main__":
    main()