import sys

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']

def checIfIsPalindrome(morse):
    size = len(morse)
    half = int(size / 2)
    left = morse[:half]
    right = morse[-half:]
    return left == right[::-1]

for linen in sys.stdin:
    line = linen.strip("\n")

    if line == "Palindrome!":
        break

    clear = ""
    for letter in line:
        if letter.upper() in alphabet:
            clear += letter

    clear = clear.lower()

    palindrme = checIfIsPalindrome(clear)

    if palindrme:
        print('"'+line+'"'+" is a palindrome")
    else:
        print('"'+line+'"'+" is not a palindrome")