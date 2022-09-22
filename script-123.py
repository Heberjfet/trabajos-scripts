valores = []
numPrimos = []
for val in range(2, 101):
    for a in range(2, val):
        i = val % a
        while i >= 0:
            i = val % a
            if not val in numPrimos:
                numPrimos.append(val)
    print(numPrimos)
