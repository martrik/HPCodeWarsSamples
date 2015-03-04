import sys
energy = [6,2,5,5,4,5,6,3,7,6]

cycles = int(sys.stdin.readline())

for i in range(cycles):
    line = sys.stdin.readline().rstrip('\n')
    total = 0
    for c in line:
        if c == ":":
            total += 20
        else:
             total += (energy[int(c)] * 15)
    print(total, "milliamps")





