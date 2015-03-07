import sys

for line in sys.stdin:
    x = int(line)

    if x == 0:
        break

    prime = True

    for i in range(int(x/2)):
        if i>1:
            if x%(i) == 0:
                prime = False

    if prime:
        print(str(x)+" is prime")
    else:
        print(str(x)+" is not prime")