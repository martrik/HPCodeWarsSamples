import sys

max = 0

def isPrime(x):
    prime = True

    for i in range(int(x/2)):
        if i>1:
            if x%(i) == 0:
                prime = False
        else:
            prime = False

    return prime

def findDivisors(num):
    array = []
    for k in range(int(num/2)+1):
        print(isPrime(k))
        if isPrime(k) and k>1:
            if num%k == 0:
                max = k
                array.append(k)

    x = num
    alldivdic = {}

    for j in array:
        alldivarray = []
        while x%j == 0:
            x = x/j
            alldivarray.append(j)

        alldivdic[j] = alldivarray

    return alldivdic

def matchDics(dic1, dic2, max):
    finaldic = {}
    for i in range(max):
        if isPrime(i):
            if i in dic1 and i in dic2:
                if len(dic1[i]) < len(dic2[i]):
                    finaldic[i] = dic1[i]
                else:
                    finaldic[i] = dic2[i]

    return finaldic

def matchAndExtra(dic1, dic2, max):
    finaldic = {}
    for i in range(max):
        if isPrime(i):
            if i in dic1 and i in dic2:
                if len(dic1[i]) >= len(dic2[i]):
                    finaldic[i] = dic1[i]
                else:
                    finaldic[i] = dic2[i]

    return finaldic

def dicToarray(dic):
    array = []
    for i in dic:
        for j in i:
            array.append(j)
    return array

def multiplyArray(arr):
    multiplicitat = 1
    for i in arr:
        multiplicitat *= i

    return multiplicitat

for linen in sys.stdin:
    line = int(linen.strip("\n"))

    if line == 0:
        break

    print(findDivisors(line))
