def minimumSwaps(array):
    swaps = 0
    for x in range(0,n):
        while array[x] != x+1:
            temp = array[x] - 1
            array[x], array[temp] = array[temp], array[x]
            swaps +=1
    return swaps