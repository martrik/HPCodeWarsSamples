import math

def p(t):
    return 100 * math.sqrt(t) + 201/(t+1) + 1

while True:
    inp = int(input())
    if inp == 0:
        break
    print(str(inp) + " " +str(math.trunc(p(inp))))