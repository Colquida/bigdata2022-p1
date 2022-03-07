import sys

curkey = None
total = 0
counter = 0
for line in sys.stdin:
        key,val = line.split("\t")
        val = int(val)

        if key == curkey:
                total += val
                counter +=1


        else:
                if curkey is not None:
                        print(curkey, "\t", total/counter)
                curkey = key
                total = val
                counter=1
print(curkey, "\t", total/counter)