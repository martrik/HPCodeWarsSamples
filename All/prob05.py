import sys

def T(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return T(n-3)+T(n-2)+T(n-1)

for line in sys.stdin:
    x = int(line)
    if(x == -1):
        break

    if x >= 0:
        print(str(T(x)))
