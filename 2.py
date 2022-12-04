#convert X,Y,Z -> A,B,C -> 0,1,2
#0 (rock) is beaten by 1 (paper)
#1 (paper) is beaten by 2 (scissors)
#2 (scissors) is beaten by 0 (rock)
#winning play is (their_play + 1) % 3
#losing play is (their_play + 2) % 3

def get_score(their_play, my_play):
    score = 0
    score += my_play + 1
    if their_play == my_play: #draw
        score += 3
    elif my_play == (their_play + 1) % 3: #I win
        score += 6
    return score

def part1(input):
    score = 0
    for round in input:
        their_play = ord(round[0]) - ord('A')
        my_play = ord(round[1]) - ord('X')
        score += get_score(their_play, my_play)
    return score

def part2(input):
    score = 0
    for round in input:
        their_play = ord(round[0]) - ord('A')
        desired_outcome = round[1]
        my_play = their_play

        if desired_outcome == 'X': #I need to lose
            my_play = (their_play + 2) % 3
        elif desired_outcome == 'Z': #I need to win
            my_play = (their_play + 1) % 3
        
        score += get_score(their_play, my_play)
    return score

def main():
    input = []
    with open("2.txt") as file:
        input = [x.split() for x in file.readlines() if x.strip() != ""]

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()