import sys

curkey = None
total = 0

for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)

        if key == curkey:
                total += val
        else:
                if curkey is not None:
                        print(total, "\t", curkey)
                curkey = key
                total = val
print(total, "\t", curkey)