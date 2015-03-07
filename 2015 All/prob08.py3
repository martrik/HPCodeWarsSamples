import sys

firstline = sys.stdin.readline().strip("\n")
width, height = firstline.split()
dic = {}

for i in range(int(height)):
    line = sys.stdin.readline().strip("\n")

    array = line.split()

    for var in array:
        if var in dic:
            dic[var] += 1
        else:
            dic[var] = 1

for f in range(16):
    f += 1
    string = ""

    for c in range(16):
        string += str(dic[str(16*f+c)]) + " "

    print(string.strip(" "))