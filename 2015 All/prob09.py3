import sys
import codecs

result = ""

for linen in sys.stdin:
    line = codecs.decode(linen.rstrip("\n").upper(), encoding="utf-8", errors="ignore")

    result += line[0]

print(result)