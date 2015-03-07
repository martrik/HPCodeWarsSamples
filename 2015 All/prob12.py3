import sys

intialAmount = float(sys.stdin.readline())

for line in sys.stdin:
    amountToGet = float(line.strip("\n"))

    if amountToGet == 0:
        break

    if amountToGet+0.5 <= intialAmount:
        if amountToGet%5 == 0:
            intialAmount -= amountToGet + 0.5

    print(str(amountToGet)+" "+str(intialAmount))