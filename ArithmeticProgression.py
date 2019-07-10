

def ap(ar):
    diff1 = 0
    nextInt = 0
    diff = ar[1] - ar[0]
    for i in range(len(ar)-1):
        diff1 = ar[i+1] - ar[i]
        if diff1 > diff:
            nextInt = ar[i] + diff
        elif diff1 < diff:
            nextInt = ar[0] + diff1
    print("THE MISSING NUMBER IS :" + str(nextInt))


ap([1, 5, 7, 9, 11])
ap([2,6,10,14,20])
ap([2,10,14,16,20,24])
