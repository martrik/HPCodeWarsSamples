import sys
import math

for line in sys.stdin:
    x1, y1, x2, y2, x3, y3 = map(float, line.split())

    if(x1 == 0 and x2 == 0 and x3 == 0 and y1 == 0 and y2 == 0 and y3 == 0):
        break

    a = math.sqrt(math.pow((x2-x1), 2)+math.pow((y2-y1), 2))
    b = math.sqrt(math.pow((x3-x2), 2)+math.pow((y3-y2), 2))
    c = math.sqrt(math.pow((x3-x1), 2)+math.pow((y3-y1), 2))

    w = math.acos((math.pow(a, 2)+math.pow(b, 2)-math.pow(c, 2))/(2*a*b))

    print(str(round(a*b*math.sin(w)*0.5, 4)))