import sys

for line in sys.stdin:
        county = line.split(",")[8]
        town = line.split(",")[6]
        print(county, "\t", town)