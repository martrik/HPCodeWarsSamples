import sys

mile = 1.609

miles = float(sys.stdin.readline())

print(str(miles)+" miles are "+str(round(miles*mile, 2))+" kilometers")