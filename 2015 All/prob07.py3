import sys

for linen in sys.stdin:
    line = linen.strip("\n")

    if line == ".":
        break

    resultat = ""
    for letter in line:
        if letter == "G":
            resultat += "C"
        elif letter == "C":
            resultat += "G"
        elif letter == "A":
            resultat += "T"
        elif letter == "T":
            resultat += "A"

    girada = resultat[::-1]

    print(girada)