

tup = (1, 1, 0, -1, -1)

def plusMinus(arr):
    minus, plus, zero = 0, 0, 0
    for elem in arr:
        if elem > 0:
            plus += 1
        elif elem < 0:
            minus += 1
        else:
            zero +=1
    print(plus/len(arr))
    print(minus/len(arr))
    print(zero/len(arr))

print(plusMinus(tup))