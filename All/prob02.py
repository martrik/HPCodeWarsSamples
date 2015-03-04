import sys

ounce = 28.3495

def calcMass(weight):
    return str(float(weight)*ounce)

input = sys.stdin.readline()
sys.stdout.write(calcMass(input))