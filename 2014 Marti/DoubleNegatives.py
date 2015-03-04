import sys
import re

negatives = ["DON'T", "CAN'T", "ISN'T", "HAVEN'T", 'CANNOT', "WOULDN'T", "COULDN'T",
"WON'T", 'NO', 'NOT', 'NEVER', 'NOBODY', 'NOWHERE', 'NEITHER', "AIN'T"]

while True:
    line = sys.stdin.readline().rstrip()
    counter = 0
    if line[0] == ".": break
    words = re.findall("[\w']+", line)
    for c in words:
        if c in negatives:
            counter +=1
    print(str(counter)+": "+line)