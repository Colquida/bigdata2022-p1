
import sys

for line in sys.stdin:
        town = line.split(",")[6]
        county = line.split(",")[8]
        print(county, '\t', town)