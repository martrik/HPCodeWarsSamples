import sys

for linen in sys.stdin:
    line = linen.strip().upper()

    if int(line) == -1:
        break

    count = 0

    for i in range(int(line)+1):
        for j in str(i):
            if j == "1":
                count += 1

    print(str(count))