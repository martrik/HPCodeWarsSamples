import sys
import math
goal = int(sys.stdin.readline())
cycles = int(sys.stdin.readline())
winner = []
winnerBet = goal

for i in range(cycles):
    line = sys.stdin.readline().rstrip('\n').split()

    if math.fabs(goal-int(line[0])) < winnerBet:
        winnerBet = math.fabs(goal-int(line[0]))
        winner = []
        winner.append(line[1])

    elif winnerBet == math.fabs(goal-int(line[0])):
         winner.append(line[1])

print(winner)