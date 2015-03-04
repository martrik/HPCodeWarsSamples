import sys

for line in sys.stdin:
    name, earth_weight, planet, conversion = line.split()
    if(name == "END"):
        break
    weight = float(earth_weight)*float(conversion)
    print("On "+planet+", "+name+" would weight "+str(weight)+" pounds.")
