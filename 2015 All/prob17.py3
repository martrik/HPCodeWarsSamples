import sys

number = int(sys.stdin.readline().strip("\n"))
conversions = {"EUR":1.00}

def currToEuro(curr, val):
    return val/conversions[curr]

def EuroToCurr(curr, val):
    return val*conversions[curr]

for i in range(number):
    conversion = sys.stdin.readline().strip("\n")
    conv, name = conversion.split()

    conversions[name]=float(conv)

for linen in sys.stdin:
    line = linen.strip("\n")

    if line == ".":
        break

    valToConvert, curr1, inc, curr2 = line.split()

    resultat = EuroToCurr(curr2, currToEuro(curr1, float(valToConvert)))

    print(str(valToConvert)+" "+curr1+" = "+str(round(resultat, 2))+" "+curr2)