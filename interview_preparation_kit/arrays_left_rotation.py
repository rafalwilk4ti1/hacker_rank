def rotLeft(a, d):
    for x in range(d):
        deleted = a[0]
        a.append(deleted)
        a.pop(0)
    return a