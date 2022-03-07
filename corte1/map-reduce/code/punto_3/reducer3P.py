import sys

curkey = None
minimum_price = 0

for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)

        if key == curkey:
                if val < minimum_price:
                        minimum_price = val
        else:
                if curkey is not None:
                        print(curkey, "\t", minimum_price) #aqui va el minimo

                minimum_price = val
                curkey = key

print(curkey, "\t", minimum_price)