import sys

repeatTimes = sys.stdin.readline().strip().upper()

for i in range(int(repeatTimes)):
    line = sys.stdin.readline().strip("\n")
    paraules = line.split()

    #problem not working yet
    for i in range(len(paraules)):
        if paraules[i] == "is" and paraules[i+1] == "not":
            paraules.remove(i+1)
        elif paraules[i] == "is" and not paraules[i+1] == "not":
            paraules.insert(i+1, "not")

    sentence = ""

    for paraula in paraules:
        sentence += paraula + " "

    print(sentence.strip(" ")+".")