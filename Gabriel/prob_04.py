real_number = int(input())
numbers = []
names = []

def find_closer():
    diferences = []
    closers = []
    global numbers
    global real_number
    for i in numbers:
        diference = real_number - i
        if diference < 0:
            diferences.append(-diference)
        else:
            diferences.append(diference)

    minimum = min(diferences)
    for i in range(diferences.__len__()):
        if(diferences[i] == minimum):
            closers.append(i)
    return closers

inp = int(input())

for i in range(inp):
    aposta = input()
    space = aposta.find(" ")
    number = int(aposta[:space])
    name = aposta[space+1:]
    numbers.append(number)
    names.append(name)

to_print = ""
for i in find_closer():
    to_print += names[i]+" "

print(to_print[:to_print.__len__()-1])

