import sys

def calcProfit(sold):
    profit = int(sold)*8-95
    if profit >= 0:
        return str(profit)
    else:
        return "0"

sys.stdout.write(calcProfit(sys.stdin.readline()))
