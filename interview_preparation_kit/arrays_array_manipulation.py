def arrayManipulation(n, queries):
    list_zeros = [0] * (n+1)
    for query in queries:
        a = query[0] - 1
        b = query[1]
        k = query[2]
        list_zeros[a] += k
        list_zeros[b] -=k
    max_value = 0
    running_count = 0
    for x in list_zeros:
        running_count +=x
        if running_count > max_value:
            max_value = running_count
    return max_value