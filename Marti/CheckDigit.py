import sys

cicles = int(sys.stdin.readline())

for i in range(cicles):
    line = sys.stdin.readline().rstrip('\n')
    checkNumber = 0
    currentDigit = 1
    for i in line:
        if i.isdigit():
            value = int(i)
            if (currentDigit % 2 == 0):
                checkNumber += value
            else:
                checkNumber += value*3
            currentDigit += 1
    if checkNumber%10 == 0:
        print(line, 0)
    else: print(line, 10 - checkNumber%10)




