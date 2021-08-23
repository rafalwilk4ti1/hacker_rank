def countingValleys(steps, path):
    valley = 0
    level = 0
    for x in path:
        if x == 'U':
            level +=1
            if level == 0:
                valley +=1
        else:
            level -=1
    return valley