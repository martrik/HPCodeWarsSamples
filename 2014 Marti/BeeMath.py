import  math
import sys


for line in sys.stdin:
    days = int(line)
    if days == 0:
        break

    print (days, days*23)



