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
        inMorse += morse[letter]

    return inMorse

#doesn't work yet
def checIfIsPalindrome(possiblePalindrome):
    print(str(possiblePalindrome.__len__()))
    if possiblePalindrome.__len__()%2 == 0:
        left = possiblePalindrome[0, possiblePalindrome.__len__()/2-1]
        right = possiblePalindrome[possiblePalindrome.__len__()/2, possiblePalindrome.__len__()]
    else:
        left = possiblePalindrome[0, int(((possiblePalindrome.__len__()-1)/2)-1)]
        right = possiblePalindrome[(possiblePalindrome.__len__()-1)/2+1, possiblePalindrome.__len__()]

    for i in range(left.__len__()):
        if not left[i] == right[right.__len__()-1-i]:
            return False

    return True

for linen in sys.stdin:
    line = linen.strip().upper()

    if line == ".":
        break

    if checIfIsPalindrome(convertToMorse(line)):
        print(line+" is a MCP")
    else:
        print(line+" is *not* a MCP")