import sys
import math

for line in sys.stdin:
    minutesAfter = int(line)

    if minutesAfter == -1:
        break

    minutes = math.trunc(minutesAfter/5)

    if not minutesAfter%5 == 0:
        minutes += 1

    hour = 12 - minutes

    minutesStr = str(minutesAfter)

    if minutesStr.__len__() == 1:
        print(str(hour)+":0"+str(minutesAfter))
    else:
        print(str(hour)+":"+str(minutesAfter))
