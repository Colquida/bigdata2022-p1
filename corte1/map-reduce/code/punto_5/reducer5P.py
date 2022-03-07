import sys

curkey = None
curkey_year = None
total = 0

for line in sys.stdin:
	key_year, key_month, val = line.split("\t")
	val = int(val)

	if key_month == curkey and key_year == curkey_year:
		total += val
	else:
		if (curkey and curkey_year) is not None:
			print(curkey_year, "\t", curkey, "\t", total)
		curkey = key_month
		curkey_year = key_year
		total = val
print(curkey_year, "\t", curkey, "\t", total)