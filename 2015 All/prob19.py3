import sys

number = int(sys.stdin.readline().strip("\n"))
gens = []

for i in range(number):
    gen = sys.stdin.readline().strip("\n")

    gens.append(gen)

dna = sys.stdin.readline().strip("\n")

for gen in gens:
    match = False
    count = 0
    for dnaletter in dna:
        if gen[0] == dnaletter:
            index = 0
            mutations = 0

            for genletter in dna[count:len(gen)+count]:
                if not genletter == gen[index]:
                    mutations += 1

                index += 1

            if mutations <= 1 and match == False:
                print(str(count+1)+" "+str(mutations))
                match = True

        count += 1

    if not match:
        print("0")