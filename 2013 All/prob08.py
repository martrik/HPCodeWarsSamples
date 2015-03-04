import sys

for linen in sys.stdin:
    line = linen.strip().upper()

    if line == ".":
        break

    dic = {}
    string = " USES DISTINCT LETTERS"

    for letter in line:
        if letter in dic:
            dic[letter] += 1
        else:
            dic[letter] = 1

    for key in dic:
        if dic[key] >= 2:
            string = " DOES NOT USE DISTINCT LETTERS"

    print(line + string)