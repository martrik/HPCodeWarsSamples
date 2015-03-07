import sys

letter = {"I":1, "V":5, "X":10, "L":50, "C" : 100, "D" : 500, "M":1000}

for linen in sys.stdin:

    if linen == ".":
        break

    line = linen.strip("\n")
    result = 0
    ignore = False

    for n in range(len(line)):
        if not ignore:
            if (n+1) < len(line):
                if letter[line[n]] < letter[line[n+1]]:
                    result += letter[line[n+1]] - letter[line[n]]
                    ignore = True

                elif line[n] == "M": result = result + 1000
                elif line[n] == "D": result = result + 500
                elif line[n] == "C": result = result + 100
                elif line[n] == "L": result = result + 50
                elif line[n] == "X": result = result + 10
                elif line[n] == "V": result = result + 5
                elif line[n] == "I": result = result + 1

            elif line[n] == "M": result = result + 1000
            elif line[n] == "D": result = result + 500
            elif line[n] == "C": result = result + 100
            elif line[n] == "L": result = result + 50
            elif line[n] == "X": result = result + 10
            elif line[n] == "V": result = result + 5
            elif line[n] == "I": result = result + 1

        ignore = False

    print(str(result))
