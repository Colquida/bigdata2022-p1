import sys

counter = 0
llave_actual = None
val_actual = None

for line in sys.stdin:
        key, val = line.split("\t")

        if key == llave_actual:

                #print(val, val_actual)
                if val != val_actual:
                        counter+=1
        else:
                if llave_actual is not None:
                        print(counter,"\t", "1")
                        #print(counter, "\t", llave_actual)
                counter = 1
        llave_actual = key
        val_actual = val
print(counter, "\t", "1")
#print(counter, "\t", llave_actual)