segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def calculate_power(input):
    power = 0
    for i in input:
        if not i == ":":
            power += segments[int(i)]*15
        else:
            power += 20
    return power

inp = int(input())

for i in range(inp):
    hour = input()
    print(str(calculate_power(hour))+" milliamps")