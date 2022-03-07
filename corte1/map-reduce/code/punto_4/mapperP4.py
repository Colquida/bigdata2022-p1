
import sys

input = sys.stdin
next(input)

for line in input:
        if not line:
                break

        date = line.split(",")[2]
        year = date.split("-")[0]
        price = line.split(",")[1]
        town = line.split(",")[6]

        if year == "2015" and town == "STAMFORD":
                print(town, "\t", '%010d'%int(price))