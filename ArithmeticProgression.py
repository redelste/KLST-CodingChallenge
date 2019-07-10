#  Assumptions: 
#   - The input array is of length 5.
#   - The contents of the array is comprised of integers
#  Complexity:
#   - The complexity of this is O(n). The usage of if-statements
#   - provides a negligible amount of computation time hense O(n)
    

def ap(ar):
    # Diff1: A variable to store the difference between the 
    #        elements in the array.
    diff1 = 0
    # NextInt: A variable that is calculated once the differences between numbers
    #          has been calculated. This is the missing number or "next int".
    nextInt = 0
    # diff: A variable in which we check the difference between the first and second element.
    #       This creates a reference value to see what the arithmetic progression is.
    diff = ar[1] - ar[0]
    # Here we iterate through the input array
    for i in range(len(ar)-1):
        # Here is when the calculation for diff1 is made. 
        diff1 = ar[i+1] - ar[i]
        # check to see if the difference between the first and second number is less than the difference
        # between the other numbers.
        if diff1 > diff:
            # if it is, we add the lower number to the value as we know the values between arithmetic progressions is always constant.
            nextInt = ar[i] + diff
        elif diff1 < diff:
            nextInt = ar[0] + diff1
    print("THE MISSING NUMBER IS :" + str(nextInt))

