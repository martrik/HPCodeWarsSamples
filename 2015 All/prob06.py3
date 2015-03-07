import sys

alphabet = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
vowels = ["A", "E", "I", "O", "U"]

v = 0
c = 0

for line in sys.stdin:
    text = line.upper()
    for letter in text:
        if letter == "#":
            break

        if letter in alphabet:
            c += 1
        elif letter in vowels:
            v += 1

print("Consonants: "+str(c))
print("Vowels: "+str(v))

if c == 0:
    print("Ratio: Infinite")
else:
    print("Ratio: "+str(round(v/c, 3)))