import sys

letter = {"M":10000, "C":1000, "H":100, "D":10, "P" : 5, "I" : 1}
count = int(sys.stdin.readline())

for x in range(count):
    line = sys.stdin.readline().rstrip()
    result = ""
    if line.isdigit():
        factors = []
        exponent = len(line)
        for c in line:
            exponent -= 1
            factor = int(int(c)*10**(exponent))
            factors.append(factor)
        for n in factors:
            new = ""
            if n % 10000 == 0: new = 'M' * int(n/10000)
            elif n % 1000 == 0: new = 'C'* int((n/1000))
            elif n % 100 == 0: new = 'H'* int((n/100))
            elif n % 10 == 0: new = 'D'* int((n/10))
            elif n % 5 == 0: new = 'P'* int((n/5))
            elif n % 1 == 0: new = 'I'* int((n/1))

            if len(new) >= 5:
                if new[0] == "I": result = result + "P" + new[0]*(len(new)-5)
                else: result = result + "P" + new[0]*(len(new)-4)

            else: result = result + new

    else:
        result = 0
        ignore = False
        for n in range(len(line)):
            if ignore == False:
                if line[n] == "P":
                    if ((n+1) < len(line)):
                        if (line[n+1] == "I"): result = result + 5
                        else:
                            ignore = True
                            result = result + letter[line[n+1]]*5
                    else: result = result + 5
                elif line[n] == "M": result = result + 10000
                elif line[n] == "C": result = result + 1000
                elif line[n] == "H": result = result + 100
                elif line[n] == "D": result = result + 10
                elif line[n] == "I": result = result + 1
            else: ignore = False

    print(result)
