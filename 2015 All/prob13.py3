import sys

number = int(sys.stdin.readline().strip("\n"))
array = []
dic = {}

for i in range(number):
    line = sys.stdin.readline().strip("\n")

    if line in dic:
        dic[line] += 1
    else:
        dic[line] = 1
        array.append(line)

for i in array:
    print(str(dic[i])+" "+i)