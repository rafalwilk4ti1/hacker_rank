def twoStrings(s1, s2):
    decision = 'NO'
    for x in s1:
        if x in s2:
            decision = 'YES'

    return decision