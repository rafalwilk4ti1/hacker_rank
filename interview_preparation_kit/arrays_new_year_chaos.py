def minimumBribes(array):
    moves = 0
    array = [p - 1 for p in array]
    for x,y in enumerate(array):
        if y - x > 2:
            print('Too chaotic')
            return
        for z in range(max(y-1,0),x):
            if array[z] > y:
                moves +=1
    print(moves)