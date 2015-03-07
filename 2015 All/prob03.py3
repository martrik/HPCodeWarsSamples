import sys

input = int(sys.stdin.readline())
name = sys.stdin.readline().strip("\n")

if input <= 2:
    age = input *10
else:
    age = 20 +(input -2)*4

print(name+" is "+str(age)+" human years old")