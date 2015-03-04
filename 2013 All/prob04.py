import sys
import math

velocitat = float(sys.stdin.readline())
angle = float(sys.stdin.readline())*math.pi/180

print(str(math.pow(velocitat, 2)*math.sin(angle*2)/9.81))