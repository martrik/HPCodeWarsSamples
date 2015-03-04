abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

negations = ["DON'T", "CAN'T", "ISN'T", "HAVEN'T", "CANNOT", "WOULDN'T", "COULDN'T", "WON'T", "NO",
             "NOT", "NEVER", "NOBODY", "NOWHERE", "NEITHER", "AIN'T"]

while True:
    inp = input()

    if inp == ".":
        break

    count = 0
    for i in negations:
        index = 0

        while True:
            index = inp.find(i, index+1)

            if index == -1:
                break

            if abc.count(inp[index-1]) == 0 and abc.count(inp[index+i.__len__()]) == 0:
                count += 1

    print(str(count)+": "+inp)
