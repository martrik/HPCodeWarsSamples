abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

while True:
    inp = input()

    if(inp == "."):
        break

    isPerfect = True
    isPangram = True

    for i in abc:
        count = inp.count(i)
        if count == 0:
            isPerfect = False
            isPangram = False
        elif count > 1:
            isPerfect = False

    if isPerfect:
        print("PERFECT: "+inp)
    elif isPangram:
        print("PANGRAM: "+inp)
    else:
        print("NEITHER: "+inp)