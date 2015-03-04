inp = int(input())

symbols = ["I", "P", "D", "H", "C", "M"]
values = {"I":1, "P":5, "D":10, "H":100, "C":1000, "M":10000}

for i in range(inp):
    number_to_convert = input()
    isGreek = False
    isMoreThanTen = False

    for i in symbols:
        if not number_to_convert.count(i) == 0:
            isGreek = True

    if isGreek:
        for i in symbols:
            if not i == "P" and not i == "I":
                if not number_to_convert.count(i) == 0:
                    isMoreThanTen = True

        if isMoreThanTen:
            count = number_to_convert.count("P")
            index = 0
            for i in range(count):
                index = number_to_convert.index("P", index + 1)
                number_to_convert.insert(number_to_convert[index+1]*5, index)

        value = 0
        for i in number_to_convert:
            value += values[i]

    #else: convert to ancient