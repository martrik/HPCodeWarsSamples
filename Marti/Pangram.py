import sys

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']

while True:
    counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0]
    line = sys.stdin.readline().rstrip()
    if line == ".":
        break
    else:
        for c in line:
            if c.isalpha():
                counter[alphabet.index(c)] += 1

    label = "PERFECT: "

    for i in counter:
        if i > 1:
            label = "PANGRAM: "
        elif i == 0:
            label = "NEITHER: "

    print(label + line)





