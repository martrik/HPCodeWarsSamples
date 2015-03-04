import sys

repeatTimes = sys.stdin.readline().strip().upper()

for i in range(int(repeatTimes)):
    line = sys.stdin.readline().strip().upper()
    paraules = line.split()

    #problem not working yet
    for i in range(paraules.__len__()):
        if paraules[i] == "IS" and paraules[i+1] == "NOT":
            paraules.remove(i+1)
        elif paraules[i] == "IS" and not paraules[i+1] == "NOT":
            paraules.insert(i+1, "NOT")

    sentence = ""

    for paraula in paraules:
        sentence += paraula + " "

    print(sentence.strip(" ")+".")