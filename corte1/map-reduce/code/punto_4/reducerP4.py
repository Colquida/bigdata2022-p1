import sys

for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)

        print(key, "\t", val)