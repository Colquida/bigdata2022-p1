import sys

for line in sys.stdin:
	date = line.split(",")[2]
	month = date.split("-")[1]
	year = date.split("-")[0]
	print(year, "\t", month, "\t", "1")