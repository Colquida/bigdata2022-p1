import sys

input = sys.stdin
next(input)

for line in input:
        if not line:
                break
        price = line.split(",")[1]
        town = line.split(",")[6]
        print(town, '\t', price)