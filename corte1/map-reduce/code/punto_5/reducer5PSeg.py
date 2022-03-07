import sys

curkey = None
curkey_month = None
maximum_sales = 0
maximum_month = 0
maximum_year = 0

for line in sys.stdin:
	key_year, key_month, val = line.split("\t")
	val = int(val)
	
	if key_year == curkey:
		if val > maximum_sales:
			maximum_sales = val
			maximum_month = key_month
	else:
		if curkey is not None:
			print(curkey, "\t", maximum_month)
		maximum_month = key_month
		curkey = key_year
		maximum_sales = val
print(curkey, "\t", maximum_month)