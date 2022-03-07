import sys

curkey = None
curval = None
counter = 0
total = 0

for line in sys.stdin:
        key, val = line.split("\t")

        if key == curkey:
                if val != curval:
                        counter+=1
        else:
                if curkey is not None:
                        print(counter, "\t", "1")
                        #print("1", "\t", counter)
                curkey = key
                curval = val
                counter = 1
print(counter, "\t", "1")
#print("1", "\t", counter)