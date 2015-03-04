import sys

morse = {"A": "·-",
         "B": "-···",
         "C": "-·-·",
         "D": "-··",
         "E": "·",
         "F": "··-·",
         "G": "--·",
         "H": "····",
         "I": "··",
         "J": "·---",
         "K": "-·-",
         "L": "·-··",
         "M": "--",
         "N": "-·",
         "O": "---",
         "P": "·--·",
         "Q": "--·-",
         "R": "·-·",
         "S": "···",
         "T": "-",
         "U": "··-",
         "V": "···-",
         "X": "-··-",
         "Y": "-·--",
         "Z": "--··"}

#converting to morse without spaces
def convertToMorse(toConvert):
    inMorse = ""
    for letter in toConvert:
        if letter in morse:
            inMorse += morse[letter]

    return inMorse

def checIfIsPalindrome(morse):
    size = len(morse)
    half = int(size / 2)
    left = morse[:half]
    right = morse[-half:]
    return left == right[::-1]

for linen in sys.stdin:
    line = linen.strip().upper()

    if line == ".":
        break

    if checIfIsPalindrome(convertToMorse(line)):
        print(line+" is a MCP")
    else:
        print(line+" is *not* a MCP")