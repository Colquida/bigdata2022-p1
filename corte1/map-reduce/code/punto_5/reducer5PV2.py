import sys
curkey = None
curkey_year = None
total = 0

for line in sys.stdin:
	key_year, key_month, val = line.split("\t")
	val = int(val)
	print(key_year, "\t", key_month)
